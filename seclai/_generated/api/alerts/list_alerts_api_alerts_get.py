import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_alerts_api_alerts_get_response_list_alerts_api_alerts_get import (
    ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    time_from: datetime.datetime | None | Unset = UNSET,
    time_to: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

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

    json_time_from: None | str | Unset
    if isinstance(time_from, Unset):
        json_time_from = UNSET
    elif isinstance(time_from, datetime.datetime):
        json_time_from = time_from.isoformat()
    else:
        json_time_from = time_from
    params["time_from"] = json_time_from

    json_time_to: None | str | Unset
    if isinstance(time_to, Unset):
        json_time_to = UNSET
    elif isinstance(time_to, datetime.datetime):
        json_time_to = time_to.isoformat()
    else:
        json_time_to = time_to
    params["time_to"] = json_time_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet | None:
    if response.status_code == 200:
        response_200 = ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet.from_dict(
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
    HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet
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
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    time_from: datetime.datetime | None | Unset = UNSET,
    time_to: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet
]:
    """List alerts

     List alerts for the account with optional filters.

    Filters:
    - `status`: triggered, acknowledged, resolved, dismissed
    - `agent_id`: filter by agent
    - `source_connection_id`: filter by source
    - `time_from` / `time_to`: ISO 8601 date range

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        status (None | str | Unset): Filter by alert status
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        time_from (datetime.datetime | None | Unset): From (ISO 8601)
        time_to (datetime.datetime | None | Unset): To (ISO 8601)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        status=status,
        agent_id=agent_id,
        source_connection_id=source_connection_id,
        time_from=time_from,
        time_to=time_to,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    time_from: datetime.datetime | None | Unset = UNSET,
    time_to: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet | None:
    """List alerts

     List alerts for the account with optional filters.

    Filters:
    - `status`: triggered, acknowledged, resolved, dismissed
    - `agent_id`: filter by agent
    - `source_connection_id`: filter by source
    - `time_from` / `time_to`: ISO 8601 date range

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        status (None | str | Unset): Filter by alert status
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        time_from (datetime.datetime | None | Unset): From (ISO 8601)
        time_to (datetime.datetime | None | Unset): To (ISO 8601)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        status=status,
        agent_id=agent_id,
        source_connection_id=source_connection_id,
        time_from=time_from,
        time_to=time_to,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    time_from: datetime.datetime | None | Unset = UNSET,
    time_to: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet
]:
    """List alerts

     List alerts for the account with optional filters.

    Filters:
    - `status`: triggered, acknowledged, resolved, dismissed
    - `agent_id`: filter by agent
    - `source_connection_id`: filter by source
    - `time_from` / `time_to`: ISO 8601 date range

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        status (None | str | Unset): Filter by alert status
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        time_from (datetime.datetime | None | Unset): From (ISO 8601)
        time_to (datetime.datetime | None | Unset): To (ISO 8601)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        status=status,
        agent_id=agent_id,
        source_connection_id=source_connection_id,
        time_from=time_from,
        time_to=time_to,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    source_connection_id: None | str | Unset = UNSET,
    time_from: datetime.datetime | None | Unset = UNSET,
    time_to: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet | None:
    """List alerts

     List alerts for the account with optional filters.

    Filters:
    - `status`: triggered, acknowledged, resolved, dismissed
    - `agent_id`: filter by agent
    - `source_connection_id`: filter by source
    - `time_from` / `time_to`: ISO 8601 date range

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Results are scoped to the caller's account.

    Args:
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        status (None | str | Unset): Filter by alert status
        agent_id (None | str | Unset): Filter by agent ID
        source_connection_id (None | str | Unset): Filter by source connection ID
        time_from (datetime.datetime | None | Unset): From (ISO 8601)
        time_to (datetime.datetime | None | Unset): To (ISO 8601)
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListAlertsApiAlertsGetResponseListAlertsApiAlertsGet
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            status=status,
            agent_id=agent_id,
            source_connection_id=source_connection_id,
            time_from=time_from,
            time_to=time_to,
            x_account_id=x_account_id,
        )
    ).parsed
