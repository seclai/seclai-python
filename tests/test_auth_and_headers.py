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


def test_missing_api_key_falls_back_to_sso(
    monkeypatch: pytest.MonkeyPatch, tmp_path: pytest.TempPathFactory
) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)
    monkeypatch.setenv("SECLAI_CONFIG_DIR", str(tmp_path))
    client = Seclai()
    # With built-in SSO defaults, client succeeds and falls back to SSO mode
    assert client._options.auth_state.mode == "sso"


def test_both_api_key_and_access_token_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)
    with pytest.raises(SeclaiConfigurationError, match="not both"):
        _ = Seclai(api_key="k", access_token="t")


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


# ── Bearer Token Auth ────────────────────────────────────────────────────────


def test_bearer_token_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("authorization") == "Bearer my-jwt"
        assert "x-api-key" not in request.headers
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(access_token="my-jwt", http_client=http_client)
    assert client.request("GET", "/ping") == {"ok": True}


def test_bearer_provider_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    call_count = 0

    def provider() -> str:
        nonlocal call_count
        call_count += 1
        return f"token-{call_count}"

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("authorization", "").startswith("Bearer token-")
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(access_token=provider, http_client=http_client)
    client.request("GET", "/ping1")
    client.request("GET", "/ping2")
    assert call_count == 2


def test_account_id_header_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("x-account-id") == "acct-123"
        assert request.headers.get("authorization") == "Bearer tok"
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(access_token="tok", account_id="acct-123", http_client=http_client)
    assert client.request("GET", "/ping") == {"ok": True}


@pytest.mark.asyncio
async def test_bearer_token_async(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("authorization") == "Bearer async-jwt"
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(
        transport=transport, base_url="https://example.invalid"
    )
    client = AsyncSeclai(access_token="async-jwt", http_client=http_client)
    assert await client.request("GET", "/ping") == {"ok": True}
    await http_client.aclose()


# ── Bearer auth on typed (generated-client) methods ──────────────────────────


def test_bearer_token_on_typed_method_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    """Typed wrapper methods (list_sources etc.) must send bearer auth headers."""
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("authorization") == "Bearer typed-jwt"
        assert "x-api-key" not in request.headers
        return httpx.Response(
            200,
            json={
                "data": [],
                "pagination": {
                    "page": 1,
                    "limit": 20,
                    "total": 0,
                    "pages": 0,
                    "has_next": False,
                    "has_prev": False,
                },
            },
        )

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(access_token="typed-jwt", http_client=http_client)
    # Also wire mock transport into the generated client used by typed methods
    gc = client._generated_client()
    gc.set_httpx_client(
        httpx.Client(
            transport=transport,
            base_url="https://example.invalid",
            headers=dict(gc._headers),
        )
    )
    result = client.list_sources()
    assert result.data == []


def test_bearer_provider_on_typed_method_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    """Typed wrapper methods must resolve dynamic bearer providers per-request."""
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    call_count = 0

    def provider() -> str:
        nonlocal call_count
        call_count += 1
        return f"dyn-token-{call_count}"

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("authorization", "").startswith("Bearer dyn-token-")
        return httpx.Response(
            200,
            json={
                "data": [],
                "pagination": {
                    "page": 1,
                    "limit": 20,
                    "total": 0,
                    "pages": 0,
                    "has_next": False,
                    "has_prev": False,
                },
            },
        )

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(access_token=provider, http_client=http_client)
    # Also wire mock transport into the generated client used by typed methods
    gc = client._generated_client()
    gc.set_httpx_client(
        httpx.Client(
            transport=transport,
            base_url="https://example.invalid",
            headers=dict(gc._headers),
        )
    )
    client.list_sources()
    client.list_sources()
    assert call_count == 2


# ── X-Account-Id only for bearer/SSO ─────────────────────────────────────────


def test_account_id_not_sent_for_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """X-Account-Id should NOT be sent when using api_key auth."""
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)

    def handler(request: httpx.Request) -> httpx.Response:
        assert "x-account-id" not in request.headers
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(api_key="k", account_id="acct-123", http_client=http_client)
    assert client.request("GET", "/ping") == {"ok": True}
