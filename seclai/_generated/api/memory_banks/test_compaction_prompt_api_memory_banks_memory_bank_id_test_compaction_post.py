from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compaction_test_response_model import CompactionTestResponseModel
from ...models.http_validation_error import HTTPValidationError
from ...models.test_compaction_request import TestCompactionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    memory_bank_id: str,
    *,
    body: TestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/memory_banks/{memory_bank_id}/test-compaction".format(
            memory_bank_id=quote(str(memory_bank_id), safe=""),
        ),
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
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[CompactionTestResponseModel | HTTPValidationError]:
    """Test Compaction Prompt

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (TestCompactionRequest): Request body for testing a compaction prompt against an
            existing bank.

            The user may supply a ``compaction_prompt`` to override (or provide when
            the bank has none).  Content can come from three sources:

            1. Existing entries in the bank (default when neither field is set).
            2. ``sample_entries`` – caller-provided list of strings.
            3. ``generate_direction`` – an instruction to the LLM to generate sample
               memory entries.  Useful for trying a prompt before any real data
               exists.

            At most one of ``sample_entries`` / ``generate_direction`` may be given.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompactionTestResponseModel | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> CompactionTestResponseModel | HTTPValidationError | None:
    """Test Compaction Prompt

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (TestCompactionRequest): Request body for testing a compaction prompt against an
            existing bank.

            The user may supply a ``compaction_prompt`` to override (or provide when
            the bank has none).  Content can come from three sources:

            1. Existing entries in the bank (default when neither field is set).
            2. ``sample_entries`` – caller-provided list of strings.
            3. ``generate_direction`` – an instruction to the LLM to generate sample
               memory entries.  Useful for trying a prompt before any real data
               exists.

            At most one of ``sample_entries`` / ``generate_direction`` may be given.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompactionTestResponseModel | HTTPValidationError
    """

    return sync_detailed(
        memory_bank_id=memory_bank_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[CompactionTestResponseModel | HTTPValidationError]:
    """Test Compaction Prompt

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (TestCompactionRequest): Request body for testing a compaction prompt against an
            existing bank.

            The user may supply a ``compaction_prompt`` to override (or provide when
            the bank has none).  Content can come from three sources:

            1. Existing entries in the bank (default when neither field is set).
            2. ``sample_entries`` – caller-provided list of strings.
            3. ``generate_direction`` – an instruction to the LLM to generate sample
               memory entries.  Useful for trying a prompt before any real data
               exists.

            At most one of ``sample_entries`` / ``generate_direction`` may be given.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompactionTestResponseModel | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        body=body,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestCompactionRequest,
    x_account_id: str | Unset = UNSET,
) -> CompactionTestResponseModel | HTTPValidationError | None:
    """Test Compaction Prompt

     Test a compaction prompt by running the summarizer and evaluating the result with an LLM-as-judge.
    Returns original entries, compaction summary, surviving entries, and a structured quality evaluation
    with verdict, score, and reasoning.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (TestCompactionRequest): Request body for testing a compaction prompt against an
            existing bank.

            The user may supply a ``compaction_prompt`` to override (or provide when
            the bank has none).  Content can come from three sources:

            1. Existing entries in the bank (default when neither field is set).
            2. ``sample_entries`` – caller-provided list of strings.
            3. ``generate_direction`` – an instruction to the LLM to generate sample
               memory entries.  Useful for trying a prompt before any real data
               exists.

            At most one of ``sample_entries`` / ``generate_direction`` may be given.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompactionTestResponseModel | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            memory_bank_id=memory_bank_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
