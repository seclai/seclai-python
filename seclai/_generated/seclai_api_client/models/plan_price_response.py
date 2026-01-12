from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlanPriceResponse")


@_attrs_define
class PlanPriceResponse:
    """Response model for plan pricing.

    Attributes:
        available_at (None | str):
        currency (str):
        expires_at (None | str):
        id (str):
        price (float):
    """

    available_at: None | str
    currency: str
    expires_at: None | str
    id: str
    price: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_at: None | str
        available_at = self.available_at

        currency = self.currency

        expires_at: None | str
        expires_at = self.expires_at

        id = self.id

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_at": available_at,
                "currency": currency,
                "expires_at": expires_at,
                "id": id,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_available_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        available_at = _parse_available_at(d.pop("available_at"))

        currency = d.pop("currency")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        id = d.pop("id")

        price = d.pop("price")

        plan_price_response = cls(
            available_at=available_at,
            currency=currency,
            expires_at=expires_at,
            id=id,
            price=price,
        )

        plan_price_response.additional_properties = d
        return plan_price_response

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
