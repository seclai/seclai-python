from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_drive_response_model import CloudDriveResponseModel
from ...models.cloud_drive_update_request import CloudDriveUpdateRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_id: UUID,
    *,
    body: CloudDriveUpdateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud-drives/{connection_id}".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = CloudDriveResponseModel.from_dict(response.json())

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
) -> Response[CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError]:
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
    body: CloudDriveUpdateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError]:
    """Update a cloud-drive connection

     Rename a connection and/or change the folder it watches. Changing the folder resets the sync cursor,
    so existing files in the new folder are not replayed as triggers.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CloudDriveUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
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
    body: CloudDriveUpdateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError | None:
    """Update a cloud-drive connection

     Rename a connection and/or change the folder it watches. Changing the folder resets the sync cursor,
    so existing files in the new folder are not replayed as triggers.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CloudDriveUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloudDriveUpdateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError]:
    """Update a cloud-drive connection

     Rename a connection and/or change the folder it watches. Changing the folder resets the sync cursor,
    so existing files in the new folder are not replayed as triggers.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CloudDriveUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloudDriveUpdateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError | None:
    """Update a cloud-drive connection

     Rename a connection and/or change the folder it watches. Changing the folder resets the sync cursor,
    so existing files in the new folder are not replayed as triggers.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (CloudDriveUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudDriveResponseModel | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
