from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsRecordResponse")


@_attrs_define
class DnsRecordResponse:
    """
    Attributes:
        key (str):
        name (str):
        ok (bool):
        relative_name (str):
        type_ (str):
        value (str):
        detail (None | str | Unset):
        mx_host (None | str | Unset):
        mx_priority (int | None | Unset):
    """

    key: str
    name: str
    ok: bool
    relative_name: str
    type_: str
    value: str
    detail: None | str | Unset = UNSET
    mx_host: None | str | Unset = UNSET
    mx_priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        ok = self.ok

        relative_name = self.relative_name

        type_ = self.type_

        value = self.value

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        mx_host: None | str | Unset
        if isinstance(self.mx_host, Unset):
            mx_host = UNSET
        else:
            mx_host = self.mx_host

        mx_priority: int | None | Unset
        if isinstance(self.mx_priority, Unset):
            mx_priority = UNSET
        else:
            mx_priority = self.mx_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "ok": ok,
                "relative_name": relative_name,
                "type": type_,
                "value": value,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if mx_host is not UNSET:
            field_dict["mx_host"] = mx_host
        if mx_priority is not UNSET:
            field_dict["mx_priority"] = mx_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        ok = d.pop("ok")

        relative_name = d.pop("relative_name")

        type_ = d.pop("type")

        value = d.pop("value")

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_mx_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mx_host = _parse_mx_host(d.pop("mx_host", UNSET))

        def _parse_mx_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mx_priority = _parse_mx_priority(d.pop("mx_priority", UNSET))

        dns_record_response = cls(
            key=key,
            name=name,
            ok=ok,
            relative_name=relative_name,
            type_=type_,
            value=value,
            detail=detail,
            mx_host=mx_host,
            mx_priority=mx_priority,
        )

        dns_record_response.additional_properties = d
        return dns_record_response

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
