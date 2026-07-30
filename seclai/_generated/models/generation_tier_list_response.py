from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.generation_tier_response import GenerationTierResponse


T = TypeVar("T", bound="GenerationTierListResponse")


@_attrs_define
class GenerationTierListResponse:
    """``GET /models/generation-tiers`` legacy/default shape; 2026-07-27+ clients
    get the canonical ``{data, pagination}`` envelope.

        Attributes:
            tiers (list[GenerationTierResponse]):
    """

    tiers: list[GenerationTierResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tiers = []
        for tiers_item_data in self.tiers:
            tiers_item = tiers_item_data.to_dict()
            tiers.append(tiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tiers": tiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generation_tier_response import GenerationTierResponse

        d = dict(src_dict)
        tiers = []
        _tiers = d.pop("tiers")
        for tiers_item_data in _tiers:
            tiers_item = GenerationTierResponse.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        generation_tier_list_response = cls(
            tiers=tiers,
        )

        generation_tier_list_response.additional_properties = d
        return generation_tier_list_response

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
