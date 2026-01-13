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
import os
from collections.abc import Mapping
from dataclasses import dataclass
from http import HTTPStatus
from io import BytesIO
from pathlib import Path
from typing import Any, BinaryIO, Self, TypedDict, cast

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

logger = logging.getLogger(__name__)


JSONValue = dict[str, "JSONValue"] | list["JSONValue"] | str | int | float | bool | None


class AgentRunStreamRequest(TypedDict):
    """Request body for streaming agent runs.

    This matches the API schema for POST /api/agents/{agent_id}/runs/stream.
    """

    input: str | None
    metadata: dict[str, JSONValue]


SECLAI_API_URL = os.getenv("SECLAI_API_URL", "https://seclai.com")


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
        super().__init__(
            message=message,
            status_code=status_code,
            method=method,
            url=url,
            response_text=response_text,
        )
        self.validation_error = validation_error


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
    """Resolved client configuration options."""

    api_key: str
    timeout: float
    api_key_header: str
    default_headers: Mapping[str, str]


def _build_default_headers(
    *,
    api_key: str,
    api_key_header: str,
    default_headers: Mapping[str, str] | None,
) -> dict[str, str]:
    """Build default request headers including API key auth and user-agent."""
    headers: dict[str, str] = {
        api_key_header: api_key,
        "user-agent": "seclai-python",
    }
    if default_headers:
        headers.update(default_headers)
    return headers


