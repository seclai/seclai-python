from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_experiment_api_models_playground_experiments_post_response_create_experiment_api_models_playground_experiments_post import (
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.playground_create_request import PlaygroundCreateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id

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
) -> (
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost.from_dict(
            response.json()
        )

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
) -> Response[
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost
    | HTTPValidationError
]:
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
) -> Response[
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost
    | HTTPValidationError
]:
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost | HTTPValidationError]
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
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost
    | HTTPValidationError
    | None
):
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_account_id=x_account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> Response[
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost
    | HTTPValidationError
]:
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost | HTTPValidationError]
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
    body: PlaygroundCreateRequest,
    x_account_id: UUID | Unset = UNSET,
) -> (
    CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost
    | HTTPValidationError
    | None
):
    """Create Experiment

     Create and schedule a model playground experiment.

    Runs the given prompt against 1-10 models in parallel and optionally evaluates the outputs with an
    LLM judge.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token.

    Args:
        x_account_id (UUID | Unset):
        body (PlaygroundCreateRequest): Create a model playground experiment via the public API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateExperimentApiModelsPlaygroundExperimentsPostResponseCreateExperimentApiModelsPlaygroundExperimentsPost | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_account_id=x_account_id,
        )
    ).parsed
