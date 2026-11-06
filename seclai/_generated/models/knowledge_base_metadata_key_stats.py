from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_key_window_response import MetadataKeyWindowResponse


T = TypeVar("T", bound="KnowledgeBaseMetadataKeyStats")


@_attrs_define
class KnowledgeBaseMetadataKeyStats:
    """
    Attributes:
        knowledge_base_id (str):
        windows (list[MetadataKeyWindowResponse]):
    """

    knowledge_base_id: str
    windows: list[MetadataKeyWindowResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_base_id = self.knowledge_base_id

        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_base_id": knowledge_base_id,
                "windows": windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_key_window_response import MetadataKeyWindowResponse

        d = dict(src_dict)
        knowledge_base_id = d.pop("knowledge_base_id")

        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = MetadataKeyWindowResponse.from_dict(windows_item_data)

            windows.append(windows_item)

        knowledge_base_metadata_key_stats = cls(
            knowledge_base_id=knowledge_base_id,
            windows=windows,
        )

        knowledge_base_metadata_key_stats.additional_properties = d
        return knowledge_base_metadata_key_stats

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
