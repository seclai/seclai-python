from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_stream_request import AgentRunStreamRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: AgentRunStreamRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/runs/stream".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunStreamRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Run an agent (stream events)

     Start a **priority** agent run and stream run events using Server-Sent Events (SSE).

    This is the best option for interactive UIs where you want progress updates as the run executes.

    How it works:
    - The first `init` event contains an `AgentRunResponse` snapshot, including the `run_id`.
    - Subsequent events are forwarded from the run event stream (status changes, step events, etc).
    - The final `done` event contains the terminal snapshot (including `output` and `credits` when
    available).

    Input options (for `dynamic_input` triggers):
    - `input`: text input passed directly.
    - `input_upload_id`: reference a file uploaded via `POST /agents/{agent_id}/upload-input` (mutually
    exclusive with `input`).

    Client guidance:
    - Keep the connection open and handle keepalive comments.
    - On `timeout` or `error`, the payload includes `run_id` so clients can resume by polling `GET
    /agents/runs/{run_id}`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunStreamRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Run an agent (stream events)

     Start a **priority** agent run and stream run events using Server-Sent Events (SSE).

    This is the best option for interactive UIs where you want progress updates as the run executes.

    How it works:
    - The first `init` event contains an `AgentRunResponse` snapshot, including the `run_id`.
    - Subsequent events are forwarded from the run event stream (status changes, step events, etc).
    - The final `done` event contains the terminal snapshot (including `output` and `credits` when
    available).

    Input options (for `dynamic_input` triggers):
    - `input`: text input passed directly.
    - `input_upload_id`: reference a file uploaded via `POST /agents/{agent_id}/upload-input` (mutually
    exclusive with `input`).

    Client guidance:
    - Keep the connection open and handle keepalive comments.
    - On `timeout` or `error`, the payload includes `run_id` so clients can resume by polling `GET
    /agents/runs/{run_id}`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunStreamRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Run an agent (stream events)

     Start a **priority** agent run and stream run events using Server-Sent Events (SSE).

    This is the best option for interactive UIs where you want progress updates as the run executes.

    How it works:
    - The first `init` event contains an `AgentRunResponse` snapshot, including the `run_id`.
    - Subsequent events are forwarded from the run event stream (status changes, step events, etc).
    - The final `done` event contains the terminal snapshot (including `output` and `credits` when
    available).

    Input options (for `dynamic_input` triggers):
    - `input`: text input passed directly.
    - `input_upload_id`: reference a file uploaded via `POST /agents/{agent_id}/upload-input` (mutually
    exclusive with `input`).

    Client guidance:
    - Keep the connection open and handle keepalive comments.
    - On `timeout` or `error`, the payload includes `run_id` so clients can resume by polling `GET
    /agents/runs/{run_id}`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunStreamRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Run an agent (stream events)

     Start a **priority** agent run and stream run events using Server-Sent Events (SSE).

    This is the best option for interactive UIs where you want progress updates as the run executes.

    How it works:
    - The first `init` event contains an `AgentRunResponse` snapshot, including the `run_id`.
    - Subsequent events are forwarded from the run event stream (status changes, step events, etc).
    - The final `done` event contains the terminal snapshot (including `output` and `credits` when
    available).

    Input options (for `dynamic_input` triggers):
    - `input`: text input passed directly.
    - `input_upload_id`: reference a file uploaded via `POST /agents/{agent_id}/upload-input` (mutually
    exclusive with `input`).

    Client guidance:
    - Keep the connection open and handle keepalive comments.
    - On `timeout` or `error`, the payload includes `run_id` so clients can resume by polling `GET
    /agents/runs/{run_id}`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
