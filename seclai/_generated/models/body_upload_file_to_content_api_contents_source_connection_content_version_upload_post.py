from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost")


@_attrs_define
class BodyUploadFileToContentApiContentsSourceConnectionContentVersionUploadPost:
    """
    Attributes:
        file (File): File to upload
        metadata (None | str | Unset): Optional JSON object string of metadata. Example:
            `{"category":"docs","author":"Ada"}`. `title` will be merged into this dictionary as `metadata.title` if it is
            not already present.
        title (str | Unset): Optional title for the content
    """

    file: File
    metadata: None | str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        metadata: None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.metadata, Unset):
            if isinstance(self.metadata, str):
                files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))
            else:
                files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        def _parse_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        title = d.pop("title", UNSET)

        body_upload_file_to_content_api_contents_source_connection_content_version_upload_post = cls(
            file=file,
            metadata=metadata,
            title=title,
        )

        body_upload_file_to_content_api_contents_source_connection_content_version_upload_post.additional_properties = d
        return body_upload_file_to_content_api_contents_source_connection_content_version_upload_post

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
