from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_bank_ai_assistant_request import MemoryBankAiAssistantRequest
from ...models.memory_bank_ai_assistant_response import MemoryBankAiAssistantResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MemoryBankAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ai-assistant/memory-bank",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MemoryBankAiAssistantResponse | None:
    if response.status_code == 200:
        response_200 = MemoryBankAiAssistantResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MemoryBankAiAssistantResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MemoryBankAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBankAiAssistantResponse]:
    """Generate a memory bank configuration (standalone)

     Generate a memory bank configuration suggestion via the AI assistant. The AI proposes name, type,
    mode, compaction prompt, and retention settings.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (MemoryBankAiAssistantRequest): Request body for the memory bank AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBankAiAssistantResponse]
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
    body: MemoryBankAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | MemoryBankAiAssistantResponse | None:
    """Generate a memory bank configuration (standalone)

     Generate a memory bank configuration suggestion via the AI assistant. The AI proposes name, type,
    mode, compaction prompt, and retention settings.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (MemoryBankAiAssistantRequest): Request body for the memory bank AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBankAiAssistantResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MemoryBankAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBankAiAssistantResponse]:
    """Generate a memory bank configuration (standalone)

     Generate a memory bank configuration suggestion via the AI assistant. The AI proposes name, type,
    mode, compaction prompt, and retention settings.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (MemoryBankAiAssistantRequest): Request body for the memory bank AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBankAiAssistantResponse]
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
    body: MemoryBankAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | MemoryBankAiAssistantResponse | None:
    """Generate a memory bank configuration (standalone)

     Generate a memory bank configuration suggestion via the AI assistant. The AI proposes name, type,
    mode, compaction prompt, and retention settings.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (MemoryBankAiAssistantRequest): Request body for the memory bank AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBankAiAssistantResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
