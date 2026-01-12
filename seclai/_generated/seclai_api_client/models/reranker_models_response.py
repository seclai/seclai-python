from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.embedding_cost_info import EmbeddingCostInfo
    from ..models.reranker_model_info import RerankerModelInfo


T = TypeVar("T", bound="RerankerModelsResponse")


@_attrs_define
class RerankerModelsResponse:
    """Response model for reranker models list

    Attributes:
        default_model_type (str):
        embedding_costs (list[EmbeddingCostInfo]):
        models (list[RerankerModelInfo]):
        search_processing_credits (float):
    """

    default_model_type: str
    embedding_costs: list[EmbeddingCostInfo]
    models: list[RerankerModelInfo]
    search_processing_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_model_type = self.default_model_type

        embedding_costs = []
        for embedding_costs_item_data in self.embedding_costs:
            embedding_costs_item = embedding_costs_item_data.to_dict()
            embedding_costs.append(embedding_costs_item)

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        search_processing_credits = self.search_processing_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_model_type": default_model_type,
                "embedding_costs": embedding_costs,
                "models": models,
                "search_processing_credits": search_processing_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedding_cost_info import EmbeddingCostInfo
        from ..models.reranker_model_info import RerankerModelInfo

        d = dict(src_dict)
        default_model_type = d.pop("default_model_type")

        embedding_costs = []
        _embedding_costs = d.pop("embedding_costs")
        for embedding_costs_item_data in _embedding_costs:
            embedding_costs_item = EmbeddingCostInfo.from_dict(
                embedding_costs_item_data
            )

            embedding_costs.append(embedding_costs_item)

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = RerankerModelInfo.from_dict(models_item_data)

            models.append(models_item)

        search_processing_credits = d.pop("search_processing_credits")

        reranker_models_response = cls(
            default_model_type=default_model_type,
            embedding_costs=embedding_costs,
            models=models,
            search_processing_credits=search_processing_credits,
        )

        reranker_models_response.additional_properties = d
        return reranker_models_response

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
