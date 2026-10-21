from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accepted_attachments_response import AcceptedAttachmentsResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.set_accepted_attachments_request import SetAcceptedAttachmentsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    trigger_id: str,
    *,
    body: SetAcceptedAttachmentsRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/agents/{agent_id}/triggers/{trigger_id}/accepted-attachments".format(
            agent_id=quote(str(agent_id), safe=""),
            trigger_id=quote(str(trigger_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = AcceptedAttachmentsResponse.from_dict(response.json())

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
) -> Response[
    AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAcceptedAttachmentsRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError
]:
    """Declare the input attachments a trigger accepts

     Replace the input attachments a trigger accepts. A run's files are each assigned to one declared
    attachment before any step runs; steps reference one as ``{{agent.attachments.<name>}}``. Rejected
    with HTTP 400 when the agent references an attachment the new declaration leaves out. `trigger_id`
    is the one `GET /agents/{agent_id}` returns.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetAcceptedAttachmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        trigger_id=trigger_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAcceptedAttachmentsRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Declare the input attachments a trigger accepts

     Replace the input attachments a trigger accepts. A run's files are each assigned to one declared
    attachment before any step runs; steps reference one as ``{{agent.attachments.<name>}}``. Rejected
    with HTTP 400 when the agent references an attachment the new declaration leaves out. `trigger_id`
    is the one `GET /agents/{agent_id}` returns.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetAcceptedAttachmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        agent_id=agent_id,
        trigger_id=trigger_id,
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAcceptedAttachmentsRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError
]:
    """Declare the input attachments a trigger accepts

     Replace the input attachments a trigger accepts. A run's files are each assigned to one declared
    attachment before any step runs; steps reference one as ``{{agent.attachments.<name>}}``. Rejected
    with HTTP 400 when the agent references an attachment the new declaration leaves out. `trigger_id`
    is the one `GET /agents/{agent_id}` returns.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetAcceptedAttachmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        trigger_id=trigger_id,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAcceptedAttachmentsRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Declare the input attachments a trigger accepts

     Replace the input attachments a trigger accepts. A run's files are each assigned to one declared
    attachment before any step runs; steps reference one as ``{{agent.attachments.<name>}}``. Rejected
    with HTTP 400 when the agent references an attachment the new declaration leaves out. `trigger_id`
    is the one `GET /agents/{agent_id}` returns.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetAcceptedAttachmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptedAttachmentsResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            trigger_id=trigger_id,
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
