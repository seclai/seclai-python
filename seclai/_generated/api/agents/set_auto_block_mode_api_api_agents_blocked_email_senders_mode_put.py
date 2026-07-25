from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blocked_email_sender_list_response import BlockedEmailSenderListResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.set_auto_block_mode_request import SetAutoBlockModeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SetAutoBlockModeRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/agents/blocked-email-senders/mode",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    body: SetAutoBlockModeRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[BlockedEmailSenderListResponse | HTTPValidationError]:
    """Set the governance auto-block mode

     Set whether a governance BLOCK on an authenticated inbound email sender auto-adds them to the
    blocklist (`disabled`, `input`, or `input_and_output`); returns the updated list.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        body (SetAutoBlockModeRequest): Set the account's governance auto-block mode (shared REST
            request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockedEmailSenderListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SetAutoBlockModeRequest,
    x_account_id: UUID | Unset = UNSET,
) -> BlockedEmailSenderListResponse | HTTPValidationError | None:
    """Set the governance auto-block mode

     Set whether a governance BLOCK on an authenticated inbound email sender auto-adds them to the
    blocklist (`disabled`, `input`, or `input_and_output`); returns the updated list.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        body (SetAutoBlockModeRequest): Set the account's governance auto-block mode (shared REST
            request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockedEmailSenderListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetAutoBlockModeRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[BlockedEmailSenderListResponse | HTTPValidationError]:
    """Set the governance auto-block mode

     Set whether a governance BLOCK on an authenticated inbound email sender auto-adds them to the
    blocklist (`disabled`, `input`, or `input_and_output`); returns the updated list.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        body (SetAutoBlockModeRequest): Set the account's governance auto-block mode (shared REST
            request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockedEmailSenderListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetAutoBlockModeRequest,
    x_account_id: UUID | Unset = UNSET,
) -> BlockedEmailSenderListResponse | HTTPValidationError | None:
    """Set the governance auto-block mode

     Set whether a governance BLOCK on an authenticated inbound email sender auto-adds them to the
    blocklist (`disabled`, `input`, or `input_and_output`); returns the updated list.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token for an account owner/admin; scoped
    to the key's account.

    Args:
        x_account_id (UUID | Unset):
        body (SetAutoBlockModeRequest): Set the account's governance auto-block mode (shared REST
            request).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockedEmailSenderListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
