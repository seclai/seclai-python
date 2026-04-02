from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_alerts_api_models_alerts_get_response_list_alerts_api_models_alerts_get import (
    ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | str | Unset = UNSET,
    unread_only: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    params["unread_only"] = unread_only

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/alerts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
    | None
):
    if response.status_code == 200:
        response_200 = (
            ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet.from_dict(
                response.json()
            )
        )

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
) -> Response[
    HTTPValidationError
    | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    unread_only: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
]:
    """List Alerts

     List model lifecycle alerts for the account.

    Returns in-app notifications about model deprecations, sunsets, and newer model availability.
    Supports filtering by agent, unread-only, and pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Alerts are scoped to the caller's account.

    Args:
        agent_id (None | str | Unset): Filter alerts to a specific agent UUID.
        unread_only (bool | Unset): When true, only return unread alerts. Default: False.
        limit (int | Unset): Maximum number of alerts to return (1-100). Default: 50.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        unread_only=unread_only,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    unread_only: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
    | None
):
    """List Alerts

     List model lifecycle alerts for the account.

    Returns in-app notifications about model deprecations, sunsets, and newer model availability.
    Supports filtering by agent, unread-only, and pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Alerts are scoped to the caller's account.

    Args:
        agent_id (None | str | Unset): Filter alerts to a specific agent UUID.
        unread_only (bool | Unset): When true, only return unread alerts. Default: False.
        limit (int | Unset): Maximum number of alerts to return (1-100). Default: 50.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        unread_only=unread_only,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    unread_only: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
]:
    """List Alerts

     List model lifecycle alerts for the account.

    Returns in-app notifications about model deprecations, sunsets, and newer model availability.
    Supports filtering by agent, unread-only, and pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Alerts are scoped to the caller's account.

    Args:
        agent_id (None | str | Unset): Filter alerts to a specific agent UUID.
        unread_only (bool | Unset): When true, only return unread alerts. Default: False.
        limit (int | Unset): Maximum number of alerts to return (1-100). Default: 50.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        unread_only=unread_only,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    unread_only: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
    | None
):
    """List Alerts

     List model lifecycle alerts for the account.

    Returns in-app notifications about model deprecations, sunsets, and newer model availability.
    Supports filtering by agent, unread-only, and pagination.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Alerts are scoped to the caller's account.

    Args:
        agent_id (None | str | Unset): Filter alerts to a specific agent UUID.
        unread_only (bool | Unset): When true, only return unread alerts. Default: False.
        limit (int | Unset): Maximum number of alerts to return (1-100). Default: 50.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAlertsApiModelsAlertsGetResponseListAlertsApiModelsAlertsGet
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            unread_only=unread_only,
            limit=limit,
            offset=offset,
            x_account_id=x_account_id,
        )
    ).parsed
