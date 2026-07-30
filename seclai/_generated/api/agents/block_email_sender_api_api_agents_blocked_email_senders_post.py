from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_email_sender_request import BlockEmailSenderRequest
from ...models.blocked_email_sender_response import BlockedEmailSenderResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BlockEmailSenderRequest,
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
        "url": "/agents/blocked-email-senders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BlockedEmailSenderResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = BlockedEmailSenderResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BlockedEmailSenderResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BlockEmailSenderRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[BlockedEmailSenderResponse | HTTPValidationError]:
    """Block an inbound email sender or domain

     Add a sender address or a whole domain to the account blocklist (idempotent; `match_type` is
    `address` (default) or `domain`).

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BlockEmailSenderRequest): Add one sender/domain to the account blocklist (shared
            REST request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockedEmailSenderResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: BlockEmailSenderRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> BlockedEmailSenderResponse | HTTPValidationError | None:
    """Block an inbound email sender or domain

     Add a sender address or a whole domain to the account blocklist (idempotent; `match_type` is
    `address` (default) or `domain`).

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BlockEmailSenderRequest): Add one sender/domain to the account blocklist (shared
            REST request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockedEmailSenderResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BlockEmailSenderRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[BlockedEmailSenderResponse | HTTPValidationError]:
    """Block an inbound email sender or domain

     Add a sender address or a whole domain to the account blocklist (idempotent; `match_type` is
    `address` (default) or `domain`).

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BlockEmailSenderRequest): Add one sender/domain to the account blocklist (shared
            REST request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockedEmailSenderResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BlockEmailSenderRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> BlockedEmailSenderResponse | HTTPValidationError | None:
    """Block an inbound email sender or domain

     Add a sender address or a whole domain to the account blocklist (idempotent; `match_type` is
    `address` (default) or `domain`).

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (BlockEmailSenderRequest): Add one sender/domain to the account blocklist (shared
            REST request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockedEmailSenderResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
