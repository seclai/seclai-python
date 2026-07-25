from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.provider_group_response import ProviderGroupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider: None | str | Unset = UNSET,
    supports_tool_use: bool | None | Unset = UNSET,
    supports_thinking: bool | None | Unset = UNSET,
    supports_input_media: None | str | Unset = UNSET,
    supports_output_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_provider: None | str | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider

    json_supports_tool_use: bool | None | Unset
    if isinstance(supports_tool_use, Unset):
        json_supports_tool_use = UNSET
    else:
        json_supports_tool_use = supports_tool_use
    params["supports_tool_use"] = json_supports_tool_use

    json_supports_thinking: bool | None | Unset
    if isinstance(supports_thinking, Unset):
        json_supports_thinking = UNSET
    else:
        json_supports_thinking = supports_thinking
    params["supports_thinking"] = json_supports_thinking

    json_supports_input_media: None | str | Unset
    if isinstance(supports_input_media, Unset):
        json_supports_input_media = UNSET
    else:
        json_supports_input_media = supports_input_media
    params["supports_input_media"] = json_supports_input_media

    json_supports_output_media: None | str | Unset
    if isinstance(supports_output_media, Unset):
        json_supports_output_media = UNSET
    else:
        json_supports_output_media = supports_output_media
    params["supports_output_media"] = json_supports_output_media

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ProviderGroupResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderGroupResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[ProviderGroupResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider: None | str | Unset = UNSET,
    supports_tool_use: bool | None | Unset = UNSET,
    supports_thinking: bool | None | Unset = UNSET,
    supports_input_media: None | str | Unset = UNSET,
    supports_output_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | list[ProviderGroupResponse]]:
    """List Models

     List all enabled LLM models with full details.

    Returns models grouped by provider, including capabilities, credit pricing, tool support, variant
    tiers, and lifecycle status.

    Optional query parameters:
    - `provider`: filter by provider (e.g. 'anthropic', 'openai')
    - `supports_tool_use`: filter to models with tool calling support
    - `supports_thinking`: filter to models with extended thinking support
    - `supports_input_media`: filter to models accepting an input modality
    (`image`/`audio`/`video`/`pdf` or a full MIME)
    - `supports_output_media`: filter to models producing an output modality (`image`/`audio`/`video`) —
    e.g. to find generation models

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        provider (None | str | Unset): Filter by provider name
        supports_tool_use (bool | None | Unset): Filter to models that support tool use
        supports_thinking (bool | None | Unset): Filter to models that support extended thinking
        supports_input_media (None | str | Unset): Filter to models that accept this input
            modality — a coarse kind (`image`, `audio`, `video`, `pdf`) or a full MIME.
        supports_output_media (None | str | Unset): Filter to models that produce this output
            modality — a coarse kind (`image`, `audio`, `video`) or a full MIME. Use to find
            image/audio/video generation models.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ProviderGroupResponse]]
    """

    kwargs = _get_kwargs(
        provider=provider,
        supports_tool_use=supports_tool_use,
        supports_thinking=supports_thinking,
        supports_input_media=supports_input_media,
        supports_output_media=supports_output_media,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    provider: None | str | Unset = UNSET,
    supports_tool_use: bool | None | Unset = UNSET,
    supports_thinking: bool | None | Unset = UNSET,
    supports_input_media: None | str | Unset = UNSET,
    supports_output_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | list[ProviderGroupResponse] | None:
    """List Models

     List all enabled LLM models with full details.

    Returns models grouped by provider, including capabilities, credit pricing, tool support, variant
    tiers, and lifecycle status.

    Optional query parameters:
    - `provider`: filter by provider (e.g. 'anthropic', 'openai')
    - `supports_tool_use`: filter to models with tool calling support
    - `supports_thinking`: filter to models with extended thinking support
    - `supports_input_media`: filter to models accepting an input modality
    (`image`/`audio`/`video`/`pdf` or a full MIME)
    - `supports_output_media`: filter to models producing an output modality (`image`/`audio`/`video`) —
    e.g. to find generation models

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        provider (None | str | Unset): Filter by provider name
        supports_tool_use (bool | None | Unset): Filter to models that support tool use
        supports_thinking (bool | None | Unset): Filter to models that support extended thinking
        supports_input_media (None | str | Unset): Filter to models that accept this input
            modality — a coarse kind (`image`, `audio`, `video`, `pdf`) or a full MIME.
        supports_output_media (None | str | Unset): Filter to models that produce this output
            modality — a coarse kind (`image`, `audio`, `video`) or a full MIME. Use to find
            image/audio/video generation models.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ProviderGroupResponse]
    """

    return sync_detailed(
        client=client,
        provider=provider,
        supports_tool_use=supports_tool_use,
        supports_thinking=supports_thinking,
        supports_input_media=supports_input_media,
        supports_output_media=supports_output_media,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider: None | str | Unset = UNSET,
    supports_tool_use: bool | None | Unset = UNSET,
    supports_thinking: bool | None | Unset = UNSET,
    supports_input_media: None | str | Unset = UNSET,
    supports_output_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | list[ProviderGroupResponse]]:
    """List Models

     List all enabled LLM models with full details.

    Returns models grouped by provider, including capabilities, credit pricing, tool support, variant
    tiers, and lifecycle status.

    Optional query parameters:
    - `provider`: filter by provider (e.g. 'anthropic', 'openai')
    - `supports_tool_use`: filter to models with tool calling support
    - `supports_thinking`: filter to models with extended thinking support
    - `supports_input_media`: filter to models accepting an input modality
    (`image`/`audio`/`video`/`pdf` or a full MIME)
    - `supports_output_media`: filter to models producing an output modality (`image`/`audio`/`video`) —
    e.g. to find generation models

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        provider (None | str | Unset): Filter by provider name
        supports_tool_use (bool | None | Unset): Filter to models that support tool use
        supports_thinking (bool | None | Unset): Filter to models that support extended thinking
        supports_input_media (None | str | Unset): Filter to models that accept this input
            modality — a coarse kind (`image`, `audio`, `video`, `pdf`) or a full MIME.
        supports_output_media (None | str | Unset): Filter to models that produce this output
            modality — a coarse kind (`image`, `audio`, `video`) or a full MIME. Use to find
            image/audio/video generation models.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ProviderGroupResponse]]
    """

    kwargs = _get_kwargs(
        provider=provider,
        supports_tool_use=supports_tool_use,
        supports_thinking=supports_thinking,
        supports_input_media=supports_input_media,
        supports_output_media=supports_output_media,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    provider: None | str | Unset = UNSET,
    supports_tool_use: bool | None | Unset = UNSET,
    supports_thinking: bool | None | Unset = UNSET,
    supports_input_media: None | str | Unset = UNSET,
    supports_output_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | list[ProviderGroupResponse] | None:
    """List Models

     List all enabled LLM models with full details.

    Returns models grouped by provider, including capabilities, credit pricing, tool support, variant
    tiers, and lifecycle status.

    Optional query parameters:
    - `provider`: filter by provider (e.g. 'anthropic', 'openai')
    - `supports_tool_use`: filter to models with tool calling support
    - `supports_thinking`: filter to models with extended thinking support
    - `supports_input_media`: filter to models accepting an input modality
    (`image`/`audio`/`video`/`pdf` or a full MIME)
    - `supports_output_media`: filter to models producing an output modality (`image`/`audio`/`video`) —
    e.g. to find generation models

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        provider (None | str | Unset): Filter by provider name
        supports_tool_use (bool | None | Unset): Filter to models that support tool use
        supports_thinking (bool | None | Unset): Filter to models that support extended thinking
        supports_input_media (None | str | Unset): Filter to models that accept this input
            modality — a coarse kind (`image`, `audio`, `video`, `pdf`) or a full MIME.
        supports_output_media (None | str | Unset): Filter to models that produce this output
            modality — a coarse kind (`image`, `audio`, `video`) or a full MIME. Use to find
            image/audio/video generation models.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ProviderGroupResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            provider=provider,
            supports_tool_use=supports_tool_use,
            supports_thinking=supports_thinking,
            supports_input_media=supports_input_media,
            supports_output_media=supports_output_media,
            x_account_id=x_account_id,
        )
    ).parsed
