import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_memory_bank_entry_stats_api_memory_banks_memory_bank_id_stats_get_response_get_memory_bank_entry_stats_api_memory_banks_memory_bank_id_stats_get import (
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    memory_bank_id: str,
    *,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["days"] = days

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.date):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.date):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memory_banks/{memory_bank_id}/stats".format(
            memory_bank_id=quote(str(memory_bank_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet.from_dict(
            response.json()
        )

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
) -> Response[
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet
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
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet
    | HTTPValidationError
]:
    """Get Memory Bank Entry Stats

     Return aggregated entry statistics for a memory bank, including total counts, token/age/entries-per-
    key distributions (avg, p95, min, max), and top conversation keys, group keys, speakers, and tags.
    Supports time-range filtering via `days`, `start_date`, and `end_date` query parameters.

    Args:
        memory_bank_id (str):
        days (int | Unset):  Default: 30.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        days=days,
        start_date=start_date,
        end_date=end_date,
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
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> (
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet
    | HTTPValidationError
    | None
):
    """Get Memory Bank Entry Stats

     Return aggregated entry statistics for a memory bank, including total counts, token/age/entries-per-
    key distributions (avg, p95, min, max), and top conversation keys, group keys, speakers, and tags.
    Supports time-range filtering via `days`, `start_date`, and `end_date` query parameters.

    Args:
        memory_bank_id (str):
        days (int | Unset):  Default: 30.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet | HTTPValidationError
    """

    return sync_detailed(
        memory_bank_id=memory_bank_id,
        client=client,
        days=days,
        start_date=start_date,
        end_date=end_date,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet
    | HTTPValidationError
]:
    """Get Memory Bank Entry Stats

     Return aggregated entry statistics for a memory bank, including total counts, token/age/entries-per-
    key distributions (avg, p95, min, max), and top conversation keys, group keys, speakers, and tags.
    Supports time-range filtering via `days`, `start_date`, and `end_date` query parameters.

    Args:
        memory_bank_id (str):
        days (int | Unset):  Default: 30.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        days=days,
        start_date=start_date,
        end_date=end_date,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> (
    GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet
    | HTTPValidationError
    | None
):
    """Get Memory Bank Entry Stats

     Return aggregated entry statistics for a memory bank, including total counts, token/age/entries-per-
    key distributions (avg, p95, min, max), and top conversation keys, group keys, speakers, and tags.
    Supports time-range filtering via `days`, `start_date`, and `end_date` query parameters.

    Args:
        memory_bank_id (str):
        days (int | Unset):  Default: 30.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGetResponseGetMemoryBankEntryStatsApiMemoryBanksMemoryBankIdStatsGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            memory_bank_id=memory_bank_id,
            client=client,
            days=days,
            start_date=start_date,
            end_date=end_date,
            x_account_id=x_account_id,
        )
    ).parsed
