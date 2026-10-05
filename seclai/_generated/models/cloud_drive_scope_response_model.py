from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CloudDriveScopeResponseModel")


@_attrs_define
class CloudDriveScopeResponseModel:
    """
    Attributes:
        description (str): What the scope allows.
        key (str): The OAuth scope string sent to the provider.
        label (str): Short human-readable name.
        recommended (bool): Whether this scope is requested by default on connect.
    """

    description: str
    key: str
    label: str
    recommended: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        key = self.key

        label = self.label

        recommended = self.recommended

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "key": key,
                "label": label,
                "recommended": recommended,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        key = d.pop("key")

        label = d.pop("label")

        recommended = d.pop("recommended")

        cloud_drive_scope_response_model = cls(
            description=description,
            key=key,
            label=label,
            recommended=recommended,
        )

        cloud_drive_scope_response_model.additional_properties = d
        return cloud_drive_scope_response_model

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
