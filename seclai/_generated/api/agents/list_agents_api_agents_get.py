from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_list_response import AgentListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentListResponse.from_dict(response.json())

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
) -> Response[AgentListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentListResponse | HTTPValidationError]:
    """List agents

     List agents for the account with pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> AgentListResponse | HTTPValidationError | None:
    """List agents

     List agents for the account with pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentListResponse | HTTPValidationError]:
    """List agents

     List agents for the account with pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> AgentListResponse | HTTPValidationError | None:
    """List agents

     List agents for the account with pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            x_account_id=x_account_id,
        )
    ).parsed
