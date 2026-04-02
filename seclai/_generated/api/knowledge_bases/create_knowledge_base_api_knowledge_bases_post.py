from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_knowledge_base_body import CreateKnowledgeBaseBody
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_base import KnowledgeBase
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateKnowledgeBaseBody,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/knowledge_bases",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | KnowledgeBase | None:
    if response.status_code == 201:
        response_201 = KnowledgeBase.from_dict(response.json())

        return response_201

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | KnowledgeBase]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeBaseBody,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | KnowledgeBase]:
    """Create Knowledge Base

     Create a new knowledge base.

    At least one `source_id` is required. The source connections must belong to the same account.

    Args:
        x_account_id (str | Unset):
        body (CreateKnowledgeBaseBody): Request body for creating a knowledge base.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeBase]
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
    body: CreateKnowledgeBaseBody,
    x_account_id: str | Unset = UNSET,
) -> Any | HTTPValidationError | KnowledgeBase | None:
    """Create Knowledge Base

     Create a new knowledge base.

    At least one `source_id` is required. The source connections must belong to the same account.

    Args:
        x_account_id (str | Unset):
        body (CreateKnowledgeBaseBody): Request body for creating a knowledge base.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeBase
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeBaseBody,
    x_account_id: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | KnowledgeBase]:
    """Create Knowledge Base

     Create a new knowledge base.

    At least one `source_id` is required. The source connections must belong to the same account.

    Args:
        x_account_id (str | Unset):
        body (CreateKnowledgeBaseBody): Request body for creating a knowledge base.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeBase]
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
    body: CreateKnowledgeBaseBody,
    x_account_id: str | Unset = UNSET,
) -> Any | HTTPValidationError | KnowledgeBase | None:
    """Create Knowledge Base

     Create a new knowledge base.

    At least one `source_id` is required. The source connections must belong to the same account.

    Args:
        x_account_id (str | Unset):
        body (CreateKnowledgeBaseBody): Request body for creating a knowledge base.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeBase
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
