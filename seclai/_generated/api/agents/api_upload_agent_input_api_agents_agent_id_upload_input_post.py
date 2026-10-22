from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.upload_agent_input_api_response import UploadAgentInputApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
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
        "url": "/agents/{agent_id}/upload-input".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse | None:
    if response.status_code == 202:
        response_202 = UploadAgentInputApiResponse.from_dict(response.json())

        return response_202

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
    HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse
]:
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
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse
]:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run. Any other agent rejects the upload
    with HTTP 400.

    **Size limit:** 200 MB per file.

    From `Seclai-Version: 2026-10-16` a file of any type is accepted and is `ready` at once: pass
    `input_upload_id` to `POST /agents/{agent_id}/runs`. Each step receives the file itself when its
    model reads that type, and otherwise its text (OCR, extraction or transcript), made once for the
    steps that need it; a type nothing reads or converts is passed on as a file only. `input` carries a
    `# filename` heading per file.

    Earlier versions accept only these extensions: avi, bmp, csv, docx, epub, flac, gif, html, jpg,
    json, m4a, markdown, md, mov, mp3, mp4, msg, ogg, pdf, png, ppt, pptx, svg, tiff, txt, wav, webp,
    xls, xlsx, xml, zip. They write each file's text into `input`, so poll `GET
    /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready` before running.

    The agent-input-binary janitor sweeps originals once they pass your account's agent-trace retention
    (the agent-traces source's retention period; free default 7 days).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
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
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse | None:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run. Any other agent rejects the upload
    with HTTP 400.

    **Size limit:** 200 MB per file.

    From `Seclai-Version: 2026-10-16` a file of any type is accepted and is `ready` at once: pass
    `input_upload_id` to `POST /agents/{agent_id}/runs`. Each step receives the file itself when its
    model reads that type, and otherwise its text (OCR, extraction or transcript), made once for the
    steps that need it; a type nothing reads or converts is passed on as a file only. `input` carries a
    `# filename` heading per file.

    Earlier versions accept only these extensions: avi, bmp, csv, docx, epub, flac, gif, html, jpg,
    json, m4a, markdown, md, mov, mp3, mp4, msg, ogg, pdf, png, ppt, pptx, svg, tiff, txt, wav, webp,
    xls, xlsx, xml, zip. They write each file's text into `input`, so poll `GET
    /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready` before running.

    The agent-input-binary janitor sweeps originals once they pass your account's agent-trace retention
    (the agent-traces source's retention period; free default 7 days).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse
]:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run. Any other agent rejects the upload
    with HTTP 400.

    **Size limit:** 200 MB per file.

    From `Seclai-Version: 2026-10-16` a file of any type is accepted and is `ready` at once: pass
    `input_upload_id` to `POST /agents/{agent_id}/runs`. Each step receives the file itself when its
    model reads that type, and otherwise its text (OCR, extraction or transcript), made once for the
    steps that need it; a type nothing reads or converts is passed on as a file only. `input` carries a
    `# filename` heading per file.

    Earlier versions accept only these extensions: avi, bmp, csv, docx, epub, flac, gif, html, jpg,
    json, m4a, markdown, md, mov, mp3, mp4, msg, ogg, pdf, png, ppt, pptx, svg, tiff, txt, wav, webp,
    xls, xlsx, xml, zip. They write each file's text into `input`, so poll `GET
    /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready` before running.

    The agent-input-binary janitor sweeps originals once they pass your account's agent-trace retention
    (the agent-traces source's retention period; free default 7 days).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse | None:
    """Upload file input

     Upload a file to use as input for a `dynamic_input` agent run. Any other agent rejects the upload
    with HTTP 400.

    **Size limit:** 200 MB per file.

    From `Seclai-Version: 2026-10-16` a file of any type is accepted and is `ready` at once: pass
    `input_upload_id` to `POST /agents/{agent_id}/runs`. Each step receives the file itself when its
    model reads that type, and otherwise its text (OCR, extraction or transcript), made once for the
    steps that need it; a type nothing reads or converts is passed on as a file only. `input` carries a
    `# filename` heading per file.

    Earlier versions accept only these extensions: avi, bmp, csv, docx, epub, flac, gif, html, jpg,
    json, m4a, markdown, md, mov, mp3, mp4, msg, ogg, pdf, png, ppt, pptx, svg, tiff, txt, wav, webp,
    xls, xlsx, xml, zip. They write each file's text into `input`, so poll `GET
    /agents/{agent_id}/input-uploads/{upload_id}` until `status` is `ready` before running.

    The agent-input-binary janitor sweeps originals once they pass your account's agent-trace retention
    (the agent-traces source's retention period; free default 7 days).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | UploadAgentInputApiResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
