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


_DONE_DATA = f"data: {json.dumps(_agent_run_payload('completed', output='final'))}\n"


class _DoneSpanningTheDeadline(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT_AND_RESULT + b"event: done\n"
        time.sleep(0.15)  # past the 0.05s deadline
        yield _DONE_DATA.encode()
        time.sleep(0.15)
        yield b"\n"


class _AsyncDoneSpanningTheDeadline(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT_AND_RESULT + b"event: done\n"
        await asyncio.sleep(0.15)  # past the 0.05s deadline
        yield _DONE_DATA.encode()
        await asyncio.sleep(0.15)
        yield b"\n"


# The deadline is checked only between events: an event that began before it
# is read to its end.


def test_run_streaming_agent_and_wait_finishes_an_event_begun_before_the_deadline() -> (
    None
):
    client = _sync_client(_DoneSpanningTheDeadline())
    start = time.monotonic()
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
    )
    assert time.monotonic() - start < 0.6
    assert res.status == "completed"
    assert res.output == "final"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_finishes_an_event_begun_before_the_deadline() -> (
    None
):
    async with _async_client(_AsyncDoneSpanningTheDeadline()) as client:
        start = time.monotonic()
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
        )
    assert time.monotonic() - start < 0.6
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


# The stream endings the wait helpers and `run_streaming_agent()` share one
# parser for: the server's `error` and `timeout` events, an event read before
# a cut, a final line without a newline, and a plain JSON reply.

_INIT = _sse(("init", _agent_run_payload("processing")))
_ERROR = _sse(("error", {"run_id": "run_1", "error": "worker crashed"}))
_TIMEOUT = _sse(("timeout", {"run_id": "run_1"}))
_DONE_EVENT = b"event: done\n" + _DONE_DATA.encode()  # no closing blank line


@pytest.mark.parametrize("raise_on_incomplete", [False, True])
def test_run_streaming_agent_and_wait_raises_on_an_error_event(
    raise_on_incomplete: bool,
) -> None:
    client = _sync_client(_INIT_AND_RESULT + _ERROR)
    with pytest.raises(SeclaiStreamingError, match="worker crashed") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1",
            body=AgentRunStreamRequest(input="hi"),
            raise_on_incomplete=raise_on_incomplete,
        )
    assert exc.value.run is not None
    assert exc.value.run.output == "answer"
    assert exc.value.run_id == "run_1"


@pytest.mark.asyncio
@pytest.mark.parametrize("raise_on_incomplete", [False, True])
async def test_async_run_streaming_agent_and_wait_raises_on_an_error_event(
    raise_on_incomplete: bool,
) -> None:
    async with _async_client(_INIT + _ERROR) as client:
        with pytest.raises(SeclaiStreamingError, match="worker crashed") as exc:
            await client.run_streaming_agent_and_wait(
                "agent_1",
                body=AgentRunStreamRequest(input="hi"),
                raise_on_incomplete=raise_on_incomplete,
            )
    assert exc.value.run is not None
    assert exc.value.run.status == "processing"


def test_run_streaming_agent_and_wait_raises_on_an_error_event_before_any_run() -> None:
    client = _sync_client(_ERROR)
    with pytest.raises(SeclaiStreamingError, match="worker crashed") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )
    assert exc.value.run is None
    assert exc.value.run_id == "run_1"


@pytest.mark.parametrize("raise_on_incomplete", [False, True])
def test_run_streaming_agent_and_wait_raises_on_a_timeout_event(
    raise_on_incomplete: bool,
) -> None:
    client = _sync_client(_INIT + _TIMEOUT)
    with pytest.raises(SeclaiStreamingError, match="server timed out") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1",
            body=AgentRunStreamRequest(input="hi"),
            raise_on_incomplete=raise_on_incomplete,
        )
    assert exc.value.run is not None
    assert exc.value.run.status == "processing"


