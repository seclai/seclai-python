from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_detail_response_metadata_type_0_item import (
        ContentDetailResponseMetadataType0Item,
    )
    from ..models.skipped_attachment_response import SkippedAttachmentResponse


T = TypeVar("T", bound="ContentDetailResponse")


@_attrs_define
class ContentDetailResponse:
    """Response model for content detail.

    Attributes:
        content_duration (int | None): Duration of the content in seconds.
        content_duration_display (None | str): Display string for content duration.
        content_status (str): Status of the content.
        content_type (str): Type of the content.
        content_type_display (str): Display name of the content type.
        content_url (str): URL of the content.
        content_word_count (int | None): Word count of the content.
        description (None | str): Description of the content.
        error (None | str): Error message, if any.
        id (str): Unique identifier for the content version.
        metadata (list[ContentDetailResponseMetadataType0Item] | None): Metadata associated with the content.
        published_at (None | str): Timestamp when the content was published.
        pulled_at (str): Timestamp when the content was pulled.
        source_connection_content_version_id (str): ID of the source connection content version.
        source_connection_id (str): ID of the source connection.
        source_name (str): Name of the source.
        source_type (str): Type of the source.
        text_content (None | str): Text content.
        text_content_end (int): End position of the text content.
        text_content_start (int): Start position of the text content.
        text_content_total_length (int): Total length of the text content.
        title (None | str): Title of the content.
        extracted_media_capped (bool | Unset): True when extraction stopped with media still unread, so the item
            references more media than was attached and media search will not match anything past the cut. The cause is a
            web page that ran out of the budget for fetching remote assets or listed more media than is recorded, or a web
            page or document that could not be read to the end. Default: False.
        extracted_media_count (int | None | Unset): Number of images / videos in this web page's main content, or of
            images inside this PDF or Office document, that were attached to the item on this source; a file over the per-
            file size limit, listed as a failed attachment, is not counted. Null when there is no media record for the item:
            the extraction pass has not run, does not apply to this container or this source's settings, or found nothing.
            Treat null as 'unknown', never as zero.
        extracted_media_limit (int | None | Unset): The bound that was reached, when extracted_media_capped is true and
            the stop was a bound — a number of fetch attempts, of seconds, of bytes, or of media listed. Null when
            extraction was not capped, or when it stopped because the container could not be read rather than because a
            bound fired.
        skipped_attachments (list[SkippedAttachmentResponse] | Unset): Parts of an email delivered to an email content
            source that were not stored as attachments of this item, each with the reason: displayed_in_body (an image the
            message body shows, such as a signature logo), over_cap (beyond the per-message attachment limit), no_filename,
            or undecodable. size_bytes is null for a part that was never decoded. Empty for every other item.
    """

    content_duration: int | None
    content_duration_display: None | str
    content_status: str
    content_type: str
    content_type_display: str
    content_url: str
    content_word_count: int | None
    description: None | str
    error: None | str
    id: str
    metadata: list[ContentDetailResponseMetadataType0Item] | None
    published_at: None | str
    pulled_at: str
    source_connection_content_version_id: str
    source_connection_id: str
    source_name: str
    source_type: str
    text_content: None | str
    text_content_end: int
    text_content_start: int
    text_content_total_length: int
    title: None | str
    extracted_media_capped: bool | Unset = False
    extracted_media_count: int | None | Unset = UNSET
    extracted_media_limit: int | None | Unset = UNSET
    skipped_attachments: list[SkippedAttachmentResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_duration: int | None
        content_duration = self.content_duration

        content_duration_display: None | str
        content_duration_display = self.content_duration_display

        content_status = self.content_status

        content_type = self.content_type

        content_type_display = self.content_type_display

        content_url = self.content_url

        content_word_count: int | None
        content_word_count = self.content_word_count

        description: None | str
        description = self.description

        error: None | str
        error = self.error

        id = self.id

        metadata: list[dict[str, Any]] | None
        if isinstance(self.metadata, list):
            metadata = []
            for metadata_type_0_item_data in self.metadata:
                metadata_type_0_item = metadata_type_0_item_data.to_dict()
                metadata.append(metadata_type_0_item)

        else:
            metadata = self.metadata

        published_at: None | str
        published_at = self.published_at

        pulled_at = self.pulled_at

        source_connection_content_version_id = self.source_connection_content_version_id

        source_connection_id = self.source_connection_id

        source_name = self.source_name

        source_type = self.source_type

        text_content: None | str
        text_content = self.text_content

        text_content_end = self.text_content_end

        text_content_start = self.text_content_start

        text_content_total_length = self.text_content_total_length

        title: None | str
        title = self.title

        extracted_media_capped = self.extracted_media_capped

        extracted_media_count: int | None | Unset
        if isinstance(self.extracted_media_count, Unset):
            extracted_media_count = UNSET
        else:
            extracted_media_count = self.extracted_media_count

        extracted_media_limit: int | None | Unset
        if isinstance(self.extracted_media_limit, Unset):
            extracted_media_limit = UNSET
        else:
            extracted_media_limit = self.extracted_media_limit

        skipped_attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped_attachments, Unset):
            skipped_attachments = []
            for skipped_attachments_item_data in self.skipped_attachments:
                skipped_attachments_item = skipped_attachments_item_data.to_dict()
                skipped_attachments.append(skipped_attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_duration": content_duration,
                "content_duration_display": content_duration_display,
                "content_status": content_status,
                "content_type": content_type,
                "content_type_display": content_type_display,
                "content_url": content_url,
                "content_word_count": content_word_count,
                "description": description,
                "error": error,
                "id": id,
                "metadata": metadata,
                "published_at": published_at,
                "pulled_at": pulled_at,
                "source_connection_content_version_id": source_connection_content_version_id,
                "source_connection_id": source_connection_id,
                "source_name": source_name,
                "source_type": source_type,
                "text_content": text_content,
                "text_content_end": text_content_end,
                "text_content_start": text_content_start,
                "text_content_total_length": text_content_total_length,
                "title": title,
            }
        )
        if extracted_media_capped is not UNSET:
            field_dict["extracted_media_capped"] = extracted_media_capped
        if extracted_media_count is not UNSET:
            field_dict["extracted_media_count"] = extracted_media_count
        if extracted_media_limit is not UNSET:
            field_dict["extracted_media_limit"] = extracted_media_limit
        if skipped_attachments is not UNSET:
            field_dict["skipped_attachments"] = skipped_attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_detail_response_metadata_type_0_item import (
            ContentDetailResponseMetadataType0Item,
        )
        from ..models.skipped_attachment_response import SkippedAttachmentResponse

        d = dict(src_dict)

        def _parse_content_duration(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        content_duration = _parse_content_duration(d.pop("content_duration"))

        def _parse_content_duration_display(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_duration_display = _parse_content_duration_display(
            d.pop("content_duration_display")
        )

        content_status = d.pop("content_status")

        content_type = d.pop("content_type")

        content_type_display = d.pop("content_type_display")

        content_url = d.pop("content_url")

        def _parse_content_word_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        content_word_count = _parse_content_word_count(d.pop("content_word_count"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        id = d.pop("id")

        def _parse_metadata(
            data: object,
        ) -> list[ContentDetailResponseMetadataType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_type_0 = []
                _metadata_type_0 = data
                for metadata_type_0_item_data in _metadata_type_0:
                    metadata_type_0_item = (
                        ContentDetailResponseMetadataType0Item.from_dict(
                            metadata_type_0_item_data
                        )
                    )

                    metadata_type_0.append(metadata_type_0_item)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContentDetailResponseMetadataType0Item] | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        pulled_at = d.pop("pulled_at")

        source_connection_content_version_id = d.pop(
            "source_connection_content_version_id"
        )

        source_connection_id = d.pop("source_connection_id")

        source_name = d.pop("source_name")

        source_type = d.pop("source_type")

        def _parse_text_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text_content = _parse_text_content(d.pop("text_content"))

        text_content_end = d.pop("text_content_end")

        text_content_start = d.pop("text_content_start")

        text_content_total_length = d.pop("text_content_total_length")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        extracted_media_capped = d.pop("extracted_media_capped", UNSET)

        def _parse_extracted_media_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        extracted_media_count = _parse_extracted_media_count(
            d.pop("extracted_media_count", UNSET)
        )

        def _parse_extracted_media_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        extracted_media_limit = _parse_extracted_media_limit(
            d.pop("extracted_media_limit", UNSET)
        )

        _skipped_attachments = d.pop("skipped_attachments", UNSET)
        skipped_attachments: list[SkippedAttachmentResponse] | Unset = UNSET
        if _skipped_attachments is not UNSET:
            skipped_attachments = []
            for skipped_attachments_item_data in _skipped_attachments:
                skipped_attachments_item = SkippedAttachmentResponse.from_dict(
                    skipped_attachments_item_data
                )

                skipped_attachments.append(skipped_attachments_item)

        content_detail_response = cls(
            content_duration=content_duration,
            content_duration_display=content_duration_display,
            content_status=content_status,
            content_type=content_type,
            content_type_display=content_type_display,
            content_url=content_url,
            content_word_count=content_word_count,
            description=description,
            error=error,
            id=id,
            metadata=metadata,
            published_at=published_at,
            pulled_at=pulled_at,
            source_connection_content_version_id=source_connection_content_version_id,
            source_connection_id=source_connection_id,
            source_name=source_name,
            source_type=source_type,
            text_content=text_content,
            text_content_end=text_content_end,
            text_content_start=text_content_start,
            text_content_total_length=text_content_total_length,
            title=title,
            extracted_media_capped=extracted_media_capped,
            extracted_media_count=extracted_media_count,
            extracted_media_limit=extracted_media_limit,
            skipped_attachments=skipped_attachments,
        )

        content_detail_response.additional_properties = d
        return content_detail_response

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
