from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreditPurchaseWithPaymentMethodRequest")


@_attrs_define
class CreditPurchaseWithPaymentMethodRequest:
    """
    Attributes:
        amount (float): Amount to spend on credits ($10 - $1,000)
        payment_method_id (str): ID of the existing payment method to use
    """

    amount: float
    payment_method_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        payment_method_id = self.payment_method_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "payment_method_id": payment_method_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        payment_method_id = d.pop("payment_method_id")

        credit_purchase_with_payment_method_request = cls(
            amount=amount,
            payment_method_id=payment_method_id,
        )

        credit_purchase_with_payment_method_request.additional_properties = d
        return credit_purchase_with_payment_method_request

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
