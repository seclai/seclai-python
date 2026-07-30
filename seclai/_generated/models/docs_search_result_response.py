from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocsSearchResultResponse")


@_attrs_define
class DocsSearchResultResponse:
    """
    Attributes:
        anchor (None | str):
        doc_slug (str):
        highlight (None | str):
        score (float):
        snippet (None | str):
        title (str):
    """

    anchor: None | str
    doc_slug: str
    highlight: None | str
    score: float
    snippet: None | str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor: None | str
        anchor = self.anchor

        doc_slug = self.doc_slug

        highlight: None | str
        highlight = self.highlight

        score = self.score

        snippet: None | str
        snippet = self.snippet

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anchor": anchor,
                "doc_slug": doc_slug,
                "highlight": highlight,
                "score": score,
                "snippet": snippet,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_anchor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        anchor = _parse_anchor(d.pop("anchor"))

        doc_slug = d.pop("doc_slug")

        def _parse_highlight(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        highlight = _parse_highlight(d.pop("highlight"))

        score = d.pop("score")

        def _parse_snippet(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        snippet = _parse_snippet(d.pop("snippet"))

        title = d.pop("title")

        docs_search_result_response = cls(
            anchor=anchor,
            doc_slug=doc_slug,
            highlight=highlight,
            score=score,
            snippet=snippet,
            title=title,
        )

        docs_search_result_response.additional_properties = d
        return docs_search_result_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
