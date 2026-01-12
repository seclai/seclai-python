from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionResponse")


@_attrs_define
class SubscriptionResponse:
    """Response model for subscription information.

    Attributes:
        created_at (str):
        id (str):
        is_trial (bool):
        plan_id (str):
        plan_name (str):
        status (str):
        updated_at (str):
        billing_cycle_anchor (None | str | Unset):
        current_period_end (None | str | Unset):
        current_period_start (None | str | Unset):
        trial_end_date (None | str | Unset):
    """

    created_at: str
    id: str
    is_trial: bool
    plan_id: str
    plan_name: str
    status: str
    updated_at: str
    billing_cycle_anchor: None | str | Unset = UNSET
    current_period_end: None | str | Unset = UNSET
    current_period_start: None | str | Unset = UNSET
    trial_end_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        is_trial = self.is_trial

        plan_id = self.plan_id

        plan_name = self.plan_name

        status = self.status

        updated_at = self.updated_at

        billing_cycle_anchor: None | str | Unset
        if isinstance(self.billing_cycle_anchor, Unset):
            billing_cycle_anchor = UNSET
        else:
            billing_cycle_anchor = self.billing_cycle_anchor

        current_period_end: None | str | Unset
        if isinstance(self.current_period_end, Unset):
            current_period_end = UNSET
        else:
            current_period_end = self.current_period_end

        current_period_start: None | str | Unset
        if isinstance(self.current_period_start, Unset):
            current_period_start = UNSET
        else:
            current_period_start = self.current_period_start

        trial_end_date: None | str | Unset
        if isinstance(self.trial_end_date, Unset):
            trial_end_date = UNSET
        else:
            trial_end_date = self.trial_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "is_trial": is_trial,
                "plan_id": plan_id,
                "plan_name": plan_name,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if billing_cycle_anchor is not UNSET:
            field_dict["billing_cycle_anchor"] = billing_cycle_anchor
        if current_period_end is not UNSET:
            field_dict["current_period_end"] = current_period_end
        if current_period_start is not UNSET:
            field_dict["current_period_start"] = current_period_start
        if trial_end_date is not UNSET:
            field_dict["trial_end_date"] = trial_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = d.pop("id")

        is_trial = d.pop("is_trial")

        plan_id = d.pop("plan_id")

        plan_name = d.pop("plan_name")

        status = d.pop("status")

        updated_at = d.pop("updated_at")

        def _parse_billing_cycle_anchor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_cycle_anchor = _parse_billing_cycle_anchor(
            d.pop("billing_cycle_anchor", UNSET)
        )

        def _parse_current_period_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_period_end = _parse_current_period_end(
            d.pop("current_period_end", UNSET)
        )

        def _parse_current_period_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_period_start = _parse_current_period_start(
            d.pop("current_period_start", UNSET)
        )

        def _parse_trial_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trial_end_date = _parse_trial_end_date(d.pop("trial_end_date", UNSET))

        subscription_response = cls(
            created_at=created_at,
            id=id,
            is_trial=is_trial,
            plan_id=plan_id,
            plan_name=plan_name,
            status=status,
            updated_at=updated_at,
            billing_cycle_anchor=billing_cycle_anchor,
            current_period_end=current_period_end,
            current_period_start=current_period_start,
            trial_end_date=trial_end_date,
        )

        subscription_response.additional_properties = d
        return subscription_response

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
