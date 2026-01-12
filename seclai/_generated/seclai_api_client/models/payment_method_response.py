from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.payment_method_response_card import PaymentMethodResponseCard


T = TypeVar("T", bound="PaymentMethodResponse")


@_attrs_define
class PaymentMethodResponse:
    """
    Attributes:
        card (PaymentMethodResponseCard):
        id (str):
        is_default (bool):
        type_ (str):
    """

    card: PaymentMethodResponseCard
    id: str
    is_default: bool
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        id = self.id

        is_default = self.is_default

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
                "id": id,
                "is_default": is_default,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_method_response_card import PaymentMethodResponseCard

        d = dict(src_dict)
        card = PaymentMethodResponseCard.from_dict(d.pop("card"))

        id = d.pop("id")

        is_default = d.pop("is_default")

        type_ = d.pop("type")

        payment_method_response = cls(
            card=card,
            id=id,
            is_default=is_default,
            type_=type_,
        )

        payment_method_response.additional_properties = d
        return payment_method_response

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
