from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_assistant_generate_request import AiAssistantGenerateRequest
from ...models.ai_assistant_generate_response import AiAssistantGenerateResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    solution_id: UUID,
    *,
    body: AiAssistantGenerateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/solutions/{solution_id}/ai-assistant/source".format(
            solution_id=quote(str(solution_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AiAssistantGenerateResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AiAssistantGenerateResponse.from_dict(response.json())

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
) -> Response[AiAssistantGenerateResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AiAssistantGenerateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AiAssistantGenerateResponse | HTTPValidationError]:
    """Generate source plan

     Generate a content source plan via the source AI assistant.

    Describe what sources you need in natural language and the assistant will propose a plan with
    create, update, or delete actions. Review the proposed actions and use the accept or decline
    endpoint to execute or discard the plan.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AiAssistantGenerateRequest): Request body for AI assistant generate endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiAssistantGenerateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AiAssistantGenerateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AiAssistantGenerateResponse | HTTPValidationError | None:
    """Generate source plan

     Generate a content source plan via the source AI assistant.

    Describe what sources you need in natural language and the assistant will propose a plan with
    create, update, or delete actions. Review the proposed actions and use the accept or decline
    endpoint to execute or discard the plan.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AiAssistantGenerateRequest): Request body for AI assistant generate endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiAssistantGenerateResponse | HTTPValidationError
    """

    return sync_detailed(
        solution_id=solution_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AiAssistantGenerateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AiAssistantGenerateResponse | HTTPValidationError]:
    """Generate source plan

     Generate a content source plan via the source AI assistant.

    Describe what sources you need in natural language and the assistant will propose a plan with
    create, update, or delete actions. Review the proposed actions and use the accept or decline
    endpoint to execute or discard the plan.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AiAssistantGenerateRequest): Request body for AI assistant generate endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiAssistantGenerateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        solution_id=solution_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    solution_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AiAssistantGenerateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AiAssistantGenerateResponse | HTTPValidationError | None:
    """Generate source plan

     Generate a content source plan via the source AI assistant.

    Describe what sources you need in natural language and the assistant will propose a plan with
    create, update, or delete actions. Review the proposed actions and use the accept or decline
    endpoint to execute or discard the plan.

    Args:
        solution_id (UUID):
        x_account_id (UUID | Unset):
        body (AiAssistantGenerateRequest): Request body for AI assistant generate endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiAssistantGenerateResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            solution_id=solution_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
