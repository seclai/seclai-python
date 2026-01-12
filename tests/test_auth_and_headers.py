import httpx
import pytest

from seclai import AsyncSeclai, Seclai, SeclaiConfigurationError


def test_api_key_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SECLAI_API_KEY", "env-key")
    client = Seclai()
    assert client.api_key == "env-key"


def test_api_key_param_takes_precedence(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SECLAI_API_KEY", "env-key")
    client = Seclai(api_key="param-key")
    assert client.api_key == "param-key"


def test_missing_api_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)
    with pytest.raises(SeclaiConfigurationError):
        _ = Seclai()


def test_header_injected_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SECLAI_API_KEY", "env-key")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("x-api-key") == "env-key"
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(http_client=http_client)
    assert client.request("GET", "/ping") == {"ok": True}


@pytest.mark.asyncio
async def test_header_injected_async(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SECLAI_API_KEY", "env-key")

    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("x-api-key") == "env-key"
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(
        transport=transport, base_url="https://example.invalid"
    )
    client = AsyncSeclai(http_client=http_client)
    assert await client.request("GET", "/ping") == {"ok": True}
    await http_client.aclose()
