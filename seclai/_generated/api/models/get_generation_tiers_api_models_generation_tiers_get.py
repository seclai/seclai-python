from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generation_tier_list_response import GenerationTierListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/models/generation-tiers",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenerationTierListResponse | None:
    if response.status_code == 200:
        response_200 = GenerationTierListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenerationTierListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[GenerationTierListResponse]:
    """Get Generation Tiers

     List the media-generation quality tiers and the model + cost each resolves to.

    On a prompt_call's `media_generation` tool — and the dedicated generate_* steps via tier routing —
    the author/LLM chooses a *tier* (fast/balanced/thorough), never a model. This is the surface that
    maps each `(modality, tier)` to its concrete generator, raw `credits_per_unit`, `unit_label`, and a
    human-readable scaled `price_label`. Global routing/pricing (the same for every account); read-only.
    REST parity with the `list_generation_tiers` MCP tool.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerationTierListResponse]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> GenerationTierListResponse | None:
    """Get Generation Tiers

     List the media-generation quality tiers and the model + cost each resolves to.

    On a prompt_call's `media_generation` tool — and the dedicated generate_* steps via tier routing —
    the author/LLM chooses a *tier* (fast/balanced/thorough), never a model. This is the surface that
    maps each `(modality, tier)` to its concrete generator, raw `credits_per_unit`, `unit_label`, and a
    human-readable scaled `price_label`. Global routing/pricing (the same for every account); read-only.
    REST parity with the `list_generation_tiers` MCP tool.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerationTierListResponse
    """

    return sync_detailed(
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[GenerationTierListResponse]:
    """Get Generation Tiers

     List the media-generation quality tiers and the model + cost each resolves to.

    On a prompt_call's `media_generation` tool — and the dedicated generate_* steps via tier routing —
    the author/LLM chooses a *tier* (fast/balanced/thorough), never a model. This is the surface that
    maps each `(modality, tier)` to its concrete generator, raw `credits_per_unit`, `unit_label`, and a
    human-readable scaled `price_label`. Global routing/pricing (the same for every account); read-only.
    REST parity with the `list_generation_tiers` MCP tool.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerationTierListResponse]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> GenerationTierListResponse | None:
    """Get Generation Tiers

     List the media-generation quality tiers and the model + cost each resolves to.

    On a prompt_call's `media_generation` tool — and the dedicated generate_* steps via tier routing —
    the author/LLM chooses a *tier* (fast/balanced/thorough), never a model. This is the surface that
    maps each `(modality, tier)` to its concrete generator, raw `credits_per_unit`, `unit_label`, and a
    human-readable scaled `price_label`. Global routing/pricing (the same for every account); read-only.
    REST parity with the `list_generation_tiers` MCP tool.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerationTierListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
