from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_evaluation_criteria_request import CreateEvaluationCriteriaRequest
from ...models.evaluation_criteria_response import EvaluationCriteriaResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: CreateEvaluationCriteriaRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/evaluation-criteria".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EvaluationCriteriaResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = EvaluationCriteriaResponse.from_dict(response.json())

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
) -> Response[EvaluationCriteriaResponse | HTTPValidationError]:
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
    body: CreateEvaluationCriteriaRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[EvaluationCriteriaResponse | HTTPValidationError]:
    """Create Evaluation Criteria

     Create new step evaluation settings for an agent.

    The evaluation mode, retry settings, and sample frequency are inherited
    from the agent and stored on the criteria row for historical reference.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationCriteriaRequest): Request body for creating an evaluation criteria.

            The evaluation mode, retry settings, and sample frequency are set at the
            agent level, not per-criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationCriteriaResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
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
    body: CreateEvaluationCriteriaRequest,
    x_account_id: str | Unset = UNSET,
) -> EvaluationCriteriaResponse | HTTPValidationError | None:
    """Create Evaluation Criteria

     Create new step evaluation settings for an agent.

    The evaluation mode, retry settings, and sample frequency are inherited
    from the agent and stored on the criteria row for historical reference.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationCriteriaRequest): Request body for creating an evaluation criteria.

            The evaluation mode, retry settings, and sample frequency are set at the
            agent level, not per-criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationCriteriaResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEvaluationCriteriaRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[EvaluationCriteriaResponse | HTTPValidationError]:
    """Create Evaluation Criteria

     Create new step evaluation settings for an agent.

    The evaluation mode, retry settings, and sample frequency are inherited
    from the agent and stored on the criteria row for historical reference.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationCriteriaRequest): Request body for creating an evaluation criteria.

            The evaluation mode, retry settings, and sample frequency are set at the
            agent level, not per-criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationCriteriaResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEvaluationCriteriaRequest,
    x_account_id: str | Unset = UNSET,
) -> EvaluationCriteriaResponse | HTTPValidationError | None:
    """Create Evaluation Criteria

     Create new step evaluation settings for an agent.

    The evaluation mode, retry settings, and sample frequency are inherited
    from the agent and stored on the criteria row for historical reference.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (CreateEvaluationCriteriaRequest): Request body for creating an evaluation criteria.

            The evaluation mode, retry settings, and sample frequency are set at the
            agent level, not per-criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationCriteriaResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
