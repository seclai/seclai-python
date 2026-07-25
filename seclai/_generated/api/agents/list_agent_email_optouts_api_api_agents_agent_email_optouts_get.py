from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_email_opt_out_list_response import AgentEmailOptOutListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/agent-email-optouts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentEmailOptOutListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentEmailOptOutListResponse.from_dict(response.json())

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
) -> Response[AgentEmailOptOutListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentEmailOptOutListResponse | HTTPValidationError]:
    """List agent-email opt-outs

     List recipients who have opted out of this account's agent emails (filter to one agent via
    `agent_id`; account-wide opt-outs always apply). Paginated via `limit`/`offset`; returns the page
    plus the `total` count.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        agent_id (None | str | Unset): Filter to one agent (account-wide opt-outs still apply)
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentEmailOptOutListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> AgentEmailOptOutListResponse | HTTPValidationError | None:
    """List agent-email opt-outs

     List recipients who have opted out of this account's agent emails (filter to one agent via
    `agent_id`; account-wide opt-outs always apply). Paginated via `limit`/`offset`; returns the page
    plus the `total` count.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        agent_id (None | str | Unset): Filter to one agent (account-wide opt-outs still apply)
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentEmailOptOutListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentEmailOptOutListResponse | HTTPValidationError]:
    """List agent-email opt-outs

     List recipients who have opted out of this account's agent emails (filter to one agent via
    `agent_id`; account-wide opt-outs always apply). Paginated via `limit`/`offset`; returns the page
    plus the `total` count.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        agent_id (None | str | Unset): Filter to one agent (account-wide opt-outs still apply)
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentEmailOptOutListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> AgentEmailOptOutListResponse | HTTPValidationError | None:
    """List agent-email opt-outs

     List recipients who have opted out of this account's agent emails (filter to one agent via
    `agent_id`; account-wide opt-outs always apply). Paginated via `limit`/`offset`; returns the page
    plus the `total` count.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        agent_id (None | str | Unset): Filter to one agent (account-wide opt-outs still apply)
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentEmailOptOutListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            limit=limit,
            offset=offset,
            x_account_id=x_account_id,
        )
    ).parsed
