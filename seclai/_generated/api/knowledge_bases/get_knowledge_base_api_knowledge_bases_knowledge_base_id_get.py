from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_base import KnowledgeBase
from ...types import UNSET, Response, Unset


def _get_kwargs(
    knowledge_base_id: str,
    *,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/knowledge_bases/{knowledge_base_id}".format(
            knowledge_base_id=quote(str(knowledge_base_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | KnowledgeBase | None:
    if response.status_code == 200:
        response_200 = KnowledgeBase.from_dict(response.json())

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
) -> Response[HTTPValidationError | KnowledgeBase]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_base_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | KnowledgeBase]:
    """Get Knowledge Base

     Fetch a knowledge base by ID.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access knowledge bases belonging
    to your account.

    Args:
        knowledge_base_id (str):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeBase]
    """

    kwargs = _get_kwargs(
        knowledge_base_id=knowledge_base_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_base_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | KnowledgeBase | None:
    """Get Knowledge Base

     Fetch a knowledge base by ID.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access knowledge bases belonging
    to your account.

    Args:
        knowledge_base_id (str):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeBase
    """

    return sync_detailed(
        knowledge_base_id=knowledge_base_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    knowledge_base_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> Response[HTTPValidationError | KnowledgeBase]:
    """Get Knowledge Base

     Fetch a knowledge base by ID.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access knowledge bases belonging
    to your account.

    Args:
        knowledge_base_id (str):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeBase]
    """

    kwargs = _get_kwargs(
        knowledge_base_id=knowledge_base_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_base_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: str | Unset = UNSET,
) -> HTTPValidationError | KnowledgeBase | None:
    """Get Knowledge Base

     Fetch a knowledge base by ID.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access knowledge bases belonging
    to your account.

    Args:
        knowledge_base_id (str):
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeBase
    """

    return (
        await asyncio_detailed(
            knowledge_base_id=knowledge_base_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
