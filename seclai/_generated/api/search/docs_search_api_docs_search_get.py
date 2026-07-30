from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.docs_search_api_docs_search_get_mode import (
    DocsSearchApiDocsSearchGetMode,
)
from ...models.docs_search_response import DocsSearchResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    mode: (
        DocsSearchApiDocsSearchGetMode | Unset
    ) = DocsSearchApiDocsSearchGetMode.KEYWORD,
    limit: int | Unset = 8,
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

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/docs-search",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocsSearchResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DocsSearchResponse.from_dict(response.json())

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
) -> Response[DocsSearchResponse | HTTPValidationError]:
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
    mode: (
        DocsSearchApiDocsSearchGetMode | Unset
    ) = DocsSearchApiDocsSearchGetMode.KEYWORD,
    limit: int | Unset = 8,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[DocsSearchResponse | HTTPValidationError]:
    """Search documentation

     Search the Seclai documentation by content and return matching pages. `mode=keyword` matches page
    titles and summaries (fast, no AI cost); `mode=semantic` matches page body content by meaning (uses
    an embedding). Each result carries a `doc_slug` and an optional section `anchor` for building a
    `https://seclai.com/docs/<doc_slug>[#<anchor>]` link, a `score` (relevance; not comparable across
    modes), and — in semantic mode — a `highlight` (best matching verbatim sentence; `null` for
    keyword). Documentation is global, so results are not account-scoped.

    Args:
        q (str): Search query
        mode (DocsSearchApiDocsSearchGetMode | Unset): Search strategy Default:
            DocsSearchApiDocsSearchGetMode.KEYWORD.
        limit (int | Unset): Maximum results Default: 8.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocsSearchResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        q=q,
        mode=mode,
        limit=limit,
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
    mode: (
        DocsSearchApiDocsSearchGetMode | Unset
    ) = DocsSearchApiDocsSearchGetMode.KEYWORD,
    limit: int | Unset = 8,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> DocsSearchResponse | HTTPValidationError | None:
    """Search documentation

     Search the Seclai documentation by content and return matching pages. `mode=keyword` matches page
    titles and summaries (fast, no AI cost); `mode=semantic` matches page body content by meaning (uses
    an embedding). Each result carries a `doc_slug` and an optional section `anchor` for building a
    `https://seclai.com/docs/<doc_slug>[#<anchor>]` link, a `score` (relevance; not comparable across
    modes), and — in semantic mode — a `highlight` (best matching verbatim sentence; `null` for
    keyword). Documentation is global, so results are not account-scoped.

    Args:
        q (str): Search query
        mode (DocsSearchApiDocsSearchGetMode | Unset): Search strategy Default:
            DocsSearchApiDocsSearchGetMode.KEYWORD.
        limit (int | Unset): Maximum results Default: 8.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocsSearchResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        q=q,
        mode=mode,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    mode: (
        DocsSearchApiDocsSearchGetMode | Unset
    ) = DocsSearchApiDocsSearchGetMode.KEYWORD,
    limit: int | Unset = 8,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[DocsSearchResponse | HTTPValidationError]:
    """Search documentation

     Search the Seclai documentation by content and return matching pages. `mode=keyword` matches page
    titles and summaries (fast, no AI cost); `mode=semantic` matches page body content by meaning (uses
    an embedding). Each result carries a `doc_slug` and an optional section `anchor` for building a
    `https://seclai.com/docs/<doc_slug>[#<anchor>]` link, a `score` (relevance; not comparable across
    modes), and — in semantic mode — a `highlight` (best matching verbatim sentence; `null` for
    keyword). Documentation is global, so results are not account-scoped.

    Args:
        q (str): Search query
        mode (DocsSearchApiDocsSearchGetMode | Unset): Search strategy Default:
            DocsSearchApiDocsSearchGetMode.KEYWORD.
        limit (int | Unset): Maximum results Default: 8.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocsSearchResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        q=q,
        mode=mode,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    mode: (
        DocsSearchApiDocsSearchGetMode | Unset
    ) = DocsSearchApiDocsSearchGetMode.KEYWORD,
    limit: int | Unset = 8,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> DocsSearchResponse | HTTPValidationError | None:
    """Search documentation

     Search the Seclai documentation by content and return matching pages. `mode=keyword` matches page
    titles and summaries (fast, no AI cost); `mode=semantic` matches page body content by meaning (uses
    an embedding). Each result carries a `doc_slug` and an optional section `anchor` for building a
    `https://seclai.com/docs/<doc_slug>[#<anchor>]` link, a `score` (relevance; not comparable across
    modes), and — in semantic mode — a `highlight` (best matching verbatim sentence; `null` for
    keyword). Documentation is global, so results are not account-scoped.

    Args:
        q (str): Search query
        mode (DocsSearchApiDocsSearchGetMode | Unset): Search strategy Default:
            DocsSearchApiDocsSearchGetMode.KEYWORD.
        limit (int | Unset): Maximum results Default: 8.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocsSearchResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            mode=mode,
            limit=limit,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
