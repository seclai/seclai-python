from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_export_response import AgentExportResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    download: bool | Unset = True,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    params: dict[str, Any] = {}

    params["download"] = download

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/export".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentExportResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentExportResponse.from_dict(response.json())

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
) -> Response[AgentExportResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    download: bool | Unset = True,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentExportResponse | HTTPValidationError]:
    r"""Export agent definition

     Export an agent definition as a portable JSON snapshot.

    The response contains the full definition, trigger configuration with schedules, alert configs,
    evaluation criteria, agent-scoped governance policies, and a resolved dependency manifest that maps
    every referenced external entity UUID to its human-readable name.

    Response shape:
    - `export_version`: schema version (currently `\"2\"`)
    - `exported_at`: ISO-8601 timestamp
    - `agent`: name, description, schema_version, definition, timestamps
    - `trigger`: trigger type, input template, schedules
    - `alert_configs`: alert type, thresholds, recipients
    - `evaluation_criteria`: evaluation settings per step
    - `governance_policies`: agent-scoped governance policies
    - `dependencies`: knowledge_bases, memory_banks, source_connections, agents, users

    Query params:
    - `download` (default true): when true, sets `Content-Disposition: attachment` so clients treat the
    response as a file download.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When using OAuth, you may target a different organization account with `X-Account-Id`; for API
    keys, the key's account is always used.
    - You can only export agents belonging to the resolved account.

    Args:
        agent_id (str):
        download (bool | Unset): Return as file download Default: True.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentExportResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        download=download,
        x_account_id=x_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    download: bool | Unset = True,
    x_account_id: UUID | Unset = UNSET,
) -> AgentExportResponse | HTTPValidationError | None:
    r"""Export agent definition

     Export an agent definition as a portable JSON snapshot.

    The response contains the full definition, trigger configuration with schedules, alert configs,
    evaluation criteria, agent-scoped governance policies, and a resolved dependency manifest that maps
    every referenced external entity UUID to its human-readable name.

    Response shape:
    - `export_version`: schema version (currently `\"2\"`)
    - `exported_at`: ISO-8601 timestamp
    - `agent`: name, description, schema_version, definition, timestamps
    - `trigger`: trigger type, input template, schedules
    - `alert_configs`: alert type, thresholds, recipients
    - `evaluation_criteria`: evaluation settings per step
    - `governance_policies`: agent-scoped governance policies
    - `dependencies`: knowledge_bases, memory_banks, source_connections, agents, users

    Query params:
    - `download` (default true): when true, sets `Content-Disposition: attachment` so clients treat the
    response as a file download.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When using OAuth, you may target a different organization account with `X-Account-Id`; for API
    keys, the key's account is always used.
    - You can only export agents belonging to the resolved account.

    Args:
        agent_id (str):
        download (bool | Unset): Return as file download Default: True.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentExportResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        download=download,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    download: bool | Unset = True,
    x_account_id: UUID | Unset = UNSET,
) -> Response[AgentExportResponse | HTTPValidationError]:
    r"""Export agent definition

     Export an agent definition as a portable JSON snapshot.

    The response contains the full definition, trigger configuration with schedules, alert configs,
    evaluation criteria, agent-scoped governance policies, and a resolved dependency manifest that maps
    every referenced external entity UUID to its human-readable name.

    Response shape:
    - `export_version`: schema version (currently `\"2\"`)
    - `exported_at`: ISO-8601 timestamp
    - `agent`: name, description, schema_version, definition, timestamps
    - `trigger`: trigger type, input template, schedules
    - `alert_configs`: alert type, thresholds, recipients
    - `evaluation_criteria`: evaluation settings per step
    - `governance_policies`: agent-scoped governance policies
    - `dependencies`: knowledge_bases, memory_banks, source_connections, agents, users

    Query params:
    - `download` (default true): when true, sets `Content-Disposition: attachment` so clients treat the
    response as a file download.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When using OAuth, you may target a different organization account with `X-Account-Id`; for API
    keys, the key's account is always used.
    - You can only export agents belonging to the resolved account.

    Args:
        agent_id (str):
        download (bool | Unset): Return as file download Default: True.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentExportResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        download=download,
        x_account_id=x_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    download: bool | Unset = True,
    x_account_id: UUID | Unset = UNSET,
) -> AgentExportResponse | HTTPValidationError | None:
    r"""Export agent definition

     Export an agent definition as a portable JSON snapshot.

    The response contains the full definition, trigger configuration with schedules, alert configs,
    evaluation criteria, agent-scoped governance policies, and a resolved dependency manifest that maps
    every referenced external entity UUID to its human-readable name.

    Response shape:
    - `export_version`: schema version (currently `\"2\"`)
    - `exported_at`: ISO-8601 timestamp
    - `agent`: name, description, schema_version, definition, timestamps
    - `trigger`: trigger type, input template, schedules
    - `alert_configs`: alert type, thresholds, recipients
    - `evaluation_criteria`: evaluation settings per step
    - `governance_policies`: agent-scoped governance policies
    - `dependencies`: knowledge_bases, memory_banks, source_connections, agents, users

    Query params:
    - `download` (default true): when true, sets `Content-Disposition: attachment` so clients treat the
    response as a file download.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When using OAuth, you may target a different organization account with `X-Account-Id`; for API
    keys, the key's account is always used.
    - You can only export agents belonging to the resolved account.

    Args:
        agent_id (str):
        download (bool | Unset): Return as file download Default: True.
        x_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentExportResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            download=download,
            x_account_id=x_account_id,
        )
    ).parsed
