from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenerationTierResponse")


@_attrs_define
class GenerationTierResponse:
    """
    Attributes:
        credits_per_unit (int | None):
        modality (str):
        model_id (str):
        model_name (str):
        price_label (None | str):
        tier (str):
        unit_label (None | str):
    """

    credits_per_unit: int | None
    modality: str
    model_id: str
    model_name: str
    price_label: None | str
    tier: str
    unit_label: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_per_unit: int | None
        credits_per_unit = self.credits_per_unit

        modality = self.modality

        model_id = self.model_id

        model_name = self.model_name

        price_label: None | str
        price_label = self.price_label

        tier = self.tier

        unit_label: None | str
        unit_label = self.unit_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits_per_unit": credits_per_unit,
                "modality": modality,
                "model_id": model_id,
                "model_name": model_name,
                "price_label": price_label,
                "tier": tier,
                "unit_label": unit_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_credits_per_unit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        credits_per_unit = _parse_credits_per_unit(d.pop("credits_per_unit"))

        modality = d.pop("modality")

        model_id = d.pop("model_id")

        model_name = d.pop("model_name")

        def _parse_price_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        price_label = _parse_price_label(d.pop("price_label"))

        tier = d.pop("tier")

        def _parse_unit_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit_label = _parse_unit_label(d.pop("unit_label"))

        generation_tier_response = cls(
            credits_per_unit=credits_per_unit,
            modality=modality,
            model_id=model_id,
            model_name=model_name,
            price_label=price_label,
            tier=tier,
            unit_label=unit_label,
        )

        generation_tier_response.additional_properties = d
        return generation_tier_response

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
