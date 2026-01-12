from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaymentIntentHistoryItem")


@_attrs_define
class PaymentIntentHistoryItem:
    """
    Attributes:
        amount (int):
        created_at (str):
        currency (str):
        description (str):
        id (str):
        payment_type (str):
        statement (str):
        status (str):
    """

    amount: int
    created_at: str
    currency: str
    description: str
    id: str
    payment_type: str
    statement: str
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at

        currency = self.currency

        description = self.description

        id = self.id

        payment_type = self.payment_type

        statement = self.statement

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "created_at": created_at,
                "currency": currency,
                "description": description,
                "id": id,
                "payment_type": payment_type,
                "statement": statement,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        created_at = d.pop("created_at")

        currency = d.pop("currency")

        description = d.pop("description")

        id = d.pop("id")

        payment_type = d.pop("payment_type")

        statement = d.pop("statement")

        status = d.pop("status")

        payment_intent_history_item = cls(
            amount=amount,
            created_at=created_at,
            currency=currency,
            description=description,
            id=id,
            payment_type=payment_type,
            statement=statement,
            status=status,
        )

        payment_intent_history_item.additional_properties = d
        return payment_intent_history_item

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
