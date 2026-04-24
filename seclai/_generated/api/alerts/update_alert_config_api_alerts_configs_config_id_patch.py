from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_alert_config_api_alerts_configs_config_id_patch_response_update_alert_config_api_alerts_configs_config_id_patch import (
    UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch,
)
from ...models.update_alert_config_request import UpdateAlertConfigRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    config_id: str,
    *,
    body: UpdateAlertConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/alerts/configs/{config_id}".format(
            config_id=quote(str(config_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
    | None
):
    if response.status_code == 200:
        response_200 = UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch.from_dict(
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
    | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
]:
    """Update alert config

     Update an alert configuration. Only provided fields are updated.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        config_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
    | None
):
    """Update alert config

     Update an alert configuration. Only provided fields are updated.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        config_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
    """

    return sync_detailed(
        config_id=config_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
]:
    """Update alert config

     Update an alert configuration. Only provided fields are updated.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        config_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAlertConfigRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
    | None
):
    """Update alert config

     Update an alert configuration. Only provided fields are updated.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        config_id (str):
        x_account_id (UUID | Unset):
        body (UpdateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateAlertConfigApiAlertsConfigsConfigIdPatchResponseUpdateAlertConfigApiAlertsConfigsConfigIdPatch
    """

    return (
        await asyncio_detailed(
            config_id=config_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
