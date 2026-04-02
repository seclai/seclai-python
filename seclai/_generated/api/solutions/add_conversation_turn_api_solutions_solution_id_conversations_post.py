from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_conversation_turn_request import AddConversationTurnRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.solution_conversation_response import SolutionConversationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    solution_id: UUID,
    *,
    body: AddConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/solutions/{solution_id}/conversations".format(
            solution_id=quote(str(solution_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SolutionConversationResponse | None:
    if response.status_code == 201:
        response_201 = SolutionConversationResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SolutionConversationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AddConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | SolutionConversationResponse]:
    """Add conversation turn

     Add a conversation turn to a solution's AI assistant history.

    Records a user input and optional AI response and actions taken. This is typically called internally
    by AI assistant endpoints, but can also be used to manually log interactions.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AddConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionConversationResponse]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AddConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | SolutionConversationResponse | None:
    """Add conversation turn

     Add a conversation turn to a solution's AI assistant history.

    Records a user input and optional AI response and actions taken. This is typically called internally
    by AI assistant endpoints, but can also be used to manually log interactions.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AddConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionConversationResponse
    """

    return sync_detailed(
        solution_id=solution_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AddConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | SolutionConversationResponse]:
    """Add conversation turn

     Add a conversation turn to a solution's AI assistant history.

    Records a user input and optional AI response and actions taken. This is typically called internally
    by AI assistant endpoints, but can also be used to manually log interactions.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AddConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionConversationResponse]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AddConversationTurnRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | SolutionConversationResponse | None:
    """Add conversation turn

     Add a conversation turn to a solution's AI assistant history.

    Records a user input and optional AI response and actions taken. This is typically called internally
    by AI assistant endpoints, but can also be used to manually log interactions.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AddConversationTurnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionConversationResponse
    """

    return (
        await asyncio_detailed(
            solution_id=solution_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
