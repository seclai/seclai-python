from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_attachment_refs_api_response import AgentAttachmentRefsApiResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/attachment-references".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentAttachmentRefsApiResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentAttachmentRefsApiResponse.from_dict(response.json())

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
) -> Response[AgentAttachmentRefsApiResponse | HTTPValidationError]:
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
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentAttachmentRefsApiResponse | HTTPValidationError]:
    """Get agent attachment-reference contract

     Return the static attachment-reference contract for an agent — what files the agent's definition
    expects on a run.

    Call this BEFORE staging uploads so you know whether the agent accepts files at all
    (``requires_uploads``), and which specific filenames/indexes/patterns the templates reference.
    Mismatched batches are rejected at run time with HTTP 400.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentAttachmentRefsApiResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentAttachmentRefsApiResponse | HTTPValidationError | None:
    """Get agent attachment-reference contract

     Return the static attachment-reference contract for an agent — what files the agent's definition
    expects on a run.

    Call this BEFORE staging uploads so you know whether the agent accepts files at all
    (``requires_uploads``), and which specific filenames/indexes/patterns the templates reference.
    Mismatched batches are rejected at run time with HTTP 400.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentAttachmentRefsApiResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentAttachmentRefsApiResponse | HTTPValidationError]:
    """Get agent attachment-reference contract

     Return the static attachment-reference contract for an agent — what files the agent's definition
    expects on a run.

    Call this BEFORE staging uploads so you know whether the agent accepts files at all
    (``requires_uploads``), and which specific filenames/indexes/patterns the templates reference.
    Mismatched batches are rejected at run time with HTTP 400.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentAttachmentRefsApiResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentAttachmentRefsApiResponse | HTTPValidationError | None:
    """Get agent attachment-reference contract

     Return the static attachment-reference contract for an agent — what files the agent's definition
    expects on a run.

    Call this BEFORE staging uploads so you know whether the agent accepts files at all
    (``requires_uploads``), and which specific filenames/indexes/patterns the templates reference.
    Mismatched batches are rejected at run time with HTTP 400.

    Args:
        agent_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentAttachmentRefsApiResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
