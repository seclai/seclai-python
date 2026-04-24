from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.prompt_model_response import PromptModelResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/{model_id}/details".format(
            model_id=quote(str(model_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PromptModelResponse | None:
    if response.status_code == 200:
        response_200 = PromptModelResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PromptModelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | PromptModelResponse]:
    """Get Model

     Get detailed information about a specific model.

    Returns full model details including capabilities, credit pricing, tool support, variant tiers, and
    lifecycle status.

    The `model_id` is the model enum identifier (e.g. 'anthropic_claude_opus_4_6').

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PromptModelResponse]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | PromptModelResponse | None:
    """Get Model

     Get detailed information about a specific model.

    Returns full model details including capabilities, credit pricing, tool support, variant tiers, and
    lifecycle status.

    The `model_id` is the model enum identifier (e.g. 'anthropic_claude_opus_4_6').

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PromptModelResponse
    """

    return sync_detailed(
        model_id=model_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | PromptModelResponse]:
    """Get Model

     Get detailed information about a specific model.

    Returns full model details including capabilities, credit pricing, tool support, variant tiers, and
    lifecycle status.

    The `model_id` is the model enum identifier (e.g. 'anthropic_claude_opus_4_6').

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PromptModelResponse]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | PromptModelResponse | None:
    """Get Model

     Get detailed information about a specific model.

    Returns full model details including capabilities, credit pricing, tool support, variant tiers, and
    lifecycle status.

    The `model_id` is the model enum identifier (e.g. 'anthropic_claude_opus_4_6').

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PromptModelResponse
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