@pytest.mark.asyncio
@pytest.mark.parametrize("raise_on_incomplete", [False, True])
async def test_async_run_streaming_agent_and_wait_raises_on_a_timeout_event(
    raise_on_incomplete: bool,
) -> None:
    async with _async_client(_INIT_AND_RESULT + _TIMEOUT) as client:
        with pytest.raises(SeclaiStreamingError, match="server timed out") as exc:
            await client.run_streaming_agent_and_wait(
                "agent_1",
                body=AgentRunStreamRequest(input="hi"),
                raise_on_incomplete=raise_on_incomplete,
            )
    assert exc.value.run is not None
    assert exc.value.run.output == "answer"


class _CutAfterDone(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT_AND_RESULT + _DONE_EVENT
        raise httpx.ReadError("connection reset")


class _AsyncCutAfterDone(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT_AND_RESULT + _DONE_EVENT
        raise httpx.ReadError("connection reset")


def test_run_streaming_agent_and_wait_keeps_a_done_read_before_a_cut() -> None:
    client = _sync_client(_CutAfterDone())
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi")
    )
    assert res.status == "completed"
    assert res.output == "final"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_keeps_a_done_read_before_a_cut() -> (
    None
):
    async with _async_client(_AsyncCutAfterDone()) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )
    assert res.status == "completed"


class _CutInsideResult(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT + b"event: result\n"
        yield f"data: {json.dumps(_reported('processing'))}\n".encode()
        raise httpx.ReadError("connection reset")


def test_run_streaming_agent_and_wait_keeps_a_result_read_before_a_cut() -> None:
    client = _sync_client(_CutInsideResult())
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), return_on_result=True
    )
    assert res.output == "answer"


def test_run_streaming_agent_ends_at_a_done_read_before_a_cut() -> None:
    client = _sync_client(_CutAfterDone())
    seen = [
        name
        for name, _data in client.run_streaming_agent(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        )
    ]
    assert seen == ["init", "result", "done"]


@pytest.mark.asyncio
async def test_async_run_streaming_agent_ends_at_a_done_read_before_a_cut() -> None:
    async with _async_client(_AsyncCutAfterDone()) as client:
        seen = [
            name
            async for name, _data in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )
        ]
    assert seen == ["init", "result", "done"]


def test_run_streaming_agent_yields_a_result_read_before_a_cut() -> None:
    client = _sync_client(_CutInsideResult())
    seen: list[str] = []
    with pytest.raises(httpx.ReadError):
        for name, _data in client.run_streaming_agent(
            "agent_1", body=AgentRunStreamRequest(input="hi")
        ):
            seen.append(name)
    assert seen == ["init", "result"]


_UNTERMINATED = _INIT + b"event: done\n" + _DONE_DATA.encode().rstrip(b"\n")


def test_run_streaming_agent_parses_a_final_line_without_a_newline() -> None:
    client = _sync_client(_UNTERMINATED)
    events = list(
        client.run_streaming_agent("agent_1", body=AgentRunStreamRequest(input="hi"))
    )
    assert [name for name, _ in events] == ["init", "done"]
    assert events[-1][1]["output"] == "final"
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), raise_on_incomplete=True
    )
    assert res.output == "final"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_parses_a_final_line_without_a_newline() -> (
    None
):
    async with _async_client(_UNTERMINATED) as client:
        events = [
            e
            async for e in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )
        ]
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), raise_on_incomplete=True
        )
    assert [name for name, _ in events] == ["init", "done"]
    assert res.output == "final"


def _json_client(sync: bool) -> Any:
    payload = _agent_run_payload("completed", output="plain")

    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=payload)

    transport = httpx.MockTransport(handler)
    if sync:
        return Seclai(
            api_key="test",
            http_client=httpx.Client(
                base_url="https://example.invalid", transport=transport
            ),
        )
    return AsyncSeclai(
        api_key="test",
        http_client=httpx.AsyncClient(
            base_url="https://example.invalid", transport=transport
        ),
    )


