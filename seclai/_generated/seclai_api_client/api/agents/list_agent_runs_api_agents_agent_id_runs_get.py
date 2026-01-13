from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_list_response import AgentRunListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/runs".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentRunListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentRunListResponse.from_dict(response.json())

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
) -> Response[AgentRunListResponse | HTTPValidationError]:
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
    page: int | Unset = 1,
    limit: int | Unset = 50,
) -> Response[AgentRunListResponse | HTTPValidationError]:
    """List Agent Runs

     List agent runs for an agent with pagination.

    Args:
        agent_id (str):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 50,
) -> AgentRunListResponse | HTTPValidationError | None:
    """List Agent Runs

     List agent runs for an agent with pagination.

    Args:
        agent_id (str):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunListResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 50,
) -> Response[AgentRunListResponse | HTTPValidationError]:
    """List Agent Runs

     List agent runs for an agent with pagination.

    Args:
        agent_id (str):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 50,
) -> AgentRunListResponse | HTTPValidationError | None:
    """List Agent Runs

     List agent runs for an agent with pagination.

    Args:
        agent_id (str):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed
