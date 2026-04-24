from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_agent_input_api_response import UploadAgentInputApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/upload-input".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UploadAgentInputApiResponse | None:
    if response.status_code == 202:
        response_202 = UploadAgentInputApiResponse.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | UploadAgentInputApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | UploadAgentInputApiResponse]:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run.

    Supports the same file types as content source uploads: text, PDF, DOCX, audio, video, images, etc.
    Text and document files are processed synchronously; audio/video are submitted for asynchronous
    transcription.

    **Size limit:** 200 MB per file.

    **Supported extensions:** txt, html, md, csv, xml, json, pdf, msg, docx, doc, pptx, ppt, xlsx, xls,
    zip, epub, png, jpg, gif, bmp, tiff, webp, mp3, wav, m4a, flac, ogg, mp4, mov, avi.

    After uploading, poll `GET /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready`,
    then pass `input_upload_id` to `POST /agents/{agent_id}/runs`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadAgentInputApiResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | UploadAgentInputApiResponse | None:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run.

    Supports the same file types as content source uploads: text, PDF, DOCX, audio, video, images, etc.
    Text and document files are processed synchronously; audio/video are submitted for asynchronous
    transcription.

    **Size limit:** 200 MB per file.

    **Supported extensions:** txt, html, md, csv, xml, json, pdf, msg, docx, doc, pptx, ppt, xlsx, xls,
    zip, epub, png, jpg, gif, bmp, tiff, webp, mp3, wav, m4a, flac, ogg, mp4, mov, avi.

    After uploading, poll `GET /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready`,
    then pass `input_upload_id` to `POST /agents/{agent_id}/runs`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadAgentInputApiResponse
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | UploadAgentInputApiResponse]:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run.

    Supports the same file types as content source uploads: text, PDF, DOCX, audio, video, images, etc.
    Text and document files are processed synchronously; audio/video are submitted for asynchronous
    transcription.

    **Size limit:** 200 MB per file.

    **Supported extensions:** txt, html, md, csv, xml, json, pdf, msg, docx, doc, pptx, ppt, xlsx, xls,
    zip, epub, png, jpg, gif, bmp, tiff, webp, mp3, wav, m4a, flac, ogg, mp4, mov, avi.

    After uploading, poll `GET /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready`,
    then pass `input_upload_id` to `POST /agents/{agent_id}/runs`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadAgentInputApiResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | UploadAgentInputApiResponse | None:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run.

    Supports the same file types as content source uploads: text, PDF, DOCX, audio, video, images, etc.
    Text and document files are processed synchronously; audio/video are submitted for asynchronous
    transcription.

    **Size limit:** 200 MB per file.

    **Supported extensions:** txt, html, md, csv, xml, json, pdf, msg, docx, doc, pptx, ppt, xlsx, xls,
    zip, epub, png, jpg, gif, bmp, tiff, webp, mp3, wav, m4a, flac, ogg, mp4, mov, avi.

    After uploading, poll `GET /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready`,
    then pass `input_upload_id` to `POST /agents/{agent_id}/runs`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadAgentInputApiResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
