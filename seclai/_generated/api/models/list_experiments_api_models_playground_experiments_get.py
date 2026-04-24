import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_experiments_api_models_playground_experiments_get_response_list_experiments_api_models_playground_experiments_get import (
    ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["days"] = days

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.date):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.date):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/playground/experiments",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
    | None
):
    if response.status_code == 200:
        response_200 = ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet.from_dict(
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
    | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
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
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
]:
    """List Experiments

     List model playground experiments for the account.

    Returns a paginated, time-filtered list of experiments ordered by creation date descending.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Experiments are scoped to the caller's account.

    Args:
        days (int | Unset): Look-back window in days. Default: 30.
        start_date (datetime.date | None | Unset): Explicit start date (overrides days).
        end_date (datetime.date | None | Unset): Explicit end date (overrides days).
        limit (int | Unset): Page size. Default: 20.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet]
    """

    kwargs = _get_kwargs(
        days=days,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
    | None
):
    """List Experiments

     List model playground experiments for the account.

    Returns a paginated, time-filtered list of experiments ordered by creation date descending.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Experiments are scoped to the caller's account.

    Args:
        days (int | Unset): Look-back window in days. Default: 30.
        start_date (datetime.date | None | Unset): Explicit start date (overrides days).
        end_date (datetime.date | None | Unset): Explicit end date (overrides days).
        limit (int | Unset): Page size. Default: 20.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
    """

    return sync_detailed(
        client=client,
        days=days,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
]:
    """List Experiments

     List model playground experiments for the account.

    Returns a paginated, time-filtered list of experiments ordered by creation date descending.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Experiments are scoped to the caller's account.

    Args:
        days (int | Unset): Look-back window in days. Default: 30.
        start_date (datetime.date | None | Unset): Explicit start date (overrides days).
        end_date (datetime.date | None | Unset): Explicit end date (overrides days).
        limit (int | Unset): Page size. Default: 20.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet]
    """

    kwargs = _get_kwargs(
        days=days,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
    | None
):
    """List Experiments

     List model playground experiments for the account.

    Returns a paginated, time-filtered list of experiments ordered by creation date descending.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Experiments are scoped to the caller's account.

    Args:
        days (int | Unset): Look-back window in days. Default: 30.
        start_date (datetime.date | None | Unset): Explicit start date (overrides days).
        end_date (datetime.date | None | Unset): Explicit end date (overrides days).
        limit (int | Unset): Page size. Default: 20.
        offset (int | Unset): Pagination offset. Default: 0.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListExperimentsApiModelsPlaygroundExperimentsGetResponseListExperimentsApiModelsPlaygroundExperimentsGet
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            offset=offset,
            x_account_id=x_account_id,
        )
    ).parsed
