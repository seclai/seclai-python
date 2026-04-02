from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.non_manual_evaluation_summary_response import (
    NonManualEvaluationSummaryResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 30,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["days"] = days

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/evaluation-results/non-manual-summary",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | NonManualEvaluationSummaryResponse | None:
    if response.status_code == 200:
        response_200 = NonManualEvaluationSummaryResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | NonManualEvaluationSummaryResponse]:
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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | NonManualEvaluationSummaryResponse]:
    """Get Non Manual Evaluation Summary

     Get account-level evaluation summary for API key clients.

    Returns aggregated pass/fail/flagged counts and pass rates for each evaluation mode (eval_and_retry,
    sample_and_flag).

    Args:
        days (int | Unset):  Default: 30.
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NonManualEvaluationSummaryResponse]
    """

    kwargs = _get_kwargs(
        days=days,
        start_date=start_date,
        end_date=end_date,
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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | NonManualEvaluationSummaryResponse | None:
    """Get Non Manual Evaluation Summary

     Get account-level evaluation summary for API key clients.

    Returns aggregated pass/fail/flagged counts and pass rates for each evaluation mode (eval_and_retry,
    sample_and_flag).

    Args:
        days (int | Unset):  Default: 30.
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NonManualEvaluationSummaryResponse
    """

    return sync_detailed(
        client=client,
        days=days,
        start_date=start_date,
        end_date=end_date,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | NonManualEvaluationSummaryResponse]:
    """Get Non Manual Evaluation Summary

     Get account-level evaluation summary for API key clients.

    Returns aggregated pass/fail/flagged counts and pass rates for each evaluation mode (eval_and_retry,
    sample_and_flag).

    Args:
        days (int | Unset):  Default: 30.
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NonManualEvaluationSummaryResponse]
    """

    kwargs = _get_kwargs(
        days=days,
        start_date=start_date,
        end_date=end_date,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | NonManualEvaluationSummaryResponse | None:
    """Get Non Manual Evaluation Summary

     Get account-level evaluation summary for API key clients.

    Returns aggregated pass/fail/flagged counts and pass rates for each evaluation mode (eval_and_retry,
    sample_and_flag).

    Args:
        days (int | Unset):  Default: 30.
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NonManualEvaluationSummaryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            start_date=start_date,
            end_date=end_date,
            x_account_id=x_account_id,
        )
    ).parsed
