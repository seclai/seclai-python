from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_experiment_response import CreateExperimentResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.playground_create_request import PlaygroundCreateRequest
from ...models.service_unavailable_error import ServiceUnavailableError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

    if not isinstance(seclai_version, Unset):
        headers["Seclai-Version"] = seclai_version

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/models/playground/experiments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError | None:
    if response.status_code == 200:
        response_200 = CreateExperimentResponse.from_dict(response.json())

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
) -> Response[CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError]:
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When the credential is bound to a user, the experiment belongs to that user; only that user or an
    account-scoped key can cancel or delete it.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When the credential is bound to a user, the experiment belongs to that user; only that user or an
    account-scoped key can cancel or delete it.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError]:
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When the credential is bound to a user, the experiment belongs to that user; only that user or an
    account-scoped key can cancel or delete it.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError | None:
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.
    - When the credential is bound to a user, the experiment belongs to that user; only that user or an
    account-scoped key can cancel or delete it.

    Args:
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateExperimentResponse | HTTPValidationError | ServiceUnavailableError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
