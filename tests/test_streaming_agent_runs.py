import asyncio
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

import httpx
import pytest

from seclai import (
    AgentRunStreamRequest,
    AsyncSeclai,
    Seclai,
    SeclaiError,
    SeclaiStreamingError,
)


def _agent_run_payload(status: str, *, output: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "attempts": [],
        "credits": None,
        "error_count": 0,
        "input": None,
        "output": output,
        "priority": False,
        "run_id": "run_1",
        "status": status,
    }
    return payload


def test_run_streaming_agent_and_wait_parses_done() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/agents/agent_1/runs/stream"
        assert "text/event-stream" in (request.headers.get("accept") or "")

        init_data = json.dumps(_agent_run_payload("processing"))
        done_data = json.dumps(_agent_run_payload("completed", output="ok"))

        content = (
            b": keepalive\n\n"
            + f"event: init\ndata: {init_data}\n\n".encode()
            + f"event: done\ndata: {done_data}\n\n".encode()
        )
        return httpx.Response(
            status_code=200,
            headers={"content-type": "text/event-stream"},
            content=content,
        )

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(base_url="https://example.invalid", transport=transport)

    client = Seclai(api_key="test", http_client=http_client)
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi", metadata={})
    )

    assert res.run_id == "run_1"
    assert res.output == "ok"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_parses_done() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/agents/agent_1/runs/stream"
        assert "text/event-stream" in (request.headers.get("accept") or "")

        init_data = json.dumps(_agent_run_payload("processing"))
        done_data = json.dumps(_agent_run_payload("completed", output="ok"))

        content = (
            b": keepalive\n\n"
            + f"event: init\ndata: {init_data}\n\n".encode()
            + f"event: done\ndata: {done_data}\n\n".encode()
        )
        return httpx.Response(
            status_code=200,
            headers={"content-type": "text/event-stream"},
            content=content,
        )

    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(
        base_url="https://example.invalid", transport=transport
    )

    async with AsyncSeclai(api_key="test", http_client=http_client) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi", metadata={})
        )

    assert res.run_id == "run_1"
    assert res.output == "ok"


def test_run_streaming_agent_and_wait_times_out() -> None:
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_POST(self) -> None:  # noqa: N802
            if self.path != "/agents/agent_1/runs/stream":
                self.send_response(404)
                self.end_headers()
                return

            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()

            self.wfile.write(b"event: init\n")
            self.wfile.write(b"data: {}\n\n")
            self.wfile.flush()

            # Keep the connection open longer than the client timeout.
            time.sleep(1.0)

        def log_message(self, format: str, *args: object) -> None:  # noqa: A003
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    try:
        base_url = f"http://127.0.0.1:{server.server_address[1]}"
        http_client = httpx.Client(base_url=base_url)
        client = Seclai(api_key="test", http_client=http_client)

        with pytest.raises(SeclaiError):
            client.run_streaming_agent_and_wait(
                "agent_1",
                body=AgentRunStreamRequest(input="hi", metadata={}),
                timeout=0.05,
            )
    finally:
        server.shutdown()
        server.server_close()


def _reported(status: str) -> dict[str, Any]:
    payload = _agent_run_payload(status, output="answer")
    payload["result_reported_at"] = "2026-11-05T00:00:00Z"
    return payload


def _sse(*events: tuple[str, dict[str, Any]]) -> bytes:
    return b"".join(
        f"event: {name}\ndata: {json.dumps(data)}\n\n".encode() for name, data in events
    )


def _stream_response(content: bytes) -> httpx.Response:
    return httpx.Response(
        status_code=200, headers={"content-type": "text/event-stream"}, content=content
    )


def _sync_client(stream: httpx.SyncByteStream | bytes) -> Seclai:
    def handler(req: httpx.Request) -> httpx.Response:
        if isinstance(stream, bytes):
            return _stream_response(stream)
        return httpx.Response(
            200, headers={"content-type": "text/event-stream"}, stream=stream
        )

    return Seclai(
        api_key="test",
        http_client=httpx.Client(
            base_url="https://example.invalid",
            transport=httpx.MockTransport(handler),
        ),
    )


def _async_client(stream: httpx.AsyncByteStream | bytes) -> AsyncSeclai:
    def handler(req: httpx.Request) -> httpx.Response:
        if isinstance(stream, bytes):
            return _stream_response(stream)
        return httpx.Response(
            200, headers={"content-type": "text/event-stream"}, stream=stream
        )

    return AsyncSeclai(
        api_key="test",
        http_client=httpx.AsyncClient(
            base_url="https://example.invalid",
            transport=httpx.MockTransport(handler),
        ),
    )


