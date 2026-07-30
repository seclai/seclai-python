"""Tests for all new convenience methods added to Seclai / AsyncSeclai.

Each group covers one resource area. Tests verify the correct HTTP method, path,
query parameters, and JSON body are sent via ``MockTransport``.
"""

from __future__ import annotations

import json
import pathlib
from typing import Any

import httpx
import pytest

import seclai
from seclai import AsyncSeclai, Seclai
from seclai import versions as seclai_versions

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sync_client(handler, **options: Any) -> Seclai:
    """A client wired to a MockTransport, with teardown.

    Takes **options so a test needing `api_version` or
    `allow_unknown_api_version` does not have to hand-build a client — three
    that did leaked their httpx client, and one reached the live base URL
    because it passed no transport at all.
    """
    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(base_url="https://example.invalid", transport=transport)
    client = Seclai(api_key="test", http_client=http_client, **options)
    # Ensure the externally-provided httpx client is closed when the SDK client closes.
    client._owns_client = True
    return client


def _async_client(handler, **options: Any) -> AsyncSeclai:
    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(
        base_url="https://example.invalid", transport=transport
    )
    client = AsyncSeclai(api_key="test", http_client=http_client, **options)
    client._owns_client = True
    return client


def _json_response(body: Any = None, status: int = 200) -> httpx.Response:
    if body is None:
        return httpx.Response(status_code=status)
    return httpx.Response(status_code=status, json=body)


# ---------------------------------------------------------------------------
# Agents
# ---------------------------------------------------------------------------


class TestAgents:
    def test_list_agents(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["page"] = req.url.params.get("page")
            return _json_response({"items": [], "total": 0})

        client = _sync_client(handler)
        result = client.list_agents(page=2, limit=10)
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents"
        assert seen["page"] == "2"
        assert result == {"items": [], "total": 0}

    def test_create_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response({"id": "a1", "name": "Test"})

        client = _sync_client(handler)
        result = client.create_agent({"name": "Test"})
        assert seen == {"method": "POST", "path": "/agents", "body": {"name": "Test"}}
        assert result["id"] == "a1"

    def test_get_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "a1"})

        client = _sync_client(handler)
        result = client.get_agent("a1")
        assert seen == {"method": "GET", "path": "/agents/a1"}
        assert result["id"] == "a1"

    def test_update_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response({"id": "a1", "name": "Updated"})

        client = _sync_client(handler)
        result = client.update_agent("a1", {"name": "Updated"})
        assert seen["method"] == "PUT"
        assert seen["path"] == "/agents/a1"
        assert result["name"] == "Updated"

    def test_delete_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_agent("a1")
        assert seen == {"method": "DELETE", "path": "/agents/a1"}

    def test_preview_import_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {
                    "ok": True,
                    "agent_name": "n",
                    "description": None,
                    "step_count": 0,
                    "schedules": 0,
                    "alert_configs": 0,
                    "evaluation_criteria": 0,
                    "governance_policies": 0,
                }
            )

        client = _sync_client(handler)
        result = client.preview_import_agent(
            {"agent_definition": {"agent": {"name": "n"}}}
        )
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/preview-import"
        assert seen["body"] == {"agent_definition": {"agent": {"name": "n"}}}
        assert result["ok"] is True


# ---------------------------------------------------------------------------
# Agent Definitions
# ---------------------------------------------------------------------------


