from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_detail_response import ContentDetailResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_connection_content_version: str,
    *,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contents/{source_connection_content_version}".format(
            source_connection_content_version=quote(
                str(source_connection_content_version), safe=""
            ),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContentDetailResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContentDetailResponse.from_dict(response.json())

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
) -> Response[ContentDetailResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: str | Unset = UNSET,
) -> Response[ContentDetailResponse | HTTPValidationError]:
    """Get content details

     Get detailed information about a specific content item (a `SourceConnectionContentVersion`).

    This is useful when you want to:
    - Inspect the extracted text for debugging or review.
    - Display content details in a UI.

    Text range:
    - `start` and `end` control the character range returned in `text_content` so clients can page
    through large documents.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access content belonging to your
    account.

    Args:
        source_connection_content_version (str):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentDetailResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        start=start,
        end=end,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: str | Unset = UNSET,
) -> ContentDetailResponse | HTTPValidationError | None:
    """Get content details

     Get detailed information about a specific content item (a `SourceConnectionContentVersion`).

    This is useful when you want to:
    - Inspect the extracted text for debugging or review.
    - Display content details in a UI.

    Text range:
    - `start` and `end` control the character range returned in `text_content` so clients can page
    through large documents.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access content belonging to your
    account.

    Args:
        source_connection_content_version (str):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentDetailResponse | HTTPValidationError
    """

    return sync_detailed(
        source_connection_content_version=source_connection_content_version,
        client=client,
        start=start,
        end=end,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: str | Unset = UNSET,
) -> Response[ContentDetailResponse | HTTPValidationError]:
    """Get content details

     Get detailed information about a specific content item (a `SourceConnectionContentVersion`).

    This is useful when you want to:
    - Inspect the extracted text for debugging or review.
    - Display content details in a UI.

    Text range:
    - `start` and `end` control the character range returned in `text_content` so clients can page
    through large documents.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access content belonging to your
    account.

    Args:
        source_connection_content_version (str):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentDetailResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_connection_content_version=source_connection_content_version,
        start=start,
        end=end,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_connection_content_version: str,
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 0,
    end: int | Unset = 5000,
    x_account_id: str | Unset = UNSET,
) -> ContentDetailResponse | HTTPValidationError | None:
    """Get content details

     Get detailed information about a specific content item (a `SourceConnectionContentVersion`).

    This is useful when you want to:
    - Inspect the extracted text for debugging or review.
    - Display content details in a UI.

    Text range:
    - `start` and `end` control the character range returned in `text_content` so clients can page
    through large documents.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only access content belonging to your
    account.

    Args:
        source_connection_content_version (str):
        start (int | Unset):  Default: 0.
        end (int | Unset):  Default: 5000.
        x_account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentDetailResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_connection_content_version=source_connection_content_version,
            client=client,
            start=start,
            end=end,
            x_account_id=x_account_id,
        )
    ).parsed