def _merge_request_headers(
    *,
    options: ClientOptions,
    request_headers: Mapping[str, str] | None,
) -> dict[str, str]:
    """Merge client default headers with per-request overrides."""
    merged = _build_default_headers(
        api_key=options.api_key,
        api_key_header=options.api_key_header,
        default_headers=options.default_headers,
    )
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

    This class centralizes API key resolution, option storage, and configuration of
    the generated OpenAPI client.
    """

    def __init__(
        self,
        *,
        api_key: str | None,
        timeout: float,
        api_key_header: str,
        default_headers: Mapping[str, str] | None,
    ) -> None:
        """Initialize shared client state.

        Args:
            api_key: API key used for authentication. If omitted, `SECLAI_API_KEY` is used.
            timeout: Request timeout (seconds).
            api_key_header: Header name to use for the API key.
            default_headers: Extra headers to include on every request.

        Raises:
            SeclaiConfigurationError: If no API key is provided and `SECLAI_API_KEY` is not set.
        """
        resolved_key = _resolve_api_key(api_key)
        self._options = ClientOptions(
            api_key=resolved_key,
            timeout=timeout,
            api_key_header=api_key_header,
            default_headers=default_headers or {},
        )

        self._generated_client_instance: GeneratedClient | None = None
        self._owns_generated_client = False

    @property
    def api_key(self) -> str:
        """Return the resolved API key used for authentication."""
        return self._options.api_key

    def _default_headers(self) -> dict[str, str]:
        """Build default request headers for the underlying HTTP clients.

        Returns:
            A header dictionary containing API key auth, user-agent, and any configured defaults.
        """
        return _build_default_headers(
            api_key=self._options.api_key,
            api_key_header=self._options.api_key_header,
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
            path: API path used (e.g. `"/api/sources/"`).
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
        timeout: float = 30.0,
        api_key_header: str = "x-api-key",
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Create a synchronous Seclai client.

        Args:
            api_key: API key used for authentication. If omitted, `SECLAI_API_KEY` is used.
            timeout: Request timeout (seconds).
            api_key_header: Header name to use for the API key.
            default_headers: Extra headers to include on every request.
            http_client: Optional pre-configured `httpx.Client` to use.

        Raises:
            SeclaiConfigurationError: If no API key is provided and `SECLAI_API_KEY` is not set.
        """
        super().__init__(
            api_key=api_key,
            timeout=timeout,
            api_key_header=api_key_header,
            default_headers=default_headers,
        )
        self._client = http_client or httpx.Client(
            base_url=SECLAI_API_URL,
            timeout=self._options.timeout,
            headers=self._default_headers(),
        )
        self._owns_client = http_client is None

    def close(self) -> None:
        """Close underlying HTTP resources owned by this client."""
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
            path: Request path relative to `SECLAI_API_URL` (e.g. `"/api/sources/"`).
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

        path = f"/api/agents/{agent_id}/runs"
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

        This uses POST /api/agents/{agent_id}/runs/stream and consumes Server-Sent Events (SSE).
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

        path = f"/api/agents/{agent_id}/runs/stream"

        merged_headers = _merge_request_headers(options=self._options, request_headers=headers)
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

        path = f"/api/agents/{agent_id}/runs"
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

    def get_agent_run(self, agent_id: str, run_id: str) -> AgentRunResponse:
        """Get details of a specific agent run.

        Fetches the current state and details for a previously created run.

        Args:
            agent_id: Agent identifier.
            run_id: Run identifier.

        Returns:
            Agent run details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.get_agent_run_api_agents_agent_id_runs_run_id_get import (
            sync_detailed,
        )

        path = f"/api/agents/{agent_id}/runs/{run_id}"
        response = sync_detailed(
            agent_id=agent_id, run_id=run_id, client=self._generated_client()
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

    def delete_agent_run(self, agent_id: str, run_id: str) -> AgentRunResponse:
        """Cancel an agent run.

        Requests cancellation of a run and returns the updated run record. Note: cancellation will not stop the currently executing step, but will prevent any further steps from running.

        Args:
            agent_id: Agent identifier.
            run_id: Run identifier.

        Returns:
            The updated agent run.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.delete_agent_run_api_agents_agent_id_runs_run_id_delete import (
            sync_detailed,
        )

        path = f"/api/agents/{agent_id}/runs/{run_id}"
        response = sync_detailed(
            agent_id=agent_id, run_id=run_id, client=self._generated_client()
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

        path = f"/api/contents/{source_connection_content_version}"
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

        path = f"/api/contents/{source_connection_content_version}"
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

        path = f"/api/contents/{source_connection_content_version}/embeddings"
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

        path = "/api/sources/"
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
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> FileUploadResponse:
        """Upload a file to a specific source connection.

        Sends a file to be ingested under the given source connection.

        Notes:
            - If `file` is a path or `bytes`, this method creates an in-memory/file handle and
              closes it before returning.
            - If `file` is a file-like object, the caller owns its lifecycle.

        Args:
            source_connection_id: Source connection identifier.
            file: File payload. Accepts raw bytes, a filesystem path, or a binary file-like.
            title: Optional title for the uploaded file.
            file_name: Optional filename to send when `file` is bytes or a file-like.
            mime_type: Optional MIME type to send.

        Returns:
            Upload response details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.sources.upload_file_to_source_api_sources_source_connection_id_upload_post import (
            sync_detailed,
        )
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
                created_payload = file_path.open("rb")
                upload_file = File(
                    payload=created_payload,
                    file_name=file_name or file_path.name,
                    mime_type=mime_type,
                )
            elif isinstance(file, bytes):
                created_payload = BytesIO(file)
                upload_file = File(
                    payload=created_payload, file_name=file_name, mime_type=mime_type
                )
            else:
                upload_file = File(
                    payload=file, file_name=file_name, mime_type=mime_type
                )

            body = BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost(
                file=upload_file,
                title=UNSET if title is None else title,
            )
            endpoint_path = f"/api/sources/{source_connection_id}/upload"
            response = sync_detailed(
                source_connection_id=source_connection_id,
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
        timeout: float = 30.0,
        api_key_header: str = "x-api-key",
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create an asynchronous Seclai client.

        Args:
            api_key: API key used for authentication. If omitted, `SECLAI_API_KEY` is used.
            timeout: Request timeout (seconds).
            api_key_header: Header name to use for the API key.
            default_headers: Extra headers to include on every request.
            http_client: Optional pre-configured `httpx.AsyncClient` to use.

        Raises:
            SeclaiConfigurationError: If no API key is provided and `SECLAI_API_KEY` is not set.
        """
        super().__init__(
            api_key=api_key,
            timeout=timeout,
            api_key_header=api_key_header,
            default_headers=default_headers,
        )
        self._client = http_client or httpx.AsyncClient(
            base_url=SECLAI_API_URL,
            timeout=self._options.timeout,
            headers=self._default_headers(),
        )
        self._owns_client = http_client is None

    async def aclose(self) -> None:
        """Close underlying HTTP resources owned by this client."""
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
            path: Request path relative to `SECLAI_API_URL` (e.g. `"/api/sources/"`).
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

        path = f"/api/agents/{agent_id}/runs"
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

        This uses POST /api/agents/{agent_id}/runs/stream and consumes Server-Sent Events (SSE).
        The method returns when an `event: done` message is received.
        """
        import json as _json
        import time as _time

        path = f"/api/agents/{agent_id}/runs/stream"

        merged_headers = _merge_request_headers(options=self._options, request_headers=headers)
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

        path = f"/api/agents/{agent_id}/runs"
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

    async def get_agent_run(self, agent_id: str, run_id: str) -> AgentRunResponse:
        """Get details of a specific agent run.

        Fetches the current state and details for a previously created run.

        Args:
            agent_id: Agent identifier.
            run_id: Run identifier.

        Returns:
            Agent run details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.get_agent_run_api_agents_agent_id_runs_run_id_get import (
            asyncio_detailed,
        )

        path = f"/api/agents/{agent_id}/runs/{run_id}"
        response = await asyncio_detailed(
            agent_id=agent_id,
            run_id=run_id,
            client=self._generated_client(),
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

    async def delete_agent_run(self, agent_id: str, run_id: str) -> AgentRunResponse:
        """Cancel an agent run.

        Requests cancellation of a run and returns the updated run record.

        Args:
            agent_id: Agent identifier.
            run_id: Run identifier.

        Returns:
            The updated agent run.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.agents.delete_agent_run_api_agents_agent_id_runs_run_id_delete import (
            asyncio_detailed,
        )

        path = f"/api/agents/{agent_id}/runs/{run_id}"
        response = await asyncio_detailed(
            agent_id=agent_id,
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

        path = f"/api/contents/{source_connection_content_version}"
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

        path = f"/api/contents/{source_connection_content_version}"
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

        path = f"/api/contents/{source_connection_content_version}/embeddings"
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

        path = "/api/sources/"
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
        file_name: str | None = None,
        mime_type: str | None = None,
    ) -> FileUploadResponse:
        """Upload a file to a specific source connection.

        Sends a file to be ingested under the given source connection.

        Notes:
            - If `file` is a path or `bytes`, this method creates an in-memory/file handle and
              closes it before returning.
            - If `file` is a file-like object, the caller owns its lifecycle.

        Args:
            source_connection_id: Source connection identifier.
            file: File payload. Accepts raw bytes, a filesystem path, or a binary file-like.
            title: Optional title for the uploaded file.
            file_name: Optional filename to send when `file` is bytes or a file-like.
            mime_type: Optional MIME type to send.

        Returns:
            Upload response details.

        Raises:
            SeclaiAPIValidationError: If the API returns a validation error.
            SeclaiAPIStatusError: If the API returns a non-success status code.
        """
        from seclai._generated.api.sources.upload_file_to_source_api_sources_source_connection_id_upload_post import (
            asyncio_detailed,
        )
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
                created_payload = file_path.open("rb")
                upload_file = File(
                    payload=created_payload,
                    file_name=file_name or file_path.name,
                    mime_type=mime_type,
                )
            elif isinstance(file, bytes):
                created_payload = BytesIO(file)
                upload_file = File(
                    payload=created_payload, file_name=file_name, mime_type=mime_type
                )
            else:
                upload_file = File(
                    payload=file, file_name=file_name, mime_type=mime_type
                )

            body = BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost(
                file=upload_file,
                title=UNSET if title is None else title,
            )
            endpoint_path = f"/api/sources/{source_connection_id}/upload"
            response = await asyncio_detailed(
                source_connection_id=source_connection_id,
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
