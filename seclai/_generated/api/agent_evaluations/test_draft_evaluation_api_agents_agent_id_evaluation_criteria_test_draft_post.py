from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.test_draft_evaluation_request import TestDraftEvaluationRequest
from ...models.test_draft_evaluation_response import TestDraftEvaluationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: TestDraftEvaluationRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/evaluation-criteria/test-draft".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TestDraftEvaluationResponse | None:
    if response.status_code == 200:
        response_200 = TestDraftEvaluationResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TestDraftEvaluationResponse]:
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
    body: TestDraftEvaluationRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | TestDraftEvaluationResponse]:
    """Test Draft Evaluation

     Run an ephemeral evaluation against provided step output without persisting results.

    Use this to interactively test evaluation prompts and expectation
    configurations while editing criteria.  No credits are consumed because
    the result is not recorded.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (TestDraftEvaluationRequest): Request body for ephemeral (non-persisted) evaluation
            testing.

            Provide either ``step_output`` (raw text) **or** ``agent_step_run_id``
            (to load output from storage).  Exactly one must be supplied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestDraftEvaluationResponse]
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
    body: TestDraftEvaluationRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | TestDraftEvaluationResponse | None:
    """Test Draft Evaluation

     Run an ephemeral evaluation against provided step output without persisting results.

    Use this to interactively test evaluation prompts and expectation
    configurations while editing criteria.  No credits are consumed because
    the result is not recorded.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (TestDraftEvaluationRequest): Request body for ephemeral (non-persisted) evaluation
            testing.

            Provide either ``step_output`` (raw text) **or** ``agent_step_run_id``
            (to load output from storage).  Exactly one must be supplied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestDraftEvaluationResponse
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
    body: TestDraftEvaluationRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | TestDraftEvaluationResponse]:
    """Test Draft Evaluation

     Run an ephemeral evaluation against provided step output without persisting results.

    Use this to interactively test evaluation prompts and expectation
    configurations while editing criteria.  No credits are consumed because
    the result is not recorded.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (TestDraftEvaluationRequest): Request body for ephemeral (non-persisted) evaluation
            testing.

            Provide either ``step_output`` (raw text) **or** ``agent_step_run_id``
            (to load output from storage).  Exactly one must be supplied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestDraftEvaluationResponse]
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
    body: TestDraftEvaluationRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | TestDraftEvaluationResponse | None:
    """Test Draft Evaluation

     Run an ephemeral evaluation against provided step output without persisting results.

    Use this to interactively test evaluation prompts and expectation
    configurations while editing criteria.  No credits are consumed because
    the result is not recorded.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (TestDraftEvaluationRequest): Request body for ephemeral (non-persisted) evaluation
            testing.

            Provide either ``step_output`` (raw text) **or** ``agent_step_run_id``
            (to load output from storage).  Exactly one must be supplied.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestDraftEvaluationResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
