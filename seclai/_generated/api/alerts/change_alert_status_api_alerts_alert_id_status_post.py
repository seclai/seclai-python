from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_alert_status_api_alerts_alert_id_status_post_response_change_alert_status_api_alerts_alert_id_status_post import (
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost,
)
from ...models.change_status_request import ChangeStatusRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_id: str,
    *,
    body: ChangeStatusRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alerts/{alert_id}/status".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost.from_dict(
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
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost
    | HTTPValidationError
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
    body: ChangeStatusRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost
    | HTTPValidationError
]:
    """Change alert status

     Change the status of an alert. Valid statuses: triggered, acknowledged, resolved, dismissed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):
        body (ChangeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
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
    body: ChangeStatusRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost
    | HTTPValidationError
    | None
):
    """Change alert status

     Change the status of an alert. Valid statuses: triggered, acknowledged, resolved, dismissed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):
        body (ChangeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost | HTTPValidationError
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangeStatusRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost
    | HTTPValidationError
]:
    """Change alert status

     Change the status of an alert. Valid statuses: triggered, acknowledged, resolved, dismissed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):
        body (ChangeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangeStatusRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost
    | HTTPValidationError
    | None
):
    """Change alert status

     Change the status of an alert. Valid statuses: triggered, acknowledged, resolved, dismissed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        alert_id (str):
        x_account_id (UUID | Unset):
        body (ChangeStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeAlertStatusApiAlertsAlertIdStatusPostResponseChangeAlertStatusApiAlertsAlertIdStatusPost | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
