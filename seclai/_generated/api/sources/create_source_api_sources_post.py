from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_source_body import CreateSourceBody
from ...models.http_validation_error import HTTPValidationError
from ...models.source_response import SourceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSourceBody,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | SourceResponse | None:
    if response.status_code == 201:
        response_201 = SourceResponse.from_dict(response.json())

        return response_201

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | SourceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSourceBody,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError | SourceResponse]:
    """Create Source

     Create a new content source.

    Source types: `rss`, `website`, `file_uploads`, `custom_index`.

    For RSS and website sources, provide the URL. For file upload and custom index sources, the URL is
    created automatically.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSourceBody): Request body for creating a content source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SourceResponse]
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
    body: CreateSourceBody,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | SourceResponse | None:
    """Create Source

     Create a new content source.

    Source types: `rss`, `website`, `file_uploads`, `custom_index`.

    For RSS and website sources, provide the URL. For file upload and custom index sources, the URL is
    created automatically.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSourceBody): Request body for creating a content source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SourceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSourceBody,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError | SourceResponse]:
    """Create Source

     Create a new content source.

    Source types: `rss`, `website`, `file_uploads`, `custom_index`.

    For RSS and website sources, provide the URL. For file upload and custom index sources, the URL is
    created automatically.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSourceBody): Request body for creating a content source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SourceResponse]
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
    body: CreateSourceBody,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | SourceResponse | None:
    """Create Source

     Create a new content source.

    Source types: `rss`, `website`, `file_uploads`, `custom_index`.

    For RSS and website sources, provide the URL. For file upload and custom index sources, the URL is
    created automatically.

    Args:
        x_account_id (UUID | Unset):
        body (CreateSourceBody): Request body for creating a content source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SourceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
