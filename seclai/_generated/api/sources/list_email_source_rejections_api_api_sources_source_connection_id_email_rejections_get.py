from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_source_rejection_list_response import (
    EmailSourceRejectionListResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/{source_connection_id}/email-rejections".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EmailSourceRejectionListResponse
    | HTTPValidationError
    | ServiceUnavailableError
    | None
):
    if response.status_code == 200:
        response_200 = EmailSourceRejectionListResponse.from_dict(response.json())

        return response_200

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
    EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError
]:
    """List mail an email source refused

     List mail that an email content source refused, newest first. Each entry says who sent the message
    and why it was refused, never its subject or body. A message refused as `unsafe_content` also has a
    prompt-scan record, which keeps the scanned text.

    To accept a refused sender, add its `from_address` or that address's domain to the source's
    `email_allowed_senders`. That only helps when `authenticated` is true. A `repeat_*` reason marks a
    message the source received before; allowing its sender does not store it.

    Requires an account owner or administrator: a key or token bound to another member gets 403. Returns
    404 for a source that is not an email source.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number. Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    EmailSourceRejectionListResponse
    | HTTPValidationError
    | ServiceUnavailableError
    | None
):
    """List mail an email source refused

     List mail that an email content source refused, newest first. Each entry says who sent the message
    and why it was refused, never its subject or body. A message refused as `unsafe_content` also has a
    prompt-scan record, which keeps the scanned text.

    To accept a refused sender, add its `from_address` or that address's domain to the source's
    `email_allowed_senders`. That only helps when `authenticated` is true. A `repeat_*` reason marks a
    message the source received before; allowing its sender does not store it.

    Requires an account owner or administrator: a key or token bound to another member gets 403. Returns
    404 for a source that is not an email source.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number. Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError
]:
    """List mail an email source refused

     List mail that an email content source refused, newest first. Each entry says who sent the message
    and why it was refused, never its subject or body. A message refused as `unsafe_content` also has a
    prompt-scan record, which keeps the scanned text.

    To accept a refused sender, add its `from_address` or that address's domain to the source's
    `email_allowed_senders`. That only helps when `authenticated` is true. A `repeat_*` reason marks a
    message the source received before; allowing its sender does not store it.

    Requires an account owner or administrator: a key or token bound to another member gets 403. Returns
    404 for a source that is not an email source.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number. Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    EmailSourceRejectionListResponse
    | HTTPValidationError
    | ServiceUnavailableError
    | None
):
    """List mail an email source refused

     List mail that an email content source refused, newest first. Each entry says who sent the message
    and why it was refused, never its subject or body. A message refused as `unsafe_content` also has a
    prompt-scan record, which keeps the scanned text.

    To accept a refused sender, add its `from_address` or that address's domain to the source's
    `email_allowed_senders`. That only helps when `authenticated` is true. A `repeat_*` reason marks a
    message the source received before; allowing its sender does not store it.

    Requires an account owner or administrator: a key or token bound to another member gets 403. Returns
    404 for a source that is not an email source.

    Args:
        source_connection_id (UUID):
        page (int | Unset): Page number. Default: 1.
        limit (int | Unset): Items per page. Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailSourceRejectionListResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            page=page,
            limit=limit,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
