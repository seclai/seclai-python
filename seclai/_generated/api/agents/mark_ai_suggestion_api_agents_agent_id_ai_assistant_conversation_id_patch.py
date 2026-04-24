from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.mark_ai_suggestion_api_agents_agent_id_ai_assistant_conversation_id_patch_response_mark_ai_suggestion_api_agents_agent_id_ai_assistant_conversation_id_patch import (
    MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch,
)
from ...models.mark_ai_suggestion_request import MarkAiSuggestionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    conversation_id: str,
    *,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/agents/{agent_id}/ai-assistant/{conversation_id}".format(
            agent_id=quote(str(agent_id), safe=""),
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
    HTTPValidationError
    | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
    | None
):
    if response.status_code == 200:
        response_200 = MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch.from_dict(
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
    HTTPValidationError
    | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
]:
    """Accept or decline suggestion

     Accept or decline a proposed AI assistant configuration for a conversation turn.

    This only updates the tracking status on the conversation record. To actually apply the proposed
    configuration, use the agent definition update endpoint separately.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The conversation must belong to one of your
    agents.

    Args:
        agent_id (str):
        conversation_id (str):
        x_account_id (UUID | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
    | None
):
    """Accept or decline suggestion

     Accept or decline a proposed AI assistant configuration for a conversation turn.

    This only updates the tracking status on the conversation record. To actually apply the proposed
    configuration, use the agent definition update endpoint separately.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The conversation must belong to one of your
    agents.

    Args:
        agent_id (str):
        conversation_id (str):
        x_account_id (UUID | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
    """

    return sync_detailed(
        agent_id=agent_id,
        conversation_id=conversation_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
]:
    """Accept or decline suggestion

     Accept or decline a proposed AI assistant configuration for a conversation turn.

    This only updates the tracking status on the conversation record. To actually apply the proposed
    configuration, use the agent definition update endpoint separately.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The conversation must belong to one of your
    agents.

    Args:
        agent_id (str):
        conversation_id (str):
        x_account_id (UUID | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
    | None
):
    """Accept or decline suggestion

     Accept or decline a proposed AI assistant configuration for a conversation turn.

    This only updates the tracking status on the conversation record. To actually apply the proposed
    configuration, use the agent definition update endpoint separately.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The conversation must belong to one of your
    agents.

    Args:
        agent_id (str):
        conversation_id (str):
        x_account_id (UUID | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatchResponseMarkAiSuggestionApiAgentsAgentIdAiAssistantConversationIdPatch
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            conversation_id=conversation_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
