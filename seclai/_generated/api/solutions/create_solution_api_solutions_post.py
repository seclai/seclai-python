from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_solution_request import CreateSolutionRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.solution_response import SolutionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSolutionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/solutions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SolutionResponse | None:
    if response.status_code == 201:
        response_201 = SolutionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SolutionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSolutionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | SolutionResponse]:
    """Create a solution

     Create a new solution for the caller's account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Provide a
    `name` and optional `description` in the request body.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSolutionRequest): Request model for creating a new solution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionResponse]
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
    body: CreateSolutionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | SolutionResponse | None:
    """Create a solution

     Create a new solution for the caller's account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Provide a
    `name` and optional `description` in the request body.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSolutionRequest): Request model for creating a new solution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSolutionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | SolutionResponse]:
    """Create a solution

     Create a new solution for the caller's account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Provide a
    `name` and optional `description` in the request body.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSolutionRequest): Request model for creating a new solution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionResponse]
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
    body: CreateSolutionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | SolutionResponse | None:
    """Create a solution

     Create a new solution for the caller's account.

    A *solution* groups agents, knowledge bases, and content sources into a cohesive unit. Provide a
    `name` and optional `description` in the request body.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSolutionRequest): Request model for creating a new solution

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
