"""`paginate()` stopping rule: what is yielded, how many requests, what raises."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import httpx
import pytest

from seclai import AsyncSeclai, Seclai, SeclaiAPIStatusError, SeclaiError

Query = dict[str, str]
Answer = Callable[[Query], Any]


def _rows(n: int) -> list[dict[str, Any]]:
    return [{"id": f"x{i}"} for i in range(n)]


class _Server:
    """A handler recording how many requests a walk made."""

    def __init__(self, answer: Answer) -> None:
        self.requests = 0
        self._answer = answer

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests += 1
        body = self._answer(dict(request.url.params))
        if isinstance(body, httpx.Response):
            return body
        return httpx.Response(200, json=body)


def _sync(server: _Server) -> Seclai:
    http = httpx.Client(
        base_url="https://example.invalid", transport=httpx.MockTransport(server)
    )
    client = Seclai(api_key="test", http_client=http)
    client._owns_client = True
    return client


def _async(server: _Server) -> AsyncSeclai:
    http = httpx.AsyncClient(
        base_url="https://example.invalid", transport=httpx.MockTransport(server)
    )
    client = AsyncSeclai(api_key="test", http_client=http)
    client._owns_client = True
    return client


def _everything(body: Any) -> Answer:
    """An endpoint that ignores the cursor and `limit`."""
    return lambda query: body


def _first_page_only(rows: list[dict[str, Any]], key: str, **extra: Any) -> Answer:
    """An endpoint that honours `limit` but not the cursor it was sent."""
    return lambda query: {key: rows[: int(query["limit"])], **extra}


def _by_page(
    rows: list[dict[str, Any]], key: str, *, total: bool, has_next: bool = False
) -> Answer:
    def answer(query: Query) -> Any:
        limit = int(query["limit"])
        start = (int(query["page"]) - 1) * limit
        body: dict[str, Any] = {key: rows[start : start + limit]}
        if total:
            body["total"] = len(rows)
        if has_next:
            body["pagination"] = {"has_next": start + limit < len(rows)}
        return body

    return answer


def _by_offset(rows: list[dict[str, Any]], key: str) -> Answer:
    def answer(query: Query) -> Any:
        start, limit = int(query.get("offset", 0)), int(query["limit"])
        return {key: rows[start : start + limit], "total": len(rows)}

    return answer


def _envelope(rows: list[dict[str, Any]]) -> Answer:
    def answer(query: Query) -> Any:
        limit, page = int(query["limit"]), int(query["page"])
        start = (page - 1) * limit
        return {
            "data": rows[start : start + limit],
            "pagination": {
                "page": page,
                "limit": limit,
                "total": len(rows),
                "pages": -(-len(rows) // limit),
                "has_next": start + limit < len(rows),
                "has_prev": page > 1,
            },
        }

    return answer


def _fails_on_page_two(query: Query) -> Any:
    if query["page"] != "1":
        return httpx.Response(500, json={"detail": "boom"})
    return {"data": _rows(50), "total": 120}


def _own_page_size(
    rows: list[dict[str, Any]], size: int, *, signal: str | None
) -> Answer:
    """An endpoint that pages honestly but by its own page size, ignoring `limit`."""

    def answer(query: Query) -> Any:
        if "offset" in query:
            start = int(query["offset"])
        else:
            start = (int(query["page"]) - 1) * size
        body: dict[str, Any] = {"data": rows[start : start + size]}
        if signal == "total":
            body["total"] = len(rows)
        if signal == "has_next":
            body["pagination"] = {"has_next": start + size < len(rows)}
        return body

    return answer


SAME = [{"kind": "x"}] * 150
CONFIGS = {"items_key": "configs"}
ALERTS = {"items_key": "alerts"}

# (id, path, paginate kwargs, answer, items yielded, requests, exception, mutate)
Case = tuple[str, str, dict[str, Any], Answer, list[Any], int, Any, bool]
CASES: list[Case] = [
    # The README example on the default API version, where the endpoint ignores
    # `page`/`limit` and returns every config with `total`.
    *[
        (
            f"alert configs, default version, {n} configs",
            "/alerts/configs",
            CONFIGS,
            _everything({"configs": _rows(n), "total": n}),
            _rows(n),
            1,
            None,
            False,
        )
        for n in (49, 50, 51, 120)
    ],
    # A page longer than `limit` ends the walk only when the body does not say
    # that more exist: an endpoint with its own page size is walked to the end.
    *[
        (
            f"own page size 20, limit 10, 65 rows, {signal} reported",
            "/things",
            {"limit": 10},
            _own_page_size(_rows(65), 20, signal=signal),
            _rows(65),
            4,
            None,
            False,
        )
        for signal in ("total", "has_next")
    ],
    (
        "own page size 20 by offset, limit 10, 65 rows, total reported",
        "/things",
        {"limit": 10, "param_style": "offset"},
        _own_page_size(_rows(65), 20, signal="total"),
        _rows(65),
        4,
        None,
        False,
    ),
    (
        "longer than limit with no paging information is the whole collection",
        "/things",
        {"limit": 10},
        _own_page_size(_rows(65), 20, signal=None),
        _rows(20),
        1,
        None,
        False,
    ),
    # Endpoints that return everything on the default version (pattern D).
    (
        "organization preferences, exactly a page, with total",
        "/alerts/organization-preferences/list",
        {"items_key": "preferences"},
        _everything({"preferences": _rows(50), "total": 50}),
        _rows(50),
        1,
        None,
        False,
    ),
    *[
        (
            f"generation tiers, {n} rows, no counters",
            "/models/generation-tiers",
            {"items_key": "tiers"},
            _everything({"tiers": _rows(n)}),
            _rows(n),
            requests,
            None,
            False,
        )
        # Exactly `limit` rows is the one count that needs a second request.
        for n, requests in ((49, 1), (50, 2), (60, 1))
    ],
    (
        "embedders, exactly a page, no counters",
        "/models/embedders",
        {"items_key": "models"},
        _everything({"models": _rows(50), "default_model_type": "m"}),
        _rows(50),
        2,
        None,
        False,
    ),
    (
        "rerankers, exactly a page, no counters",
        "/models/rerankers",
        {"items_key": "models", "limit": 5},
        _everything({"models": _rows(5), "default_model_type": "r"}),
        _rows(5),
        2,
        None,
        False,
    ),
    (
        "email domains, exactly a page, no counters",
        "/email-domains",
        {"items_key": "domains", "limit": 2},
        _everything({"domains": _rows(2), "can_add_vanity": True}),
        _rows(2),
        2,
        None,
        False,
    ),
    (
        "email domains, more than a page, no counters",
        "/email-domains",
        {"items_key": "domains", "limit": 1},
        _everything({"domains": _rows(2), "can_add_vanity": True}),
        _rows(2),
        1,
        None,
        False,
    ),
    # An offset-only endpoint walked with `page`: the body says 120 exist.
    (
        "offset-only endpoint walked by page raises",
        "/models/alerts",
        ALERTS,
        _first_page_only(_rows(120), "alerts", total=120),
        _rows(50),
        2,
        SeclaiError,
        False,
    ),
    (
        "offset-only endpoint walked by offset",
        "/models/alerts",
        {**ALERTS, "param_style": "offset"},
        _by_offset(_rows(120), "alerts"),
        _rows(120),
        3,
        None,
        False,
    ),
    (
        "offset walk, total reached on a full page",
        "/models/alerts",
        {**ALERTS, "param_style": "offset"},
        _by_offset(_rows(100), "alerts"),
        _rows(100),
        2,
        None,
        False,
    ),
    # A caller that mutates what it is handed must not change the outcome.
    (
        "mutating caller, repeated page with total raises",
        "/models/alerts",
        ALERTS,
        _first_page_only(_rows(120), "alerts", total=120),
        _rows(50),
        2,
        SeclaiError,
        True,
    ),
    (
        "mutating caller, repeated page without total ends",
        "/models/alerts",
        ALERTS,
        _first_page_only(_rows(120), "alerts"),
        _rows(50),
        2,
        None,
        True,
    ),
    (
        "mutating caller, honest paging",
        "/knowledge_bases",
        {"items_key": "knowledge_bases"},
        _by_page(_rows(120), "knowledge_bases", total=True),
        _rows(120),
        3,
        None,
        True,
    ),
    # Honest paging whose last page is full.
    (
        "full last page, no counters, ends on the empty page",
        "/knowledge_bases",
        {"items_key": "knowledge_bases"},
        _by_page(_rows(100), "knowledge_bases", total=False),
        _rows(100),
        3,
        None,
        False,
    ),
    (
        "full last page, flat total",
        "/knowledge_bases",
        {"items_key": "knowledge_bases"},
        _by_page(_rows(100), "knowledge_bases", total=True),
        _rows(100),
        2,
        None,
        False,
    ),
    (
        "full last page, has_next only",
        "/knowledge_bases",
        {"items_key": "knowledge_bases"},
        _by_page(_rows(100), "knowledge_bases", total=False, has_next=True),
        _rows(100),
        2,
        None,
        False,
    ),
    (
        "full last page, envelope",
        "/alerts/configs",
        CONFIGS,
        _envelope(_rows(100)),
        _rows(100),
        2,
        None,
        False,
    ),
    (
        "short last page, envelope",
        "/alerts/configs",
        CONFIGS,
        _envelope(_rows(120)),
        _rows(120),
        3,
        None,
        False,
    ),
    # 150 rows with no distinguishing field, honestly paged: page 2 equals page
    # 1, which is indistinguishable from an endpoint ignoring the cursor.
    (
        "identical rows, flat total: raises instead of truncating",
        "/knowledge_bases",
        {"items_key": "knowledge_bases"},
        _by_page(SAME, "knowledge_bases", total=True),
        SAME[:50],
        2,
        SeclaiError,
        False,
    ),
    (
        "identical rows, envelope: raises instead of truncating",
        "/alerts/configs",
        CONFIGS,
        _envelope(SAME),
        SAME[:50],
        2,
        SeclaiError,
        False,
    ),
    (
        "identical rows, no paging information: ends after one page",
        "/knowledge_bases",
        {"items_key": "knowledge_bases"},
        _by_page(SAME, "knowledge_bases", total=False),
        SAME[:50],
        2,
        None,
        False,
    ),
    (
        "second page fails",
        "/alerts/configs",
        {},
        _fails_on_page_two,
        _rows(50),
        2,
        SeclaiAPIStatusError,
        False,
    ),
    (
        "bare array",
        "/cloud-drives",
        {},
        _everything(_rows(120)),
        _rows(120),
        1,
        None,
        False,
    ),  # fmt: skip
    ("empty", "/alerts/configs", {}, _everything({"data": []}), [], 1, None, False),
    (
        "not a list",
        "/alerts/configs",
        CONFIGS,
        _everything({"error": {"code": "x"}}),
        [],
        1,
        SeclaiError,
        False,
    ),
    *[
        (
            f"limit={limit!r} is rejected before any request",
            "/alerts/configs",
            {**CONFIGS, "limit": limit},
            _everything({"configs": [], "total": 0}),
            [],
            0,
            ValueError,
            False,
        )
        for limit in (0, -1, True, 2.5, "50")
    ],
    (
        "param_style is rejected before any request",
        "/alerts/configs",
        {"param_style": "cursor"},
        _everything({"data": []}),
        [],
        0,
        ValueError,
        False,
    ),
]
# A walk that yields this many more items than expected is not terminating.
SLACK = 5


@pytest.mark.parametrize("case", CASES, ids=[c[0] for c in CASES])
class TestPaginate:
    def test_sync(self, case: Case) -> None:
        _id, path, kwargs, answer, expected, requests, exception, mutate = case
        server = _Server(answer)
        seen: list[Any] = []
        raised: BaseException | None = None
        with _sync(server) as client:
            try:
                for item in client.paginate("GET", path, **kwargs):
                    seen.append(dict(item))
                    if mutate:
                        item["seen"] = True
                    assert len(seen) <= len(expected) + SLACK, "did not terminate"
            except (SeclaiError, ValueError) as exc:
                raised = exc
        assert seen == expected
        assert server.requests == requests
        assert type(raised) is (exception or type(None))

    async def test_async(self, case: Case) -> None:
        _id, path, kwargs, answer, expected, requests, exception, mutate = case
        server = _Server(answer)
        seen: list[Any] = []
        raised: BaseException | None = None
        async with _async(server) as client:
            try:
                async for item in client.paginate("GET", path, **kwargs):
                    seen.append(dict(item))
                    if mutate:
                        item["seen"] = True
                    assert len(seen) <= len(expected) + SLACK, "did not terminate"
            except (SeclaiError, ValueError) as exc:
                raised = exc
        assert seen == expected
        assert server.requests == requests
        assert type(raised) is (exception or type(None))


def test_repeated_page_error_names_param_style() -> None:
    server = _Server(_first_page_only(_rows(120), "alerts", total=120))
    with _sync(server) as client, pytest.raises(SeclaiError, match="param_style='offset'"):  # fmt: skip
        list(client.paginate("GET", "/models/alerts", items_key="alerts"))


def test_closing_early_makes_no_further_request() -> None:
    server = _Server(_envelope(_rows(120)))
    with _sync(server) as client:
        walk = client.paginate("GET", "/alerts/configs")
        assert next(walk) == {"id": "x0"}
        walk.close()
        assert list(walk) == []
    assert server.requests == 1


async def test_async_closing_early_makes_no_further_request() -> None:
    server = _Server(_envelope(_rows(120)))
    async with _async(server) as client:
        walk = client.paginate("GET", "/alerts/configs")
        assert await anext(walk) == {"id": "x0"}
        await walk.aclose()
        assert [item async for item in walk] == []
    assert server.requests == 1


def test_caller_params_are_sent_on_every_page_and_not_mutated() -> None:
    queries: list[Query] = []

    def answer(query: Query) -> Any:
        queries.append(query)
        return _envelope(_rows(120))(query)

    params = {"status": "open"}
    with _sync(_Server(answer)) as client:
        assert len(list(client.paginate("GET", "/alerts", params=params))) == 120
    assert params == {"status": "open"}
    assert [q["status"] for q in queries] == ["open"] * 3
    assert [q["page"] for q in queries] == ["1", "2", "3"]
