from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_domain_response import EmailDomainResponse


T = TypeVar("T", bound="EmailDomainsListResponse")


@_attrs_define
class EmailDomainsListResponse:
    """
    Attributes:
        can_add_custom (bool | Unset):  Default: False.
        can_add_vanity (bool | Unset):  Default: False.
        custom_plan_names (list[str] | Unset):
        domains (list[EmailDomainResponse] | Unset):
        has_custom (bool | Unset):  Default: False.
        has_vanity (bool | Unset):  Default: False.
        vanity_plan_names (list[str] | Unset):
    """

    can_add_custom: bool | Unset = False
    can_add_vanity: bool | Unset = False
    custom_plan_names: list[str] | Unset = UNSET
    domains: list[EmailDomainResponse] | Unset = UNSET
    has_custom: bool | Unset = False
    has_vanity: bool | Unset = False
    vanity_plan_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_add_custom = self.can_add_custom

        can_add_vanity = self.can_add_vanity

        custom_plan_names: list[str] | Unset = UNSET
        if not isinstance(self.custom_plan_names, Unset):
            custom_plan_names = self.custom_plan_names

        domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for domains_item_data in self.domains:
                domains_item = domains_item_data.to_dict()
                domains.append(domains_item)

        has_custom = self.has_custom

        has_vanity = self.has_vanity

        vanity_plan_names: list[str] | Unset = UNSET
        if not isinstance(self.vanity_plan_names, Unset):
            vanity_plan_names = self.vanity_plan_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_add_custom is not UNSET:
            field_dict["can_add_custom"] = can_add_custom
        if can_add_vanity is not UNSET:
            field_dict["can_add_vanity"] = can_add_vanity
        if custom_plan_names is not UNSET:
            field_dict["custom_plan_names"] = custom_plan_names
        if domains is not UNSET:
            field_dict["domains"] = domains
        if has_custom is not UNSET:
            field_dict["has_custom"] = has_custom
        if has_vanity is not UNSET:
            field_dict["has_vanity"] = has_vanity
        if vanity_plan_names is not UNSET:
            field_dict["vanity_plan_names"] = vanity_plan_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_domain_response import EmailDomainResponse

        d = dict(src_dict)
        can_add_custom = d.pop("can_add_custom", UNSET)

        can_add_vanity = d.pop("can_add_vanity", UNSET)

        custom_plan_names = cast(list[str], d.pop("custom_plan_names", UNSET))

        _domains = d.pop("domains", UNSET)
        domains: list[EmailDomainResponse] | Unset = UNSET
        if _domains is not UNSET:
            domains = []
            for domains_item_data in _domains:
                domains_item = EmailDomainResponse.from_dict(domains_item_data)

                domains.append(domains_item)

        has_custom = d.pop("has_custom", UNSET)

        has_vanity = d.pop("has_vanity", UNSET)

        vanity_plan_names = cast(list[str], d.pop("vanity_plan_names", UNSET))

        email_domains_list_response = cls(
            can_add_custom=can_add_custom,
            can_add_vanity=can_add_vanity,
            custom_plan_names=custom_plan_names,
            domains=domains,
            has_custom=has_custom,
            has_vanity=has_vanity,
            vanity_plan_names=vanity_plan_names,
        )

        email_domains_list_response.additional_properties = d
        return email_domains_list_response

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
