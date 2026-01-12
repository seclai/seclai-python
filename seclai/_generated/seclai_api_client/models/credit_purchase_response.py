from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditPurchaseResponse")


@_attrs_define
class CreditPurchaseResponse:
    """
    Attributes:
        message (str):
        success (bool):
        client_secret (None | str | Unset):
        credits_ (int | None | Unset):
        payment_intent_id (None | str | Unset):
    """

    message: str
    success: bool
    client_secret: None | str | Unset = UNSET
    credits_: int | None | Unset = UNSET
    payment_intent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        success = self.success

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        credits_: int | None | Unset
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = self.credits_

        payment_intent_id: None | str | Unset
        if isinstance(self.payment_intent_id, Unset):
            payment_intent_id = UNSET
        else:
            payment_intent_id = self.payment_intent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "success": success,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if payment_intent_id is not UNSET:
            field_dict["payment_intent_id"] = payment_intent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        success = d.pop("success")

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_credits_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        def _parse_payment_intent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_intent_id = _parse_payment_intent_id(d.pop("payment_intent_id", UNSET))

        credit_purchase_response = cls(
            message=message,
            success=success,
            client_secret=client_secret,
            credits_=credits_,
            payment_intent_id=payment_intent_id,
        )

        credit_purchase_response.additional_properties = d
        return credit_purchase_response

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
