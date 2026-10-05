from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_source_api_sources_source_connection_id_upload_post import (
    BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: str,
    *,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources/{source_connection_id}/upload".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | ServiceUnavailableError | None:
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
) -> Response[Any | HTTPValidationError | ServiceUnavailableError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | ServiceUnavailableError]:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes, except `image/svg+xml` at 5242880 bytes (SVG is sanitized
    before it is stored).

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/pdf`
    - `application/vnd.ms-excel`
    - `application/vnd.ms-outlook`
    - `application/vnd.ms-powerpoint`
    - `application/vnd.openxmlformats-officedocument.presentationml.presentation`
    - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
    - `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
    - `application/xml`
    - `application/zip`
    - `audio/flac`
    - `audio/mp4`
    - `audio/mpeg`
    - `audio/ogg`
    - `audio/wav`
    - `image/bmp`
    - `image/gif`
    - `image/jpeg`
    - `image/png`
    - `image/svg+xml`
    - `image/tiff`
    - `image/webp`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`
    - `video/mp4`
    - `video/quicktime`
    - `video/x-msvideo`

    Notes:
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - If the uploaded file's content type is `application/octet-stream`, the server attempts to infer
    the type from the file extension.
    - Use `metadata` to attach an arbitrary JSON object of metadata (for example
    `metadata={\"author\":\"Ada\",\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Response:
    - `status` is `uploaded` for a new upload, or `duplicate` when the same file already exists for this
    source.

    Tracking indexing progress:
    - **Which id you get back depends on `status`, and they are not interchangeable:**
      - `uploaded` — a new item. `content_version_id` is set and `source_connection_content_version_id`
    is `null`. Indexing continues in the background after this call returns.
      - `duplicate` — this exact file is already on the source, so nothing was created and nothing is
    being indexed. `content_version_id` is `null` and `source_connection_content_version_id` is the
    existing, already-indexed item: pass it straight to `GET /contents/{id}`. There is nothing to poll.
    - For an `uploaded` item, poll `GET /sources/{id}/contents/{content_version_id}` with the returned
    `content_version_id`, or `GET /sources/{id}/contents?content_version_id=…&content_version_id=…` for
    a whole batch, to follow each item through to `completed` or `failed`.
    - On those status endpoints `source_connection_content_version_id` stays `null` until the item
    finishes indexing; that is the id `GET /contents/{id}` takes.

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | HTTPValidationError | ServiceUnavailableError | None:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes, except `image/svg+xml` at 5242880 bytes (SVG is sanitized
    before it is stored).

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/pdf`
    - `application/vnd.ms-excel`
    - `application/vnd.ms-outlook`
    - `application/vnd.ms-powerpoint`
    - `application/vnd.openxmlformats-officedocument.presentationml.presentation`
    - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
    - `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
    - `application/xml`
    - `application/zip`
    - `audio/flac`
    - `audio/mp4`
    - `audio/mpeg`
    - `audio/ogg`
    - `audio/wav`
    - `image/bmp`
    - `image/gif`
    - `image/jpeg`
    - `image/png`
    - `image/svg+xml`
    - `image/tiff`
    - `image/webp`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`
    - `video/mp4`
    - `video/quicktime`
    - `video/x-msvideo`

    Notes:
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - If the uploaded file's content type is `application/octet-stream`, the server attempts to infer
    the type from the file extension.
    - Use `metadata` to attach an arbitrary JSON object of metadata (for example
    `metadata={\"author\":\"Ada\",\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Response:
    - `status` is `uploaded` for a new upload, or `duplicate` when the same file already exists for this
    source.

    Tracking indexing progress:
    - **Which id you get back depends on `status`, and they are not interchangeable:**
      - `uploaded` — a new item. `content_version_id` is set and `source_connection_content_version_id`
    is `null`. Indexing continues in the background after this call returns.
      - `duplicate` — this exact file is already on the source, so nothing was created and nothing is
    being indexed. `content_version_id` is `null` and `source_connection_content_version_id` is the
    existing, already-indexed item: pass it straight to `GET /contents/{id}`. There is nothing to poll.
    - For an `uploaded` item, poll `GET /sources/{id}/contents/{content_version_id}` with the returned
    `content_version_id`, or `GET /sources/{id}/contents?content_version_id=…&content_version_id=…` for
    a whole batch, to follow each item through to `completed` or `failed`.
    - On those status endpoints `source_connection_content_version_id` stays `null` until the item
    finishes indexing; that is the id `GET /contents/{id}` takes.

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | ServiceUnavailableError]:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes, except `image/svg+xml` at 5242880 bytes (SVG is sanitized
    before it is stored).

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/pdf`
    - `application/vnd.ms-excel`
    - `application/vnd.ms-outlook`
    - `application/vnd.ms-powerpoint`
    - `application/vnd.openxmlformats-officedocument.presentationml.presentation`
    - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
    - `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
    - `application/xml`
    - `application/zip`
    - `audio/flac`
    - `audio/mp4`
    - `audio/mpeg`
    - `audio/ogg`
    - `audio/wav`
    - `image/bmp`
    - `image/gif`
    - `image/jpeg`
    - `image/png`
    - `image/svg+xml`
    - `image/tiff`
    - `image/webp`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`
    - `video/mp4`
    - `video/quicktime`
    - `video/x-msvideo`

    Notes:
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - If the uploaded file's content type is `application/octet-stream`, the server attempts to infer
    the type from the file extension.
    - Use `metadata` to attach an arbitrary JSON object of metadata (for example
    `metadata={\"author\":\"Ada\",\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Response:
    - `status` is `uploaded` for a new upload, or `duplicate` when the same file already exists for this
    source.

    Tracking indexing progress:
    - **Which id you get back depends on `status`, and they are not interchangeable:**
      - `uploaded` — a new item. `content_version_id` is set and `source_connection_content_version_id`
    is `null`. Indexing continues in the background after this call returns.
      - `duplicate` — this exact file is already on the source, so nothing was created and nothing is
    being indexed. `content_version_id` is `null` and `source_connection_content_version_id` is the
    existing, already-indexed item: pass it straight to `GET /contents/{id}`. There is nothing to poll.
    - For an `uploaded` item, poll `GET /sources/{id}/contents/{content_version_id}` with the returned
    `content_version_id`, or `GET /sources/{id}/contents?content_version_id=…&content_version_id=…` for
    a whole batch, to follow each item through to `completed` or `failed`.
    - On those status endpoints `source_connection_content_version_id` stays `null` until the item
    finishes indexing; that is the id `GET /contents/{id}` takes.

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | HTTPValidationError | ServiceUnavailableError | None:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes, except `image/svg+xml` at 5242880 bytes (SVG is sanitized
    before it is stored).

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/pdf`
    - `application/vnd.ms-excel`
    - `application/vnd.ms-outlook`
    - `application/vnd.ms-powerpoint`
    - `application/vnd.openxmlformats-officedocument.presentationml.presentation`
    - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
    - `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
    - `application/xml`
    - `application/zip`
    - `audio/flac`
    - `audio/mp4`
    - `audio/mpeg`
    - `audio/ogg`
    - `audio/wav`
    - `image/bmp`
    - `image/gif`
    - `image/jpeg`
    - `image/png`
    - `image/svg+xml`
    - `image/tiff`
    - `image/webp`
    - `text/csv`
    - `text/html`
    - `text/markdown`
    - `text/plain`
    - `text/x-markdown`
    - `text/xml`
    - `video/mp4`
    - `video/quicktime`
    - `video/x-msvideo`

    Notes:
    - A key bound to a user must belong to an owner or administrator of the account; a viewer's key is
    refused with 403 `permission_denied`. Account-scoped keys carry no user and are unaffected.
    - If the uploaded file's content type is `application/octet-stream`, the server attempts to infer
    the type from the file extension.
    - Use `metadata` to attach an arbitrary JSON object of metadata (for example
    `metadata={\"author\":\"Ada\",\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Response:
    - `status` is `uploaded` for a new upload, or `duplicate` when the same file already exists for this
    source.

    Tracking indexing progress:
    - **Which id you get back depends on `status`, and they are not interchangeable:**
      - `uploaded` — a new item. `content_version_id` is set and `source_connection_content_version_id`
    is `null`. Indexing continues in the background after this call returns.
      - `duplicate` — this exact file is already on the source, so nothing was created and nothing is
    being indexed. `content_version_id` is `null` and `source_connection_content_version_id` is the
    existing, already-indexed item: pass it straight to `GET /contents/{id}`. There is nothing to poll.
    - For an `uploaded` item, poll `GET /sources/{id}/contents/{content_version_id}` with the returned
    `content_version_id`, or `GET /sources/{id}/contents?content_version_id=…&content_version_id=…` for
    a whole batch, to follow each item through to `completed` or `failed`.
    - On those status endpoints `source_connection_content_version_id` stays `null` until the item
    finishes indexing; that is the id `GET /contents/{id}` takes.

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
