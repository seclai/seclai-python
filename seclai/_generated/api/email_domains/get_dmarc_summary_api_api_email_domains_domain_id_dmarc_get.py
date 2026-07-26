from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dmarc_summary_response import DmarcSummaryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    domain_id: UUID,
    *,
    days: int | Unset = 30,
    top_sources: int | Unset = 10,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["days"] = days

    params["top_sources"] = top_sources

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/email-domains/{domain_id}/dmarc".format(
            domain_id=quote(str(domain_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DmarcSummaryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DmarcSummaryResponse.from_dict(response.json())

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
) -> Response[DmarcSummaryResponse | HTTPValidationError]:
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
    days: int | Unset = 30,
    top_sources: int | Unset = 10,
    x_account_id: UUID | Unset = UNSET,
) -> Response[DmarcSummaryResponse | HTTPValidationError]:
    """DMARC aggregate-report summary for a domain

     Pass rate, disposition breakdown (`none`/`quarantine`/`reject`), and top failing source IPs from the
    DMARC `rua` aggregate reports over the last `days` (clamped by the service). Populated for domains
    whose DNS zone Seclai controls (vanity + delegated custom); a self-managed custom domain keeps its
    own DMARC reporting and returns an all-zero summary.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        days (int | Unset):  Default: 30.
        top_sources (int | Unset):  Default: 10.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DmarcSummaryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        days=days,
        top_sources=top_sources,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    top_sources: int | Unset = 10,
    x_account_id: UUID | Unset = UNSET,
) -> DmarcSummaryResponse | HTTPValidationError | None:
    """DMARC aggregate-report summary for a domain

     Pass rate, disposition breakdown (`none`/`quarantine`/`reject`), and top failing source IPs from the
    DMARC `rua` aggregate reports over the last `days` (clamped by the service). Populated for domains
    whose DNS zone Seclai controls (vanity + delegated custom); a self-managed custom domain keeps its
    own DMARC reporting and returns an all-zero summary.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        days (int | Unset):  Default: 30.
        top_sources (int | Unset):  Default: 10.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DmarcSummaryResponse | HTTPValidationError
    """

    return sync_detailed(
        domain_id=domain_id,
        client=client,
        days=days,
        top_sources=top_sources,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    top_sources: int | Unset = 10,
    x_account_id: UUID | Unset = UNSET,
) -> Response[DmarcSummaryResponse | HTTPValidationError]:
    """DMARC aggregate-report summary for a domain

     Pass rate, disposition breakdown (`none`/`quarantine`/`reject`), and top failing source IPs from the
    DMARC `rua` aggregate reports over the last `days` (clamped by the service). Populated for domains
    whose DNS zone Seclai controls (vanity + delegated custom); a self-managed custom domain keeps its
    own DMARC reporting and returns an all-zero summary.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        days (int | Unset):  Default: 30.
        top_sources (int | Unset):  Default: 10.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DmarcSummaryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        days=days,
        top_sources=top_sources,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    top_sources: int | Unset = 10,
    x_account_id: UUID | Unset = UNSET,
) -> DmarcSummaryResponse | HTTPValidationError | None:
    """DMARC aggregate-report summary for a domain

     Pass rate, disposition breakdown (`none`/`quarantine`/`reject`), and top failing source IPs from the
    DMARC `rua` aggregate reports over the last `days` (clamped by the service). Populated for domains
    whose DNS zone Seclai controls (vanity + delegated custom); a self-managed custom domain keeps its
    own DMARC reporting and returns an all-zero summary.

    Auth & scoping: requires an `X-API-Key` header or OAuth Bearer token bound to a **user** (an
    account-only key is refused with 403); the domain is scoped to the key's account.

    Args:
        domain_id (UUID):
        days (int | Unset):  Default: 30.
        top_sources (int | Unset):  Default: 10.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DmarcSummaryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            domain_id=domain_id,
            client=client,
            days=days,
            top_sources=top_sources,
            x_account_id=x_account_id,
        )
    ).parsed
