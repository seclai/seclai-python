from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_version_response import ApiVersionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.update_api_version_request import UpdateApiVersionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UpdateApiVersionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/version",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiVersionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ApiVersionResponse.from_dict(response.json())

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
) -> Response[ApiVersionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiVersionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[ApiVersionResponse | HTTPValidationError]:
    """Pin (or clear) the account's API version

     Sets the account's sticky `Seclai-Version` to the given `YYYY-MM-DD` date, or clears it with `null`.
    The new pin applies to subsequent header-less requests; a `Seclai-Version` request header still
    overrides it. Owner/admin only. `effective_version` in the response reflects the current request,
    not the new pin.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateApiVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiVersionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiVersionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> ApiVersionResponse | HTTPValidationError | None:
    """Pin (or clear) the account's API version

     Sets the account's sticky `Seclai-Version` to the given `YYYY-MM-DD` date, or clears it with `null`.
    The new pin applies to subsequent header-less requests; a `Seclai-Version` request header still
    overrides it. Owner/admin only. `effective_version` in the response reflects the current request,
    not the new pin.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateApiVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiVersionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiVersionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[ApiVersionResponse | HTTPValidationError]:
    """Pin (or clear) the account's API version

     Sets the account's sticky `Seclai-Version` to the given `YYYY-MM-DD` date, or clears it with `null`.
    The new pin applies to subsequent header-less requests; a `Seclai-Version` request header still
    overrides it. Owner/admin only. `effective_version` in the response reflects the current request,
    not the new pin.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateApiVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiVersionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiVersionRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> ApiVersionResponse | HTTPValidationError | None:
    """Pin (or clear) the account's API version

     Sets the account's sticky `Seclai-Version` to the given `YYYY-MM-DD` date, or clears it with `null`.
    The new pin applies to subsequent header-less requests; a `Seclai-Version` request header still
    overrides it. Owner/admin only. `effective_version` in the response reflects the current request,
    not the new pin.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (UpdateApiVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiVersionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
