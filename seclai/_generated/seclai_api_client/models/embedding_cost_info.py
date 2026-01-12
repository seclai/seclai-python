from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmbeddingCostInfo")


@_attrs_define
class EmbeddingCostInfo:
    """Embedding cost information for a specific model/dimension combination

    Costs are calculated for a 15-word query using the conversion formula:
    - 4 characters per token
    - 6 characters average per English word
    - Therefore: 15 words × (4/6) tokens/word = 10 tokens

        Attributes:
            credits_per_15_word_query (float):
            dimensions (int):
            model (str):
    """

    credits_per_15_word_query: float
    dimensions: int
    model: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_per_15_word_query = self.credits_per_15_word_query

        dimensions = self.dimensions

        model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits_per_15_word_query": credits_per_15_word_query,
                "dimensions": dimensions,
                "model": model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_per_15_word_query = d.pop("credits_per_15_word_query")

        dimensions = d.pop("dimensions")

        model = d.pop("model")

        embedding_cost_info = cls(
            credits_per_15_word_query=credits_per_15_word_query,
            dimensions=dimensions,
            model=model,
        )

        embedding_cost_info.additional_properties = d
        return embedding_cost_info

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
