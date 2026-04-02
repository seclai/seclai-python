from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_conversation_history_response import AiConversationHistoryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    step_type: str,
    step_id: None | str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["step_type"] = step_type

    json_step_id: None | str | Unset
    if isinstance(step_id, Unset):
        json_step_id = UNSET
    else:
        json_step_id = step_id
    params["step_id"] = json_step_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/ai-assistant/conversations".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AiConversationHistoryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AiConversationHistoryResponse.from_dict(response.json())

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
) -> Response[AiConversationHistoryResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    step_type: str,
    step_id: None | str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    x_account_id: str | Unset = UNSET,
) -> Response[AiConversationHistoryResponse | HTTPValidationError]:
    """Get AI conversation history

     Fetch the AI assistant conversation history for a specific step of an agent.

    Returns past conversation turns (user inputs, AI responses, accept/decline status) ordered oldest
    first. Use `step_type` to filter by step type, and optionally `step_id` to narrow to a specific step
    instance.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    queried.

    Args:
        agent_id (str):
        step_type (str): Step type to look up.
        step_id (None | str | Unset): Step ID to filter by.
        limit (int | Unset): Max turns to return. Default: 10.
        offset (int | Unset): Number of recent turns to skip. Default: 0.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiConversationHistoryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        step_type=step_type,
        step_id=step_id,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    step_type: str,
    step_id: None | str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    x_account_id: str | Unset = UNSET,
) -> AiConversationHistoryResponse | HTTPValidationError | None:
    """Get AI conversation history

     Fetch the AI assistant conversation history for a specific step of an agent.

    Returns past conversation turns (user inputs, AI responses, accept/decline status) ordered oldest
    first. Use `step_type` to filter by step type, and optionally `step_id` to narrow to a specific step
    instance.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    queried.

    Args:
        agent_id (str):
        step_type (str): Step type to look up.
        step_id (None | str | Unset): Step ID to filter by.
        limit (int | Unset): Max turns to return. Default: 10.
        offset (int | Unset): Number of recent turns to skip. Default: 0.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiConversationHistoryResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        step_type=step_type,
        step_id=step_id,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    step_type: str,
    step_id: None | str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    x_account_id: str | Unset = UNSET,
) -> Response[AiConversationHistoryResponse | HTTPValidationError]:
    """Get AI conversation history

     Fetch the AI assistant conversation history for a specific step of an agent.

    Returns past conversation turns (user inputs, AI responses, accept/decline status) ordered oldest
    first. Use `step_type` to filter by step type, and optionally `step_id` to narrow to a specific step
    instance.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    queried.

    Args:
        agent_id (str):
        step_type (str): Step type to look up.
        step_id (None | str | Unset): Step ID to filter by.
        limit (int | Unset): Max turns to return. Default: 10.
        offset (int | Unset): Number of recent turns to skip. Default: 0.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiConversationHistoryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        step_type=step_type,
        step_id=step_id,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    step_type: str,
    step_id: None | str | Unset = UNSET,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    x_account_id: str | Unset = UNSET,
) -> AiConversationHistoryResponse | HTTPValidationError | None:
    """Get AI conversation history

     Fetch the AI assistant conversation history for a specific step of an agent.

    Returns past conversation turns (user inputs, AI responses, accept/decline status) ordered oldest
    first. Use `step_type` to filter by step type, and optionally `step_id` to narrow to a specific step
    instance.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    queried.

    Args:
        agent_id (str):
        step_type (str): Step type to look up.
        step_id (None | str | Unset): Step ID to filter by.
        limit (int | Unset): Max turns to return. Default: 10.
        offset (int | Unset): Number of recent turns to skip. Default: 0.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiConversationHistoryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            step_type=step_type,
            step_id=step_id,
            limit=limit,
            offset=offset,
            x_account_id=x_account_id,
        )
    ).parsed
