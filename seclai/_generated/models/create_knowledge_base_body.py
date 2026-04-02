from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeBaseBody")


@_attrs_define
class CreateKnowledgeBaseBody:
    """Request body for creating a knowledge base.

    Attributes:
        name (str): Knowledge base name.
        source_ids (list[str]): List of source connection IDs to link.
        default_score_threshold (float | None | Unset): Default minimum rerank score threshold.
        default_top_k (int | None | Unset): Default results after reranking.
        default_top_n (int | None | Unset): Default number of results.
        description (None | str | Unset): Optional description.
        reranker_model (None | str | Unset): Reranker model to use (null for no reranking).
    """

    name: str
    source_ids: list[str]
    default_score_threshold: float | None | Unset = UNSET
    default_top_k: int | None | Unset = UNSET
    default_top_n: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    reranker_model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source_ids = self.source_ids

        default_score_threshold: float | None | Unset
        if isinstance(self.default_score_threshold, Unset):
            default_score_threshold = UNSET
        else:
            default_score_threshold = self.default_score_threshold

        default_top_k: int | None | Unset
        if isinstance(self.default_top_k, Unset):
            default_top_k = UNSET
        else:
            default_top_k = self.default_top_k

        default_top_n: int | None | Unset
        if isinstance(self.default_top_n, Unset):
            default_top_n = UNSET
        else:
            default_top_n = self.default_top_n

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        reranker_model: None | str | Unset
        if isinstance(self.reranker_model, Unset):
            reranker_model = UNSET
        else:
            reranker_model = self.reranker_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source_ids": source_ids,
            }
        )
        if default_score_threshold is not UNSET:
            field_dict["default_score_threshold"] = default_score_threshold
        if default_top_k is not UNSET:
            field_dict["default_top_k"] = default_top_k
        if default_top_n is not UNSET:
            field_dict["default_top_n"] = default_top_n
        if description is not UNSET:
            field_dict["description"] = description
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        source_ids = cast(list[str], d.pop("source_ids"))

        def _parse_default_score_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_score_threshold = _parse_default_score_threshold(
            d.pop("default_score_threshold", UNSET)
        )

        def _parse_default_top_k(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_top_k = _parse_default_top_k(d.pop("default_top_k", UNSET))

        def _parse_default_top_n(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_top_n = _parse_default_top_n(d.pop("default_top_n", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_reranker_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reranker_model = _parse_reranker_model(d.pop("reranker_model", UNSET))

        create_knowledge_base_body = cls(
            name=name,
            source_ids=source_ids,
            default_score_threshold=default_score_threshold,
            default_top_k=default_top_k,
            default_top_n=default_top_n,
            description=description,
            reranker_model=reranker_model,
        )

        create_knowledge_base_body.additional_properties = d
        return create_knowledge_base_body

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
