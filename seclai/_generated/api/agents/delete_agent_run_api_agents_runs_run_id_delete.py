from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_response import AgentRunResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/agents/runs/{run_id}".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentRunResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentRunResponse.from_dict(response.json())

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
) -> Response[AgentRunResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Cancel an agent run

     Cancel a running agent run.

    If the run is already in a terminal state (`completed` or `failed`), cancellation will be rejected.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only cancel runs belonging to your
    account.

    Args:
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> AgentRunResponse | HTTPValidationError | None:
    """Cancel an agent run

     Cancel a running agent run.

    If the run is already in a terminal state (`completed` or `failed`), cancellation will be rejected.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only cancel runs belonging to your
    account.

    Args:
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Cancel an agent run

     Cancel a running agent run.

    If the run is already in a terminal state (`completed` or `failed`), cancellation will be rejected.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only cancel runs belonging to your
    account.

    Args:
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
) -> AgentRunResponse | HTTPValidationError | None:
    """Cancel an agent run

     Cancel a running agent run.

    If the run is already in a terminal state (`completed` or `failed`), cancellation will be rejected.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. You can only cancel runs belonging to your
    account.

    Args:
        run_id (str):
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            x_account_id=x_account_id,
        )
    ).parsed
