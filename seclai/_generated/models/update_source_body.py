from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSourceBody")


@_attrs_define
class UpdateSourceBody:
    """Request body for updating a content source.

    Attributes:
        cloud_drive_content_types (None | str | Unset): For a cloud_drive source: comma-separated MIME types a file must
            have to be indexed. Send an empty string to clear it; omit to leave it unchanged.
        cloud_drive_folder_path (None | str | Unset): For a cloud_drive source: the folder to index, as a path inside
            the drive. Send an empty string to index the connected drive's own folder; omit to leave it unchanged.
        cloud_drive_max_file_mb (int | None | Unset): For a cloud_drive source: files larger than this many megabytes
            are skipped. Send 0 to clear the source's own limit; omit to leave it unchanged.
        cloud_drive_path_pattern (None | str | Unset): For a cloud_drive source: a glob a file's path must match to be
            indexed, such as `**/*.pdf` or `/reports/*`. Send an empty string to clear it; omit to leave it unchanged.
        document_images (bool | None | Unset): Whether the images inside PDF, DOCX, PPTX and XLSX files are attached to
            the item and indexed; on a text-only embedder, by the text in each image. Applies to documents added after it
            changes. Omit the field to leave it unchanged. On a website or RSS source it is ignored: `media_types` decides.
        email_allowed_senders (list[str] | None | Unset): For an email source: replaces the allowed senders. Each entry
            is a full address or a bare domain. The list cannot be emptied. Omit to leave it unchanged.
        feed_attachments (list[str] | None | Unset): Kinds of file listed beside a feed item's content to attach to the
            item and index, on an RSS source. Subset of ['enclosures', 'item_image', 'media_rss']; any other value is
            refused. [] attaches none. Applies to items added after it changes. Omit the field to leave it unchanged.
        media_types (list[str] | None | Unset): Media kinds in a web page's main content to attach to the page's item
            and index, on a website or RSS source. Subset of ['images', 'video']. From `Seclai-Version: 2026-10-13` any
            other value, and any kind on another source type, is refused with a 400; older versions drop an unknown value
            and store the rest. A kind the source's embedder cannot index is stored and not indexed (see
            `supported_input_media` on GET /models/embedders). [] attaches no media from web pages. 'images' also covers the
            images inside PDF, DOCX, PPTX and XLSX files. Applies to pages and documents added after it changes.
        name (None | str | Unset): New name.
        polling (None | str | Unset): New polling interval.
        retention_days (int | None | Unset): New retention period in days — content older than this is deleted
            permanently. Send null to clear the window: content is then kept indefinitely. Omit the field to leave it
            unchanged.
    """

    cloud_drive_content_types: None | str | Unset = UNSET
    cloud_drive_folder_path: None | str | Unset = UNSET
    cloud_drive_max_file_mb: int | None | Unset = UNSET
    cloud_drive_path_pattern: None | str | Unset = UNSET
    document_images: bool | None | Unset = UNSET
    email_allowed_senders: list[str] | None | Unset = UNSET
    feed_attachments: list[str] | None | Unset = UNSET
    media_types: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    polling: None | str | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_drive_content_types: None | str | Unset
        if isinstance(self.cloud_drive_content_types, Unset):
            cloud_drive_content_types = UNSET
        else:
            cloud_drive_content_types = self.cloud_drive_content_types

        cloud_drive_folder_path: None | str | Unset
        if isinstance(self.cloud_drive_folder_path, Unset):
            cloud_drive_folder_path = UNSET
        else:
            cloud_drive_folder_path = self.cloud_drive_folder_path

        cloud_drive_max_file_mb: int | None | Unset
        if isinstance(self.cloud_drive_max_file_mb, Unset):
            cloud_drive_max_file_mb = UNSET
        else:
            cloud_drive_max_file_mb = self.cloud_drive_max_file_mb

        cloud_drive_path_pattern: None | str | Unset
        if isinstance(self.cloud_drive_path_pattern, Unset):
            cloud_drive_path_pattern = UNSET
        else:
            cloud_drive_path_pattern = self.cloud_drive_path_pattern

        document_images: bool | None | Unset
        if isinstance(self.document_images, Unset):
            document_images = UNSET
        else:
            document_images = self.document_images

        email_allowed_senders: list[str] | None | Unset
        if isinstance(self.email_allowed_senders, Unset):
            email_allowed_senders = UNSET
        elif isinstance(self.email_allowed_senders, list):
            email_allowed_senders = self.email_allowed_senders

        else:
            email_allowed_senders = self.email_allowed_senders

        feed_attachments: list[str] | None | Unset
        if isinstance(self.feed_attachments, Unset):
            feed_attachments = UNSET
        elif isinstance(self.feed_attachments, list):
            feed_attachments = self.feed_attachments

        else:
            feed_attachments = self.feed_attachments

        media_types: list[str] | None | Unset
        if isinstance(self.media_types, Unset):
            media_types = UNSET
        elif isinstance(self.media_types, list):
            media_types = self.media_types

        else:
            media_types = self.media_types

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        polling: None | str | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        else:
            polling = self.polling

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_drive_content_types is not UNSET:
            field_dict["cloud_drive_content_types"] = cloud_drive_content_types
        if cloud_drive_folder_path is not UNSET:
            field_dict["cloud_drive_folder_path"] = cloud_drive_folder_path
        if cloud_drive_max_file_mb is not UNSET:
            field_dict["cloud_drive_max_file_mb"] = cloud_drive_max_file_mb
        if cloud_drive_path_pattern is not UNSET:
            field_dict["cloud_drive_path_pattern"] = cloud_drive_path_pattern
        if document_images is not UNSET:
            field_dict["document_images"] = document_images
        if email_allowed_senders is not UNSET:
            field_dict["email_allowed_senders"] = email_allowed_senders
        if feed_attachments is not UNSET:
            field_dict["feed_attachments"] = feed_attachments
        if media_types is not UNSET:
            field_dict["media_types"] = media_types
        if name is not UNSET:
            field_dict["name"] = name
        if polling is not UNSET:
            field_dict["polling"] = polling
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cloud_drive_content_types(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cloud_drive_content_types = _parse_cloud_drive_content_types(
            d.pop("cloud_drive_content_types", UNSET)
        )

        def _parse_cloud_drive_folder_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cloud_drive_folder_path = _parse_cloud_drive_folder_path(
            d.pop("cloud_drive_folder_path", UNSET)
        )

        def _parse_cloud_drive_max_file_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_drive_max_file_mb = _parse_cloud_drive_max_file_mb(
            d.pop("cloud_drive_max_file_mb", UNSET)
        )

        def _parse_cloud_drive_path_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cloud_drive_path_pattern = _parse_cloud_drive_path_pattern(
            d.pop("cloud_drive_path_pattern", UNSET)
        )

        def _parse_document_images(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        document_images = _parse_document_images(d.pop("document_images", UNSET))

        def _parse_email_allowed_senders(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                email_allowed_senders_type_0 = cast(list[str], data)

                return email_allowed_senders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        email_allowed_senders = _parse_email_allowed_senders(
            d.pop("email_allowed_senders", UNSET)
        )

        def _parse_feed_attachments(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                feed_attachments_type_0 = cast(list[str], data)

                return feed_attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        feed_attachments = _parse_feed_attachments(d.pop("feed_attachments", UNSET))

        def _parse_media_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_types_type_0 = cast(list[str], data)

                return media_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        media_types = _parse_media_types(d.pop("media_types", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_polling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        update_source_body = cls(
            cloud_drive_content_types=cloud_drive_content_types,
            cloud_drive_folder_path=cloud_drive_folder_path,
            cloud_drive_max_file_mb=cloud_drive_max_file_mb,
            cloud_drive_path_pattern=cloud_drive_path_pattern,
            document_images=document_images,
            email_allowed_senders=email_allowed_senders,
            feed_attachments=feed_attachments,
            media_types=media_types,
            name=name,
            polling=polling,
            retention_days=retention_days,
        )

        update_source_body.additional_properties = d
        return update_source_body

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
