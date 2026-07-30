from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.mark_ai_suggestion_request import MarkAiSuggestionRequest
from ...models.ok_response import OkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    conversation_id: str,
    *,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

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
) -> HTTPValidationError | OkResponse | None:
    if response.status_code == 200:
        response_200 = OkResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | OkResponse]:
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
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | OkResponse]:
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
        seclai_version (str | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OkResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
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
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | OkResponse | None:
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
        seclai_version (str | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OkResponse
    """

    return sync_detailed(
        agent_id=agent_id,
        conversation_id=conversation_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkAiSuggestionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | OkResponse]:
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
        seclai_version (str | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OkResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
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
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | OkResponse | None:
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
        seclai_version (str | Unset):
        body (MarkAiSuggestionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OkResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            conversation_id=conversation_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
