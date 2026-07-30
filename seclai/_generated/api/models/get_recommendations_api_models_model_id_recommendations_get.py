from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.model_recommendations_response import ModelRecommendationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_id: str,
    *,
    require_tool_use: bool | None | Unset = UNSET,
    require_structured_output: bool | None | Unset = UNSET,
    require_thinking: bool | None | Unset = UNSET,
    min_context_tokens: int | None | Unset = UNSET,
    min_output_tokens: int | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    json_require_tool_use: bool | None | Unset
    if isinstance(require_tool_use, Unset):
        json_require_tool_use = UNSET
    else:
        json_require_tool_use = require_tool_use
    params["require_tool_use"] = json_require_tool_use

    json_require_structured_output: bool | None | Unset
    if isinstance(require_structured_output, Unset):
        json_require_structured_output = UNSET
    else:
        json_require_structured_output = require_structured_output
    params["require_structured_output"] = json_require_structured_output

    json_require_thinking: bool | None | Unset
    if isinstance(require_thinking, Unset):
        json_require_thinking = UNSET
    else:
        json_require_thinking = require_thinking
    params["require_thinking"] = json_require_thinking

    json_min_context_tokens: int | None | Unset
    if isinstance(min_context_tokens, Unset):
        json_min_context_tokens = UNSET
    else:
        json_min_context_tokens = min_context_tokens
    params["min_context_tokens"] = json_min_context_tokens

    json_min_output_tokens: int | None | Unset
    if isinstance(min_output_tokens, Unset):
        json_min_output_tokens = UNSET
    else:
        json_min_output_tokens = min_output_tokens
    params["min_output_tokens"] = json_min_output_tokens

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/{model_id}/recommendations".format(
            model_id=quote(str(model_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ModelRecommendationsResponse | None:
    if response.status_code == 200:
        response_200 = ModelRecommendationsResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ModelRecommendationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    require_tool_use: bool | None | Unset = UNSET,
    require_structured_output: bool | None | Unset = UNSET,
    require_thinking: bool | None | Unset = UNSET,
    min_context_tokens: int | None | Unset = UNSET,
    min_output_tokens: int | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | ModelRecommendationsResponse]:
    """Get Recommendations

     Get replacement/upgrade recommendations for a model.

    Returns a designated successor (if any), same-family upgrades, and cross-provider/cross-family
    alternatives.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        require_tool_use (bool | None | Unset): Only recommend models that support tool use.
        require_structured_output (bool | None | Unset): Only recommend models that support
            structured output.
        require_thinking (bool | None | Unset): Only recommend models that support
            thinking/reasoning.
        min_context_tokens (int | None | Unset): Minimum context window size in tokens.
        min_output_tokens (int | None | Unset): Minimum output token limit.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ModelRecommendationsResponse]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        require_tool_use=require_tool_use,
        require_structured_output=require_structured_output,
        require_thinking=require_thinking,
        min_context_tokens=min_context_tokens,
        min_output_tokens=min_output_tokens,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    require_tool_use: bool | None | Unset = UNSET,
    require_structured_output: bool | None | Unset = UNSET,
    require_thinking: bool | None | Unset = UNSET,
    min_context_tokens: int | None | Unset = UNSET,
    min_output_tokens: int | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | ModelRecommendationsResponse | None:
    """Get Recommendations

     Get replacement/upgrade recommendations for a model.

    Returns a designated successor (if any), same-family upgrades, and cross-provider/cross-family
    alternatives.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        require_tool_use (bool | None | Unset): Only recommend models that support tool use.
        require_structured_output (bool | None | Unset): Only recommend models that support
            structured output.
        require_thinking (bool | None | Unset): Only recommend models that support
            thinking/reasoning.
        min_context_tokens (int | None | Unset): Minimum context window size in tokens.
        min_output_tokens (int | None | Unset): Minimum output token limit.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ModelRecommendationsResponse
    """

    return sync_detailed(
        model_id=model_id,
        client=client,
        require_tool_use=require_tool_use,
        require_structured_output=require_structured_output,
        require_thinking=require_thinking,
        min_context_tokens=min_context_tokens,
        min_output_tokens=min_output_tokens,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    require_tool_use: bool | None | Unset = UNSET,
    require_structured_output: bool | None | Unset = UNSET,
    require_thinking: bool | None | Unset = UNSET,
    min_context_tokens: int | None | Unset = UNSET,
    min_output_tokens: int | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | ModelRecommendationsResponse]:
    """Get Recommendations

     Get replacement/upgrade recommendations for a model.

    Returns a designated successor (if any), same-family upgrades, and cross-provider/cross-family
    alternatives.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        require_tool_use (bool | None | Unset): Only recommend models that support tool use.
        require_structured_output (bool | None | Unset): Only recommend models that support
            structured output.
        require_thinking (bool | None | Unset): Only recommend models that support
            thinking/reasoning.
        min_context_tokens (int | None | Unset): Minimum context window size in tokens.
        min_output_tokens (int | None | Unset): Minimum output token limit.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ModelRecommendationsResponse]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        require_tool_use=require_tool_use,
        require_structured_output=require_structured_output,
        require_thinking=require_thinking,
        min_context_tokens=min_context_tokens,
        min_output_tokens=min_output_tokens,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    require_tool_use: bool | None | Unset = UNSET,
    require_structured_output: bool | None | Unset = UNSET,
    require_thinking: bool | None | Unset = UNSET,
    min_context_tokens: int | None | Unset = UNSET,
    min_output_tokens: int | None | Unset = UNSET,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | ModelRecommendationsResponse | None:
    """Get Recommendations

     Get replacement/upgrade recommendations for a model.

    Returns a designated successor (if any), same-family upgrades, and cross-provider/cross-family
    alternatives.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        model_id (str):
        require_tool_use (bool | None | Unset): Only recommend models that support tool use.
        require_structured_output (bool | None | Unset): Only recommend models that support
            structured output.
        require_thinking (bool | None | Unset): Only recommend models that support
            thinking/reasoning.
        min_context_tokens (int | None | Unset): Minimum context window size in tokens.
        min_output_tokens (int | None | Unset): Minimum output token limit.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ModelRecommendationsResponse
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            client=client,
            require_tool_use=require_tool_use,
            require_structured_output=require_structured_output,
            require_thinking=require_thinking,
            min_context_tokens=min_context_tokens,
            min_output_tokens=min_output_tokens,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
