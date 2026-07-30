from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_trigger_config_response import EmailTriggerConfigResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.set_email_trigger_config_request import SetEmailTriggerConfigRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    trigger_id: str,
    *,
    body: SetEmailTriggerConfigRequest,
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
        "url": "/agents/{agent_id}/triggers/{trigger_id}/email-config".format(
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
) -> EmailTriggerConfigResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EmailTriggerConfigResponse.from_dict(response.json())

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
) -> Response[EmailTriggerConfigResponse | HTTPValidationError]:
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
    body: SetEmailTriggerConfigRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[EmailTriggerConfigResponse | HTTPValidationError]:
    """Configure an EMAIL_RECEIVED trigger

     Set the custom alias, sender allowlist, and inbound-handling flags (`ignore_auto_generated`,
    `require_sender_auth`, `queue_on_quota`) on an agent's EMAIL_RECEIVED trigger, and return its
    computed email address(es). Omitted fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetEmailTriggerConfigRequest): Alias and/or sender allowlist for an EMAIL_RECEIVED
            trigger.

            A field omitted is left unchanged; passing ``null`` (or ``""`` for
            ``alias``) clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailTriggerConfigResponse | HTTPValidationError]
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
    body: SetEmailTriggerConfigRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> EmailTriggerConfigResponse | HTTPValidationError | None:
    """Configure an EMAIL_RECEIVED trigger

     Set the custom alias, sender allowlist, and inbound-handling flags (`ignore_auto_generated`,
    `require_sender_auth`, `queue_on_quota`) on an agent's EMAIL_RECEIVED trigger, and return its
    computed email address(es). Omitted fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetEmailTriggerConfigRequest): Alias and/or sender allowlist for an EMAIL_RECEIVED
            trigger.

            A field omitted is left unchanged; passing ``null`` (or ``""`` for
            ``alias``) clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailTriggerConfigResponse | HTTPValidationError
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
    body: SetEmailTriggerConfigRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[EmailTriggerConfigResponse | HTTPValidationError]:
    """Configure an EMAIL_RECEIVED trigger

     Set the custom alias, sender allowlist, and inbound-handling flags (`ignore_auto_generated`,
    `require_sender_auth`, `queue_on_quota`) on an agent's EMAIL_RECEIVED trigger, and return its
    computed email address(es). Omitted fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetEmailTriggerConfigRequest): Alias and/or sender allowlist for an EMAIL_RECEIVED
            trigger.

            A field omitted is left unchanged; passing ``null`` (or ``""`` for
            ``alias``) clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailTriggerConfigResponse | HTTPValidationError]
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
    body: SetEmailTriggerConfigRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> EmailTriggerConfigResponse | HTTPValidationError | None:
    """Configure an EMAIL_RECEIVED trigger

     Set the custom alias, sender allowlist, and inbound-handling flags (`ignore_auto_generated`,
    `require_sender_auth`, `queue_on_quota`) on an agent's EMAIL_RECEIVED trigger, and return its
    computed email address(es). Omitted fields are left unchanged.

    Auth & scoping: requires `X-API-Key` header or OAuth Bearer token; the trigger must belong to an
    agent in the key's account.

    Args:
        agent_id (str):
        trigger_id (str):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (SetEmailTriggerConfigRequest): Alias and/or sender allowlist for an EMAIL_RECEIVED
            trigger.

            A field omitted is left unchanged; passing ``null`` (or ``""`` for
            ``alias``) clears it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailTriggerConfigResponse | HTTPValidationError
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
