from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    limit: int | Unset = 10,
    entity_type: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    json_entity_type: None | str | Unset
    if isinstance(entity_type, Unset):
        json_entity_type = UNSET
    else:
        json_entity_type = entity_type
    params["entity_type"] = json_entity_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
    entity_type: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | SearchResponse]:
    """Search resources

     Search across all resource types in your account.  Accepts a free-text keyword query or a UUID.
    UUIDs are matched exactly; keywords are matched by name and description (case-insensitive
    substring).  Results are ranked: name-prefix > name-substring > description-substring.  Searchable
    types: agent, knowledge_base, source_connection, solution, memory_bank, alert, api_key,
    governance_policy, mcp_client.

    Args:
        q (str): Search query
        limit (int | Unset): Maximum results Default: 10.
        entity_type (None | str | Unset): Optional entity type filter (e.g. 'agent',
            'knowledge_base')
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SearchResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        entity_type=entity_type,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
    entity_type: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | SearchResponse | None:
    """Search resources

     Search across all resource types in your account.  Accepts a free-text keyword query or a UUID.
    UUIDs are matched exactly; keywords are matched by name and description (case-insensitive
    substring).  Results are ranked: name-prefix > name-substring > description-substring.  Searchable
    types: agent, knowledge_base, source_connection, solution, memory_bank, alert, api_key,
    governance_policy, mcp_client.

    Args:
        q (str): Search query
        limit (int | Unset): Maximum results Default: 10.
        entity_type (None | str | Unset): Optional entity type filter (e.g. 'agent',
            'knowledge_base')
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SearchResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
        entity_type=entity_type,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
    entity_type: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | SearchResponse]:
    """Search resources

     Search across all resource types in your account.  Accepts a free-text keyword query or a UUID.
    UUIDs are matched exactly; keywords are matched by name and description (case-insensitive
    substring).  Results are ranked: name-prefix > name-substring > description-substring.  Searchable
    types: agent, knowledge_base, source_connection, solution, memory_bank, alert, api_key,
    governance_policy, mcp_client.

    Args:
        q (str): Search query
        limit (int | Unset): Maximum results Default: 10.
        entity_type (None | str | Unset): Optional entity type filter (e.g. 'agent',
            'knowledge_base')
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SearchResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        entity_type=entity_type,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
    entity_type: None | str | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | SearchResponse | None:
    """Search resources

     Search across all resource types in your account.  Accepts a free-text keyword query or a UUID.
    UUIDs are matched exactly; keywords are matched by name and description (case-insensitive
    substring).  Results are ranked: name-prefix > name-substring > description-substring.  Searchable
    types: agent, knowledge_base, source_connection, solution, memory_bank, alert, api_key,
    governance_policy, mcp_client.

    Args:
        q (str): Search query
        limit (int | Unset): Maximum results Default: 10.
        entity_type (None | str | Unset): Optional entity type filter (e.g. 'agent',
            'knowledge_base')
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
            entity_type=entity_type,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
