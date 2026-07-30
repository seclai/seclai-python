from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.inbound_email_status_response import InboundEmailStatusResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/agents/inbound-email-status",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InboundEmailStatusResponse | None:
    if response.status_code == 200:
        response_200 = InboundEmailStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InboundEmailStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[InboundEmailStatusResponse]:
    """Account inbound-email overload status

     Whether the account-wide overload circuit breaker has currently paused new inbound email (all
    inbound turned away until the queued backlog drains), plus the size of the QUEUED (over-quota
    parked) run backlog.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InboundEmailStatusResponse]
    """

    kwargs = _get_kwargs(
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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> InboundEmailStatusResponse | None:
    """Account inbound-email overload status

     Whether the account-wide overload circuit breaker has currently paused new inbound email (all
    inbound turned away until the queued backlog drains), plus the size of the QUEUED (over-quota
    parked) run backlog.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InboundEmailStatusResponse
    """

    return sync_detailed(
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[InboundEmailStatusResponse]:
    """Account inbound-email overload status

     Whether the account-wide overload circuit breaker has currently paused new inbound email (all
    inbound turned away until the queued backlog drains), plus the size of the QUEUED (over-quota
    parked) run backlog.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InboundEmailStatusResponse]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> InboundEmailStatusResponse | None:
    """Account inbound-email overload status

     Whether the account-wide overload circuit breaker has currently paused new inbound email (all
    inbound turned away until the queued backlog drains), plus the size of the QUEUED (over-quota
    parked) run backlog.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; always scoped to the key's
    account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InboundEmailStatusResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
