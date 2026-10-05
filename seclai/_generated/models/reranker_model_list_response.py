from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reranker_model_response import RerankerModelResponse


T = TypeVar("T", bound="RerankerModelListResponse")


@_attrs_define
class RerankerModelListResponse:
    """Legacy (header-less) response shape for the reranker catalog.

    Attributes:
        default_model_type (str): Reranker used when a knowledge base does not choose one
        models (list[RerankerModelResponse]): Available reranker models
        search_processing_credits (float): Credits charged for processing a search request
    """

    default_model_type: str
    models: list[RerankerModelResponse]
    search_processing_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_model_type = self.default_model_type

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
                "models": models,
                "search_processing_credits": search_processing_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reranker_model_response import RerankerModelResponse

        d = dict(src_dict)
        default_model_type = d.pop("default_model_type")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = RerankerModelResponse.from_dict(models_item_data)

            models.append(models_item)

        search_processing_credits = d.pop("search_processing_credits")

        reranker_model_list_response = cls(
            default_model_type=default_model_type,
            models=models,
            search_processing_credits=search_processing_credits,
        )

        reranker_model_list_response.additional_properties = d
        return reranker_model_list_response

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
