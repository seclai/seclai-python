from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_attachment_response_metadata import (
        ContentAttachmentResponseMetadata,
    )


T = TypeVar("T", bound="ContentAttachmentResponse")


@_attrs_define
class ContentAttachmentResponse:
    """A file attached to a content item.

    Attributes:
        content_type (str): MIME type of the attached file.
        created_at (str): When the file was first attached.
        id (str): The attachment's id, which the single-attachment endpoints take.
        indexed (bool): Whether indexing the file for search was asked for.
        indexing_error (None | str): Why the file was not indexed, when `indexing_status` is `failed`.
        indexing_status (None | str): `pending`, `completed` or `failed`; null when indexing was not asked for. Search
            finds the file only when `completed`.
        key (str): The attachment's key, unique within the item.
        metadata (ContentAttachmentResponseMetadata): What is known about the file beyond its bytes. An image extracted
            from a PDF carries its `page_number`, and `page_render: true` when it is a render of the whole page. An image or
            video from a web page carries `source_url` (the address it was fetched from), `position` (its place among the
            media the page listed, from 0) and, when the page gave one, `alt_text`. Empty for most files. A retrieval
            metadata filter matches these keys, except `alt_text`, which is indexed as the attachment's text.
        size_bytes (int): Size of the attached file in bytes.
        updated_at (str): When the attachment last changed.
    """

    content_type: str
    created_at: str
    id: str
    indexed: bool
    indexing_error: None | str
    indexing_status: None | str
    key: str
    metadata: ContentAttachmentResponseMetadata
    size_bytes: int
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        id = self.id

        indexed = self.indexed

        indexing_error: None | str
        indexing_error = self.indexing_error

        indexing_status: None | str
        indexing_status = self.indexing_status

        key = self.key

        metadata = self.metadata.to_dict()

        size_bytes = self.size_bytes

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "created_at": created_at,
                "id": id,
                "indexed": indexed,
                "indexing_error": indexing_error,
                "indexing_status": indexing_status,
                "key": key,
                "metadata": metadata,
                "size_bytes": size_bytes,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_attachment_response_metadata import (
            ContentAttachmentResponseMetadata,
        )

        d = dict(src_dict)
        content_type = d.pop("content_type")

        created_at = d.pop("created_at")

        id = d.pop("id")

        indexed = d.pop("indexed")

        def _parse_indexing_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        indexing_error = _parse_indexing_error(d.pop("indexing_error"))

        def _parse_indexing_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        indexing_status = _parse_indexing_status(d.pop("indexing_status"))

        key = d.pop("key")

        metadata = ContentAttachmentResponseMetadata.from_dict(d.pop("metadata"))

        size_bytes = d.pop("size_bytes")

        updated_at = d.pop("updated_at")

        content_attachment_response = cls(
            content_type=content_type,
            created_at=created_at,
            id=id,
            indexed=indexed,
            indexing_error=indexing_error,
            indexing_status=indexing_status,
            key=key,
            metadata=metadata,
            size_bytes=size_bytes,
            updated_at=updated_at,
        )

        content_attachment_response.additional_properties = d
        return content_attachment_response

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
