from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationResponse")


@_attrs_define
class OrganizationResponse:
    """Response model for organization data.

    Attributes:
        created_at (str):
        description (None | str):
        id (str):
        independent_billing (bool):
        member_count (int):
        monthly_credit_limit (int | None):
        name (str):
        updated_at (str):
        user_role (str):
    """

    created_at: str
    description: None | str
    id: str
    independent_billing: bool
    member_count: int
    monthly_credit_limit: int | None
    name: str
    updated_at: str
    user_role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description: None | str
        description = self.description

        id = self.id

        independent_billing = self.independent_billing

        member_count = self.member_count

        monthly_credit_limit: int | None
        monthly_credit_limit = self.monthly_credit_limit

        name = self.name

        updated_at = self.updated_at

        user_role = self.user_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "independent_billing": independent_billing,
                "member_count": member_count,
                "monthly_credit_limit": monthly_credit_limit,
                "name": name,
                "updated_at": updated_at,
                "user_role": user_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = d.pop("id")

        independent_billing = d.pop("independent_billing")

        member_count = d.pop("member_count")

        def _parse_monthly_credit_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monthly_credit_limit = _parse_monthly_credit_limit(d.pop("monthly_credit_limit"))

        name = d.pop("name")

        updated_at = d.pop("updated_at")

        user_role = d.pop("user_role")

        organization_response = cls(
            created_at=created_at,
            description=description,
            id=id,
            independent_billing=independent_billing,
            member_count=member_count,
            monthly_credit_limit=monthly_credit_limit,
            name=name,
            updated_at=updated_at,
            user_role=user_role,
        )

        organization_response.additional_properties = d
        return organization_response

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
