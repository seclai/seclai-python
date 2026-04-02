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
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/{source_connection_id}/embedding-migration".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | None | SourceEmbeddingMigrationResponse | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> None | SourceEmbeddingMigrationResponse:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SourceEmbeddingMigrationResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceEmbeddingMigrationResponse, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[HTTPValidationError | None | SourceEmbeddingMigrationResponse]:
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
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | None | SourceEmbeddingMigrationResponse]:
    """Get Source Embedding Migration

     Get the latest embedding migration status for a custom-index source.

    Returns `null` when no migration has ever been started for this source.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | None | SourceEmbeddingMigrationResponse]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
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
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | None | SourceEmbeddingMigrationResponse | None:
    """Get Source Embedding Migration

     Get the latest embedding migration status for a custom-index source.

    Returns `null` when no migration has ever been started for this source.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | None | SourceEmbeddingMigrationResponse
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | None | SourceEmbeddingMigrationResponse]:
    """Get Source Embedding Migration

     Get the latest embedding migration status for a custom-index source.

    Returns `null` when no migration has ever been started for this source.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | None | SourceEmbeddingMigrationResponse]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | None | SourceEmbeddingMigrationResponse | None:
    """Get Source Embedding Migration

     Get the latest embedding migration status for a custom-index source.

    Returns `null` when no migration has ever been started for this source.

    Args:
        source_connection_id (UUID):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | None | SourceEmbeddingMigrationResponse
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
