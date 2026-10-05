from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_drive_provider_response_model import (
    CloudDriveProviderResponseModel,
)
from ...models.service_unavailable_error import ServiceUnavailableError
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
        "url": "/cloud-drives/providers",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceUnavailableError | list[CloudDriveProviderResponseModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CloudDriveProviderResponseModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 503:
        response_503 = ServiceUnavailableError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceUnavailableError | list[CloudDriveProviderResponseModel]]:
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
) -> Response[ServiceUnavailableError | list[CloudDriveProviderResponseModel]]:
    """List configured cloud-drive providers

     List the cloud-drive providers whose OAuth app is configured on this deployment (e.g. Dropbox,
    Google Drive), with the permissions each requests. A provider missing from this list cannot be
    connected here.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceUnavailableError | list[CloudDriveProviderResponseModel]]
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
) -> ServiceUnavailableError | list[CloudDriveProviderResponseModel] | None:
    """List configured cloud-drive providers

     List the cloud-drive providers whose OAuth app is configured on this deployment (e.g. Dropbox,
    Google Drive), with the permissions each requests. A provider missing from this list cannot be
    connected here.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceUnavailableError | list[CloudDriveProviderResponseModel]
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
) -> Response[ServiceUnavailableError | list[CloudDriveProviderResponseModel]]:
    """List configured cloud-drive providers

     List the cloud-drive providers whose OAuth app is configured on this deployment (e.g. Dropbox,
    Google Drive), with the permissions each requests. A provider missing from this list cannot be
    connected here.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceUnavailableError | list[CloudDriveProviderResponseModel]]
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
) -> ServiceUnavailableError | list[CloudDriveProviderResponseModel] | None:
    """List configured cloud-drive providers

     List the cloud-drive providers whose OAuth app is configured on this deployment (e.g. Dropbox,
    Google Drive), with the permissions each requests. A provider missing from this list cannot be
    connected here.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceUnavailableError | list[CloudDriveProviderResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
