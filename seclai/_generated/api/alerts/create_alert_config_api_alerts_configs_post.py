from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_alert_config_api_alerts_configs_post_response_create_alert_config_api_alerts_configs_post import (
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost,
)
from ...models.create_alert_config_request import CreateAlertConfigRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateAlertConfigRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alerts/configs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost
    | HTTPValidationError
    | None
):
    if response.status_code == 201:
        response_201 = CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost.from_dict(
            response.json()
        )

        return response_201

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
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost
    | HTTPValidationError
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
    body: CreateAlertConfigRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost
    | HTTPValidationError
]:
    """Create alert config

     Create a new alert configuration.

    Agent alert types: run_failed, consecutive_failures, error_rate_spike, run_burst, slow_run,
    credits_low_threshold, credits_runout_prediction, credits_usage_spike, non_manual_eval_failed,
    non_manual_eval_flagged, governance_flagged, governance_blocked, model_newer_available,
    model_deprecated, model_sunset.
    Source alert types: pull_failed, consecutive_pull_failures, pull_error_rate_spike.

    Distribution types: owner, owner_admins, selected_members. Organization accounts are normalized to
    owner_admins.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (CreateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAlertConfigRequest,
    x_account_id: str | Unset = UNSET,
) -> (
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost
    | HTTPValidationError
    | None
):
    """Create alert config

     Create a new alert configuration.

    Agent alert types: run_failed, consecutive_failures, error_rate_spike, run_burst, slow_run,
    credits_low_threshold, credits_runout_prediction, credits_usage_spike, non_manual_eval_failed,
    non_manual_eval_flagged, governance_flagged, governance_blocked, model_newer_available,
    model_deprecated, model_sunset.
    Source alert types: pull_failed, consecutive_pull_failures, pull_error_rate_spike.

    Distribution types: owner, owner_admins, selected_members. Organization accounts are normalized to
    owner_admins.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (CreateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAlertConfigRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost
    | HTTPValidationError
]:
    """Create alert config

     Create a new alert configuration.

    Agent alert types: run_failed, consecutive_failures, error_rate_spike, run_burst, slow_run,
    credits_low_threshold, credits_runout_prediction, credits_usage_spike, non_manual_eval_failed,
    non_manual_eval_flagged, governance_flagged, governance_blocked, model_newer_available,
    model_deprecated, model_sunset.
    Source alert types: pull_failed, consecutive_pull_failures, pull_error_rate_spike.

    Distribution types: owner, owner_admins, selected_members. Organization accounts are normalized to
    owner_admins.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (CreateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAlertConfigRequest,
    x_account_id: str | Unset = UNSET,
) -> (
    CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost
    | HTTPValidationError
    | None
):
    """Create alert config

     Create a new alert configuration.

    Agent alert types: run_failed, consecutive_failures, error_rate_spike, run_burst, slow_run,
    credits_low_threshold, credits_runout_prediction, credits_usage_spike, non_manual_eval_failed,
    non_manual_eval_flagged, governance_flagged, governance_blocked, model_newer_available,
    model_deprecated, model_sunset.
    Source alert types: pull_failed, consecutive_pull_failures, pull_error_rate_spike.

    Distribution types: owner, owner_admins, selected_members. Organization accounts are normalized to
    owner_admins.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (str | Unset):
        body (CreateAlertConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAlertConfigApiAlertsConfigsPostResponseCreateAlertConfigApiAlertsConfigsPost | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
