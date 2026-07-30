from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_domain_response import EmailDomainResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    domain_id: UUID,
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
        "url": "/email-domains/{domain_id}/primary".format(
            domain_id=quote(str(domain_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailDomainResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EmailDomainResponse.from_dict(response.json())

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
) -> Response[EmailDomainResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[EmailDomainResponse | HTTPValidationError]:
    """Make a verified domain the account's primary sending/inbound domain

     Promote a verified domain to the account's primary domain — agent email then sends FROM and receives
    ON this domain (`<agentID>@<domain>`, `<alias>@<domain>`) instead of the shared `agent.seclai.com`.
    The domain must be verified. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailDomainResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> EmailDomainResponse | HTTPValidationError | None:
    """Make a verified domain the account's primary sending/inbound domain

     Promote a verified domain to the account's primary domain — agent email then sends FROM and receives
    ON this domain (`<agentID>@<domain>`, `<alias>@<domain>`) instead of the shared `agent.seclai.com`.
    The domain must be verified. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailDomainResponse | HTTPValidationError
    """

    return sync_detailed(
        domain_id=domain_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[EmailDomainResponse | HTTPValidationError]:
    """Make a verified domain the account's primary sending/inbound domain

     Promote a verified domain to the account's primary domain — agent email then sends FROM and receives
    ON this domain (`<agentID>@<domain>`, `<alias>@<domain>`) instead of the shared `agent.seclai.com`.
    The domain must be verified. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailDomainResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> EmailDomainResponse | HTTPValidationError | None:
    """Make a verified domain the account's primary sending/inbound domain

     Promote a verified domain to the account's primary domain — agent email then sends FROM and receives
    ON this domain (`<agentID>@<domain>`, `<alias>@<domain>`) instead of the shared `agent.seclai.com`.
    The domain must be verified. Owner/admin only.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailDomainResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            domain_id=domain_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
