from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_agent_steps_request import GenerateAgentStepsRequest
from ...models.generate_agent_steps_response import GenerateAgentStepsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: GenerateAgentStepsRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/ai-assistant/generate-steps".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenerateAgentStepsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GenerateAgentStepsResponse.from_dict(response.json())

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
) -> Response[GenerateAgentStepsResponse | HTTPValidationError]:
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
    body: GenerateAgentStepsRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[GenerateAgentStepsResponse | HTTPValidationError]:
    """Generate agent workflow

     Use the AI assistant to generate a full agent step workflow from a natural language description.

    Provide a description of what the agent should do, along with optional context (current steps,
    trigger type). The AI produces a complete set of agent steps.
    Use mode 'generate_full' for new workflows or 'modify_workflow' to refine existing ones.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (GenerateAgentStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateAgentStepsResponse | HTTPValidationError]
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
    body: GenerateAgentStepsRequest,
    x_account_id: str | Unset = UNSET,
) -> GenerateAgentStepsResponse | HTTPValidationError | None:
    """Generate agent workflow

     Use the AI assistant to generate a full agent step workflow from a natural language description.

    Provide a description of what the agent should do, along with optional context (current steps,
    trigger type). The AI produces a complete set of agent steps.
    Use mode 'generate_full' for new workflows or 'modify_workflow' to refine existing ones.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (GenerateAgentStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateAgentStepsResponse | HTTPValidationError
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
    body: GenerateAgentStepsRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[GenerateAgentStepsResponse | HTTPValidationError]:
    """Generate agent workflow

     Use the AI assistant to generate a full agent step workflow from a natural language description.

    Provide a description of what the agent should do, along with optional context (current steps,
    trigger type). The AI produces a complete set of agent steps.
    Use mode 'generate_full' for new workflows or 'modify_workflow' to refine existing ones.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (GenerateAgentStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateAgentStepsResponse | HTTPValidationError]
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
    body: GenerateAgentStepsRequest,
    x_account_id: str | Unset = UNSET,
) -> GenerateAgentStepsResponse | HTTPValidationError | None:
    """Generate agent workflow

     Use the AI assistant to generate a full agent step workflow from a natural language description.

    Provide a description of what the agent should do, along with optional context (current steps,
    trigger type). The AI produces a complete set of agent steps.
    Use mode 'generate_full' for new workflows or 'modify_workflow' to refine existing ones.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (str | Unset):
        body (GenerateAgentStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateAgentStepsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
