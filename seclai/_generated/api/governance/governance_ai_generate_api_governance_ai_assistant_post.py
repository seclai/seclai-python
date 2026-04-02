from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.governance_ai_assistant_request import GovernanceAiAssistantRequest
from ...models.governance_ai_assistant_response import GovernanceAiAssistantResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GovernanceAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/governance/ai-assistant",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GovernanceAiAssistantResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GovernanceAiAssistantResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GovernanceAiAssistantResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GovernanceAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | GovernanceAiAssistantResponse | HTTPValidationError]:
    """Generate a governance plan

     Send a natural-language request to the governance AI assistant to generate a plan of policy changes.
    Returns a conversation with proposed actions that can be accepted or declined.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        x_account_id (str | Unset):
        body (GovernanceAiAssistantRequest): Request body for the governance AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GovernanceAiAssistantResponse | HTTPValidationError]
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
    body: GovernanceAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> Any | GovernanceAiAssistantResponse | HTTPValidationError | None:
    """Generate a governance plan

     Send a natural-language request to the governance AI assistant to generate a plan of policy changes.
    Returns a conversation with proposed actions that can be accepted or declined.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        x_account_id (str | Unset):
        body (GovernanceAiAssistantRequest): Request body for the governance AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GovernanceAiAssistantResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GovernanceAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | GovernanceAiAssistantResponse | HTTPValidationError]:
    """Generate a governance plan

     Send a natural-language request to the governance AI assistant to generate a plan of policy changes.
    Returns a conversation with proposed actions that can be accepted or declined.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        x_account_id (str | Unset):
        body (GovernanceAiAssistantRequest): Request body for the governance AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GovernanceAiAssistantResponse | HTTPValidationError]
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
    body: GovernanceAiAssistantRequest,
    x_account_id: str | Unset = UNSET,
) -> Any | GovernanceAiAssistantResponse | HTTPValidationError | None:
    """Generate a governance plan

     Send a natural-language request to the governance AI assistant to generate a plan of policy changes.
    Returns a conversation with proposed actions that can be accepted or declined.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        x_account_id (str | Unset):
        body (GovernanceAiAssistantRequest): Request body for the governance AI assistant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GovernanceAiAssistantResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
