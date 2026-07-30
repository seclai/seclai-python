from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_experiment_response import CancelExperimentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    experiment_id: UUID,
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
        "method": "post",
        "url": "/models/playground/experiments/{experiment_id}/cancel".format(
            experiment_id=quote(str(experiment_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelExperimentResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CancelExperimentResponse.from_dict(response.json())

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
) -> Response[CancelExperimentResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    experiment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[CancelExperimentResponse | HTTPValidationError]:
    """Cancel Experiment Endpoint

     Cancel a running or pending model playground experiment.

    Signals running model calls to abort and marks the experiment as canceled.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The experiment must belong to the caller's
    account.

    Args:
        experiment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelExperimentResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experiment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> CancelExperimentResponse | HTTPValidationError | None:
    """Cancel Experiment Endpoint

     Cancel a running or pending model playground experiment.

    Signals running model calls to abort and marks the experiment as canceled.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The experiment must belong to the caller's
    account.

    Args:
        experiment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelExperimentResponse | HTTPValidationError
    """

    return sync_detailed(
        experiment_id=experiment_id,
        client=client,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    ).parsed


async def asyncio_detailed(
    experiment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> Response[CancelExperimentResponse | HTTPValidationError]:
    """Cancel Experiment Endpoint

     Cancel a running or pending model playground experiment.

    Signals running model calls to abort and marks the experiment as canceled.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The experiment must belong to the caller's
    account.

    Args:
        experiment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelExperimentResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
        x_account_id=x_account_id,
        seclai_version=seclai_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experiment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_account_id: UUID | Unset = UNSET,
    seclai_version: str | Unset = UNSET,
) -> CancelExperimentResponse | HTTPValidationError | None:
    """Cancel Experiment Endpoint

     Cancel a running or pending model playground experiment.

    Signals running model calls to abort and marks the experiment as canceled.

    Auth & scoping:
    - Requires `X-API-Key` header or OAuth Bearer token. The experiment must belong to the caller's
    account.

    Args:
        experiment_id (UUID):
        x_account_id (UUID | Unset):
        seclai_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelExperimentResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            experiment_id=experiment_id,
            client=client,
            x_account_id=x_account_id,
            seclai_version=seclai_version,
        )
    ).parsed