def test_a_plain_json_reply_is_one_done_event() -> None:
    client = _json_client(sync=True)
    events = list(
        client.run_streaming_agent("agent_1", body=AgentRunStreamRequest(input="hi"))
    )
    assert [name for name, _ in events] == ["done"]
    assert events[0][1]["output"] == "plain"
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), raise_on_incomplete=True
    )
    assert res.output == "plain"


@pytest.mark.asyncio
async def test_async_a_plain_json_reply_is_one_done_event() -> None:
    async with _json_client(sync=False) as client:
        events = [
            e
            async for e in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )
        ]
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), raise_on_incomplete=True
        )
    assert [name for name, _ in events] == ["done"]
    assert res.output == "plain"


def test_run_streaming_agent_raises_the_server_error_text() -> None:
    client = _sync_client(_INIT + _ERROR)
    with pytest.raises(SeclaiStreamingError) as exc:
        list(
            client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )
        )
    assert exc.value.message == "worker crashed"
    assert exc.value.run_id == "run_1"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_raises_the_server_error_text() -> None:
    async with _async_client(_INIT + _ERROR) as client:
        with pytest.raises(SeclaiStreamingError) as exc:
            async for _ in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            ):
                pass
    assert exc.value.message == "worker crashed"


def test_run_streaming_agent_still_yields_a_timeout_event() -> None:
    client = _sync_client(_INIT + _TIMEOUT)
    events = list(
        client.run_streaming_agent("agent_1", body=AgentRunStreamRequest(input="hi"))
    )
    assert events[-1] == ("timeout", {"run_id": "run_1"})


def test_run_streaming_agent_and_wait_ignores_update_events_as_released() -> None:
    update = _agent_run_payload("processing", output="partial")
    client = _sync_client(_INIT + _sse(("update", update)))
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi")
    )
    assert res.output is None  # the `init` snapshot, not the `update` one


# `Seclai(timeout=None)` means no limit: the streaming methods then have no
# deadline and send no httpx limit, unless a per-call `timeout` is passed.

_INIT_AND_DONE = _INIT + _sse(("done", _agent_run_payload("completed", output="ok")))


def _no_timeout_client(sync: bool, seen: list[httpx.Request]) -> Any:
    def handler(req: httpx.Request) -> httpx.Response:
        seen.append(req)
        return _stream_response(_INIT_AND_DONE)

    no_timeout: Any = None
    client: Any = (Seclai if sync else AsyncSeclai)(api_key="test", timeout=no_timeout)
    client._client._transport = httpx.MockTransport(handler)
    return client


@pytest.mark.parametrize(("per_call", "expected"), [(None, None), (5.0, 5.0)])
def test_streaming_methods_take_a_none_client_timeout_as_no_limit(
    per_call: float | None, expected: float | None
) -> None:
    seen: list[httpx.Request] = []
    client = _no_timeout_client(True, seen)
    body = AgentRunStreamRequest(input="hi")
    events = list(client.run_streaming_agent("agent_1", body=body, timeout=per_call))
    res = client.run_streaming_agent_and_wait("agent_1", body=body, timeout=per_call)
    assert [name for name, _ in events] == ["init", "done"]
    assert res.output == "ok"
    assert [set(r.extensions["timeout"].values()) for r in seen] == [{expected}] * 2


@pytest.mark.asyncio
@pytest.mark.parametrize(("per_call", "expected"), [(None, None), (5.0, 5.0)])
async def test_async_streaming_methods_take_a_none_client_timeout_as_no_limit(
    per_call: float | None, expected: float | None
) -> None:
    seen: list[httpx.Request] = []
    client = _no_timeout_client(False, seen)
    body = AgentRunStreamRequest(input="hi")
    events = [
        e
        async for e in client.run_streaming_agent(
            "agent_1", body=body, timeout=per_call
        )
    ]
    res = await client.run_streaming_agent_and_wait(
        "agent_1", body=body, timeout=per_call
    )
    assert [name for name, _ in events] == ["init", "done"]
    assert res.output == "ok"
    assert [set(r.extensions["timeout"].values()) for r in seen] == [{expected}] * 2


