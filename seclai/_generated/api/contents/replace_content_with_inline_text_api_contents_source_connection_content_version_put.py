from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_upload_response import FileUploadResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.inline_text_replace_request import InlineTextReplaceRequest
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_content_version: str,
    *,
    body: InlineTextReplaceRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/contents/{source_connection_content_version}".format(
            source_connection_content_version=quote(
                str(source_connection_content_version), safe=""
            ),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = FileUploadResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
) -> Response[Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextReplaceRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError]:
    """Replace a content version with inline text

     Replace a content version using a small inline text payload.

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
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.
    - The replacement is indexed in the background. This `SourceConnectionContentVersion` ID keeps
    working, and reads return the previous content until indexing finishes; poll
    `list_source_content_status` to follow it. The returned `content_version_id` is the new version.

    Args:
        source_connection_content_version (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (InlineTextReplaceRequest): Request model for inline text content replacement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextReplaceRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Replace a content version with inline text

     Replace a content version using a small inline text payload.

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
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.
    - The replacement is indexed in the background. This `SourceConnectionContentVersion` ID keeps
    working, and reads return the previous content until indexing finishes; poll
    `list_source_content_status` to follow it. The returned `content_version_id` is the new version.

    Args:
        source_connection_content_version (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (InlineTextReplaceRequest): Request model for inline text content replacement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        source_connection_content_version=source_connection_content_version,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextReplaceRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError]:
    """Replace a content version with inline text

     Replace a content version using a small inline text payload.

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
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.
    - The replacement is indexed in the background. This `SourceConnectionContentVersion` ID keeps
    working, and reads return the previous content until indexing finishes; poll
    `list_source_content_status` to follow it. The returned `content_version_id` is the new version.

    Args:
        source_connection_content_version (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (InlineTextReplaceRequest): Request model for inline text content replacement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: InlineTextReplaceRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Replace a content version with inline text

     Replace a content version using a small inline text payload.

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
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - Use this endpoint for small text payloads; larger files should use `/upload`.
    - `title` is merged into `metadata.title` when not already present.
    - The replacement is indexed in the background. This `SourceConnectionContentVersion` ID keeps
    working, and reads return the previous content until indexing finishes; poll
    `list_source_content_status` to follow it. The returned `content_version_id` is the new version.

    Args:
        source_connection_content_version (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (InlineTextReplaceRequest): Request model for inline text content replacement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileUploadResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
