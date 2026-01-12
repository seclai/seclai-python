from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateStopAtBudgetLimitRequest")


@_attrs_define
class UpdateStopAtBudgetLimitRequest:
    """
    Attributes:
        stop_at_budget_limit (bool):
    """

    stop_at_budget_limit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_at_budget_limit = self.stop_at_budget_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stop_at_budget_limit": stop_at_budget_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stop_at_budget_limit = d.pop("stop_at_budget_limit")

        update_stop_at_budget_limit_request = cls(
            stop_at_budget_limit=stop_at_budget_limit,
        )

        update_stop_at_budget_limit_request.additional_properties = d
        return update_stop_at_budget_limit_request

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
