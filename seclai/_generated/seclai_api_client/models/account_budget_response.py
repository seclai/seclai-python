from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.activity_budget_response import ActivityBudgetResponse


T = TypeVar("T", bound="AccountBudgetResponse")


@_attrs_define
class AccountBudgetResponse:
    """
    Attributes:
        account_credits (int):
        activity_budgets (list[ActivityBudgetResponse]):
        auto_purchase_overages (bool):
        monthly_overage_budget (int):
        pending_credits (int):
        stop_at_budget_limit (bool):
    """

    account_credits: int
    activity_budgets: list[ActivityBudgetResponse]
    auto_purchase_overages: bool
    monthly_overage_budget: int
    pending_credits: int
    stop_at_budget_limit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_credits = self.account_credits

        activity_budgets = []
        for activity_budgets_item_data in self.activity_budgets:
            activity_budgets_item = activity_budgets_item_data.to_dict()
            activity_budgets.append(activity_budgets_item)

        auto_purchase_overages = self.auto_purchase_overages

        monthly_overage_budget = self.monthly_overage_budget

        pending_credits = self.pending_credits

        stop_at_budget_limit = self.stop_at_budget_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_credits": account_credits,
                "activity_budgets": activity_budgets,
                "auto_purchase_overages": auto_purchase_overages,
                "monthly_overage_budget": monthly_overage_budget,
                "pending_credits": pending_credits,
                "stop_at_budget_limit": stop_at_budget_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_budget_response import ActivityBudgetResponse

        d = dict(src_dict)
        account_credits = d.pop("account_credits")

        activity_budgets = []
        _activity_budgets = d.pop("activity_budgets")
        for activity_budgets_item_data in _activity_budgets:
            activity_budgets_item = ActivityBudgetResponse.from_dict(activity_budgets_item_data)

            activity_budgets.append(activity_budgets_item)

        auto_purchase_overages = d.pop("auto_purchase_overages")

        monthly_overage_budget = d.pop("monthly_overage_budget")

        pending_credits = d.pop("pending_credits")

        stop_at_budget_limit = d.pop("stop_at_budget_limit")

        account_budget_response = cls(
            account_credits=account_credits,
            activity_budgets=activity_budgets,
            auto_purchase_overages=auto_purchase_overages,
            monthly_overage_budget=monthly_overage_budget,
            pending_credits=pending_credits,
            stop_at_budget_limit=stop_at_budget_limit,
        )

        account_budget_response.additional_properties = d
        return account_budget_response

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
