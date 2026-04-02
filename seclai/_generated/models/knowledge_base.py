from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_connection_response_model import SourceConnectionResponseModel


T = TypeVar("T", bound="KnowledgeBase")


@_attrs_define
class KnowledgeBase:
    """Response model for a single knowledge base.

    Attributes:
        created_at (str): ISO-8601 creation timestamp.
        id (str): Unique knowledge base identifier.
        name (str): Human-readable name.
        updated_at (str): ISO-8601 last-update timestamp.
        default_score_threshold (float | None | Unset): Default minimum rerank score.
        default_top_k (int | None | Unset): Default results after reranking.
        default_top_n (int | None | Unset): Default number of results to return.
        description (None | str | Unset): Optional description.
        readonly (bool | Unset): Whether the knowledge base is read-only. Default: False.
        reranker_model (None | str | Unset): Reranker model in use.
        sources (list[SourceConnectionResponseModel] | Unset): Linked source connections.
    """

    created_at: str
    id: str
    name: str
    updated_at: str
    default_score_threshold: float | None | Unset = UNSET
    default_top_k: int | None | Unset = UNSET
    default_top_n: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    readonly: bool | Unset = False
    reranker_model: None | str | Unset = UNSET
    sources: list[SourceConnectionResponseModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        name = self.name

        updated_at = self.updated_at

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

        readonly = self.readonly

        reranker_model: None | str | Unset
        if isinstance(self.reranker_model, Unset):
            reranker_model = UNSET
        else:
            reranker_model = self.reranker_model

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "updated_at": updated_at,
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
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_connection_response_model import (
            SourceConnectionResponseModel,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = d.pop("id")

        name = d.pop("name")

        updated_at = d.pop("updated_at")

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

        readonly = d.pop("readonly", UNSET)

        def _parse_reranker_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reranker_model = _parse_reranker_model(d.pop("reranker_model", UNSET))

        _sources = d.pop("sources", UNSET)
        sources: list[SourceConnectionResponseModel] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = SourceConnectionResponseModel.from_dict(
                    sources_item_data
                )

                sources.append(sources_item)

        knowledge_base = cls(
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            default_score_threshold=default_score_threshold,
            default_top_k=default_top_k,
            default_top_n=default_top_n,
            description=description,
            readonly=readonly,
            reranker_model=reranker_model,
            sources=sources,
        )

        knowledge_base.additional_properties = d
        return knowledge_base

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
