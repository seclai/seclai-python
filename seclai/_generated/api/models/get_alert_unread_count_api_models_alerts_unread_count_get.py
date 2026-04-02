from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_alert_unread_count_api_models_alerts_unread_count_get_response_get_alert_unread_count_api_models_alerts_unread_count_get import (
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/alerts/unread-count",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
    | None
):
    if response.status_code == 200:
        response_200 = GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
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
    x_account_id: str | Unset = UNSET,
) -> Response[
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
]:
    """Get Alert Unread Count

     Get the count of unread model lifecycle alerts.

    Useful for badge indicators in UIs and dashboards.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Count is scoped to the caller's account.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> (
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
    | None
):
    """Get Alert Unread Count

     Get the count of unread model lifecycle alerts.

    Useful for badge indicators in UIs and dashboards.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Count is scoped to the caller's account.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
    """

    return sync_detailed(
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
]:
    """Get Alert Unread Count

     Get the count of unread model lifecycle alerts.

    Useful for badge indicators in UIs and dashboards.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Count is scoped to the caller's account.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> (
    GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
    | None
):
    """Get Alert Unread Count

     Get the count of unread model lifecycle alerts.

    Useful for badge indicators in UIs and dashboards.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Count is scoped to the caller's account.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAlertUnreadCountApiModelsAlertsUnreadCountGetResponseGetAlertUnreadCountApiModelsAlertsUnreadCountGet
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