_INIT_AND_RESULT = _sse(
    ("init", _agent_run_payload("processing")),
    ("result", _reported("processing")),
)


def test_run_streaming_agent_and_wait_raises_with_result_when_stream_ends() -> None:
    client = _sync_client(_INIT_AND_RESULT)
    with pytest.raises(SeclaiStreamingError, match="reported its result") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1",
            body=AgentRunStreamRequest(input="hi"),
            raise_on_incomplete=True,
        )
    assert exc.value.run is not None
    assert exc.value.run.output == "answer"
    assert exc.value.run_id == "run_1"


def test_run_streaming_agent_and_wait_raises_with_init_when_stream_ends() -> None:
    client = _sync_client(_sse(("init", _agent_run_payload("processing"))))
    with pytest.raises(SeclaiStreamingError, match="not reported a result") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1",
            body=AgentRunStreamRequest(input="hi"),
            raise_on_incomplete=True,
        )
    assert exc.value.run is not None
    assert exc.value.run.status == "processing"


def test_run_streaming_agent_and_wait_prefers_done_over_result() -> None:
    client = _sync_client(
        _INIT_AND_RESULT + _sse(("done", _reported("failed"))),
    )
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi")
    )
    assert res.status == "failed"


def test_run_streaming_agent_and_wait_return_on_result() -> None:
    client = _sync_client(
        _INIT_AND_RESULT + _sse(("done", _reported("failed"))),
    )
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), return_on_result=True
    )
    assert res.status == "processing"
    assert res.output == "answer"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_raises_with_result_when_stream_ends() -> (
    None
):
    async with _async_client(_INIT_AND_RESULT) as client:
        with pytest.raises(SeclaiStreamingError) as exc:
            await client.run_streaming_agent_and_wait(
                "agent_1",
                body=AgentRunStreamRequest(input="hi"),
                raise_on_incomplete=True,
            )
    assert exc.value.run is not None
    assert exc.value.run.output == "answer"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_return_on_result() -> None:
    async with _async_client(
        _INIT_AND_RESULT + _sse(("done", _reported("failed")))
    ) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), return_on_result=True
        )
    assert res.status == "processing"


_CUTS = [httpx.ReadError("connection reset"), httpx.RemoteProtocolError("cut")]


class _CutAfterResult(httpx.SyncByteStream):
    def __init__(self, error: Exception) -> None:
        self.error = error

    def __iter__(self) -> Any:
        yield _INIT_AND_RESULT
        raise self.error


class _AsyncCutAfterResult(httpx.AsyncByteStream):
    def __init__(self, error: Exception) -> None:
        self.error = error

    async def __aiter__(self) -> Any:
        yield _INIT_AND_RESULT
        raise self.error


@pytest.mark.parametrize("error", _CUTS)
def test_run_streaming_agent_and_wait_raises_with_result_when_stream_is_cut(
    error: Exception,
) -> None:
    client = _sync_client(_CutAfterResult(error))
    with pytest.raises(SeclaiStreamingError, match="stream was cut") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1",
            body=AgentRunStreamRequest(input="hi"),
            raise_on_incomplete=True,
        )
    assert exc.value.run is not None
    assert exc.value.run.output == "answer"
    assert exc.value.__cause__ is error


@pytest.mark.asyncio
@pytest.mark.parametrize("error", _CUTS)
async def test_async_run_streaming_agent_and_wait_raises_with_result_when_stream_is_cut(
    error: Exception,
) -> None:
    async with _async_client(_AsyncCutAfterResult(error)) as client:
        with pytest.raises(SeclaiStreamingError, match="stream was cut") as exc:
            await client.run_streaming_agent_and_wait(
                "agent_1",
                body=AgentRunStreamRequest(input="hi"),
                raise_on_incomplete=True,
            )
    assert exc.value.run is not None
    assert exc.value.run.output == "answer"


_DONE = _sse(("done", _agent_run_payload("completed", output="final")))


