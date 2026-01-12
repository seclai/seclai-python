from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_upload_config_response_supported_types import FileUploadConfigResponseSupportedTypes


T = TypeVar("T", bound="FileUploadConfigResponse")


@_attrs_define
class FileUploadConfigResponse:
    """Response model for file upload configuration

    Attributes:
        max_file_size (int): Maximum file size in bytes
        supported_types (FileUploadConfigResponseSupportedTypes): Map of MIME types to file info with 'ext' and
            'category' keys
    """

    max_file_size: int
    supported_types: FileUploadConfigResponseSupportedTypes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_file_size = self.max_file_size

        supported_types = self.supported_types.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_file_size": max_file_size,
                "supported_types": supported_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_upload_config_response_supported_types import FileUploadConfigResponseSupportedTypes

        d = dict(src_dict)
        max_file_size = d.pop("max_file_size")

        supported_types = FileUploadConfigResponseSupportedTypes.from_dict(d.pop("supported_types"))

        file_upload_config_response = cls(
            max_file_size=max_file_size,
            supported_types=supported_types,
        )

        file_upload_config_response.additional_properties = d
        return file_upload_config_response

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
