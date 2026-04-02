from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_templates_api_memory_banks_templates_get_response_200_item import (
    ListTemplatesApiMemoryBanksTemplatesGetResponse200Item,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memory_banks/templates",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                ListTemplatesApiMemoryBanksTemplatesGetResponse200Item.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]]:
    """List Templates

     Return pre-built template configurations for common memory bank use cases.

    Each template includes a name, description, suggested use case, and full default settings that can
    be used directly with the create endpoint.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item] | None:
    """List Templates

     Return pre-built template configurations for common memory bank use cases.

    Each template includes a name, description, suggested use case, and full default settings that can
    be used directly with the create endpoint.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]
    """

    return sync_detailed(
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]]:
    """List Templates

     Return pre-built template configurations for common memory bank use cases.

    Each template includes a name, description, suggested use case, and full default settings that can
    be used directly with the create endpoint.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item] | None:
    """List Templates

     Return pre-built template configurations for common memory bank use cases.

    Each template includes a name, description, suggested use case, and full default settings that can
    be used directly with the create endpoint.

    Args:
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListTemplatesApiMemoryBanksTemplatesGetResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
