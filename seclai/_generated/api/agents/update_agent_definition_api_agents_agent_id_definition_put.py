from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_definition_response import AgentDefinitionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.update_agent_definition_request import UpdateAgentDefinitionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/agents/{agent_id}/definition".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentDefinitionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentDefinitionResponse.from_dict(response.json())

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
) -> Response[AgentDefinitionResponse | HTTPValidationError]:
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
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError]:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /api/agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `transform`, `gate`, `retry`, `evaluate_step`, `insight`, `extract_content`, `streaming_result`,
    `send_email`, `webhook_call`, `write_aws_s3_object`, `call_agent`, `write_metadata`,
    `write_content_attachment`, `load_content_attachment`, `load_content`, `display_result`, `join`,
    `combinator`, and `text`. Non-composite step types (`display_result`, `join`, `retry`,
    `evaluate_step`, `streaming_result`) cannot contain child steps.

    **Retry steps** re-execute from a target ancestor step for quality-control loops. Configure with
    `target_step_id` (ancestor step ID) and `max_retries` (1–10). Best practice: place a `gate` step
    before the retry to make retries conditional.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError]
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
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | None:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /api/agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `transform`, `gate`, `retry`, `evaluate_step`, `insight`, `extract_content`, `streaming_result`,
    `send_email`, `webhook_call`, `write_aws_s3_object`, `call_agent`, `write_metadata`,
    `write_content_attachment`, `load_content_attachment`, `load_content`, `display_result`, `join`,
    `combinator`, and `text`. Non-composite step types (`display_result`, `join`, `retry`,
    `evaluate_step`, `streaming_result`) cannot contain child steps.

    **Retry steps** re-execute from a target ancestor step for quality-control loops. Configure with
    `target_step_id` (ancestor step ID) and `max_retries` (1–10). Best practice: place a `gate` step
    before the retry to make retries conditional.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionResponse | HTTPValidationError
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
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError]:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /api/agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `transform`, `gate`, `retry`, `evaluate_step`, `insight`, `extract_content`, `streaming_result`,
    `send_email`, `webhook_call`, `write_aws_s3_object`, `call_agent`, `write_metadata`,
    `write_content_attachment`, `load_content_attachment`, `load_content`, `display_result`, `join`,
    `combinator`, and `text`. Non-composite step types (`display_result`, `join`, `retry`,
    `evaluate_step`, `streaming_result`) cannot contain child steps.

    **Retry steps** re-execute from a target ancestor step for quality-control loops. Configure with
    `target_step_id` (ancestor step ID) and `max_retries` (1–10). Best practice: place a `gate` step
    before the retry to make retries conditional.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError]
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
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | None:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /api/agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `transform`, `gate`, `retry`, `evaluate_step`, `insight`, `extract_content`, `streaming_result`,
    `send_email`, `webhook_call`, `write_aws_s3_object`, `call_agent`, `write_metadata`,
    `write_content_attachment`, `load_content_attachment`, `load_content`, `display_result`, `join`,
    `combinator`, and `text`. Non-composite step types (`display_result`, `join`, `retry`,
    `evaluate_step`, `streaming_result`) cannot contain child steps.

    **Retry steps** re-execute from a target ancestor step for quality-control loops. Configure with
    `target_step_id` (ancestor step ID) and `max_retries` (1–10). Best practice: place a `gate` step
    before the retry to make retries conditional.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
