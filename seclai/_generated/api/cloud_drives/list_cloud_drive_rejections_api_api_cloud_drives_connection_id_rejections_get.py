from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_drive_rejection_response_model import (
    CloudDriveRejectionResponseModel,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_id: UUID,
    *,
    limit: int | Unset = 50,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud-drives/{connection_id}/rejections".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | list[CloudDriveRejectionResponseModel]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CloudDriveRejectionResponseModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
    HTTPValidationError
    | ServiceUnavailableError
    | list[CloudDriveRejectionResponseModel]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ServiceUnavailableError
    | list[CloudDriveRejectionResponseModel]
]:
    r"""List files this connection did not process

     Recent files the connection deliberately skipped, newest first, with the reason: `too_large` (above
    the size cap), `download_failed` (the provider would not serve the bytes), or `flood` (the per-sync
    or per-account run cap was hit, so remaining changes were dropped).

    This is the answer to \"why didn't my agent run for that file?\" — a skipped file fires no trigger
    and appears nowhere else.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        limit (int | Unset):  Default: 50.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | list[CloudDriveRejectionResponseModel]]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | list[CloudDriveRejectionResponseModel]
    | None
):
    r"""List files this connection did not process

     Recent files the connection deliberately skipped, newest first, with the reason: `too_large` (above
    the size cap), `download_failed` (the provider would not serve the bytes), or `flood` (the per-sync
    or per-account run cap was hit, so remaining changes were dropped).

    This is the answer to \"why didn't my agent run for that file?\" — a skipped file fires no trigger
    and appears nowhere else.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        limit (int | Unset):  Default: 50.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | list[CloudDriveRejectionResponseModel]
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ServiceUnavailableError
    | list[CloudDriveRejectionResponseModel]
]:
    r"""List files this connection did not process

     Recent files the connection deliberately skipped, newest first, with the reason: `too_large` (above
    the size cap), `download_failed` (the provider would not serve the bytes), or `flood` (the per-sync
    or per-account run cap was hit, so remaining changes were dropped).

    This is the answer to \"why didn't my agent run for that file?\" — a skipped file fires no trigger
    and appears nowhere else.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        limit (int | Unset):  Default: 50.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | list[CloudDriveRejectionResponseModel]]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | list[CloudDriveRejectionResponseModel]
    | None
):
    r"""List files this connection did not process

     Recent files the connection deliberately skipped, newest first, with the reason: `too_large` (above
    the size cap), `download_failed` (the provider would not serve the bytes), or `flood` (the per-sync
    or per-account run cap was hit, so remaining changes were dropped).

    This is the answer to \"why didn't my agent run for that file?\" — a skipped file fires no trigger
    and appears nowhere else.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        limit (int | Unset):  Default: 50.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | list[CloudDriveRejectionResponseModel]
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            limit=limit,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
