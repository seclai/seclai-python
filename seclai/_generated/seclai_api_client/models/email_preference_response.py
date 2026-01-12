from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmailPreferenceResponse")


@_attrs_define
class EmailPreferenceResponse:
    """Response model for email preference

    Attributes:
        email_type (str): Type of email
        mandatory (bool): Whether this preference is mandatory
        subscribed (bool): Whether user is subscribed
    """

    email_type: str
    mandatory: bool
    subscribed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_type = self.email_type

        mandatory = self.mandatory

        subscribed = self.subscribed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_type": email_type,
                "mandatory": mandatory,
                "subscribed": subscribed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_type = d.pop("email_type")

        mandatory = d.pop("mandatory")

        subscribed = d.pop("subscribed")

        email_preference_response = cls(
            email_type=email_type,
            mandatory=mandatory,
            subscribed=subscribed,
        )

        email_preference_response.additional_properties = d
        return email_preference_response

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
