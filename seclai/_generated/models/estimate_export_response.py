from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EstimateExportResponse")


@_attrs_define
class EstimateExportResponse:
    """Rough size estimate for a potential export.

    Attributes:
        estimated_size_bytes (int): Estimated export file size in bytes.
        source_connection_id (str): Source connection ID.
    """

    estimated_size_bytes: int
    source_connection_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        estimated_size_bytes = self.estimated_size_bytes

        source_connection_id = self.source_connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "estimated_size_bytes": estimated_size_bytes,
                "source_connection_id": source_connection_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        estimated_size_bytes = d.pop("estimated_size_bytes")

        source_connection_id = d.pop("source_connection_id")

        estimate_export_response = cls(
            estimated_size_bytes=estimated_size_bytes,
            source_connection_id=source_connection_id,
        )

        estimate_export_response.additional_properties = d
        return estimate_export_response

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
