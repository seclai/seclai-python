from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.governance_conversation_response import GovernanceConversationResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/governance/ai-assistant/conversations",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[GovernanceConversationResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GovernanceConversationResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

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
) -> Response[Any | HTTPValidationError | list[GovernanceConversationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[GovernanceConversationResponse]]:
    """List AI assistant conversations

     Return recent governance AI assistant conversations for the account, ordered by most recent first.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        limit (int | Unset): Number of conversations. Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[GovernanceConversationResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> Any | HTTPValidationError | list[GovernanceConversationResponse] | None:
    """List AI assistant conversations

     Return recent governance AI assistant conversations for the account, ordered by most recent first.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        limit (int | Unset): Number of conversations. Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[GovernanceConversationResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[GovernanceConversationResponse]]:
    """List AI assistant conversations

     Return recent governance AI assistant conversations for the account, ordered by most recent first.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        limit (int | Unset): Number of conversations. Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[GovernanceConversationResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    x_account_id: str | Unset = UNSET,
) -> Any | HTTPValidationError | list[GovernanceConversationResponse] | None:
    """List AI assistant conversations

     Return recent governance AI assistant conversations for the account, ordered by most recent first.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        limit (int | Unset): Number of conversations. Default: 20.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[GovernanceConversationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            x_account_id=x_account_id,
        )
    ).parsed
