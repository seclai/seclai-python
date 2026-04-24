from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_agent_input_api_response import UploadAgentInputApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    upload_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/input-uploads/{upload_id}".format(
            agent_id=quote(str(agent_id), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UploadAgentInputApiResponse | None:
    if response.status_code == 200:
        response_200 = UploadAgentInputApiResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UploadAgentInputApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | UploadAgentInputApiResponse]:
    """Get upload status

     Poll the processing status of a file upload created via `POST /agents/{agent_id}/upload-input`.

    Possible `status` values: `processing`, `ready`, `failed`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        upload_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadAgentInputApiResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        upload_id=upload_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | UploadAgentInputApiResponse | None:
    """Get upload status

     Poll the processing status of a file upload created via `POST /agents/{agent_id}/upload-input`.

    Possible `status` values: `processing`, `ready`, `failed`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        upload_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadAgentInputApiResponse
    """

    return sync_detailed(
        agent_id=agent_id,
        upload_id=upload_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | UploadAgentInputApiResponse]:
    """Get upload status

     Poll the processing status of a file upload created via `POST /agents/{agent_id}/upload-input`.

    Possible `status` values: `processing`, `ready`, `failed`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        upload_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadAgentInputApiResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        upload_id=upload_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | UploadAgentInputApiResponse | None:
    """Get upload status

     Poll the processing status of a file upload created via `POST /agents/{agent_id}/upload-input`.

    Possible `status` values: `processing`, `ready`, `failed`.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. All resources are scoped to the caller's
    account.

    Args:
        agent_id (str):
        upload_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadAgentInputApiResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            upload_id=upload_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
