from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.inline_text_upload_request import InlineTextUploadRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    body: InlineTextUploadRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources/{source_connection_id}".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError]:
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
    body: InlineTextUploadRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """Upload inline text to a content source

     Upload a small text payload to a content source (no multipart/form-data required).

    **Maximum payload size:** 8192 bytes (UTF-8).

    **Supported content types:**
    - `application/json`
    - `application/xml`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`

    Notes:
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (InlineTextUploadRequest): Request model for inline text uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextUploadRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | None:
    """Upload inline text to a content source

     Upload a small text payload to a content source (no multipart/form-data required).

    **Maximum payload size:** 8192 bytes (UTF-8).

    **Supported content types:**
    - `application/json`
    - `application/xml`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`

    Notes:
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (InlineTextUploadRequest): Request model for inline text uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextUploadRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """Upload inline text to a content source

     Upload a small text payload to a content source (no multipart/form-data required).

    **Maximum payload size:** 8192 bytes (UTF-8).

    **Supported content types:**
    - `application/json`
    - `application/xml`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`

    Notes:
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (InlineTextUploadRequest): Request model for inline text uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextUploadRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | None:
    """Upload inline text to a content source

     Upload a small text payload to a content source (no multipart/form-data required).

    **Maximum payload size:** 8192 bytes (UTF-8).

    **Supported content types:**
    - `application/json`
    - `application/xml`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`

    Notes:
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (InlineTextUploadRequest): Request model for inline text uploads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
