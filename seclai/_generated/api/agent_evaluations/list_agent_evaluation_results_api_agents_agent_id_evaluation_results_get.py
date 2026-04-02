from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluation_result_with_criteria_list_response import (
    EvaluationResultWithCriteriaListResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    status: None | str | Unset = UNSET,
    step: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_step: None | str | Unset
    if isinstance(step, Unset):
        json_step = UNSET
    else:
        json_step = step
    params["step"] = json_step

    params["flagged_only"] = flagged_only

    json_time_from: None | str | Unset
    if isinstance(time_from, Unset):
        json_time_from = UNSET
    else:
        json_time_from = time_from
    params["time_from"] = json_time_from

    json_time_to: None | str | Unset
    if isinstance(time_to, Unset):
        json_time_to = UNSET
    else:
        json_time_to = time_to
    params["time_to"] = json_time_to

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/evaluation-results".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EvaluationResultWithCriteriaListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EvaluationResultWithCriteriaListResponse.from_dict(
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
) -> Response[EvaluationResultWithCriteriaListResponse | HTTPValidationError]:
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
    status: None | str | Unset = UNSET,
    step: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> Response[EvaluationResultWithCriteriaListResponse | HTTPValidationError]:
    """List Agent Evaluation Results

     List evaluation results across all criteria configured on an agent.

    Returns a paginated list of evaluation results with optional filtering by status, criteria, and date
    range. Results include score, pass/fail status, and details.

    Args:
        agent_id (str):
        status (None | str | Unset):
        step (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationResultWithCriteriaListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        status=status,
        step=step,
        flagged_only=flagged_only,
        time_from=time_from,
        time_to=time_to,
        page=page,
        limit=limit,
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
    status: None | str | Unset = UNSET,
    step: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> EvaluationResultWithCriteriaListResponse | HTTPValidationError | None:
    """List Agent Evaluation Results

     List evaluation results across all criteria configured on an agent.

    Returns a paginated list of evaluation results with optional filtering by status, criteria, and date
    range. Results include score, pass/fail status, and details.

    Args:
        agent_id (str):
        status (None | str | Unset):
        step (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationResultWithCriteriaListResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        status=status,
        step=step,
        flagged_only=flagged_only,
        time_from=time_from,
        time_to=time_to,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    step: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> Response[EvaluationResultWithCriteriaListResponse | HTTPValidationError]:
    """List Agent Evaluation Results

     List evaluation results across all criteria configured on an agent.

    Returns a paginated list of evaluation results with optional filtering by status, criteria, and date
    range. Results include score, pass/fail status, and details.

    Args:
        agent_id (str):
        status (None | str | Unset):
        step (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationResultWithCriteriaListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        status=status,
        step=step,
        flagged_only=flagged_only,
        time_from=time_from,
        time_to=time_to,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    step: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> EvaluationResultWithCriteriaListResponse | HTTPValidationError | None:
    """List Agent Evaluation Results

     List evaluation results across all criteria configured on an agent.

    Returns a paginated list of evaluation results with optional filtering by status, criteria, and date
    range. Results include score, pass/fail status, and details.

    Args:
        agent_id (str):
        status (None | str | Unset):
        step (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationResultWithCriteriaListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            status=status,
            step=step,
            flagged_only=flagged_only,
            time_from=time_from,
            time_to=time_to,
            page=page,
            limit=limit,
            x_account_id=x_account_id,
        )
    ).parsed
