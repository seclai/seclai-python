from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_definition_response import AgentDefinitionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.update_agent_definition_request import UpdateAgentDefinitionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

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
) -> AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = AgentDefinitionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = ServiceUnavailableError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]:
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
    seclai_version: str | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `regex_replace`, `evaluate_step`, `extract_data`, `extract_content`, `add_chat_turn`,
    `load_chat_history`, `add_memory`, `search_memory`, `load_memory`, `send_email`, `webhook_call`,
    `write_aws_s3_object`, `call_agent`, `write_metadata`, `write_content_attachment`,
    `load_content_attachment`, `load_content`, `text`, `for_each`, `repeat_until`, `if_else`, `switch`
    and `parallel`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step. A list
    of more than one step is stored as a `parallel` block with one lane per step, which no later step
    reads.

    **parallel** starts every lane in `lanes` with the block's input, and the step after it starts once
    every lane has finished. Its output is a JSON object keyed by lane name, or its `output_template`,
    where `{{lane.<name>}}` is a lane's result.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    **repeat_until** runs its `body[]`, then tests its `conditions` against the iteration's verdict
    (`verdict_template`, else the iteration's value); it repeats until they match or `max_iterations` is
    reached.

    **if_else** runs `then_steps` when its `conditions` match, otherwise its optional `else_steps`.
    Either branch's output flows to the if_else step's own `child_steps` (the post-branch continuation
    chain).

    **switch** dispatches on a `discriminator` template (default `{{input}}`) to the first matching case
    (equality by default; pass a list in `match` for `$in` semantics) or to `else_steps` when no case
    matches. Cases own their own `steps` subtrees; the chosen branch's output flows to the switch step's
    own `child_steps`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
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
    seclai_version: str | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `regex_replace`, `evaluate_step`, `extract_data`, `extract_content`, `add_chat_turn`,
    `load_chat_history`, `add_memory`, `search_memory`, `load_memory`, `send_email`, `webhook_call`,
    `write_aws_s3_object`, `call_agent`, `write_metadata`, `write_content_attachment`,
    `load_content_attachment`, `load_content`, `text`, `for_each`, `repeat_until`, `if_else`, `switch`
    and `parallel`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step. A list
    of more than one step is stored as a `parallel` block with one lane per step, which no later step
    reads.

    **parallel** starts every lane in `lanes` with the block's input, and the step after it starts once
    every lane has finished. Its output is a JSON object keyed by lane name, or its `output_template`,
    where `{{lane.<name>}}` is a lane's result.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    **repeat_until** runs its `body[]`, then tests its `conditions` against the iteration's verdict
    (`verdict_template`, else the iteration's value); it repeats until they match or `max_iterations` is
    reached.

    **if_else** runs `then_steps` when its `conditions` match, otherwise its optional `else_steps`.
    Either branch's output flows to the if_else step's own `child_steps` (the post-branch continuation
    chain).

    **switch** dispatches on a `discriminator` template (default `{{input}}`) to the first matching case
    (equality by default; pass a list in `match` for `$in` semantics) or to `else_steps` when no case
    matches. Cases own their own `steps` subtrees; the chosen branch's output flows to the switch step's
    own `child_steps`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `regex_replace`, `evaluate_step`, `extract_data`, `extract_content`, `add_chat_turn`,
    `load_chat_history`, `add_memory`, `search_memory`, `load_memory`, `send_email`, `webhook_call`,
    `write_aws_s3_object`, `call_agent`, `write_metadata`, `write_content_attachment`,
    `load_content_attachment`, `load_content`, `text`, `for_each`, `repeat_until`, `if_else`, `switch`
    and `parallel`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step. A list
    of more than one step is stored as a `parallel` block with one lane per step, which no later step
    reads.

    **parallel** starts every lane in `lanes` with the block's input, and the step after it starts once
    every lane has finished. Its output is a JSON object keyed by lane name, or its `output_template`,
    where `{{lane.<name>}}` is a lane's result.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    **repeat_until** runs its `body[]`, then tests its `conditions` against the iteration's verdict
    (`verdict_template`, else the iteration's value); it repeats until they match or `max_iterations` is
    reached.

    **if_else** runs `then_steps` when its `conditions` match, otherwise its optional `else_steps`.
    Either branch's output flows to the if_else step's own `child_steps` (the post-branch continuation
    chain).

    **switch** dispatches on a `discriminator` template (default `{{input}}`) to the first matching case
    (equality by default; pass a list in `match` for `$in` semantics) or to `else_steps` when no case
    matches. Cases own their own `steps` subtrees; the chosen branch's output flows to the switch step's
    own `child_steps`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAgentDefinitionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Update agent definition

     Update the agent's definition on the main branch.

    Uses **optimistic locking**: provide `expected_change_id` from the last `GET
    /agents/{agent_id}/definition`. Returns `409 Conflict` if the definition was modified since your
    last read.

    The definition contains the agent's step workflow. Step types include `prompt_call`, `retrieval`,
    `regex_replace`, `evaluate_step`, `extract_data`, `extract_content`, `add_chat_turn`,
    `load_chat_history`, `add_memory`, `search_memory`, `load_memory`, `send_email`, `webhook_call`,
    `write_aws_s3_object`, `call_agent`, `write_metadata`, `write_content_attachment`,
    `load_content_attachment`, `load_content`, `text`, `for_each`, `repeat_until`, `if_else`, `switch`
    and `parallel`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step. A list
    of more than one step is stored as a `parallel` block with one lane per step, which no later step
    reads.

    **parallel** starts every lane in `lanes` with the block's input, and the step after it starts once
    every lane has finished. Its output is a JSON object keyed by lane name, or its `output_template`,
    where `{{lane.<name>}}` is a lane's result.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    **repeat_until** runs its `body[]`, then tests its `conditions` against the iteration's verdict
    (`verdict_template`, else the iteration's value); it repeats until they match or `max_iterations` is
    reached.

    **if_else** runs `then_steps` when its `conditions` match, otherwise its optional `else_steps`.
    Either branch's output flows to the if_else step's own `child_steps` (the post-branch continuation
    chain).

    **switch** dispatches on a `discriminator` template (default `{{input}}`) to the first matching case
    (equality by default; pass a list in `match` for `$in` semantics) or to `else_steps` when no case
    matches. Cases own their own `steps` subtrees; the chosen branch's output flows to the switch step's
    own `child_steps`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only update agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateAgentDefinitionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
