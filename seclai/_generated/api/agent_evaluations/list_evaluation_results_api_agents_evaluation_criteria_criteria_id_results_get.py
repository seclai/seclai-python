from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluation_result_list_response import EvaluationResultListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    criteria_id: str,
    *,
    status: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params["flagged_only"] = flagged_only

    json_time_from: None | str | Unset
    if isinstance(time_from, Unset):
        json_time_from = UNSET
    else:
        json_time_from = time_from
    params["time_from"] = json_time_from

    json_time_to: None | str | Unset
    if isinstance(time_to, Unset):
        json_time_to = UNSET
    else:
        json_time_to = time_to
    params["time_to"] = json_time_to

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/evaluation-criteria/{criteria_id}/results".format(
            criteria_id=quote(str(criteria_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EvaluationResultListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EvaluationResultListResponse.from_dict(response.json())

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
) -> Response[EvaluationResultListResponse | HTTPValidationError]:
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
    status: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> Response[EvaluationResultListResponse | HTTPValidationError]:
    """List Evaluation Results

     List evaluation results for a criteria with optional filtering.

    Supports filtering by status (pending, passed, failed, skipped, error),
    flagged-only mode, and an optional time range.  Results are paginated
    with configurable page size.

    Args:
        criteria_id (str):
        status (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationResultListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        criteria_id=criteria_id,
        status=status,
        flagged_only=flagged_only,
        time_from=time_from,
        time_to=time_to,
        page=page,
        limit=limit,
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
    status: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> EvaluationResultListResponse | HTTPValidationError | None:
    """List Evaluation Results

     List evaluation results for a criteria with optional filtering.

    Supports filtering by status (pending, passed, failed, skipped, error),
    flagged-only mode, and an optional time range.  Results are paginated
    with configurable page size.

    Args:
        criteria_id (str):
        status (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationResultListResponse | HTTPValidationError
    """

    return sync_detailed(
        criteria_id=criteria_id,
        client=client,
        status=status,
        flagged_only=flagged_only,
        time_from=time_from,
        time_to=time_to,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> Response[EvaluationResultListResponse | HTTPValidationError]:
    """List Evaluation Results

     List evaluation results for a criteria with optional filtering.

    Supports filtering by status (pending, passed, failed, skipped, error),
    flagged-only mode, and an optional time range.  Results are paginated
    with configurable page size.

    Args:
        criteria_id (str):
        status (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluationResultListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        criteria_id=criteria_id,
        status=status,
        flagged_only=flagged_only,
        time_from=time_from,
        time_to=time_to,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    criteria_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    flagged_only: bool | Unset = False,
    time_from: None | str | Unset = UNSET,
    time_to: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
) -> EvaluationResultListResponse | HTTPValidationError | None:
    """List Evaluation Results

     List evaluation results for a criteria with optional filtering.

    Supports filtering by status (pending, passed, failed, skipped, error),
    flagged-only mode, and an optional time range.  Results are paginated
    with configurable page size.

    Args:
        criteria_id (str):
        status (None | str | Unset):
        flagged_only (bool | Unset):  Default: False.
        time_from (None | str | Unset):
        time_to (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluationResultListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            criteria_id=criteria_id,
            client=client,
            status=status,
            flagged_only=flagged_only,
            time_from=time_from,
            time_to=time_to,
            page=page,
            limit=limit,
            x_account_id=x_account_id,
        )
    ).parsed
