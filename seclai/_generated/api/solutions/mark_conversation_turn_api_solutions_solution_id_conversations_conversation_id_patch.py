from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.mark_conversation_turn_request import MarkConversationTurnRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    solution_id: UUID,
    conversation_id: UUID,
    *,
    body: MarkConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/solutions/{solution_id}/conversations/{conversation_id}".format(
            solution_id=quote(str(solution_id), safe=""),
            conversation_id=quote(str(conversation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    solution_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Mark conversation turn

     Mark a conversation turn as accepted or declined.

    Updates the `accepted` field on an existing conversation turn. Use this after reviewing a proposed
    plan to record whether it was accepted or declined by the user.

    Args:
        solution_id (UUID):
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MarkConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    solution_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Mark conversation turn

     Mark a conversation turn as accepted or declined.

    Updates the `accepted` field on an existing conversation turn. Use this after reviewing a proposed
    plan to record whether it was accepted or declined by the user.

    Args:
        solution_id (UUID):
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MarkConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        solution_id=solution_id,
        conversation_id=conversation_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    solution_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Mark conversation turn

     Mark a conversation turn as accepted or declined.

    Updates the `accepted` field on an existing conversation turn. Use this after reviewing a proposed
    plan to record whether it was accepted or declined by the user.

    Args:
        solution_id (UUID):
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MarkConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        conversation_id=conversation_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    solution_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Mark conversation turn

     Mark a conversation turn as accepted or declined.

    Updates the `accepted` field on an existing conversation turn. Use this after reviewing a proposed
    plan to record whether it was accepted or declined by the user.

    Args:
        solution_id (UUID):
        conversation_id (UUID):
        x_account_id (UUID | Unset):
        body (MarkConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            solution_id=solution_id,
            conversation_id=conversation_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
