from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_evaluation_result_request import CreateEvaluationResultRequest
from ...models.evaluation_result_response import EvaluationResultResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    criteria_id: str,
    *,
    body: CreateEvaluationResultRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/evaluation-criteria/{criteria_id}/results".format(
            criteria_id=quote(str(criteria_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EvaluationResultResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = EvaluationResultResponse.from_dict(response.json())

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
) -> Response[EvaluationResultResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEvaluationResultRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[EvaluationResultResponse | HTTPValidationError]:
    """Create Evaluation Result

     Record an evaluation result for a criteria.

    Use this endpoint to push results from external test harnesses, CI/CD
    pipelines, or custom evaluation logic.  Each result is linked to an
    agent run and optionally a specific step run.

    Args:
        criteria_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationResultRequest): Request body for recording an evaluation result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationResultResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        criteria_id=criteria_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEvaluationResultRequest,
    x_account_id: str | Unset = UNSET,
) -> EvaluationResultResponse | HTTPValidationError | None:
    """Create Evaluation Result

     Record an evaluation result for a criteria.

    Use this endpoint to push results from external test harnesses, CI/CD
    pipelines, or custom evaluation logic.  Each result is linked to an
    agent run and optionally a specific step run.

    Args:
        criteria_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationResultRequest): Request body for recording an evaluation result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationResultResponse | HTTPValidationError
    """

    return sync_detailed(
        criteria_id=criteria_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEvaluationResultRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[EvaluationResultResponse | HTTPValidationError]:
    """Create Evaluation Result

     Record an evaluation result for a criteria.

    Use this endpoint to push results from external test harnesses, CI/CD
    pipelines, or custom evaluation logic.  Each result is linked to an
    agent run and optionally a specific step run.

    Args:
        criteria_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationResultRequest): Request body for recording an evaluation result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationResultResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        criteria_id=criteria_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEvaluationResultRequest,
    x_account_id: str | Unset = UNSET,
) -> EvaluationResultResponse | HTTPValidationError | None:
    """Create Evaluation Result

     Record an evaluation result for a criteria.

    Use this endpoint to push results from external test harnesses, CI/CD
    pipelines, or custom evaluation logic.  Each result is linked to an
    agent run and optionally a specific step run.

    Args:
        criteria_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationResultRequest): Request body for recording an evaluation result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationResultResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            criteria_id=criteria_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
