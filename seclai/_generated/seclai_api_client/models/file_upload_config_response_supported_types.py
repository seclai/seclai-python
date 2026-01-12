from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_upload_config_response_supported_types_additional_property import (
        FileUploadConfigResponseSupportedTypesAdditionalProperty,
    )


T = TypeVar("T", bound="FileUploadConfigResponseSupportedTypes")


@_attrs_define
class FileUploadConfigResponseSupportedTypes:
    """Map of MIME types to file info with 'ext' and 'category' keys"""

    additional_properties: dict[
        str, FileUploadConfigResponseSupportedTypesAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_upload_config_response_supported_types_additional_property import (
            FileUploadConfigResponseSupportedTypesAdditionalProperty,
        )

        d = dict(src_dict)
        file_upload_config_response_supported_types = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                FileUploadConfigResponseSupportedTypesAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        file_upload_config_response_supported_types.additional_properties = (
            additional_properties
        )
        return file_upload_config_response_supported_types

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> FileUploadConfigResponseSupportedTypesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: FileUploadConfigResponseSupportedTypesAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
