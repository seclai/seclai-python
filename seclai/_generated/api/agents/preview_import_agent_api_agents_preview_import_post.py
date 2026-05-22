from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_definition_import_error_response import (
    AgentDefinitionImportErrorResponse,
)
from ...models.agent_import_preview_request import AgentImportPreviewRequest
from ...models.agent_import_preview_response import AgentImportPreviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AgentImportPreviewRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/agents/preview-import",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentDefinitionImportErrorResponse | AgentImportPreviewResponse | None:
    if response.status_code == 200:
        response_200 = AgentImportPreviewResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = AgentDefinitionImportErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentDefinitionImportErrorResponse | AgentImportPreviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentImportPreviewRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentDefinitionImportErrorResponse | AgentImportPreviewResponse]:
    """Preview an agent_definition import

     Validate an `agent_definition` payload (the same shape produced by `GET
    /api/agents/{agent_id}/export`) without creating or modifying any agent. On success returns a
    summary the client can show before commit (counts of steps, schedules, alert configs, evaluation
    criteria, governance policies). On failure returns the same 422 body shape used by `POST
    /api/agents` and `PUT /api/agents/{id}` so callers can render line/column-anchored errors.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. No DB writes.

    Args:
        x_account_id (UUID | Unset):
        body (AgentImportPreviewRequest): Dry-run import request — same payload shape as the
            export endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionImportErrorResponse | AgentImportPreviewResponse]
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
    body: AgentImportPreviewRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentDefinitionImportErrorResponse | AgentImportPreviewResponse | None:
    """Preview an agent_definition import

     Validate an `agent_definition` payload (the same shape produced by `GET
    /api/agents/{agent_id}/export`) without creating or modifying any agent. On success returns a
    summary the client can show before commit (counts of steps, schedules, alert configs, evaluation
    criteria, governance policies). On failure returns the same 422 body shape used by `POST
    /api/agents` and `PUT /api/agents/{id}` so callers can render line/column-anchored errors.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. No DB writes.

    Args:
        x_account_id (UUID | Unset):
        body (AgentImportPreviewRequest): Dry-run import request — same payload shape as the
            export endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionImportErrorResponse | AgentImportPreviewResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentImportPreviewRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentDefinitionImportErrorResponse | AgentImportPreviewResponse]:
    """Preview an agent_definition import

     Validate an `agent_definition` payload (the same shape produced by `GET
    /api/agents/{agent_id}/export`) without creating or modifying any agent. On success returns a
    summary the client can show before commit (counts of steps, schedules, alert configs, evaluation
    criteria, governance policies). On failure returns the same 422 body shape used by `POST
    /api/agents` and `PUT /api/agents/{id}` so callers can render line/column-anchored errors.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. No DB writes.

    Args:
        x_account_id (UUID | Unset):
        body (AgentImportPreviewRequest): Dry-run import request — same payload shape as the
            export endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentDefinitionImportErrorResponse | AgentImportPreviewResponse]
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
    body: AgentImportPreviewRequest,
    x_account_id: UUID | Unset = UNSET,
) -> AgentDefinitionImportErrorResponse | AgentImportPreviewResponse | None:
    """Preview an agent_definition import

     Validate an `agent_definition` payload (the same shape produced by `GET
    /api/agents/{agent_id}/export`) without creating or modifying any agent. On success returns a
    summary the client can show before commit (counts of steps, schedules, alert configs, evaluation
    criteria, governance policies). On failure returns the same 422 body shape used by `POST
    /api/agents` and `PUT /api/agents/{id}` so callers can render line/column-anchored errors.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. No DB writes.

    Args:
        x_account_id (UUID | Unset):
        body (AgentImportPreviewRequest): Dry-run import request — same payload shape as the
            export endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentDefinitionImportErrorResponse | AgentImportPreviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
