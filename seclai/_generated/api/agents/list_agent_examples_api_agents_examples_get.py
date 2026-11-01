from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_example_list_response import AgentExampleListResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: None | str | Unset = UNSET,
    use_case: None | str | Unset = UNSET,
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

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_use_case: None | str | Unset
    if isinstance(use_case, Unset):
        json_use_case = UNSET
    else:
        json_use_case = use_case
    params["use_case"] = json_use_case

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agents/examples",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = AgentExampleListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = ServiceUnavailableError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: None | str | Unset = UNSET,
    use_case: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError]:
    """List agent gallery examples

     List the agent gallery: example agents to start from, searchable by text and filterable by use case.
    Pass an entry's `key` as `agent_template` on POST /agents, with `resource_bindings` for the
    resources it needs.

    Args:
        query (None | str | Unset): Words every match must contain.
        use_case (None | str | Unset): Only entries for this use case.
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        query=query,
        use_case=use_case,
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
    *,
    client: AuthenticatedClient | Client,
    query: None | str | Unset = UNSET,
    use_case: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError | None:
    """List agent gallery examples

     List the agent gallery: example agents to start from, searchable by text and filterable by use case.
    Pass an entry's `key` as `agent_template` on POST /agents, with `resource_bindings` for the
    resources it needs.

    Args:
        query (None | str | Unset): Words every match must contain.
        use_case (None | str | Unset): Only entries for this use case.
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        client=client,
        query=query,
        use_case=use_case,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: None | str | Unset = UNSET,
    use_case: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError]:
    """List agent gallery examples

     List the agent gallery: example agents to start from, searchable by text and filterable by use case.
    Pass an entry's `key` as `agent_template` on POST /agents, with `resource_bindings` for the
    resources it needs.

    Args:
        query (None | str | Unset): Words every match must contain.
        use_case (None | str | Unset): Only entries for this use case.
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        query=query,
        use_case=use_case,
        page=page,
        limit=limit,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: None | str | Unset = UNSET,
    use_case: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError | None:
    """List agent gallery examples

     List the agent gallery: example agents to start from, searchable by text and filterable by use case.
    Pass an entry's `key` as `agent_template` on POST /agents, with `resource_bindings` for the
    resources it needs.

    Args:
        query (None | str | Unset): Words every match must contain.
        use_case (None | str | Unset): Only entries for this use case.
        page (int | Unset): Page number Default: 1.
        limit (int | Unset): Items per page Default: 20.
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentExampleListResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            use_case=use_case,
            page=page,
            limit=limit,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
