from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationAlertPreferenceResponse")


@_attrs_define
class OrganizationAlertPreferenceResponse:
    """
    Attributes:
        alert_type (str):
        is_override (bool):
        organization_id (str):
        subscribed (bool):
    """

    alert_type: str
    is_override: bool
    organization_id: str
    subscribed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_type = self.alert_type

        is_override = self.is_override

        organization_id = self.organization_id

        subscribed = self.subscribed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_type": alert_type,
                "is_override": is_override,
                "organization_id": organization_id,
                "subscribed": subscribed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_type = d.pop("alert_type")

        is_override = d.pop("is_override")

        organization_id = d.pop("organization_id")

        subscribed = d.pop("subscribed")

        organization_alert_preference_response = cls(
            alert_type=alert_type,
            is_override=is_override,
            organization_id=organization_id,
            subscribed=subscribed,
        )

        organization_alert_preference_response.additional_properties = d
        return organization_alert_preference_response

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
