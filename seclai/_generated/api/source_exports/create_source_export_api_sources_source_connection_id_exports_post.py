from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_export_request import CreateExportRequest
from ...models.export_response import ExportResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    body: CreateExportRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources/{source_connection_id}/exports".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ExportResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 202:
        response_202 = ExportResponse.from_dict(response.json())

        return response_202

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
) -> Response[Any | ExportResponse | HTTPValidationError | ServiceUnavailableError]:
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
    body: CreateExportRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | ExportResponse | HTTPValidationError | ServiceUnavailableError]:
    """Create export

     Start an asynchronous export job. Poll GET .../exports/{export_id} until status becomes completed,
    then use /download to retrieve the file.  On an organization account, a key bound to a user must
    belong to an owner or administrator; a viewer's key is refused with 403 `permission_denied`.
    Personal accounts and account-scoped keys are unaffected.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CreateExportRequest): Parameters for creating a new export job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExportResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateExportRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | ExportResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Create export

     Start an asynchronous export job. Poll GET .../exports/{export_id} until status becomes completed,
    then use /download to retrieve the file.  On an organization account, a key bound to a user must
    belong to an owner or administrator; a viewer's key is refused with 403 `permission_denied`.
    Personal accounts and account-scoped keys are unaffected.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CreateExportRequest): Parameters for creating a new export job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExportResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        source_connection_id=source_connection_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateExportRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[Any | ExportResponse | HTTPValidationError | ServiceUnavailableError]:
    """Create export

     Start an asynchronous export job. Poll GET .../exports/{export_id} until status becomes completed,
    then use /download to retrieve the file.  On an organization account, a key bound to a user must
    belong to an owner or administrator; a viewer's key is refused with 403 `permission_denied`.
    Personal accounts and account-scoped keys are unaffected.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CreateExportRequest): Parameters for creating a new export job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExportResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        source_connection_id=source_connection_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateExportRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Any | ExportResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Create export

     Start an asynchronous export job. Poll GET .../exports/{export_id} until status becomes completed,
    then use /download to retrieve the file.  On an organization account, a key bound to a user must
    belong to an owner or administrator; a viewer's key is refused with 403 `permission_denied`.
    Personal accounts and account-scoped keys are unaffected.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CreateExportRequest): Parameters for creating a new export job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExportResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
