from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKnowledgeBaseBody")


@_attrs_define
class UpdateKnowledgeBaseBody:
    """Request body for updating a knowledge base.

    Attributes:
        default_score_threshold (float | None | Unset): Default score threshold (-1 to clear).
        default_top_k (int | None | Unset): Default reranked results (0 to clear).
        default_top_n (int | None | Unset): Default results (0 to clear).
        description (None | str | Unset): New description.
        name (None | str | Unset): New name.
        reranker_model (None | str | Unset): Reranker model (empty string for no reranking).
        source_ids (list[str] | None | Unset): New list of source connection IDs.
    """

    default_score_threshold: float | None | Unset = UNSET
    default_top_k: int | None | Unset = UNSET
    default_top_n: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    reranker_model: None | str | Unset = UNSET
    source_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        reranker_model: None | str | Unset
        if isinstance(self.reranker_model, Unset):
            reranker_model = UNSET
        else:
            reranker_model = self.reranker_model

        source_ids: list[str] | None | Unset
        if isinstance(self.source_ids, Unset):
            source_ids = UNSET
        elif isinstance(self.source_ids, list):
            source_ids = self.source_ids

        else:
            source_ids = self.source_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_score_threshold is not UNSET:
            field_dict["default_score_threshold"] = default_score_threshold
        if default_top_k is not UNSET:
            field_dict["default_top_k"] = default_top_k
        if default_top_n is not UNSET:
            field_dict["default_top_n"] = default_top_n
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model
        if source_ids is not UNSET:
            field_dict["source_ids"] = source_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_reranker_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reranker_model = _parse_reranker_model(d.pop("reranker_model", UNSET))

        def _parse_source_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_ids_type_0 = cast(list[str], data)

                return source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_ids = _parse_source_ids(d.pop("source_ids", UNSET))

        update_knowledge_base_body = cls(
            default_score_threshold=default_score_threshold,
            default_top_k=default_top_k,
            default_top_n=default_top_n,
            description=description,
            name=name,
            reranker_model=reranker_model,
            source_ids=source_ids,
        )

        update_knowledge_base_body.additional_properties = d
        return update_knowledge_base_body

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
