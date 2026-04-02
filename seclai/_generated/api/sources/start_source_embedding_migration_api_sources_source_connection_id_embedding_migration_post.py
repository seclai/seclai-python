from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.source_embedding_migration_response import (
    SourceEmbeddingMigrationResponse,
)
from ...models.start_source_embedding_migration_request import (
    StartSourceEmbeddingMigrationRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    body: StartSourceEmbeddingMigrationRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources/{source_connection_id}/embedding-migration".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | SourceEmbeddingMigrationResponse | None:
    if response.status_code == 200:
        response_200 = SourceEmbeddingMigrationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | SourceEmbeddingMigrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: StartSourceEmbeddingMigrationRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | SourceEmbeddingMigrationResponse]:
    """Start Source Embedding Migration

     Start an embedding model migration for a custom-index source.

    The migration runs asynchronously in the background.  Poll `GET /api/sources/{id}/embedding-
    migration` to track progress.

    Optionally override chunking configuration (`chunk_size`, `chunk_overlap`, `chunk_language`,
    `chunk_separators`, `chunk_regex_separators`).  When a chunking field is omitted (null), the current
    source's value is preserved.

    Constraints:
    - Only `custom_index` source types support migration.
    - A migration cannot be started while another is already active.
    - The target model + dimensions must differ from the source's current settings.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):
        body (StartSourceEmbeddingMigrationRequest): Request payload to start a source embedding
            migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SourceEmbeddingMigrationResponse]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: StartSourceEmbeddingMigrationRequest,
    x_account_id: str | Unset = UNSET,
) -> Any | HTTPValidationError | SourceEmbeddingMigrationResponse | None:
    """Start Source Embedding Migration

     Start an embedding model migration for a custom-index source.

    The migration runs asynchronously in the background.  Poll `GET /api/sources/{id}/embedding-
    migration` to track progress.

    Optionally override chunking configuration (`chunk_size`, `chunk_overlap`, `chunk_language`,
    `chunk_separators`, `chunk_regex_separators`).  When a chunking field is omitted (null), the current
    source's value is preserved.

    Constraints:
    - Only `custom_index` source types support migration.
    - A migration cannot be started while another is already active.
    - The target model + dimensions must differ from the source's current settings.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):
        body (StartSourceEmbeddingMigrationRequest): Request payload to start a source embedding
            migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SourceEmbeddingMigrationResponse
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: StartSourceEmbeddingMigrationRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | SourceEmbeddingMigrationResponse]:
    """Start Source Embedding Migration

     Start an embedding model migration for a custom-index source.

    The migration runs asynchronously in the background.  Poll `GET /api/sources/{id}/embedding-
    migration` to track progress.

    Optionally override chunking configuration (`chunk_size`, `chunk_overlap`, `chunk_language`,
    `chunk_separators`, `chunk_regex_separators`).  When a chunking field is omitted (null), the current
    source's value is preserved.

    Constraints:
    - Only `custom_index` source types support migration.
    - A migration cannot be started while another is already active.
    - The target model + dimensions must differ from the source's current settings.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):
        body (StartSourceEmbeddingMigrationRequest): Request payload to start a source embedding
            migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SourceEmbeddingMigrationResponse]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: StartSourceEmbeddingMigrationRequest,
    x_account_id: str | Unset = UNSET,
) -> Any | HTTPValidationError | SourceEmbeddingMigrationResponse | None:
    """Start Source Embedding Migration

     Start an embedding model migration for a custom-index source.

    The migration runs asynchronously in the background.  Poll `GET /api/sources/{id}/embedding-
    migration` to track progress.

    Optionally override chunking configuration (`chunk_size`, `chunk_overlap`, `chunk_language`,
    `chunk_separators`, `chunk_regex_separators`).  When a chunking field is omitted (null), the current
    source's value is preserved.

    Constraints:
    - Only `custom_index` source types support migration.
    - A migration cannot be started while another is already active.
    - The target model + dimensions must differ from the source's current settings.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):
        body (StartSourceEmbeddingMigrationRequest): Request payload to start a source embedding
            migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SourceEmbeddingMigrationResponse
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
