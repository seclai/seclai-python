from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActivityCreditUsageResponse")


@_attrs_define
class ActivityCreditUsageResponse:
    """
    Attributes:
        activity (str):
        credits_ (float):
        origin (str):
    """

    activity: str
    credits_: float
    origin: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = self.activity

        credits_ = self.credits_

        origin = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity": activity,
                "credits": credits_,
                "origin": origin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity = d.pop("activity")

        credits_ = d.pop("credits")

        origin = d.pop("origin")

        activity_credit_usage_response = cls(
            activity=activity,
            credits_=credits_,
            origin=origin,
        )

        activity_credit_usage_response.additional_properties = d
        return activity_credit_usage_response

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
