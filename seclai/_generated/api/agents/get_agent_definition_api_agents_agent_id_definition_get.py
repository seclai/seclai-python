from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_definition_response import AgentDefinitionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/definition".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

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
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError]:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `transform`: Reshape data with a Liquid template
    - `gate`: Evaluate conditions, stop or continue child execution
    - `retry`: Re-execute from a target ancestor step (for quality-control loops; pair with a `gate`
    step for conditional retrying. Fields: `target_step_id` (ancestor step ID), `max_retries` (1–10))
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `insight`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `send_email`: Send email with step output
    - `webhook_call`: POST data to an external URL
    - `write_aws_s3_object`: Write output to S3
    - `call_agent`: Invoke another agent
    - `write_metadata`: Write a value to content metadata (for filtering/gates; content-triggered agents
    only. Fields: `metadata_key`, `content`)
    - `write_content_attachment`: Write a file-backed attachment to content (optionally indexed for
    retrieval; content-triggered agents only. Fields: `attachment_key`, `content`, `content_type`,
    `indexed`)
    - `load_content_attachment`: Load a previously written attachment (content-triggered agents only.
    Fields: `attachment_key`)
    - `load_content`: Load the full text body of a source document (typically used with content-
    triggered agents; can also load by explicit `content_version_id`. Fields: `content_version_id`
    optional)
    - `streaming_result`: Stream LLM tokens in real-time via SSE (must be a direct child of
    `prompt_call`; requires `dynamic_input` trigger; `priority: true` enables real-time streaming)
    - `display_result`: Show output to the user
    - `join`: Merge parallel branches
    - `combinator`: Combine multiple inputs
    - `text`: Static text literal

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
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
    x_account_id: UUID | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | None:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `transform`: Reshape data with a Liquid template
    - `gate`: Evaluate conditions, stop or continue child execution
    - `retry`: Re-execute from a target ancestor step (for quality-control loops; pair with a `gate`
    step for conditional retrying. Fields: `target_step_id` (ancestor step ID), `max_retries` (1–10))
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `insight`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `send_email`: Send email with step output
    - `webhook_call`: POST data to an external URL
    - `write_aws_s3_object`: Write output to S3
    - `call_agent`: Invoke another agent
    - `write_metadata`: Write a value to content metadata (for filtering/gates; content-triggered agents
    only. Fields: `metadata_key`, `content`)
    - `write_content_attachment`: Write a file-backed attachment to content (optionally indexed for
    retrieval; content-triggered agents only. Fields: `attachment_key`, `content`, `content_type`,
    `indexed`)
    - `load_content_attachment`: Load a previously written attachment (content-triggered agents only.
    Fields: `attachment_key`)
    - `load_content`: Load the full text body of a source document (typically used with content-
    triggered agents; can also load by explicit `content_version_id`. Fields: `content_version_id`
    optional)
    - `streaming_result`: Stream LLM tokens in real-time via SSE (must be a direct child of
    `prompt_call`; requires `dynamic_input` trigger; `priority: true` enables real-time streaming)
    - `display_result`: Show output to the user
    - `join`: Merge parallel branches
    - `combinator`: Combine multiple inputs
    - `text`: Static text literal

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError]:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `transform`: Reshape data with a Liquid template
    - `gate`: Evaluate conditions, stop or continue child execution
    - `retry`: Re-execute from a target ancestor step (for quality-control loops; pair with a `gate`
    step for conditional retrying. Fields: `target_step_id` (ancestor step ID), `max_retries` (1–10))
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `insight`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `send_email`: Send email with step output
    - `webhook_call`: POST data to an external URL
    - `write_aws_s3_object`: Write output to S3
    - `call_agent`: Invoke another agent
    - `write_metadata`: Write a value to content metadata (for filtering/gates; content-triggered agents
    only. Fields: `metadata_key`, `content`)
    - `write_content_attachment`: Write a file-backed attachment to content (optionally indexed for
    retrieval; content-triggered agents only. Fields: `attachment_key`, `content`, `content_type`,
    `indexed`)
    - `load_content_attachment`: Load a previously written attachment (content-triggered agents only.
    Fields: `attachment_key`)
    - `load_content`: Load the full text body of a source document (typically used with content-
    triggered agents; can also load by explicit `content_version_id`. Fields: `content_version_id`
    optional)
    - `streaming_result`: Stream LLM tokens in real-time via SSE (must be a direct child of
    `prompt_call`; requires `dynamic_input` trigger; `priority: true` enables real-time streaming)
    - `display_result`: Show output to the user
    - `join`: Merge parallel branches
    - `combinator`: Combine multiple inputs
    - `text`: Static text literal

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | None:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `transform`: Reshape data with a Liquid template
    - `gate`: Evaluate conditions, stop or continue child execution
    - `retry`: Re-execute from a target ancestor step (for quality-control loops; pair with a `gate`
    step for conditional retrying. Fields: `target_step_id` (ancestor step ID), `max_retries` (1–10))
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `insight`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `send_email`: Send email with step output
    - `webhook_call`: POST data to an external URL
    - `write_aws_s3_object`: Write output to S3
    - `call_agent`: Invoke another agent
    - `write_metadata`: Write a value to content metadata (for filtering/gates; content-triggered agents
    only. Fields: `metadata_key`, `content`)
    - `write_content_attachment`: Write a file-backed attachment to content (optionally indexed for
    retrieval; content-triggered agents only. Fields: `attachment_key`, `content`, `content_type`,
    `indexed`)
    - `load_content_attachment`: Load a previously written attachment (content-triggered agents only.
    Fields: `attachment_key`)
    - `load_content`: Load the full text body of a source document (typically used with content-
    triggered agents; can also load by explicit `content_version_id`. Fields: `content_version_id`
    optional)
    - `streaming_result`: Stream LLM tokens in real-time via SSE (must be a direct child of
    `prompt_call`; requires `dynamic_input` trigger; `priority: true` enables real-time streaming)
    - `display_result`: Show output to the user
    - `join`: Merge parallel branches
    - `combinator`: Combine multiple inputs
    - `text`: Static text literal

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):

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
            x_account_id=x_account_id,
        )
    ).parsed
