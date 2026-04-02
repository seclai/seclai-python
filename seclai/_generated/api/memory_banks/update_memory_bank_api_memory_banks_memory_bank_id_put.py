from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_bank import MemoryBank
from ...models.update_memory_bank_body import UpdateMemoryBankBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    memory_bank_id: str,
    *,
    body: UpdateMemoryBankBody,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/memory_banks/{memory_bank_id}".format(
            memory_bank_id=quote(str(memory_bank_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MemoryBank | None:
    if response.status_code == 200:
        response_200 = MemoryBank.from_dict(response.json())

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
) -> Response[HTTPValidationError | MemoryBank]:
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
    body: UpdateMemoryBankBody,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBank]:
    """Update Memory Bank

     Update a memory bank's configuration. Only provided fields are changed; omitted fields are left
    unchanged.

    Note: the embedding `mode` cannot be changed after creation because it determines the vector
    dimensions used to store entries.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (UpdateMemoryBankBody): Request body for updating a memory bank.

            Omitted fields are left unchanged.  To **clear** a field back to null,
            send a zero-value sentinel: ``0`` for integers, ``""`` for strings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBank]
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
    body: UpdateMemoryBankBody,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | MemoryBank | None:
    """Update Memory Bank

     Update a memory bank's configuration. Only provided fields are changed; omitted fields are left
    unchanged.

    Note: the embedding `mode` cannot be changed after creation because it determines the vector
    dimensions used to store entries.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (UpdateMemoryBankBody): Request body for updating a memory bank.

            Omitted fields are left unchanged.  To **clear** a field back to null,
            send a zero-value sentinel: ``0`` for integers, ``""`` for strings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBank
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
    body: UpdateMemoryBankBody,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | MemoryBank]:
    """Update Memory Bank

     Update a memory bank's configuration. Only provided fields are changed; omitted fields are left
    unchanged.

    Note: the embedding `mode` cannot be changed after creation because it determines the vector
    dimensions used to store entries.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (UpdateMemoryBankBody): Request body for updating a memory bank.

            Omitted fields are left unchanged.  To **clear** a field back to null,
            send a zero-value sentinel: ``0`` for integers, ``""`` for strings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryBank]
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
    body: UpdateMemoryBankBody,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | MemoryBank | None:
    """Update Memory Bank

     Update a memory bank's configuration. Only provided fields are changed; omitted fields are left
    unchanged.

    Note: the embedding `mode` cannot be changed after creation because it determines the vector
    dimensions used to store entries.

    Args:
        memory_bank_id (str):
        x_account_id (str | Unset):
        body (UpdateMemoryBankBody): Request body for updating a memory bank.

            Omitted fields are left unchanged.  To **clear** a field back to null,
            send a zero-value sentinel: ``0`` for integers, ``""`` for strings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryBank
    """

    return (
        await asyncio_detailed(
            memory_bank_id=memory_bank_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
