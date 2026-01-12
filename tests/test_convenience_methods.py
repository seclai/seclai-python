import httpx
import pytest

from seclai import AsyncSeclai, Seclai


def test_convenience_delete_content_uses_generated_client_transport() -> None:
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        return httpx.Response(status_code=204)

    transport = httpx.MockTransport(handler)

    client = Seclai(api_key="test")
    gen = client._generated_client()
    gen.set_httpx_client(
        httpx.Client(base_url="https://api.seclai.com", transport=transport)
    )

    client.delete_content("sc_cv_123")
    assert seen == {"method": "DELETE", "path": "/api/contents/sc_cv_123"}


@pytest.mark.asyncio
async def test_async_convenience_delete_content_uses_generated_client_transport() -> None:
    seen: dict[str, str] = {}

    async def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        return httpx.Response(status_code=204)

    transport = httpx.MockTransport(handler)

    client = AsyncSeclai(api_key="test")
    gen = client._generated_client()
    gen.set_async_httpx_client(
        httpx.AsyncClient(base_url="https://api.seclai.com", transport=transport)
    )

    await client.delete_content("sc_cv_123")
    assert seen == {"method": "DELETE", "path": "/api/contents/sc_cv_123"}
