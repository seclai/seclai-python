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
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `regex_replace`: Reshape text via ordered regex find/replace rules
    - `repeat_until`: Run a body (`body[]`) again until its `conditions` match the iteration's verdict
    or `max_iterations` (1–1000, default 3) is reached. Fields: `conditions`, `match`, optional
    `verdict_template`, `output` (`last` or `all`), `fail_when_max_reached`
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `extract_data`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `add_chat_turn` / `load_chat_history`: Record a turn or load running history from a conversation
    memory bank
    - `add_memory` / `search_memory` / `load_memory`: Write, semantic-search, or load entries on a
    general memory bank
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
    - `parallel`: Run its named `lanes` at the same time. The step after it reads their results as the
    block's output: a JSON object keyed by lane name, or its `output_template`, where `{{lane.<name>}}`
    is a lane's result
    - `text`: Produce output from a template, and select files with `attachments`
    - `for_each`: Iterate a body over a list of items (body lives in `body[]`)
    - `if_else`: Conditional dispatch. Evaluates `conditions` and runs `then_steps` on match, otherwise
    the optional `else_steps`. The chosen branch's output flows to the if_else step's own `child_steps`
    (post-branch continuation chain).
    - `switch`: Single-discriminator dispatch. Renders `discriminator` (default `{{input}}`) and routes
    to the first matching `cases[]` entry (equality by default; pass a list in `match` for `$in`
    semantics) or to `else_steps` when nothing matches. The chosen case's output flows to the switch
    step's own `child_steps`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step; steps
    that run at the same time are a `parallel` block's lanes. A scope's result (a branch arm's, a loop
    iteration's, a lane's) is its last step's output; an empty arm's is the branch's input, and an empty
    lane's the block's input.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `regex_replace`: Reshape text via ordered regex find/replace rules
    - `repeat_until`: Run a body (`body[]`) again until its `conditions` match the iteration's verdict
    or `max_iterations` (1–1000, default 3) is reached. Fields: `conditions`, `match`, optional
    `verdict_template`, `output` (`last` or `all`), `fail_when_max_reached`
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `extract_data`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `add_chat_turn` / `load_chat_history`: Record a turn or load running history from a conversation
    memory bank
    - `add_memory` / `search_memory` / `load_memory`: Write, semantic-search, or load entries on a
    general memory bank
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
    - `parallel`: Run its named `lanes` at the same time. The step after it reads their results as the
    block's output: a JSON object keyed by lane name, or its `output_template`, where `{{lane.<name>}}`
    is a lane's result
    - `text`: Produce output from a template, and select files with `attachments`
    - `for_each`: Iterate a body over a list of items (body lives in `body[]`)
    - `if_else`: Conditional dispatch. Evaluates `conditions` and runs `then_steps` on match, otherwise
    the optional `else_steps`. The chosen branch's output flows to the if_else step's own `child_steps`
    (post-branch continuation chain).
    - `switch`: Single-discriminator dispatch. Renders `discriminator` (default `{{input}}`) and routes
    to the first matching `cases[]` entry (equality by default; pass a list in `match` for `$in`
    semantics) or to `else_steps` when nothing matches. The chosen case's output flows to the switch
    step's own `child_steps`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step; steps
    that run at the same time are a `parallel` block's lanes. A scope's result (a branch arm's, a loop
    iteration's, a lane's) is its last step's output; an empty arm's is the branch's input, and an empty
    lane's the block's input.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `regex_replace`: Reshape text via ordered regex find/replace rules
    - `repeat_until`: Run a body (`body[]`) again until its `conditions` match the iteration's verdict
    or `max_iterations` (1–1000, default 3) is reached. Fields: `conditions`, `match`, optional
    `verdict_template`, `output` (`last` or `all`), `fail_when_max_reached`
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `extract_data`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `add_chat_turn` / `load_chat_history`: Record a turn or load running history from a conversation
    memory bank
    - `add_memory` / `search_memory` / `load_memory`: Write, semantic-search, or load entries on a
    general memory bank
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
    - `parallel`: Run its named `lanes` at the same time. The step after it reads their results as the
    block's output: a JSON object keyed by lane name, or its `output_template`, where `{{lane.<name>}}`
    is a lane's result
    - `text`: Produce output from a template, and select files with `attachments`
    - `for_each`: Iterate a body over a list of items (body lives in `body[]`)
    - `if_else`: Conditional dispatch. Evaluates `conditions` and runs `then_steps` on match, otherwise
    the optional `else_steps`. The chosen branch's output flows to the if_else step's own `child_steps`
    (post-branch continuation chain).
    - `switch`: Single-discriminator dispatch. Renders `discriminator` (default `{{input}}`) and routes
    to the first matching `cases[]` entry (equality by default; pass a list in `match` for `$in`
    semantics) or to `else_steps` when nothing matches. The chosen case's output flows to the switch
    step's own `child_steps`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step; steps
    that run at the same time are a `parallel` block's lanes. A scope's result (a branch arm's, a loop
    iteration's, a lane's) is its last step's output; an empty arm's is the branch's input, and an empty
    lane's the block's input.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentDefinitionResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Get agent definition

     Fetch the current agent definition from the main branch.

    The response includes `change_id` which must be provided when updating the definition (optimistic
    locking).

    The definition contains the agent's step workflow. Available step types:
    - `prompt_call`: Call an LLM with a prompt template
    - `retrieval`: Search a knowledge base
    - `regex_replace`: Reshape text via ordered regex find/replace rules
    - `repeat_until`: Run a body (`body[]`) again until its `conditions` match the iteration's verdict
    or `max_iterations` (1–1000, default 3) is reached. Fields: `conditions`, `match`, optional
    `verdict_template`, `output` (`last` or `all`), `fail_when_max_reached`
    - `evaluate_step`: Score a selected previous step output and emit JSON with `score`, `passed`, and
    `pass_threshold` (fields: `target_step_id`, `evaluation_prompt`, `pass_threshold`, optional
    `evaluation_tier`, optional `expectation_config`)
    - `extract_data`: Progressively read and analyze large input
    - `extract_content`: Extract structured data (JSON, HTML, XML)
    - `add_chat_turn` / `load_chat_history`: Record a turn or load running history from a conversation
    memory bank
    - `add_memory` / `search_memory` / `load_memory`: Write, semantic-search, or load entries on a
    general memory bank
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
    - `parallel`: Run its named `lanes` at the same time. The step after it reads their results as the
    block's output: a JSON object keyed by lane name, or its `output_template`, where `{{lane.<name>}}`
    is a lane's result
    - `text`: Produce output from a template, and select files with `attachments`
    - `for_each`: Iterate a body over a list of items (body lives in `body[]`)
    - `if_else`: Conditional dispatch. Evaluates `conditions` and runs `then_steps` on match, otherwise
    the optional `else_steps`. The chosen branch's output flows to the if_else step's own `child_steps`
    (post-branch continuation chain).
    - `switch`: Single-discriminator dispatch. Renders `discriminator` (default `{{input}}`) and routes
    to the first matching `cases[]` entry (equality by default; pass a list in `match` for `$in`
    semantics) or to `else_steps` when nothing matches. The chosen case's output flows to the switch
    step's own `child_steps`.

    Each list of steps (`child_steps`, a branch arm, a loop body, a lane) holds at most one step; steps
    that run at the same time are a `parallel` block's lanes. A scope's result (a branch arm's, a loop
    iteration's, a lane's) is its last step's output; an empty arm's is the branch's input, and an empty
    lane's the block's input.

    `run_result` marks a step's output as the run's answer. Only a `prompt_call`, `text`, `call_agent`,
    `generate_image`, `generate_audio` or `generate_video` step may carry it; a run reaches at most one,
    and no loop body holds one. Plain text: a `text` or `prompt_call` step carrying it. JSON: a `text`
    step whose template is a single placeholder naming a JSON step, or that sets `content_type`
    `application/json`. HTML: a `text` step whose `content_type` is `text/html`. Files or generated
    media: the flag's `attachments`, a `text` step's `attachments`, or a generate step carrying it. A
    streamed answer: a `prompt_call` carrying it with `stream` on. No answer: no step carries it, and
    the agent reports success at start or at completion.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access agents belonging to your
    account.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

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
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
