from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadFileToSourceAuthenticatedSourcesSourceConnectionIdUploadPost")


@_attrs_define
class BodyUploadFileToSourceAuthenticatedSourcesSourceConnectionIdUploadPost:
    """
    Attributes:
        file (File): File to upload
        title (str | Unset): Optional title for the content
    """

    file: File
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        title = d.pop("title", UNSET)

        body_upload_file_to_source_authenticated_sources_source_connection_id_upload_post = cls(
            file=file,
            title=title,
        )

        body_upload_file_to_source_authenticated_sources_source_connection_id_upload_post.additional_properties = d
        return body_upload_file_to_source_authenticated_sources_source_connection_id_upload_post

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
