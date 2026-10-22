from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_attachment_detail_response import ContentAttachmentDetailResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contents/{source_connection_content_version}/attachments/{attachment_id}".format(
            source_connection_content_version=quote(
                str(source_connection_content_version), safe=""
            ),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ContentAttachmentDetailResponse
    | HTTPValidationError
    | ServiceUnavailableError
    | None
):
    if response.status_code == 200:
        response_200 = ContentAttachmentDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

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
    Any
    | ContentAttachmentDetailResponse
    | HTTPValidationError
    | ServiceUnavailableError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    Any
    | ContentAttachmentDetailResponse
    | HTTPValidationError
    | ServiceUnavailableError
]:
    """Get a content attachment

     Get one file attached to a content item: its indexing status and reason, its metadata, and the text
    it is indexed by.

    `attachment_id` is the `id` of an entry in the item's attachment list. Use `start` and `end` to page
    through long text. A file that was not indexed has no text.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContentAttachmentDetailResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        attachment_id=attachment_id,
        start=start,
        end=end,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    Any
    | ContentAttachmentDetailResponse
    | HTTPValidationError
    | ServiceUnavailableError
    | None
):
    """Get a content attachment

     Get one file attached to a content item: its indexing status and reason, its metadata, and the text
    it is indexed by.

    `attachment_id` is the `id` of an entry in the item's attachment list. Use `start` and `end` to page
    through long text. A file that was not indexed has no text.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContentAttachmentDetailResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        source_connection_content_version=source_connection_content_version,
        attachment_id=attachment_id,
        client=client,
        start=start,
        end=end,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    Any
    | ContentAttachmentDetailResponse
    | HTTPValidationError
    | ServiceUnavailableError
]:
    """Get a content attachment

     Get one file attached to a content item: its indexing status and reason, its metadata, and the text
    it is indexed by.

    `attachment_id` is the `id` of an entry in the item's attachment list. Use `start` and `end` to page
    through long text. A file that was not indexed has no text.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContentAttachmentDetailResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        attachment_id=attachment_id,
        start=start,
        end=end,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    Any
    | ContentAttachmentDetailResponse
    | HTTPValidationError
    | ServiceUnavailableError
    | None
):
    """Get a content attachment

     Get one file attached to a content item: its indexing status and reason, its metadata, and the text
    it is indexed by.

    `attachment_id` is the `id` of an entry in the item's attachment list. Use `start` and `end` to page
    through long text. A file that was not indexed has no text.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContentAttachmentDetailResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            attachment_id=attachment_id,
            client=client,
            start=start,
            end=end,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
