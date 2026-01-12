from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DefaultChunkingConfig")


@_attrs_define
class DefaultChunkingConfig:
    """Default chunking configuration

    Attributes:
        chunk_mode (str): Default chunking mode: 'custom' or 'language'
        chunk_overlap (int): Default chunk overlap in characters
        chunk_size (int): Default chunk size in characters
    """

    chunk_mode: str
    chunk_overlap: int
    chunk_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunk_mode = self.chunk_mode

        chunk_overlap = self.chunk_overlap

        chunk_size = self.chunk_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_mode": chunk_mode,
                "chunk_overlap": chunk_overlap,
                "chunk_size": chunk_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_mode = d.pop("chunk_mode")

        chunk_overlap = d.pop("chunk_overlap")

        chunk_size = d.pop("chunk_size")

        default_chunking_config = cls(
            chunk_mode=chunk_mode,
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
        )

        default_chunking_config.additional_properties = d
        return default_chunking_config

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
