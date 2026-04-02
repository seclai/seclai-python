from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.governance_ai_accept_response import GovernanceAiAcceptResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: UUID,
    *,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/governance/ai-assistant/{conversation_id}/accept".format(
            conversation_id=quote(str(conversation_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GovernanceAiAcceptResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GovernanceAiAcceptResponse.from_dict(response.json())

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
) -> Response[Any | GovernanceAiAcceptResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | GovernanceAiAcceptResponse | HTTPValidationError]:
    """Accept a governance plan

     Execute the proposed policy changes from a governance AI assistant conversation. Each action is
    applied in order and results are returned.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        conversation_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GovernanceAiAcceptResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Any | GovernanceAiAcceptResponse | HTTPValidationError | None:
    """Accept a governance plan

     Execute the proposed policy changes from a governance AI assistant conversation. Each action is
    applied in order and results are returned.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        conversation_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GovernanceAiAcceptResponse | HTTPValidationError
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | GovernanceAiAcceptResponse | HTTPValidationError]:
    """Accept a governance plan

     Execute the proposed policy changes from a governance AI assistant conversation. Each action is
    applied in order and results are returned.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        conversation_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GovernanceAiAcceptResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Any | GovernanceAiAcceptResponse | HTTPValidationError | None:
    """Accept a governance plan

     Execute the proposed policy changes from a governance AI assistant conversation. Each action is
    applied in order and results are returned.

    Auth: requires `X-API-Key` header or OAuth Bearer token with governance access.

    Args:
        conversation_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GovernanceAiAcceptResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
