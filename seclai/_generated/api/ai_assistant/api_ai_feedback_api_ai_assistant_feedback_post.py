from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_assistant_feedback_request import AiAssistantFeedbackRequest
from ...models.ai_assistant_feedback_response import AiAssistantFeedbackResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AiAssistantFeedbackRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ai-assistant/feedback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AiAssistantFeedbackResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AiAssistantFeedbackResponse.from_dict(response.json())

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
) -> Response[AiAssistantFeedbackResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AiAssistantFeedbackRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AiAssistantFeedbackResponse | HTTPValidationError]:
    """Submit AI assistant feedback

     Submit thumbs-up/down feedback on any AI assistant interaction. Negative feedback with a comment is
    analyzed for concerning issues.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (AiAssistantFeedbackRequest): Request body for submitting AI assistant feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiAssistantFeedbackResponse | HTTPValidationError]
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
    body: AiAssistantFeedbackRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AiAssistantFeedbackResponse | HTTPValidationError | None:
    """Submit AI assistant feedback

     Submit thumbs-up/down feedback on any AI assistant interaction. Negative feedback with a comment is
    analyzed for concerning issues.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (AiAssistantFeedbackRequest): Request body for submitting AI assistant feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiAssistantFeedbackResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AiAssistantFeedbackRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AiAssistantFeedbackResponse | HTTPValidationError]:
    """Submit AI assistant feedback

     Submit thumbs-up/down feedback on any AI assistant interaction. Negative feedback with a comment is
    analyzed for concerning issues.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (AiAssistantFeedbackRequest): Request body for submitting AI assistant feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiAssistantFeedbackResponse | HTTPValidationError]
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
    body: AiAssistantFeedbackRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AiAssistantFeedbackResponse | HTTPValidationError | None:
    """Submit AI assistant feedback

     Submit thumbs-up/down feedback on any AI assistant interaction. Negative feedback with a comment is
    analyzed for concerning issues.

    Auth: requires ``X-API-Key`` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (AiAssistantFeedbackRequest): Request body for submitting AI assistant feedback.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiAssistantFeedbackResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
