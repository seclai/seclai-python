import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compatible_run_list_response import CompatibleRunListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    criteria_id: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    started_after: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_started_after: None | str | Unset
    if isinstance(started_after, Unset):
        json_started_after = UNSET
    elif isinstance(started_after, datetime.datetime):
        json_started_after = started_after.isoformat()
    else:
        json_started_after = started_after
    params["started_after"] = json_started_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/evaluation-criteria/{criteria_id}/compatible-runs".format(
            criteria_id=quote(str(criteria_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompatibleRunListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CompatibleRunListResponse.from_dict(response.json())

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
) -> Response[CompatibleRunListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    started_after: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[CompatibleRunListResponse | HTTPValidationError]:
    """List Compatible Runs

     List agent runs that have a completed step matching the criteria's target step.

    Returns runs whose step output can be used for testing or replaying the
    evaluation criteria.  Results are ordered newest-first and paginated.

    Args:
        criteria_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        started_after (datetime.datetime | None | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompatibleRunListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        criteria_id=criteria_id,
        page=page,
        limit=limit,
        started_after=started_after,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    started_after: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> CompatibleRunListResponse | HTTPValidationError | None:
    """List Compatible Runs

     List agent runs that have a completed step matching the criteria's target step.

    Returns runs whose step output can be used for testing or replaying the
    evaluation criteria.  Results are ordered newest-first and paginated.

    Args:
        criteria_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        started_after (datetime.datetime | None | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompatibleRunListResponse | HTTPValidationError
    """

    return sync_detailed(
        criteria_id=criteria_id,
        client=client,
        page=page,
        limit=limit,
        started_after=started_after,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    started_after: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[CompatibleRunListResponse | HTTPValidationError]:
    """List Compatible Runs

     List agent runs that have a completed step matching the criteria's target step.

    Returns runs whose step output can be used for testing or replaying the
    evaluation criteria.  Results are ordered newest-first and paginated.

    Args:
        criteria_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        started_after (datetime.datetime | None | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompatibleRunListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        criteria_id=criteria_id,
        page=page,
        limit=limit,
        started_after=started_after,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    started_after: datetime.datetime | None | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> CompatibleRunListResponse | HTTPValidationError | None:
    """List Compatible Runs

     List agent runs that have a completed step matching the criteria's target step.

    Returns runs whose step output can be used for testing or replaying the
    evaluation criteria.  Results are ordered newest-first and paginated.

    Args:
        criteria_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        started_after (datetime.datetime | None | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompatibleRunListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            criteria_id=criteria_id,
            client=client,
            page=page,
            limit=limit,
            started_after=started_after,
            x_account_id=x_account_id,
        )
    ).parsed
