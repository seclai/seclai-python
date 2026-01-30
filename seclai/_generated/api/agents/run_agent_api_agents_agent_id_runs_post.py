from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_request import AgentRunRequest
from ...models.agent_run_response import AgentRunResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    agent_id: str,
    *,
    body: AgentRunRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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
) -> AgentRunResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentRunResponse.from_dict(response.json())

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
) -> Response[AgentRunResponse | HTTPValidationError]:
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
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `priority`: set true for latency-sensitive, user-facing work.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. All resources are scoped to the API key's account.

    Args:
        agent_id (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
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
) -> AgentRunResponse | HTTPValidationError | None:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `priority`: set true for latency-sensitive, user-facing work.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. All resources are scoped to the API key's account.

    Args:
        agent_id (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunRequest,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `priority`: set true for latency-sensitive, user-facing work.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. All resources are scoped to the API key's account.

    Args:
        agent_id (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunRequest,
) -> AgentRunResponse | HTTPValidationError | None:
    """Run an agent

     Start an agent run.

    An *agent* is an automated workflow that can monitor content from your sources, process it with AI,
    and trigger actions. This endpoint creates a new run and returns a `run_id` you can poll to retrieve
    status and output.

    When to use:
    - Use this endpoint for request/response style integrations where polling is acceptable.
    - Use `POST /agents/{agent_id}/runs/stream` if you need real-time progress via SSE.

    Key fields:
    - `priority`: set true for latency-sensitive, user-facing work.
    - `metadata`: a JSON object that becomes available to agent steps for string substitution.

    After starting:
    - Poll `GET /agents/runs/{run_id}` until `status` is `completed` or `failed`.
    - Use `include_step_outputs=true` to include per-step outputs, timing, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. All resources are scoped to the API key's account.

    Args:
        agent_id (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
        )
    ).parsed