class _LateDone(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT_AND_RESULT
        time.sleep(0.15)  # past the 0.05s deadline
        yield _DONE


class _AsyncLateDone(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT_AND_RESULT
        await asyncio.sleep(0.15)  # past the 0.05s deadline
        yield _DONE


def test_run_streaming_agent_and_wait_uses_done_read_past_the_deadline() -> None:
    client = _sync_client(_LateDone())
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
    )
    assert res.status == "completed"
    assert res.output == "final"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_uses_done_read_past_the_deadline() -> (
    None
):
    async with _async_client(_AsyncLateDone()) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
        )
    assert res.status == "completed"


class _ResultThenHang(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_POST(self) -> None:  # noqa: N802
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        self.wfile.write(_INIT_AND_RESULT)
        self.wfile.flush()
        time.sleep(1.0)  # longer than the client timeout; `done` never comes

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return


def test_run_streaming_agent_and_wait_raises_with_result_on_timeout() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _ResultThenHang)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    try:
        base_url = f"http://127.0.0.1:{server.server_address[1]}"
        client = Seclai(api_key="test", http_client=httpx.Client(base_url=base_url))
        with pytest.raises(SeclaiStreamingError, match="Timed out") as exc:
            client.run_streaming_agent_and_wait(
                "agent_1",
                body=AgentRunStreamRequest(input="hi"),
                timeout=0.2,
                raise_on_incomplete=True,
            )
        assert exc.value.run is not None
        assert exc.value.run.output == "answer"
    finally:
        server.shutdown()
        server.server_close()


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_raises_with_result_on_timeout() -> (
    None
):
    server = ThreadingHTTPServer(("127.0.0.1", 0), _ResultThenHang)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    try:
        base_url = f"http://127.0.0.1:{server.server_address[1]}"
        async with AsyncSeclai(
            api_key="test", http_client=httpx.AsyncClient(base_url=base_url)
        ) as client:
            with pytest.raises(SeclaiStreamingError, match="Timed out") as exc:
                await client.run_streaming_agent_and_wait(
                    "agent_1",
                    body=AgentRunStreamRequest(input="hi"),
                    timeout=0.2,
                    raise_on_incomplete=True,
                )
        assert exc.value.run is not None
        assert exc.value.run.output == "answer"
    finally:
        server.shutdown()
        server.server_close()


# With `raise_on_incomplete` off (the default), each ending behaves as in 1.9.0.


def test_run_streaming_agent_and_wait_returns_the_last_snapshot_when_stream_ends() -> (
    None
):
    client = _sync_client(_sse(("init", _agent_run_payload("processing"))))
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi")
    )
    assert res.status == "processing"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_returns_the_last_snapshot_when_stream_ends() -> (
    None
):
    async with _async_client(
        _sse(("init", _agent_run_payload("processing")))
    ) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )
    assert res.status == "processing"


def test_run_streaming_agent_and_wait_raises_on_an_empty_stream() -> None:
    client = _sync_client(b": keepalive\n\n")
    with pytest.raises(SeclaiError, match="before"):
        client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )


class _CutAfterInit(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _sse(("init", _agent_run_payload("processing")))
        raise httpx.ReadError("connection reset")


class _AsyncCutAfterInit(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _sse(("init", _agent_run_payload("processing")))
        raise httpx.ReadError("connection reset")


def test_run_streaming_agent_and_wait_lets_a_cut_through_by_default() -> None:
    client = _sync_client(_CutAfterInit())
    with pytest.raises(httpx.ReadError):
        client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_lets_a_cut_through_by_default() -> (
    None
):
    async with _async_client(_AsyncCutAfterInit()) as client:
        with pytest.raises(httpx.ReadError):
            await client.run_streaming_agent_and_wait(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_times_out_by_default() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _ResultThenHang)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    try:
        base_url = f"http://127.0.0.1:{server.server_address[1]}"
        async with AsyncSeclai(
            api_key="test", http_client=httpx.AsyncClient(base_url=base_url)
        ) as client:
            with pytest.raises(SeclaiError, match="Timed out"):
                await client.run_streaming_agent_and_wait(
                    "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.2
                )
    finally:
        server.shutdown()
        server.server_close()


# The one difference from 1.9.0, which ignored `result`: the latest snapshot
# returned at the end of the stream is the `result` one when it arrived.


def test_run_streaming_agent_and_wait_returns_the_result_snapshot_when_stream_ends() -> (
    None
):
    client = _sync_client(_INIT_AND_RESULT)
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi")
    )
    assert res.output == "answer"
    assert res.result_reported_at


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_returns_the_result_snapshot_when_stream_ends() -> (
    None
):
    async with _async_client(_INIT_AND_RESULT) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )
    assert res.output == "answer"
