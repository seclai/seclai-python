from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileUploadResponse")


@_attrs_define
class FileUploadResponse:
    """Response model for content file replacement upload.

    Attributes:
        content_version_id (None | str): ID of the content version being replaced
        filename (str): Original filename
        source_connection_content_version_id (None | str): ID of the source connection content version
        status (str): Processing status
    """

    content_version_id: None | str
    filename: str
    source_connection_content_version_id: None | str
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_version_id: None | str
        content_version_id = self.content_version_id

        filename = self.filename

        source_connection_content_version_id: None | str
        source_connection_content_version_id = self.source_connection_content_version_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_version_id": content_version_id,
                "filename": filename,
                "source_connection_content_version_id": source_connection_content_version_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content_version_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_version_id = _parse_content_version_id(d.pop("content_version_id"))

        filename = d.pop("filename")

        def _parse_source_connection_content_version_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_connection_content_version_id = _parse_source_connection_content_version_id(
            d.pop("source_connection_content_version_id")
        )

        status = d.pop("status")

        file_upload_response = cls(
            content_version_id=content_version_id,
            filename=filename,
            source_connection_content_version_id=source_connection_content_version_id,
            status=status,
        )

        file_upload_response.additional_properties = d
        return file_upload_response

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
