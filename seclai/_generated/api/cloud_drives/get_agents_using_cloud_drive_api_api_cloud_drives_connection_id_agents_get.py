from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_using_cloud_drive_response_model import (
    AgentUsingCloudDriveResponseModel,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_id: UUID,
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
        "url": "/cloud-drives/{connection_id}/agents".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | list[AgentUsingCloudDriveResponseModel]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AgentUsingCloudDriveResponseModel.from_dict(
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
    | list[AgentUsingCloudDriveResponseModel]
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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ServiceUnavailableError
    | list[AgentUsingCloudDriveResponseModel]
]:
    """List agents using a cloud-drive connection

     Agents that reference this connection — via a cloud-drive step, a `prompt_call` cloud-drive tool, or
    a file-change trigger. Check this before disconnecting or deleting a connection.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | list[AgentUsingCloudDriveResponseModel]]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | list[AgentUsingCloudDriveResponseModel]
    | None
):
    """List agents using a cloud-drive connection

     Agents that reference this connection — via a cloud-drive step, a `prompt_call` cloud-drive tool, or
    a file-change trigger. Check this before disconnecting or deleting a connection.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | list[AgentUsingCloudDriveResponseModel]
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ServiceUnavailableError
    | list[AgentUsingCloudDriveResponseModel]
]:
    """List agents using a cloud-drive connection

     Agents that reference this connection — via a cloud-drive step, a `prompt_call` cloud-drive tool, or
    a file-change trigger. Check this before disconnecting or deleting a connection.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | list[AgentUsingCloudDriveResponseModel]]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ServiceUnavailableError
    | list[AgentUsingCloudDriveResponseModel]
    | None
):
    """List agents using a cloud-drive connection

     Agents that reference this connection — via a cloud-drive step, a `prompt_call` cloud-drive tool, or
    a file-change trigger. Check this before disconnecting or deleting a connection.

    Requires an API key or OAuth token scoped to the account. Cloud-drive secrets are never returned.

    Args:
        connection_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | list[AgentUsingCloudDriveResponseModel]
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
