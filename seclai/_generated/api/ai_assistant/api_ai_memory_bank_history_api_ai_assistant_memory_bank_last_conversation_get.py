from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_bank_last_conversation_response import (
    MemoryBankLastConversationResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 5,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ai-assistant/memory-bank/last-conversation",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MemoryBankLastConversationResponse | None:
    if response.status_code == 200:
        response_200 = MemoryBankLastConversationResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MemoryBankLastConversationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 5,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBankLastConversationResponse]:
    """Fetch memory bank AI conversation history

     Fetch the most recent memory bank AI assistant conversation turns for the authenticated user.
    Returns turns in oldest-first order with a total count for pagination via limit/offset query
    parameters.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        limit (int | Unset): Max turns. Default: 5.
        offset (int | Unset): Skip count. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBankLastConversationResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 5,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | MemoryBankLastConversationResponse | None:
    """Fetch memory bank AI conversation history

     Fetch the most recent memory bank AI assistant conversation turns for the authenticated user.
    Returns turns in oldest-first order with a total count for pagination via limit/offset query
    parameters.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        limit (int | Unset): Max turns. Default: 5.
        offset (int | Unset): Skip count. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBankLastConversationResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 5,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBankLastConversationResponse]:
    """Fetch memory bank AI conversation history

     Fetch the most recent memory bank AI assistant conversation turns for the authenticated user.
    Returns turns in oldest-first order with a total count for pagination via limit/offset query
    parameters.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        limit (int | Unset): Max turns. Default: 5.
        offset (int | Unset): Skip count. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBankLastConversationResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 5,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | MemoryBankLastConversationResponse | None:
    """Fetch memory bank AI conversation history

     Fetch the most recent memory bank AI assistant conversation turns for the authenticated user.
    Returns turns in oldest-first order with a total count for pagination via limit/offset query
    parameters.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        limit (int | Unset): Max turns. Default: 5.
        offset (int | Unset): Skip count. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBankLastConversationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            x_account_id=x_account_id,
        )
    ).parsed
