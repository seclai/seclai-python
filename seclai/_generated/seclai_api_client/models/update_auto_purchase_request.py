from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAutoPurchaseRequest")


@_attrs_define
class UpdateAutoPurchaseRequest:
    """
    Attributes:
        auto_purchase_overages (bool):
    """

    auto_purchase_overages: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_purchase_overages = self.auto_purchase_overages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auto_purchase_overages": auto_purchase_overages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_purchase_overages = d.pop("auto_purchase_overages")

        update_auto_purchase_request = cls(
            auto_purchase_overages=auto_purchase_overages,
        )

        update_auto_purchase_request.additional_properties = d
        return update_auto_purchase_request

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
