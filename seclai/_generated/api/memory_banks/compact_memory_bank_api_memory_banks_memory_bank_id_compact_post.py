from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compact_memory_bank_api_memory_banks_memory_bank_id_compact_post_response_compact_memory_bank_api_memory_banks_memory_bank_id_compact_post import (
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    memory_bank_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/memory_banks/{memory_bank_id}/compact".format(
            memory_bank_id=quote(str(memory_bank_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost
    | HTTPValidationError
    | None
):
    if response.status_code == 202:
        response_202 = CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost.from_dict(
            response.json()
        )

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost
    | HTTPValidationError
]:
    """Compact Memory Bank

     Trigger an on-demand compaction run for a memory bank.

    The bank must have at least one compaction threshold configured (max_age_days, max_turns, or
    max_size_tokens). Compaction runs asynchronously — the response confirms scheduling, not completion.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> (
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost
    | HTTPValidationError
    | None
):
    """Compact Memory Bank

     Trigger an on-demand compaction run for a memory bank.

    The bank must have at least one compaction threshold configured (max_age_days, max_turns, or
    max_size_tokens). Compaction runs asynchronously — the response confirms scheduling, not completion.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost | HTTPValidationError
    """

    return sync_detailed(
        memory_bank_id=memory_bank_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost
    | HTTPValidationError
]:
    """Compact Memory Bank

     Trigger an on-demand compaction run for a memory bank.

    The bank must have at least one compaction threshold configured (max_age_days, max_turns, or
    max_size_tokens). Compaction runs asynchronously — the response confirms scheduling, not completion.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> (
    CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost
    | HTTPValidationError
    | None
):
    """Compact Memory Bank

     Trigger an on-demand compaction run for a memory bank.

    The bank must have at least one compaction threshold configured (max_age_days, max_turns, or
    max_size_tokens). Compaction runs asynchronously — the response confirms scheduling, not completion.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompactMemoryBankApiMemoryBanksMemoryBankIdCompactPostResponseCompactMemoryBankApiMemoryBanksMemoryBankIdCompactPost | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            memory_bank_id=memory_bank_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
