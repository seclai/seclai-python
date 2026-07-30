from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluation_criteria_response import EvaluationCriteriaResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/{agent_id}/evaluation-criteria".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[EvaluationCriteriaResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EvaluationCriteriaResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[EvaluationCriteriaResponse]]:
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
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | list[EvaluationCriteriaResponse]]:
    """List Evaluation Criteria

     List evaluation criteria configured for an agent.

    Response shape is version-gated by the ``Seclai-Version`` header:

    - **Default / legacy** (no header, or a date before ``2026-07-27``): a bare
      JSON array of criteria (unpaginated — every criterion for the agent).
    - **``Seclai-Version: 2026-07-27`` or later**: the canonical paginated
      envelope ``{data, pagination: {page, limit, total, pages, has_next,
      has_prev}}``.

    Each criterion carries its type, configuration, and a summary of results
    (pass / fail counts).  Criteria can be filtered client-side by type or
    enabled status.

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[EvaluationCriteriaResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        page=page,
        limit=limit,
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
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | list[EvaluationCriteriaResponse] | None:
    """List Evaluation Criteria

     List evaluation criteria configured for an agent.

    Response shape is version-gated by the ``Seclai-Version`` header:

    - **Default / legacy** (no header, or a date before ``2026-07-27``): a bare
      JSON array of criteria (unpaginated — every criterion for the agent).
    - **``Seclai-Version: 2026-07-27`` or later**: the canonical paginated
      envelope ``{data, pagination: {page, limit, total, pages, has_next,
      has_prev}}``.

    Each criterion carries its type, configuration, and a summary of results
    (pass / fail counts).  Criteria can be filtered client-side by type or
    enabled status.

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[EvaluationCriteriaResponse]
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[HTTPValidationError | list[EvaluationCriteriaResponse]]:
    """List Evaluation Criteria

     List evaluation criteria configured for an agent.

    Response shape is version-gated by the ``Seclai-Version`` header:

    - **Default / legacy** (no header, or a date before ``2026-07-27``): a bare
      JSON array of criteria (unpaginated — every criterion for the agent).
    - **``Seclai-Version: 2026-07-27`` or later**: the canonical paginated
      envelope ``{data, pagination: {page, limit, total, pages, has_next,
      has_prev}}``.

    Each criterion carries its type, configuration, and a summary of results
    (pass / fail counts).  Criteria can be filtered client-side by type or
    enabled status.

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[EvaluationCriteriaResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> HTTPValidationError | list[EvaluationCriteriaResponse] | None:
    """List Evaluation Criteria

     List evaluation criteria configured for an agent.

    Response shape is version-gated by the ``Seclai-Version`` header:

    - **Default / legacy** (no header, or a date before ``2026-07-27``): a bare
      JSON array of criteria (unpaginated — every criterion for the agent).
    - **``Seclai-Version: 2026-07-27`` or later**: the canonical paginated
      envelope ``{data, pagination: {page, limit, total, pages, has_next,
      has_prev}}``.

    Each criterion carries its type, configuration, and a summary of results
    (pass / fail counts).  Criteria can be filtered client-side by type or
    enabled status.

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[EvaluationCriteriaResponse]
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            page=page,
            limit=limit,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
