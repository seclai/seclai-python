from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    run_id: UUID,
    attachment_id: str,
    *,
    download_name: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_download_name: None | str | Unset
    if isinstance(download_name, Unset):
        json_download_name = UNSET
    else:
        json_download_name = download_name
    params["download_name"] = json_download_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/agent-runs/{run_id}/attachments/{attachment_id}".format(
            run_id=quote(str(run_id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[File | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: UUID,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    download_name: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[File | HTTPValidationError]:
    """Download an agent-run attachment

     Streams the bytes of an attachment emitted by a step in the given agent run.  ``attachment_id`` is
    the URL-safe-base64-encoded ``storage_key`` (use the encoder shared by webhook + email payload
    builders).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, unreferenced storage_key) all collapse to a single 404 to prevent cross-tenant
    existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain,
    application/vnd.seclai.manifest+json) are served with their declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        attachment_id=attachment_id,
        download_name=download_name,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: UUID,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    download_name: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> File | HTTPValidationError | None:
    """Download an agent-run attachment

     Streams the bytes of an attachment emitted by a step in the given agent run.  ``attachment_id`` is
    the URL-safe-base64-encoded ``storage_key`` (use the encoder shared by webhook + email payload
    builders).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, unreferenced storage_key) all collapse to a single 404 to prevent cross-tenant
    existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain,
    application/vnd.seclai.manifest+json) are served with their declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | HTTPValidationError
    """

    return sync_detailed(
        run_id=run_id,
        attachment_id=attachment_id,
        client=client,
        download_name=download_name,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    run_id: UUID,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    download_name: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[File | HTTPValidationError]:
    """Download an agent-run attachment

     Streams the bytes of an attachment emitted by a step in the given agent run.  ``attachment_id`` is
    the URL-safe-base64-encoded ``storage_key`` (use the encoder shared by webhook + email payload
    builders).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, unreferenced storage_key) all collapse to a single 404 to prevent cross-tenant
    existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain,
    application/vnd.seclai.manifest+json) are served with their declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        attachment_id=attachment_id,
        download_name=download_name,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: UUID,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    download_name: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> File | HTTPValidationError | None:
    """Download an agent-run attachment

     Streams the bytes of an attachment emitted by a step in the given agent run.  ``attachment_id`` is
    the URL-safe-base64-encoded ``storage_key`` (use the encoder shared by webhook + email payload
    builders).

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, unreferenced storage_key) all collapse to a single 404 to prevent cross-tenant
    existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain,
    application/vnd.seclai.manifest+json) are served with their declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            attachment_id=attachment_id,
            client=client,
            download_name=download_name,
            x_account_id=x_account_id,
        )
    ).parsed
