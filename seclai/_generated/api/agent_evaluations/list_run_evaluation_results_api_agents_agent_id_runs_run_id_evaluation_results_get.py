from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluation_result_with_criteria_response import (
    EvaluationResultWithCriteriaResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    run_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/runs/{run_id}/evaluation-results".format(
            agent_id=quote(str(agent_id), safe=""),
            run_id=quote(str(run_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[EvaluationResultWithCriteriaResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EvaluationResultWithCriteriaResponse.from_dict(
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
) -> Response[HTTPValidationError | list[EvaluationResultWithCriteriaResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | list[EvaluationResultWithCriteriaResponse]]:
    """List Run Evaluation Results

     List all evaluation results recorded for a specific agent run.

    Returns results across all evaluation criteria for the given run,
    useful for getting a complete quality snapshot of a single execution.

    Args:
        agent_id (str):
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[EvaluationResultWithCriteriaResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        run_id=run_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | list[EvaluationResultWithCriteriaResponse] | None:
    """List Run Evaluation Results

     List all evaluation results recorded for a specific agent run.

    Returns results across all evaluation criteria for the given run,
    useful for getting a complete quality snapshot of a single execution.

    Args:
        agent_id (str):
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[EvaluationResultWithCriteriaResponse]
    """

    return sync_detailed(
        agent_id=agent_id,
        run_id=run_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | list[EvaluationResultWithCriteriaResponse]]:
    """List Run Evaluation Results

     List all evaluation results recorded for a specific agent run.

    Returns results across all evaluation criteria for the given run,
    useful for getting a complete quality snapshot of a single execution.

    Args:
        agent_id (str):
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[EvaluationResultWithCriteriaResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        run_id=run_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | list[EvaluationResultWithCriteriaResponse] | None:
    """List Run Evaluation Results

     List all evaluation results recorded for a specific agent run.

    Returns results across all evaluation criteria for the given run,
    useful for getting a complete quality snapshot of a single execution.

    Args:
        agent_id (str):
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[EvaluationResultWithCriteriaResponse]
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            run_id=run_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
