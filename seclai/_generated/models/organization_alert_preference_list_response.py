from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_alert_preference_response import (
        OrganizationAlertPreferenceResponse,
    )


T = TypeVar("T", bound="OrganizationAlertPreferenceListResponse")


@_attrs_define
class OrganizationAlertPreferenceListResponse:
    """
    Attributes:
        preferences (list[OrganizationAlertPreferenceResponse]):
        total (int):
    """

    preferences: list[OrganizationAlertPreferenceResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preferences = []
        for preferences_item_data in self.preferences:
            preferences_item = preferences_item_data.to_dict()
            preferences.append(preferences_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preferences": preferences,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_alert_preference_response import (
            OrganizationAlertPreferenceResponse,
        )

        d = dict(src_dict)
        preferences = []
        _preferences = d.pop("preferences")
        for preferences_item_data in _preferences:
            preferences_item = OrganizationAlertPreferenceResponse.from_dict(
                preferences_item_data
            )

            preferences.append(preferences_item)

        total = d.pop("total")

        organization_alert_preference_list_response = cls(
            preferences=preferences,
            total=total,
        )

        organization_alert_preference_list_response.additional_properties = d
        return organization_alert_preference_list_response

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
