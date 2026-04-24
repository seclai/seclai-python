from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.organization_alert_preference_list_response import (
    OrganizationAlertPreferenceListResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: None | Unset | UUID = UNSET,
    include_defaults: bool | Unset = False,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_organization_id: None | str | Unset
    if isinstance(organization_id, Unset):
        json_organization_id = UNSET
    elif isinstance(organization_id, UUID):
        json_organization_id = str(organization_id)
    else:
        json_organization_id = organization_id
    params["organization_id"] = json_organization_id

    params["include_defaults"] = include_defaults

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/organization-preferences/list",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OrganizationAlertPreferenceListResponse | None:
    if response.status_code == 200:
        response_200 = OrganizationAlertPreferenceListResponse.from_dict(
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
) -> Response[HTTPValidationError | OrganizationAlertPreferenceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: None | Unset | UUID = UNSET,
    include_defaults: bool | Unset = False,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | OrganizationAlertPreferenceListResponse]:
    """List organization alert delivery preferences

     List per-organization alert delivery preferences for the authenticated user.

    By default, only explicit override rows are returned. Set `include_defaults=true` to return the
    effective subscribed state for every alert type in every organization the user can manage.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only organizations where the user is an owner or administrator are included.

    Args:
        organization_id (None | Unset | UUID): Optional organization filter
        include_defaults (bool | Unset): Include default subscribed entries for all alert types
            Default: False.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OrganizationAlertPreferenceListResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        include_defaults=include_defaults,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    organization_id: None | Unset | UUID = UNSET,
    include_defaults: bool | Unset = False,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | OrganizationAlertPreferenceListResponse | None:
    """List organization alert delivery preferences

     List per-organization alert delivery preferences for the authenticated user.

    By default, only explicit override rows are returned. Set `include_defaults=true` to return the
    effective subscribed state for every alert type in every organization the user can manage.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only organizations where the user is an owner or administrator are included.

    Args:
        organization_id (None | Unset | UUID): Optional organization filter
        include_defaults (bool | Unset): Include default subscribed entries for all alert types
            Default: False.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OrganizationAlertPreferenceListResponse
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        include_defaults=include_defaults,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: None | Unset | UUID = UNSET,
    include_defaults: bool | Unset = False,
    x_account_id: UUID | Unset = UNSET,
) -> Response[HTTPValidationError | OrganizationAlertPreferenceListResponse]:
    """List organization alert delivery preferences

     List per-organization alert delivery preferences for the authenticated user.

    By default, only explicit override rows are returned. Set `include_defaults=true` to return the
    effective subscribed state for every alert type in every organization the user can manage.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only organizations where the user is an owner or administrator are included.

    Args:
        organization_id (None | Unset | UUID): Optional organization filter
        include_defaults (bool | Unset): Include default subscribed entries for all alert types
            Default: False.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OrganizationAlertPreferenceListResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        include_defaults=include_defaults,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: None | Unset | UUID = UNSET,
    include_defaults: bool | Unset = False,
    x_account_id: UUID | Unset = UNSET,
) -> HTTPValidationError | OrganizationAlertPreferenceListResponse | None:
    """List organization alert delivery preferences

     List per-organization alert delivery preferences for the authenticated user.

    By default, only explicit override rows are returned. Set `include_defaults=true` to return the
    effective subscribed state for every alert type in every organization the user can manage.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - Only organizations where the user is an owner or administrator are included.

    Args:
        organization_id (None | Unset | UUID): Optional organization filter
        include_defaults (bool | Unset): Include default subscribed entries for all alert types
            Default: False.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OrganizationAlertPreferenceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            include_defaults=include_defaults,
            x_account_id=x_account_id,
        )
    ).parsed
