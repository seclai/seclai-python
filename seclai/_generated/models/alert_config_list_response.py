from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_config_response import AlertConfigResponse


T = TypeVar("T", bound="AlertConfigListResponse")


@_attrs_define
class AlertConfigListResponse:
    """``GET /alerts/configs`` legacy/default shape (header-less clients).

    ``Seclai-Version: 2026-07-27+`` clients receive the canonical
    ``{data, pagination}`` envelope instead (the handler returns a ``JSONResponse``
    that bypasses this ``response_model``); this documents the default shape.

        Attributes:
            configs (list[AlertConfigResponse]):
            total (int):
    """

    configs: list[AlertConfigResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configs = []
        for configs_item_data in self.configs:
            configs_item = configs_item_data.to_dict()
            configs.append(configs_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configs": configs,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_config_response import AlertConfigResponse

        d = dict(src_dict)
        configs = []
        _configs = d.pop("configs")
        for configs_item_data in _configs:
            configs_item = AlertConfigResponse.from_dict(configs_item_data)

            configs.append(configs_item)

        total = d.pop("total")

        alert_config_list_response = cls(
            configs=configs,
            total=total,
        )

        alert_config_list_response.additional_properties = d
        return alert_config_list_response

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