# Time the caller spends on the last event does not count against the deadline.


def test_run_streaming_agent_ignores_time_spent_by_the_caller_on_the_last_event() -> (
    None
):
    client = _sync_client(_INIT_AND_DONE)
    names: list[str] = []
    for name, _ in client.run_streaming_agent(
        "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.2
    ):
        names.append(name)
        if name == "done":
            time.sleep(0.3)
    assert names == ["init", "done"]


@pytest.mark.asyncio
async def test_async_run_streaming_agent_ignores_time_spent_by_the_caller_on_the_last_event() -> (
    None
):
    names: list[str] = []
    async with _async_client(_INIT_AND_DONE) as client:
        async for name, _ in client.run_streaming_agent(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.2
        ):
            names.append(name)
            if name == "done":
                await asyncio.sleep(0.3)
    assert names == ["init", "done"]


# When the deadline passes inside an event, that event is read to its end and
# yielded before the error.

_RESULT_DATA = f"data: {json.dumps(_reported('processing'))}\n".encode()


class _ResultSpanningTheDeadline(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT + b"event: result\n"
        time.sleep(0.15)  # past the 0.05s deadline
        yield _RESULT_DATA + b"\n"
        time.sleep(1.0)


class _AsyncResultSpanningTheDeadline(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT + b"event: result\n"
        await asyncio.sleep(0.15)  # past the 0.05s deadline
        yield _RESULT_DATA + b"\n"
        await asyncio.sleep(1.0)


def test_run_streaming_agent_yields_the_event_read_when_the_deadline_passes() -> None:
    client = _sync_client(_ResultSpanningTheDeadline())
    names: list[str] = []
    with pytest.raises(SeclaiError, match="Timed out"):
        for name, _ in client.run_streaming_agent(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
        ):
            names.append(name)
    assert names == ["init", "result"]


@pytest.mark.asyncio
async def test_async_run_streaming_agent_yields_the_event_read_when_the_deadline_passes() -> (
    None
):
    names: list[str] = []
    async with _async_client(_AsyncResultSpanningTheDeadline()) as client:
        with pytest.raises(SeclaiError, match="Timed out"):
            async for name, _ in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
            ):
                names.append(name)
    assert names == ["init", "result"]


class _AsyncCutInsideResult(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT + b"event: result\n"
        yield f"data: {json.dumps(_reported('processing'))}\n".encode()
        raise httpx.ReadError("connection reset")


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_keeps_a_result_read_before_a_cut() -> (
    None
):
    async with _async_client(_AsyncCutInsideResult()) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), return_on_result=True
        )
    assert res.output == "answer"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_raises_on_an_error_event_before_any_run() -> (
    None
):
    async with _async_client(_ERROR) as client:
        with pytest.raises(SeclaiStreamingError, match="worker crashed") as exc:
            await client.run_streaming_agent_and_wait(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )
    assert exc.value.run is None
    assert exc.value.run_id == "run_1"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_still_yields_a_timeout_event() -> None:
    async with _async_client(_INIT + _TIMEOUT) as client:
        events = [
            e
            async for e in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi")
            )
        ]
    assert events[-1] == ("timeout", {"run_id": "run_1"})


# The server closes the stream after `done`, so the deadline never follows it.


class _DoneClosedAfterTheDeadline(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT + b"event: done\n" + _DONE_DATA.encode()
        time.sleep(0.15)  # past the 0.05s deadline
        yield b"\n"


class _AsyncDoneClosedAfterTheDeadline(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT + b"event: done\n" + _DONE_DATA.encode()
        await asyncio.sleep(0.15)  # past the 0.05s deadline
        yield b"\n"


def test_run_streaming_agent_does_not_time_out_after_done() -> None:
    client = _sync_client(_DoneClosedAfterTheDeadline())
    names = [
        name
        for name, _ in client.run_streaming_agent(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
        )
    ]
    assert names == ["init", "done"]


@pytest.mark.asyncio
async def test_async_run_streaming_agent_does_not_time_out_after_done() -> None:
    async with _async_client(_AsyncDoneClosedAfterTheDeadline()) as client:
        names = [
            name
            async for name, _ in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
            )
        ]
    assert names == ["init", "done"]


# A JSON reply carrying a run that has not finished is its latest snapshot.


def _json_run_client(sync: bool, payload: dict[str, Any]) -> Any:
    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=payload)

    transport = httpx.MockTransport(handler)
    if sync:
        return Seclai(
            api_key="test",
            http_client=httpx.Client(
                base_url="https://example.invalid", transport=transport
            ),
        )
    return AsyncSeclai(
        api_key="test",
        http_client=httpx.AsyncClient(
            base_url="https://example.invalid", transport=transport
        ),
    )


