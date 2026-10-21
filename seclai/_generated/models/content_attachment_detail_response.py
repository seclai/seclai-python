from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_attachment_detail_response_metadata import (
        ContentAttachmentDetailResponseMetadata,
    )


T = TypeVar("T", bound="ContentAttachmentDetailResponse")


@_attrs_define
class ContentAttachmentDetailResponse:
    """One attached file, with the text indexed from it.

    Attributes:
        content_type (str): MIME type of the attached file.
        created_at (str): When the file was first attached.
        file_withheld (None | str): Why the file's bytes are not served, or null when they are:
            `blocked_by_governance_policy`, `redacted_by_governance_policy` (any text below is the redacted text), or
            `pending_screening`.
        id (str): The attachment's id, which the single-attachment endpoints take.
        indexed (bool): Whether indexing the file for search was asked for.
        indexing_error (None | str): Why the file was not indexed, when `indexing_status` is `failed`.
        indexing_status (None | str): `pending`, `completed` or `failed`; null when indexing was not asked for. Search
            finds the file only when `completed`.
        key (str): The attachment's key, unique within the item.
        metadata (ContentAttachmentDetailResponseMetadata): What is known about the file beyond its bytes. An image
            extracted from a PDF carries its `page_number`, and `page_render: true` when it is a render of the whole page.
            An image or video from a web page carries `source_url` (the address it was fetched from), `position` (its place
            among the media the page listed, from 0) and, when the page gave one, `alt_text`. Empty for most files. A
            retrieval metadata filter matches these keys, except `alt_text`, which is indexed as the attachment's text.
        size_bytes (int): Size of the attached file in bytes.
        text_content (None | str): The requested range of the text the file is indexed by; null when the file has no
            completed index or was indexed without text.
        text_content_end (int):
        text_content_start (int):
        text_content_total_length (int):
        updated_at (str): When the attachment last changed.
    """

    content_type: str
    created_at: str
    file_withheld: None | str
    id: str
    indexed: bool
    indexing_error: None | str
    indexing_status: None | str
    key: str
    metadata: ContentAttachmentDetailResponseMetadata
    size_bytes: int
    text_content: None | str
    text_content_end: int
    text_content_start: int
    text_content_total_length: int
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        file_withheld: None | str
        file_withheld = self.file_withheld

        id = self.id

        indexed = self.indexed

        indexing_error: None | str
        indexing_error = self.indexing_error

        indexing_status: None | str
        indexing_status = self.indexing_status

        key = self.key

        metadata = self.metadata.to_dict()

        size_bytes = self.size_bytes

        text_content: None | str
        text_content = self.text_content

        text_content_end = self.text_content_end

        text_content_start = self.text_content_start

        text_content_total_length = self.text_content_total_length

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "created_at": created_at,
                "file_withheld": file_withheld,
                "id": id,
                "indexed": indexed,
                "indexing_error": indexing_error,
                "indexing_status": indexing_status,
                "key": key,
                "metadata": metadata,
                "size_bytes": size_bytes,
                "text_content": text_content,
                "text_content_end": text_content_end,
                "text_content_start": text_content_start,
                "text_content_total_length": text_content_total_length,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_attachment_detail_response_metadata import (
            ContentAttachmentDetailResponseMetadata,
        )

        d = dict(src_dict)
        content_type = d.pop("content_type")

        created_at = d.pop("created_at")

        def _parse_file_withheld(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_withheld = _parse_file_withheld(d.pop("file_withheld"))

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

        metadata = ContentAttachmentDetailResponseMetadata.from_dict(d.pop("metadata"))

        size_bytes = d.pop("size_bytes")

        def _parse_text_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text_content = _parse_text_content(d.pop("text_content"))

        text_content_end = d.pop("text_content_end")

        text_content_start = d.pop("text_content_start")

        text_content_total_length = d.pop("text_content_total_length")

        updated_at = d.pop("updated_at")

        content_attachment_detail_response = cls(
            content_type=content_type,
            created_at=created_at,
            file_withheld=file_withheld,
            id=id,
            indexed=indexed,
            indexing_error=indexing_error,
            indexing_status=indexing_status,
            key=key,
            metadata=metadata,
            size_bytes=size_bytes,
            text_content=text_content,
            text_content_end=text_content_end,
            text_content_start=text_content_start,
            text_content_total_length=text_content_total_length,
            updated_at=updated_at,
        )

        content_attachment_detail_response.additional_properties = d
        return content_attachment_detail_response

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
