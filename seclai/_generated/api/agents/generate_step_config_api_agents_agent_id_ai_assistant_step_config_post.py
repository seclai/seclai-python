from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_step_config_request import GenerateStepConfigRequest
from ...models.generate_step_config_response import GenerateStepConfigResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: GenerateStepConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/{agent_id}/ai-assistant/step-config".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenerateStepConfigResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GenerateStepConfigResponse.from_dict(response.json())

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
) -> Response[GenerateStepConfigResponse | HTTPValidationError]:
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
    body: GenerateStepConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[GenerateStepConfigResponse | HTTPValidationError]:
    """Generate step configuration

     Use the AI assistant to generate or refine a single step's configuration.

    Provide the step type, a natural language instruction, and optionally the current configuration. The
    AI will produce a proposed configuration along with an explanation. The suggestion is stored as a
    conversation turn that can be accepted or declined separately via the mark endpoint.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (GenerateStepConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateStepConfigResponse | HTTPValidationError]
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
    body: GenerateStepConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> GenerateStepConfigResponse | HTTPValidationError | None:
    """Generate step configuration

     Use the AI assistant to generate or refine a single step's configuration.

    Provide the step type, a natural language instruction, and optionally the current configuration. The
    AI will produce a proposed configuration along with an explanation. The suggestion is stored as a
    conversation turn that can be accepted or declined separately via the mark endpoint.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (GenerateStepConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateStepConfigResponse | HTTPValidationError
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
    body: GenerateStepConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[GenerateStepConfigResponse | HTTPValidationError]:
    """Generate step configuration

     Use the AI assistant to generate or refine a single step's configuration.

    Provide the step type, a natural language instruction, and optionally the current configuration. The
    AI will produce a proposed configuration along with an explanation. The suggestion is stored as a
    conversation turn that can be accepted or declined separately via the mark endpoint.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (GenerateStepConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateStepConfigResponse | HTTPValidationError]
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
    body: GenerateStepConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> GenerateStepConfigResponse | HTTPValidationError | None:
    """Generate step configuration

     Use the AI assistant to generate or refine a single step's configuration.

    Provide the step type, a natural language instruction, and optionally the current configuration. The
    AI will produce a proposed configuration along with an explanation. The suggestion is stored as a
    conversation turn that can be accepted or declined separately via the mark endpoint.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Only agents belonging to your account can be
    used.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        body (GenerateStepConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateStepConfigResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