def test_an_unfinished_json_reply_raises_with_raise_on_incomplete() -> None:
    client = _json_run_client(True, _agent_run_payload("processing"))
    body = AgentRunStreamRequest(input="hi")
    with pytest.raises(SeclaiStreamingError, match="JSON") as exc:
        client.run_streaming_agent_and_wait(
            "agent_1", body=body, raise_on_incomplete=True
        )
    assert exc.value.run is not None
    assert exc.value.run.status == "processing"
    res = client.run_streaming_agent_and_wait("agent_1", body=body)
    assert res.status == "processing"


@pytest.mark.asyncio
async def test_async_an_unfinished_json_reply_raises_with_raise_on_incomplete() -> None:
    body = AgentRunStreamRequest(input="hi")
    async with _json_run_client(False, _agent_run_payload("processing")) as client:
        with pytest.raises(SeclaiStreamingError, match="JSON") as exc:
            await client.run_streaming_agent_and_wait(
                "agent_1", body=body, raise_on_incomplete=True
            )
        res = await client.run_streaming_agent_and_wait("agent_1", body=body)
    assert exc.value.run is not None
    assert res.status == "processing"


def test_a_reported_json_reply_is_returned_with_return_on_result() -> None:
    client = _json_run_client(True, _reported("processing"))
    res = client.run_streaming_agent_and_wait(
        "agent_1",
        body=AgentRunStreamRequest(input="hi"),
        return_on_result=True,
        raise_on_incomplete=True,
    )
    assert res.output == "answer"


# The deadline is checked only at an event boundary (issue #23): an event
# whose first line has arrived is read to its end, while a stream of
# keepalives still times out.

_WHOLE_DONE = b"id: 2\n" + _sse(
    ("done", _agent_run_payload("completed", output="final"))
)


