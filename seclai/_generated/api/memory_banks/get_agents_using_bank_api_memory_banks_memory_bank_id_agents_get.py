from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_agents_using_bank_api_memory_banks_memory_bank_id_agents_get_response_200_item import (
    GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    memory_bank_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memory_banks/{memory_bank_id}/agents".format(
            memory_bank_id=quote(str(memory_bank_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
    | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
]:
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
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
]:
    """Get Agents Using Bank

     List agents whose current definition references this memory bank.

    Returns an array of `{agent_id, agent_name}` objects.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
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
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
    | None
):
    """Get Agents Using Bank

     List agents whose current definition references this memory bank.

    Returns an array of `{agent_id, agent_name}` objects.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
    """

    return sync_detailed(
        memory_bank_id=memory_bank_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
]:
    """Get Agents Using Bank

     List agents whose current definition references this memory bank.

    Returns an array of `{agent_id, agent_name}` objects.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        memory_bank_id=memory_bank_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    memory_bank_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> (
    HTTPValidationError
    | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
    | None
):
    """Get Agents Using Bank

     List agents whose current definition references this memory bank.

    Returns an array of `{agent_id, agent_name}` objects.

    Args:
        memory_bank_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[GetAgentsUsingBankApiMemoryBanksMemoryBankIdAgentsGetResponse200Item]
    """

    return (
        await asyncio_detailed(
            memory_bank_id=memory_bank_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
