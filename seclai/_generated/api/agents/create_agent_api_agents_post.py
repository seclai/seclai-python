from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_summary_response import AgentSummaryResponse
from ...models.create_agent_request import CreateAgentRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentSummaryResponse | Any | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = AgentSummaryResponse.from_dict(response.json())

        return response_201

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentSummaryResponse | Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentSummaryResponse | Any | HTTPValidationError]:
    """Create an agent

     Create a new agent.

    Trigger types:
    - `dynamic_input`: triggered via API with user-provided input
    - `template_input`: triggered via API with a predefined template
    - `schedule`: triggered on a schedule
    - `new_content`: triggered when new content arrives

    Templates: `blank`, `retrieval_example`, `simple_qa`, `summarizer`, `json_extractor`,
    `content_change_notifier`, `scheduled_report`, `webhook_pipeline`

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Agent is created in the caller's account.

    Args:
        x_account_id (UUID | Unset):
        body (CreateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSummaryResponse | Any | HTTPValidationError]
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
    body: CreateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentSummaryResponse | Any | HTTPValidationError | None:
    """Create an agent

     Create a new agent.

    Trigger types:
    - `dynamic_input`: triggered via API with user-provided input
    - `template_input`: triggered via API with a predefined template
    - `schedule`: triggered on a schedule
    - `new_content`: triggered when new content arrives

    Templates: `blank`, `retrieval_example`, `simple_qa`, `summarizer`, `json_extractor`,
    `content_change_notifier`, `scheduled_report`, `webhook_pipeline`

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Agent is created in the caller's account.

    Args:
        x_account_id (UUID | Unset):
        body (CreateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSummaryResponse | Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentSummaryResponse | Any | HTTPValidationError]:
    """Create an agent

     Create a new agent.

    Trigger types:
    - `dynamic_input`: triggered via API with user-provided input
    - `template_input`: triggered via API with a predefined template
    - `schedule`: triggered on a schedule
    - `new_content`: triggered when new content arrives

    Templates: `blank`, `retrieval_example`, `simple_qa`, `summarizer`, `json_extractor`,
    `content_change_notifier`, `scheduled_report`, `webhook_pipeline`

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Agent is created in the caller's account.

    Args:
        x_account_id (UUID | Unset):
        body (CreateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentSummaryResponse | Any | HTTPValidationError]
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
    body: CreateAgentRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentSummaryResponse | Any | HTTPValidationError | None:
    """Create an agent

     Create a new agent.

    Trigger types:
    - `dynamic_input`: triggered via API with user-provided input
    - `template_input`: triggered via API with a predefined template
    - `schedule`: triggered on a schedule
    - `new_content`: triggered when new content arrives

    Templates: `blank`, `retrieval_example`, `simple_qa`, `summarizer`, `json_extractor`,
    `content_change_notifier`, `scheduled_report`, `webhook_pipeline`

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Agent is created in the caller's account.

    Args:
        x_account_id (UUID | Unset):
        body (CreateAgentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentSummaryResponse | Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
