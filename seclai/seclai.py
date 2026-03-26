"""Seclai Python SDK.

This package provides two primary clients:

- `Seclai`: synchronous client (uses `httpx.Client`)
- `AsyncSeclai`: asynchronous client (uses `httpx.AsyncClient`)

Authentication
--------------
Pass `api_key=...` when constructing a client, or set `SECLAI_API_KEY`.

Configuration
-------------
Set `SECLAI_API_URL` to override the API base URL.

Errors
------
Convenience endpoint methods raise SDK exceptions instead of returning “error models”:

- `SeclaiAPIStatusError`: non-success HTTP status codes
- `SeclaiAPIValidationError`: validation error payloads (typically HTTP 422)

Quickstart
----------
Sync:

    from seclai import Seclai

    client = Seclai(api_key="...")
    run = client.run_agent("agent_123", body=...)

Async:

    from seclai import AsyncSeclai

    async with AsyncSeclai(api_key="...") as client:
        run = await client.run_agent("agent_123", body=...)
"""

import logging
import mimetypes
import os
import time
from collections.abc import AsyncGenerator, Generator, Mapping
from dataclasses import dataclass
from http import HTTPStatus
from io import BytesIO
from pathlib import Path
from typing import Any, Awaitable, BinaryIO, Callable, Self, TypedDict, cast, overload

import httpx

from seclai._generated.client import Client as GeneratedClient
from seclai._generated.models.agent_run_list_response import AgentRunListResponse
from seclai._generated.models.agent_run_request import AgentRunRequest
from seclai._generated.models.agent_run_response import AgentRunResponse
from seclai._generated.models.content_detail_response import ContentDetailResponse
from seclai._generated.models.content_embeddings_list_response import (
    ContentEmbeddingsListResponse,
)
from seclai._generated.models.file_upload_response import FileUploadResponse
from seclai._generated.models.http_validation_error import HTTPValidationError
from seclai._generated.models.source_list_response import SourceListResponse
from seclai._generated.types import Response as OpenAPIResponse
from seclai.auth import (
    AuthState,
    resolve_auth_headers_async,
    resolve_auth_headers_sync,
    resolve_credential_chain,
)

logger = logging.getLogger(__name__)


#: Recursive type alias for JSON-serializable values.
#: Used as the return type for methods that return raw JSON payloads.
JSONValue = dict[str, "JSONValue"] | list["JSONValue"] | str | int | float | bool | None


class AgentRunStreamRequest(TypedDict):
    """Request body for streaming agent runs.

    This matches the API schema for POST /agents/{agent_id}/runs/stream.
    """

    input: str | None
    metadata: dict[str, JSONValue]


#: Default API base URL. Override via the ``SECLAI_API_URL`` environment variable.
SECLAI_API_URL = os.getenv("SECLAI_API_URL", "https://seclai.com")


def _strip_none(params: dict[str, Any]) -> dict[str, Any]:
    """Remove keys with ``None`` values from a parameter dictionary."""
    return {k: v for k, v in params.items() if v is not None}


class SeclaiError(Exception):
    """Base error for the Seclai SDK."""


class SeclaiConfigurationError(SeclaiError):
    """Raised when the client is misconfigured (e.g., missing API key)."""


class SeclaiAPIStatusError(SeclaiError):
    """Raised when the Seclai API returns a non-success status code.

    Attributes:
        status_code: HTTP status code returned by the API.
        method: HTTP method used for the request.
        url: Full request URL.
        response_text: Best-effort response body text, if available.
    """

    def __init__(
        self,
        *,
        message: str,
        status_code: int,
        method: str,
        url: str,
        response_text: str | None,
    ) -> None:
        """Create a status error for a non-2xx API response."""
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.method = method
        self.url = url
        self.response_text = response_text


class SeclaiAPIValidationError(SeclaiAPIStatusError):
    """Raised when the API returns a validation error response (typically HTTP 422).

    Attributes:
        validation_error: Parsed validation details returned by the API.
    """

    def __init__(
        self,
        *,
        message: str,
        status_code: int,
        method: str,
        url: str,
        response_text: str | None,
        validation_error: HTTPValidationError,
    ) -> None:
        """Initialize with validation error details."""
        super().__init__(
            message=message,
            status_code=status_code,
            method=method,
            url=url,
            response_text=response_text,
        )
        self.validation_error = validation_error


class SeclaiStreamingError(SeclaiError):
    """Raised when an error event is received during a streaming agent run.

    Attributes:
        message: Human-readable error message from the stream.
        run_id: Agent run identifier, if available.
    """

    def __init__(self, message: str, *, run_id: str | None = None) -> None:
        """Initialize with stream error message and optional run ID."""
        super().__init__(message)
        self.message = message
        self.run_id = run_id


def _guess_mime_type(file_name: str | None) -> str | None:
    """Guess the MIME type from a filename, or return ``None``."""
    if not file_name:
        return None
    guessed, _ = mimetypes.guess_type(file_name)
    return guessed


def _resolve_api_key(api_key: str | None) -> str:
    """Resolve the API key from an explicit value or `SECLAI_API_KEY`.

    Raises:
        SeclaiConfigurationError: If no API key is provided or present in the environment.
    """
    resolved = (api_key or os.getenv("SECLAI_API_KEY") or "").strip()
    if not resolved:
        raise SeclaiConfigurationError(
            "Missing API key. Pass api_key=... or set SECLAI_API_KEY."
        )
    return resolved


@dataclass(frozen=True, slots=True)
class ClientOptions:
    """Resolved client configuration options.

    All values are resolved at construction time and immutable thereafter.

    Attributes:
        auth_state: Resolved authentication state.
        timeout: Request timeout in seconds.
        api_key_header: HTTP header name used to transmit the API key.
        default_headers: Extra headers included on every request.
    """

    auth_state: AuthState
    timeout: float
    api_key_header: str
    default_headers: Mapping[str, str]


def _build_default_headers(
    *,
    auth_state: AuthState,
    default_headers: Mapping[str, str] | None,
) -> dict[str, str]:
    """Build default request headers including auth and user-agent."""
    headers: dict[str, str] = {
        "user-agent": "seclai-python",
    }
    # Add static auth headers (for api_key and bearer_static modes).
    # Dynamic modes (bearer_provider, sso) are resolved per-request.
    if auth_state.mode == "api_key":
        headers[auth_state.api_key_header] = auth_state.api_key  # type: ignore[assignment]
    elif auth_state.mode == "bearer_static":
        headers["authorization"] = f"Bearer {auth_state.access_token}"
    if auth_state.account_id:
        headers["x-account-id"] = auth_state.account_id
    if default_headers:
        headers.update(default_headers)
    return headers


def _merge_request_headers(
    *,
    options: ClientOptions,
    request_headers: Mapping[str, str] | None,
) -> dict[str, str]:
    """Merge client default headers with per-request overrides including dynamic auth."""
    merged = _build_default_headers(
        auth_state=options.auth_state,
        default_headers=options.default_headers,
    )
    # For dynamic auth modes, resolve per-request headers
    if options.auth_state.mode in ("bearer_provider", "sso"):
        auth_headers = resolve_auth_headers_sync(options.auth_state)
        merged.update(auth_headers)
    if request_headers:
        merged.update(request_headers)
    return merged


async def _merge_request_headers_async(
    *,
    options: ClientOptions,
    request_headers: Mapping[str, str] | None,
) -> dict[str, str]:
    """Merge client default headers with per-request overrides including dynamic auth (async)."""
    merged = _build_default_headers(
        auth_state=options.auth_state,
        default_headers=options.default_headers,
    )
    # For dynamic auth modes, resolve per-request headers asynchronously
    if options.auth_state.mode in ("bearer_provider", "sso"):
        auth_headers = await resolve_auth_headers_async(options.auth_state)
        merged.update(auth_headers)
    if request_headers:
        merged.update(request_headers)
    return merged


def _raise_for_status(response: httpx.Response) -> None:
    """Raise `SeclaiAPIStatusError` when the response status is not successful."""
    if 200 <= response.status_code < 400:
        return
    try:
        response_text = response.text
    except Exception:
        response_text = None
    raise SeclaiAPIStatusError(
        message=f"Request failed with status {response.status_code}",
        status_code=response.status_code,
        method=response.request.method,
        url=str(response.request.url),
        response_text=response_text,
    )


class _SeclaiBase:
    """Shared implementation for Seclai sync/async clients.

    This class centralizes credential resolution, option storage, and configuration of
    the generated OpenAPI client.
    """

    def __init__(
        self,
        *,
        api_key: str | None,
        access_token: str | Callable[[], str | Awaitable[str]] | None,
        timeout: float,
        api_key_header: str,
        default_headers: Mapping[str, str] | None,
        profile: str | None,
        config_dir: str | None,
        auto_refresh: bool,
        account_id: str | None,
    ) -> None:
        """Initialize shared client state.

        Args:
            api_key: API key used for authentication. If omitted, ``SECLAI_API_KEY`` is used.
            access_token: Static bearer token string or a provider callable.
                Mutually exclusive with ``api_key``.
            timeout: Request timeout (seconds).
            api_key_header: Header name to use for the API key.
            default_headers: Extra headers to include on every request.
            profile: SSO profile name from ``~/.seclai/config``.
            config_dir: Override the config directory path.
            auto_refresh: Whether to auto-refresh expired SSO tokens. Defaults to ``True``.
            account_id: Target organization account ID (``X-Account-Id`` header).

        Raises:
            SeclaiConfigurationError: If no credentials are found or if both ``api_key``
                and ``access_token`` are provided.
        """
        if api_key and access_token:
            raise SeclaiConfigurationError(
                "Provide either api_key or access_token, not both."
            )

        # Determine access_token vs provider
        access_token_str: str | None = None
        access_token_provider: Callable[[], str | Awaitable[str]] | None = None
        if callable(access_token):
            access_token_provider = access_token
        elif isinstance(access_token, str):
            access_token_str = access_token

        try:
            auth_state = resolve_credential_chain(
                api_key=api_key,
                access_token=access_token_str,
                access_token_provider=access_token_provider,
                profile=profile,
                config_dir=config_dir,
                auto_refresh=auto_refresh,
                account_id=account_id,
                api_key_header=api_key_header,
            )
        except RuntimeError as e:
            raise SeclaiConfigurationError(str(e)) from e

        self._options = ClientOptions(
            auth_state=auth_state,
            timeout=timeout,
            api_key_header=api_key_header,
            default_headers=default_headers or {},
        )

        self._generated_client_instance: GeneratedClient | None = None
        self._owns_generated_client = False

    @property
    def api_key(self) -> str | None:
        """Return the resolved API key used for authentication, or ``None`` for bearer auth."""
        return self._options.auth_state.api_key

    def _default_headers(self) -> dict[str, str]:
        """Build default request headers for the underlying HTTP clients.

        Returns:
            A header dictionary containing auth, user-agent, and any configured defaults.
        """
        return _build_default_headers(
            auth_state=self._options.auth_state,
            default_headers=self._options.default_headers,
        )

    def _generated_client(self) -> GeneratedClient:
        """Return a cached generated OpenAPI client configured with this client's auth.

        This is primarily used internally by the wrapper methods in this file. Advanced
        usage may call this to access generated request helpers.
        """
        if self._generated_client_instance is None:
            self._generated_client_instance = GeneratedClient(
                base_url=SECLAI_API_URL,
                headers=self._default_headers(),
            )
            self._owns_generated_client = True
        return self._generated_client_instance

    def _build_url(self, path: str) -> str:
        """Build an absolute URL string from a request path.

        Args:
            path: API path (with or without a leading `/`).

        Returns:
            Absolute URL combining the configured base URL and the given path.
        """
        base = SECLAI_API_URL.rstrip("/")
        rel = path if path.startswith("/") else f"/{path}"
        return f"{base}{rel}"

    def _raise_for_openapi_response(
        self,
        *,
        method: str,
        path: str,
        response: OpenAPIResponse[Any],
        ok_statuses: set[HTTPStatus],
    ) -> None:
        """Raise an SDK exception if an OpenAPI response is not an expected success.

        Args:
            method: HTTP method used (e.g. `"GET"`).
            path: API path used (e.g. `"/sources/"`).
            response: The generated client's detailed response object.
            ok_statuses: Acceptable HTTP status codes for this operation.

        Raises:
            SeclaiAPIValidationError: If the API returned a validation error payload.
            SeclaiAPIStatusError: For any other non-success status.
        """
        if response.status_code in ok_statuses:
            return

        response_text: str | None
        try:
            response_text = response.content.decode("utf-8")
        except Exception:
            response_text = None

        if isinstance(response.parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message=f"Request failed with status {int(response.status_code)}",
                status_code=int(response.status_code),
                method=method,
                url=self._build_url(path),
                response_text=response_text,
                validation_error=response.parsed,
            )

        raise SeclaiAPIStatusError(
            message=f"Request failed with status {int(response.status_code)}",
            status_code=int(response.status_code),
            method=method,
            url=self._build_url(path),
            response_text=response_text,
        )


