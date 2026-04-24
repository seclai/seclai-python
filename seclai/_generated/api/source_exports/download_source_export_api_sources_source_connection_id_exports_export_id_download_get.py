from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    export_id: UUID,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/{source_connection_id}/exports/{export_id}/download".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
            export_id=quote(str(export_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_id: UUID,
    export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Download export

     Stream the completed export file.  Returns the file content with appropriate Content-Type and
    Content-Disposition headers.  Returns 409 if the export is not yet completed and 410 if it has
    expired.

    Args:
        source_connection_id (UUID):
        export_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        export_id=export_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: UUID,
    export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Download export

     Stream the completed export file.  Returns the file content with appropriate Content-Type and
    Content-Disposition headers.  Returns 409 if the export is not yet completed and 410 if it has
    expired.

    Args:
        source_connection_id (UUID):
        export_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        export_id=export_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Download export

     Stream the completed export file.  Returns the file content with appropriate Content-Type and
    Content-Disposition headers.  Returns 409 if the export is not yet completed and 410 if it has
    expired.

    Args:
        source_connection_id (UUID):
        export_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        export_id=export_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Download export

     Stream the completed export file.  Returns the file content with appropriate Content-Type and
    Content-Disposition headers.  Returns 409 if the export is not yet completed and 410 if it has
    expired.

    Args:
        source_connection_id (UUID):
        export_id (UUID):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            export_id=export_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
