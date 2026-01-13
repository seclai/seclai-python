from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_intent_status_response_payment_intent_type_0 import (
        PaymentIntentStatusResponsePaymentIntentType0,
    )


T = TypeVar("T", bound="PaymentIntentStatusResponse")


@_attrs_define
class PaymentIntentStatusResponse:
    """
    Attributes:
        message (str):
        success (bool):
        payment_intent (None | PaymentIntentStatusResponsePaymentIntentType0 | Unset):
    """

    message: str
    success: bool
    payment_intent: None | PaymentIntentStatusResponsePaymentIntentType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_intent_status_response_payment_intent_type_0 import (
            PaymentIntentStatusResponsePaymentIntentType0,
        )

        message = self.message

        success = self.success

        payment_intent: dict[str, Any] | None | Unset
        if isinstance(self.payment_intent, Unset):
            payment_intent = UNSET
        elif isinstance(self.payment_intent, PaymentIntentStatusResponsePaymentIntentType0):
            payment_intent = self.payment_intent.to_dict()
        else:
            payment_intent = self.payment_intent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "success": success,
            }
        )
        if payment_intent is not UNSET:
            field_dict["payment_intent"] = payment_intent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_intent_status_response_payment_intent_type_0 import (
            PaymentIntentStatusResponsePaymentIntentType0,
        )

        d = dict(src_dict)
        message = d.pop("message")

        success = d.pop("success")

        def _parse_payment_intent(
            data: object,
        ) -> None | PaymentIntentStatusResponsePaymentIntentType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_intent_type_0 = PaymentIntentStatusResponsePaymentIntentType0.from_dict(data)

                return payment_intent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaymentIntentStatusResponsePaymentIntentType0 | Unset, data)

        payment_intent = _parse_payment_intent(d.pop("payment_intent", UNSET))

        payment_intent_status_response = cls(
            message=message,
            success=success,
            payment_intent=payment_intent,
        )

        payment_intent_status_response.additional_properties = d
        return payment_intent_status_response

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
