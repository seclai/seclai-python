from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compaction_test_response_model import CompactionTestResponseModel
from ...models.http_validation_error import HTTPValidationError
from ...models.standalone_test_compaction_request import StandaloneTestCompactionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StandaloneTestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/memory_banks/test-compaction",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompactionTestResponseModel | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CompactionTestResponseModel.from_dict(response.json())

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
) -> Response[CompactionTestResponseModel | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StandaloneTestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[CompactionTestResponseModel | HTTPValidationError]:
    """Test Compaction Prompt Standalone

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        x_account_id (str | Unset):
        body (StandaloneTestCompactionRequest): Request body for testing a compaction prompt
            *without* an existing bank.

            Used on the create-memory-bank page where no bank ID exists yet.
            ``compaction_prompt`` is required (no bank to fall back to).
            Content must come from ``sample_entries`` or ``generate_direction``
            (no existing entries to fetch).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompactionTestResponseModel | HTTPValidationError]
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
    body: StandaloneTestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> CompactionTestResponseModel | HTTPValidationError | None:
    """Test Compaction Prompt Standalone

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        x_account_id (str | Unset):
        body (StandaloneTestCompactionRequest): Request body for testing a compaction prompt
            *without* an existing bank.

            Used on the create-memory-bank page where no bank ID exists yet.
            ``compaction_prompt`` is required (no bank to fall back to).
            Content must come from ``sample_entries`` or ``generate_direction``
            (no existing entries to fetch).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompactionTestResponseModel | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StandaloneTestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[CompactionTestResponseModel | HTTPValidationError]:
    """Test Compaction Prompt Standalone

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        x_account_id (str | Unset):
        body (StandaloneTestCompactionRequest): Request body for testing a compaction prompt
            *without* an existing bank.

            Used on the create-memory-bank page where no bank ID exists yet.
            ``compaction_prompt`` is required (no bank to fall back to).
            Content must come from ``sample_entries`` or ``generate_direction``
            (no existing entries to fetch).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompactionTestResponseModel | HTTPValidationError]
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
    body: StandaloneTestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> CompactionTestResponseModel | HTTPValidationError | None:
    """Test Compaction Prompt Standalone

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        x_account_id (str | Unset):
        body (StandaloneTestCompactionRequest): Request body for testing a compaction prompt
            *without* an existing bank.

            Used on the create-memory-bank page where no bank ID exists yet.
            ``compaction_prompt`` is required (no bank to fall back to).
            Content must come from ``sample_entries`` or ``generate_direction``
            (no existing entries to fetch).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompactionTestResponseModel | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
