from http import HTTPStatus
from io import BytesIO
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    run_id: UUID,
    attachment_id: str,
    *,
    download_name: None | str | Unset = UNSET,
    range_: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(range_, Unset):
        headers["Range"] = range_

    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

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
) -> Any | File | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 206:
        response_206 = File(payload=BytesIO(response.content))

        return response_206

    if response.status_code == 416:
        response_416 = cast(Any, None)
        return response_416

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
) -> Response[Any | File | HTTPValidationError | ServiceUnavailableError]:
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
    range_: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | File | HTTPValidationError | ServiceUnavailableError]:
    """Download an agent-run attachment

     Streams the bytes of a file of the given agent run: one a step emitted, or one the run started with.
    ``attachment_id`` is the ``id`` of an entry in the run's or a step's ``attachments``, or the URL-
    safe-base64-encoded storage key, which webhook and email links carry.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, a run whose trace was purged, a file not in the run) all collapse to a single 404 to
    prevent cross-tenant existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain) are served with their
    declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Byte ranges:
    - Every 200 and 206 carries ``Accept-Ranges: bytes`` and ``Content-Length``.
    - One range of a non-empty file (``bytes=start-end``, ``bytes=start-`` or ``bytes=-suffix`` with a
    positive suffix) is answered with 206 and ``Content-Range``, or with 416 and ``Content-Range: bytes
    */<size>`` when it starts at or past the end of the file or ends before it starts.
    - Any other ``Range``, including more than one range, is ignored and the whole file is served.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        range_ (None | str | Unset):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        attachment_id=attachment_id,
        download_name=download_name,
        range_=range_,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
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
    range_: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | File | HTTPValidationError | ServiceUnavailableError | None:
    """Download an agent-run attachment

     Streams the bytes of a file of the given agent run: one a step emitted, or one the run started with.
    ``attachment_id`` is the ``id`` of an entry in the run's or a step's ``attachments``, or the URL-
    safe-base64-encoded storage key, which webhook and email links carry.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, a run whose trace was purged, a file not in the run) all collapse to a single 404 to
    prevent cross-tenant existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain) are served with their
    declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Byte ranges:
    - Every 200 and 206 carries ``Accept-Ranges: bytes`` and ``Content-Length``.
    - One range of a non-empty file (``bytes=start-end``, ``bytes=start-`` or ``bytes=-suffix`` with a
    positive suffix) is answered with 206 and ``Content-Range``, or with 416 and ``Content-Range: bytes
    */<size>`` when it starts at or past the end of the file or ends before it starts.
    - Any other ``Range``, including more than one range, is ignored and the whole file is served.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        range_ (None | str | Unset):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        run_id=run_id,
        attachment_id=attachment_id,
        client=client,
        download_name=download_name,
        range_=range_,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    run_id: UUID,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    download_name: None | str | Unset = UNSET,
    range_: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | File | HTTPValidationError | ServiceUnavailableError]:
    """Download an agent-run attachment

     Streams the bytes of a file of the given agent run: one a step emitted, or one the run started with.
    ``attachment_id`` is the ``id`` of an entry in the run's or a step's ``attachments``, or the URL-
    safe-base64-encoded storage key, which webhook and email links carry.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, a run whose trace was purged, a file not in the run) all collapse to a single 404 to
    prevent cross-tenant existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain) are served with their
    declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Byte ranges:
    - Every 200 and 206 carries ``Accept-Ranges: bytes`` and ``Content-Length``.
    - One range of a non-empty file (``bytes=start-end``, ``bytes=start-`` or ``bytes=-suffix`` with a
    positive suffix) is answered with 206 and ``Content-Range``, or with 416 and ``Content-Range: bytes
    */<size>`` when it starts at or past the end of the file or ends before it starts.
    - Any other ``Range``, including more than one range, is ignored and the whole file is served.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        range_ (None | str | Unset):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        attachment_id=attachment_id,
        download_name=download_name,
        range_=range_,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: UUID,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    download_name: None | str | Unset = UNSET,
    range_: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | File | HTTPValidationError | ServiceUnavailableError | None:
    """Download an agent-run attachment

     Streams the bytes of a file of the given agent run: one a step emitted, or one the run started with.
    ``attachment_id`` is the ``id`` of an entry in the run's or a step's ``attachments``, or the URL-
    safe-base64-encoded storage key, which webhook and email links carry.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - The calling account must own ``run_id``; lookup failures (missing run, cross-account run, soft-
    deleted agent, a run whose trace was purged, a file not in the run) all collapse to a single 404 to
    prevent cross-tenant existence enumeration.

    MIME handling:
    - Inline-safe MIMEs (image/*, audio/*, video/*, application/pdf, text/plain) are served with their
    declared type.
    - Everything else is served as ``application/octet-stream`` with an attachment disposition to
    prevent stored-XSS.

    Byte ranges:
    - Every 200 and 206 carries ``Accept-Ranges: bytes`` and ``Content-Length``.
    - One range of a non-empty file (``bytes=start-end``, ``bytes=start-`` or ``bytes=-suffix`` with a
    positive suffix) is answered with 206 and ``Content-Range``, or with 416 and ``Content-Range: bytes
    */<size>`` when it starts at or past the end of the file or ends before it starts.
    - Any other ``Range``, including more than one range, is ignored and the whole file is served.

    Args:
        run_id (UUID):
        attachment_id (str):
        download_name (None | str | Unset):
        range_ (None | str | Unset):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            attachment_id=attachment_id,
            client=client,
            download_name=download_name,
            range_=range_,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
