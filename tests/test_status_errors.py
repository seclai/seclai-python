import httpx
import pytest

from seclai import Seclai, SeclaiAPIStatusError


def test_non_2xx_raises_status_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SECLAI_API_KEY", "k")

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"error": "unauthorized"})

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport, base_url="https://example.invalid")
    client = Seclai(http_client=http_client)

    with pytest.raises(SeclaiAPIStatusError) as exc:
        _ = client.request("GET", "/private")

    assert exc.value.status_code == 401
    assert exc.value.method == "GET"
