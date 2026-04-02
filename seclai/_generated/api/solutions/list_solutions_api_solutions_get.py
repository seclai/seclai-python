from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.solution_list_response import SolutionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    search: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["sort"] = sort

    params["order"] = order

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/solutions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SolutionListResponse | None:
    if response.status_code == 200:
        response_200 = SolutionListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SolutionListResponse]:
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
    search: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | SolutionListResponse]:
    """List solutions

     List solutions for your account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Use solutions
    to organise related resources and leverage AI assistants for automated setup.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).
    - Filtering: `search` to filter by solution name (case-insensitive partial match).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        search (None | str | Unset): Filter by solution name (case-insensitive partial match)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        search=search,
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
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    search: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | SolutionListResponse | None:
    """List solutions

     List solutions for your account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Use solutions
    to organise related resources and leverage AI assistants for automated setup.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).
    - Filtering: `search` to filter by solution name (case-insensitive partial match).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        search (None | str | Unset): Filter by solution name (case-insensitive partial match)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionListResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        search=search,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    search: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | SolutionListResponse]:
    """List solutions

     List solutions for your account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Use solutions
    to organise related resources and leverage AI assistants for automated setup.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).
    - Filtering: `search` to filter by solution name (case-insensitive partial match).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        search (None | str | Unset): Filter by solution name (case-insensitive partial match)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        search=search,
        x_account_id=x_account_id,
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
    search: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | SolutionListResponse | None:
    """List solutions

     List solutions for your account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Use solutions
    to organise related resources and leverage AI assistants for automated setup.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/updated_at/name) and `order` (asc/desc).
    - Filtering: `search` to filter by solution name (case-insensitive partial match).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        search (None | str | Unset): Filter by solution name (case-insensitive partial match)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            search=search,
            x_account_id=x_account_id,
        )
    ).parsed
