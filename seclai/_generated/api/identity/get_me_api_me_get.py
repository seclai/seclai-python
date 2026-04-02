from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.me_response import MeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/me",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MeResponse | None:
    if response.status_code == 200:
        response_200 = MeResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MeResponse]:
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
) -> Response[MeResponse]:
    """Get current user identity

     Returns the authenticated user's personal account ID and a list of organisations they belong to.
    Each organisation entry includes the organisation's own id, display name, and account_id.  Useful
    for CLI tooling that needs to let the user pick an org context.

    Args:
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeResponse]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> MeResponse | None:
    """Get current user identity

     Returns the authenticated user's personal account ID and a list of organisations they belong to.
    Each organisation entry includes the organisation's own id, display name, and account_id.  Useful
    for CLI tooling that needs to let the user pick an org context.

    Args:
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeResponse
    """

    return sync_detailed(
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[MeResponse]:
    """Get current user identity

     Returns the authenticated user's personal account ID and a list of organisations they belong to.
    Each organisation entry includes the organisation's own id, display name, and account_id.  Useful
    for CLI tooling that needs to let the user pick an org context.

    Args:
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeResponse]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> MeResponse | None:
    """Get current user identity

     Returns the authenticated user's personal account ID and a list of organisations they belong to.
    Each organisation entry includes the organisation's own id, display name, and account_id.  Useful
    for CLI tooling that needs to let the user pick an org context.

    Args:
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
