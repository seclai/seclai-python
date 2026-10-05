from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.source_content_status_list_response import (
    SourceContentStatusListResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    status: None | str | Unset = UNSET,
    content_version_id: list[UUID] | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["sort"] = sort

    params["order"] = order

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_content_version_id: list[str] | None | Unset
    if isinstance(content_version_id, Unset):
        json_content_version_id = UNSET
    elif isinstance(content_version_id, list):
        json_content_version_id = []
        for content_version_id_type_0_item_data in content_version_id:
            content_version_id_type_0_item = str(content_version_id_type_0_item_data)
            json_content_version_id.append(content_version_id_type_0_item)

    else:
        json_content_version_id = content_version_id
    params["content_version_id"] = json_content_version_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/{source_connection_id}/contents".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | SourceContentStatusListResponse
    | None
):
    if response.status_code == 200:
        response_200 = SourceContentStatusListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = ServiceUnavailableError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    status: None | str | Unset = UNSET,
    content_version_id: list[UUID] | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse
]:
    """List content items and their indexing status

     List every content item this source has attempted to index, with the status of each.

    Unlike the source's `content_count`, which only counts finished items, this listing includes items
    that are still processing and items that failed — so a bulk upload can report per-item progress and
    point at the specific items that did not make it.

    Correlating with an upload:
    - Each item is keyed by `content_version_id`, which is what the upload endpoints return. Pass those
    ids as repeated `content_version_id` query parameters to poll exactly the items you uploaded.
    - `source_connection_content_version_id` is `null` until an item finishes indexing; once set, it is
    the id `GET /contents/{id}` takes.
    - `content_status` reaches `completed` on success and `failed` on error, with the reason in `error`.
    The intermediate values are `pending`, `fetching`, `transcribing`, `scanning`, and `indexing`.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/title/status) and `order` (asc/desc). `created_at` sorts on when the
    item was uploaded or pulled.
    - Filtering: `status` and repeatable `content_version_id`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only list content for sources belonging
    to your account.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field (created_at/title/status) Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        status (None | str | Unset): Filter to one status: pending, fetching, transcribing,
            scanning, indexing, completed, or failed. Use `failed` to list only the items that could
            not be indexed.
        content_version_id (list[UUID] | None | Unset): Filter to specific content versions,
            repeatable. Pass the `content_version_id` values returned by the upload endpoints to poll
            exactly the items you uploaded in a single request. At most 500 ids per request — beyond
            that, page through the unfiltered listing or split the poll.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        status=status,
        content_version_id=content_version_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    status: None | str | Unset = UNSET,
    content_version_id: list[UUID] | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | SourceContentStatusListResponse
    | None
):
    """List content items and their indexing status

     List every content item this source has attempted to index, with the status of each.

    Unlike the source's `content_count`, which only counts finished items, this listing includes items
    that are still processing and items that failed — so a bulk upload can report per-item progress and
    point at the specific items that did not make it.

    Correlating with an upload:
    - Each item is keyed by `content_version_id`, which is what the upload endpoints return. Pass those
    ids as repeated `content_version_id` query parameters to poll exactly the items you uploaded.
    - `source_connection_content_version_id` is `null` until an item finishes indexing; once set, it is
    the id `GET /contents/{id}` takes.
    - `content_status` reaches `completed` on success and `failed` on error, with the reason in `error`.
    The intermediate values are `pending`, `fetching`, `transcribing`, `scanning`, and `indexing`.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/title/status) and `order` (asc/desc). `created_at` sorts on when the
    item was uploaded or pulled.
    - Filtering: `status` and repeatable `content_version_id`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only list content for sources belonging
    to your account.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field (created_at/title/status) Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        status (None | str | Unset): Filter to one status: pending, fetching, transcribing,
            scanning, indexing, completed, or failed. Use `failed` to list only the items that could
            not be indexed.
        content_version_id (list[UUID] | None | Unset): Filter to specific content versions,
            repeatable. Pass the `content_version_id` values returned by the upload endpoints to poll
            exactly the items you uploaded in a single request. At most 500 ids per request — beyond
            that, page through the unfiltered listing or split the poll.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        status=status,
        content_version_id=content_version_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    status: None | str | Unset = UNSET,
    content_version_id: list[UUID] | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse
]:
    """List content items and their indexing status

     List every content item this source has attempted to index, with the status of each.

    Unlike the source's `content_count`, which only counts finished items, this listing includes items
    that are still processing and items that failed — so a bulk upload can report per-item progress and
    point at the specific items that did not make it.

    Correlating with an upload:
    - Each item is keyed by `content_version_id`, which is what the upload endpoints return. Pass those
    ids as repeated `content_version_id` query parameters to poll exactly the items you uploaded.
    - `source_connection_content_version_id` is `null` until an item finishes indexing; once set, it is
    the id `GET /contents/{id}` takes.
    - `content_status` reaches `completed` on success and `failed` on error, with the reason in `error`.
    The intermediate values are `pending`, `fetching`, `transcribing`, `scanning`, and `indexing`.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/title/status) and `order` (asc/desc). `created_at` sorts on when the
    item was uploaded or pulled.
    - Filtering: `status` and repeatable `content_version_id`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only list content for sources belonging
    to your account.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field (created_at/title/status) Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        status (None | str | Unset): Filter to one status: pending, fetching, transcribing,
            scanning, indexing, completed, or failed. Use `failed` to list only the items that could
            not be indexed.
        content_version_id (list[UUID] | None | Unset): Filter to specific content versions,
            repeatable. Pass the `content_version_id` values returned by the upload endpoints to poll
            exactly the items you uploaded in a single request. At most 500 ids per request — beyond
            that, page through the unfiltered listing or split the poll.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        page=page,
        limit=limit,
        sort=sort,
        order=order,
        status=status,
        content_version_id=content_version_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    sort: str | Unset = "created_at",
    order: str | Unset = "desc",
    status: None | str | Unset = UNSET,
    content_version_id: list[UUID] | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | SourceContentStatusListResponse
    | None
):
    """List content items and their indexing status

     List every content item this source has attempted to index, with the status of each.

    Unlike the source's `content_count`, which only counts finished items, this listing includes items
    that are still processing and items that failed — so a bulk upload can report per-item progress and
    point at the specific items that did not make it.

    Correlating with an upload:
    - Each item is keyed by `content_version_id`, which is what the upload endpoints return. Pass those
    ids as repeated `content_version_id` query parameters to poll exactly the items you uploaded.
    - `source_connection_content_version_id` is `null` until an item finishes indexing; once set, it is
    the id `GET /contents/{id}` takes.
    - `content_status` reaches `completed` on success and `failed` on error, with the reason in `error`.
    The intermediate values are `pending`, `fetching`, `transcribing`, `scanning`, and `indexing`.

    Parameters:
    - Pagination: `page` and `limit`.
    - Sorting: `sort` (created_at/title/status) and `order` (asc/desc). `created_at` sorts on when the
    item was uploaded or pulled.
    - Filtering: `status` and repeatable `content_version_id`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only list content for sources belonging
    to your account.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        sort (str | Unset): Sort field (created_at/title/status) Default: 'created_at'.
        order (str | Unset): Sort order Default: 'desc'.
        status (None | str | Unset): Filter to one status: pending, fetching, transcribing,
            scanning, indexing, completed, or failed. Use `failed` to list only the items that could
            not be indexed.
        content_version_id (list[UUID] | None | Unset): Filter to specific content versions,
            repeatable. Pass the `content_version_id` values returned by the upload endpoints to poll
            exactly the items you uploaded in a single request. At most 500 ids per request — beyond
            that, page through the unfiltered listing or split the poll.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | SourceContentStatusListResponse
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            order=order,
            status=status,
            content_version_id=content_version_id,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
