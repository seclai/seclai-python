from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartSubscriptionRequest")


@_attrs_define
class StartSubscriptionRequest:
    """
    Attributes:
        plan_id (UUID):
        payment_method_id (None | str | Unset):
    """

    plan_id: UUID
    payment_method_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_id = str(self.plan_id)

        payment_method_id: None | str | Unset
        if isinstance(self.payment_method_id, Unset):
            payment_method_id = UNSET
        else:
            payment_method_id = self.payment_method_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan_id": plan_id,
            }
        )
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_id = UUID(d.pop("plan_id"))

        def _parse_payment_method_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method_id = _parse_payment_method_id(d.pop("payment_method_id", UNSET))

        start_subscription_request = cls(
            plan_id=plan_id,
            payment_method_id=payment_method_id,
        )

        start_subscription_request.additional_properties = d
        return start_subscription_request

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
