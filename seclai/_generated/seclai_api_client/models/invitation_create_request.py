from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.membership_type import MembershipType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationCreateRequest")


@_attrs_define
class InvitationCreateRequest:
    """Request model for creating an organization invitation.

    Attributes:
        email (str):
        membership_type (MembershipType | Unset): Organization membership types
    """

    email: str
    membership_type: MembershipType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        membership_type: str | Unset = UNSET
        if not isinstance(self.membership_type, Unset):
            membership_type = self.membership_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if membership_type is not UNSET:
            field_dict["membership_type"] = membership_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _membership_type = d.pop("membership_type", UNSET)
        membership_type: MembershipType | Unset
        if isinstance(_membership_type, Unset):
            membership_type = UNSET
        else:
            membership_type = MembershipType(_membership_type)

        invitation_create_request = cls(
            email=email,
            membership_type=membership_type,
        )

        invitation_create_request.additional_properties = d
        return invitation_create_request

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