class Seclai(_SeclaiBase):
    """Seclai synchronous client.

    Most users should prefer the typed convenience methods (e.g. `run_agent`, `list_sources`)
    which raise SDK exceptions on failures.

    This client can be used as a context manager:

        with Seclai(api_key="...") as client:
            sources = client.list_sources()
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        access_token: str | Callable[[], str] | None = None,
        timeout: float = 30.0,
        api_key_header: str = "x-api-key",
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.Client | None = None,
        profile: str | None = None,
        config_dir: str | None = None,
        auto_refresh: bool = True,
        account_id: str | None = None,
    ) -> None:
        """Create a synchronous Seclai client.

        Credentials are resolved via a chain (first match wins):

        1. Explicit ``api_key``
        2. Explicit ``access_token`` (static string or provider callable)
        3. ``SECLAI_API_KEY`` environment variable
        4. SSO profile from ``~/.seclai/config`` + cached tokens

        Args:
            api_key: API key used for authentication. If omitted, ``SECLAI_API_KEY`` is used.
            access_token: Static bearer token string or a callable returning one.
                Mutually exclusive with ``api_key``.
            timeout: Request timeout (seconds).
            api_key_header: Header name to use for the API key.
            default_headers: Extra headers to include on every request.
            http_client: Optional pre-configured ``httpx.Client`` to use.
            profile: SSO profile name from ``~/.seclai/config``.
            config_dir: Override the config directory path.
            auto_refresh: Auto-refresh expired SSO tokens. Defaults to ``True``.
            account_id: Target organization account ID (``X-Account-Id`` header).

        Raises:
            SeclaiConfigurationError: If no credentials are found.
        """
        super().__init__(
            api_key=api_key,
            access_token=access_token,
            timeout=timeout,
            api_key_header=api_key_header,
            default_headers=default_headers,
            profile=profile,
            config_dir=config_dir,
            auto_refresh=auto_refresh,
            account_id=account_id,
        )
        self._client = http_client or httpx.Client(
            base_url=SECLAI_API_URL,
            timeout=self._options.timeout,
            headers=self._default_headers(),
        )
        self._owns_client = http_client is None

    def close(self) -> None:
        """Close underlying HTTP resources owned by this client.

        If you created the client with a custom ``http_client``, this is a no-op
        for that client (you remain responsible for closing it).
        """
        if self._owns_client:
            self._client.close()
        if self._owns_generated_client and self._generated_client_instance is not None:
            self._generated_client_instance.get_httpx_client().close()

    def __enter__(self) -> Self:
        """Enter a context manager and return self."""
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        """Exit the context manager and close resources.

        Args:
            exc_type: Exception type (if any).
            exc: Exception instance (if any).
            tb: Traceback (if any).
        """
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: JSONValue | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> JSONValue | str | None:
        """Make a raw HTTP request to the Seclai API.

        This is a low-level escape hatch. For most operations, prefer the typed
        convenience methods on this client.

        Args:
            method: HTTP method (e.g. `"GET"`, `"POST"`).
            path: Request path relative to `SECLAI_API_URL` (e.g. `"/sources/"`).
            params: Query parameters.
            json: JSON body to send.
            headers: Per-request header overrides.

        Returns:
            Parsed JSON for JSON responses, raw text for non-JSON responses, or `None` for empty bodies.

        Raises:
            SeclaiAPIStatusError: If the response status code is not successful.
        """
        response = self._client.request(
            method,
            path,
            params=params,
            json=json,
            headers=_merge_request_headers(
                options=self._options, request_headers=headers
            ),
        )
        _raise_for_status(response)
        if not response.content:
            return None
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            return cast(JSONValue, response.json())
        return response.text

    def run_agent(self, agent_id: str, body: AgentRunRequest) -> AgentRunResponse:
        """Run an agent.

        Starts a new agent run for the given agent and returns the run record. You'll need the agent run ID to track the run's progress and fetch the result of completed runs.

        Args:
            agent_id: Agent identifier.
            body: Agent run request payload.

        Returns:
            The created agent run.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.run_agent_api_agents_agent_id_runs_post import (
            sync_detailed,
        )

        path = f"/agents/{agent_id}/runs"
        response = sync_detailed(
            agent_id=agent_id, client=self._generated_client(), body=body
        )
        self._raise_for_openapi_response(
            method="POST",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="POST",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="POST",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    def run_streaming_agent_and_wait(
        self,
        agent_id: str,
        body: AgentRunStreamRequest,
        *,
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> AgentRunResponse:
        """Run an agent via SSE streaming and block until completion.

        This uses POST /agents/{agent_id}/runs/stream and consumes Server-Sent Events (SSE).
        The method returns when an `event: done` message is received.

        Args:
            agent_id: Agent identifier.
            body: Streaming agent run request payload.
            timeout: Max time (seconds) to wait for the final result (client-side). Defaults to this
                client's configured timeout.
            headers: Optional extra headers for this request.

        Returns:
            The final agent run payload from the `done` event.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
            SeclaiError: If the stream ends early or times out.
        """
        import json as _json
        import time as _time

        path = f"/agents/{agent_id}/runs/stream"

        merged_headers = _merge_request_headers(
            options=self._options, request_headers=headers
        )
        merged_headers.setdefault("accept", "text/event-stream")

        timeout_seconds = self._options.timeout if timeout is None else timeout
        start = _time.monotonic()

        try:
            with self._client.stream(
                "POST",
                path,
                json=body,
                headers=merged_headers,
                timeout=timeout_seconds,
            ) as response:
                if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                    payload = response.json()
                    raise SeclaiAPIValidationError(
                        message=f"Request failed with status {response.status_code}",
                        status_code=int(response.status_code),
                        method="POST",
                        url=self._build_url(path),
                        response_text=response.text,
                        validation_error=HTTPValidationError.from_dict(payload),
                    )
                _raise_for_status(response)

                current_event: str | None = None
                data_lines: list[str] = []
                last_seen: AgentRunResponse | None = None

                def dispatch() -> AgentRunResponse | None:
                    nonlocal current_event, data_lines, last_seen
                    if current_event is None and not data_lines:
                        return None
                    data = "\n".join(data_lines)
                    evt = current_event
                    current_event = None
                    data_lines = []
                    if not data:
                        return None
                    if evt not in {"init", "done"}:
                        return None
                    try:
                        parsed_dict = cast(dict[str, Any], _json.loads(data))
                        parsed = AgentRunResponse.from_dict(parsed_dict)
                        last_seen = parsed
                        if evt == "done":
                            return parsed
                    except Exception:
                        return None
                    return None

                for line in response.iter_lines():
                    if _time.monotonic() - start > timeout_seconds:
                        raise SeclaiError(
                            f"Timed out after {timeout_seconds}s waiting for streaming agent run to complete."
                        )

                    if line == "":
                        done = dispatch()
                        if done is not None:
                            return done
                        continue
                    if line.startswith(":"):
                        continue
                    if line.startswith("event:"):
                        current_event = line[len("event:") :].strip() or None
                        continue
                    if line.startswith("data:"):
                        data_lines.append(line[len("data:") :].lstrip())
                        continue

                done = dispatch()
                if done is not None:
                    return done
                if last_seen is not None:
                    return last_seen
                raise SeclaiError("Stream ended before receiving a 'done' event.")
        except httpx.TimeoutException as e:
            raise SeclaiError(
                f"Timed out after {timeout_seconds}s waiting for streaming agent run to complete."
            ) from e

    def list_agent_runs(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> AgentRunListResponse:
        """List agent runs.

        Returns paginated runs for a single agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            A paginated list of runs.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.list_agent_runs_api_agents_agent_id_runs_get import (
            sync_detailed,
        )

        path = f"/agents/{agent_id}/runs"
        response = sync_detailed(
            agent_id=agent_id,
            client=self._generated_client(),
            page=page,
            limit=limit,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    @overload
    def get_agent_run(
        self, run_id: str, /, *, include_step_outputs: bool = False
    ) -> AgentRunResponse: ...

    @overload
    def get_agent_run(
        self, agent_id: str, run_id: str, /, *, include_step_outputs: bool = False
    ) -> AgentRunResponse: ...

    def get_agent_run(
        self, *args: str, include_step_outputs: bool = False
    ) -> AgentRunResponse:
        """Get details of a specific agent run.

        Fetches the current state and details for a previously created run.

        Args:
            run_id: Run identifier.
            agent_id: Deprecated. Ignored if provided; maintained for backwards compatibility.
            include_step_outputs: If true, include per-step outputs with timing,
                durations, and credits. Defaults to False.

        Returns:
            Agent run details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        if len(args) == 1:
            run_id = args[0]
        elif len(args) == 2:
            # Backwards compatible: get_agent_run(agent_id, run_id)
            run_id = args[1]
        else:
            raise TypeError("get_agent_run expects (run_id) or (agent_id, run_id)")

        from seclai._generated.api.agents.get_agent_run_api_agents_runs_run_id_get import (
            sync_detailed,
        )

        path = f"/agents/runs/{run_id}"
        response = sync_detailed(
            run_id=run_id,
            client=self._generated_client(),
            include_step_outputs=include_step_outputs,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    @overload
    def delete_agent_run(self, run_id: str, /) -> AgentRunResponse: ...

    @overload
    def delete_agent_run(self, agent_id: str, run_id: str, /) -> AgentRunResponse: ...

    def delete_agent_run(self, *args: str) -> AgentRunResponse:
        """Cancel an agent run.

        Requests cancellation of a run and returns the updated run record. Note: cancellation will not stop the currently executing step, but will prevent any further steps from running.

        Args:
            run_id: Run identifier.
            agent_id: Deprecated. Ignored if provided; maintained for backwards compatibility.

        Returns:
            The updated agent run.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        if len(args) == 1:
            run_id = args[0]
        elif len(args) == 2:
            # Backwards compatible: delete_agent_run(agent_id, run_id)
            run_id = args[1]
        else:
            raise TypeError("delete_agent_run expects (run_id) or (agent_id, run_id)")

        from seclai._generated.api.agents.delete_agent_run_api_agents_runs_run_id_delete import (
            sync_detailed,
        )

        path = f"/agents/runs/{run_id}"
        response = sync_detailed(run_id=run_id, client=self._generated_client())
        self._raise_for_openapi_response(
            method="DELETE",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="DELETE",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="DELETE",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    def get_content_detail(
        self,
        source_connection_content_version: str,
        *,
        start: int = 0,
        end: int = 5000,
    ) -> ContentDetailResponse:
        """Get content detail.

        Fetches a slice of a content version (use `start`/`end` to page through large content).

        Args:
            source_connection_content_version: Content version identifier.
            start: Start offset for returned content detail.
            end: End offset for returned content detail.

        Returns:
            Content details for the requested range.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.contents.get_content_detail_api_contents_source_connection_content_version_get import (
            sync_detailed,
        )

        path = f"/contents/{source_connection_content_version}"
        response = sync_detailed(
            source_connection_content_version=source_connection_content_version,
            client=self._generated_client(),
            start=start,
            end=end,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    def delete_content(self, source_connection_content_version: str) -> None:
        """Delete a specific content version.

        Permanently removes a content version identified by `source_connection_content_version`.

        Args:
            source_connection_content_version: Content version identifier.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.contents.delete_content_api_contents_source_connection_content_version_delete import (
            sync_detailed,
        )

        path = f"/contents/{source_connection_content_version}"
        response = sync_detailed(
            source_connection_content_version=source_connection_content_version,
            client=self._generated_client(),
        )
        self._raise_for_openapi_response(
            method="DELETE",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.NO_CONTENT},
        )
        return None

    def list_content_embeddings(
        self,
        source_connection_content_version: str,
        *,
        page: int = 1,
        limit: int = 20,
    ) -> ContentEmbeddingsListResponse:
        """List embeddings for a content version.

        Returns paginated embeddings that were computed for the given content version.

        Args:
            source_connection_content_version: Content version identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            A paginated list of embeddings.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.contents.list_content_embeddings_api_contents_source_connection_content_version_embeddings_get import (
            sync_detailed,
        )

        path = f"/contents/{source_connection_content_version}/embeddings"
        response = sync_detailed(
            source_connection_content_version=source_connection_content_version,
            client=self._generated_client(),
            page=page,
            limit=limit,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    def list_sources(
        self,
        *,
        page: int = 1,
        limit: int = 20,
        sort: str = "created_at",
        order: str = "desc",
        account_id: str | None = None,
    ) -> SourceListResponse:
        """List sources.

        Returns the sources visible to your account (optionally filtered by `account_id`).

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (e.g. `"asc"` or `"desc"`).
            account_id: Optional account id; defaults to the API key's account.

        Returns:
            A paginated list of sources.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.sources.list_sources_api_sources_get import (
            sync_detailed,
        )

        path = "/sources/"
        response = sync_detailed(
            client=self._generated_client(),
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            account_id=account_id,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    def upload_file_to_source(
        self,
        source_connection_id: str,
        *,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        title: str | None = None,
        metadata: Mapping[str, Any] | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> FileUploadResponse:
        """Upload a file to a specific source connection.

        Sends a file to be ingested under the given source connection.

        Maximum file size: 200 MiB.

        Supported MIME types:
            - `application/epub+zip`
            - `application/json`
            - `application/msword`
            - `application/pdf`
            - `application/vnd.ms-excel`
            - `application/vnd.ms-outlook`
            - `application/vnd.ms-powerpoint`
            - `application/vnd.openxmlformats-officedocument.presentationml.presentation`
            - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
            - `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
            - `application/xml`
            - `application/zip`
            - `audio/flac`
            - `audio/mp4`
            - `audio/mpeg`
            - `audio/ogg`
            - `audio/wav`
            - `image/bmp`
            - `image/gif`
            - `image/jpeg`
            - `image/png`
            - `image/tiff`
            - `image/webp`
            - `text/csv`
            - `text/html`
            - `text/markdown` / `text/x-markdown`
            - `text/plain`
            - `text/xml`
            - `video/mp4`
            - `video/quicktime`
            - `video/x-msvideo`

        If `mime_type` is omitted and a filename is available, the SDK tries to infer it.
        If the upload is sent as `application/octet-stream`, the server attempts to infer
        the type from the file extension.

        Notes:
            - If `file` is a path or `bytes`, this method creates an in-memory/file handle and
              closes it before returning.
            - If `file` is a file-like object, the caller owns its lifecycle.

        Args:
            source_connection_id: Source connection identifier.
            file: File payload. Accepts raw bytes, a filesystem path, or a binary file-like.
            title: Optional title for the uploaded file.
            metadata: Optional metadata dictionary to associate with the uploaded content.
            file_name: Optional filename to send when `file` is bytes or a file-like.
            mime_type: Optional MIME type to send.

        Returns:
            Upload response details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        import json as _json

        from seclai._generated.models.body_upload_file_to_source_api_sources_source_connection_id_upload_post import (
            BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
        )
        from seclai._generated.types import UNSET, File

        created_payload: BinaryIO | None = None
        try:
            upload_file: File
            if isinstance(file, File):
                upload_file = file
            elif isinstance(file, (str, os.PathLike)):
                file_path = Path(file)
                resolved_file_name = file_name or file_path.name
                resolved_mime_type = mime_type or _guess_mime_type(resolved_file_name)
                created_payload = file_path.open("rb")
                upload_file = File(
                    payload=created_payload,
                    file_name=resolved_file_name,
                    mime_type=resolved_mime_type,
                )
            elif isinstance(file, bytes):
                created_payload = BytesIO(file)
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=created_payload,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )
            else:
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=file,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )

            body = BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost(
                file=upload_file,
                title=UNSET if title is None else title,
            )

            if metadata is not None:
                body["metadata"] = _json.dumps(metadata)

            endpoint_path = f"/sources/{source_connection_id}/upload"

            # Note: openapi-python-client currently struggles with Seclai's spec for this endpoint
            # due to duplicate schema names, so we send the multipart request directly and parse
            # into our SDK model types.
            http = self._generated_client().get_httpx_client()
            raw = http.request(
                "POST",
                endpoint_path,
                files=body.to_multipart(),
            )

            parsed: FileUploadResponse | HTTPValidationError | None = None
            if raw.status_code == 200:
                payload = cast(dict[str, Any], raw.json())
                parsed = FileUploadResponse.from_dict(payload)
            elif raw.status_code == 422:
                payload = cast(dict[str, Any], raw.json())
                parsed = HTTPValidationError.from_dict(payload)

            response = OpenAPIResponse(
                status_code=HTTPStatus(raw.status_code),
                content=raw.content,
                headers=raw.headers,
                parsed=parsed,
            )
            self._raise_for_openapi_response(
                method="POST",
                path=endpoint_path,
                response=response,
                ok_statuses={HTTPStatus.OK},
            )
            if response.parsed is None:
                raise SeclaiAPIStatusError(
                    message="Empty response",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                )
            parsed_response = cast(
                FileUploadResponse | HTTPValidationError, response.parsed
            )
            if isinstance(parsed_response, HTTPValidationError):
                raise SeclaiAPIValidationError(
                    message="Validation error",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                    validation_error=parsed_response,
                )
            if not isinstance(parsed_response, FileUploadResponse):
                raise SeclaiAPIStatusError(
                    message="Unexpected response shape",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                )
            return parsed_response
        finally:
            if created_payload is not None:
                created_payload.close()

    def upload_file_to_content(
        self,
        source_connection_content_version: str,
        *,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        title: str | None = None,
        metadata: Mapping[str, Any] | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> FileUploadResponse:
        """Replace an existing content version with a new file upload.

        This uploads a new file to `/contents/{source_connection_content_version}/upload` and replaces
        the content backing that existing content version.

        Args:
            source_connection_content_version: Source connection content version identifier.
            file: File payload. Accepts raw bytes, a filesystem path, or a binary file-like.
            title: Optional title for the uploaded file.
            metadata: Optional metadata dictionary to associate with the uploaded content.
            file_name: Optional filename to send when `file` is bytes or a file-like.
            mime_type: Optional MIME type to send.

        Returns:
            Upload response details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        import json as _json

        from seclai._generated.api.contents.upload_file_to_content_api_contents_source_connection_content_version_upload_post import (
            sync_detailed,
        )
        from seclai._generated.models.body_upload_file_to_content_api_contents_source_connection_content_version_upload_post import (
            BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
        )
        from seclai._generated.types import UNSET, File

        created_payload: BinaryIO | None = None
        try:
            upload_file: File
            if isinstance(file, File):
                upload_file = file
            elif isinstance(file, (str, os.PathLike)):
                file_path = Path(file)
                resolved_file_name = file_name or file_path.name
                resolved_mime_type = mime_type or _guess_mime_type(resolved_file_name)
                created_payload = file_path.open("rb")
                upload_file = File(
                    payload=created_payload,
                    file_name=resolved_file_name,
                    mime_type=resolved_mime_type,
                )
            elif isinstance(file, bytes):
                created_payload = BytesIO(file)
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=created_payload,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )
            else:
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=file,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )

            body = BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost(
                file=upload_file,
                title=UNSET if title is None else title,
                metadata=UNSET if metadata is None else _json.dumps(metadata),
            )
            endpoint_path = f"/contents/{source_connection_content_version}/upload"
            response = sync_detailed(
                source_connection_content_version=source_connection_content_version,
                client=self._generated_client(),
                body=body,
            )
            self._raise_for_openapi_response(
                method="POST",
                path=endpoint_path,
                response=response,
                ok_statuses={HTTPStatus.OK},
            )
            if response.parsed is None:
                raise SeclaiAPIStatusError(
                    message="Empty response",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                )
            parsed = response.parsed
            if isinstance(parsed, HTTPValidationError):
                raise SeclaiAPIValidationError(
                    message="Validation error",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                    validation_error=parsed,
                )
            return parsed
        finally:
            if created_payload is not None:
                created_payload.close()

    # ── Agents ────────────────────────────────────────────────────────────────

    def list_agents(self, *, page: int = 1, limit: int = 50) -> dict[str, Any]:
        """List all agents.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of agents.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/agents",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def create_agent(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a new agent.

        Args:
            body: Agent creation payload (name, description, etc.).

        Returns:
            The created agent.
        """
        return cast(dict[str, Any], self.request("POST", "/agents", json=body))

    def get_agent(self, agent_id: str) -> dict[str, Any]:
        """Get an agent by ID.

        Args:
            agent_id: Agent identifier.

        Returns:
            Agent details.
        """
        return cast(dict[str, Any], self.request("GET", f"/agents/{agent_id}"))

    def update_agent(self, agent_id: str, body: dict[str, Any]) -> dict[str, Any]:
        """Update an agent.

        Args:
            agent_id: Agent identifier.
            body: Fields to update.

        Returns:
            The updated agent.
        """
        return cast(
            dict[str, Any], self.request("PUT", f"/agents/{agent_id}", json=body)
        )

    def delete_agent(self, agent_id: str) -> None:
        """Delete an agent.

        Args:
            agent_id: Agent identifier.
        """
        self.request("DELETE", f"/agents/{agent_id}")

    # ── Agent Definitions ─────────────────────────────────────────────────────

    def get_agent_definition(self, agent_id: str) -> dict[str, Any]:
        """Get the step definition for an agent.

        Args:
            agent_id: Agent identifier.

        Returns:
            The agent's step definition.
        """
        return cast(
            dict[str, Any], self.request("GET", f"/agents/{agent_id}/definition")
        )

    def update_agent_definition(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update the step definition for an agent.

        Args:
            agent_id: Agent identifier.
            body: New definition payload (must include ``change_id`` for optimistic locking).

        Returns:
            The updated agent definition.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PUT",
                f"/agents/{agent_id}/definition",
                json=body,
            ),
        )

    # ── Agent Runs (additional) ───────────────────────────────────────────────

    def search_agent_runs(self, body: dict[str, Any]) -> dict[str, Any]:
        """Search agent runs across agents.

        Args:
            body: Search request with query filters.

        Returns:
            Search results with matching runs.
        """
        return cast(
            dict[str, Any], self.request("POST", "/agents/runs/search", json=body)
        )

    def cancel_agent_run(self, run_id: str) -> dict[str, Any]:
        """Cancel an in-progress agent run.

        Args:
            run_id: Run identifier.

        Returns:
            The updated agent run.
        """
        return cast(
            dict[str, Any], self.request("POST", f"/agents/runs/{run_id}/cancel")
        )

    # ── Agent Input Uploads ───────────────────────────────────────────────────

    def upload_agent_input(
        self,
        agent_id: str,
        *,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> dict[str, Any]:
        """Upload a file as input for an agent run.

        Args:
            agent_id: Agent identifier.
            file: File payload (bytes, path, or file-like).
            file_name: Filename to send.
            mime_type: MIME type of the file.

        Returns:
            Upload response with the input upload ID.
        """
        payload, created = self._prepare_upload_payload(file, file_name, mime_type)
        try:
            response = self._client.post(
                f"/agents/{agent_id}/upload-input",
                files={"file": payload},
                headers=_merge_request_headers(
                    options=self._options, request_headers=None
                ),
            )
            _raise_for_status(response)
            return cast(dict[str, Any], response.json())
        finally:
            if created is not None:
                created.close()

    def get_agent_input_upload_status(
        self, agent_id: str, upload_id: str
    ) -> dict[str, Any]:
        """Get the status of an agent input upload.

        Args:
            agent_id: Agent identifier.
            upload_id: Upload identifier.

        Returns:
            Upload status details.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/{agent_id}/input-uploads/{upload_id}",
            ),
        )

    # ── Agent AI Assistant ────────────────────────────────────────────────────

    def generate_agent_steps(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate agent steps.

        Args:
            agent_id: Agent identifier.
            body: Prompt and context for step generation.

        Returns:
            Generated steps suggestion.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/agents/{agent_id}/ai-assistant/generate-steps",
                json=body,
            ),
        )

    def generate_step_config(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate configuration for a single step.

        Args:
            agent_id: Agent identifier.
            body: Step type and context for config generation.

        Returns:
            Generated step configuration.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/agents/{agent_id}/ai-assistant/step-config",
                json=body,
            ),
        )

    def get_agent_ai_conversation_history(self, agent_id: str) -> dict[str, Any]:
        """Get the AI assistant conversation history for an agent.

        Args:
            agent_id: Agent identifier.

        Returns:
            Conversation history with the AI assistant.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/{agent_id}/ai-assistant/conversations",
            ),
        )

    def mark_agent_ai_suggestion(
        self, agent_id: str, conversation_id: str, body: dict[str, Any]
    ) -> None:
        """Mark an AI assistant suggestion as accepted or rejected.

        Args:
            agent_id: Agent identifier.
            conversation_id: Conversation identifier.
            body: Acceptance/rejection payload.
        """
        self.request(
            "PATCH",
            f"/agents/{agent_id}/ai-assistant/{conversation_id}",
            json=body,
        )

    # ── Agent Evaluations ─────────────────────────────────────────────────────

    def list_evaluation_criteria(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> list[dict[str, Any]]:
        """List evaluation criteria for an agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            List of evaluation criteria.
        """
        return cast(
            list[dict[str, Any]],
            self.request(
                "GET",
                f"/agents/{agent_id}/evaluation-criteria",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def create_evaluation_criteria(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Create evaluation criteria for an agent.

        Args:
            agent_id: Agent identifier.
            body: Criteria definition.

        Returns:
            The created evaluation criteria.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/agents/{agent_id}/evaluation-criteria",
                json=body,
            ),
        )

    def get_evaluation_criteria(self, criteria_id: str) -> dict[str, Any]:
        """Get evaluation criteria by ID.

        Args:
            criteria_id: Evaluation criteria identifier.

        Returns:
            Evaluation criteria details.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}",
            ),
        )

    def update_evaluation_criteria(
        self, criteria_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
            body: Fields to update.

        Returns:
            The updated evaluation criteria.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PATCH",
                f"/agents/evaluation-criteria/{criteria_id}",
                json=body,
            ),
        )

    def delete_evaluation_criteria(self, criteria_id: str) -> None:
        """Delete evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
        """
        self.request("DELETE", f"/agents/evaluation-criteria/{criteria_id}")

    def get_evaluation_criteria_summary(self, criteria_id: str) -> dict[str, Any]:
        """Get the result summary for evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.

        Returns:
            Summary of evaluation results.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}/summary",
            ),
        )

    def list_evaluation_results(
        self, criteria_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List evaluation results for criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation results.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}/results",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def create_evaluation_result(
        self, criteria_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Create a manual evaluation result.

        Args:
            criteria_id: Evaluation criteria identifier.
            body: Evaluation result payload.

        Returns:
            The created evaluation result.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/agents/evaluation-criteria/{criteria_id}/results",
                json=body,
            ),
        )

    def list_compatible_runs(
        self, criteria_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List agent runs compatible with evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of compatible runs.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}/compatible-runs",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def test_draft_evaluation(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Test a draft evaluation criteria without persisting.

        Args:
            agent_id: Agent identifier.
            body: Draft evaluation criteria and test run.

        Returns:
            Test evaluation result.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/agents/{agent_id}/evaluation-criteria/test-draft",
                json=body,
            ),
        )

    def list_agent_evaluation_results(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List all evaluation results for an agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation results with criteria.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/{agent_id}/evaluation-results",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def list_run_evaluation_results(
        self, agent_id: str, run_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List evaluation results for a specific agent run.

        Args:
            agent_id: Agent identifier.
            run_id: Run identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation results with criteria.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/{agent_id}/runs/{run_id}/evaluation-results",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def list_evaluation_runs(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List evaluation run summaries for an agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation run summaries.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/agents/{agent_id}/evaluation-runs",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def get_non_manual_evaluation_summary(self, agent_id: str) -> dict[str, Any]:
        """Get the non-manual evaluation summary for an agent.

        Args:
            agent_id: Agent identifier.

        Returns:
            Summary of automated evaluation results.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/agents/evaluation-results/non-manual-summary",
                params={"agent_id": agent_id},
            ),
        )

    # ── Knowledge Bases ───────────────────────────────────────────────────────

    def list_knowledge_bases(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        sort: str = "created_at",
        order: str = "desc",
    ) -> dict[str, Any]:
        """List knowledge bases.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (``"asc"`` or ``"desc"``).

        Returns:
            Paginated list of knowledge bases.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/knowledge_bases",
                params=_strip_none(
                    {"page": page, "limit": limit, "sort": sort, "order": order}
                ),
            ),
        )

    def create_knowledge_base(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a knowledge base.

        Args:
            body: Knowledge base creation payload.

        Returns:
            The created knowledge base.
        """
        return cast(dict[str, Any], self.request("POST", "/knowledge_bases", json=body))

    def get_knowledge_base(self, knowledge_base_id: str) -> dict[str, Any]:
        """Get a knowledge base by ID.

        Args:
            knowledge_base_id: Knowledge base identifier.

        Returns:
            Knowledge base details.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/knowledge_bases/{knowledge_base_id}",
            ),
        )

    def update_knowledge_base(
        self, knowledge_base_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a knowledge base.

        Args:
            knowledge_base_id: Knowledge base identifier.
            body: Fields to update.

        Returns:
            The updated knowledge base.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PUT",
                f"/knowledge_bases/{knowledge_base_id}",
                json=body,
            ),
        )

    def delete_knowledge_base(self, knowledge_base_id: str) -> None:
        """Delete a knowledge base.

        Args:
            knowledge_base_id: Knowledge base identifier.
        """
        self.request("DELETE", f"/knowledge_bases/{knowledge_base_id}")

    # ── Memory Banks ──────────────────────────────────────────────────────────

    def list_memory_banks(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        sort: str = "created_at",
        order: str = "desc",
    ) -> dict[str, Any]:
        """List memory banks.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (``"asc"`` or ``"desc"``).

        Returns:
            Paginated list of memory banks.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/memory_banks",
                params=_strip_none(
                    {"page": page, "limit": limit, "sort": sort, "order": order}
                ),
            ),
        )

    def create_memory_bank(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a memory bank.

        Args:
            body: Memory bank creation payload (name, type, config, etc.).

        Returns:
            The created memory bank.
        """
        return cast(dict[str, Any], self.request("POST", "/memory_banks", json=body))

    def get_memory_bank(self, memory_bank_id: str) -> dict[str, Any]:
        """Get a memory bank by ID.

        Args:
            memory_bank_id: Memory bank identifier.

        Returns:
            Memory bank details.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/memory_banks/{memory_bank_id}",
            ),
        )

    def update_memory_bank(
        self, memory_bank_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
            body: Fields to update.

        Returns:
            The updated memory bank.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PUT",
                f"/memory_banks/{memory_bank_id}",
                json=body,
            ),
        )

    def delete_memory_bank(self, memory_bank_id: str) -> None:
        """Delete a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
        """
        self.request("DELETE", f"/memory_banks/{memory_bank_id}")

    def get_agents_using_memory_bank(self, memory_bank_id: str) -> JSONValue:
        """Get agents that use a specific memory bank.

        Args:
            memory_bank_id: Memory bank identifier.

        Returns:
            List of agents using this memory bank.
        """
        return self.request("GET", f"/memory_banks/{memory_bank_id}/agents")

    def get_memory_bank_stats(self, memory_bank_id: str) -> JSONValue:
        """Get statistics for a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.

        Returns:
            Memory bank statistics.
        """
        return self.request("GET", f"/memory_banks/{memory_bank_id}/stats")

    def compact_memory_bank(self, memory_bank_id: str) -> None:
        """Trigger compaction of a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
        """
        self.request("POST", f"/memory_banks/{memory_bank_id}/compact")

    def delete_memory_bank_source(self, memory_bank_id: str) -> None:
        """Delete the source backing a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
        """
        self.request("DELETE", f"/memory_banks/{memory_bank_id}/source")

    def test_memory_bank_compaction(
        self, memory_bank_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Test compaction of a memory bank without applying.

        Args:
            memory_bank_id: Memory bank identifier.
            body: Test compaction parameters.

        Returns:
            Compaction test result.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/memory_banks/{memory_bank_id}/test-compaction",
                json=body,
            ),
        )

    def test_compaction_prompt_standalone(self, body: dict[str, Any]) -> dict[str, Any]:
        """Test a compaction prompt without an existing memory bank.

        Args:
            body: Standalone test compaction parameters.

        Returns:
            Compaction test result.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/memory_banks/test-compaction",
                json=body,
            ),
        )

    def list_memory_bank_templates(self) -> JSONValue:
        """List available memory bank templates.

        Returns:
            Available templates.
        """
        return self.request("GET", "/memory_banks/templates")

    def generate_memory_bank_config(self, body: dict[str, Any]) -> dict[str, Any]:
        """Use the AI assistant to generate memory bank configuration.

        Args:
            body: Prompt and context for config generation.

        Returns:
            Generated memory bank configuration.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/memory_banks/ai-assistant",
                json=body,
            ),
        )

    def get_memory_bank_ai_last_conversation(self) -> dict[str, Any]:
        """Get the last AI assistant conversation for memory banks.

        Returns:
            Last conversation with the memory bank AI assistant.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/memory_banks/ai-assistant/last-conversation",
            ),
        )

    def accept_memory_bank_ai_suggestion(
        self, conversation_id: str, body: dict[str, Any]
    ) -> JSONValue:
        """Accept an AI assistant suggestion for a memory bank.

        Args:
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Acceptance result.
        """
        return self.request(
            "PATCH",
            f"/memory_banks/ai-assistant/{conversation_id}",
            json=body,
        )

    # ── Sources (additional) ──────────────────────────────────────────────────

    def create_source(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a new source.

        Args:
            body: Source creation payload.

        Returns:
            The created source.
        """
        return cast(dict[str, Any], self.request("POST", "/sources", json=body))

    def get_source(self, source_id: str) -> dict[str, Any]:
        """Get a source by ID.

        Args:
            source_id: Source identifier.

        Returns:
            Source details.
        """
        return cast(dict[str, Any], self.request("GET", f"/sources/{source_id}"))

    def update_source(self, source_id: str, body: dict[str, Any]) -> dict[str, Any]:
        """Update a source.

        Args:
            source_id: Source identifier.
            body: Fields to update.

        Returns:
            The updated source.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PUT",
                f"/sources/{source_id}",
                json=body,
            ),
        )

    def delete_source(self, source_id: str) -> None:
        """Delete a source.

        Args:
            source_id: Source identifier.
        """
        self.request("DELETE", f"/sources/{source_id}")

    def upload_inline_text_to_source(
        self, source_connection_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Upload inline text content to a source connection.

        Args:
            source_connection_id: Source connection identifier.
            body: Inline text payload with title and content.

        Returns:
            Upload response details.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/sources/{source_connection_id}",
                json=body,
            ),
        )

    # ── Source Exports ────────────────────────────────────────────────────────

    def list_source_exports(
        self, source_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List exports for a source.

        Args:
            source_id: Source identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of exports.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/sources/{source_id}/exports",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    def create_source_export(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Create an export for a source.

        Args:
            source_id: Source identifier.
            body: Export configuration (format, filters, etc.).

        Returns:
            The created export.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/sources/{source_id}/exports",
                json=body,
            ),
        )

    def get_source_export(self, source_id: str, export_id: str) -> dict[str, Any]:
        """Get details of a source export.

        Args:
            source_id: Source identifier.
            export_id: Export identifier.

        Returns:
            Export details.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/sources/{source_id}/exports/{export_id}",
            ),
        )

    def cancel_source_export(self, source_id: str, export_id: str) -> dict[str, Any]:
        """Cancel a source export.

        Args:
            source_id: Source identifier.
            export_id: Export identifier.

        Returns:
            The updated export.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/sources/{source_id}/exports/{export_id}/cancel",
            ),
        )

    def delete_source_export(self, source_id: str, export_id: str) -> None:
        """Delete a source export.

        Args:
            source_id: Source identifier.
            export_id: Export identifier.
        """
        self.request("DELETE", f"/sources/{source_id}/exports/{export_id}")

    def download_source_export(self, source_id: str, export_id: str) -> httpx.Response:
        """Download a completed source export.

        Returns a **streaming** response. The caller is responsible for
        consuming and closing the response::

            response = client.download_source_export("src", "exp")
            with response:
                for chunk in response.iter_bytes():
                    f.write(chunk)

        Args:
            source_id: Source identifier.
            export_id: Export identifier.

        Returns:
            A streaming ``httpx.Response``. Must be closed by the caller.
        """
        request = self._client.build_request(
            "GET",
            f"/sources/{source_id}/exports/{export_id}/download",
            headers=_merge_request_headers(options=self._options, request_headers=None),
        )
        response = self._client.send(request, stream=True)
        _raise_for_status(response)
        return response

    def estimate_source_export(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Estimate the size/cost of a source export.

        Args:
            source_id: Source identifier.
            body: Export estimation parameters.

        Returns:
            Export estimate.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/sources/{source_id}/exports/estimate",
                json=body,
            ),
        )

    # ── Source Embedding Migrations ───────────────────────────────────────────

    def get_source_embedding_migration(self, source_id: str) -> dict[str, Any]:
        """Get the embedding migration status for a source.

        Args:
            source_id: Source identifier.

        Returns:
            Migration status.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                f"/sources/{source_id}/embedding-migration",
            ),
        )

    def start_source_embedding_migration(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Start an embedding migration for a source.

        Args:
            source_id: Source identifier.
            body: Migration configuration.

        Returns:
            The started migration.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/sources/{source_id}/embedding-migration",
                json=body,
            ),
        )

    def cancel_source_embedding_migration(self, source_id: str) -> dict[str, Any]:
        """Cancel an in-progress embedding migration for a source.

        Args:
            source_id: Source identifier.

        Returns:
            The cancelled migration.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/sources/{source_id}/embedding-migration/cancel",
            ),
        )

    # ── Content (additional) ──────────────────────────────────────────────────

    def replace_content_with_inline_text(
        self, content_version_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Replace content with inline text.

        Args:
            content_version_id: Content version identifier.
            body: Inline text payload.

        Returns:
            Upload response.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PUT",
                f"/contents/{content_version_id}",
                json=body,
            ),
        )

    # ── Solutions ─────────────────────────────────────────────────────────────

    def list_solutions(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        sort: str = "created_at",
        order: str = "desc",
    ) -> dict[str, Any]:
        """List solutions.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (``"asc"`` or ``"desc"``).

        Returns:
            Paginated list of solutions.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/solutions",
                params=_strip_none(
                    {"page": page, "limit": limit, "sort": sort, "order": order}
                ),
            ),
        )

    def create_solution(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a solution.

        Args:
            body: Solution creation payload.

        Returns:
            The created solution.
        """
        return cast(dict[str, Any], self.request("POST", "/solutions", json=body))

    def get_solution(self, solution_id: str) -> dict[str, Any]:
        """Get a solution by ID.

        Args:
            solution_id: Solution identifier.

        Returns:
            Solution details.
        """
        return cast(dict[str, Any], self.request("GET", f"/solutions/{solution_id}"))

    def update_solution(self, solution_id: str, body: dict[str, Any]) -> dict[str, Any]:
        """Update a solution.

        Args:
            solution_id: Solution identifier.
            body: Fields to update.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "PATCH",
                f"/solutions/{solution_id}",
                json=body,
            ),
        )

    def delete_solution(self, solution_id: str) -> None:
        """Delete a solution.

        Args:
            solution_id: Solution identifier.
        """
        self.request("DELETE", f"/solutions/{solution_id}")

    def link_agents_to_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Link agents to a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to link.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/agents",
                json=body,
            ),
        )

    def unlink_agents_from_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Unlink agents from a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to unlink.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "DELETE",
                f"/solutions/{solution_id}/agents",
                json=body,
            ),
        )

    def link_knowledge_bases_to_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Link knowledge bases to a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to link.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/knowledge-bases",
                json=body,
            ),
        )

    def unlink_knowledge_bases_from_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Unlink knowledge bases from a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to unlink.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "DELETE",
                f"/solutions/{solution_id}/knowledge-bases",
                json=body,
            ),
        )

    def link_source_connections_to_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Link source connections to a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to link.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/source-connections",
                json=body,
            ),
        )

    def unlink_source_connections_from_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Unlink source connections from a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to unlink.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            self.request(
                "DELETE",
                f"/solutions/{solution_id}/source-connections",
                json=body,
            ),
        )

    def list_solution_conversations(self, solution_id: str) -> list[dict[str, Any]]:
        """List AI assistant conversations for a solution.

        Args:
            solution_id: Solution identifier.

        Returns:
            List of conversations.
        """
        return cast(
            list[dict[str, Any]],
            self.request(
                "GET",
                f"/solutions/{solution_id}/conversations",
            ),
        )

    def add_solution_conversation_turn(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Add a turn to a solution AI conversation.

        Args:
            solution_id: Solution identifier.
            body: Conversation turn payload.

        Returns:
            The conversation response.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/conversations",
                json=body,
            ),
        )

    def mark_solution_conversation_turn(
        self, solution_id: str, conversation_id: str, body: dict[str, Any]
    ) -> None:
        """Mark a solution conversation turn as accepted or rejected.

        Args:
            solution_id: Solution identifier.
            conversation_id: Conversation identifier.
            body: Acceptance/rejection payload.
        """
        self.request(
            "PATCH",
            f"/solutions/{solution_id}/conversations/{conversation_id}",
            json=body,
        )

    def generate_solution_ai_plan(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate a solution plan.

        Args:
            solution_id: Solution identifier.
            body: Prompt and context.

        Returns:
            Generated plan with proposed actions.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/generate",
                json=body,
            ),
        )

    def generate_solution_ai_knowledge_base(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate a knowledge base plan for a solution.

        Args:
            solution_id: Solution identifier.
            body: Prompt and context.

        Returns:
            Generated knowledge base plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/knowledge-base",
                json=body,
            ),
        )

    def generate_solution_ai_source(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate a source plan for a solution.

        Args:
            solution_id: Solution identifier.
            body: Prompt and context.

        Returns:
            Generated source plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/source",
                json=body,
            ),
        )

    def accept_solution_ai_plan(
        self, solution_id: str, conversation_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Accept an AI-generated solution plan.

        Args:
            solution_id: Solution identifier.
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Result of applying the plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/{conversation_id}/accept",
                json=body,
            ),
        )

    def decline_solution_ai_plan(self, solution_id: str, conversation_id: str) -> None:
        """Decline an AI-generated solution plan.

        Args:
            solution_id: Solution identifier.
            conversation_id: Conversation identifier.
        """
        self.request(
            "POST",
            f"/solutions/{solution_id}/ai-assistant/{conversation_id}/decline",
        )

    # ── Governance AI ─────────────────────────────────────────────────────────

    def generate_governance_ai_plan(self, body: dict[str, Any]) -> dict[str, Any]:
        """Use the AI assistant to generate a governance plan.

        Args:
            body: Prompt and context for governance policy management.

        Returns:
            Generated governance plan with proposed actions.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/governance/ai-assistant",
                json=body,
            ),
        )

    def list_governance_ai_conversations(self) -> list[dict[str, Any]]:
        """List governance AI assistant conversations.

        Returns:
            List of governance conversations.
        """
        return cast(
            list[dict[str, Any]],
            self.request(
                "GET",
                "/governance/ai-assistant/conversations",
            ),
        )

    def accept_governance_ai_plan(self, conversation_id: str) -> dict[str, Any]:
        """Accept an AI-generated governance plan.

        Args:
            conversation_id: Conversation identifier.

        Returns:
            Result of applying the governance plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/governance/ai-assistant/{conversation_id}/accept",
            ),
        )

    def decline_governance_ai_plan(self, conversation_id: str) -> None:
        """Decline an AI-generated governance plan.

        Args:
            conversation_id: Conversation identifier.
        """
        self.request(
            "POST",
            f"/governance/ai-assistant/{conversation_id}/decline",
        )

    # ── Alerts ────────────────────────────────────────────────────────────────

    def list_alerts(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        status: str | None = None,
        severity: str | None = None,
    ) -> JSONValue:
        """List alerts.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            status: Filter by alert status.
            severity: Filter by severity.

        Returns:
            Paginated list of alerts.
        """
        return self.request(
            "GET",
            "/alerts",
            params=_strip_none(
                {"page": page, "limit": limit, "status": status, "severity": severity}
            ),
        )

    def get_alert(self, alert_id: str) -> JSONValue:
        """Get an alert by ID.

        Args:
            alert_id: Alert identifier.

        Returns:
            Alert details.
        """
        return self.request("GET", f"/alerts/{alert_id}")

    def change_alert_status(self, alert_id: str, body: dict[str, Any]) -> JSONValue:
        """Change the status of an alert.

        Args:
            alert_id: Alert identifier.
            body: New status payload.

        Returns:
            Updated alert.
        """
        return self.request("POST", f"/alerts/{alert_id}/status", json=body)

    def add_alert_comment(self, alert_id: str, body: dict[str, Any]) -> JSONValue:
        """Add a comment to an alert.

        Args:
            alert_id: Alert identifier.
            body: Comment payload.

        Returns:
            Comment result.
        """
        return self.request("POST", f"/alerts/{alert_id}/comments", json=body)

    def subscribe_to_alert(self, alert_id: str) -> JSONValue:
        """Subscribe to an alert.

        Args:
            alert_id: Alert identifier.

        Returns:
            Subscription result.
        """
        return self.request("POST", f"/alerts/{alert_id}/subscribe")

    def unsubscribe_from_alert(self, alert_id: str) -> JSONValue:
        """Unsubscribe from an alert.

        Args:
            alert_id: Alert identifier.

        Returns:
            Unsubscription result.
        """
        return self.request("POST", f"/alerts/{alert_id}/unsubscribe")

    # ── Alert Configs ─────────────────────────────────────────────────────────

    def list_alert_configs(self, *, page: int = 1, limit: int = 50) -> JSONValue:
        """List alert configurations.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of alert configurations.
        """
        return self.request(
            "GET",
            "/alerts/configs",
            params=_strip_none({"page": page, "limit": limit}),
        )

    def create_alert_config(self, body: dict[str, Any]) -> JSONValue:
        """Create an alert configuration.

        Args:
            body: Alert config creation payload.

        Returns:
            The created alert configuration.
        """
        return self.request("POST", "/alerts/configs", json=body)

    def get_alert_config(self, config_id: str) -> JSONValue:
        """Get an alert configuration by ID.

        Args:
            config_id: Alert config identifier.

        Returns:
            Alert configuration details.
        """
        return self.request("GET", f"/alerts/configs/{config_id}")

    def update_alert_config(self, config_id: str, body: dict[str, Any]) -> JSONValue:
        """Update an alert configuration.

        Args:
            config_id: Alert config identifier.
            body: Fields to update.

        Returns:
            The updated alert configuration.
        """
        return self.request("PATCH", f"/alerts/configs/{config_id}", json=body)

    def delete_alert_config(self, config_id: str) -> None:
        """Delete an alert configuration.

        Args:
            config_id: Alert config identifier.
        """
        self.request("DELETE", f"/alerts/configs/{config_id}")

    # ── Alert Preferences ─────────────────────────────────────────────────────

    def list_organization_alert_preferences(self) -> dict[str, Any]:
        """List organization alert preferences.

        Returns:
            Alert preferences for the organization.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/alerts/organization-preferences/list",
            ),
        )

    def update_organization_alert_preference(
        self, organization_id: str, alert_type: str, body: dict[str, Any]
    ) -> JSONValue:
        """Update an organization alert preference.

        Args:
            organization_id: Organization identifier.
            alert_type: Alert type to configure.
            body: Preference update payload.

        Returns:
            Updated preference.
        """
        return self.request(
            "PATCH",
            f"/alerts/organization-preferences/{organization_id}/{alert_type}",
            json=body,
        )

    # ── Model Alerts ──────────────────────────────────────────────────────────

    def list_model_alerts(self, *, page: int = 1, limit: int = 50) -> JSONValue:
        """List model alerts.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of model alerts.
        """
        return self.request(
            "GET",
            "/models/alerts",
            params=_strip_none({"page": page, "limit": limit}),
        )

    def mark_all_model_alerts_read(self) -> None:
        """Mark all model alerts as read for the current account."""
        self.request("POST", "/models/alerts/mark-all-read")

    def get_unread_model_alert_count(self) -> JSONValue:
        """Get the count of unread model alerts.

        Returns:
            Unread alert count.
        """
        return self.request("GET", "/models/alerts/unread-count")

    def mark_model_alert_read(self, alert_id: str) -> None:
        """Mark a model alert as read.

        Args:
            alert_id: Alert identifier.
        """
        self.request("PATCH", f"/models/alerts/{alert_id}/read")

    # ── Models ────────────────────────────────────────────────────────────────

    def get_model_recommendations(self, model_id: str) -> JSONValue:
        """Get recommendations for a model.

        Args:
            model_id: Model identifier.

        Returns:
            Model recommendations.
        """
        return self.request("GET", f"/models/{model_id}/recommendations")

    # ── Search ────────────────────────────────────────────────────────────────

    def search(
        self,
        *,
        query: str,
        limit: int = 10,
        entity_type: str | None = None,
    ) -> JSONValue:
        """Search across the Seclai platform.

        Args:
            query: Search query string.
            limit: Maximum results to return.
            entity_type: Optional entity type filter.

        Returns:
            Search results.
        """
        return self.request(
            "GET",
            "/search",
            params=_strip_none(
                {"query": query, "limit": limit, "entity_type": entity_type}
            ),
        )

    # ── Top-level AI Assistant ─────────────────────────────────────────────────

    def submit_ai_feedback(self, body: dict[str, Any]) -> dict[str, Any]:
        """Submit feedback to the AI assistant.

        Args:
            body: Feedback payload.

        Returns:
            Feedback response.
        """
        return cast(
            dict[str, Any], self.request("POST", "/ai-assistant/feedback", json=body)
        )

    def ai_assistant_knowledge_base(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a knowledge base plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/ai-assistant/knowledge-base",
                json=body,
            ),
        )

    def ai_assistant_source(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a source plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/ai-assistant/source",
                json=body,
            ),
        )

    def ai_assistant_solution(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a solution plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/ai-assistant/solution",
                json=body,
            ),
        )

    def ai_assistant_memory_bank(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a memory bank plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                "/ai-assistant/memory-bank",
                json=body,
            ),
        )

    def get_ai_assistant_memory_bank_history(self) -> dict[str, Any]:
        """Get the last AI assistant memory bank conversation.

        Returns:
            Last conversation.
        """
        return cast(
            dict[str, Any],
            self.request(
                "GET",
                "/ai-assistant/memory-bank/last-conversation",
            ),
        )

    def accept_ai_assistant_plan(
        self, conversation_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Accept a top-level AI assistant plan.

        Args:
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Result of applying the plan.
        """
        return cast(
            dict[str, Any],
            self.request(
                "POST",
                f"/ai-assistant/{conversation_id}/accept",
                json=body,
            ),
        )

    def decline_ai_assistant_plan(self, conversation_id: str) -> None:
        """Decline a top-level AI assistant plan.

        Args:
            conversation_id: Conversation identifier.
        """
        self.request("POST", f"/ai-assistant/{conversation_id}/decline")

    def accept_ai_memory_bank_suggestion(
        self, conversation_id: str, body: dict[str, Any]
    ) -> JSONValue:
        """Accept a top-level AI memory bank suggestion.

        Args:
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Acceptance result.
        """
        return self.request(
            "PATCH",
            f"/ai-assistant/memory-bank/{conversation_id}",
            json=body,
        )

    # ── Pagination helper ─────────────────────────────────────────────────────

    def paginate(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        limit: int = 50,
        items_key: str = "data",
    ) -> Generator[dict[str, Any]]:
        """Auto-paginate a list endpoint.

        Yields individual items from each page.
        Stops when a page returns fewer items than ``limit`` or the items list is empty.

        Args:
            method: HTTP method (typically ``"GET"``).
            path: API path.
            params: Extra query parameters (``page`` and ``limit`` are managed automatically).
            limit: Items per page.
            items_key: JSON key containing the list of items (default ``"data"``).

        Yields:
            Individual item dicts from each page.
        """
        page = 1
        base_params = dict(params) if params else {}
        while True:
            base_params["page"] = page
            base_params["limit"] = limit
            result = self.request(method, path, params=base_params)
            if not isinstance(result, dict):
                return
            items = result.get(items_key, [])
            if not isinstance(items, list):
                return
            for item in items:
                yield cast(dict[str, Any], item)
            if len(items) < limit:
                return
            page += 1

    # ── High-level Abstractions ───────────────────────────────────────────────

    def run_agent_and_poll(
        self,
        agent_id: str,
        body: AgentRunRequest,
        *,
        poll_interval: float = 2.0,
        include_step_outputs: bool = False,
    ) -> AgentRunResponse:
        """Run an agent and poll until it reaches a terminal status.

        Starts the agent run and then repeatedly polls ``get_agent_run`` until
        the status is ``"completed"`` or ``"failed"``.

        Args:
            agent_id: Agent identifier.
            body: Agent run request payload.
            poll_interval: Seconds between poll attempts (default 2.0).
            include_step_outputs: Include per-step outputs when polling.

        Returns:
            The final agent run (completed or failed).

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        run = self.run_agent(agent_id, body)
        while run.status not in ("completed", "failed"):
            time.sleep(poll_interval)
            run = self.get_agent_run(
                run.run_id, include_step_outputs=include_step_outputs
            )
        return run

    def run_streaming_agent(
        self,
        agent_id: str,
        body: AgentRunStreamRequest,
        *,
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Generator[tuple[str, dict[str, Any]]]:
        """Run an agent via SSE streaming, yielding events as they arrive.

        This is a generator that yields ``(event_type, data)`` tuples for each
        SSE event received. Event types include ``"init"`` and ``"done"``.

        Args:
            agent_id: Agent identifier.
            body: Streaming agent run request payload.
            timeout: Max time (seconds) to wait. Defaults to this client's timeout.
            headers: Optional extra headers.

        Yields:
            Tuples of ``(event_type, parsed_data)`` for each SSE event.

        Raises:
            SeclaiAPIStatusError: If the API returns a non-success status code.
            SeclaiStreamingError: If an error event is received.
            SeclaiError: If the stream times out.
        """
        import json as _json

        path = f"/agents/{agent_id}/runs/stream"
        merged_headers = _merge_request_headers(
            options=self._options, request_headers=headers
        )
        merged_headers.setdefault("accept", "text/event-stream")
        timeout_seconds = self._options.timeout if timeout is None else timeout
        start = time.monotonic()

        try:
            with self._client.stream(
                "POST",
                path,
                json=body,
                headers=merged_headers,
                timeout=timeout_seconds,
            ) as response:
                _raise_for_status(response)
                current_event: str | None = None
                data_lines: list[str] = []

                for line in response.iter_lines():
                    if time.monotonic() - start > timeout_seconds:
                        raise SeclaiError(
                            f"Timed out after {timeout_seconds}s waiting for streaming agent run."
                        )
                    if line == "":
                        if current_event and data_lines:
                            data = "\n".join(data_lines)
                            try:
                                parsed = cast(dict[str, Any], _json.loads(data))
                            except Exception:
                                parsed = {"raw": data}
                            if current_event == "error":
                                raise SeclaiStreamingError(
                                    parsed.get("message", data),
                                    run_id=parsed.get("run_id"),
                                )
                            yield (current_event, parsed)
                        current_event = None
                        data_lines = []
                        continue
                    if line.startswith(":"):
                        continue
                    if line.startswith("event:"):
                        current_event = line[len("event:") :].strip() or None
                        continue
                    if line.startswith("data:"):
                        data_lines.append(line[len("data:") :].lstrip())
                        continue

                # Flush any final event
                if current_event and data_lines:
                    data = "\n".join(data_lines)
                    try:
                        parsed = cast(dict[str, Any], _json.loads(data))
                    except Exception:
                        parsed = {"raw": data}
                    if current_event == "error":
                        raise SeclaiStreamingError(
                            parsed.get("message", data),
                            run_id=parsed.get("run_id"),
                        )
                    yield (current_event, parsed)
        except httpx.TimeoutException as e:
            raise SeclaiError(
                f"Timed out after {timeout_seconds}s waiting for streaming agent run."
            ) from e

    # ── Upload Helper ─────────────────────────────────────────────────────────

    def _prepare_upload_payload(
        self,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        file_name: str | None,
        mime_type: str | None,
    ) -> tuple[tuple[str | None, BinaryIO, str | None], BinaryIO | None]:
        """Prepare a file for multipart upload.

        Returns:
            A ``(file_tuple, created_handle)`` pair. ``created_handle`` must be
            closed by the caller when non-``None``.
        """
        created: BinaryIO | None = None
        if isinstance(file, (str, os.PathLike)):
            file_path = Path(file)
            resolved_name = file_name or file_path.name
            resolved_mime = mime_type or _guess_mime_type(resolved_name)
            created = file_path.open("rb")
            return (resolved_name, created, resolved_mime), created
        if isinstance(file, bytes):
            created = BytesIO(file)
            resolved_mime = mime_type or _guess_mime_type(file_name)
            return (file_name, created, resolved_mime), created
        resolved_mime = mime_type or _guess_mime_type(file_name)
        return (file_name, file, resolved_mime), None


class AsyncSeclai(_SeclaiBase):
    """Seclai asynchronous client.

    Most users should prefer the typed convenience methods (e.g. `run_agent`, `list_sources`)
    which raise SDK exceptions on failures.

    This client can be used as an async context manager:

        async with AsyncSeclai(api_key="...") as client:
            sources = await client.list_sources()
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        access_token: str | Callable[[], str | Awaitable[str]] | None = None,
        timeout: float = 30.0,
        api_key_header: str = "x-api-key",
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
        profile: str | None = None,
        config_dir: str | None = None,
        auto_refresh: bool = True,
        account_id: str | None = None,
    ) -> None:
        """Create an asynchronous Seclai client.

        Credentials are resolved via a chain (first match wins):

        1. Explicit ``api_key``
        2. Explicit ``access_token`` (static string or provider callable)
        3. ``SECLAI_API_KEY`` environment variable
        4. SSO profile from ``~/.seclai/config`` + cached tokens

        Args:
            api_key: API key used for authentication. If omitted, ``SECLAI_API_KEY`` is used.
            access_token: Static bearer token string or a callable returning one
                (sync or async). Mutually exclusive with ``api_key``.
            timeout: Request timeout (seconds).
            api_key_header: Header name to use for the API key.
            default_headers: Extra headers to include on every request.
            http_client: Optional pre-configured ``httpx.AsyncClient`` to use.
            profile: SSO profile name from ``~/.seclai/config``.
            config_dir: Override the config directory path.
            auto_refresh: Auto-refresh expired SSO tokens. Defaults to ``True``.
            account_id: Target organization account ID (``X-Account-Id`` header).

        Raises:
            SeclaiConfigurationError: If no credentials are found.
        """
        super().__init__(
            api_key=api_key,
            access_token=access_token,
            timeout=timeout,
            api_key_header=api_key_header,
            default_headers=default_headers,
            profile=profile,
            config_dir=config_dir,
            auto_refresh=auto_refresh,
            account_id=account_id,
        )
        self._client = http_client or httpx.AsyncClient(
            base_url=SECLAI_API_URL,
            timeout=self._options.timeout,
            headers=self._default_headers(),
        )
        self._owns_client = http_client is None

    async def aclose(self) -> None:
        """Close underlying HTTP resources owned by this client.

        If you created the client with a custom ``http_client``, this is a no-op
        for that client (you remain responsible for closing it).
        """
        if self._owns_client:
            await self._client.aclose()
        if self._owns_generated_client and self._generated_client_instance is not None:
            await self._generated_client_instance.get_async_httpx_client().aclose()

    async def __aenter__(self) -> Self:
        """Enter an async context manager and return self."""
        return self

    async def __aexit__(self, exc_type: object, exc: object, tb: object) -> None:
        """Exit the async context manager and close resources.

        Args:
            exc_type: Exception type (if any).
            exc: Exception instance (if any).
            tb: Traceback (if any).
        """
        await self.aclose()

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: JSONValue | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> JSONValue | str | None:
        """Make a raw HTTP request to the Seclai API.

        This is a low-level escape hatch. For most operations, prefer the typed
        convenience methods on this client.

        Args:
            method: HTTP method (e.g. `"GET"`, `"POST"`).
            path: Request path relative to `SECLAI_API_URL` (e.g. `"/sources/"`).
            params: Query parameters.
            json: JSON body to send.
            headers: Per-request header overrides.

        Returns:
            Parsed JSON for JSON responses, raw text for non-JSON responses, or `None` for empty bodies.

        Raises:
            SeclaiAPIStatusError: If the response status code is not successful.
        """
        response = await self._client.request(
            method,
            path,
            params=params,
            json=json,
            headers=await _merge_request_headers_async(
                options=self._options, request_headers=headers
            ),
        )
        _raise_for_status(response)
        if not response.content:
            return None
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            return cast(JSONValue, response.json())
        return response.text

    async def run_agent(self, agent_id: str, body: AgentRunRequest) -> AgentRunResponse:
        """Run an agent.

        Starts a new agent run for the given agent and returns the run record.

        Args:
            agent_id: Agent identifier.
            body: Agent run request payload.

        Returns:
            The created agent run.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.run_agent_api_agents_agent_id_runs_post import (
            asyncio_detailed,
        )

        path = f"/agents/{agent_id}/runs"
        response = await asyncio_detailed(
            agent_id=agent_id, client=self._generated_client(), body=body
        )
        self._raise_for_openapi_response(
            method="POST",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="POST",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="POST",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    async def run_streaming_agent_and_wait(
        self,
        agent_id: str,
        body: AgentRunStreamRequest,
        *,
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> AgentRunResponse:
        """Run an agent via SSE streaming and block until completion (async).

        This uses POST /agents/{agent_id}/runs/stream and consumes Server-Sent Events (SSE).
        The method returns when an `event: done` message is received.
        """
        import json as _json
        import time as _time

        path = f"/agents/{agent_id}/runs/stream"

        merged_headers = await _merge_request_headers_async(
            options=self._options, request_headers=headers
        )
        merged_headers.setdefault("accept", "text/event-stream")

        timeout_seconds = self._options.timeout if timeout is None else timeout
        start = _time.monotonic()

        try:
            async with self._client.stream(
                "POST",
                path,
                json=body,
                headers=merged_headers,
                timeout=timeout_seconds,
            ) as response:
                if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                    payload = response.json()
                    raise SeclaiAPIValidationError(
                        message=f"Request failed with status {response.status_code}",
                        status_code=int(response.status_code),
                        method="POST",
                        url=self._build_url(path),
                        response_text=response.text,
                        validation_error=HTTPValidationError.from_dict(payload),
                    )
                _raise_for_status(response)

                current_event: str | None = None
                data_lines: list[str] = []
                last_seen: AgentRunResponse | None = None

                def dispatch() -> AgentRunResponse | None:
                    nonlocal current_event, data_lines, last_seen
                    if current_event is None and not data_lines:
                        return None
                    data = "\n".join(data_lines)
                    evt = current_event
                    current_event = None
                    data_lines = []
                    if not data:
                        return None
                    if evt not in {"init", "done"}:
                        return None
                    try:
                        parsed_dict = cast(dict[str, Any], _json.loads(data))
                        parsed = AgentRunResponse.from_dict(parsed_dict)
                        last_seen = parsed
                        if evt == "done":
                            return parsed
                    except Exception:
                        return None
                    return None

                async for line in response.aiter_lines():
                    if _time.monotonic() - start > timeout_seconds:
                        raise SeclaiError(
                            f"Timed out after {timeout_seconds}s waiting for streaming agent run to complete."
                        )

                    if line == "":
                        done = dispatch()
                        if done is not None:
                            return done
                        continue
                    if line.startswith(":"):
                        continue
                    if line.startswith("event:"):
                        current_event = line[len("event:") :].strip() or None
                        continue
                    if line.startswith("data:"):
                        data_lines.append(line[len("data:") :].lstrip())
                        continue

                done = dispatch()
                if done is not None:
                    return done
                if last_seen is not None:
                    return last_seen
                raise SeclaiError("Stream ended before receiving a 'done' event.")
        except httpx.TimeoutException as e:
            raise SeclaiError(
                f"Timed out after {timeout_seconds}s waiting for streaming agent run to complete."
            ) from e

    async def list_agent_runs(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> AgentRunListResponse:
        """List agent runs.

        Returns paginated runs for a single agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            A paginated list of runs.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.list_agent_runs_api_agents_agent_id_runs_get import (
            asyncio_detailed,
        )

        path = f"/agents/{agent_id}/runs"
        response = await asyncio_detailed(
            agent_id=agent_id,
            client=self._generated_client(),
            page=page,
            limit=limit,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    @overload
    async def get_agent_run(
        self, run_id: str, /, *, include_step_outputs: bool = False
    ) -> AgentRunResponse: ...

    @overload
    async def get_agent_run(
        self, agent_id: str, run_id: str, /, *, include_step_outputs: bool = False
    ) -> AgentRunResponse: ...

    async def get_agent_run(
        self, *args: str, include_step_outputs: bool = False
    ) -> AgentRunResponse:
        """Get details of a specific agent run.

        Fetches the current state and details for a previously created run.

        Args:
            run_id: Run identifier.
            agent_id: Deprecated. Ignored if provided; maintained for backwards compatibility.
            include_step_outputs: If true, include per-step outputs with timing,
                durations, and credits. Defaults to False.

        Returns:
            Agent run details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        if len(args) == 1:
            run_id = args[0]
        elif len(args) == 2:
            # Backwards compatible: get_agent_run(agent_id, run_id)
            run_id = args[1]
        else:
            raise TypeError("get_agent_run expects (run_id) or (agent_id, run_id)")

        from seclai._generated.api.agents.get_agent_run_api_agents_runs_run_id_get import (
            asyncio_detailed,
        )

        path = f"/agents/runs/{run_id}"
        response = await asyncio_detailed(
            run_id=run_id,
            client=self._generated_client(),
            include_step_outputs=include_step_outputs,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    @overload
    async def delete_agent_run(self, run_id: str, /) -> AgentRunResponse: ...

    @overload
    async def delete_agent_run(
        self, agent_id: str, run_id: str, /
    ) -> AgentRunResponse: ...

    async def delete_agent_run(self, *args: str) -> AgentRunResponse:
        """Cancel an agent run.

        Requests cancellation of a run and returns the updated run record.

        Args:
            run_id: Run identifier.
            agent_id: Deprecated. Ignored if provided; maintained for backwards compatibility.

        Returns:
            The updated agent run.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        if len(args) == 1:
            run_id = args[0]
        elif len(args) == 2:
            # Backwards compatible: delete_agent_run(agent_id, run_id)
            run_id = args[1]
        else:
            raise TypeError("delete_agent_run expects (run_id) or (agent_id, run_id)")

        from seclai._generated.api.agents.delete_agent_run_api_agents_runs_run_id_delete import (
            asyncio_detailed,
        )

        path = f"/agents/runs/{run_id}"
        response = await asyncio_detailed(
            run_id=run_id,
            client=self._generated_client(),
        )
        self._raise_for_openapi_response(
            method="DELETE",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="DELETE",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="DELETE",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    async def get_content_detail(
        self,
        source_connection_content_version: str,
        *,
        start: int = 0,
        end: int = 5000,
    ) -> ContentDetailResponse:
        """Get content detail.

        Fetches a slice of a content version (use `start`/`end` to page through large content).

        Args:
            source_connection_content_version: Content version identifier.
            start: Start offset for returned content detail.
            end: End offset for returned content detail.

        Returns:
            Content details for the requested range.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.contents.get_content_detail_api_contents_source_connection_content_version_get import (
            asyncio_detailed,
        )

        path = f"/contents/{source_connection_content_version}"
        response = await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=self._generated_client(),
            start=start,
            end=end,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    async def delete_content(self, source_connection_content_version: str) -> None:
        """Delete a specific content version.

        Permanently removes a content version identified by `source_connection_content_version`.

        Args:
            source_connection_content_version: Content version identifier.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.contents.delete_content_api_contents_source_connection_content_version_delete import (
            asyncio_detailed,
        )

        path = f"/contents/{source_connection_content_version}"
        response = await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=self._generated_client(),
        )
        self._raise_for_openapi_response(
            method="DELETE",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.NO_CONTENT},
        )
        return None

    async def list_content_embeddings(
        self,
        source_connection_content_version: str,
        *,
        page: int = 1,
        limit: int = 20,
    ) -> ContentEmbeddingsListResponse:
        """List embeddings for a content version.

        Returns paginated embeddings that were computed for the given content version.

        Args:
            source_connection_content_version: Content version identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            A paginated list of embeddings.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.contents.list_content_embeddings_api_contents_source_connection_content_version_embeddings_get import (
            asyncio_detailed,
        )

        path = f"/contents/{source_connection_content_version}/embeddings"
        response = await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=self._generated_client(),
            page=page,
            limit=limit,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    async def list_sources(
        self,
        *,
        page: int = 1,
        limit: int = 20,
        sort: str = "created_at",
        order: str = "desc",
        account_id: str | None = None,
    ) -> SourceListResponse:
        """List sources.

        Returns the sources visible to your account (optionally filtered by `account_id`).

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (e.g. `"asc"` or `"desc"`).
            account_id: Optional account id; defaults to the API key's account.

        Returns:
            A paginated list of sources.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.sources.list_sources_api_sources_get import (
            asyncio_detailed,
        )

        path = "/sources/"
        response = await asyncio_detailed(
            client=self._generated_client(),
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            account_id=account_id,
        )
        self._raise_for_openapi_response(
            method="GET",
            path=path,
            response=response,
            ok_statuses={HTTPStatus.OK},
        )
        if response.parsed is None:
            raise SeclaiAPIStatusError(
                message="Empty response",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
            )
        parsed = response.parsed
        if isinstance(parsed, HTTPValidationError):
            raise SeclaiAPIValidationError(
                message="Validation error",
                status_code=int(response.status_code),
                method="GET",
                url=self._build_url(path),
                response_text=None,
                validation_error=parsed,
            )
        return parsed

    async def upload_file_to_source(
        self,
        source_connection_id: str,
        *,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        title: str | None = None,
        metadata: Mapping[str, Any] | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> FileUploadResponse:
        """Upload a file to a specific source connection.

        Sends a file to be ingested under the given source connection.

        Maximum file size: 200 MiB.

        Supported MIME types:
            - `application/epub+zip`
            - `application/json`
            - `application/msword`
            - `application/pdf`
            - `application/vnd.ms-excel`
            - `application/vnd.ms-outlook`
            - `application/vnd.ms-powerpoint`
            - `application/vnd.openxmlformats-officedocument.presentationml.presentation`
            - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
            - `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
            - `application/xml`
            - `application/zip`
            - `audio/flac`
            - `audio/mp4`
            - `audio/mpeg`
            - `audio/ogg`
            - `audio/wav`
            - `image/bmp`
            - `image/gif`
            - `image/jpeg`
            - `image/png`
            - `image/tiff`
            - `image/webp`
            - `text/csv`
            - `text/html`
            - `text/markdown` / `text/x-markdown`
            - `text/plain`
            - `text/xml`
            - `video/mp4`
            - `video/quicktime`
            - `video/x-msvideo`

        If `mime_type` is omitted and a filename is available, the SDK tries to infer it.
        If the upload is sent as `application/octet-stream`, the server attempts to infer
        the type from the file extension.

        Notes:
            - If `file` is a path or `bytes`, this method creates an in-memory/file handle and
              closes it before returning.
            - If `file` is a file-like object, the caller owns its lifecycle.

        Args:
            source_connection_id: Source connection identifier.
            file: File payload. Accepts raw bytes, a filesystem path, or a binary file-like.
            title: Optional title for the uploaded file.
            metadata: Optional metadata dictionary to associate with the uploaded content.
            file_name: Optional filename to send when `file` is bytes or a file-like.
            mime_type: Optional MIME type to send.

        Returns:
            Upload response details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        import json as _json

        from seclai._generated.models.body_upload_file_to_source_api_sources_source_connection_id_upload_post import (
            BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
        )
        from seclai._generated.types import UNSET, File

        created_payload: BinaryIO | None = None
        try:
            upload_file: File
            if isinstance(file, File):
                upload_file = file
            elif isinstance(file, (str, os.PathLike)):
                file_path = Path(file)
                resolved_file_name = file_name or file_path.name
                resolved_mime_type = mime_type or _guess_mime_type(resolved_file_name)
                created_payload = file_path.open("rb")
                upload_file = File(
                    payload=created_payload,
                    file_name=resolved_file_name,
                    mime_type=resolved_mime_type,
                )
            elif isinstance(file, bytes):
                created_payload = BytesIO(file)
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=created_payload,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )
            else:
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=file,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )

            body = BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost(
                file=upload_file,
                title=UNSET if title is None else title,
            )

            if metadata is not None:
                body["metadata"] = _json.dumps(metadata)

            endpoint_path = f"/sources/{source_connection_id}/upload"

            http = self._generated_client().get_async_httpx_client()
            raw = await http.request(
                "POST",
                endpoint_path,
                files=body.to_multipart(),
            )

            parsed: FileUploadResponse | HTTPValidationError | None = None
            if raw.status_code == 200:
                payload = cast(dict[str, Any], raw.json())
                parsed = FileUploadResponse.from_dict(payload)
            elif raw.status_code == 422:
                payload = cast(dict[str, Any], raw.json())
                parsed = HTTPValidationError.from_dict(payload)

            response = OpenAPIResponse(
                status_code=HTTPStatus(raw.status_code),
                content=raw.content,
                headers=raw.headers,
                parsed=parsed,
            )
            self._raise_for_openapi_response(
                method="POST",
                path=endpoint_path,
                response=response,
                ok_statuses={HTTPStatus.OK},
            )
            if response.parsed is None:
                raise SeclaiAPIStatusError(
                    message="Empty response",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                )
            parsed_response = cast(
                FileUploadResponse | HTTPValidationError, response.parsed
            )
            if isinstance(parsed_response, HTTPValidationError):
                raise SeclaiAPIValidationError(
                    message="Validation error",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                    validation_error=parsed_response,
                )
            if not isinstance(parsed_response, FileUploadResponse):
                raise SeclaiAPIStatusError(
                    message="Unexpected response shape",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                )
            return parsed_response
        finally:
            if created_payload is not None:
                created_payload.close()

    async def upload_file_to_content(
        self,
        source_connection_content_version: str,
        *,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        title: str | None = None,
        metadata: Mapping[str, Any] | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> FileUploadResponse:
        """Replace an existing content version with a new file upload.

        This uploads a new file to `/contents/{source_connection_content_version}/upload` and replaces
        the content backing that existing content version.

        Args:
            source_connection_content_version: Source connection content version identifier.
            file: File payload. Accepts raw bytes, a filesystem path, or a binary file-like.
            title: Optional title for the uploaded file.
            metadata: Optional metadata dictionary to associate with the uploaded content.
            file_name: Optional filename to send when `file` is bytes or a file-like.
            mime_type: Optional MIME type to send.

        Returns:
            Upload response details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        import json as _json

        from seclai._generated.api.contents.upload_file_to_content_api_contents_source_connection_content_version_upload_post import (
            asyncio_detailed,
        )
        from seclai._generated.models.body_upload_file_to_content_api_contents_source_connection_content_version_upload_post import (
            BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
        )
        from seclai._generated.types import UNSET, File

        created_payload: BinaryIO | None = None
        try:
            upload_file: File
            if isinstance(file, File):
                upload_file = file
            elif isinstance(file, (str, os.PathLike)):
                file_path = Path(file)
                resolved_file_name = file_name or file_path.name
                resolved_mime_type = mime_type or _guess_mime_type(resolved_file_name)
                created_payload = file_path.open("rb")
                upload_file = File(
                    payload=created_payload,
                    file_name=resolved_file_name,
                    mime_type=resolved_mime_type,
                )
            elif isinstance(file, bytes):
                created_payload = BytesIO(file)
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=created_payload,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )
            else:
                resolved_mime_type = mime_type or _guess_mime_type(file_name)
                upload_file = File(
                    payload=file,
                    file_name=file_name,
                    mime_type=resolved_mime_type,
                )

            body = BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost(
                file=upload_file,
                title=UNSET if title is None else title,
                metadata=UNSET if metadata is None else _json.dumps(metadata),
            )
            endpoint_path = f"/contents/{source_connection_content_version}/upload"
            response = await asyncio_detailed(
                source_connection_content_version=source_connection_content_version,
                client=self._generated_client(),
                body=body,
            )
            self._raise_for_openapi_response(
                method="POST",
                path=endpoint_path,
                response=response,
                ok_statuses={HTTPStatus.OK},
            )
            if response.parsed is None:
                raise SeclaiAPIStatusError(
                    message="Empty response",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                )
            parsed = response.parsed
            if isinstance(parsed, HTTPValidationError):
                raise SeclaiAPIValidationError(
                    message="Validation error",
                    status_code=int(response.status_code),
                    method="POST",
                    url=self._build_url(endpoint_path),
                    response_text=None,
                    validation_error=parsed,
                )
            return parsed
        finally:
            if created_payload is not None:
                created_payload.close()

    # ── Agents ────────────────────────────────────────────────────────────────

    async def list_agents(self, *, page: int = 1, limit: int = 50) -> dict[str, Any]:
        """List all agents.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of agents.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/agents",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def create_agent(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a new agent.

        Args:
            body: Agent creation payload (name, description, etc.).

        Returns:
            The created agent.
        """
        return cast(dict[str, Any], await self.request("POST", "/agents", json=body))

    async def get_agent(self, agent_id: str) -> dict[str, Any]:
        """Get an agent by ID.

        Args:
            agent_id: Agent identifier.

        Returns:
            Agent details.
        """
        return cast(dict[str, Any], await self.request("GET", f"/agents/{agent_id}"))

    async def update_agent(self, agent_id: str, body: dict[str, Any]) -> dict[str, Any]:
        """Update an agent.

        Args:
            agent_id: Agent identifier.
            body: Fields to update.

        Returns:
            The updated agent.
        """
        return cast(
            dict[str, Any], await self.request("PUT", f"/agents/{agent_id}", json=body)
        )

    async def delete_agent(self, agent_id: str) -> None:
        """Delete an agent.

        Args:
            agent_id: Agent identifier.
        """
        await self.request("DELETE", f"/agents/{agent_id}")

    # ── Agent Definitions ─────────────────────────────────────────────────────

    async def get_agent_definition(self, agent_id: str) -> dict[str, Any]:
        """Get the step definition for an agent.

        Args:
            agent_id: Agent identifier.

        Returns:
            The agent's step definition.
        """
        return cast(
            dict[str, Any], await self.request("GET", f"/agents/{agent_id}/definition")
        )

    async def update_agent_definition(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update the step definition for an agent.

        Args:
            agent_id: Agent identifier.
            body: New definition payload (must include ``change_id`` for optimistic locking).

        Returns:
            The updated agent definition.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PUT",
                f"/agents/{agent_id}/definition",
                json=body,
            ),
        )

    # ── Agent Runs (additional) ───────────────────────────────────────────────

    async def search_agent_runs(self, body: dict[str, Any]) -> dict[str, Any]:
        """Search agent runs across agents.

        Args:
            body: Search request with query filters.

        Returns:
            Search results with matching runs.
        """
        return cast(
            dict[str, Any], await self.request("POST", "/agents/runs/search", json=body)
        )

    async def cancel_agent_run(self, run_id: str) -> dict[str, Any]:
        """Cancel an in-progress agent run.

        Args:
            run_id: Run identifier.

        Returns:
            The updated agent run.
        """
        return cast(
            dict[str, Any], await self.request("POST", f"/agents/runs/{run_id}/cancel")
        )

    # ── Agent Input Uploads ───────────────────────────────────────────────────

    async def upload_agent_input(
        self,
        agent_id: str,
        *,
        file: bytes | str | os.PathLike[str] | BinaryIO,
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> dict[str, Any]:
        """Upload a file as input for an agent run.

        Args:
            agent_id: Agent identifier.
            file: File payload (bytes, path, or file-like).
            file_name: Filename to send.
            mime_type: MIME type of the file.

        Returns:
            Upload response with the input upload ID.
        """
        payload, created = Seclai._prepare_upload_payload(
            self,  # type: ignore[arg-type]  # reuse sync helper from async context
            file,
            file_name,
            mime_type,
        )
        try:
            response = await self._client.post(
                f"/agents/{agent_id}/upload-input",
                files={"file": payload},
                headers=await _merge_request_headers_async(
                    options=self._options, request_headers=None
                ),
            )
            _raise_for_status(response)
            return cast(dict[str, Any], response.json())
        finally:
            if created is not None:
                created.close()

    async def get_agent_input_upload_status(
        self, agent_id: str, upload_id: str
    ) -> dict[str, Any]:
        """Get the status of an agent input upload.

        Args:
            agent_id: Agent identifier.
            upload_id: Upload identifier.

        Returns:
            Upload status details.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/{agent_id}/input-uploads/{upload_id}",
            ),
        )

    # ── Agent AI Assistant ────────────────────────────────────────────────────

    async def generate_agent_steps(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate agent steps.

        Args:
            agent_id: Agent identifier.
            body: Prompt and context for step generation.

        Returns:
            Generated steps suggestion.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/agents/{agent_id}/ai-assistant/generate-steps",
                json=body,
            ),
        )

    async def generate_step_config(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate configuration for a single step.

        Args:
            agent_id: Agent identifier.
            body: Step type and context for config generation.

        Returns:
            Generated step configuration.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/agents/{agent_id}/ai-assistant/step-config",
                json=body,
            ),
        )

    async def get_agent_ai_conversation_history(self, agent_id: str) -> dict[str, Any]:
        """Get the AI assistant conversation history for an agent.

        Args:
            agent_id: Agent identifier.

        Returns:
            Conversation history with the AI assistant.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/{agent_id}/ai-assistant/conversations",
            ),
        )

    async def mark_agent_ai_suggestion(
        self, agent_id: str, conversation_id: str, body: dict[str, Any]
    ) -> None:
        """Mark an AI assistant suggestion as accepted or rejected.

        Args:
            agent_id: Agent identifier.
            conversation_id: Conversation identifier.
            body: Acceptance/rejection payload.
        """
        await self.request(
            "PATCH",
            f"/agents/{agent_id}/ai-assistant/{conversation_id}",
            json=body,
        )

    # ── Agent Evaluations ─────────────────────────────────────────────────────

    async def list_evaluation_criteria(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> list[dict[str, Any]]:
        """List evaluation criteria for an agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            List of evaluation criteria.
        """
        return cast(
            list[dict[str, Any]],
            await self.request(
                "GET",
                f"/agents/{agent_id}/evaluation-criteria",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def create_evaluation_criteria(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Create evaluation criteria for an agent.

        Args:
            agent_id: Agent identifier.
            body: Criteria definition.

        Returns:
            The created evaluation criteria.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/agents/{agent_id}/evaluation-criteria",
                json=body,
            ),
        )

    async def get_evaluation_criteria(self, criteria_id: str) -> dict[str, Any]:
        """Get evaluation criteria by ID.

        Args:
            criteria_id: Evaluation criteria identifier.

        Returns:
            Evaluation criteria details.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}",
            ),
        )

    async def update_evaluation_criteria(
        self, criteria_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
            body: Fields to update.

        Returns:
            The updated evaluation criteria.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PATCH",
                f"/agents/evaluation-criteria/{criteria_id}",
                json=body,
            ),
        )

    async def delete_evaluation_criteria(self, criteria_id: str) -> None:
        """Delete evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
        """
        await self.request("DELETE", f"/agents/evaluation-criteria/{criteria_id}")

    async def get_evaluation_criteria_summary(self, criteria_id: str) -> dict[str, Any]:
        """Get the result summary for evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.

        Returns:
            Summary of evaluation results.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}/summary",
            ),
        )

    async def list_evaluation_results(
        self, criteria_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List evaluation results for criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation results.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}/results",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def create_evaluation_result(
        self, criteria_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Create a manual evaluation result.

        Args:
            criteria_id: Evaluation criteria identifier.
            body: Evaluation result payload.

        Returns:
            The created evaluation result.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/agents/evaluation-criteria/{criteria_id}/results",
                json=body,
            ),
        )

    async def list_compatible_runs(
        self, criteria_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List agent runs compatible with evaluation criteria.

        Args:
            criteria_id: Evaluation criteria identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of compatible runs.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/evaluation-criteria/{criteria_id}/compatible-runs",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def test_draft_evaluation(
        self, agent_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Test a draft evaluation criteria without persisting.

        Args:
            agent_id: Agent identifier.
            body: Draft evaluation criteria and test run.

        Returns:
            Test evaluation result.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/agents/{agent_id}/evaluation-criteria/test-draft",
                json=body,
            ),
        )

    async def list_agent_evaluation_results(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List all evaluation results for an agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation results with criteria.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/{agent_id}/evaluation-results",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def list_run_evaluation_results(
        self, agent_id: str, run_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List evaluation results for a specific agent run.

        Args:
            agent_id: Agent identifier.
            run_id: Run identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation results with criteria.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/{agent_id}/runs/{run_id}/evaluation-results",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def list_evaluation_runs(
        self, agent_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List evaluation run summaries for an agent.

        Args:
            agent_id: Agent identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated evaluation run summaries.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/agents/{agent_id}/evaluation-runs",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def get_non_manual_evaluation_summary(self, agent_id: str) -> dict[str, Any]:
        """Get the non-manual evaluation summary for an agent.

        Args:
            agent_id: Agent identifier.

        Returns:
            Summary of automated evaluation results.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/agents/evaluation-results/non-manual-summary",
                params={"agent_id": agent_id},
            ),
        )

    # ── Knowledge Bases ───────────────────────────────────────────────────────

    async def list_knowledge_bases(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        sort: str = "created_at",
        order: str = "desc",
    ) -> dict[str, Any]:
        """List knowledge bases.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (``"asc"`` or ``"desc"``).

        Returns:
            Paginated list of knowledge bases.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/knowledge_bases",
                params=_strip_none(
                    {"page": page, "limit": limit, "sort": sort, "order": order}
                ),
            ),
        )

    async def create_knowledge_base(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a knowledge base.

        Args:
            body: Knowledge base creation payload.

        Returns:
            The created knowledge base.
        """
        return cast(
            dict[str, Any], await self.request("POST", "/knowledge_bases", json=body)
        )

    async def get_knowledge_base(self, knowledge_base_id: str) -> dict[str, Any]:
        """Get a knowledge base by ID.

        Args:
            knowledge_base_id: Knowledge base identifier.

        Returns:
            Knowledge base details.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/knowledge_bases/{knowledge_base_id}",
            ),
        )

    async def update_knowledge_base(
        self, knowledge_base_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a knowledge base.

        Args:
            knowledge_base_id: Knowledge base identifier.
            body: Fields to update.

        Returns:
            The updated knowledge base.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PUT",
                f"/knowledge_bases/{knowledge_base_id}",
                json=body,
            ),
        )

    async def delete_knowledge_base(self, knowledge_base_id: str) -> None:
        """Delete a knowledge base.

        Args:
            knowledge_base_id: Knowledge base identifier.
        """
        await self.request("DELETE", f"/knowledge_bases/{knowledge_base_id}")

    # ── Memory Banks ──────────────────────────────────────────────────────────

    async def list_memory_banks(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        sort: str = "created_at",
        order: str = "desc",
    ) -> dict[str, Any]:
        """List memory banks.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (``"asc"`` or ``"desc"``).

        Returns:
            Paginated list of memory banks.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/memory_banks",
                params=_strip_none(
                    {"page": page, "limit": limit, "sort": sort, "order": order}
                ),
            ),
        )

    async def create_memory_bank(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a memory bank.

        Args:
            body: Memory bank creation payload (name, type, config, etc.).

        Returns:
            The created memory bank.
        """
        return cast(
            dict[str, Any], await self.request("POST", "/memory_banks", json=body)
        )

    async def get_memory_bank(self, memory_bank_id: str) -> dict[str, Any]:
        """Get a memory bank by ID.

        Args:
            memory_bank_id: Memory bank identifier.

        Returns:
            Memory bank details.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/memory_banks/{memory_bank_id}",
            ),
        )

    async def update_memory_bank(
        self, memory_bank_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
            body: Fields to update.

        Returns:
            The updated memory bank.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PUT",
                f"/memory_banks/{memory_bank_id}",
                json=body,
            ),
        )

    async def delete_memory_bank(self, memory_bank_id: str) -> None:
        """Delete a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
        """
        await self.request("DELETE", f"/memory_banks/{memory_bank_id}")

    async def get_agents_using_memory_bank(self, memory_bank_id: str) -> JSONValue:
        """Get agents that use a specific memory bank.

        Args:
            memory_bank_id: Memory bank identifier.

        Returns:
            List of agents using this memory bank.
        """
        return await self.request("GET", f"/memory_banks/{memory_bank_id}/agents")

    async def get_memory_bank_stats(self, memory_bank_id: str) -> JSONValue:
        """Get statistics for a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.

        Returns:
            Memory bank statistics.
        """
        return await self.request("GET", f"/memory_banks/{memory_bank_id}/stats")

    async def compact_memory_bank(self, memory_bank_id: str) -> None:
        """Trigger compaction of a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
        """
        await self.request("POST", f"/memory_banks/{memory_bank_id}/compact")

    async def delete_memory_bank_source(self, memory_bank_id: str) -> None:
        """Delete the source backing a memory bank.

        Args:
            memory_bank_id: Memory bank identifier.
        """
        await self.request("DELETE", f"/memory_banks/{memory_bank_id}/source")

    async def test_memory_bank_compaction(
        self, memory_bank_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Test compaction of a memory bank without applying.

        Args:
            memory_bank_id: Memory bank identifier.
            body: Test compaction parameters.

        Returns:
            Compaction test result.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/memory_banks/{memory_bank_id}/test-compaction",
                json=body,
            ),
        )

    async def test_compaction_prompt_standalone(
        self, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Test a compaction prompt without an existing memory bank.

        Args:
            body: Standalone test compaction parameters.

        Returns:
            Compaction test result.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/memory_banks/test-compaction",
                json=body,
            ),
        )

    async def list_memory_bank_templates(self) -> JSONValue:
        """List available memory bank templates.

        Returns:
            Available templates.
        """
        return await self.request("GET", "/memory_banks/templates")

    async def generate_memory_bank_config(self, body: dict[str, Any]) -> dict[str, Any]:
        """Use the AI assistant to generate memory bank configuration.

        Args:
            body: Prompt and context for config generation.

        Returns:
            Generated memory bank configuration.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/memory_banks/ai-assistant",
                json=body,
            ),
        )

    async def get_memory_bank_ai_last_conversation(self) -> dict[str, Any]:
        """Get the last AI assistant conversation for memory banks.

        Returns:
            Last conversation with the memory bank AI assistant.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/memory_banks/ai-assistant/last-conversation",
            ),
        )

    async def accept_memory_bank_ai_suggestion(
        self, conversation_id: str, body: dict[str, Any]
    ) -> JSONValue:
        """Accept an AI assistant suggestion for a memory bank.

        Args:
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Acceptance result.
        """
        return await self.request(
            "PATCH",
            f"/memory_banks/ai-assistant/{conversation_id}",
            json=body,
        )

    # ── Sources (additional) ──────────────────────────────────────────────────

    async def create_source(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a new source.

        Args:
            body: Source creation payload.

        Returns:
            The created source.
        """
        return cast(dict[str, Any], await self.request("POST", "/sources", json=body))

    async def get_source(self, source_id: str) -> dict[str, Any]:
        """Get a source by ID.

        Args:
            source_id: Source identifier.

        Returns:
            Source details.
        """
        return cast(dict[str, Any], await self.request("GET", f"/sources/{source_id}"))

    async def update_source(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a source.

        Args:
            source_id: Source identifier.
            body: Fields to update.

        Returns:
            The updated source.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PUT",
                f"/sources/{source_id}",
                json=body,
            ),
        )

    async def delete_source(self, source_id: str) -> None:
        """Delete a source.

        Args:
            source_id: Source identifier.
        """
        await self.request("DELETE", f"/sources/{source_id}")

    async def upload_inline_text_to_source(
        self, source_connection_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Upload inline text content to a source connection.

        Args:
            source_connection_id: Source connection identifier.
            body: Inline text payload with title and content.

        Returns:
            Upload response details.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/sources/{source_connection_id}",
                json=body,
            ),
        )

    # ── Source Exports ────────────────────────────────────────────────────────

    async def list_source_exports(
        self, source_id: str, *, page: int = 1, limit: int = 50
    ) -> dict[str, Any]:
        """List exports for a source.

        Args:
            source_id: Source identifier.
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of exports.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/sources/{source_id}/exports",
                params=_strip_none({"page": page, "limit": limit}),
            ),
        )

    async def create_source_export(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Create an export for a source.

        Args:
            source_id: Source identifier.
            body: Export configuration (format, filters, etc.).

        Returns:
            The created export.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/sources/{source_id}/exports",
                json=body,
            ),
        )

    async def get_source_export(self, source_id: str, export_id: str) -> dict[str, Any]:
        """Get details of a source export.

        Args:
            source_id: Source identifier.
            export_id: Export identifier.

        Returns:
            Export details.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/sources/{source_id}/exports/{export_id}",
            ),
        )

    async def cancel_source_export(
        self, source_id: str, export_id: str
    ) -> dict[str, Any]:
        """Cancel a source export.

        Args:
            source_id: Source identifier.
            export_id: Export identifier.

        Returns:
            The updated export.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/sources/{source_id}/exports/{export_id}/cancel",
            ),
        )

    async def delete_source_export(self, source_id: str, export_id: str) -> None:
        """Delete a source export.

        Args:
            source_id: Source identifier.
            export_id: Export identifier.
        """
        await self.request("DELETE", f"/sources/{source_id}/exports/{export_id}")

    async def download_source_export(
        self, source_id: str, export_id: str
    ) -> httpx.Response:
        """Download a completed source export.

        Returns a **streaming** response. The caller is responsible for
        consuming and closing the response::

            response = await client.download_source_export("src", "exp")
            async with response:
                async for chunk in response.aiter_bytes():
                    f.write(chunk)

        Args:
            source_id: Source identifier.
            export_id: Export identifier.

        Returns:
            A streaming ``httpx.Response``. Must be closed by the caller.
        """
        request = self._client.build_request(
            "GET",
            f"/sources/{source_id}/exports/{export_id}/download",
            headers=_merge_request_headers(options=self._options, request_headers=None),
        )
        response = await self._client.send(request, stream=True)
        _raise_for_status(response)
        return response

    async def estimate_source_export(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Estimate the size/cost of a source export.

        Args:
            source_id: Source identifier.
            body: Export estimation parameters.

        Returns:
            Export estimate.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/sources/{source_id}/exports/estimate",
                json=body,
            ),
        )

    # ── Source Embedding Migrations ───────────────────────────────────────────

    async def get_source_embedding_migration(self, source_id: str) -> dict[str, Any]:
        """Get the embedding migration status for a source.

        Args:
            source_id: Source identifier.

        Returns:
            Migration status.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                f"/sources/{source_id}/embedding-migration",
            ),
        )

    async def start_source_embedding_migration(
        self, source_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Start an embedding migration for a source.

        Args:
            source_id: Source identifier.
            body: Migration configuration.

        Returns:
            The started migration.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/sources/{source_id}/embedding-migration",
                json=body,
            ),
        )

    async def cancel_source_embedding_migration(self, source_id: str) -> dict[str, Any]:
        """Cancel an in-progress embedding migration for a source.

        Args:
            source_id: Source identifier.

        Returns:
            The cancelled migration.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/sources/{source_id}/embedding-migration/cancel",
            ),
        )

    # ── Content (additional) ──────────────────────────────────────────────────

    async def replace_content_with_inline_text(
        self, content_version_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Replace content with inline text.

        Args:
            content_version_id: Content version identifier.
            body: Inline text payload.

        Returns:
            Upload response.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PUT",
                f"/contents/{content_version_id}",
                json=body,
            ),
        )

    # ── Solutions ─────────────────────────────────────────────────────────────

    async def list_solutions(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        sort: str = "created_at",
        order: str = "desc",
    ) -> dict[str, Any]:
        """List solutions.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            sort: Sort field.
            order: Sort order (``"asc"`` or ``"desc"``).

        Returns:
            Paginated list of solutions.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/solutions",
                params=_strip_none(
                    {"page": page, "limit": limit, "sort": sort, "order": order}
                ),
            ),
        )

    async def create_solution(self, body: dict[str, Any]) -> dict[str, Any]:
        """Create a solution.

        Args:
            body: Solution creation payload.

        Returns:
            The created solution.
        """
        return cast(dict[str, Any], await self.request("POST", "/solutions", json=body))

    async def get_solution(self, solution_id: str) -> dict[str, Any]:
        """Get a solution by ID.

        Args:
            solution_id: Solution identifier.

        Returns:
            Solution details.
        """
        return cast(
            dict[str, Any], await self.request("GET", f"/solutions/{solution_id}")
        )

    async def update_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a solution.

        Args:
            solution_id: Solution identifier.
            body: Fields to update.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "PATCH",
                f"/solutions/{solution_id}",
                json=body,
            ),
        )

    async def delete_solution(self, solution_id: str) -> None:
        """Delete a solution.

        Args:
            solution_id: Solution identifier.
        """
        await self.request("DELETE", f"/solutions/{solution_id}")

    async def link_agents_to_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Link agents to a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to link.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/agents",
                json=body,
            ),
        )

    async def unlink_agents_from_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Unlink agents from a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to unlink.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "DELETE",
                f"/solutions/{solution_id}/agents",
                json=body,
            ),
        )

    async def link_knowledge_bases_to_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Link knowledge bases to a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to link.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/knowledge-bases",
                json=body,
            ),
        )

    async def unlink_knowledge_bases_from_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Unlink knowledge bases from a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to unlink.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "DELETE",
                f"/solutions/{solution_id}/knowledge-bases",
                json=body,
            ),
        )

    async def link_source_connections_to_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Link source connections to a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to link.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/source-connections",
                json=body,
            ),
        )

    async def unlink_source_connections_from_solution(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Unlink source connections from a solution.

        Args:
            solution_id: Solution identifier.
            body: Resource IDs to unlink.

        Returns:
            The updated solution.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "DELETE",
                f"/solutions/{solution_id}/source-connections",
                json=body,
            ),
        )

    async def list_solution_conversations(
        self, solution_id: str
    ) -> list[dict[str, Any]]:
        """List AI assistant conversations for a solution.

        Args:
            solution_id: Solution identifier.

        Returns:
            List of conversations.
        """
        return cast(
            list[dict[str, Any]],
            await self.request(
                "GET",
                f"/solutions/{solution_id}/conversations",
            ),
        )

    async def add_solution_conversation_turn(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Add a turn to a solution AI conversation.

        Args:
            solution_id: Solution identifier.
            body: Conversation turn payload.

        Returns:
            The conversation response.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/conversations",
                json=body,
            ),
        )

    async def mark_solution_conversation_turn(
        self, solution_id: str, conversation_id: str, body: dict[str, Any]
    ) -> None:
        """Mark a solution conversation turn as accepted or rejected.

        Args:
            solution_id: Solution identifier.
            conversation_id: Conversation identifier.
            body: Acceptance/rejection payload.
        """
        await self.request(
            "PATCH",
            f"/solutions/{solution_id}/conversations/{conversation_id}",
            json=body,
        )

    async def generate_solution_ai_plan(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate a solution plan.

        Args:
            solution_id: Solution identifier.
            body: Prompt and context.

        Returns:
            Generated plan with proposed actions.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/generate",
                json=body,
            ),
        )

    async def generate_solution_ai_knowledge_base(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate a knowledge base plan for a solution.

        Args:
            solution_id: Solution identifier.
            body: Prompt and context.

        Returns:
            Generated knowledge base plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/knowledge-base",
                json=body,
            ),
        )

    async def generate_solution_ai_source(
        self, solution_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Use the AI assistant to generate a source plan for a solution.

        Args:
            solution_id: Solution identifier.
            body: Prompt and context.

        Returns:
            Generated source plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/source",
                json=body,
            ),
        )

    async def accept_solution_ai_plan(
        self, solution_id: str, conversation_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Accept an AI-generated solution plan.

        Args:
            solution_id: Solution identifier.
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Result of applying the plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/solutions/{solution_id}/ai-assistant/{conversation_id}/accept",
                json=body,
            ),
        )

    async def decline_solution_ai_plan(
        self, solution_id: str, conversation_id: str
    ) -> None:
        """Decline an AI-generated solution plan.

        Args:
            solution_id: Solution identifier.
            conversation_id: Conversation identifier.
        """
        await self.request(
            "POST",
            f"/solutions/{solution_id}/ai-assistant/{conversation_id}/decline",
        )

    # ── Governance AI ─────────────────────────────────────────────────────────

    async def generate_governance_ai_plan(self, body: dict[str, Any]) -> dict[str, Any]:
        """Use the AI assistant to generate a governance plan.

        Args:
            body: Prompt and context for governance policy management.

        Returns:
            Generated governance plan with proposed actions.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/governance/ai-assistant",
                json=body,
            ),
        )

    async def list_governance_ai_conversations(self) -> list[dict[str, Any]]:
        """List governance AI assistant conversations.

        Returns:
            List of governance conversations.
        """
        return cast(
            list[dict[str, Any]],
            await self.request(
                "GET",
                "/governance/ai-assistant/conversations",
            ),
        )

    async def accept_governance_ai_plan(self, conversation_id: str) -> dict[str, Any]:
        """Accept an AI-generated governance plan.

        Args:
            conversation_id: Conversation identifier.

        Returns:
            Result of applying the governance plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/governance/ai-assistant/{conversation_id}/accept",
            ),
        )

    async def decline_governance_ai_plan(self, conversation_id: str) -> None:
        """Decline an AI-generated governance plan.

        Args:
            conversation_id: Conversation identifier.
        """
        await self.request(
            "POST",
            f"/governance/ai-assistant/{conversation_id}/decline",
        )

    # ── Alerts ────────────────────────────────────────────────────────────────

    async def list_alerts(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        status: str | None = None,
        severity: str | None = None,
    ) -> JSONValue:
        """List alerts.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.
            status: Filter by alert status.
            severity: Filter by severity.

        Returns:
            Paginated list of alerts.
        """
        return await self.request(
            "GET",
            "/alerts",
            params=_strip_none(
                {"page": page, "limit": limit, "status": status, "severity": severity}
            ),
        )

    async def get_alert(self, alert_id: str) -> JSONValue:
        """Get an alert by ID.

        Args:
            alert_id: Alert identifier.

        Returns:
            Alert details.
        """
        return await self.request("GET", f"/alerts/{alert_id}")

    async def change_alert_status(
        self, alert_id: str, body: dict[str, Any]
    ) -> JSONValue:
        """Change the status of an alert.

        Args:
            alert_id: Alert identifier.
            body: New status payload.

        Returns:
            Updated alert.
        """
        return await self.request("POST", f"/alerts/{alert_id}/status", json=body)

    async def add_alert_comment(self, alert_id: str, body: dict[str, Any]) -> JSONValue:
        """Add a comment to an alert.

        Args:
            alert_id: Alert identifier.
            body: Comment payload.

        Returns:
            Comment result.
        """
        return await self.request("POST", f"/alerts/{alert_id}/comments", json=body)

    async def subscribe_to_alert(self, alert_id: str) -> JSONValue:
        """Subscribe to an alert.

        Args:
            alert_id: Alert identifier.

        Returns:
            Subscription result.
        """
        return await self.request("POST", f"/alerts/{alert_id}/subscribe")

    async def unsubscribe_from_alert(self, alert_id: str) -> JSONValue:
        """Unsubscribe from an alert.

        Args:
            alert_id: Alert identifier.

        Returns:
            Unsubscription result.
        """
        return await self.request("POST", f"/alerts/{alert_id}/unsubscribe")

    # ── Alert Configs ─────────────────────────────────────────────────────────

    async def list_alert_configs(self, *, page: int = 1, limit: int = 50) -> JSONValue:
        """List alert configurations.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of alert configurations.
        """
        return await self.request(
            "GET",
            "/alerts/configs",
            params=_strip_none({"page": page, "limit": limit}),
        )

    async def create_alert_config(self, body: dict[str, Any]) -> JSONValue:
        """Create an alert configuration.

        Args:
            body: Alert config creation payload.

        Returns:
            The created alert configuration.
        """
        return await self.request("POST", "/alerts/configs", json=body)

    async def get_alert_config(self, config_id: str) -> JSONValue:
        """Get an alert configuration by ID.

        Args:
            config_id: Alert config identifier.

        Returns:
            Alert configuration details.
        """
        return await self.request("GET", f"/alerts/configs/{config_id}")

    async def update_alert_config(
        self, config_id: str, body: dict[str, Any]
    ) -> JSONValue:
        """Update an alert configuration.

        Args:
            config_id: Alert config identifier.
            body: Fields to update.

        Returns:
            The updated alert configuration.
        """
        return await self.request("PATCH", f"/alerts/configs/{config_id}", json=body)

    async def delete_alert_config(self, config_id: str) -> None:
        """Delete an alert configuration.

        Args:
            config_id: Alert config identifier.
        """
        await self.request("DELETE", f"/alerts/configs/{config_id}")

    # ── Alert Preferences ─────────────────────────────────────────────────────

    async def list_organization_alert_preferences(self) -> dict[str, Any]:
        """List organization alert preferences.

        Returns:
            Alert preferences for the organization.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/alerts/organization-preferences/list",
            ),
        )

    async def update_organization_alert_preference(
        self, organization_id: str, alert_type: str, body: dict[str, Any]
    ) -> JSONValue:
        """Update an organization alert preference.

        Args:
            organization_id: Organization identifier.
            alert_type: Alert type to configure.
            body: Preference update payload.

        Returns:
            Updated preference.
        """
        return await self.request(
            "PATCH",
            f"/alerts/organization-preferences/{organization_id}/{alert_type}",
            json=body,
        )

    # ── Model Alerts ──────────────────────────────────────────────────────────

    async def list_model_alerts(self, *, page: int = 1, limit: int = 50) -> JSONValue:
        """List model alerts.

        Args:
            page: Page number (1-indexed).
            limit: Items per page.

        Returns:
            Paginated list of model alerts.
        """
        return await self.request(
            "GET",
            "/models/alerts",
            params=_strip_none({"page": page, "limit": limit}),
        )

    async def mark_all_model_alerts_read(self) -> None:
        """Mark all model alerts as read for the current account."""
        await self.request("POST", "/models/alerts/mark-all-read")

    async def get_unread_model_alert_count(self) -> JSONValue:
        """Get the count of unread model alerts.

        Returns:
            Unread alert count.
        """
        return await self.request("GET", "/models/alerts/unread-count")

    async def mark_model_alert_read(self, alert_id: str) -> None:
        """Mark a model alert as read.

        Args:
            alert_id: Alert identifier.
        """
        await self.request("PATCH", f"/models/alerts/{alert_id}/read")

    # ── Models ────────────────────────────────────────────────────────────────

    async def get_model_recommendations(self, model_id: str) -> JSONValue:
        """Get recommendations for a model.

        Args:
            model_id: Model identifier.

        Returns:
            Model recommendations.
        """
        return await self.request("GET", f"/models/{model_id}/recommendations")

    # ── Search ────────────────────────────────────────────────────────────────

    async def search(
        self,
        *,
        query: str,
        limit: int = 10,
        entity_type: str | None = None,
    ) -> JSONValue:
        """Search across the Seclai platform.

        Args:
            query: Search query string.
            limit: Maximum results to return.
            entity_type: Optional entity type filter.

        Returns:
            Search results.
        """
        return await self.request(
            "GET",
            "/search",
            params=_strip_none(
                {"query": query, "limit": limit, "entity_type": entity_type}
            ),
        )

    # ── Top-level AI Assistant ─────────────────────────────────────────────────

    async def submit_ai_feedback(self, body: dict[str, Any]) -> dict[str, Any]:
        """Submit feedback to the AI assistant.

        Args:
            body: Feedback payload.

        Returns:
            Feedback response.
        """
        return cast(
            dict[str, Any],
            await self.request("POST", "/ai-assistant/feedback", json=body),
        )

    async def ai_assistant_knowledge_base(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a knowledge base plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/ai-assistant/knowledge-base",
                json=body,
            ),
        )

    async def ai_assistant_source(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a source plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/ai-assistant/source",
                json=body,
            ),
        )

    async def ai_assistant_solution(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a solution plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/ai-assistant/solution",
                json=body,
            ),
        )

    async def ai_assistant_memory_bank(self, body: dict[str, Any]) -> dict[str, Any]:
        """Generate a memory bank plan via the top-level AI assistant.

        Args:
            body: Prompt and context.

        Returns:
            Generated plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                "/ai-assistant/memory-bank",
                json=body,
            ),
        )

    async def get_ai_assistant_memory_bank_history(self) -> dict[str, Any]:
        """Get the last AI assistant memory bank conversation.

        Returns:
            Last conversation.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "GET",
                "/ai-assistant/memory-bank/last-conversation",
            ),
        )

    async def accept_ai_assistant_plan(
        self, conversation_id: str, body: dict[str, Any]
    ) -> dict[str, Any]:
        """Accept a top-level AI assistant plan.

        Args:
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Result of applying the plan.
        """
        return cast(
            dict[str, Any],
            await self.request(
                "POST",
                f"/ai-assistant/{conversation_id}/accept",
                json=body,
            ),
        )

    async def decline_ai_assistant_plan(self, conversation_id: str) -> None:
        """Decline a top-level AI assistant plan.

        Args:
            conversation_id: Conversation identifier.
        """
        await self.request("POST", f"/ai-assistant/{conversation_id}/decline")

    async def accept_ai_memory_bank_suggestion(
        self, conversation_id: str, body: dict[str, Any]
    ) -> JSONValue:
        """Accept a top-level AI memory bank suggestion.

        Args:
            conversation_id: Conversation identifier.
            body: Acceptance payload.

        Returns:
            Acceptance result.
        """
        return await self.request(
            "PATCH",
            f"/ai-assistant/memory-bank/{conversation_id}",
            json=body,
        )

    # ── Pagination helper ─────────────────────────────────────────────────────

    async def paginate(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        limit: int = 50,
        items_key: str = "data",
    ) -> AsyncGenerator[dict[str, Any]]:
        """Auto-paginate a list endpoint, yielding items lazily.

        Fetches pages sequentially until a page returns fewer items than ``limit``
        or the items list is empty.  Use ``async for item in client.paginate(...):``
        to iterate.

        Args:
            method: HTTP method (typically ``"GET"``).
            path: API path.
            params: Extra query parameters (``page`` and ``limit`` are managed automatically).
            limit: Items per page.
            items_key: JSON key containing the list of items (default ``"data"``).

        Yields:
            Individual items from each page.
        """
        page = 1
        base_params = dict(params) if params else {}
        while True:
            base_params["page"] = page
            base_params["limit"] = limit
            result = await self.request(method, path, params=base_params)
            if not isinstance(result, dict):
                break
            items = result.get(items_key, [])
            if not isinstance(items, list):
                break
            for item in items:
                yield cast(dict[str, Any], item)
            if len(items) < limit:
                break
            page += 1

    # ── High-level Abstractions ───────────────────────────────────────────────

    async def run_agent_and_poll(
        self,
        agent_id: str,
        body: AgentRunRequest,
        *,
        poll_interval: float = 2.0,
        include_step_outputs: bool = False,
    ) -> AgentRunResponse:
        """Run an agent and poll until it reaches a terminal status.

        Starts the agent run and then repeatedly polls ``get_agent_run`` until
        the status is ``"completed"`` or ``"failed"``.

        Args:
            agent_id: Agent identifier.
            body: Agent run request payload.
            poll_interval: Seconds between poll attempts (default 2.0).
            include_step_outputs: Include per-step outputs when polling.

        Returns:
            The final agent run (completed or failed).

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        import asyncio

        run = await self.run_agent(agent_id, body)
        while run.status not in ("completed", "failed"):
            await asyncio.sleep(poll_interval)
            run = await self.get_agent_run(
                run.run_id, include_step_outputs=include_step_outputs
            )
        return run

    async def run_streaming_agent(
        self,
        agent_id: str,
        body: AgentRunStreamRequest,
        *,
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> AsyncGenerator[tuple[str, dict[str, Any]]]:
        """Run an agent via SSE streaming and yield events as they arrive.

        Use ``async for event_type, data in client.run_streaming_agent(...)`` to
        process events lazily without buffering the entire stream.

        Args:
            agent_id: Agent identifier.
            body: Streaming agent run request payload.
            timeout: Max time (seconds) to wait. Defaults to this client's timeout.
            headers: Optional extra headers.

        Yields:
            ``(event_type, parsed_data)`` tuples for each SSE event.

        Raises:
            SeclaiAPIStatusError: If the API returns a non-success status code.
            SeclaiStreamingError: If an error event is received.
            SeclaiError: If the stream times out.
        """
        import json as _json

        path = f"/agents/{agent_id}/runs/stream"
        merged_headers = await _merge_request_headers_async(
            options=self._options, request_headers=headers
        )
        merged_headers.setdefault("accept", "text/event-stream")
        timeout_seconds = self._options.timeout if timeout is None else timeout
        start = time.monotonic()

        try:
            async with self._client.stream(
                "POST",
                path,
                json=body,
                headers=merged_headers,
                timeout=timeout_seconds,
            ) as response:
                _raise_for_status(response)
                current_event: str | None = None
                data_lines: list[str] = []

                async for line in response.aiter_lines():
                    if time.monotonic() - start > timeout_seconds:
                        raise SeclaiError(
                            f"Timed out after {timeout_seconds}s waiting for streaming agent run."
                        )
                    if line == "":
                        if current_event and data_lines:
                            data = "\n".join(data_lines)
                            try:
                                parsed = cast(dict[str, Any], _json.loads(data))
                            except Exception:
                                parsed = {"raw": data}
                            if current_event == "error":
                                raise SeclaiStreamingError(
                                    parsed.get("message", data),
                                    run_id=parsed.get("run_id"),
                                )
                            yield (current_event, parsed)
                        current_event = None
                        data_lines = []
                        continue
                    if line.startswith(":"):
                        continue
                    if line.startswith("event:"):
                        current_event = line[len("event:") :].strip() or None
                        continue
                    if line.startswith("data:"):
                        data_lines.append(line[len("data:") :].lstrip())
                        continue

                if current_event and data_lines:
                    data = "\n".join(data_lines)
                    try:
                        parsed = cast(dict[str, Any], _json.loads(data))
                    except Exception:
                        parsed = {"raw": data}
                    if current_event == "error":
                        raise SeclaiStreamingError(
                            parsed.get("message", data),
                            run_id=parsed.get("run_id"),
                        )
                    yield (current_event, parsed)
        except httpx.TimeoutException as e:
            raise SeclaiError(
                f"Timed out after {timeout_seconds}s waiting for streaming agent run."
            ) from e
