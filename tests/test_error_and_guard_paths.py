"""Error mapping on the generated-client path, and the guards on ``paginate()``
and on a per-request ``Seclai-Version``."""

from __future__ import annotations

from typing import Any

import httpx
import pytest

import seclai
from seclai import AgentRunStreamRequest, AsyncSeclai, Seclai

_BASE_URL = "https://example.invalid"

_FIELD_DETAIL = {"detail": [{"loc": ["query", "page"], "msg": "bad", "type": "x"}]}


def _typed_client(handler: Any) -> Seclai:
    """A client whose typed (generated-client) methods answer from ``handler``."""
    client = Seclai(api_key="k")
    client._generated_client().set_httpx_client(
        httpx.Client(transport=httpx.MockTransport(handler), base_url=_BASE_URL)
    )
    return client


def _request_client(handler: Any, **options: Any) -> Seclai:
    return Seclai(
        api_key="k",
        http_client=httpx.Client(
            transport=httpx.MockTransport(handler), base_url=_BASE_URL
        ),
        **options,
    )


class TestTypedMethodErrorBodies:
    @pytest.mark.parametrize(
        "response",
        [
            httpx.Response(503, text="<html>Service Unavailable</html>"),
            httpx.Response(503, json={"message": "upstream down"}),
            httpx.Response(
                503,
                json={"error": {"code": "database_unavailable", "message": "retry"}},
            ),
        ],
        ids=["html", "foreign-json", "documented-body"],
    )
    def test_a_503_is_a_status_error_whatever_its_body(
        self, response: httpx.Response
    ) -> None:
        client = _typed_client(lambda req: response)
        with pytest.raises(seclai.SeclaiAPIStatusError) as exc:
            client.list_sources()
        assert exc.value.status_code == 503
        assert exc.value.response_text

    def test_a_422_with_a_string_detail_is_a_status_error(self) -> None:
        client = _typed_client(lambda req: httpx.Response(422, json={"detail": "no"}))
        with pytest.raises(seclai.SeclaiAPIStatusError) as exc:
            client.list_sources()
        assert exc.value.status_code == 422
        assert not isinstance(exc.value, seclai.SeclaiAPIValidationError)

    def test_a_422_with_field_detail_is_a_validation_error(self) -> None:
        client = _typed_client(lambda req: httpx.Response(422, json=_FIELD_DETAIL))
        with pytest.raises(seclai.SeclaiAPIValidationError) as exc:
            client.list_sources()
        assert exc.value.validation_error is not None

    def test_an_upload_422_with_a_string_detail_is_a_status_error(self) -> None:
        client = _typed_client(lambda req: httpx.Response(422, json={"detail": "no"}))
        with pytest.raises(seclai.SeclaiAPIStatusError) as exc:
            client.upload_file_to_source("s1", file=b"x", file_name="a.txt")
        assert exc.value.status_code == 422

    def test_a_success_still_decodes(self) -> None:
        body = {
            "data": [],
            "pagination": {
                "page": 1,
                "limit": 20,
                "total": 0,
                "pages": 0,
                "has_next": False,
                "has_prev": False,
            },
        }
        client = _typed_client(lambda req: httpx.Response(200, json=body))
        assert client.list_sources().data == []

    @pytest.mark.asyncio
    async def test_async_503_html_is_a_status_error(self) -> None:
        client = AsyncSeclai(api_key="k")
        client._generated_client().set_async_httpx_client(
            httpx.AsyncClient(
                transport=httpx.MockTransport(
                    lambda req: httpx.Response(503, text="<html>down</html>")
                ),
                base_url=_BASE_URL,
            )
        )
        with pytest.raises(seclai.SeclaiAPIStatusError) as exc:
            await client.list_sources()
        assert exc.value.status_code == 503


class TestPaginateGuards:
    def test_the_legacy_key_also_reads_the_canonical_envelope(self) -> None:
        client = _request_client(
            lambda req: httpx.Response(200, json={"data": [{"id": "c1"}]})
        )
        items = list(client.paginate("GET", "/alerts/configs", items_key="configs"))
        assert items == [{"id": "c1"}]

    def test_the_legacy_key_is_still_read(self) -> None:
        client = _request_client(
            lambda req: httpx.Response(200, json={"configs": [{"id": "c1"}]})
        )
        items = list(client.paginate("GET", "/alerts/configs", items_key="configs"))
        assert items == [{"id": "c1"}]

    def test_an_unreadable_shape_raises_instead_of_yielding_nothing(self) -> None:
        client = _request_client(
            lambda req: httpx.Response(200, json={"rows": [{"id": "c1"}]})
        )
        with pytest.raises(seclai.SeclaiError):
            list(client.paginate("GET", "/alerts/configs", items_key="configs"))

    def test_an_unknown_param_style_is_refused(self) -> None:
        requests: list[httpx.Request] = []

        def handler(req: httpx.Request) -> httpx.Response:
            requests.append(req)
            return httpx.Response(200, json={"data": []})

        client = _request_client(handler)
        with pytest.raises(ValueError, match="param_style"):
            list(
                client.paginate(
                    "GET",
                    "/models/alerts",
                    param_style="Offset",  # type: ignore[arg-type]
                )
            )
        assert requests == []


class TestPerRequestVersionHeader:
    def test_an_unknown_version_is_refused(self) -> None:
        requests: list[httpx.Request] = []

        def handler(req: httpx.Request) -> httpx.Response:
            requests.append(req)
            return httpx.Response(200, json={"data": []})

        client = _request_client(handler)
        with pytest.raises(seclai.SeclaiConfigurationError, match="2099-01-01"):
            client.request("GET", "/agents", headers={"seclai-version": "2099-01-01"})
        assert requests == []

    def test_an_unknown_version_is_refused_on_a_streaming_method(self) -> None:
        client = _request_client(lambda req: httpx.Response(200, text=""))
        with pytest.raises(seclai.SeclaiConfigurationError, match="2099-01-01"):
            client.run_streaming_agent_and_wait(
                "a1",
                AgentRunStreamRequest(input="hi", metadata={}),
                headers={"Seclai-Version": "2099-01-01"},
            )

    def test_the_escape_hatch_allows_it(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["version"] = req.headers.get("seclai-version")
            return httpx.Response(200, json={"data": []})

        client = _request_client(handler, allow_unknown_api_version=True)
        client.request("GET", "/agents", headers={"Seclai-Version": "2099-01-01"})
        assert seen["version"] == "2099-01-01"

    def test_a_known_version_still_overrides(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["version"] = req.headers.get("seclai-version")
            return httpx.Response(200, json={"data": []})

        client = _request_client(handler, api_version="2026-07-01")
        client.request("GET", "/agents", headers={"Seclai-Version": "2026-10-03"})
        assert seen["version"] == "2026-10-03"

    def test_the_spelling_that_reaches_the_wire_is_the_one_checked(self) -> None:
        seen: dict[str, Any] = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["versions"] = req.headers.get_list("seclai-version")
            return httpx.Response(200, json={"data": []})

        client = _request_client(handler)
        client.request(
            "GET",
            "/agents",
            headers={"seclai-version": "2099-01-01", "Seclai-Version": "2026-10-03"},
        )
        assert seen["versions"] == ["2026-10-03"]

        with pytest.raises(seclai.SeclaiConfigurationError, match="2099-01-01"):
            client.request(
                "GET",
                "/agents",
                headers={
                    "Seclai-Version": "2026-10-03",
                    "seclai-version": "2099-01-01",
                },
            )
