from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_caller_api_response import AgentCallerApiResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/callers".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[AgentCallerApiResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AgentCallerApiResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[AgentCallerApiResponse]]:
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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | list[AgentCallerApiResponse]]:
    """List agents that call this agent

     List the live agents that call this agent via a `call_agent` step. They must be disabled before this
    agent can be paused.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the agent must belong to the
    key's account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AgentCallerApiResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | list[AgentCallerApiResponse] | None:
    """List agents that call this agent

     List the live agents that call this agent via a `call_agent` step. They must be disabled before this
    agent can be paused.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the agent must belong to the
    key's account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AgentCallerApiResponse]
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | list[AgentCallerApiResponse]]:
    """List agents that call this agent

     List the live agents that call this agent via a `call_agent` step. They must be disabled before this
    agent can be paused.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the agent must belong to the
    key's account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AgentCallerApiResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | list[AgentCallerApiResponse] | None:
    """List agents that call this agent

     List the live agents that call this agent via a `call_agent` step. They must be disabled before this
    agent can be paused.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the agent must belong to the
    key's account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AgentCallerApiResponse]
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
