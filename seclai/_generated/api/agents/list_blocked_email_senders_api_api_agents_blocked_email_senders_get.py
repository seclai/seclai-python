from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blocked_email_sender_list_response import BlockedEmailSenderListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/blocked-email-senders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BlockedEmailSenderListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BlockedEmailSenderListResponse.from_dict(response.json())

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
) -> Response[BlockedEmailSenderListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[BlockedEmailSenderListResponse | HTTPValidationError]:
    """List blocked inbound email senders + the auto-block mode

     List the account's blocked inbound email senders (newest first, paginated via `limit`/`offset`) plus
    the governance `auto_block_mode`.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockedEmailSenderListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> BlockedEmailSenderListResponse | HTTPValidationError | None:
    """List blocked inbound email senders + the auto-block mode

     List the account's blocked inbound email senders (newest first, paginated via `limit`/`offset`) plus
    the governance `auto_block_mode`.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockedEmailSenderListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[BlockedEmailSenderListResponse | HTTPValidationError]:
    """List blocked inbound email senders + the auto-block mode

     List the account's blocked inbound email senders (newest first, paginated via `limit`/`offset`) plus
    the governance `auto_block_mode`.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockedEmailSenderListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> BlockedEmailSenderListResponse | HTTPValidationError | None:
    """List blocked inbound email senders + the auto-block mode

     List the account's blocked inbound email senders (newest first, paginated via `limit`/`offset`) plus
    the governance `auto_block_mode`.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockedEmailSenderListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
