import pytest

from seclai import Seclai
from seclai import seclai as seclai_module


def test_generated_client_get_httpx_client_has_api_key_header(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("SECLAI_API_KEY", "k")
    monkeypatch.setattr(seclai_module, "SECLAI_API_URL", "https://example.invalid")
    client = Seclai()

    gen = client._generated_client()
    http = gen.get_httpx_client()

    assert http.headers.get("x-api-key") == "k"
