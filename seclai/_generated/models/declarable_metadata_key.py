from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_origin import MetadataOrigin

T = TypeVar("T", bound="DeclarableMetadataKey")


@_attrs_define
class DeclarableMetadataKey:
    """
    Attributes:
        always_present (bool): Whether every run carries this key.
        key (str):
        origin (MetadataOrigin): Who writes a run metadata key (docs/architecture/run-metadata.md, Q2).
    """

    always_present: bool
    key: str
    origin: MetadataOrigin
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        always_present = self.always_present

        key = self.key

        origin = self.origin.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "always_present": always_present,
                "key": key,
                "origin": origin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        always_present = d.pop("always_present")

        key = d.pop("key")

        origin = MetadataOrigin(d.pop("origin"))

        declarable_metadata_key = cls(
            always_present=always_present,
            key=key,
            origin=origin,
        )

        declarable_metadata_key.additional_properties = d
        return declarable_metadata_key

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
