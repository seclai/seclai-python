from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_source_api_sources_source_connection_id_upload_post import (
    BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: str,
    *,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

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
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError]:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes.

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

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

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
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | None:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes.

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

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

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
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError]:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes.

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

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

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
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | None:
    r"""Upload a file to a content source

     Upload a file to a content source.

    **Maximum file size:** 209715200 bytes.

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

    Args:
        source_connection_id (str):
        x_account_id (UUID | Unset):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

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
