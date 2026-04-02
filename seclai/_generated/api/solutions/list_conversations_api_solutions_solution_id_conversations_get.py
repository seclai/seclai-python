from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.solution_conversation_response import SolutionConversationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    solution_id: UUID,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/solutions/{solution_id}/conversations".format(
            solution_id=quote(str(solution_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[SolutionConversationResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SolutionConversationResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[SolutionConversationResponse]]:
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
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | list[SolutionConversationResponse]]:
    """List conversations

     List AI assistant conversation history for a solution.

    Returns all conversation turns for the given solution, including user inputs, AI responses, proposed
    actions, and acceptance status.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SolutionConversationResponse]]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
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
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | list[SolutionConversationResponse] | None:
    """List conversations

     List AI assistant conversation history for a solution.

    Returns all conversation turns for the given solution, including user inputs, AI responses, proposed
    actions, and acceptance status.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SolutionConversationResponse]
    """

    return sync_detailed(
        solution_id=solution_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | list[SolutionConversationResponse]]:
    """List conversations

     List AI assistant conversation history for a solution.

    Returns all conversation turns for the given solution, including user inputs, AI responses, proposed
    actions, and acceptance status.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SolutionConversationResponse]]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | list[SolutionConversationResponse] | None:
    """List conversations

     List AI assistant conversation history for a solution.

    Returns all conversation turns for the given solution, including user inputs, AI responses, proposed
    actions, and acceptance status.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SolutionConversationResponse]
    """

    return (
        await asyncio_detailed(
            solution_id=solution_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
