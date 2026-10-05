from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embedding_model_list_response import EmbeddingModelListResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    supports_input_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    json_supports_input_media: None | str | Unset
    if isinstance(supports_input_media, Unset):
        json_supports_input_media = UNSET
    else:
        json_supports_input_media = supports_input_media
    params["supports_input_media"] = json_supports_input_media

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/embedders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = EmbeddingModelListResponse.from_dict(response.json())

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
) -> Response[
    EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    supports_input_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError
]:
    """List Embedding Models

     List the embedding models a source can be created with.

    Each entry carries the `model_type` to pass as `embedding_model` when creating a source, the
    `dimensions` it supports, and — most importantly for multi-modal indexing — `supported_input_media`:
    the modalities that embedder can actually index. A source only honours a `media_types` entry its
    embedder lists here; unsupported kinds are dropped at save time with an `embedder_warning`, so check
    this before choosing an embedder for a knowledge base of images or video.

    Text-only embedders report `supported_input_media` as null. Pricing is reported as `credits` (per
    ~1,000 English words of text) plus `per_modality_rates` for the non-text modalities a multi-modal
    embedder bills differently.

    An embedder whose credit rate has not been published yet is omitted, so you are never offered one
    that cannot be billed.

    Optional query parameters:
    - `supports_input_media`: keep only embedders that can index this modality
    (`text`/`image`/`video`/`audio` or a full MIME)

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The catalog is global reference data, identical
    for every account.

    Args:
        supports_input_media (None | str | Unset): Filter to embedders that can index this input
            modality — a coarse kind (text, image, video, audio) or a full MIME.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        supports_input_media=supports_input_media,
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
    supports_input_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError | None:
    """List Embedding Models

     List the embedding models a source can be created with.

    Each entry carries the `model_type` to pass as `embedding_model` when creating a source, the
    `dimensions` it supports, and — most importantly for multi-modal indexing — `supported_input_media`:
    the modalities that embedder can actually index. A source only honours a `media_types` entry its
    embedder lists here; unsupported kinds are dropped at save time with an `embedder_warning`, so check
    this before choosing an embedder for a knowledge base of images or video.

    Text-only embedders report `supported_input_media` as null. Pricing is reported as `credits` (per
    ~1,000 English words of text) plus `per_modality_rates` for the non-text modalities a multi-modal
    embedder bills differently.

    An embedder whose credit rate has not been published yet is omitted, so you are never offered one
    that cannot be billed.

    Optional query parameters:
    - `supports_input_media`: keep only embedders that can index this modality
    (`text`/`image`/`video`/`audio` or a full MIME)

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The catalog is global reference data, identical
    for every account.

    Args:
        supports_input_media (None | str | Unset): Filter to embedders that can index this input
            modality — a coarse kind (text, image, video, audio) or a full MIME.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        client=client,
        supports_input_media=supports_input_media,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    supports_input_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError
]:
    """List Embedding Models

     List the embedding models a source can be created with.

    Each entry carries the `model_type` to pass as `embedding_model` when creating a source, the
    `dimensions` it supports, and — most importantly for multi-modal indexing — `supported_input_media`:
    the modalities that embedder can actually index. A source only honours a `media_types` entry its
    embedder lists here; unsupported kinds are dropped at save time with an `embedder_warning`, so check
    this before choosing an embedder for a knowledge base of images or video.

    Text-only embedders report `supported_input_media` as null. Pricing is reported as `credits` (per
    ~1,000 English words of text) plus `per_modality_rates` for the non-text modalities a multi-modal
    embedder bills differently.

    An embedder whose credit rate has not been published yet is omitted, so you are never offered one
    that cannot be billed.

    Optional query parameters:
    - `supports_input_media`: keep only embedders that can index this modality
    (`text`/`image`/`video`/`audio` or a full MIME)

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The catalog is global reference data, identical
    for every account.

    Args:
        supports_input_media (None | str | Unset): Filter to embedders that can index this input
            modality — a coarse kind (text, image, video, audio) or a full MIME.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        supports_input_media=supports_input_media,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    supports_input_media: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError | None:
    """List Embedding Models

     List the embedding models a source can be created with.

    Each entry carries the `model_type` to pass as `embedding_model` when creating a source, the
    `dimensions` it supports, and — most importantly for multi-modal indexing — `supported_input_media`:
    the modalities that embedder can actually index. A source only honours a `media_types` entry its
    embedder lists here; unsupported kinds are dropped at save time with an `embedder_warning`, so check
    this before choosing an embedder for a knowledge base of images or video.

    Text-only embedders report `supported_input_media` as null. Pricing is reported as `credits` (per
    ~1,000 English words of text) plus `per_modality_rates` for the non-text modalities a multi-modal
    embedder bills differently.

    An embedder whose credit rate has not been published yet is omitted, so you are never offered one
    that cannot be billed.

    Optional query parameters:
    - `supports_input_media`: keep only embedders that can index this modality
    (`text`/`image`/`video`/`audio` or a full MIME)

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The catalog is global reference data, identical
    for every account.

    Args:
        supports_input_media (None | str | Unset): Filter to embedders that can index this input
            modality — a coarse kind (text, image, video, audio) or a full MIME.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbeddingModelListResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            client=client,
            supports_input_media=supports_input_media,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
