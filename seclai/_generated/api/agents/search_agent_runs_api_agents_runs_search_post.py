from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_trace_search_request import AgentTraceSearchRequest
from ...models.agent_trace_search_response import AgentTraceSearchResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AgentTraceSearchRequest,
    x_account_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/runs/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentTraceSearchResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentTraceSearchResponse.from_dict(response.json())

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
) -> Response[AgentTraceSearchResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentTraceSearchRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[AgentTraceSearchResponse | HTTPValidationError]:
    """Search agent traces

     Search agent traces using semantic similarity.

    Finds step-run outputs that are most semantically similar to the query.
    Results include the matching text, agent/step metadata, and a similarity score.

    Agent traces are automatically indexed when runs complete. The first 7 days of storage are free;
    extended retention is billed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Searches only within your account's traces.

    Args:
        x_account_id (str | Unset):
        body (AgentTraceSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTraceSearchResponse | HTTPValidationError]
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
    body: AgentTraceSearchRequest,
    x_account_id: str | Unset = UNSET,
) -> AgentTraceSearchResponse | HTTPValidationError | None:
    """Search agent traces

     Search agent traces using semantic similarity.

    Finds step-run outputs that are most semantically similar to the query.
    Results include the matching text, agent/step metadata, and a similarity score.

    Agent traces are automatically indexed when runs complete. The first 7 days of storage are free;
    extended retention is billed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Searches only within your account's traces.

    Args:
        x_account_id (str | Unset):
        body (AgentTraceSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTraceSearchResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentTraceSearchRequest,
    x_account_id: str | Unset = UNSET,
) -> Response[AgentTraceSearchResponse | HTTPValidationError]:
    """Search agent traces

     Search agent traces using semantic similarity.

    Finds step-run outputs that are most semantically similar to the query.
    Results include the matching text, agent/step metadata, and a similarity score.

    Agent traces are automatically indexed when runs complete. The first 7 days of storage are free;
    extended retention is billed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Searches only within your account's traces.

    Args:
        x_account_id (str | Unset):
        body (AgentTraceSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTraceSearchResponse | HTTPValidationError]
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
    body: AgentTraceSearchRequest,
    x_account_id: str | Unset = UNSET,
) -> AgentTraceSearchResponse | HTTPValidationError | None:
    """Search agent traces

     Search agent traces using semantic similarity.

    Finds step-run outputs that are most semantically similar to the query.
    Results include the matching text, agent/step metadata, and a similarity score.

    Agent traces are automatically indexed when runs complete. The first 7 days of storage are free;
    extended retention is billed.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. Searches only within your account's traces.

    Args:
        x_account_id (str | Unset):
        body (AgentTraceSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTraceSearchResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