class _DoneWholeAfterTheDeadline(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield b"id: 1\n" + _INIT
        time.sleep(0.15)  # past the 0.05s deadline
        yield _WHOLE_DONE


class _AsyncDoneWholeAfterTheDeadline(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield b"id: 1\n" + _INIT
        await asyncio.sleep(0.15)  # past the 0.05s deadline
        yield _WHOLE_DONE


def test_run_streaming_agent_and_wait_reads_an_event_arriving_whole_late() -> None:
    client = _sync_client(_DoneWholeAfterTheDeadline())
    res = client.run_streaming_agent_and_wait(
        "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
    )
    assert res.status == "completed"
    assert res.output == "final"


@pytest.mark.asyncio
async def test_async_run_streaming_agent_and_wait_reads_an_event_arriving_whole_late() -> (
    None
):
    async with _async_client(_AsyncDoneWholeAfterTheDeadline()) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
        )
    assert res.status == "completed"


def test_run_streaming_agent_reads_an_event_arriving_whole_late() -> None:
    client = _sync_client(_DoneWholeAfterTheDeadline())
    names = [
        name
        for name, _ in client.run_streaming_agent(
            "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
        )
    ]
    assert names == ["init", "done"]


@pytest.mark.asyncio
async def test_async_run_streaming_agent_reads_an_event_arriving_whole_late() -> None:
    async with _async_client(_AsyncDoneWholeAfterTheDeadline()) as client:
        names = [
            name
            async for name, _ in client.run_streaming_agent(
                "agent_1", body=AgentRunStreamRequest(input="hi"), timeout=0.05
            )
        ]
    assert names == ["init", "done"]


class _Keepalives(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        for _ in range(40):
            yield b": keepalive\n\n"
            time.sleep(0.05)


class _AsyncKeepalives(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        for _ in range(40):
            yield b": keepalive\n\n"
            await asyncio.sleep(0.05)


def test_streaming_methods_time_out_on_keepalives() -> None:
    client = _sync_client(_Keepalives())
    body = AgentRunStreamRequest(input="hi")
    start = time.monotonic()
    with pytest.raises(SeclaiError, match="Timed out"):
        list(client.run_streaming_agent("agent_1", body=body, timeout=0.2))
    with pytest.raises(SeclaiStreamingError, match="Timed out"):
        client.run_streaming_agent_and_wait("agent_1", body=body, timeout=0.2)
    assert time.monotonic() - start < 1.0


@pytest.mark.asyncio
async def test_async_streaming_methods_time_out_on_keepalives() -> None:
    body = AgentRunStreamRequest(input="hi")
    start = time.monotonic()
    async with _async_client(_AsyncKeepalives()) as client:
        with pytest.raises(SeclaiError, match="Timed out"):
            async for _ in client.run_streaming_agent(
                "agent_1", body=body, timeout=0.2
            ):
                pass
        with pytest.raises(SeclaiStreamingError, match="Timed out"):
            await client.run_streaming_agent_and_wait("agent_1", body=body, timeout=0.2)
    assert time.monotonic() - start < 1.0


class _CrlfSplitAcrossChunks(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        done = json.dumps(_agent_run_payload("completed", output="ok"))
        yield b"event: done\r"
        yield f"\ndata: {done}\r".encode()
        yield b"\n\r\n"


def test_run_streaming_agent_reads_a_crlf_split_across_chunks() -> None:
    client = _sync_client(_CrlfSplitAcrossChunks())
    events = list(
        client.run_streaming_agent("agent_1", body=AgentRunStreamRequest(input="hi"))
    )
    assert [(name, data["output"]) for name, data in events] == [("done", "ok")]


# A `done` larger than one read, whose first bytes arrive after the deadline,
# is read to its end in every chunk it comes in (issue #23).

_BIG_DONE = _sse(("done", _agent_run_payload("completed", output="x" * 200_000)))
_BIG_DONE_CHUNKS = [_BIG_DONE[i : i + 65_536] for i in range(0, len(_BIG_DONE), 65_536)]


class _BigDoneAfterTheDeadline(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT
        time.sleep(0.25)  # past the 0.2s deadline, before the 0.4s cap
        for chunk in _BIG_DONE_CHUNKS:
            yield chunk
            time.sleep(0.01)


class _AsyncBigDoneAfterTheDeadline(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT
        await asyncio.sleep(0.25)  # past the 0.2s deadline, before the 0.4s cap
        for chunk in _BIG_DONE_CHUNKS:
            yield chunk
            await asyncio.sleep(0.01)


def test_streaming_methods_read_a_large_done_begun_after_the_deadline() -> None:
    assert len(_BIG_DONE_CHUNKS) > 1
    body = AgentRunStreamRequest(input="hi")
    client = _sync_client(_BigDoneAfterTheDeadline())
    res = client.run_streaming_agent_and_wait("agent_1", body=body, timeout=0.2)
    assert res.output == "x" * 200_000
    events = list(client.run_streaming_agent("agent_1", body=body, timeout=0.2))
    assert [name for name, _ in events] == ["init", "done"]
    assert events[-1][1]["output"] == "x" * 200_000


@pytest.mark.asyncio
async def test_async_streaming_methods_read_a_large_done_begun_after_the_deadline() -> (
    None
):
    body = AgentRunStreamRequest(input="hi")
    async with _async_client(_AsyncBigDoneAfterTheDeadline()) as client:
        res = await client.run_streaming_agent_and_wait(
            "agent_1", body=body, timeout=0.2
        )
        events = [
            e
            async for e in client.run_streaming_agent("agent_1", body=body, timeout=0.2)
        ]
    assert res.output == "x" * 200_000
    assert [name for name, _ in events] == ["init", "done"]


def test_line_splitter_clears_a_pending_cr_on_a_lone_lf_chunk() -> None:
    from seclai.seclai import _LineSplitter

    splitter = _LineSplitter()
    lines: list[str] = []
    for chunk in ["a\r", "\n", "\n"]:
        lines += splitter.decode(chunk)
    lines += splitter.flush()
    assert lines == ["a", ""]


# Only CR, LF and CRLF end an SSE line: U+2028, U+2029 and U+0085 inside a
# data field are kept (httpx's iter_lines split on them).

_ODD_OUTPUT = "a\u2028b\u2029c\u0085d"
_ODD_DONE = (
    "event: done\ndata: "
    + json.dumps(
        _agent_run_payload("completed", output=_ODD_OUTPUT), ensure_ascii=False
    )
    + "\n\n"
).encode()


def test_streaming_methods_keep_unicode_line_separators_in_data() -> None:
    body = AgentRunStreamRequest(input="hi")
    client = _sync_client(_ODD_DONE)
    assert (
        client.run_streaming_agent_and_wait("agent_1", body=body).output == _ODD_OUTPUT
    )
    events = list(client.run_streaming_agent("agent_1", body=body))
    assert events == [("done", _agent_run_payload("completed", output=_ODD_OUTPUT))]


@pytest.mark.asyncio
async def test_async_streaming_methods_keep_unicode_line_separators_in_data() -> None:
    body = AgentRunStreamRequest(input="hi")
    async with _async_client(_ODD_DONE) as client:
        res = await client.run_streaming_agent_and_wait("agent_1", body=body)
        events = [e async for e in client.run_streaming_agent("agent_1", body=body)]
    assert res.output == _ODD_OUTPUT
    assert events == [("done", _agent_run_payload("completed", output=_ODD_OUTPUT))]


# An event that never ends extends the call by at most one more `timeout`.


class _NeverEndingEvent(httpx.SyncByteStream):
    def __iter__(self) -> Any:
        yield _INIT + b"event: update\n"
        for _ in range(200):  # 2s of data lines, no blank line
            yield b"data: x\n"
            time.sleep(0.01)


class _AsyncNeverEndingEvent(httpx.AsyncByteStream):
    async def __aiter__(self) -> Any:
        yield _INIT + b"event: update\n"
        for _ in range(200):
            yield b"data: x\n"
            await asyncio.sleep(0.01)


def test_streaming_methods_cap_an_event_that_never_ends() -> None:
    body = AgentRunStreamRequest(input="hi")
    client = _sync_client(_NeverEndingEvent())
    start = time.monotonic()
    with pytest.raises(SeclaiStreamingError, match="Timed out"):
        client.run_streaming_agent_and_wait("agent_1", body=body, timeout=0.2)
    assert time.monotonic() - start < 0.7
    start = time.monotonic()
    with pytest.raises(SeclaiError, match="Timed out"):
        list(client.run_streaming_agent("agent_1", body=body, timeout=0.2))
    assert time.monotonic() - start < 0.7


@pytest.mark.asyncio
async def test_async_streaming_methods_cap_an_event_that_never_ends() -> None:
    body = AgentRunStreamRequest(input="hi")
    async with _async_client(_AsyncNeverEndingEvent()) as client:
        start = time.monotonic()
        with pytest.raises(SeclaiStreamingError, match="Timed out"):
            await client.run_streaming_agent_and_wait("agent_1", body=body, timeout=0.2)
        assert time.monotonic() - start < 0.7
        start = time.monotonic()
        with pytest.raises(SeclaiError, match="Timed out"):
            async for _ in client.run_streaming_agent(
                "agent_1", body=body, timeout=0.2
            ):
                pass
        assert time.monotonic() - start < 0.7
