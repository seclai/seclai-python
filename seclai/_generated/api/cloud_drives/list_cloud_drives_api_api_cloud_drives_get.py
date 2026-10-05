from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_drive_response_model import CloudDriveResponseModel
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
        "url": "/cloud-drives",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceUnavailableError | list[CloudDriveResponseModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CloudDriveResponseModel.from_dict(
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
) -> Response[ServiceUnavailableError | list[CloudDriveResponseModel]]:
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
) -> Response[ServiceUnavailableError | list[CloudDriveResponseModel]]:
    """List the account's cloud-drive connections

     List the account's cloud-drive connections. Use a connection's `id` as `cloud_drive_connection_id`
    when creating a `cloud_drive` content source or binding a file-change agent trigger.
    `realtime_updates` reports whether changes arrive within seconds or on the scheduled backstop sweep.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceUnavailableError | list[CloudDriveResponseModel]]
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
) -> ServiceUnavailableError | list[CloudDriveResponseModel] | None:
    """List the account's cloud-drive connections

     List the account's cloud-drive connections. Use a connection's `id` as `cloud_drive_connection_id`
    when creating a `cloud_drive` content source or binding a file-change agent trigger.
    `realtime_updates` reports whether changes arrive within seconds or on the scheduled backstop sweep.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceUnavailableError | list[CloudDriveResponseModel]
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
) -> Response[ServiceUnavailableError | list[CloudDriveResponseModel]]:
    """List the account's cloud-drive connections

     List the account's cloud-drive connections. Use a connection's `id` as `cloud_drive_connection_id`
    when creating a `cloud_drive` content source or binding a file-change agent trigger.
    `realtime_updates` reports whether changes arrive within seconds or on the scheduled backstop sweep.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceUnavailableError | list[CloudDriveResponseModel]]
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
) -> ServiceUnavailableError | list[CloudDriveResponseModel] | None:
    """List the account's cloud-drive connections

     List the account's cloud-drive connections. Use a connection's `id` as `cloud_drive_connection_id`
    when creating a `cloud_drive` content source or binding a file-change agent trigger.
    `realtime_updates` reports whether changes arrive within seconds or on the scheduled backstop sweep.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceUnavailableError | list[CloudDriveResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
