from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.solution_response import SolutionResponse
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
        "url": "/solutions/{solution_id}".format(
            solution_id=quote(str(solution_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SolutionResponse | None:
    if response.status_code == 200:
        response_200 = SolutionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SolutionResponse]:
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
) -> Response[HTTPValidationError | SolutionResponse]:
    """Get a solution

     Retrieve a solution by its ID, including all linked agents, knowledge bases, and source connections.

    Returns the full solution detail with nested resource information.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionResponse]
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
) -> HTTPValidationError | SolutionResponse | None:
    """Get a solution

     Retrieve a solution by its ID, including all linked agents, knowledge bases, and source connections.

    Returns the full solution detail with nested resource information.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionResponse
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
) -> Response[HTTPValidationError | SolutionResponse]:
    """Get a solution

     Retrieve a solution by its ID, including all linked agents, knowledge bases, and source connections.

    Returns the full solution detail with nested resource information.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SolutionResponse]
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
) -> HTTPValidationError | SolutionResponse | None:
    """Get a solution

     Retrieve a solution by its ID, including all linked agents, knowledge bases, and source connections.

    Returns the full solution detail with nested resource information.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SolutionResponse
    """

    return (
        await asyncio_detailed(
            solution_id=solution_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
