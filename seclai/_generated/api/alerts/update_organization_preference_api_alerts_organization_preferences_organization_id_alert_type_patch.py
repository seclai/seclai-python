from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.organization_alert_preference_response import (
    OrganizationAlertPreferenceResponse,
)
from ...models.update_organization_alert_preference_request import (
    UpdateOrganizationAlertPreferenceRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    alert_type: str,
    *,
    body: UpdateOrganizationAlertPreferenceRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/alerts/organization-preferences/{organization_id}/{alert_type}".format(
            organization_id=quote(str(organization_id), safe=""),
            alert_type=quote(str(alert_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OrganizationAlertPreferenceResponse | None:
    if response.status_code == 200:
        response_200 = OrganizationAlertPreferenceResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | OrganizationAlertPreferenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    alert_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrganizationAlertPreferenceRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | OrganizationAlertPreferenceResponse]:
    """Update organization alert delivery preference

     Update the authenticated user's personal delivery preference for one alert type in one organization.

    Setting `subscribed=false` stores an explicit opt-out override. Setting `subscribed=true` removes
    the override and restores the default subscribed behavior.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only owners and administrators can update preferences for an organization.

    Args:
        organization_id (UUID):
        alert_type (str):
        x_account_id (UUID | Unset):
        body (UpdateOrganizationAlertPreferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OrganizationAlertPreferenceResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        alert_type=alert_type,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    alert_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrganizationAlertPreferenceRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | OrganizationAlertPreferenceResponse | None:
    """Update organization alert delivery preference

     Update the authenticated user's personal delivery preference for one alert type in one organization.

    Setting `subscribed=false` stores an explicit opt-out override. Setting `subscribed=true` removes
    the override and restores the default subscribed behavior.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only owners and administrators can update preferences for an organization.

    Args:
        organization_id (UUID):
        alert_type (str):
        x_account_id (UUID | Unset):
        body (UpdateOrganizationAlertPreferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OrganizationAlertPreferenceResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        alert_type=alert_type,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    alert_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrganizationAlertPreferenceRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | OrganizationAlertPreferenceResponse]:
    """Update organization alert delivery preference

     Update the authenticated user's personal delivery preference for one alert type in one organization.

    Setting `subscribed=false` stores an explicit opt-out override. Setting `subscribed=true` removes
    the override and restores the default subscribed behavior.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only owners and administrators can update preferences for an organization.

    Args:
        organization_id (UUID):
        alert_type (str):
        x_account_id (UUID | Unset):
        body (UpdateOrganizationAlertPreferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OrganizationAlertPreferenceResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        alert_type=alert_type,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    alert_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrganizationAlertPreferenceRequest,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | OrganizationAlertPreferenceResponse | None:
    """Update organization alert delivery preference

     Update the authenticated user's personal delivery preference for one alert type in one organization.

    Setting `subscribed=false` stores an explicit opt-out override. Setting `subscribed=true` removes
    the override and restores the default subscribed behavior.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only owners and administrators can update preferences for an organization.

    Args:
        organization_id (UUID):
        alert_type (str):
        x_account_id (UUID | Unset):
        body (UpdateOrganizationAlertPreferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OrganizationAlertPreferenceResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            alert_type=alert_type,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
