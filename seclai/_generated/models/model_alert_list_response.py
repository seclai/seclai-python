from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_alert_response import ModelAlertResponse


T = TypeVar("T", bound="ModelAlertListResponse")


@_attrs_define
class ModelAlertListResponse:
    """``GET /models/alerts`` legacy/default shape; 2026-07-27+ clients get the
    canonical ``{data, pagination}`` envelope (bypasses this ``response_model``).

        Attributes:
            alerts (list[ModelAlertResponse]):
            total (int):
    """

    alerts: list[ModelAlertResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alerts = []
        for alerts_item_data in self.alerts:
            alerts_item = alerts_item_data.to_dict()
            alerts.append(alerts_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alerts": alerts,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_alert_response import ModelAlertResponse

        d = dict(src_dict)
        alerts = []
        _alerts = d.pop("alerts")
        for alerts_item_data in _alerts:
            alerts_item = ModelAlertResponse.from_dict(alerts_item_data)

            alerts.append(alerts_item)

        total = d.pop("total")

        model_alert_list_response = cls(
            alerts=alerts,
            total=total,
        )

        model_alert_list_response.additional_properties = d
        return model_alert_list_response

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
