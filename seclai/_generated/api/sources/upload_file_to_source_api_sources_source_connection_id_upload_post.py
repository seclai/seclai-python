from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_source_api_sources_source_connection_id_upload_post import (
    BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
)
from ...models.file_upload_response import FileUploadResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    source_connection_id: str,
    *,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
) -> Response[FileUploadResponse | HTTPValidationError]:
    """Upload a file to a content source

     Upload a file to a content source.

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

    Args:
        source_connection_id (str):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileUploadResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
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
) -> FileUploadResponse | HTTPValidationError | None:
    """Upload a file to a content source

     Upload a file to a content source.

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

    Args:
        source_connection_id (str):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileUploadResponse | HTTPValidationError
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
) -> Response[FileUploadResponse | HTTPValidationError]:
    """Upload a file to a content source

     Upload a file to a content source.

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

    Args:
        source_connection_id (str):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileUploadResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost,
) -> FileUploadResponse | HTTPValidationError | None:
    """Upload a file to a content source

     Upload a file to a content source.

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

    Args:
        source_connection_id (str):
        body (BodyUploadFileToSourceApiSourcesSourceConnectionIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileUploadResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            body=body,
        )
    ).parsed
