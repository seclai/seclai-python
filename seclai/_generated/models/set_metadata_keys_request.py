from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_key_declaration import MetadataKeyDeclaration


T = TypeVar("T", bound="SetMetadataKeysRequest")


@_attrs_define
class SetMetadataKeysRequest:
    """
    Attributes:
        metadata_keys (list[MetadataKeyDeclaration]): The whole declaration; replaces the trigger's current one.
    """

    metadata_keys: list[MetadataKeyDeclaration]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_keys = []
        for metadata_keys_item_data in self.metadata_keys:
            metadata_keys_item = metadata_keys_item_data.to_dict()
            metadata_keys.append(metadata_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata_keys": metadata_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_key_declaration import MetadataKeyDeclaration

        d = dict(src_dict)
        metadata_keys = []
        _metadata_keys = d.pop("metadata_keys")
        for metadata_keys_item_data in _metadata_keys:
            metadata_keys_item = MetadataKeyDeclaration.from_dict(
                metadata_keys_item_data
            )

            metadata_keys.append(metadata_keys_item)

        set_metadata_keys_request = cls(
            metadata_keys=metadata_keys,
        )

        set_metadata_keys_request.additional_properties = d
        return set_metadata_keys_request

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
