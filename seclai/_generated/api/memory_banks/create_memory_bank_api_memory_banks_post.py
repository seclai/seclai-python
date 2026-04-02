from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_memory_bank_body import CreateMemoryBankBody
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_bank import MemoryBank
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateMemoryBankBody,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/memory_banks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MemoryBank | None:
    if response.status_code == 201:
        response_201 = MemoryBank.from_dict(response.json())

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
) -> Response[HTTPValidationError | MemoryBank]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateMemoryBankBody,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBank]:
    """Create Memory Bank

     Create a new memory bank.

    Modes: `fast_and_cheap` (256-dim), `balanced` (512-dim), `slow_and_thorough` (1024-dim), or `custom`
    (supply your own embedding params).

    Args:
        x_account_id (UUID | Unset):
        body (CreateMemoryBankBody): Request body for creating a memory bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBank]
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
    body: CreateMemoryBankBody,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | MemoryBank | None:
    """Create Memory Bank

     Create a new memory bank.

    Modes: `fast_and_cheap` (256-dim), `balanced` (512-dim), `slow_and_thorough` (1024-dim), or `custom`
    (supply your own embedding params).

    Args:
        x_account_id (UUID | Unset):
        body (CreateMemoryBankBody): Request body for creating a memory bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBank
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateMemoryBankBody,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBank]:
    """Create Memory Bank

     Create a new memory bank.

    Modes: `fast_and_cheap` (256-dim), `balanced` (512-dim), `slow_and_thorough` (1024-dim), or `custom`
    (supply your own embedding params).

    Args:
        x_account_id (UUID | Unset):
        body (CreateMemoryBankBody): Request body for creating a memory bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBank]
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
    body: CreateMemoryBankBody,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | MemoryBank | None:
    """Create Memory Bank

     Create a new memory bank.

    Modes: `fast_and_cheap` (256-dim), `balanced` (512-dim), `slow_and_thorough` (1024-dim), or `custom`
    (supply your own embedding params).

    Args:
        x_account_id (UUID | Unset):
        body (CreateMemoryBankBody): Request body for creating a memory bank.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBank
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
