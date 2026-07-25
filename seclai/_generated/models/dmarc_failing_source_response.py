from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DmarcFailingSourceResponse")


@_attrs_define
class DmarcFailingSourceResponse:
    """
    Attributes:
        failed_count (int):
        source_ip (str):
        header_from (None | str | Unset):
    """

    failed_count: int
    source_ip: str
    header_from: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_count = self.failed_count

        source_ip = self.source_ip

        header_from: None | str | Unset
        if isinstance(self.header_from, Unset):
            header_from = UNSET
        else:
            header_from = self.header_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failed_count": failed_count,
                "source_ip": source_ip,
            }
        )
        if header_from is not UNSET:
            field_dict["header_from"] = header_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_count = d.pop("failed_count")

        source_ip = d.pop("source_ip")

        def _parse_header_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_from = _parse_header_from(d.pop("header_from", UNSET))

        dmarc_failing_source_response = cls(
            failed_count=failed_count,
            source_ip=source_ip,
            header_from=header_from,
        )

        dmarc_failing_source_response.additional_properties = d
        return dmarc_failing_source_response

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
