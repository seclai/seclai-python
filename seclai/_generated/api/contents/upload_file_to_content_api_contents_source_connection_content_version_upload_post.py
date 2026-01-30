from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_content_api_contents_source_connection_content_version_upload_post import (
    BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
)
from ...models.file_upload_response import FileUploadResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    source_connection_content_version: str,
    *,
    body: BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contents/{source_connection_content_version}/upload".format(
            source_connection_content_version=quote(str(source_connection_content_version), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileUploadResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FileUploadResponse.from_dict(response.json())

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
) -> Response[FileUploadResponse | HTTPValidationError]:
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
    body: BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
) -> Response[FileUploadResponse | HTTPValidationError]:
    r"""Replace a content version with a new upload

     Upload a new file and replace the content backing an existing `SourceConnectionContentVersion`.

    This behaves like a source file upload, but it targets an existing content version ID. This is
    useful when you want to correct or update an uploaded document while keeping references stable.

    **Maximum file size:** 209715200 bytes.

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/msword`
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
    `metadata={\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Auth & scoping:
    - Requires `X-API-Key`. You can only replace content belonging to your account.

    Args:
        source_connection_content_version (str):
        body (BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileUploadResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
) -> FileUploadResponse | HTTPValidationError | None:
    r"""Replace a content version with a new upload

     Upload a new file and replace the content backing an existing `SourceConnectionContentVersion`.

    This behaves like a source file upload, but it targets an existing content version ID. This is
    useful when you want to correct or update an uploaded document while keeping references stable.

    **Maximum file size:** 209715200 bytes.

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/msword`
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
    `metadata={\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Auth & scoping:
    - Requires `X-API-Key`. You can only replace content belonging to your account.

    Args:
        source_connection_content_version (str):
        body (BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileUploadResponse | HTTPValidationError
    """

    return sync_detailed(
        source_connection_content_version=source_connection_content_version,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
) -> Response[FileUploadResponse | HTTPValidationError]:
    r"""Replace a content version with a new upload

     Upload a new file and replace the content backing an existing `SourceConnectionContentVersion`.

    This behaves like a source file upload, but it targets an existing content version ID. This is
    useful when you want to correct or update an uploaded document while keeping references stable.

    **Maximum file size:** 209715200 bytes.

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/msword`
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
    `metadata={\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Auth & scoping:
    - Requires `X-API-Key`. You can only replace content belonging to your account.

    Args:
        source_connection_content_version (str):
        body (BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileUploadResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost,
) -> FileUploadResponse | HTTPValidationError | None:
    r"""Replace a content version with a new upload

     Upload a new file and replace the content backing an existing `SourceConnectionContentVersion`.

    This behaves like a source file upload, but it targets an existing content version ID. This is
    useful when you want to correct or update an uploaded document while keeping references stable.

    **Maximum file size:** 209715200 bytes.

    **Supported MIME types:**
    - `application/epub+zip`
    - `application/json`
    - `application/msword`
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
    `metadata={\"category\":\"docs\"}`).
    - `title` is a convenience field and is merged into the metadata as `metadata.title` (it does not
    override an existing `metadata.title`).
    - For backwards compatibility, you can also pass form fields named `metadata_<key>` (for example
    `metadata_author=...`). These override keys from `metadata`.

    Auth & scoping:
    - Requires `X-API-Key`. You can only replace content belonging to your account.

    Args:
        source_connection_content_version (str):
        body (BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileUploadResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=client,
            body=body,
        )
    ).parsed
