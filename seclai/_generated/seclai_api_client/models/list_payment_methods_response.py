from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_response import PaymentMethodResponse


T = TypeVar("T", bound="ListPaymentMethodsResponse")


@_attrs_define
class ListPaymentMethodsResponse:
    """
    Attributes:
        payment_methods (list[PaymentMethodResponse]):
        success (bool):
        message (str | Unset):  Default: ''.
    """

    payment_methods: list[PaymentMethodResponse]
    success: bool
    message: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_methods = []
        for payment_methods_item_data in self.payment_methods:
            payment_methods_item = payment_methods_item_data.to_dict()
            payment_methods.append(payment_methods_item)

        success = self.success

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_methods": payment_methods,
                "success": success,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_method_response import PaymentMethodResponse

        d = dict(src_dict)
        payment_methods = []
        _payment_methods = d.pop("payment_methods")
        for payment_methods_item_data in _payment_methods:
            payment_methods_item = PaymentMethodResponse.from_dict(payment_methods_item_data)

            payment_methods.append(payment_methods_item)

        success = d.pop("success")

        message = d.pop("message", UNSET)

        list_payment_methods_response = cls(
            payment_methods=payment_methods,
            success=success,
            message=message,
        )

        list_payment_methods_response.additional_properties = d
        return list_payment_methods_response

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
