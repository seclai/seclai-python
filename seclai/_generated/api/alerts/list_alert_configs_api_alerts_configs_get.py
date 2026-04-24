from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_alert_configs_api_alerts_configs_get_response_list_alert_configs_api_alerts_configs_get import (
    ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
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

    json_source_connection_id: None | str | Unset
    if isinstance(source_connection_id, Unset):
        json_source_connection_id = UNSET
    else:
        json_source_connection_id = source_connection_id
    params["source_connection_id"] = json_source_connection_id

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/configs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
    | None
):
    if response.status_code == 200:
        response_200 = ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet.from_dict(
            response.json()
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
    | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
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
    source_connection_id: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
]:
    """List alert configs

     List alert configurations.

    Filters:
    - `agent_id`: list configs for a specific agent
    - `source_connection_id`: list configs for a specific source
    - Neither: list account-level agent alert configs
    - `scope=source`: list account-level source alert configs

    Credits alerts (`credits_low_threshold`, `credits_runout_prediction`, `credits_usage_spike`) are
    account-level alert configs. They are evaluated by the credits alert sweep and default-enabled
    configs may be auto-created for active accounts at runtime.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        scope (None | str | Unset): Set to 'source' to list account-level source alert configs
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        source_connection_id=source_connection_id,
        scope=scope,
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
    source_connection_id: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
    | None
):
    """List alert configs

     List alert configurations.

    Filters:
    - `agent_id`: list configs for a specific agent
    - `source_connection_id`: list configs for a specific source
    - Neither: list account-level agent alert configs
    - `scope=source`: list account-level source alert configs

    Credits alerts (`credits_low_threshold`, `credits_runout_prediction`, `credits_usage_spike`) are
    account-level alert configs. They are evaluated by the credits alert sweep and default-enabled
    configs may be auto-created for active accounts at runtime.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        scope (None | str | Unset): Set to 'source' to list account-level source alert configs
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        source_connection_id=source_connection_id,
        scope=scope,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
]:
    """List alert configs

     List alert configurations.

    Filters:
    - `agent_id`: list configs for a specific agent
    - `source_connection_id`: list configs for a specific source
    - Neither: list account-level agent alert configs
    - `scope=source`: list account-level source alert configs

    Credits alerts (`credits_low_threshold`, `credits_runout_prediction`, `credits_usage_spike`) are
    account-level alert configs. They are evaluated by the credits alert sweep and default-enabled
    configs may be auto-created for active accounts at runtime.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        scope (None | str | Unset): Set to 'source' to list account-level source alert configs
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        source_connection_id=source_connection_id,
        scope=scope,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
    | None
):
    """List alert configs

     List alert configurations.

    Filters:
    - `agent_id`: list configs for a specific agent
    - `source_connection_id`: list configs for a specific source
    - Neither: list account-level agent alert configs
    - `scope=source`: list account-level source alert configs

    Credits alerts (`credits_low_threshold`, `credits_runout_prediction`, `credits_usage_spike`) are
    account-level alert configs. They are evaluated by the credits alert sweep and default-enabled
    configs may be auto-created for active accounts at runtime.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        scope (None | str | Unset): Set to 'source' to list account-level source alert configs
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAlertConfigsApiAlertsConfigsGetResponseListAlertConfigsApiAlertsConfigsGet
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            source_connection_id=source_connection_id,
            scope=scope,
            x_account_id=x_account_id,
        )
    ).parsed
