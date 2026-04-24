from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ai_memory_bank_accept_api_ai_assistant_memory_bank_conversation_id_patch_response_api_ai_memory_bank_accept_api_ai_assistant_memory_bank_conversation_id_patch import (
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_bank_accept_request import MemoryBankAcceptRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: UUID,
    *,
    body: MemoryBankAcceptRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ai-assistant/memory-bank/{conversation_id}".format(
            conversation_id=quote(str(conversation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch.from_dict(
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
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MemoryBankAcceptRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch
    | HTTPValidationError
]:
    """Accept or decline a memory bank AI suggestion

     Update the acceptance status of a memory bank AI assistant conversation turn. Set ``accepted`` to
    true to accept the proposed configuration, or false to decline it. The accepted status is recorded
    for audit purposes.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MemoryBankAcceptRequest): Accept or decline a memory bank AI suggestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MemoryBankAcceptRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch
    | HTTPValidationError
    | None
):
    """Accept or decline a memory bank AI suggestion

     Update the acceptance status of a memory bank AI assistant conversation turn. Set ``accepted`` to
    true to accept the proposed configuration, or false to decline it. The accepted status is recorded
    for audit purposes.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MemoryBankAcceptRequest): Accept or decline a memory bank AI suggestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch | HTTPValidationError
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MemoryBankAcceptRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch
    | HTTPValidationError
]:
    """Accept or decline a memory bank AI suggestion

     Update the acceptance status of a memory bank AI assistant conversation turn. Set ``accepted`` to
    true to accept the proposed configuration, or false to decline it. The accepted status is recorded
    for audit purposes.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MemoryBankAcceptRequest): Accept or decline a memory bank AI suggestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MemoryBankAcceptRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch
    | HTTPValidationError
    | None
):
    """Accept or decline a memory bank AI suggestion

     Update the acceptance status of a memory bank AI assistant conversation turn. Set ``accepted`` to
    true to accept the proposed configuration, or false to decline it. The accepted status is recorded
    for audit purposes.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MemoryBankAcceptRequest): Accept or decline a memory bank AI suggestion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatchResponseApiAiMemoryBankAcceptApiAiAssistantMemoryBankConversationIdPatch | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
