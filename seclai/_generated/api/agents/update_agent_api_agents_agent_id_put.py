from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_summary_response import AgentSummaryResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.update_agent_request import UpdateAgentRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: UpdateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/agents/{agent_id}".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentSummaryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentSummaryResponse.from_dict(response.json())

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
) -> Response[AgentSummaryResponse | HTTPValidationError]:
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
    body: UpdateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentSummaryResponse | HTTPValidationError]:
    """Update agent metadata

     Update an agent's name, description, evaluation settings, and model lifecycle settings.

    Evaluation settings: `evaluation_mode` ('output_expectation', 'eval_and_retry', 'sample_and_flag'),
    `default_evaluation_tier` ('fast', 'balanced', 'thorough'), `max_retries`, `retry_on_failure`,
    `sampling_config`.

    Model lifecycle settings: `prompt_model_auto_upgrade_strategy` ('none', 'early_adopter',
    'middle_of_road', 'cautious_adopter'), `prompt_model_auto_rollback_enabled`,
    `prompt_model_auto_rollback_triggers` (list of 'agent_eval_fail', 'governance_flag',
    'governance_block', 'agent_run_failed').

    At least one field must be provided.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSummaryResponse | HTTPValidationError]
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
    body: UpdateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentSummaryResponse | HTTPValidationError | None:
    """Update agent metadata

     Update an agent's name, description, evaluation settings, and model lifecycle settings.

    Evaluation settings: `evaluation_mode` ('output_expectation', 'eval_and_retry', 'sample_and_flag'),
    `default_evaluation_tier` ('fast', 'balanced', 'thorough'), `max_retries`, `retry_on_failure`,
    `sampling_config`.

    Model lifecycle settings: `prompt_model_auto_upgrade_strategy` ('none', 'early_adopter',
    'middle_of_road', 'cautious_adopter'), `prompt_model_auto_rollback_enabled`,
    `prompt_model_auto_rollback_triggers` (list of 'agent_eval_fail', 'governance_flag',
    'governance_block', 'agent_run_failed').

    At least one field must be provided.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSummaryResponse | HTTPValidationError
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
    body: UpdateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentSummaryResponse | HTTPValidationError]:
    """Update agent metadata

     Update an agent's name, description, evaluation settings, and model lifecycle settings.

    Evaluation settings: `evaluation_mode` ('output_expectation', 'eval_and_retry', 'sample_and_flag'),
    `default_evaluation_tier` ('fast', 'balanced', 'thorough'), `max_retries`, `retry_on_failure`,
    `sampling_config`.

    Model lifecycle settings: `prompt_model_auto_upgrade_strategy` ('none', 'early_adopter',
    'middle_of_road', 'cautious_adopter'), `prompt_model_auto_rollback_enabled`,
    `prompt_model_auto_rollback_triggers` (list of 'agent_eval_fail', 'governance_flag',
    'governance_block', 'agent_run_failed').

    At least one field must be provided.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSummaryResponse | HTTPValidationError]
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
    body: UpdateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentSummaryResponse | HTTPValidationError | None:
    """Update agent metadata

     Update an agent's name, description, evaluation settings, and model lifecycle settings.

    Evaluation settings: `evaluation_mode` ('output_expectation', 'eval_and_retry', 'sample_and_flag'),
    `default_evaluation_tier` ('fast', 'balanced', 'thorough'), `max_retries`, `retry_on_failure`,
    `sampling_config`.

    Model lifecycle settings: `prompt_model_auto_upgrade_strategy` ('none', 'early_adopter',
    'middle_of_road', 'cautious_adopter'), `prompt_model_auto_rollback_enabled`,
    `prompt_model_auto_rollback_triggers` (list of 'agent_eval_fail', 'governance_flag',
    'governance_block', 'agent_run_failed').

    At least one field must be provided.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSummaryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
