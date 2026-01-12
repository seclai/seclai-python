from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.membership_type import MembershipType

T = TypeVar("T", bound="MembershipUpdateRequest")


@_attrs_define
class MembershipUpdateRequest:
    """Request model for updating a member's role.

    Attributes:
        membership_type (MembershipType): Organization membership types
    """

    membership_type: MembershipType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        membership_type = self.membership_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "membership_type": membership_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        membership_type = MembershipType(d.pop("membership_type"))

        membership_update_request = cls(
            membership_type=membership_type,
        )

        membership_update_request.additional_properties = d
        return membership_update_request

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
