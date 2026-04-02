from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_bank_list_response_model import MemoryBankListResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    type_: None | str | Unset = UNSET,
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

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    else:
        json_type_ = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memory_banks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MemoryBankListResponseModel | None:
    if response.status_code == 200:
        response_200 = MemoryBankListResponseModel.from_dict(response.json())

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
) -> Response[HTTPValidationError | MemoryBankListResponseModel]:
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
    type_: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBankListResponseModel]:
    """List Memory Banks

     List memory banks for the account.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number (1-based). Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        sort (str | Unset): Sort field. One of: created_at, updated_at, name. Default:
            'created_at'.
        order (str | Unset): Sort direction: asc or desc. Default: 'desc'.
        type_ (None | str | Unset): Filter by bank type: conversation or general.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBankListResponseModel]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        type_=type_,
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
    type_: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | MemoryBankListResponseModel | None:
    """List Memory Banks

     List memory banks for the account.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number (1-based). Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        sort (str | Unset): Sort field. One of: created_at, updated_at, name. Default:
            'created_at'.
        order (str | Unset): Sort direction: asc or desc. Default: 'desc'.
        type_ (None | str | Unset): Filter by bank type: conversation or general.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBankListResponseModel
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        type_=type_,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    type_: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBankListResponseModel]:
    """List Memory Banks

     List memory banks for the account.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number (1-based). Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        sort (str | Unset): Sort field. One of: created_at, updated_at, name. Default:
            'created_at'.
        order (str | Unset): Sort direction: asc or desc. Default: 'desc'.
        type_ (None | str | Unset): Filter by bank type: conversation or general.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBankListResponseModel]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        type_=type_,
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
    type_: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | MemoryBankListResponseModel | None:
    """List Memory Banks

     List memory banks for the account.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        page (int | Unset): Page number (1-based). Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        sort (str | Unset): Sort field. One of: created_at, updated_at, name. Default:
            'created_at'.
        order (str | Unset): Sort direction: asc or desc. Default: 'desc'.
        type_ (None | str | Unset): Filter by bank type: conversation or general.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBankListResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            type_=type_,
            x_account_id=x_account_id,
        )
    ).parsed
