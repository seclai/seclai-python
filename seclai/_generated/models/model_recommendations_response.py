from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_recommendation_response import ModelRecommendationResponse


T = TypeVar("T", bound="ModelRecommendationsResponse")


@_attrs_define
class ModelRecommendationsResponse:
    """
    Attributes:
        alternatives (list[ModelRecommendationResponse]):
        current_model_id (str):
        current_model_name (str):
        same_provider (list[ModelRecommendationResponse]):
        upgrades (list[ModelRecommendationResponse]):
        successor (ModelRecommendationResponse | None | Unset):
    """

    alternatives: list[ModelRecommendationResponse]
    current_model_id: str
    current_model_name: str
    same_provider: list[ModelRecommendationResponse]
    upgrades: list[ModelRecommendationResponse]
    successor: ModelRecommendationResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_recommendation_response import ModelRecommendationResponse

        alternatives = []
        for alternatives_item_data in self.alternatives:
            alternatives_item = alternatives_item_data.to_dict()
            alternatives.append(alternatives_item)

        current_model_id = self.current_model_id

        current_model_name = self.current_model_name

        same_provider = []
        for same_provider_item_data in self.same_provider:
            same_provider_item = same_provider_item_data.to_dict()
            same_provider.append(same_provider_item)

        upgrades = []
        for upgrades_item_data in self.upgrades:
            upgrades_item = upgrades_item_data.to_dict()
            upgrades.append(upgrades_item)

        successor: dict[str, Any] | None | Unset
        if isinstance(self.successor, Unset):
            successor = UNSET
        elif isinstance(self.successor, ModelRecommendationResponse):
            successor = self.successor.to_dict()
        else:
            successor = self.successor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alternatives": alternatives,
                "current_model_id": current_model_id,
                "current_model_name": current_model_name,
                "same_provider": same_provider,
                "upgrades": upgrades,
            }
        )
        if successor is not UNSET:
            field_dict["successor"] = successor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_recommendation_response import ModelRecommendationResponse

        d = dict(src_dict)
        alternatives = []
        _alternatives = d.pop("alternatives")
        for alternatives_item_data in _alternatives:
            alternatives_item = ModelRecommendationResponse.from_dict(
                alternatives_item_data
            )

            alternatives.append(alternatives_item)

        current_model_id = d.pop("current_model_id")

        current_model_name = d.pop("current_model_name")

        same_provider = []
        _same_provider = d.pop("same_provider")
        for same_provider_item_data in _same_provider:
            same_provider_item = ModelRecommendationResponse.from_dict(
                same_provider_item_data
            )

            same_provider.append(same_provider_item)

        upgrades = []
        _upgrades = d.pop("upgrades")
        for upgrades_item_data in _upgrades:
            upgrades_item = ModelRecommendationResponse.from_dict(upgrades_item_data)

            upgrades.append(upgrades_item)

        def _parse_successor(
            data: object,
        ) -> ModelRecommendationResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                successor_type_0 = ModelRecommendationResponse.from_dict(data)

                return successor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelRecommendationResponse | None | Unset, data)

        successor = _parse_successor(d.pop("successor", UNSET))

        model_recommendations_response = cls(
            alternatives=alternatives,
            current_model_id=current_model_id,
            current_model_name=current_model_name,
            same_provider=same_provider,
            upgrades=upgrades,
            successor=successor,
        )

        model_recommendations_response.additional_properties = d
        return model_recommendations_response

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
