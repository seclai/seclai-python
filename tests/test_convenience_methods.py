import httpx
import pytest

import json

from seclai import AsyncSeclai, Seclai


def _extract_multipart_field(*, body: bytes, boundary: str, field_name: str) -> bytes | None:
    marker = f'name="{field_name}"'.encode()
    delim = ("--" + boundary).encode()
    for part in body.split(delim):
        if marker not in part:
            continue
        header_end = part.find(b"\r\n\r\n")
        if header_end == -1:
            continue
        value = part[header_end + 4 :]
        value = value.strip(b"\r\n")
        # Trim possible terminating boundary markers.
        value = value.strip(b"-")
        return value
    return None


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
    assert seen == {"method": "DELETE", "path": "/contents/sc_cv_123"}


def test_convenience_upload_file_to_source_sends_metadata_and_uses_generated_client_transport() -> None:
    seen: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        ct = request.headers.get("content-type", "")
        assert "multipart/form-data" in ct
        boundary = ct.split("boundary=")[-1]
        metadata_bytes = _extract_multipart_field(
            body=request.content, boundary=boundary, field_name="metadata"
        )
        assert metadata_bytes is not None
        seen["metadata"] = json.loads(metadata_bytes.decode("utf-8"))
        return httpx.Response(
            status_code=200,
            json={
                "content_version_id": "cv_1",
                "source_connection_content_version_id": "sc_cv_1",
                "filename": "hello.txt",
                "status": "uploaded",
            },
        )

    transport = httpx.MockTransport(handler)

    client = Seclai(api_key="test")
    gen = client._generated_client()
    gen.set_httpx_client(
        httpx.Client(base_url="https://api.seclai.com", transport=transport)
    )

    resp = client.upload_file_to_source(
        "sc_1",
        file=b"hello",
        file_name="hello.txt",
        mime_type="text/plain",
        metadata={"category": "docs", "author": "Ada"},
    )
    assert resp.filename == "hello.txt"
    assert seen == {
        "method": "POST",
        "path": "/sources/sc_1/upload",
        "metadata": {"category": "docs", "author": "Ada"},
    }


def test_convenience_upload_file_to_content_sends_metadata_and_uses_generated_client_transport() -> None:
    seen: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        ct = request.headers.get("content-type", "")
        assert "multipart/form-data" in ct
        boundary = ct.split("boundary=")[-1]
        metadata_bytes = _extract_multipart_field(
            body=request.content, boundary=boundary, field_name="metadata"
        )
        assert metadata_bytes is not None
        seen["metadata"] = json.loads(metadata_bytes.decode("utf-8"))
        return httpx.Response(
            status_code=200,
            json={
                "content_version_id": "cv_1",
                "source_connection_content_version_id": "sc_cv_1",
                "filename": "updated.pdf",
                "status": "pending",
            },
        )

    transport = httpx.MockTransport(handler)

    client = Seclai(api_key="test")
    gen = client._generated_client()
    gen.set_httpx_client(
        httpx.Client(base_url="https://api.seclai.com", transport=transport)
    )

    resp = client.upload_file_to_content(
        "sc_cv_1",
        file=b"%PDF",
        file_name="updated.pdf",
        mime_type="application/pdf",
        metadata={"revision": 2},
    )
    assert resp.filename == "updated.pdf"
    assert seen == {
        "method": "POST",
        "path": "/contents/sc_cv_1/upload",
        "metadata": {"revision": 2},
    }


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
    assert seen == {"method": "DELETE", "path": "/contents/sc_cv_123"}


@pytest.mark.asyncio
async def test_async_convenience_upload_file_to_source_sends_metadata_and_uses_generated_client_transport() -> None:
    seen: dict[str, object] = {}

    async def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        ct = request.headers.get("content-type", "")
        assert "multipart/form-data" in ct
        boundary = ct.split("boundary=")[-1]
        metadata_bytes = _extract_multipart_field(
            body=request.content, boundary=boundary, field_name="metadata"
        )
        assert metadata_bytes is not None
        seen["metadata"] = json.loads(metadata_bytes.decode("utf-8"))
        return httpx.Response(
            status_code=200,
            json={
                "content_version_id": "cv_1",
                "source_connection_content_version_id": "sc_cv_1",
                "filename": "hello.txt",
                "status": "uploaded",
            },
        )

    transport = httpx.MockTransport(handler)

    client = AsyncSeclai(api_key="test")
    gen = client._generated_client()
    gen.set_async_httpx_client(
        httpx.AsyncClient(base_url="https://api.seclai.com", transport=transport)
    )

    resp = await client.upload_file_to_source(
        "sc_1",
        file=b"hello",
        file_name="hello.txt",
        mime_type="text/plain",
        metadata={"category": "docs", "author": "Ada"},
    )
    assert resp.filename == "hello.txt"
    assert seen == {
        "method": "POST",
        "path": "/sources/sc_1/upload",
        "metadata": {"category": "docs", "author": "Ada"},
    }


@pytest.mark.asyncio
async def test_async_convenience_upload_file_to_content_sends_metadata_and_uses_generated_client_transport() -> None:
    seen: dict[str, object] = {}

    async def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        ct = request.headers.get("content-type", "")
        assert "multipart/form-data" in ct
        boundary = ct.split("boundary=")[-1]
        metadata_bytes = _extract_multipart_field(
            body=request.content, boundary=boundary, field_name="metadata"
        )
        assert metadata_bytes is not None
        seen["metadata"] = json.loads(metadata_bytes.decode("utf-8"))
        return httpx.Response(
            status_code=200,
            json={
                "content_version_id": "cv_1",
                "source_connection_content_version_id": "sc_cv_1",
                "filename": "updated.pdf",
                "status": "pending",
            },
        )

    transport = httpx.MockTransport(handler)

    client = AsyncSeclai(api_key="test")
    gen = client._generated_client()
    gen.set_async_httpx_client(
        httpx.AsyncClient(base_url="https://api.seclai.com", transport=transport)
    )

    resp = await client.upload_file_to_content(
        "sc_cv_1",
        file=b"%PDF",
        file_name="updated.pdf",
        mime_type="application/pdf",
        metadata={"revision": 2},
    )
    assert resp.filename == "updated.pdf"
    assert seen == {
        "method": "POST",
        "path": "/contents/sc_cv_1/upload",
        "metadata": {"revision": 2},
    }
