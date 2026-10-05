from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CloudDriveAccessLevelResponseModel")


@_attrs_define
class CloudDriveAccessLevelResponseModel:
    """
    Attributes:
        default (bool): Whether connecting without a choice uses it.
        description (str): What agents can do at this level.
        key (str): Level identifier, e.g. `read_write`/`read_only`.
        label (str): Short human-readable name.
    """

    default: bool
    description: str
    key: str
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        description = self.description

        key = self.key

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "description": description,
                "key": key,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default = d.pop("default")

        description = d.pop("description")

        key = d.pop("key")

        label = d.pop("label")

        cloud_drive_access_level_response_model = cls(
            default=default,
            description=description,
            key=key,
            label=label,
        )

        cloud_drive_access_level_response_model.additional_properties = d
        return cloud_drive_access_level_response_model

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