class TestAgentDefinitions:
    def test_get_agent_definition(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"steps": []})

        client = _sync_client(handler)
        result = client.get_agent_definition("a1")
        assert seen == {"method": "GET", "path": "/agents/a1/definition"}
        assert result == {"steps": []}

    def test_update_agent_definition(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response({"steps": [{"type": "llm"}]})

        client = _sync_client(handler)
        body = {"change_id": "c1", "steps": [{"type": "llm"}]}
        client.update_agent_definition("a1", body)
        assert seen["method"] == "PUT"
        assert seen["path"] == "/agents/a1/definition"


# ---------------------------------------------------------------------------
# Agent Runs (additional)
# ---------------------------------------------------------------------------


class TestAgentRunsAdditional:
    def test_search_agent_runs(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response({"results": []})

        client = _sync_client(handler)
        client.search_agent_runs({"query": "test"})
        assert seen == {
            "method": "POST",
            "path": "/agents/runs/search",
            "body": {"query": "test"},
        }

    def test_cancel_agent_run(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"run_id": "r1", "status": "cancelled"})

        client = _sync_client(handler)
        client.cancel_agent_run("r1")
        # Cancellation is DELETE on the run resource. This asserted
        # POST /agents/runs/{id}/cancel, a path the API has never had, so it
        # confirmed a 404-ing method rather than catching it.
        assert seen == {"method": "DELETE", "path": "/agents/runs/r1"}


# ---------------------------------------------------------------------------
# Agent Input Uploads
# ---------------------------------------------------------------------------


class TestAgentInputUploads:
    def test_upload_agent_input(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            ct = req.headers.get("content-type", "")
            seen["has_multipart"] = "multipart/form-data" in ct
            return _json_response({"upload_id": "u1"})

        client = _sync_client(handler)
        result = client.upload_agent_input("a1", file=b"hello", file_name="test.txt")
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/a1/upload-input"
        assert seen["has_multipart"] is True
        assert result["upload_id"] == "u1"

    def test_get_agent_input_upload_status(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"upload_id": "u1", "status": "completed"})

        client = _sync_client(handler)
        client.get_agent_input_upload_status("a1", "u1")
        assert seen == {"method": "GET", "path": "/agents/a1/input-uploads/u1"}

    def test_get_agent_attachment_references(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"requires_uploads": False})

        client = _sync_client(handler)
        result = client.get_agent_attachment_references("a1")
        assert seen == {"method": "GET", "path": "/agents/a1/attachment-references"}
        assert result["requires_uploads"] is False

    def test_download_agent_run_attachment(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["download_name"] = req.url.params.get("download_name")
            return httpx.Response(status_code=200, content=b"file-bytes")

        client = _sync_client(handler)
        resp = client.download_agent_run_attachment(
            "r1", "att1", download_name="report.pdf"
        )
        assert seen == {
            "method": "GET",
            "path": "/v2/agent-runs/r1/attachments/att1",
            "download_name": "report.pdf",
        }
        resp.read()
        assert resp.content == b"file-bytes"
        resp.close()

    def test_download_agent_run_attachment_error_closes_stream(self) -> None:
        """On an error status the streaming response is closed before raising."""
        from seclai import SeclaiAPIStatusError

        captured: dict[str, httpx.Response] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            resp = httpx.Response(status_code=404, content=b"not found")
            captured["resp"] = resp
            return resp

        client = _sync_client(handler)
        with pytest.raises(SeclaiAPIStatusError) as exc:
            client.download_agent_run_attachment("r1", "missing")
        # Body was read so the error carries detail, and the stream is released.
        assert exc.value.status_code == 404
        assert captured["resp"].is_closed


# ---------------------------------------------------------------------------
# Agent AI Assistant
# ---------------------------------------------------------------------------


class TestAgentAIAssistant:
    def test_generate_agent_steps(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"steps": []})

        client = _sync_client(handler)
        client.generate_agent_steps("a1", {"user_input": "Build a chatbot"})
        assert seen == {
            "method": "POST",
            "path": "/agents/a1/ai-assistant/generate-steps",
        }

    def test_generate_step_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"config": {}})

        client = _sync_client(handler)
        client.generate_step_config("a1", {"step_type": "llm"})
        assert seen == {"method": "POST", "path": "/agents/a1/ai-assistant/step-config"}

    def test_get_agent_ai_conversation_history(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["query"] = dict(req.url.params)
            return _json_response({"conversations": []})

        client = _sync_client(handler)
        client.get_agent_ai_conversation_history("a1", step_type="llm", limit=5)
        assert seen["path"] == "/agents/a1/ai-assistant/conversations"
        # The API marks step_type required; asserting only the path is what let
        # this method ship unable to send it.
        assert seen["query"] == {"step_type": "llm", "limit": "5"}

    def test_get_agent_ai_conversation_history_requires_step_type(self) -> None:
        client = _sync_client(lambda req: _json_response({"conversations": []}))
        with pytest.raises(ValueError, match="step_type is required"):
            client.get_agent_ai_conversation_history("a1")

    def test_mark_agent_ai_suggestion(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.mark_agent_ai_suggestion("a1", "c1", {"accepted": True})
        assert seen == {"method": "PATCH", "path": "/agents/a1/ai-assistant/c1"}


# ---------------------------------------------------------------------------
# Agent Evaluations
# ---------------------------------------------------------------------------


class TestAgentEvaluations:
    def test_list_evaluation_criteria(self) -> None:
        # Asserting only the path let the 2026-07 change through: the endpoint
        # started returning a paginated envelope instead of a bare list and this
        # test, which discarded the body, stayed green while callers broke.
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["query"] = dict(req.url.params)
            return _json_response(
                {
                    "data": [{"id": "ec1"}],
                    "pagination": {
                        "page": 2,
                        "limit": 25,
                        "total": 7,
                        "pages": 1,
                        "has_next": False,
                        "has_prev": True,
                    },
                }
            )

        client = _sync_client(handler)
        result = client.list_evaluation_criteria("a1", page=2, limit=25)
        assert seen["path"] == "/agents/a1/evaluation-criteria"
        assert seen["query"] == {"page": "2", "limit": "25"}
        assert result == [{"id": "ec1"}]

    def test_list_evaluation_criteria_accepts_a_bare_list(self) -> None:
        # The endpoint answered with a bare array before 2026-07 and that change
        # is not deployed yet, so both shapes are live. Decoding only one breaks
        # the client the day the other ships.
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response([{"id": "ec1"}])

        client = _sync_client(handler)
        assert client.list_evaluation_criteria("a1") == [{"id": "ec1"}]

    def test_list_evaluation_criteria_page_exposes_metadata(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response(
                {
                    "data": [{"id": "ec1"}],
                    "pagination": {
                        "page": 2,
                        "limit": 25,
                        "total": 7,
                        "pages": 1,
                        "has_next": False,
                        "has_prev": True,
                    },
                }
            )

        client = _sync_client(handler)
        page = client.list_evaluation_criteria_page("a1", page=2, limit=25)
        assert page["data"] == [{"id": "ec1"}]
        assert page["pagination"]["total"] == 7

    def test_create_evaluation_criteria(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "ec1"})

        client = _sync_client(handler)
        client.create_evaluation_criteria("a1", {"name": "accuracy"})
        assert seen == {"method": "POST", "path": "/agents/a1/evaluation-criteria"}

    def test_get_evaluation_criteria(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "ec1"})

        client = _sync_client(handler)
        client.get_evaluation_criteria("ec1")
        assert seen["path"] == "/agents/evaluation-criteria/ec1"

    def test_update_evaluation_criteria(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "ec1"})

        client = _sync_client(handler)
        client.update_evaluation_criteria("ec1", {"name": "updated"})
        assert seen == {"method": "PATCH", "path": "/agents/evaluation-criteria/ec1"}

    def test_delete_evaluation_criteria(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_evaluation_criteria("ec1")
        assert seen == {"method": "DELETE", "path": "/agents/evaluation-criteria/ec1"}

    def test_get_evaluation_criteria_summary(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"total": 5})

        client = _sync_client(handler)
        client.get_evaluation_criteria_summary("ec1")
        assert seen["path"] == "/agents/evaluation-criteria/ec1/summary"

    def test_list_evaluation_results(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_evaluation_results("ec1")
        assert seen["path"] == "/agents/evaluation-criteria/ec1/results"

    def test_create_evaluation_result(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "er1"})

        client = _sync_client(handler)
        client.create_evaluation_result("ec1", {"run_id": "r1", "score": 0.9})
        assert seen == {
            "method": "POST",
            "path": "/agents/evaluation-criteria/ec1/results",
        }

    def test_list_compatible_runs(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_compatible_runs("ec1")
        assert seen["path"] == "/agents/evaluation-criteria/ec1/compatible-runs"

    def test_test_draft_evaluation(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"score": 0.8})

        client = _sync_client(handler)
        client.test_draft_evaluation("a1", {"criteria": {}, "run_id": "r1"})
        assert seen == {
            "method": "POST",
            "path": "/agents/a1/evaluation-criteria/test-draft",
        }

    def test_list_agent_evaluation_results(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_agent_evaluation_results("a1")
        assert seen["path"] == "/agents/a1/evaluation-results"

    def test_list_run_evaluation_results(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            # A bare array: the legacy shape this endpoint actually returns. The
            # previous fixture used `{"items": []}`, a shape the API never sends,
            # and passed only because the unwrap helper failed open.
            return _json_response([{"id": "er1"}])

        client = _sync_client(handler)
        result = client.list_run_evaluation_results("a1", "r1")
        assert seen["path"] == "/agents/a1/runs/r1/evaluation-results"
        assert result == [{"id": "er1"}]

    def test_list_evaluation_runs(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_evaluation_runs("a1")
        assert seen["path"] == "/agents/a1/evaluation-runs"

    def test_get_non_manual_evaluation_summary(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["agent_id"] = req.url.params.get("agent_id")
            return _json_response({"total": 0})

        client = _sync_client(handler)
        client.get_non_manual_evaluation_summary("a1")
        assert seen["path"] == "/agents/evaluation-results/non-manual-summary"
        assert seen["agent_id"] == "a1"


# ---------------------------------------------------------------------------
# Knowledge Bases
# ---------------------------------------------------------------------------


class TestKnowledgeBases:
    def test_list_knowledge_bases(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_knowledge_bases()
        assert seen == {"method": "GET", "path": "/knowledge_bases"}

    def test_create_knowledge_base(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "kb1"})

        client = _sync_client(handler)
        client.create_knowledge_base({"name": "KB"})
        assert seen == {"method": "POST", "path": "/knowledge_bases"}

    def test_get_knowledge_base(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "kb1"})

        client = _sync_client(handler)
        client.get_knowledge_base("kb1")
        assert seen["path"] == "/knowledge_bases/kb1"

    def test_update_knowledge_base(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "kb1"})

        client = _sync_client(handler)
        client.update_knowledge_base("kb1", {"name": "Updated"})
        assert seen == {"method": "PUT", "path": "/knowledge_bases/kb1"}

    def test_delete_knowledge_base(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_knowledge_base("kb1")
        assert seen == {"method": "DELETE", "path": "/knowledge_bases/kb1"}


# ---------------------------------------------------------------------------
# Memory Banks
# ---------------------------------------------------------------------------


class TestMemoryBanks:
    def test_list_memory_banks(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_memory_banks()
        assert seen["path"] == "/memory_banks"

    def test_create_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "mb1"})

        client = _sync_client(handler)
        client.create_memory_bank({"name": "MB", "type": "conversation"})
        assert seen == {"method": "POST", "path": "/memory_banks"}

    def test_get_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "mb1"})

        client = _sync_client(handler)
        client.get_memory_bank("mb1")
        assert seen["path"] == "/memory_banks/mb1"

    def test_update_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "mb1"})

        client = _sync_client(handler)
        client.update_memory_bank("mb1", {"name": "Updated"})
        assert seen == {"method": "PUT", "path": "/memory_banks/mb1"}

    def test_delete_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_memory_bank("mb1")
        assert seen == {"method": "DELETE", "path": "/memory_banks/mb1"}

    def test_get_agents_using_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response([])

        client = _sync_client(handler)
        client.get_agents_using_memory_bank("mb1")
        assert seen["path"] == "/memory_banks/mb1/agents"

    def test_get_memory_bank_stats(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"entries": 0})

        client = _sync_client(handler)
        client.get_memory_bank_stats("mb1")
        assert seen["path"] == "/memory_banks/mb1/stats"

    def test_compact_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.compact_memory_bank("mb1")
        assert seen == {"method": "POST", "path": "/memory_banks/mb1/compact"}

    def test_delete_memory_bank_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_memory_bank_source("mb1")
        assert seen == {"method": "DELETE", "path": "/memory_banks/mb1/source"}

    def test_test_memory_bank_compaction(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"result": "ok"})

        client = _sync_client(handler)
        client.test_memory_bank_compaction("mb1", {"entries": []})
        assert seen == {"method": "POST", "path": "/memory_banks/mb1/test-compaction"}

    def test_test_compaction_prompt_standalone(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"result": "ok"})

        client = _sync_client(handler)
        client.test_compaction_prompt_standalone({"prompt": "test"})
        assert seen == {"method": "POST", "path": "/memory_banks/test-compaction"}

    def test_list_memory_bank_templates(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response([])

        client = _sync_client(handler)
        client.list_memory_bank_templates()
        assert seen["path"] == "/memory_banks/templates"

    def test_generate_memory_bank_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"config": {}})

        client = _sync_client(handler)
        client.generate_memory_bank_config({"user_input": "Create a bank"})
        assert seen == {"method": "POST", "path": "/memory_banks/ai-assistant"}


# ---------------------------------------------------------------------------
# Sources (additional)
# ---------------------------------------------------------------------------


class TestSourcesAdditional:
    def test_create_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "s1"})

        client = _sync_client(handler)
        client.create_source({"name": "S1"})
        assert seen == {"method": "POST", "path": "/sources"}

    def test_get_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "s1"})

        client = _sync_client(handler)
        client.get_source("s1")
        assert seen["path"] == "/sources/s1"

    def test_update_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "s1"})

        client = _sync_client(handler)
        client.update_source("s1", {"name": "Updated"})
        assert seen == {"method": "PUT", "path": "/sources/s1"}

    def test_delete_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_source("s1")
        assert seen == {"method": "DELETE", "path": "/sources/s1"}

    def test_upload_inline_text_to_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "c1"})

        client = _sync_client(handler)
        client.upload_inline_text_to_source("sc1", {"title": "T", "content": "C"})
        assert seen == {"method": "POST", "path": "/sources/sc1"}


# ---------------------------------------------------------------------------
# Source Exports
# ---------------------------------------------------------------------------


class TestSourceExports:
    def test_list_source_exports(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_source_exports("s1")
        assert seen["path"] == "/sources/s1/exports"

    def test_create_source_export(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "e1"})

        client = _sync_client(handler)
        client.create_source_export("s1", {"format": "json"})
        assert seen == {"method": "POST", "path": "/sources/s1/exports"}

    def test_get_source_export(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "e1"})

        client = _sync_client(handler)
        client.get_source_export("s1", "e1")
        assert seen["path"] == "/sources/s1/exports/e1"

    def test_cancel_source_export(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "e1", "status": "cancelled"})

        client = _sync_client(handler)
        client.cancel_source_export("s1", "e1")
        assert seen == {"method": "POST", "path": "/sources/s1/exports/e1/cancel"}

    def test_delete_source_export(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_source_export("s1", "e1")
        assert seen == {"method": "DELETE", "path": "/sources/s1/exports/e1"}

    def test_download_source_export(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=200, content=b"csv-data")

        client = _sync_client(handler)
        resp = client.download_source_export("s1", "e1")
        assert seen == {"method": "GET", "path": "/sources/s1/exports/e1/download"}
        resp.read()
        assert resp.content == b"csv-data"
        resp.close()

    def test_estimate_source_export(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"estimated_bytes": 1024})

        client = _sync_client(handler)
        client.estimate_source_export("s1", {"format": "json"})
        assert seen == {"method": "POST", "path": "/sources/s1/exports/estimate"}


# ---------------------------------------------------------------------------
# Source Embedding Migrations
# ---------------------------------------------------------------------------


class TestSourceEmbeddingMigrations:
    def test_get_source_embedding_migration(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"status": "idle"})

        client = _sync_client(handler)
        client.get_source_embedding_migration("s1")
        assert seen["path"] == "/sources/s1/embedding-migration"

    def test_start_source_embedding_migration(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"status": "in_progress"})

        client = _sync_client(handler)
        client.start_source_embedding_migration("s1", {"target_model": "v2"})
        assert seen == {"method": "POST", "path": "/sources/s1/embedding-migration"}

    def test_cancel_source_embedding_migration(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"status": "cancelled"})

        client = _sync_client(handler)
        client.cancel_source_embedding_migration("s1")
        assert seen == {
            "method": "POST",
            "path": "/sources/s1/embedding-migration/cancel",
        }


# ---------------------------------------------------------------------------
# Content (additional)
# ---------------------------------------------------------------------------


class TestContentAdditional:
    def test_replace_content_with_inline_text(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "cv1"})

        client = _sync_client(handler)
        client.replace_content_with_inline_text("cv1", {"title": "T", "content": "C"})
        assert seen == {"method": "PUT", "path": "/contents/cv1"}


# ---------------------------------------------------------------------------
# Solutions
# ---------------------------------------------------------------------------


class TestSolutions:
    def test_list_solutions(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_solutions()
        assert seen["path"] == "/solutions"

    def test_create_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.create_solution({"name": "Sol"})
        assert seen == {"method": "POST", "path": "/solutions"}

    def test_get_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.get_solution("sol1")
        assert seen["path"] == "/solutions/sol1"

    def test_update_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.update_solution("sol1", {"name": "Updated"})
        assert seen == {"method": "PATCH", "path": "/solutions/sol1"}

    def test_delete_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_solution("sol1")
        assert seen == {"method": "DELETE", "path": "/solutions/sol1"}

    def test_link_agents_to_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.link_agents_to_solution("sol1", {"agent_ids": ["a1"]})
        assert seen == {"method": "POST", "path": "/solutions/sol1/agents"}

    def test_unlink_agents_from_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.unlink_agents_from_solution("sol1", {"agent_ids": ["a1"]})
        assert seen == {"method": "DELETE", "path": "/solutions/sol1/agents"}

    def test_link_knowledge_bases_to_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.link_knowledge_bases_to_solution("sol1", {"kb_ids": ["kb1"]})
        assert seen == {"method": "POST", "path": "/solutions/sol1/knowledge-bases"}

    def test_unlink_knowledge_bases_from_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.unlink_knowledge_bases_from_solution("sol1", {"kb_ids": ["kb1"]})
        assert seen == {"method": "DELETE", "path": "/solutions/sol1/knowledge-bases"}

    def test_link_source_connections_to_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _sync_client(handler)
        client.link_source_connections_to_solution("sol1", {"sc_ids": ["sc1"]})
        assert seen == {"method": "POST", "path": "/solutions/sol1/source-connections"}

    def test_generate_solution_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _sync_client(handler)
        client.generate_solution_ai_plan("sol1", {"user_input": "Build it"})
        assert seen == {
            "method": "POST",
            "path": "/solutions/sol1/ai-assistant/generate",
        }

    def test_accept_solution_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"result": "applied"})

        client = _sync_client(handler)
        client.accept_solution_ai_plan("sol1", "c1", {})
        assert seen == {
            "method": "POST",
            "path": "/solutions/sol1/ai-assistant/c1/accept",
        }

    def test_decline_solution_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.decline_solution_ai_plan("sol1", "c1")
        assert seen == {
            "method": "POST",
            "path": "/solutions/sol1/ai-assistant/c1/decline",
        }


# ---------------------------------------------------------------------------
# Governance AI
# ---------------------------------------------------------------------------


class TestGovernanceAI:
    def test_generate_governance_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _sync_client(handler)
        client.generate_governance_ai_plan({"user_input": "Create a policy"})
        assert seen == {"method": "POST", "path": "/governance/ai-assistant"}

    def test_list_governance_ai_conversations(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response([])

        client = _sync_client(handler)
        client.list_governance_ai_conversations()
        assert seen["path"] == "/governance/ai-assistant/conversations"

    def test_accept_governance_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"result": "applied"})

        client = _sync_client(handler)
        client.accept_governance_ai_plan("c1")
        assert seen == {"method": "POST", "path": "/governance/ai-assistant/c1/accept"}

    def test_decline_governance_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.decline_governance_ai_plan("c1")
        assert seen == {"method": "POST", "path": "/governance/ai-assistant/c1/decline"}


# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------


class TestAlerts:
    def test_list_alerts(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_alerts()
        assert seen["path"] == "/alerts"

    def test_get_alert(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "al1"})

        client = _sync_client(handler)
        client.get_alert("al1")
        assert seen["path"] == "/alerts/al1"

    def test_change_alert_status(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "al1"})

        client = _sync_client(handler)
        client.change_alert_status("al1", {"status": "resolved"})
        assert seen == {"method": "POST", "path": "/alerts/al1/status"}

    def test_add_alert_comment(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "co1"})

        client = _sync_client(handler)
        client.add_alert_comment("al1", {"text": "Looking into it"})
        assert seen == {"method": "POST", "path": "/alerts/al1/comments"}

    def test_subscribe_to_alert(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"ok": True})

        client = _sync_client(handler)
        client.subscribe_to_alert("al1")
        assert seen == {"method": "POST", "path": "/alerts/al1/subscribe"}

    def test_unsubscribe_from_alert(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"ok": True})

        client = _sync_client(handler)
        client.unsubscribe_from_alert("al1")
        assert seen == {"method": "POST", "path": "/alerts/al1/unsubscribe"}


# ---------------------------------------------------------------------------
# Alert Configs
# ---------------------------------------------------------------------------


class TestAlertConfigs:
    def test_list_alert_configs(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_alert_configs()
        assert seen["path"] == "/alerts/configs"

    def test_create_alert_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "ac1"})

        client = _sync_client(handler)
        client.create_alert_config({"name": "Config"})
        assert seen == {"method": "POST", "path": "/alerts/configs"}

    def test_get_alert_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"id": "ac1"})

        client = _sync_client(handler)
        client.get_alert_config("ac1")
        assert seen["path"] == "/alerts/configs/ac1"

    def test_update_alert_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "ac1"})

        client = _sync_client(handler)
        client.update_alert_config("ac1", {"name": "Updated"})
        assert seen == {"method": "PATCH", "path": "/alerts/configs/ac1"}

    def test_delete_alert_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_alert_config("ac1")
        assert seen == {"method": "DELETE", "path": "/alerts/configs/ac1"}


# ---------------------------------------------------------------------------
# Alert Preferences
# ---------------------------------------------------------------------------


class TestAlertPreferences:
    def test_list_organization_alert_preferences(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"preferences": []})

        client = _sync_client(handler)
        client.list_organization_alert_preferences()
        assert seen["path"] == "/alerts/organization-preferences/list"

    def test_update_organization_alert_preference(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"ok": True})

        client = _sync_client(handler)
        client.update_organization_alert_preference(
            "org1", "anomaly", {"enabled": True}
        )
        assert seen == {
            "method": "PATCH",
            "path": "/alerts/organization-preferences/org1/anomaly",
        }


# ---------------------------------------------------------------------------
# Model Alerts
# ---------------------------------------------------------------------------


class TestModelAlerts:
    def test_list_model_alerts(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_model_alerts()
        assert seen["path"] == "/models/alerts"

    def test_mark_all_model_alerts_read(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.mark_all_model_alerts_read()
        assert seen == {"method": "POST", "path": "/models/alerts/mark-all-read"}

    def test_get_unread_model_alert_count(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"count": 3})

        client = _sync_client(handler)
        client.get_unread_model_alert_count()
        assert seen["path"] == "/models/alerts/unread-count"

    def test_mark_model_alert_read(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.mark_model_alert_read("ma1")
        assert seen == {"method": "PATCH", "path": "/models/alerts/ma1/read"}


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class TestModels:
    def test_get_model_recommendations(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"models": []})

        client = _sync_client(handler)
        client.get_model_recommendations("m1")
        assert seen["path"] == "/models/m1/recommendations"

    def test_delete_experiment(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.delete_experiment("exp1")
        assert seen == {
            "method": "DELETE",
            "path": "/models/playground/experiments/exp1",
        }


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------


class TestSearch:
    def test_search(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["q"] = req.url.params.get("q")
            seen["query"] = req.url.params.get("query")
            return _json_response({"results": []})

        client = _sync_client(handler)
        client.search(query="hello")
        assert seen["path"] == "/search"
        # The spec names this parameter `q` and marks it required; sending
        # `query` instead produced a 422 on every call.
        assert seen["q"] == "hello"
        assert seen["query"] is None


# ---------------------------------------------------------------------------
# High-level: run_streaming_agent (new generator)
# ---------------------------------------------------------------------------


class TestRunStreamingAgent:
    def test_run_streaming_agent_generator(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            assert req.url.path == "/agents/a1/runs/stream"
            init_data = json.dumps({"run_id": "r1", "status": "processing"})
            done_data = json.dumps(
                {"run_id": "r1", "status": "completed", "output": "ok"}
            )
            content = (
                f"event: init\ndata: {init_data}\n\n"
                f"event: done\ndata: {done_data}\n\n"
            ).encode()
            return httpx.Response(
                status_code=200,
                headers={"content-type": "text/event-stream"},
                content=content,
            )

        client = _sync_client(handler)
        from seclai import AgentRunStreamRequest

        events = list(
            client.run_streaming_agent(
                "a1", AgentRunStreamRequest(input="hi", metadata={})
            )
        )
        assert len(events) == 2
        assert events[0][0] == "init"
        assert events[1][0] == "done"
        assert events[1][1]["output"] == "ok"


# ---------------------------------------------------------------------------
# Async counterparts (spot-check a few resource areas)
# ---------------------------------------------------------------------------


class TestAsyncMethods:
    @pytest.mark.asyncio
    async def test_async_list_agents(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _async_client(handler)
        result = await client.list_agents()
        assert seen == {"method": "GET", "path": "/agents"}
        assert result == {"items": []}

    @pytest.mark.asyncio
    async def test_async_create_agent(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "a1"})

        client = _async_client(handler)
        result = await client.create_agent({"name": "Test"})
        assert seen == {"method": "POST", "path": "/agents"}
        assert result["id"] == "a1"

    @pytest.mark.asyncio
    async def test_async_preview_import_agent(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response({"ok": True})

        client = _async_client(handler)
        await client.preview_import_agent(
            {"agent_definition": {"agent": {"name": "n"}}}
        )
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/preview-import"
        assert seen["body"] == {"agent_definition": {"agent": {"name": "n"}}}

    @pytest.mark.asyncio
    async def test_async_delete_agent(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _async_client(handler)
        await client.delete_agent("a1")
        assert seen == {"method": "DELETE", "path": "/agents/a1"}

    @pytest.mark.asyncio
    async def test_async_list_knowledge_bases(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _async_client(handler)
        await client.list_knowledge_bases()
        assert seen["path"] == "/knowledge_bases"

    @pytest.mark.asyncio
    async def test_async_create_solution(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "sol1"})

        client = _async_client(handler)
        await client.create_solution({"name": "Sol"})
        assert seen == {"method": "POST", "path": "/solutions"}

    @pytest.mark.asyncio
    async def test_async_list_alerts(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"items": []})

        client = _async_client(handler)
        await client.list_alerts()
        assert seen["path"] == "/alerts"

    @pytest.mark.asyncio
    async def test_async_search(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["q"] = req.url.params.get("q")
            seen["query"] = req.url.params.get("query")
            return _json_response({"results": []})

        client = _async_client(handler)
        await client.search(query="test")
        assert seen["path"] == "/search"
        assert seen["q"] == "test"
        assert seen["query"] is None

    @pytest.mark.asyncio
    async def test_async_create_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "mb1"})

        client = _async_client(handler)
        await client.create_memory_bank({"name": "MB", "type": "general"})
        assert seen == {"method": "POST", "path": "/memory_banks"}

    @pytest.mark.asyncio
    async def test_async_generate_governance_ai_plan(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _async_client(handler)
        await client.generate_governance_ai_plan({"user_input": "Create policy"})
        assert seen == {"method": "POST", "path": "/governance/ai-assistant"}

    @pytest.mark.asyncio
    async def test_async_cancel_agent_run(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"status": "cancelled"})

        client = _async_client(handler)
        await client.cancel_agent_run("r1")
        assert seen == {"method": "DELETE", "path": "/agents/runs/r1"}

    @pytest.mark.asyncio
    async def test_async_get_agent_attachment_references(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"requires_uploads": True})

        client = _async_client(handler)
        result = await client.get_agent_attachment_references("a1")
        assert seen == {"method": "GET", "path": "/agents/a1/attachment-references"}
        assert result["requires_uploads"] is True

    @pytest.mark.asyncio
    async def test_async_download_agent_run_attachment(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=200, content=b"file-bytes")

        client = _async_client(handler)
        resp = await client.download_agent_run_attachment("r1", "att1")
        assert seen == {
            "method": "GET",
            "path": "/v2/agent-runs/r1/attachments/att1",
        }
        await resp.aread()
        assert resp.content == b"file-bytes"
        await resp.aclose()

    @pytest.mark.asyncio
    async def test_async_delete_experiment(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _async_client(handler)
        await client.delete_experiment("exp1")
        assert seen == {
            "method": "DELETE",
            "path": "/models/playground/experiments/exp1",
        }

    @pytest.mark.asyncio
    async def test_async_run_streaming_agent(self) -> None:
        async def handler(req: httpx.Request) -> httpx.Response:
            init_data = json.dumps({"run_id": "r1", "status": "processing"})
            done_data = json.dumps({"run_id": "r1", "status": "completed"})
            content = (
                f"event: init\ndata: {init_data}\n\n"
                f"event: done\ndata: {done_data}\n\n"
            ).encode()
            return httpx.Response(
                status_code=200,
                headers={"content-type": "text/event-stream"},
                content=content,
            )

        client = _async_client(handler)
        from seclai import AgentRunStreamRequest

        events = [
            ev
            async for ev in client.run_streaming_agent(
                "a1", AgentRunStreamRequest(input="hi", metadata={})
            )
        ]
        assert len(events) == 2
        assert events[0][0] == "init"
        assert events[1][0] == "done"

    @pytest.mark.asyncio
    async def test_async_download_source_export(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["has_api_key"] = "x-api-key" in req.headers
            return httpx.Response(status_code=200, content=b"csv-data")

        client = _async_client(handler)
        resp = await client.download_source_export("s1", "e1")
        assert seen == {
            "method": "GET",
            "path": "/sources/s1/exports/e1/download",
            "has_api_key": True,
        }
        await resp.aread()
        assert resp.content == b"csv-data"
        await resp.aclose()


# ---------------------------------------------------------------------------
# Top-level AI Assistant
# ---------------------------------------------------------------------------


class TestTopLevelAIAssistant:
    def test_submit_ai_feedback(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"ok": True})

        client = _sync_client(handler)
        client.submit_ai_feedback({"rating": 5, "comment": "Great!"})
        assert seen == {"method": "POST", "path": "/ai-assistant/feedback"}

    def test_ai_assistant_knowledge_base(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _sync_client(handler)
        client.ai_assistant_knowledge_base({"user_input": "Create a KB"})
        assert seen == {"method": "POST", "path": "/ai-assistant/knowledge-base"}

    def test_ai_assistant_source(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _sync_client(handler)
        client.ai_assistant_source({"user_input": "Create a source"})
        assert seen == {"method": "POST", "path": "/ai-assistant/source"}

    def test_ai_assistant_solution(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _sync_client(handler)
        client.ai_assistant_solution({"user_input": "Create a solution"})
        assert seen == {"method": "POST", "path": "/ai-assistant/solution"}

    def test_ai_assistant_memory_bank(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _sync_client(handler)
        client.ai_assistant_memory_bank({"user_input": "Create a bank"})
        assert seen == {"method": "POST", "path": "/ai-assistant/memory-bank"}

    def test_get_ai_assistant_memory_bank_history(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"conversations": []})

        client = _sync_client(handler)
        client.get_ai_assistant_memory_bank_history()
        assert seen["path"] == "/ai-assistant/memory-bank/last-conversation"

    def test_accept_ai_assistant_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"result": "applied"})

        client = _sync_client(handler)
        client.accept_ai_assistant_plan("c1", {"accepted": True})
        assert seen == {"method": "POST", "path": "/ai-assistant/c1/accept"}

    def test_decline_ai_assistant_plan(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        client.decline_ai_assistant_plan("c1")
        assert seen == {"method": "POST", "path": "/ai-assistant/c1/decline"}

    def test_accept_ai_memory_bank_suggestion(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"ok": True})

        client = _sync_client(handler)
        client.accept_ai_memory_bank_suggestion("c1", {"accepted": True})
        assert seen == {"method": "PATCH", "path": "/ai-assistant/memory-bank/c1"}


# ---------------------------------------------------------------------------
# Top-level AI Assistant (async)
# ---------------------------------------------------------------------------


class TestAsyncTopLevelAIAssistant:
    @pytest.mark.asyncio
    async def test_async_submit_ai_feedback(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"ok": True})

        client = _async_client(handler)
        await client.submit_ai_feedback({"rating": 5})
        assert seen == {"method": "POST", "path": "/ai-assistant/feedback"}

    @pytest.mark.asyncio
    async def test_async_ai_assistant_knowledge_base(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response({"plan": {}})

        client = _async_client(handler)
        await client.ai_assistant_knowledge_base({"user_input": "Create"})
        assert seen["path"] == "/ai-assistant/knowledge-base"

    @pytest.mark.asyncio
    async def test_async_accept_ai_assistant_plan(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"result": "applied"})

        client = _async_client(handler)
        await client.accept_ai_assistant_plan("c1", {"accepted": True})
        assert seen == {"method": "POST", "path": "/ai-assistant/c1/accept"}

    @pytest.mark.asyncio
    async def test_async_decline_ai_assistant_plan(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return httpx.Response(status_code=204)

        client = _async_client(handler)
        await client.decline_ai_assistant_plan("c1")
        assert seen == {"method": "POST", "path": "/ai-assistant/c1/decline"}


# ---------------------------------------------------------------------------
# Pagination helper
# ---------------------------------------------------------------------------


class TestPagination:
    def test_paginate_single_page(self) -> None:
        call_count = 0

        def handler(req: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            # Return fewer items than limit → single page
            return _json_response({"data": [{"id": "1"}, {"id": "2"}]})

        client = _sync_client(handler)
        items = list(client.paginate("GET", "/agents", limit=50))
        assert len(items) == 2
        assert items[0]["id"] == "1"
        assert call_count == 1

    def test_paginate_multiple_pages(self) -> None:
        call_count = 0

        def handler(req: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            page = int(req.url.params.get("page", "1"))
            if page == 1:
                return _json_response({"data": [{"id": "1"}, {"id": "2"}]})
            elif page == 2:
                return _json_response({"data": [{"id": "3"}]})
            return _json_response({"data": []})

        client = _sync_client(handler)
        items = list(client.paginate("GET", "/agents", limit=2))
        assert len(items) == 3
        assert [i["id"] for i in items] == ["1", "2", "3"]
        assert call_count == 2

    def test_paginate_empty_first_page(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response({"data": []})

        client = _sync_client(handler)
        items = list(client.paginate("GET", "/agents"))
        assert items == []

    def test_paginate_custom_items_key(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response({"items": [{"id": "1"}]})

        client = _sync_client(handler)
        items = list(client.paginate("GET", "/alerts", items_key="items"))
        assert len(items) == 1

    @pytest.mark.asyncio
    async def test_async_paginate_single_page(self) -> None:
        async def handler(req: httpx.Request) -> httpx.Response:
            return _json_response({"data": [{"id": "1"}, {"id": "2"}]})

        client = _async_client(handler)
        items = [item async for item in client.paginate("GET", "/agents", limit=50)]
        assert len(items) == 2

    @pytest.mark.asyncio
    async def test_async_paginate_multiple_pages(self) -> None:
        async def handler(req: httpx.Request) -> httpx.Response:
            page = int(req.url.params.get("page", "1"))
            if page == 1:
                return _json_response({"data": [{"id": "1"}, {"id": "2"}]})
            return _json_response({"data": [{"id": "3"}]})

        client = _async_client(handler)
        items = [item async for item in client.paginate("GET", "/agents", limit=2)]
        assert len(items) == 3


# ---------------------------------------------------------------------------
# Error edge cases
# ---------------------------------------------------------------------------


class TestErrorEdgeCases:
    def test_non_json_error_response(self) -> None:
        """Non-JSON 500 response should still raise SeclaiAPIStatusError."""
        from seclai import SeclaiAPIStatusError

        def handler(req: httpx.Request) -> httpx.Response:
            return httpx.Response(status_code=500, text="Internal Server Error")

        client = _sync_client(handler)
        with pytest.raises(SeclaiAPIStatusError) as exc:
            client.list_agents()
        assert exc.value.status_code == 500

    def test_empty_204_returns_none(self) -> None:
        """A 204 No Content should return None from request()."""

        def handler(req: httpx.Request) -> httpx.Response:
            return httpx.Response(status_code=204)

        client = _sync_client(handler)
        result = client.request("DELETE", "/agents/a1")
        assert result is None

    def test_text_response_returned_as_string(self) -> None:
        """Non-JSON 200 should return text content."""

        def handler(req: httpx.Request) -> httpx.Response:
            return httpx.Response(
                status_code=200,
                headers={"content-type": "text/plain"},
                content=b"hello text",
            )

        client = _sync_client(handler)
        result = client.request("GET", "/some/text")
        assert result == "hello text"

    def test_strip_none_removes_none_values(self) -> None:
        """_strip_none should remove None values but keep others."""
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["params"] = dict(req.url.params)
            return _json_response({"items": []})

        # Uses `status`, which the endpoint declares. This previously asserted
        # that `severity` reached the wire — a parameter GET /alerts has never
        # accepted — so the test confirmed the defect instead of catching it.
        client = _sync_client(handler)
        client.list_alerts(status=None)
        assert "status" not in seen["params"]

        client.list_alerts(status="triggered")
        assert seen["params"]["status"] == "triggered"

    def test_request_passes_custom_headers(self) -> None:
        """Per-request headers should be merged."""
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["x-custom"] = req.headers.get("x-custom")
            return _json_response({"ok": True})

        client = _sync_client(handler)
        client.request("GET", "/ping", headers={"x-custom": "val"})
        assert seen["x-custom"] == "val"

    @pytest.mark.asyncio
    async def test_async_non_json_error(self) -> None:
        from seclai import SeclaiAPIStatusError

        async def handler(req: httpx.Request) -> httpx.Response:
            return httpx.Response(status_code=502, text="Bad Gateway")

        client = _async_client(handler)
        with pytest.raises(SeclaiAPIStatusError) as exc:
            await client.list_agents()
        assert exc.value.status_code == 502


# ---------------------------------------------------------------------------
# New in this sync: identity, agent pause, email governance, email domains,
# generation tiers, docs search
# ---------------------------------------------------------------------------


class TestIdentity:
    """Identity."""

    def test_get_me(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                {"account_id": "acct_1", "organizations": []}, status=200
            )

        client = _sync_client(handler)
        result = client.get_me()
        assert seen["method"] == "GET"
        assert seen["path"] == "/me"
        assert result == {"account_id": "acct_1", "organizations": []}

    @pytest.mark.asyncio
    async def test_async_get_me(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                {"account_id": "acct_1", "organizations": []}, status=200
            )

        client = _async_client(handler)
        result = await client.get_me()
        assert seen["method"] == "GET"
        assert seen["path"] == "/me"
        assert result == {"account_id": "acct_1", "organizations": []}


class TestAgentEnableDisable:
    """Agents — enable / disable."""

    def test_disable_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "a1", "disabled": True}, status=200)

        client = _sync_client(handler)
        result = client.disable_agent("a1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/a1/disable"
        assert result == {"id": "a1", "disabled": True}

    def test_enable_agent(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "a1", "disabled": False}, status=200)

        client = _sync_client(handler)
        result = client.enable_agent("a1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/a1/enable"
        assert result == {"id": "a1", "disabled": False}

    def test_get_agent_callers(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                [{"id": "a2", "name": "Caller", "disabled": False}], status=200
            )

        client = _sync_client(handler)
        result = client.get_agent_callers("a1")
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/a1/callers"
        assert result == [{"id": "a2", "name": "Caller", "disabled": False}]

    @pytest.mark.asyncio
    async def test_async_disable_agent(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "a1", "disabled": True}, status=200)

        client = _async_client(handler)
        result = await client.disable_agent("a1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/a1/disable"
        assert result == {"id": "a1", "disabled": True}

    @pytest.mark.asyncio
    async def test_async_enable_agent(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "a1", "disabled": False}, status=200)

        client = _async_client(handler)
        result = await client.enable_agent("a1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/a1/enable"
        assert result == {"id": "a1", "disabled": False}

    @pytest.mark.asyncio
    async def test_async_get_agent_callers(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                [{"id": "a2", "name": "Caller", "disabled": False}], status=200
            )

        client = _async_client(handler)
        result = await client.get_agent_callers("a1")
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/a1/callers"
        assert result == [{"id": "a2", "name": "Caller", "disabled": False}]


class TestAgentEmailTriggers:
    """Agent email triggers."""

    def test_set_email_trigger_config(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {
                    "trigger_id": "t1",
                    "agent_id": "a1",
                    "email_addresses": ["support.acct@agent.seclai.com"],
                },
                status=200,
            )

        client = _sync_client(handler)
        result = client.set_email_trigger_config("a1", "t1", {"alias": "support"})
        assert seen["method"] == "PUT"
        assert seen["path"] == "/agents/a1/triggers/t1/email-config"
        assert seen["body"] == {"alias": "support"}
        assert result == {
            "trigger_id": "t1",
            "agent_id": "a1",
            "email_addresses": ["support.acct@agent.seclai.com"],
        }

    @pytest.mark.asyncio
    async def test_async_set_email_trigger_config(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {
                    "trigger_id": "t1",
                    "agent_id": "a1",
                    "email_addresses": ["support.acct@agent.seclai.com"],
                },
                status=200,
            )

        client = _async_client(handler)
        result = await client.set_email_trigger_config("a1", "t1", {"alias": "support"})
        assert seen["method"] == "PUT"
        assert seen["path"] == "/agents/a1/triggers/t1/email-config"
        assert seen["body"] == {"alias": "support"}
        assert result == {
            "trigger_id": "t1",
            "agent_id": "a1",
            "email_addresses": ["support.acct@agent.seclai.com"],
        }


class TestAgentEmailGovernance:
    """Agent email governance."""

    def test_list_agent_email_optouts(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"items": [], "total": 0}, status=200)

        client = _sync_client(handler)
        result = client.list_agent_email_optouts(agent_id="a1", limit=25, offset=50)
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/agent-email-optouts"
        assert seen["params"] == {"agent_id": "a1", "limit": "25", "offset": "50"}
        assert result == {"items": [], "total": 0}

    def test_list_agent_email_optouts_omits_unset(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"items": [], "total": 0}, status=200)

        client = _sync_client(handler)
        result = client.list_agent_email_optouts()
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/agent-email-optouts"
        assert seen["params"] == {}
        assert result == {"items": [], "total": 0}

    def test_remove_agent_email_optout(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(None, status=204)

        client = _sync_client(handler)
        client.remove_agent_email_optout("oo1")
        assert seen["method"] == "DELETE"
        assert seen["path"] == "/agents/agent-email-optouts/oo1"

    def test_list_blocked_email_senders(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response(
                {"items": [], "total": 0, "auto_block_mode": "disabled"}, status=200
            )

        client = _sync_client(handler)
        result = client.list_blocked_email_senders(limit=10)
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/blocked-email-senders"
        assert seen["params"] == {"limit": "10"}
        assert result == {"items": [], "total": 0, "auto_block_mode": "disabled"}

    def test_block_email_sender(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {
                    "id": "b1",
                    "sender_email": "spam@example.com",
                    "match_type": "domain",
                },
                status=201,
            )

        client = _sync_client(handler)
        result = client.block_email_sender(
            {"sender_email": "spam@example.com", "match_type": "domain"}
        )
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/blocked-email-senders"
        assert seen["body"]["match_type"] == "domain"
        assert result == {
            "id": "b1",
            "sender_email": "spam@example.com",
            "match_type": "domain",
        }

    def test_unblock_email_sender(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(None, status=204)

        client = _sync_client(handler)
        client.unblock_email_sender("b1")
        assert seen["method"] == "DELETE"
        assert seen["path"] == "/agents/blocked-email-senders/b1"

    def test_set_auto_block_mode(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {"items": [], "total": 0, "auto_block_mode": "input_and_output"},
                status=200,
            )

        client = _sync_client(handler)
        result = client.set_auto_block_mode({"mode": "input_and_output"})
        assert seen["method"] == "PUT"
        assert seen["path"] == "/agents/blocked-email-senders/mode"
        assert seen["body"] == {"mode": "input_and_output"}
        assert result == {
            "items": [],
            "total": 0,
            "auto_block_mode": "input_and_output",
        }

    def test_list_inbound_email_rejections(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response(
                [{"id": "r1", "reason": "unauthorized_sender"}], status=200
            )

        client = _sync_client(handler)
        result = client.list_inbound_email_rejections(agent_id="a1", limit=5)
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/inbound-email-rejections"
        assert seen["params"] == {"agent_id": "a1", "limit": "5"}
        assert result == [{"id": "r1", "reason": "unauthorized_sender"}]

    def test_get_inbound_email_status(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"paused": True, "queued_backlog": 42}, status=200)

        client = _sync_client(handler)
        result = client.get_inbound_email_status()
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/inbound-email-status"
        assert result == {"paused": True, "queued_backlog": 42}

    def test_cancel_queued_email_runs(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"cancelled": 7}, status=200)

        client = _sync_client(handler)
        result = client.cancel_queued_email_runs()
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/inbound-email-status/cancel-queued"
        assert result == {"cancelled": 7}

    def test_resume_inbound_email(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"resumed": True}, status=200)

        client = _sync_client(handler)
        result = client.resume_inbound_email()
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/inbound-email-status/resume"
        assert result == {"resumed": True}

    @pytest.mark.asyncio
    async def test_async_list_agent_email_optouts(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"items": [], "total": 0}, status=200)

        client = _async_client(handler)
        result = await client.list_agent_email_optouts(
            agent_id="a1", limit=25, offset=50
        )
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/agent-email-optouts"
        assert seen["params"] == {"agent_id": "a1", "limit": "25", "offset": "50"}
        assert result == {"items": [], "total": 0}

    @pytest.mark.asyncio
    async def test_async_list_agent_email_optouts_omits_unset(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"items": [], "total": 0}, status=200)

        client = _async_client(handler)
        result = await client.list_agent_email_optouts()
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/agent-email-optouts"
        assert seen["params"] == {}
        assert result == {"items": [], "total": 0}

    @pytest.mark.asyncio
    async def test_async_remove_agent_email_optout(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(None, status=204)

        client = _async_client(handler)
        await client.remove_agent_email_optout("oo1")
        assert seen["method"] == "DELETE"
        assert seen["path"] == "/agents/agent-email-optouts/oo1"

    @pytest.mark.asyncio
    async def test_async_list_blocked_email_senders(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response(
                {"items": [], "total": 0, "auto_block_mode": "disabled"}, status=200
            )

        client = _async_client(handler)
        result = await client.list_blocked_email_senders(limit=10)
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/blocked-email-senders"
        assert seen["params"] == {"limit": "10"}
        assert result == {"items": [], "total": 0, "auto_block_mode": "disabled"}

    @pytest.mark.asyncio
    async def test_async_block_email_sender(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {
                    "id": "b1",
                    "sender_email": "spam@example.com",
                    "match_type": "domain",
                },
                status=201,
            )

        client = _async_client(handler)
        result = await client.block_email_sender(
            {"sender_email": "spam@example.com", "match_type": "domain"}
        )
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/blocked-email-senders"
        assert seen["body"]["match_type"] == "domain"
        assert result == {
            "id": "b1",
            "sender_email": "spam@example.com",
            "match_type": "domain",
        }

    @pytest.mark.asyncio
    async def test_async_unblock_email_sender(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(None, status=204)

        client = _async_client(handler)
        await client.unblock_email_sender("b1")
        assert seen["method"] == "DELETE"
        assert seen["path"] == "/agents/blocked-email-senders/b1"

    @pytest.mark.asyncio
    async def test_async_set_auto_block_mode(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {"items": [], "total": 0, "auto_block_mode": "input_and_output"},
                status=200,
            )

        client = _async_client(handler)
        result = await client.set_auto_block_mode({"mode": "input_and_output"})
        assert seen["method"] == "PUT"
        assert seen["path"] == "/agents/blocked-email-senders/mode"
        assert seen["body"] == {"mode": "input_and_output"}
        assert result == {
            "items": [],
            "total": 0,
            "auto_block_mode": "input_and_output",
        }

    @pytest.mark.asyncio
    async def test_async_list_inbound_email_rejections(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response(
                [{"id": "r1", "reason": "unauthorized_sender"}], status=200
            )

        client = _async_client(handler)
        result = await client.list_inbound_email_rejections(agent_id="a1", limit=5)
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/inbound-email-rejections"
        assert seen["params"] == {"agent_id": "a1", "limit": "5"}
        assert result == [{"id": "r1", "reason": "unauthorized_sender"}]

    @pytest.mark.asyncio
    async def test_async_get_inbound_email_status(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"paused": True, "queued_backlog": 42}, status=200)

        client = _async_client(handler)
        result = await client.get_inbound_email_status()
        assert seen["method"] == "GET"
        assert seen["path"] == "/agents/inbound-email-status"
        assert result == {"paused": True, "queued_backlog": 42}

    @pytest.mark.asyncio
    async def test_async_cancel_queued_email_runs(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"cancelled": 7}, status=200)

        client = _async_client(handler)
        result = await client.cancel_queued_email_runs()
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/inbound-email-status/cancel-queued"
        assert result == {"cancelled": 7}

    @pytest.mark.asyncio
    async def test_async_resume_inbound_email(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"resumed": True}, status=200)

        client = _async_client(handler)
        result = await client.resume_inbound_email()
        assert seen["method"] == "POST"
        assert seen["path"] == "/agents/inbound-email-status/resume"
        assert result == {"resumed": True}


class TestEmailDomains:
    """Email domains."""

    def test_list_email_domains(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"domains": [], "can_add_vanity": True}, status=200)

        client = _sync_client(handler)
        result = client.list_email_domains()
        assert seen["method"] == "GET"
        assert seen["path"] == "/email-domains"
        assert result == {"domains": [], "can_add_vanity": True}

    def test_add_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {"id": "d1", "domain": "agent.example.com", "kind": "custom"},
                status=200,
            )

        client = _sync_client(handler)
        result = client.add_email_domain(
            {"kind": "custom", "value": "agent.example.com", "delegated": True}
        )
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains"
        assert seen["body"]["delegated"] is True
        assert result == {"id": "d1", "domain": "agent.example.com", "kind": "custom"}

    def test_add_email_domain_vanity_without_delegated(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {"id": "d2", "domain": "acme.seclai.com", "kind": "vanity"}, status=200
            )

        client = _sync_client(handler)
        result = client.add_email_domain({"kind": "vanity", "value": "acme"})
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains"
        assert "delegated" not in seen["body"]
        assert result == {"id": "d2", "domain": "acme.seclai.com", "kind": "vanity"}

    def test_remove_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                {"removed": True, "cleanup_note": "Delete the NS record"}, status=200
            )

        client = _sync_client(handler)
        result = client.remove_email_domain("d1")
        assert seen["method"] == "DELETE"
        assert seen["path"] == "/email-domains/d1"
        assert result == {"removed": True, "cleanup_note": "Delete the NS record"}

    def test_verify_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                {"id": "d1", "status": "verified", "verified": True}, status=200
            )

        client = _sync_client(handler)
        result = client.verify_email_domain("d1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/d1/verify"
        assert result == {"id": "d1", "status": "verified", "verified": True}

    def test_set_primary_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "d1", "is_primary": True}, status=200)

        client = _sync_client(handler)
        result = client.set_primary_email_domain("d1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/d1/primary"
        assert result == {"id": "d1", "is_primary": True}

    def test_use_shared_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(None, status=204)

        client = _sync_client(handler)
        client.use_shared_email_domain()
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/use-shared-domain"

    def test_send_email_domain_test_email(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"sent": True}, status=200)

        client = _sync_client(handler)
        result = client.send_email_domain_test_email("d1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/d1/test-email"
        assert result == {"sent": True}

    def test_get_dmarc_summary(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response(
                {"window_days": 7, "report_count": 2, "total_messages": 100}, status=200
            )

        client = _sync_client(handler)
        result = client.get_dmarc_summary("d1", days=7, top_sources=3)
        assert seen["method"] == "GET"
        assert seen["path"] == "/email-domains/d1/dmarc"
        assert seen["params"] == {"days": "7", "top_sources": "3"}
        assert result == {"window_days": 7, "report_count": 2, "total_messages": 100}

    @pytest.mark.asyncio
    async def test_async_list_email_domains(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"domains": [], "can_add_vanity": True}, status=200)

        client = _async_client(handler)
        result = await client.list_email_domains()
        assert seen["method"] == "GET"
        assert seen["path"] == "/email-domains"
        assert result == {"domains": [], "can_add_vanity": True}

    @pytest.mark.asyncio
    async def test_async_add_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {"id": "d1", "domain": "agent.example.com", "kind": "custom"},
                status=200,
            )

        client = _async_client(handler)
        result = await client.add_email_domain(
            {"kind": "custom", "value": "agent.example.com", "delegated": True}
        )
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains"
        assert seen["body"]["delegated"] is True
        assert result == {"id": "d1", "domain": "agent.example.com", "kind": "custom"}

    @pytest.mark.asyncio
    async def test_async_add_email_domain_vanity_without_delegated(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response(
                {"id": "d2", "domain": "acme.seclai.com", "kind": "vanity"}, status=200
            )

        client = _async_client(handler)
        result = await client.add_email_domain({"kind": "vanity", "value": "acme"})
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains"
        assert "delegated" not in seen["body"]
        assert result == {"id": "d2", "domain": "acme.seclai.com", "kind": "vanity"}

    @pytest.mark.asyncio
    async def test_async_remove_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                {"removed": True, "cleanup_note": "Delete the NS record"}, status=200
            )

        client = _async_client(handler)
        result = await client.remove_email_domain("d1")
        assert seen["method"] == "DELETE"
        assert seen["path"] == "/email-domains/d1"
        assert result == {"removed": True, "cleanup_note": "Delete the NS record"}

    @pytest.mark.asyncio
    async def test_async_verify_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(
                {"id": "d1", "status": "verified", "verified": True}, status=200
            )

        client = _async_client(handler)
        result = await client.verify_email_domain("d1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/d1/verify"
        assert result == {"id": "d1", "status": "verified", "verified": True}

    @pytest.mark.asyncio
    async def test_async_set_primary_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"id": "d1", "is_primary": True}, status=200)

        client = _async_client(handler)
        result = await client.set_primary_email_domain("d1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/d1/primary"
        assert result == {"id": "d1", "is_primary": True}

    @pytest.mark.asyncio
    async def test_async_use_shared_email_domain(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response(None, status=204)

        client = _async_client(handler)
        await client.use_shared_email_domain()
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/use-shared-domain"

    @pytest.mark.asyncio
    async def test_async_send_email_domain_test_email(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"sent": True}, status=200)

        client = _async_client(handler)
        result = await client.send_email_domain_test_email("d1")
        assert seen["method"] == "POST"
        assert seen["path"] == "/email-domains/d1/test-email"
        assert result == {"sent": True}

    @pytest.mark.asyncio
    async def test_async_get_dmarc_summary(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response(
                {"window_days": 7, "report_count": 2, "total_messages": 100}, status=200
            )

        client = _async_client(handler)
        result = await client.get_dmarc_summary("d1", days=7, top_sources=3)
        assert seen["method"] == "GET"
        assert seen["path"] == "/email-domains/d1/dmarc"
        assert seen["params"] == {"days": "7", "top_sources": "3"}
        assert result == {"window_days": 7, "report_count": 2, "total_messages": 100}


class TestGenerationTiersAndDocsSearch:
    """Generation tiers + docs search."""

    def test_get_generation_tiers(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"image": {"fast": {"model": "m1"}}}, status=200)

        client = _sync_client(handler)
        result = client.get_generation_tiers()
        assert seen["method"] == "GET"
        assert seen["path"] == "/models/generation-tiers"
        assert result == {"image": {"fast": {"model": "m1"}}}

    def test_search_docs(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"results": []}, status=200)

        client = _sync_client(handler)
        result = client.search_docs("email triggers", mode="semantic", limit=3)
        assert seen["method"] == "GET"
        assert seen["path"] == "/docs-search"
        assert seen["params"] == {
            "q": "email triggers",
            "mode": "semantic",
            "limit": "3",
        }
        assert result == {"results": []}

    def test_search_docs_omits_unset(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"results": []}, status=200)

        client = _sync_client(handler)
        result = client.search_docs("webhooks")
        assert seen["method"] == "GET"
        assert seen["path"] == "/docs-search"
        assert seen["params"] == {"q": "webhooks"}
        assert result == {"results": []}

    @pytest.mark.asyncio
    async def test_async_get_generation_tiers(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            return _json_response({"image": {"fast": {"model": "m1"}}}, status=200)

        client = _async_client(handler)
        result = await client.get_generation_tiers()
        assert seen["method"] == "GET"
        assert seen["path"] == "/models/generation-tiers"
        assert result == {"image": {"fast": {"model": "m1"}}}

    @pytest.mark.asyncio
    async def test_async_search_docs(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"results": []}, status=200)

        client = _async_client(handler)
        result = await client.search_docs("email triggers", mode="semantic", limit=3)
        assert seen["method"] == "GET"
        assert seen["path"] == "/docs-search"
        assert seen["params"] == {
            "q": "email triggers",
            "mode": "semantic",
            "limit": "3",
        }
        assert result == {"results": []}

    @pytest.mark.asyncio
    async def test_async_search_docs_omits_unset(self) -> None:
        seen: dict[str, Any] = {}

        async def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["params"] = dict(req.url.params)
            return _json_response({"results": []}, status=200)

        client = _async_client(handler)
        result = await client.search_docs("webhooks")
        assert seen["method"] == "GET"
        assert seen["path"] == "/docs-search"
        assert seen["params"] == {"q": "webhooks"}
        assert result == {"results": []}


class TestApiVersion:
    def test_version_header_omitted_unless_opted_in(self) -> None:
        # The point of the option: upgrading the SDK must not silently move an
        # account onto a newer API version and change response shapes.
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["headers"] = dict(req.headers)
            return _json_response({"data": []})

        client = _sync_client(handler)
        client.list_agents()
        assert "seclai-version" not in seen["headers"]

    def test_version_header_sent_when_set(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["headers"] = dict(req.headers)
            return _json_response({"data": []})

        client = _sync_client(handler, api_version="2026-07-27")
        client.list_agents()
        assert seen["headers"]["seclai-version"] == "2026-07-27"

    def test_caller_supplied_version_header_overrides_rather_than_duplicates(
        self,
    ) -> None:
        # httpx emits both keys if the cases differ, and the server then picks
        # one arbitrarily.
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["values"] = req.headers.get_list("seclai-version")
            return _json_response({"data": []})

        client = _sync_client(
            handler,
            api_version="2026-07-01",
            default_headers={"Seclai-Version": "2026-07-27"},
        )
        client.list_agents()
        assert seen["values"] == ["2026-07-27"]

    def test_get_api_version(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["method"] = req.method
            # All five fields the spec marks required, using versions the server
            # actually knows. The previous fixture omitted `default_version` and
            # invented `2026-01-01`, modelling a state no server can produce.
            return _json_response(
                {
                    "pinned_version": None,
                    "effective_version": "2026-07-01",
                    "default_version": "2026-07-01",
                    "latest_version": "2026-07-27",
                    "known_versions": ["2026-07-01", "2026-07-27"],
                }
            )

        client = _sync_client(handler)
        result = client.get_api_version()
        assert seen["method"] == "GET"
        assert seen["path"] == "/version"
        assert result["latest_version"] == "2026-07-27"
        assert result["default_version"] == "2026-07-01"

    def test_update_api_version_sends_explicit_null_to_clear(self) -> None:
        # null is the documented way to clear the pin, so it must reach the wire
        # rather than being dropped as an unset value.
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["method"] = req.method
            seen["path"] = req.url.path
            seen["body"] = json.loads(req.content)
            return _json_response({"pinned_version": None})

        client = _sync_client(handler)
        client.update_api_version(None)
        assert seen["method"] == "PUT"
        assert seen["path"] == "/version"
        assert seen["body"] == {"version": None}


class TestVersionGatedListShapes:
    """Endpoints whose response shape depends on the Seclai-Version header.

    The legacy shape is a bare, unpaginated array; opting in yields the canonical
    {data, pagination} envelope. Both are live, so each accessor must read both.
    """

    def test_run_evaluation_results_accepts_a_bare_array(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response([{"id": "er1"}])

        client = _sync_client(handler)
        assert client.list_run_evaluation_results("a1", "r1") == [{"id": "er1"}]

    def test_run_evaluation_results_unwraps_the_canonical_envelope(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response(
                {
                    "data": [{"id": "er1"}],
                    "pagination": {
                        "page": 1,
                        "limit": 50,
                        "total": 1,
                        "pages": 1,
                        "has_next": False,
                        "has_prev": False,
                    },
                }
            )

        client = _sync_client(handler)
        assert client.list_run_evaluation_results("a1", "r1") == [{"id": "er1"}]

    def test_run_evaluation_results_page_exposes_pagination(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response(
                {
                    "data": [{"id": "er1"}],
                    "pagination": {
                        "page": 2,
                        "limit": 25,
                        "total": 7,
                        "pages": 1,
                        "has_next": False,
                        "has_prev": True,
                    },
                }
            )

        client = _sync_client(handler)
        page = client.list_run_evaluation_results_page("a1", "r1", page=2, limit=25)
        assert page["pagination"]["total"] == 7

    def test_run_evaluation_results_page_omits_pagination_on_legacy(self) -> None:
        def handler(req: httpx.Request) -> httpx.Response:
            return _json_response([{"id": "er1"}])

        client = _sync_client(handler)
        page = client.list_run_evaluation_results_page("a1", "r1")
        assert page == {"data": [{"id": "er1"}]}
        assert "pagination" not in page


class TestUndeclaredQueryParams:
    """Params the endpoint does not declare become 422s once a caller opts in."""

    def test_list_alerts_does_not_send_severity(self) -> None:
        # GET /alerts declares no severity filter. It never filtered anything,
        # and sending it is a hard 422 under api_version 2026-07-27+.
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["query"] = dict(req.url.params)
            return _json_response({"data": []})

        client = _sync_client(handler)
        client.list_alerts(severity="high")
        assert "severity" not in seen["query"]

    def test_list_model_alerts_translates_page_to_offset(self) -> None:
        # /models/alerts declares limit/offset, not page, so page 2 used to
        # return page 1.
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["query"] = dict(req.url.params)
            return _json_response({"data": []})

        client = _sync_client(handler)
        client.list_model_alerts(page=3, limit=25)
        assert seen["query"] == {"offset": "50", "limit": "25"}
        assert "page" not in seen["query"]


class TestApiVersionConstants:
    def test_members_are_plain_strings(self) -> None:
        # StrEnum members must be usable anywhere a str is, since api_version is
        # typed `str | None` and lands straight in a header. Compared through a
        # str-typed variable: mypy rejects a direct literal comparison as
        # non-overlapping, which is a quirk of enum narrowing rather than a
        # runtime difference.
        member = seclai_versions.ApiVersion.V2026_07_27
        raw: str = "2026-07-27"
        assert member == raw
        assert member.value == raw
        assert isinstance(member, str)

    def test_default_and_latest_track_the_spec(self) -> None:
        spec = json.loads(
            (
                pathlib.Path(__file__).parent.parent / "openapi" / "seclai.openapi.json"
            ).read_text()
        )["x-seclai-versions"]
        assert seclai_versions.DEFAULT_API_VERSION == spec["default"]
        assert seclai_versions.LATEST_API_VERSION == spec["latest"]
        assert [v.value for v in seclai_versions.ApiVersion] == spec["known"]

    def test_an_unknown_version_is_rejected(self) -> None:
        # A newer server version can reshape responses, and the client would
        # mis-decode them silently rather than error. Fail closed at construction.
        with pytest.raises(seclai.SeclaiConfigurationError) as exc:
            Seclai(api_key="k", api_version="2099-01-01")
        assert "2099-01-01" in str(exc.value)
        assert "allow_unknown_api_version" in str(exc.value)

    def test_an_unknown_version_is_allowed_when_asked(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["headers"] = dict(req.headers)
            return _json_response({"data": []})

        client = _sync_client(
            handler, api_version="2099-01-01", allow_unknown_api_version=True
        )
        client.list_agents()
        assert seen["headers"]["seclai-version"] == "2099-01-01"

    def test_a_known_version_needs_no_escape_hatch(self) -> None:
        # Constructed through the helper: building a bare Seclai() here made a
        # real httpx.Client against the live base URL, inert only because the
        # test never issued a request.
        client = _sync_client(
            lambda req: _json_response({"data": []}),
            api_version=seclai_versions.LATEST_API_VERSION,
        )
        assert client._options.api_version == seclai_versions.LATEST_API_VERSION

    def test_update_api_version_rejects_an_unknown_pin(self) -> None:
        # The account pin is sticky and applies to every header-less caller on
        # the account, so it needs the guard at least as much as the header does.
        client = _sync_client(lambda req: _json_response({"pinned_version": None}))
        with pytest.raises(seclai.SeclaiConfigurationError) as exc:
            client.update_api_version("2099-01-01")
        assert "2099-01-01" in str(exc.value)

    def test_update_api_version_honours_the_escape_hatch(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["body"] = json.loads(req.content)
            return _json_response({"pinned_version": "2099-01-01"})

        client = _sync_client(handler, allow_unknown_api_version=True)
        client.update_api_version("2099-01-01")
        assert seen["body"] == {"version": "2099-01-01"}


class TestAsyncParityForNewBehaviour:
    """AsyncSeclai hand-duplicates every method, so nothing in the sync tests
    proves the async copy behaves the same. Each case here mirrors a sync test
    of behaviour added or changed in this release; a typo in one async body
    would otherwise ship green."""

    @pytest.mark.asyncio
    async def test_version_header_omitted_unless_opted_in(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["headers"] = dict(req.headers)
            return _json_response({"data": []})

        client = _async_client(handler)
        await client.list_agents()
        assert "seclai-version" not in seen["headers"]

    @pytest.mark.asyncio
    async def test_version_header_sent_when_set(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["headers"] = dict(req.headers)
            return _json_response({"data": []})

        client = _async_client(handler, api_version="2026-07-27")
        await client.list_agents()
        assert seen["headers"]["seclai-version"] == "2026-07-27"

    @pytest.mark.asyncio
    async def test_get_and_update_api_version(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen.setdefault("calls", []).append((req.method, req.url.path))
            if req.method == "PUT":
                seen["body"] = json.loads(req.content)
            return _json_response({"pinned_version": None})

        client = _async_client(handler)
        await client.get_api_version()
        await client.update_api_version(None)
        assert seen["calls"] == [("GET", "/version"), ("PUT", "/version")]
        assert seen["body"] == {"version": None}

    @pytest.mark.asyncio
    async def test_update_api_version_rejects_an_unknown_pin(self) -> None:
        client = _async_client(lambda req: _json_response({"pinned_version": None}))
        with pytest.raises(seclai.SeclaiConfigurationError):
            await client.update_api_version("2099-01-01")

    @pytest.mark.asyncio
    async def test_list_alerts_does_not_send_severity(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["query"] = dict(req.url.params)
            return _json_response({"data": []})

        client = _async_client(handler)
        await client.list_alerts(severity="high")
        assert "severity" not in seen["query"]

    @pytest.mark.asyncio
    async def test_list_model_alerts_translates_page_to_offset(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["query"] = dict(req.url.params)
            return _json_response({"alerts": []})

        client = _async_client(handler)
        await client.list_model_alerts(page=3, limit=25)
        assert seen["query"] == {"offset": "50", "limit": "25"}

    @pytest.mark.asyncio
    async def test_list_model_alerts_never_sends_a_negative_offset(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["query"] = dict(req.url.params)
            return _json_response({"alerts": []})

        client = _async_client(handler)
        await client.list_model_alerts(page=0, limit=25)
        assert seen["query"]["offset"] == "0"

    @pytest.mark.asyncio
    async def test_evaluation_criteria_accepts_either_wire_shape(self) -> None:
        legacy = _async_client(lambda req: _json_response([{"id": "ec1"}]))
        assert await legacy.list_evaluation_criteria("a1") == [{"id": "ec1"}]

        canonical = _async_client(
            lambda req: _json_response(
                {"data": [{"id": "ec1"}], "pagination": {"total": 1}}
            )
        )
        assert await canonical.list_evaluation_criteria("a1") == [{"id": "ec1"}]
        page = await canonical.list_evaluation_criteria_page("a1")
        assert page["pagination"]["total"] == 1

    @pytest.mark.asyncio
    async def test_run_evaluation_results_accepts_either_wire_shape(self) -> None:
        legacy = _async_client(lambda req: _json_response([{"id": "er1"}]))
        assert await legacy.list_run_evaluation_results("a1", "r1") == [{"id": "er1"}]

        canonical = _async_client(lambda req: _json_response({"data": [{"id": "er1"}]}))
        assert await canonical.list_run_evaluation_results("a1", "r1") == [
            {"id": "er1"}
        ]

    @pytest.mark.asyncio
    async def test_conversation_history_requires_step_type(self) -> None:
        client = _async_client(lambda req: _json_response({"conversations": []}))
        with pytest.raises(ValueError, match="step_type is required"):
            await client.get_agent_ai_conversation_history("a1")

    @pytest.mark.asyncio
    async def test_conversation_history_sends_step_type(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["query"] = dict(req.url.params)
            return _json_response({"conversations": []})

        client = _async_client(handler)
        await client.get_agent_ai_conversation_history("a1", step_type="llm")
        assert seen["query"] == {"step_type": "llm"}


class TestVersionGuardCannotBeBypassed:
    """`default_headers` is applied last so it wins, which means it can carry a
    Seclai-Version. Validating only the argument left the guard one header away
    from being bypassed."""

    def test_unknown_version_in_default_headers_is_rejected(self) -> None:
        with pytest.raises(seclai.SeclaiConfigurationError) as exc:
            Seclai(api_key="k", default_headers={"Seclai-Version": "2099-01-01"})
        assert "2099-01-01" in str(exc.value)
        assert "default_headers" in str(exc.value)

    def test_a_lowercase_header_key_is_caught_too(self) -> None:
        with pytest.raises(seclai.SeclaiConfigurationError):
            Seclai(api_key="k", default_headers={"seclai-version": "2099-01-01"})

    def test_the_escape_hatch_still_covers_the_header_form(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["values"] = req.headers.get_list("seclai-version")
            return _json_response({"data": []})

        client = _sync_client(
            handler,
            default_headers={"Seclai-Version": "2099-01-01"},
            allow_unknown_api_version=True,
        )
        client.list_agents()
        assert seen["values"] == ["2099-01-01"]

    def test_a_known_version_in_default_headers_needs_no_escape_hatch(self) -> None:
        client = _sync_client(
            lambda req: _json_response({"data": []}),
            default_headers={"Seclai-Version": seclai_versions.LATEST_API_VERSION},
        )
        assert client is not None


class TestDuplicateVersionHeaderSpellings:
    """`default_headers` can carry two spellings of one header. The guard must
    approve the value that survives the merge, and the merge must leave one."""

    def test_a_second_spelling_cannot_slip_past_the_guard(self) -> None:
        with pytest.raises(seclai.SeclaiConfigurationError) as exc:
            Seclai(
                api_key="k",
                default_headers={
                    "Seclai-Version": seclai_versions.LATEST_API_VERSION,
                    "seclai-version": "2099-01-01",
                },
            )
        assert "2099-01-01" in str(exc.value)

    def test_only_one_value_reaches_the_wire(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["values"] = req.headers.get_list("seclai-version")
            return _json_response({"data": []})

        client = _sync_client(
            handler,
            default_headers={
                "Seclai-Version": seclai_versions.DEFAULT_API_VERSION,
                "seclai-version": seclai_versions.LATEST_API_VERSION,
            },
        )
        client.list_agents()
        assert seen["values"] == [seclai_versions.LATEST_API_VERSION]
