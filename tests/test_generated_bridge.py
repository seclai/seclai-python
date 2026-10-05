"""The typed methods send through the same httpx client as every other method."""

from typing import Any

import httpx
import pytest

from seclai import AsyncSeclai, Seclai
from seclai import seclai as seclai_module

_PAGE = {
    "data": [],
    "pagination": {
        "page": 1,
        "limit": 20,
        "total": 0,
        "pages": 0,
        "has_next": False,
        "has_prev": False,
    },
}


def _recorder(seen: list[httpx.Request]) -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=_PAGE)

    return httpx.MockTransport(handler)


def test_typed_method_uses_the_configured_timeout() -> None:
    seen: list[httpx.Request] = []
    client = Seclai(api_key="k", timeout=7.0)
    client._client._transport = _recorder(seen)

    client.list_sources()

    assert set(seen[0].extensions["timeout"].values()) == {7.0}


def test_typed_method_sends_through_a_supplied_client() -> None:
    seen: list[httpx.Request] = []
    http_client = httpx.Client(
        transport=_recorder(seen),
        base_url="https://proxy.invalid",
        timeout=3.0,
        headers={"x-via": "supplied"},
    )
    client = Seclai(api_key="k", http_client=http_client)

    client.list_sources()

    request = seen[0]
    assert request.url.host == "proxy.invalid"
    assert request.headers["x-api-key"] == "k"
    assert request.headers["x-via"] == "supplied"
    assert set(request.extensions["timeout"].values()) == {None}


def test_typed_method_reaches_the_api_through_a_client_with_no_base_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(seclai_module, "SECLAI_API_URL", "https://api.invalid/")
    seen: list[httpx.Request] = []
    client = Seclai(api_key="k", http_client=httpx.Client(transport=_recorder(seen)))

    client.list_sources()

    assert str(seen[0].url).startswith("https://api.invalid/sources")


def test_upload_sends_through_a_supplied_client() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(503, text="<html>down</html>")

    http_client = httpx.Client(
        transport=httpx.MockTransport(handler), base_url="https://proxy.invalid"
    )
    client = Seclai(api_key="k", http_client=http_client)

    with pytest.raises(seclai_module.SeclaiAPIStatusError):
        client.upload_file_to_source("sc_1", file=b"x", file_name="a.txt")

    assert seen[0].url.host == "proxy.invalid"
    assert seen[0].headers["x-api-key"] == "k"


def test_closing_leaves_a_supplied_client_open() -> None:
    http_client = httpx.Client(transport=_recorder([]))
    Seclai(api_key="k", http_client=http_client).close()
    assert not http_client.is_closed


def test_unknown_version_on_a_supplied_client_is_refused_by_a_typed_method() -> None:
    http_client = httpx.Client(
        transport=_recorder([]), base_url="https://proxy.invalid"
    )
    client = Seclai(api_key="k", http_client=http_client)
    http_client.headers["Seclai-Version"] = "2099-01-01"

    with pytest.raises(seclai_module.SeclaiConfigurationError):
        client.list_sources()


@pytest.mark.asyncio
async def test_async_typed_method_uses_the_configured_timeout() -> None:
    seen: list[httpx.Request] = []
    client = AsyncSeclai(api_key="k", timeout=7.0)
    client._client._transport = _recorder(seen)

    await client.list_sources()

    assert set(seen[0].extensions["timeout"].values()) == {7.0}


@pytest.mark.asyncio
async def test_async_typed_method_sends_through_a_supplied_client() -> None:
    seen: list[httpx.Request] = []
    http_client = httpx.AsyncClient(
        transport=_recorder(seen), base_url="https://proxy.invalid", timeout=3.0
    )
    client = AsyncSeclai(api_key="k", http_client=http_client)

    await client.list_sources()

    assert seen[0].url.host == "proxy.invalid"
    assert seen[0].headers["x-api-key"] == "k"
    assert set(seen[0].extensions["timeout"].values()) == {None}


def test_typed_method_has_no_timeout_unless_one_is_passed() -> None:
    seen: list[httpx.Request] = []
    client = Seclai(api_key="k")
    client._client._transport = _recorder(seen)

    client.list_sources()
    client.request("GET", "/sources/")

    assert set(seen[0].extensions["timeout"].values()) == {None}
    assert set(seen[1].extensions["timeout"].values()) == {30.0}


def test_a_passed_timeout_applies_through_a_supplied_client() -> None:
    seen: list[httpx.Request] = []
    http_client = httpx.Client(
        transport=_recorder(seen), base_url="https://proxy.invalid", timeout=3.0
    )
    client = Seclai(api_key="k", timeout=7.0, http_client=http_client)

    client.list_sources()

    assert set(seen[0].extensions["timeout"].values()) == {7.0}


@pytest.mark.asyncio
async def test_async_typed_method_has_no_timeout_unless_one_is_passed() -> None:
    seen: list[httpx.Request] = []
    client = AsyncSeclai(api_key="k")
    client._client._transport = _recorder(seen)

    await client.list_sources()
    await client.request("GET", "/sources/")

    assert set(seen[0].extensions["timeout"].values()) == {None}
    assert set(seen[1].extensions["timeout"].values()) == {30.0}


def test_an_explicit_none_timeout_still_means_no_timeout_everywhere() -> None:
    seen: list[httpx.Request] = []
    no_timeout: Any = None
    client = Seclai(api_key="k", timeout=no_timeout)
    client._client._transport = _recorder(seen)

    client.list_sources()
    client.request("GET", "/sources/")

    assert set(seen[0].extensions["timeout"].values()) == {None}
    assert set(seen[1].extensions["timeout"].values()) == {None}
