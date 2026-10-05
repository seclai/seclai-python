from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_unavailable_error import ServiceUnavailableError
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
        "method": "post",
        "url": "/email-domains/use-shared-domain",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ServiceUnavailableError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 503:
        response_503 = ServiceUnavailableError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ServiceUnavailableError]:
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
) -> Response[Any | ServiceUnavailableError]:
    """Revert to the shared agent.seclai.com sending domain

     Clear the account's primary domain so agent email reverts to the shared `agent.seclai.com` sending
    domain, WITHOUT removing the configured domain(s) — they stay verified and can be promoted again
    later. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServiceUnavailableError]
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
) -> Any | ServiceUnavailableError | None:
    """Revert to the shared agent.seclai.com sending domain

     Clear the account's primary domain so agent email reverts to the shared `agent.seclai.com` sending
    domain, WITHOUT removing the configured domain(s) — they stay verified and can be promoted again
    later. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServiceUnavailableError
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
) -> Response[Any | ServiceUnavailableError]:
    """Revert to the shared agent.seclai.com sending domain

     Clear the account's primary domain so agent email reverts to the shared `agent.seclai.com` sending
    domain, WITHOUT removing the configured domain(s) — they stay verified and can be promoted again
    later. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServiceUnavailableError]
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
) -> Any | ServiceUnavailableError | None:
    """Revert to the shared agent.seclai.com sending domain

     Clear the account's primary domain so agent email reverts to the shared `agent.seclai.com` sending
    domain, WITHOUT removing the configured domain(s) — they stay verified and can be promoted again
    later. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
