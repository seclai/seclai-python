from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_response import AgentRunResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    include_step_outputs: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_step_outputs"] = include_step_outputs

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/runs/{run_id}".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

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
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_step_outputs: bool | Unset = False,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Get an agent run

     Fetch the latest snapshot for an agent run created by `POST /agents/{agent_id}/runs` or `POST
    /agents/{agent_id}/runs/stream`.

    The response includes `status`, `error_count`, and `output` once the run completes. Use
    `include_step_outputs=true` to include per-step outputs, timing, durations, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access runs belonging to your account.

    Args:
        run_id (str):
        include_step_outputs (bool | Unset): If true, include per-step outputs with timing,
            durations, and credits. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        include_step_outputs=include_step_outputs,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_step_outputs: bool | Unset = False,
) -> AgentRunResponse | HTTPValidationError | None:
    """Get an agent run

     Fetch the latest snapshot for an agent run created by `POST /agents/{agent_id}/runs` or `POST
    /agents/{agent_id}/runs/stream`.

    The response includes `status`, `error_count`, and `output` once the run completes. Use
    `include_step_outputs=true` to include per-step outputs, timing, durations, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access runs belonging to your account.

    Args:
        run_id (str):
        include_step_outputs (bool | Unset): If true, include per-step outputs with timing,
            durations, and credits. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        include_step_outputs=include_step_outputs,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_step_outputs: bool | Unset = False,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Get an agent run

     Fetch the latest snapshot for an agent run created by `POST /agents/{agent_id}/runs` or `POST
    /agents/{agent_id}/runs/stream`.

    The response includes `status`, `error_count`, and `output` once the run completes. Use
    `include_step_outputs=true` to include per-step outputs, timing, durations, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access runs belonging to your account.

    Args:
        run_id (str):
        include_step_outputs (bool | Unset): If true, include per-step outputs with timing,
            durations, and credits. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        include_step_outputs=include_step_outputs,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_step_outputs: bool | Unset = False,
) -> AgentRunResponse | HTTPValidationError | None:
    """Get an agent run

     Fetch the latest snapshot for an agent run created by `POST /agents/{agent_id}/runs` or `POST
    /agents/{agent_id}/runs/stream`.

    The response includes `status`, `error_count`, and `output` once the run completes. Use
    `include_step_outputs=true` to include per-step outputs, timing, durations, and credits.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access runs belonging to your account.

    Args:
        run_id (str):
        include_step_outputs (bool | Unset): If true, include per-step outputs with timing,
            durations, and credits. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            include_step_outputs=include_step_outputs,
        )
    ).parsed
