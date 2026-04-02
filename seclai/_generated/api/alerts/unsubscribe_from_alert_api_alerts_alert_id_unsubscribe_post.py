from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.unsubscribe_from_alert_api_alerts_alert_id_unsubscribe_post_response_unsubscribe_from_alert_api_alerts_alert_id_unsubscribe_post import (
    UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alerts/{alert_id}/unsubscribe".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
    | None
):
    if response.status_code == 200:
        response_200 = UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost.from_dict(
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
    | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
]:
    """Unsubscribe from alert

     Unsubscribe the current user from an alert. The user will no longer receive email notifications for
    status changes or new comments on this alert.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
    | None
):
    """Unsubscribe from alert

     Unsubscribe the current user from an alert. The user will no longer receive email notifications for
    status changes or new comments on this alert.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
]:
    """Unsubscribe from alert

     Unsubscribe the current user from an alert. The user will no longer receive email notifications for
    status changes or new comments on this alert.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
    | None
):
    """Unsubscribe from alert

     Unsubscribe the current user from an alert. The user will no longer receive email notifications for
    status changes or new comments on this alert.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UnsubscribeFromAlertApiAlertsAlertIdUnsubscribePostResponseUnsubscribeFromAlertApiAlertsAlertIdUnsubscribePost
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
