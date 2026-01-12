from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartSubscriptionResponse")


@_attrs_define
class StartSubscriptionResponse:
    """
    Attributes:
        message (str):
        stripe_client_secret (None | str | Unset):
        success (bool | Unset):  Default: False.
    """

    message: str
    stripe_client_secret: None | str | Unset = UNSET
    success: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        stripe_client_secret: None | str | Unset
        if isinstance(self.stripe_client_secret, Unset):
            stripe_client_secret = UNSET
        else:
            stripe_client_secret = self.stripe_client_secret

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if stripe_client_secret is not UNSET:
            field_dict["stripe_client_secret"] = stripe_client_secret
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        def _parse_stripe_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_client_secret = _parse_stripe_client_secret(
            d.pop("stripe_client_secret", UNSET)
        )

        success = d.pop("success", UNSET)

        start_subscription_response = cls(
            message=message,
            stripe_client_secret=stripe_client_secret,
            success=success,
        )

        start_subscription_response.additional_properties = d
        return start_subscription_response

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
