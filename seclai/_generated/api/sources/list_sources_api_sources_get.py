from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.source_list_response import SourceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    account_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["sort"] = sort

    params["order"] = order

    json_account_id: None | str | Unset
    if isinstance(account_id, Unset):
        json_account_id = UNSET
    else:
        json_account_id = account_id
    params["account_id"] = json_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SourceListResponse | None:
    if response.status_code == 200:
        response_200 = SourceListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SourceListResponse]:
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
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    account_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SourceListResponse]:
    """List sources

     List content sources for your account.

    A *source* is where Seclai pulls or receives content from (for example RSS feeds, websites, file
    uploads, or custom indexes). Sources are the inputs that power your agents and knowledge base
    workflows.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).

    Auth & scoping:
    - Requires `X-API-Key`. Results are scoped to the API key's account.
    - The optional `account_id` query param is only allowed when it matches the API key's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        account_id (None | str | Unset): List sources for the given account. Defaults to the api
            key's account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SourceListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        account_id=account_id,
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
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    account_id: None | str | Unset = UNSET,
) -> HTTPValidationError | SourceListResponse | None:
    """List sources

     List content sources for your account.

    A *source* is where Seclai pulls or receives content from (for example RSS feeds, websites, file
    uploads, or custom indexes). Sources are the inputs that power your agents and knowledge base
    workflows.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).

    Auth & scoping:
    - Requires `X-API-Key`. Results are scoped to the API key's account.
    - The optional `account_id` query param is only allowed when it matches the API key's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        account_id (None | str | Unset): List sources for the given account. Defaults to the api
            key's account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SourceListResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    account_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SourceListResponse]:
    """List sources

     List content sources for your account.

    A *source* is where Seclai pulls or receives content from (for example RSS feeds, websites, file
    uploads, or custom indexes). Sources are the inputs that power your agents and knowledge base
    workflows.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).

    Auth & scoping:
    - Requires `X-API-Key`. Results are scoped to the API key's account.
    - The optional `account_id` query param is only allowed when it matches the API key's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        account_id (None | str | Unset): List sources for the given account. Defaults to the api
            key's account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SourceListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    account_id: None | str | Unset = UNSET,
) -> HTTPValidationError | SourceListResponse | None:
    """List sources

     List content sources for your account.

    A *source* is where Seclai pulls or receives content from (for example RSS feeds, websites, file
    uploads, or custom indexes). Sources are the inputs that power your agents and knowledge base
    workflows.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).

    Auth & scoping:
    - Requires `X-API-Key`. Results are scoped to the API key's account.
    - The optional `account_id` query param is only allowed when it matches the API key's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        account_id (None | str | Unset): List sources for the given account. Defaults to the api
            key's account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SourceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            account_id=account_id,
        )
    ).parsed
