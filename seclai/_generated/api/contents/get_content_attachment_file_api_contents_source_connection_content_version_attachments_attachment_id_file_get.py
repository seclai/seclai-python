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
    source_connection_content_version: UUID,
    attachment_id: UUID,
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
        "method": "get",
        "url": "/contents/{source_connection_content_version}/attachments/{attachment_id}/file".format(
            source_connection_content_version=quote(
                str(source_connection_content_version), safe=""
            ),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

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
) -> Response[Any | File | HTTPValidationError | ServiceUnavailableError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | File | HTTPValidationError | ServiceUnavailableError]:
    """Download a content attachment

     Download an attached file's bytes.

    Images, audio, video, PDF and plain text are served with their own type; an SVG that cannot be
    sanitized, and anything else, is served as `application/octet-stream`.

    Answers 403 when the file is withheld: a governance policy blocked or redacted it, or it arrived
    from outside and is still being indexed. The attachment's `file_withheld` field says which before
    you ask.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        attachment_id=attachment_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | File | HTTPValidationError | ServiceUnavailableError | None:
    """Download a content attachment

     Download an attached file's bytes.

    Images, audio, video, PDF and plain text are served with their own type; an SVG that cannot be
    sanitized, and anything else, is served as `application/octet-stream`.

    Answers 403 when the file is withheld: a governance policy blocked or redacted it, or it arrived
    from outside and is still being indexed. The attachment's `file_withheld` field says which before
    you ask.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        source_connection_content_version=source_connection_content_version,
        attachment_id=attachment_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | File | HTTPValidationError | ServiceUnavailableError]:
    """Download a content attachment

     Download an attached file's bytes.

    Images, audio, video, PDF and plain text are served with their own type; an SVG that cannot be
    sanitized, and anything else, is served as `application/octet-stream`.

    Answers 403 when the file is withheld: a governance policy blocked or redacted it, or it arrived
    from outside and is still being indexed. The attachment's `file_withheld` field says which before
    you ask.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        attachment_id=attachment_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_content_version: UUID,
    attachment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | File | HTTPValidationError | ServiceUnavailableError | None:
    """Download a content attachment

     Download an attached file's bytes.

    Images, audio, video, PDF and plain text are served with their own type; an SVG that cannot be
    sanitized, and anything else, is served as `application/octet-stream`.

    Answers 403 when the file is withheld: a governance policy blocked or redacted it, or it arrived
    from outside and is still being indexed. The attachment's `file_withheld` field says which before
    you ask.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access attachments of content
    belonging to your account.

    Args:
        source_connection_content_version (UUID):
        attachment_id (UUID):
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
            source_connection_content_version=source_connection_content_version,
            attachment_id=attachment_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
