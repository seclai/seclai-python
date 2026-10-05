"""Version-gated list endpoints: both wire shapes, through every method.

The API answers each of these endpoints in its default shape (a bare array, or
an object with a per-resource key) and, once the request resolves to
``Seclai-Version`` 2026-07-27 or later, as ``{data, pagination, ...extras}``.
"""

from __future__ import annotations

import pathlib
import re
from collections.abc import Callable
from typing import Any

import httpx
import pytest

import seclai.auth as auth_mod
from seclai import (
    AsyncSeclai,
    Seclai,
    SeclaiConfigurationError,
    SeclaiError,
    unwrap_items,
)

# Every `METHOD path` the API serves through `versioned_list_response`,
# `versioned_offset_list_response` or `versioned_complete_list_response`.
# Regenerate from the API repository when one is added:
#   grep -rn "versioned_.*list_response(" backend/api/src/api/routers/api/
# and read each call site's route decorator for the method and path.
GATED = [
    "GET /alerts/configs",
    "GET /alerts/organization-preferences/list",
    "GET /models/generation-tiers",
    "GET /models/alerts",
    "GET /models/playground/experiments",
    "GET /models",
    "GET /models/embedders",
    "GET /models/rerankers",
    "GET /agents/inbound-email-rejections",
    "GET /agents/agent-email-optouts",
    "GET /agents/blocked-email-senders",
    "PUT /agents/blocked-email-senders/mode",
    "GET /agents/{agent_id}/callers",
    "GET /cloud-drives/providers",
    "GET /cloud-drives",
    "GET /cloud-drives/{connection_id}/agents",
    "GET /cloud-drives/{connection_id}/rejections",
    "GET /agents/{agent_id}/evaluation-criteria",
    "GET /agents/evaluation-criteria/{criteria_id}/results",
    "GET /agents/{agent_id}/runs/{run_id}/evaluation-results",
    "GET /agents/{agent_id}/evaluation-runs",
    "GET /agents/{agent_id}/evaluation-results",
    "GET /agents/evaluation-criteria/{criteria_id}/compatible-runs",
    "GET /solutions/{solution_id}/conversations",
    "GET /email-domains",
    "GET /knowledge_bases",
    "GET /governance/ai-assistant/conversations",
    "GET /memory_banks/templates",
    "GET /memory_banks",
    "GET /memory_banks/{memory_bank_id}/agents",
]

ITEMS = [{"id": "a"}, {"id": "b"}]
# The single page a naturally bounded list reports once opted in.
COMPLETE = {
    "page": 1,
    "limit": 2,
    "total": 2,
    "pages": 1,
    "has_next": False,
    "has_prev": False,
}
# A real page: the SDK's default `limit=50`.
PAGED = {**COMPLETE, "limit": 50}
EMBEDDER_EXTRAS = {
    "storage_credits": [{"dimensions": 1024, "credits": 1}],
    "file_processing_credits_per_mb": 2,
    "default_model_type": "m",
    "default_dimension": 1024,
}
RERANKER_EXTRAS = {"default_model_type": "r", "search_processing_credits": 3}
DOMAIN_EXTRAS = {
    "can_add_vanity": True,
    "can_add_custom": False,
    "has_vanity": False,
    "has_custom": True,
    "vanity_plan_names": ["pro"],
    "custom_plan_names": [],
}

Call = Callable[[Any], Any]

