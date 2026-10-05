from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileUploadResponse")


@_attrs_define
class FileUploadResponse:
    """Response model for content file replacement upload.

    Attributes:
        content_version_id (None | str): ID of the newly created content version. A replacement creates a new version
            rather than overwriting the previous one.
        filename (str): Original filename
        source_connection_content_version_id (None | str): ID of the source connection content version. Unchanged by a
            replacement, so it stays a stable handle for the content.
        status (str): Always `uploaded`. Unlike the create endpoints, a replacement is never rejected as a duplicate of
            another item.
        embedder_warning (None | str | Unset): Set when the file's type is not embedded directly on this source, so
            indexing relies on extracted text. Content with none (e.g. a photograph) will be marked FAILED.
    """

    content_version_id: None | str
    filename: str
    source_connection_content_version_id: None | str
    status: str
    embedder_warning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_version_id: None | str
        content_version_id = self.content_version_id

        filename = self.filename

        source_connection_content_version_id: None | str
        source_connection_content_version_id = self.source_connection_content_version_id

        status = self.status

        embedder_warning: None | str | Unset
        if isinstance(self.embedder_warning, Unset):
            embedder_warning = UNSET
        else:
            embedder_warning = self.embedder_warning

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
        if embedder_warning is not UNSET:
            field_dict["embedder_warning"] = embedder_warning

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

        source_connection_content_version_id = (
            _parse_source_connection_content_version_id(
                d.pop("source_connection_content_version_id")
            )
        )

        status = d.pop("status")

        def _parse_embedder_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedder_warning = _parse_embedder_warning(d.pop("embedder_warning", UNSET))

        file_upload_response = cls(
            content_version_id=content_version_id,
            filename=filename,
            source_connection_content_version_id=source_connection_content_version_id,
            status=status,
            embedder_warning=embedder_warning,
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
