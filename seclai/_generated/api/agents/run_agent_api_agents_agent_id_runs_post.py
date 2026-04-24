from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_request import AgentRunRequest
from ...models.agent_run_response import AgentRunResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: AgentRunRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/runs".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentRunResponse | Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentRunResponse.from_dict(response.json())

        return response_200

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentRunResponse | Any | HTTPValidationError]:
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
    body: AgentRunRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentRunResponse | Any | HTTPValidationError]:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `input`: text input for agents with a `dynamic_input` trigger.
    - `input_upload_id`: alternatively, reference a file previously uploaded via `POST
    /agents/{agent_id}/upload-input` (mutually exclusive with `input`).
    - `priority`: set true for latency-sensitive, user-facing work. For agents with a `streaming_result`
    step, set `priority=true` to enable real-time token streaming; otherwise the run still proceeds, but
    without live token streaming.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | Any | HTTPValidationError]
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
    body: AgentRunRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentRunResponse | Any | HTTPValidationError | None:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `input`: text input for agents with a `dynamic_input` trigger.
    - `input_upload_id`: alternatively, reference a file previously uploaded via `POST
    /agents/{agent_id}/upload-input` (mutually exclusive with `input`).
    - `priority`: set true for latency-sensitive, user-facing work. For agents with a `streaming_result`
    step, set `priority=true` to enable real-time token streaming; otherwise the run still proceeds, but
    without live token streaming.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | Any | HTTPValidationError
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
    body: AgentRunRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentRunResponse | Any | HTTPValidationError]:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `input`: text input for agents with a `dynamic_input` trigger.
    - `input_upload_id`: alternatively, reference a file previously uploaded via `POST
    /agents/{agent_id}/upload-input` (mutually exclusive with `input`).
    - `priority`: set true for latency-sensitive, user-facing work. For agents with a `streaming_result`
    step, set `priority=true` to enable real-time token streaming; otherwise the run still proceeds, but
    without live token streaming.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | Any | HTTPValidationError]
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
    body: AgentRunRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentRunResponse | Any | HTTPValidationError | None:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `input`: text input for agents with a `dynamic_input` trigger.
    - `input_upload_id`: alternatively, reference a file previously uploaded via `POST
    /agents/{agent_id}/upload-input` (mutually exclusive with `input`).
    - `priority`: set true for latency-sensitive, user-facing work. For agents with a `streaming_result`
    step, set `priority=true` to enable real-time token streaming; otherwise the run still proceeds, but
    without live token streaming.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