# (method, gated pair, call, default body, opted-in body,
#  return on the default body — what 1.7.0 returned, return when opted in)
ROWS: list[tuple[str, str, Call, Any, Any, Any, Any]] = [
    (
        "list_alert_configs",
        "GET /alerts/configs",
        lambda c: c.list_alert_configs(),
        {"configs": ITEMS, "total": 2},
        {"data": ITEMS, "pagination": PAGED},
        {"configs": [{"id": "a"}, {"id": "b"}], "total": 2},
        {"data": ITEMS, "pagination": PAGED, "configs": ITEMS, "total": 2},
    ),
    (
        "list_organization_alert_preferences",
        "GET /alerts/organization-preferences/list",
        lambda c: c.list_organization_alert_preferences(),
        {"preferences": ITEMS, "total": 2},
        {"data": ITEMS, "pagination": COMPLETE},
        {"preferences": [{"id": "a"}, {"id": "b"}], "total": 2},
        {"data": ITEMS, "pagination": COMPLETE, "preferences": ITEMS, "total": 2},
    ),
    (
        "get_generation_tiers",
        "GET /models/generation-tiers",
        lambda c: c.get_generation_tiers(),
        {"tiers": ITEMS},
        {"data": ITEMS, "pagination": COMPLETE},
        {"tiers": [{"id": "a"}, {"id": "b"}]},
        {"data": ITEMS, "pagination": COMPLETE, "tiers": ITEMS},
    ),
    (
        "list_model_alerts",
        "GET /models/alerts",
        lambda c: c.list_model_alerts(),
        {"alerts": ITEMS, "total": 2},
        {"data": ITEMS, "pagination": PAGED},
        {"alerts": [{"id": "a"}, {"id": "b"}], "total": 2},
        {"data": ITEMS, "pagination": PAGED, "alerts": ITEMS, "total": 2},
    ),
    (
        "list_experiments",
        "GET /models/playground/experiments",
        lambda c: c.list_experiments(),
        {"experiments": ITEMS, "total": 2},
        {"data": ITEMS, "pagination": PAGED},
        {"experiments": [{"id": "a"}, {"id": "b"}], "total": 2},
        {"data": ITEMS, "pagination": PAGED, "experiments": ITEMS, "total": 2},
    ),
    (
        "list_models",
        "GET /models",
        lambda c: c.list_models(),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_embedding_models",
        "GET /models/embedders",
        lambda c: c.list_embedding_models(),
        {"models": ITEMS, **EMBEDDER_EXTRAS},
        {"data": ITEMS, "pagination": COMPLETE, **EMBEDDER_EXTRAS},
        {
            "models": [{"id": "a"}, {"id": "b"}],
            "storage_credits": [{"dimensions": 1024, "credits": 1}],
            "file_processing_credits_per_mb": 2,
            "default_model_type": "m",
            "default_dimension": 1024,
        },
        {"data": ITEMS, "pagination": COMPLETE, "models": ITEMS, **EMBEDDER_EXTRAS},
    ),
    (
        "list_reranker_models",
        "GET /models/rerankers",
        lambda c: c.list_reranker_models(),
        {"models": ITEMS, **RERANKER_EXTRAS},
        {"data": ITEMS, "pagination": COMPLETE, **RERANKER_EXTRAS},
        {
            "models": [{"id": "a"}, {"id": "b"}],
            "default_model_type": "r",
            "search_processing_credits": 3,
        },
        {"data": ITEMS, "pagination": COMPLETE, "models": ITEMS, **RERANKER_EXTRAS},
    ),
    (
        "list_inbound_email_rejections",
        "GET /agents/inbound-email-rejections",
        lambda c: c.list_inbound_email_rejections(),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_agent_email_optouts",
        "GET /agents/agent-email-optouts",
        lambda c: c.list_agent_email_optouts(),
        {"items": ITEMS, "total": 2},
        {"data": ITEMS, "pagination": PAGED},
        {"items": [{"id": "a"}, {"id": "b"}], "total": 2},
        {"data": ITEMS, "pagination": PAGED, "items": ITEMS, "total": 2},
    ),
    (
        "list_blocked_email_senders",
        "GET /agents/blocked-email-senders",
        lambda c: c.list_blocked_email_senders(),
        {"items": ITEMS, "total": 2, "auto_block_mode": "input"},
        {"data": ITEMS, "pagination": PAGED, "auto_block_mode": "input"},
        {"items": [{"id": "a"}, {"id": "b"}], "total": 2, "auto_block_mode": "input"},
        {
            "data": ITEMS,
            "pagination": PAGED,
            "auto_block_mode": "input",
            "items": ITEMS,
            "total": 2,
        },
    ),
    (
        "set_auto_block_mode",
        "PUT /agents/blocked-email-senders/mode",
        lambda c: c.set_auto_block_mode({"mode": "input"}),
        # By default `total` is the account's count, here larger than the rows.
        {"items": ITEMS, "total": 70, "auto_block_mode": "input"},
        {"data": ITEMS, "pagination": COMPLETE, "auto_block_mode": "input"},
        {"items": [{"id": "a"}, {"id": "b"}], "total": 70, "auto_block_mode": "input"},
        {
            "data": ITEMS,
            "pagination": COMPLETE,
            "auto_block_mode": "input",
            "items": ITEMS,
            "total": 2,
        },
    ),
    (
        "get_agent_callers",
        "GET /agents/{agent_id}/callers",
        lambda c: c.get_agent_callers("a1"),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_cloud_drive_providers",
        "GET /cloud-drives/providers",
        lambda c: c.list_cloud_drive_providers(),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_cloud_drives",
        "GET /cloud-drives",
        lambda c: c.list_cloud_drives(),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "get_agents_using_cloud_drive",
        "GET /cloud-drives/{connection_id}/agents",
        lambda c: c.get_agents_using_cloud_drive("c1"),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_cloud_drive_rejections",
        "GET /cloud-drives/{connection_id}/rejections",
        lambda c: c.list_cloud_drive_rejections("c1"),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_evaluation_criteria",
        "GET /agents/{agent_id}/evaluation-criteria",
        lambda c: c.list_evaluation_criteria("a1"),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_evaluation_criteria_page",
        "GET /agents/{agent_id}/evaluation-criteria",
        lambda c: c.list_evaluation_criteria_page("a1"),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        {"data": [{"id": "a"}, {"id": "b"}]},
        {"data": ITEMS, "pagination": PAGED},
    ),
    (
        "list_evaluation_results",
        "GET /agents/evaluation-criteria/{criteria_id}/results",
        lambda c: c.list_evaluation_results("k1"),
        {"data": ITEMS, "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED},
        {"data": [{"id": "a"}, {"id": "b"}], "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED, "total": 2, "page": 1, "limit": 50},
    ),
    (
        "list_run_evaluation_results",
        "GET /agents/{agent_id}/runs/{run_id}/evaluation-results",
        lambda c: c.list_run_evaluation_results("a1", "r1"),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_run_evaluation_results_page",
        "GET /agents/{agent_id}/runs/{run_id}/evaluation-results",
        lambda c: c.list_run_evaluation_results_page("a1", "r1"),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        {"data": [{"id": "a"}, {"id": "b"}]},
        {"data": ITEMS, "pagination": PAGED},
    ),
    (
        "list_evaluation_runs",
        "GET /agents/{agent_id}/evaluation-runs",
        lambda c: c.list_evaluation_runs("a1"),
        {"data": ITEMS, "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED},
        {"data": [{"id": "a"}, {"id": "b"}], "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED, "total": 2, "page": 1, "limit": 50},
    ),
    (
        "list_agent_evaluation_results",
        "GET /agents/{agent_id}/evaluation-results",
        lambda c: c.list_agent_evaluation_results("a1"),
        {"data": ITEMS, "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED},
        {"data": [{"id": "a"}, {"id": "b"}], "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED, "total": 2, "page": 1, "limit": 50},
    ),
    (
        "list_compatible_runs",
        "GET /agents/evaluation-criteria/{criteria_id}/compatible-runs",
        lambda c: c.list_compatible_runs("k1"),
        {"data": ITEMS, "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED},
        {"data": [{"id": "a"}, {"id": "b"}], "total": 2, "page": 1, "limit": 50},
        {"data": ITEMS, "pagination": PAGED, "total": 2, "page": 1, "limit": 50},
    ),
    (
        "list_solution_conversations",
        "GET /solutions/{solution_id}/conversations",
        lambda c: c.list_solution_conversations("s1"),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_email_domains",
        "GET /email-domains",
        lambda c: c.list_email_domains(),
        {"domains": ITEMS, **DOMAIN_EXTRAS},
        {"data": ITEMS, "pagination": COMPLETE, **DOMAIN_EXTRAS},
        {
            "domains": [{"id": "a"}, {"id": "b"}],
            "can_add_vanity": True,
            "can_add_custom": False,
            "has_vanity": False,
            "has_custom": True,
            "vanity_plan_names": ["pro"],
            "custom_plan_names": [],
        },
        {"data": ITEMS, "pagination": COMPLETE, "domains": ITEMS, **DOMAIN_EXTRAS},
    ),
    (
        "list_knowledge_bases",
        "GET /knowledge_bases",
        lambda c: c.list_knowledge_bases(),
        {"knowledge_bases": ITEMS, "page": 1, "limit": 50, "total": 2},
        {"data": ITEMS, "pagination": PAGED},
        {
            "knowledge_bases": [{"id": "a"}, {"id": "b"}],
            "page": 1,
            "limit": 50,
            "total": 2,
        },
        {
            "data": ITEMS,
            "pagination": PAGED,
            "knowledge_bases": ITEMS,
            "total": 2,
            "page": 1,
            "limit": 50,
        },
    ),
    (
        "list_governance_ai_conversations",
        "GET /governance/ai-assistant/conversations",
        lambda c: c.list_governance_ai_conversations(),
        ITEMS,
        {"data": ITEMS, "pagination": PAGED},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_memory_bank_templates",
        "GET /memory_banks/templates",
        lambda c: c.list_memory_bank_templates(),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
    (
        "list_memory_banks",
        "GET /memory_banks",
        lambda c: c.list_memory_banks(),
        {"memory_banks": ITEMS, "page": 1, "limit": 50, "total": 2},
        {"data": ITEMS, "pagination": PAGED},
        {
            "memory_banks": [{"id": "a"}, {"id": "b"}],
            "page": 1,
            "limit": 50,
            "total": 2,
        },
        {
            "data": ITEMS,
            "pagination": PAGED,
            "memory_banks": ITEMS,
            "total": 2,
            "page": 1,
            "limit": 50,
        },
    ),
    (
        "get_agents_using_memory_bank",
        "GET /memory_banks/{memory_bank_id}/agents",
        lambda c: c.get_agents_using_memory_bank("m1"),
        ITEMS,
        {"data": ITEMS, "pagination": COMPLETE},
        [{"id": "a"}, {"id": "b"}],
        ITEMS,
    ),
]
ROW_IDS = [row[0] for row in ROWS]


def _serving(pair: str, body: Any) -> Callable[[httpx.Request], httpx.Response]:
    """A handler that answers ``body``, and fails on any other ``METHOD path``."""
    method, template = pair.split(" ")
    pattern = re.compile(re.sub(r"\{[^}]+\}", "[^/]+", template) + r"\Z")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == method, request.method
        assert pattern.match(request.url.path), request.url.path
        return httpx.Response(200, json=body)

    return handler


def _sync(handler: Callable[[httpx.Request], httpx.Response], **options: Any) -> Seclai:
    http = httpx.Client(
        base_url="https://example.invalid", transport=httpx.MockTransport(handler)
    )
    options.setdefault("api_key", "test")
    client = Seclai(http_client=http, **options)
    client._owns_client = True
    return client


def _async(
    handler: Callable[[httpx.Request], httpx.Response], **options: Any
) -> AsyncSeclai:
    http = httpx.AsyncClient(
        base_url="https://example.invalid", transport=httpx.MockTransport(handler)
    )
    options.setdefault("api_key", "test")
    client = AsyncSeclai(http_client=http, **options)
    client._owns_client = True
    return client


def test_every_gated_endpoint_has_a_row() -> None:
    assert len(GATED) == len(set(GATED)) == 30
    assert {row[1] for row in ROWS} == set(GATED)


def test_every_row_names_a_method_on_both_clients() -> None:
    for name in ROW_IDS:
        assert callable(getattr(Seclai, name)), name
        assert callable(getattr(AsyncSeclai, name)), name


@pytest.mark.parametrize("row", ROWS, ids=ROW_IDS)
class TestBothShapes:
    def test_default_shape_returns_what_1_7_0_returned(self, row: Any) -> None:
        _name, pair, call, default_body, _opted, expected, _ = row
        with _sync(_serving(pair, default_body)) as client:
            assert call(client) == expected

    def test_opted_in_shape(self, row: Any) -> None:
        _name, pair, call, _default, opted_body, _, expected = row
        with _sync(_serving(pair, opted_body), api_version="2026-07-27") as client:
            assert call(client) == expected

    async def test_async_default_shape_returns_what_1_7_0_returned(
        self, row: Any
    ) -> None:
        _name, pair, call, default_body, _opted, expected, _ = row
        async with _async(_serving(pair, default_body)) as client:
            assert await call(client) == expected

    async def test_async_opted_in_shape(self, row: Any) -> None:
        _name, pair, call, _default, opted_body, _, expected = row
        async with _async(
            _serving(pair, opted_body), api_version="2026-07-27"
        ) as client:
            assert await call(client) == expected

    def test_items_are_read_the_same_way_on_both_shapes(self, row: Any) -> None:
        _name, pair, call, default_body, opted_body, _, _ = row
        results = []
        for body in (default_body, opted_body):
            with _sync(_serving(pair, body)) as client:
                results.append(call(client))
        default_result, opted_result = results
        if isinstance(default_result, list):
            assert opted_result == default_result == ITEMS
            return
        keys = [k for k, v in default_result.items() if v == ITEMS]
        assert len(keys) == 1, keys
        assert opted_result[keys[0]] == ITEMS
        # Whatever the default shape carries, the opted-in result carries too.
        assert set(default_result) <= set(opted_result)


def _response(make: Callable[[], httpx.Response]) -> Any:
    return lambda request: make()


NOT_A_LIST: list[tuple[str, Callable[[], httpx.Response]]] = [
    ("error object", lambda: httpx.Response(200, json={"error": {"code": "x"}})),
    ("detail object", lambda: httpx.Response(200, json={"detail": "boom"})),
    ("empty object", lambda: httpx.Response(200, json={})),
    ("text", lambda: httpx.Response(200, text="upstream says hi")),
    ("html", lambda: httpx.Response(200, html="<html>gateway</html>")),
    (
        "json null",
        lambda: httpx.Response(
            200, content=b"null", headers={"content-type": "application/json"}
        ),
    ),
    ("empty body", lambda: httpx.Response(200)),
    ("json string", lambda: httpx.Response(200, json="nope")),
    ("json number", lambda: httpx.Response(200, json=3)),
    ("data is a string", lambda: httpx.Response(200, json={"data": "nope"})),
    ("data is an object", lambda: httpx.Response(200, json={"data": {"id": "a"}})),
]


@pytest.mark.parametrize("row", ROWS, ids=ROW_IDS)
class TestNotAList:
    @pytest.mark.parametrize("make", [m for _, m in NOT_A_LIST], ids=[n for n, _ in NOT_A_LIST])  # fmt: skip
    def test_raises(self, row: Any, make: Callable[[], httpx.Response]) -> None:
        call = row[2]
        with _sync(_response(make)) as client, pytest.raises(SeclaiError):
            call(client)

    @pytest.mark.parametrize("make", [m for _, m in NOT_A_LIST], ids=[n for n, _ in NOT_A_LIST])  # fmt: skip
    async def test_async_raises(
        self, row: Any, make: Callable[[], httpx.Response]
    ) -> None:
        call = row[2]
        async with _async(_response(make)) as client:
            with pytest.raises(SeclaiError):
                await call(client)

    def test_documented_key_holding_a_non_list_raises(self, row: Any) -> None:
        _name, pair, call, default_body, _, _, _ = row
        if not isinstance(default_body, dict):
            pytest.skip("the default shape is a bare array")
        key = next(k for k, v in default_body.items() if v == ITEMS)
        body = {**default_body, key: "nope"}
        with _sync(_serving(pair, body)) as client, pytest.raises(SeclaiError):
            call(client)

    def test_null_data_is_an_empty_list(self, row: Any) -> None:
        _name, pair, call, default_body, _, default_result, _ = row
        with _sync(_serving(pair, {"data": None})) as client:
            result = call(client)
        if isinstance(default_result, list):
            assert result == []
        else:
            key = next(k for k, v in default_result.items() if v == ITEMS)
            assert result[key] == []


class TestKeyedPrecedence:
    """Which list a dict-returning method reads when a body carries several."""

    def _optouts(self, body: Any) -> dict[str, Any]:
        with _sync(lambda request: httpx.Response(200, json=body)) as client:
            return client.list_agent_email_optouts()

    def test_data_wins_over_the_documented_key(self) -> None:
        result = self._optouts({"data": [{"id": "d"}], "items": [{"id": "i"}]})
        assert result["items"] == [{"id": "d"}]

    def test_documented_key_is_read_when_data_is_not_a_list(self) -> None:
        for data in (None, "nope"):
            result = self._optouts({"data": data, "items": [{"id": "i"}]})
            assert result["items"] == [{"id": "i"}]

    def test_a_flat_counter_the_body_carries_is_kept(self) -> None:
        result = self._optouts({"data": [], "total": 9, "pagination": {"total": 1}})
        assert result["total"] == 9

    def test_a_missing_flat_counter_comes_from_pagination(self) -> None:
        result = self._optouts({"data": [], "pagination": {"total": 4, "page": 2}})
        assert result["total"] == 4
        # `page` is not a counter this method documents on its default shape.
        assert "page" not in result

    def test_unwrap_items_still_reads_every_result(self) -> None:
        for _name, pair, call, default_body, opted_body, _, _ in ROWS:
            for body in (default_body, opted_body):
                with _sync(_serving(pair, body)) as client:
                    result = call(client)
                keys = [] if isinstance(default_body, list) else list(default_body)
                assert unwrap_items(result, *keys[:1]) == ITEMS


AUTH_NAMES = ("authorization", "x-account-id")
SPELLED = {"Authorization": "Bearer FROM-DEFAULTS", "X-Account-Id": "FROM-DEFAULTS"}


def _credentials(request: httpx.Request) -> list[tuple[str, str]]:
    return sorted(
        (name.lower(), value)
        for name, value in request.headers.multi_items()
        if name.lower() in AUTH_NAMES
    )


@pytest.fixture
def dynamic_modes(
    monkeypatch: pytest.MonkeyPatch, tmp_path: pathlib.Path
) -> dict[str, dict[str, Any]]:
    monkeypatch.delenv("SECLAI_API_KEY", raising=False)
    monkeypatch.setenv("SECLAI_CONFIG_DIR", str(tmp_path))
    monkeypatch.setattr(auth_mod, "_resolve_sso_token_sync", lambda state: "TOKEN")

    async def resolve(state: Any) -> str:
        return "TOKEN"

    monkeypatch.setattr(auth_mod, "_resolve_sso_token_async", resolve)
    return {
        "bearer_provider": {"access_token": lambda: "TOKEN", "account_id": "ACCT"},
        "sso": {"account_id": "ACCT"},
    }


@pytest.mark.parametrize("mode", ["bearer_provider", "sso"])
class TestGeneratedClientCredentials:
    """One credential per name on the typed-method path, from the first call."""

    EXPECTED = [("authorization", "Bearer TOKEN"), ("x-account-id", "ACCT")]

    def test_sync(self, mode: str, dynamic_modes: dict[str, dict[str, Any]]) -> None:
        client = Seclai(default_headers=SPELLED, **dynamic_modes[mode])
        assert client._options.auth_state.mode == mode
        for _call in ("first", "second"):
            http = client._sync_generated_client().get_httpx_client()
            assert _credentials(http.build_request("GET", "/x")) == self.EXPECTED
        client.close()

    async def test_async(
        self, mode: str, dynamic_modes: dict[str, dict[str, Any]]
    ) -> None:
        client = AsyncSeclai(default_headers=SPELLED, **dynamic_modes[mode])
        assert client._options.auth_state.mode == mode
        for _call in ("first", "second"):
            generated = await client._async_generated_client()
            http = generated.get_async_httpx_client()
            assert _credentials(http.build_request("GET", "/x")) == self.EXPECTED
        await client.aclose()

    def test_typed_method_sends_one_of_each(
        self, mode: str, dynamic_modes: dict[str, dict[str, Any]]
    ) -> None:
        seen: list[list[tuple[str, str]]] = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(_credentials(request))
            return httpx.Response(200, json={"data": [], "pagination": PAGED})

        client = Seclai(default_headers=SPELLED, **dynamic_modes[mode])
        generated = client._sync_generated_client()
        # Swap only the transport: the headers are the ones the SDK built.
        generated.get_httpx_client()._transport = httpx.MockTransport(handler)
        client.list_sources()
        client.list_sources()
        assert seen == [self.EXPECTED, self.EXPECTED]
        client.close()


UNKNOWN = "2099-01-01"
STREAM_BODY: Any = {"input": "x", "metadata": {}}


def _ok(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"ok": True})


class TestSuppliedHttpClientVersionGuard:
    def _http(self, **headers: str) -> httpx.Client:
        return httpx.Client(
            base_url="https://example.invalid",
            transport=httpx.MockTransport(_ok),
            headers=headers,
        )

    def _async_http(self, **headers: str) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            base_url="https://example.invalid",
            transport=httpx.MockTransport(_ok),
            headers=headers,
        )

    def test_unknown_version_is_rejected_at_construction(self) -> None:
        http = self._http(**{"Seclai-Version": UNKNOWN})
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            Seclai(api_key="k", http_client=http)
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            AsyncSeclai(
                api_key="k", http_client=self._async_http(**{"Seclai-Version": UNKNOWN})
            )
        assert http.headers["seclai-version"] == UNKNOWN

    @pytest.mark.parametrize("value", ["", " ", UNKNOWN, "2026-07-27"])
    @pytest.mark.parametrize("allow", [False, True])
    def test_a_value_is_treated_as_default_headers_treats_it(
        self, value: str, allow: bool
    ) -> None:
        def outcome(**options: Any) -> str:
            try:
                Seclai(api_key="k", allow_unknown_api_version=allow, **options)
            except SeclaiConfigurationError:
                return "rejected"
            return "accepted"

        via_default_headers = outcome(default_headers={"Seclai-Version": value})
        via_http_client = outcome(http_client=self._http(**{"Seclai-Version": value}))
        assert via_http_client == via_default_headers
        known_or_allowed = allow or value == "2026-07-27"
        assert via_http_client == ("accepted" if known_or_allowed else "rejected")

    def test_known_version_is_accepted_and_sent(self) -> None:
        seen: list[str | None] = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(request.headers.get("seclai-version"))
            return httpx.Response(200, json={"ok": True})

        http = httpx.Client(
            base_url="https://example.invalid",
            transport=httpx.MockTransport(handler),
            headers={"Seclai-Version": "2026-07-27"},
        )
        Seclai(api_key="k", http_client=http).request("GET", "/x")
        assert seen == ["2026-07-27"]

    def test_allow_unknown_permits_it(self) -> None:
        http = self._http(**{"Seclai-Version": UNKNOWN})
        client = Seclai(api_key="k", http_client=http, allow_unknown_api_version=True)
        assert client.request("GET", "/x") == {"ok": True}

    def test_a_version_the_sdk_sends_instead_is_the_one_checked(self) -> None:
        seen: list[list[str]] = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(request.headers.get_list("seclai-version"))
            return httpx.Response(200, json={"ok": True})

        http = httpx.Client(
            base_url="https://example.invalid",
            transport=httpx.MockTransport(handler),
            headers={"Seclai-Version": UNKNOWN},
        )
        client = Seclai(api_key="k", http_client=http, api_version="2026-07-27")
        client.request("GET", "/x")
        client.request("GET", "/x", headers={"seclai-version": "2026-08-03"})
        assert seen == [["2026-07-27"], ["2026-08-03"]]
        assert http.headers["seclai-version"] == UNKNOWN

    def test_header_added_after_construction_is_rejected_per_request(self) -> None:
        http = self._http()
        client = Seclai(api_key="k", http_client=http)
        assert client.request("GET", "/x") == {"ok": True}
        http.headers["Seclai-Version"] = UNKNOWN
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            client.request("GET", "/x")
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            client.list_alert_configs()
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            client.run_streaming_agent_and_wait("a", STREAM_BODY)
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            list(client.run_streaming_agent("a", STREAM_BODY))
        assert http.headers["seclai-version"] == UNKNOWN

    async def test_async_header_added_after_construction_is_rejected(self) -> None:
        http = self._async_http()
        client = AsyncSeclai(api_key="k", http_client=http)
        assert await client.request("GET", "/x") == {"ok": True}
        http.headers["Seclai-Version"] = UNKNOWN
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            await client.request("GET", "/x")
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            await client.run_streaming_agent_and_wait("a", STREAM_BODY)
        with pytest.raises(SeclaiConfigurationError, match="http_client"):
            async for _event in client.run_streaming_agent("a", STREAM_BODY):
                pass
        await http.aclose()

    def test_a_client_without_the_header_is_untouched(self) -> None:
        http = self._http(**{"X-Other": "1"})
        client = Seclai(api_key="k", http_client=http)
        assert client.request("GET", "/x") == {"ok": True}
        assert dict(http.headers)["x-other"] == "1"
        assert "seclai-version" not in http.headers
