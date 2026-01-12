from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_detail_activity_response import UsageDetailActivityResponse


T = TypeVar("T", bound="UsageOriginSliceResponse")


@_attrs_define
class UsageOriginSliceResponse:
    """
    Attributes:
        activities (list[UsageDetailActivityResponse]):
        credits_ (float):
        start (str):
    """

    activities: list[UsageDetailActivityResponse]
    credits_: float
    start: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = []
        for activities_item_data in self.activities:
            activities_item = activities_item_data.to_dict()
            activities.append(activities_item)

        credits_ = self.credits_

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
                "credits": credits_,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_detail_activity_response import UsageDetailActivityResponse

        d = dict(src_dict)
        activities = []
        _activities = d.pop("activities")
        for activities_item_data in _activities:
            activities_item = UsageDetailActivityResponse.from_dict(activities_item_data)

            activities.append(activities_item)

        credits_ = d.pop("credits")

        start = d.pop("start")

        usage_origin_slice_response = cls(
            activities=activities,
            credits_=credits_,
            start=start,
        )

        usage_origin_slice_response.additional_properties = d
        return usage_origin_slice_response

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
