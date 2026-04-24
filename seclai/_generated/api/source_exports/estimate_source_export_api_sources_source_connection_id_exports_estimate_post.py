from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.estimate_export_request import EstimateExportRequest
from ...models.estimate_export_response import EstimateExportResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_id: UUID,
    *,
    body: EstimateExportRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sources/{source_connection_id}/exports/estimate".format(
            source_connection_id=quote(str(source_connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EstimateExportResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EstimateExportResponse.from_dict(response.json())

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
) -> Response[EstimateExportResponse | HTTPValidationError]:
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
    body: EstimateExportRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[EstimateExportResponse | HTTPValidationError]:
    """Estimate export size

     Return an order-of-magnitude size estimate (in bytes) for an export without creating a job.  Use
    this to show users how large the download will be before they commit to running the export.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (EstimateExportRequest): Parameters for estimating export size.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimateExportResponse | HTTPValidationError]
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
    body: EstimateExportRequest,
    x_account_id: UUID | Unset = UNSET,
) -> EstimateExportResponse | HTTPValidationError | None:
    """Estimate export size

     Return an order-of-magnitude size estimate (in bytes) for an export without creating a job.  Use
    this to show users how large the download will be before they commit to running the export.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (EstimateExportRequest): Parameters for estimating export size.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimateExportResponse | HTTPValidationError
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
    body: EstimateExportRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[EstimateExportResponse | HTTPValidationError]:
    """Estimate export size

     Return an order-of-magnitude size estimate (in bytes) for an export without creating a job.  Use
    this to show users how large the download will be before they commit to running the export.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (EstimateExportRequest): Parameters for estimating export size.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimateExportResponse | HTTPValidationError]
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
    body: EstimateExportRequest,
    x_account_id: UUID | Unset = UNSET,
) -> EstimateExportResponse | HTTPValidationError | None:
    """Estimate export size

     Return an order-of-magnitude size estimate (in bytes) for an export without creating a job.  Use
    this to show users how large the download will be before they commit to running the export.

    Args:
        source_connection_id (UUID):
        x_account_id (UUID | Unset):
        body (EstimateExportRequest): Parameters for estimating export size.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimateExportResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_id=source_connection_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
