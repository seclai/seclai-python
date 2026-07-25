from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsProviderResponse")


@_attrs_define
class DnsProviderResponse:
    """
    Attributes:
        key (str):
        name (str):
        dashboard_url (None | str | Unset):
        mx_priority_separate (bool | Unset):  Default: True.
        tips (list[str] | Unset):
        txt_quotes (str | Unset):  Default: 'strip'.
    """

    key: str
    name: str
    dashboard_url: None | str | Unset = UNSET
    mx_priority_separate: bool | Unset = True
    tips: list[str] | Unset = UNSET
    txt_quotes: str | Unset = "strip"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        dashboard_url: None | str | Unset
        if isinstance(self.dashboard_url, Unset):
            dashboard_url = UNSET
        else:
            dashboard_url = self.dashboard_url

        mx_priority_separate = self.mx_priority_separate

        tips: list[str] | Unset = UNSET
        if not isinstance(self.tips, Unset):
            tips = self.tips

        txt_quotes = self.txt_quotes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
            }
        )
        if dashboard_url is not UNSET:
            field_dict["dashboard_url"] = dashboard_url
        if mx_priority_separate is not UNSET:
            field_dict["mx_priority_separate"] = mx_priority_separate
        if tips is not UNSET:
            field_dict["tips"] = tips
        if txt_quotes is not UNSET:
            field_dict["txt_quotes"] = txt_quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        def _parse_dashboard_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_url = _parse_dashboard_url(d.pop("dashboard_url", UNSET))

        mx_priority_separate = d.pop("mx_priority_separate", UNSET)

        tips = cast(list[str], d.pop("tips", UNSET))

        txt_quotes = d.pop("txt_quotes", UNSET)

        dns_provider_response = cls(
            key=key,
            name=name,
            dashboard_url=dashboard_url,
            mx_priority_separate=mx_priority_separate,
            tips=tips,
            txt_quotes=txt_quotes,
        )

        dns_provider_response.additional_properties = d
        return dns_provider_response

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
