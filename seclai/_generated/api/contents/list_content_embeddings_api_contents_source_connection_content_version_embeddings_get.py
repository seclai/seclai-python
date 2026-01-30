from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_embeddings_list_response import ContentEmbeddingsListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_content_version: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contents/{source_connection_content_version}/embeddings".format(
            source_connection_content_version=quote(str(source_connection_content_version), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContentEmbeddingsListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContentEmbeddingsListResponse.from_dict(response.json())

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
) -> Response[ContentEmbeddingsListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ContentEmbeddingsListResponse | HTTPValidationError]:
    """List content embeddings

     List the embeddings (chunk vectors) for a content item, with pagination.

    Embeddings are used for semantic search and retrieval in knowledge base workflows. This endpoint is
    primarily useful for debugging chunking, indexing, and vector contents.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access embeddings for content belonging to your account.

    Args:
        source_connection_content_version (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentEmbeddingsListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ContentEmbeddingsListResponse | HTTPValidationError | None:
    """List content embeddings

     List the embeddings (chunk vectors) for a content item, with pagination.

    Embeddings are used for semantic search and retrieval in knowledge base workflows. This endpoint is
    primarily useful for debugging chunking, indexing, and vector contents.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access embeddings for content belonging to your account.

    Args:
        source_connection_content_version (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentEmbeddingsListResponse | HTTPValidationError
    """

    return sync_detailed(
        source_connection_content_version=source_connection_content_version,
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ContentEmbeddingsListResponse | HTTPValidationError]:
    """List content embeddings

     List the embeddings (chunk vectors) for a content item, with pagination.

    Embeddings are used for semantic search and retrieval in knowledge base workflows. This endpoint is
    primarily useful for debugging chunking, indexing, and vector contents.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access embeddings for content belonging to your account.

    Args:
        source_connection_content_version (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentEmbeddingsListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ContentEmbeddingsListResponse | HTTPValidationError | None:
    """List content embeddings

     List the embeddings (chunk vectors) for a content item, with pagination.

    Embeddings are used for semantic search and retrieval in knowledge base workflows. This endpoint is
    primarily useful for debugging chunking, indexing, and vector contents.

    Auth & scoping:
    - Requires `X-API-Key`. You can only access embeddings for content belonging to your account.

    Args:
        source_connection_content_version (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentEmbeddingsListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed
