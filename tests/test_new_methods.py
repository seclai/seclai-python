"""Tests for all new convenience methods added to Seclai / AsyncSeclai.

Each group covers one resource area. Tests verify the correct HTTP method, path,
query parameters, and JSON body are sent via ``MockTransport``.
"""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from seclai import AsyncSeclai, Seclai

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sync_client(handler) -> Seclai:
    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(base_url="https://example.invalid", transport=transport)
    client = Seclai(api_key="test", http_client=http_client)
    # Ensure the externally-provided httpx client is closed when the SDK client closes.
    client._owns_client = True
    return client


def _async_client(handler) -> AsyncSeclai:
    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(
        base_url="https://example.invalid", transport=transport
    )
    client = AsyncSeclai(api_key="test", http_client=http_client)
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
        assert seen == {"method": "POST", "path": "/agents/runs/r1/cancel"}


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
            return _json_response({"conversations": []})

        client = _sync_client(handler)
        client.get_agent_ai_conversation_history("a1")
        assert seen["path"] == "/agents/a1/ai-assistant/conversations"

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
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            return _json_response([])

        client = _sync_client(handler)
        client.list_evaluation_criteria("a1")
        assert seen["path"] == "/agents/a1/evaluation-criteria"

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
            return _json_response({"items": []})

        client = _sync_client(handler)
        client.list_run_evaluation_results("a1", "r1")
        assert seen["path"] == "/agents/a1/runs/r1/evaluation-results"

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


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------


class TestSearch:
    def test_search(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["path"] = req.url.path
            seen["query"] = req.url.params.get("query")
            return _json_response({"results": []})

        client = _sync_client(handler)
        client.search(query="hello")
        assert seen["path"] == "/search"
        assert seen["query"] == "hello"


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
            seen["query"] = req.url.params.get("query")
            return _json_response({"results": []})

        client = _async_client(handler)
        await client.search(query="test")
        assert seen["path"] == "/search"
        assert seen["query"] == "test"

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
        assert seen == {"method": "POST", "path": "/agents/runs/r1/cancel"}

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

        client = _sync_client(handler)
        client.list_alerts(status=None, severity="high")
        assert "status" not in seen["params"]
        assert seen["params"]["severity"] == "high"

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
