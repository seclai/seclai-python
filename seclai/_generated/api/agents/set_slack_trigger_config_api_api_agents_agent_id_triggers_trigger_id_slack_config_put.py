from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.service_unavailable_error import ServiceUnavailableError
from ...models.set_slack_trigger_config_api_request import (
    SetSlackTriggerConfigApiRequest,
)
from ...models.slack_trigger_config_api_response import SlackTriggerConfigApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: UUID,
    trigger_id: UUID,
    *,
    body: SetSlackTriggerConfigApiRequest,
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
        "url": "/agents/{agent_id}/triggers/{trigger_id}/slack-config".format(
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
) -> (
    HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse | None
):
    if response.status_code == 200:
        response_200 = SlackTriggerConfigApiResponse.from_dict(response.json())

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
    HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetSlackTriggerConfigApiRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse
]:
    """Configure a SLACK_COMMAND trigger

     Set the Slack connection, form, channels, visibility and conversation settings of an agent's
    SLACK_COMMAND trigger, which people run from Slack with `/seclai` or the message shortcut. Omitted
    fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (UUID):
        trigger_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetSlackTriggerConfigApiRequest): Omitted fields are left unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse]
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
    agent_id: UUID,
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetSlackTriggerConfigApiRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse | None
):
    """Configure a SLACK_COMMAND trigger

     Set the Slack connection, form, channels, visibility and conversation settings of an agent's
    SLACK_COMMAND trigger, which people run from Slack with `/seclai` or the message shortcut. Omitted
    fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (UUID):
        trigger_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetSlackTriggerConfigApiRequest): Omitted fields are left unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse
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
    agent_id: UUID,
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetSlackTriggerConfigApiRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse
]:
    """Configure a SLACK_COMMAND trigger

     Set the Slack connection, form, channels, visibility and conversation settings of an agent's
    SLACK_COMMAND trigger, which people run from Slack with `/seclai` or the message shortcut. Omitted
    fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (UUID):
        trigger_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetSlackTriggerConfigApiRequest): Omitted fields are left unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse]
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
    agent_id: UUID,
    trigger_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetSlackTriggerConfigApiRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> (
    HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse | None
):
    """Configure a SLACK_COMMAND trigger

     Set the Slack connection, form, channels, visibility and conversation settings of an agent's
    SLACK_COMMAND trigger, which people run from Slack with `/seclai` or the message shortcut. Omitted
    fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (UUID):
        trigger_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetSlackTriggerConfigApiRequest): Omitted fields are left unchanged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ServiceUnavailableError | SlackTriggerConfigApiResponse
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
