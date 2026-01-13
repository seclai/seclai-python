from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_intent_history_item import PaymentIntentHistoryItem


T = TypeVar("T", bound="PaymentIntentHistoryResponse")


@_attrs_define
class PaymentIntentHistoryResponse:
    """
    Attributes:
        page (int):
        payment_intents (list[PaymentIntentHistoryItem]):
        per_page (int):
        success (bool):
        total (int):
        message (str | Unset):  Default: ''.
    """

    page: int
    payment_intents: list[PaymentIntentHistoryItem]
    per_page: int
    success: bool
    total: int
    message: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        payment_intents = []
        for payment_intents_item_data in self.payment_intents:
            payment_intents_item = payment_intents_item_data.to_dict()
            payment_intents.append(payment_intents_item)

        per_page = self.per_page

        success = self.success

        total = self.total

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "payment_intents": payment_intents,
                "per_page": per_page,
                "success": success,
                "total": total,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_intent_history_item import PaymentIntentHistoryItem

        d = dict(src_dict)
        page = d.pop("page")

        payment_intents = []
        _payment_intents = d.pop("payment_intents")
        for payment_intents_item_data in _payment_intents:
            payment_intents_item = PaymentIntentHistoryItem.from_dict(payment_intents_item_data)

            payment_intents.append(payment_intents_item)

        per_page = d.pop("per_page")

        success = d.pop("success")

        total = d.pop("total")

        message = d.pop("message", UNSET)

        payment_intent_history_response = cls(
            page=page,
            payment_intents=payment_intents,
            per_page=per_page,
            success=success,
            total=total,
            message=message,
        )

        payment_intent_history_response.additional_properties = d
        return payment_intent_history_response

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
