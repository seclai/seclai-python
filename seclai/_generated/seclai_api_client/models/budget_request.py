from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BudgetRequest")


@_attrs_define
class BudgetRequest:
    """Request model for creating or updating a budget.

    Attributes:
        budget_limit (int): Budget limit in appropriate units
        stop_usage_at_limit (bool): Whether to stop usage when limit is reached
    """

    budget_limit: int
    stop_usage_at_limit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_limit = self.budget_limit

        stop_usage_at_limit = self.stop_usage_at_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_limit": budget_limit,
                "stop_usage_at_limit": stop_usage_at_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_limit = d.pop("budget_limit")

        stop_usage_at_limit = d.pop("stop_usage_at_limit")

        budget_request = cls(
            budget_limit=budget_limit,
            stop_usage_at_limit=stop_usage_at_limit,
        )

        budget_request.additional_properties = d
        return budget_request

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
