import asyncio
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import httpx
import pytest

from seclai import AgentRunStreamRequest, AsyncSeclai, Seclai, SeclaiError


def _agent_run_payload(status: str, *, output: str | None = None) -> dict:
    payload: dict = {
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
        assert request.url.path == "/api/agents/agent_1/runs/stream"
        assert "text/event-stream" in (request.headers.get("accept") or "")

        init_data = json.dumps(_agent_run_payload("processing"))
        done_data = json.dumps(_agent_run_payload("completed", output="ok"))

        content = (
            b": keepalive\n\n"
            + f"event: init\ndata: {init_data}\n\n".encode("utf-8")
            + f"event: done\ndata: {done_data}\n\n".encode("utf-8")
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
        assert request.url.path == "/api/agents/agent_1/runs/stream"
        assert "text/event-stream" in (request.headers.get("accept") or "")

        init_data = json.dumps(_agent_run_payload("processing"))
        done_data = json.dumps(_agent_run_payload("completed", output="ok"))

        content = (
            b": keepalive\n\n"
            + f"event: init\ndata: {init_data}\n\n".encode("utf-8")
            + f"event: done\ndata: {done_data}\n\n".encode("utf-8")
        )
        return httpx.Response(
            status_code=200,
            headers={"content-type": "text/event-stream"},
            content=content,
        )

    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(base_url="https://example.invalid", transport=transport)

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
            if self.path != "/api/agents/agent_1/runs/stream":
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

