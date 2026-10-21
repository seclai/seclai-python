from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_index_mode import SourceIndexMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSourceBody")


@_attrs_define
class CreateSourceBody:
    """Request body for creating a content source.

    Attributes:
        name (str): Source name.
        source_type (str): Source type: rss_feed, website, custom_index, cloud_drive or email. The legacy value
            'file_uploads' is accepted as an alias for custom_index.
        chunk_overlap (int | None | Unset): Chunk overlap for content processing.
        chunk_size (int | None | Unset): Chunk size for content processing.
        cloud_drive_connection_id (None | str | Unset): Required for a cloud_drive source, and ignored on any other: the
            id of a connected drive, from GET /cloud-drives.
        cloud_drive_content_types (None | str | Unset): For a cloud_drive source: comma-separated MIME types a file must
            have to be indexed. Omit for no filter.
        cloud_drive_folder_path (None | str | Unset): For a cloud_drive source: the folder to index, as a path inside
            the drive. Omit to index the connected drive's own folder.
        cloud_drive_max_file_mb (int | None | Unset): For a cloud_drive source: files larger than this many megabytes
            are skipped. Omit for no limit of the source's own.
        cloud_drive_path_pattern (None | str | Unset): For a cloud_drive source: a glob a file's path must match to be
            indexed, such as `**/*.pdf` or `/reports/*`. Omit for no filter.
        content_filter (None | str | Unset): Content filter type.
        dimensions (int | None | Unset): Embedding dimensions override.
        document_images (bool | None | Unset): Whether the images inside PDF, DOCX, PPTX and XLSX files are attached to
            the item and indexed; on a text-only embedder, by the text in each image. Applies to documents added after it
            changes. Defaults to true; below Seclai-Version 2026-10-18 it defaults to false on a text-only embedder. On a
            website or RSS source it is ignored: `media_types` decides.
        email_allowed_senders (list[str] | None | Unset): Required for an email source, and only valid there: the
            senders whose mail is stored. Each entry is a full address (news@example.com) or a bare domain (example.com),
            which also matches its sub-domains. Matched against the message's From address, which must pass DMARC.
        embedding_model (None | str | Unset): Embedding model override — a `model_type` from `GET /models/embedders`,
            which also reports each embedder's `supported_input_media`. Defaults to the platform embedder
            (`default_model_type` on that endpoint) when omitted. Indexing images or video requires an embedder that lists
            that modality.
        feed_attachments (list[str] | None | Unset): Kinds of file listed beside a feed item's content to attach to the
            item and index, on an RSS source. Subset of ['enclosures', 'item_image', 'media_rss']; any other value is
            refused. None are attached unless chosen.
        index_mode (None | SourceIndexMode | Unset): Index mode for custom_index sources: fast_and_cheap (default),
            balanced, slow_and_thorough, or custom.
        media_types (list[str] | None | Unset): Media kinds in a web page's main content to attach to the page's item
            and index, on a website or RSS source. Subset of ['images', 'video']. From `Seclai-Version: 2026-10-13` any
            other value, and any kind on another source type, is refused with a 400; older versions drop an unknown value
            and store the rest. A kind the source's embedder cannot index is stored and not indexed (see
            `supported_input_media` on GET /models/embedders). 'images' also covers the images inside PDF, DOCX, PPTX and
            XLSX files. Applies to pages and documents added after it is set.
        polling (None | str | Unset): Polling interval (e.g. hourly, daily).
        polling_action (None | str | Unset): Polling action.
        polling_max_items (int | None | Unset): The most new feed items a scheduled poll takes. Read for RSS feeds only:
            from Seclai-Version 2026-10-19 any other source type rejects it with 400. Earlier versions store it there. An
            email source rejects it at every version.
        retention (int | None | Unset): Retention period in days.
        url_id (None | str | Unset): URL record ID (required for rss/website sources).
    """

    name: str
    source_type: str
    chunk_overlap: int | None | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    cloud_drive_connection_id: None | str | Unset = UNSET
    cloud_drive_content_types: None | str | Unset = UNSET
    cloud_drive_folder_path: None | str | Unset = UNSET
    cloud_drive_max_file_mb: int | None | Unset = UNSET
    cloud_drive_path_pattern: None | str | Unset = UNSET
    content_filter: None | str | Unset = UNSET
    dimensions: int | None | Unset = UNSET
    document_images: bool | None | Unset = UNSET
    email_allowed_senders: list[str] | None | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    feed_attachments: list[str] | None | Unset = UNSET
    index_mode: None | SourceIndexMode | Unset = UNSET
    media_types: list[str] | None | Unset = UNSET
    polling: None | str | Unset = UNSET
    polling_action: None | str | Unset = UNSET
    polling_max_items: int | None | Unset = UNSET
    retention: int | None | Unset = UNSET
    url_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source_type = self.source_type

        chunk_overlap: int | None | Unset
        if isinstance(self.chunk_overlap, Unset):
            chunk_overlap = UNSET
        else:
            chunk_overlap = self.chunk_overlap

        chunk_size: int | None | Unset
        if isinstance(self.chunk_size, Unset):
            chunk_size = UNSET
        else:
            chunk_size = self.chunk_size

        cloud_drive_connection_id: None | str | Unset
        if isinstance(self.cloud_drive_connection_id, Unset):
            cloud_drive_connection_id = UNSET
        else:
            cloud_drive_connection_id = self.cloud_drive_connection_id

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

        content_filter: None | str | Unset
        if isinstance(self.content_filter, Unset):
            content_filter = UNSET
        else:
            content_filter = self.content_filter

        dimensions: int | None | Unset
        if isinstance(self.dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = self.dimensions

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

        embedding_model: None | str | Unset
        if isinstance(self.embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = self.embedding_model

        feed_attachments: list[str] | None | Unset
        if isinstance(self.feed_attachments, Unset):
            feed_attachments = UNSET
        elif isinstance(self.feed_attachments, list):
            feed_attachments = self.feed_attachments

        else:
            feed_attachments = self.feed_attachments

        index_mode: None | str | Unset
        if isinstance(self.index_mode, Unset):
            index_mode = UNSET
        elif isinstance(self.index_mode, SourceIndexMode):
            index_mode = self.index_mode.value
        else:
            index_mode = self.index_mode

        media_types: list[str] | None | Unset
        if isinstance(self.media_types, Unset):
            media_types = UNSET
        elif isinstance(self.media_types, list):
            media_types = self.media_types

        else:
            media_types = self.media_types

        polling: None | str | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        else:
            polling = self.polling

        polling_action: None | str | Unset
        if isinstance(self.polling_action, Unset):
            polling_action = UNSET
        else:
            polling_action = self.polling_action

        polling_max_items: int | None | Unset
        if isinstance(self.polling_max_items, Unset):
            polling_max_items = UNSET
        else:
            polling_max_items = self.polling_max_items

        retention: int | None | Unset
        if isinstance(self.retention, Unset):
            retention = UNSET
        else:
            retention = self.retention

        url_id: None | str | Unset
        if isinstance(self.url_id, Unset):
            url_id = UNSET
        else:
            url_id = self.url_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source_type": source_type,
            }
        )
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if cloud_drive_connection_id is not UNSET:
            field_dict["cloud_drive_connection_id"] = cloud_drive_connection_id
        if cloud_drive_content_types is not UNSET:
            field_dict["cloud_drive_content_types"] = cloud_drive_content_types
        if cloud_drive_folder_path is not UNSET:
            field_dict["cloud_drive_folder_path"] = cloud_drive_folder_path
        if cloud_drive_max_file_mb is not UNSET:
            field_dict["cloud_drive_max_file_mb"] = cloud_drive_max_file_mb
        if cloud_drive_path_pattern is not UNSET:
            field_dict["cloud_drive_path_pattern"] = cloud_drive_path_pattern
        if content_filter is not UNSET:
            field_dict["content_filter"] = content_filter
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if document_images is not UNSET:
            field_dict["document_images"] = document_images
        if email_allowed_senders is not UNSET:
            field_dict["email_allowed_senders"] = email_allowed_senders
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if feed_attachments is not UNSET:
            field_dict["feed_attachments"] = feed_attachments
        if index_mode is not UNSET:
            field_dict["index_mode"] = index_mode
        if media_types is not UNSET:
            field_dict["media_types"] = media_types
        if polling is not UNSET:
            field_dict["polling"] = polling
        if polling_action is not UNSET:
            field_dict["polling_action"] = polling_action
        if polling_max_items is not UNSET:
            field_dict["polling_max_items"] = polling_max_items
        if retention is not UNSET:
            field_dict["retention"] = retention
        if url_id is not UNSET:
            field_dict["url_id"] = url_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        source_type = d.pop("source_type")

        def _parse_chunk_overlap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_overlap = _parse_chunk_overlap(d.pop("chunk_overlap", UNSET))

        def _parse_chunk_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_size = _parse_chunk_size(d.pop("chunk_size", UNSET))

        def _parse_cloud_drive_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cloud_drive_connection_id = _parse_cloud_drive_connection_id(
            d.pop("cloud_drive_connection_id", UNSET)
        )

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

        def _parse_content_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_filter = _parse_content_filter(d.pop("content_filter", UNSET))

        def _parse_dimensions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

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

        def _parse_embedding_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model = _parse_embedding_model(d.pop("embedding_model", UNSET))

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

        def _parse_index_mode(data: object) -> None | SourceIndexMode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                index_mode_type_0 = SourceIndexMode(data)

                return index_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceIndexMode | Unset, data)

        index_mode = _parse_index_mode(d.pop("index_mode", UNSET))

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

        def _parse_polling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        def _parse_polling_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polling_action = _parse_polling_action(d.pop("polling_action", UNSET))

        def _parse_polling_max_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        polling_max_items = _parse_polling_max_items(d.pop("polling_max_items", UNSET))

        def _parse_retention(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention = _parse_retention(d.pop("retention", UNSET))

        def _parse_url_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_id = _parse_url_id(d.pop("url_id", UNSET))

        create_source_body = cls(
            name=name,
            source_type=source_type,
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
            cloud_drive_connection_id=cloud_drive_connection_id,
            cloud_drive_content_types=cloud_drive_content_types,
            cloud_drive_folder_path=cloud_drive_folder_path,
            cloud_drive_max_file_mb=cloud_drive_max_file_mb,
            cloud_drive_path_pattern=cloud_drive_path_pattern,
            content_filter=content_filter,
            dimensions=dimensions,
            document_images=document_images,
            email_allowed_senders=email_allowed_senders,
            embedding_model=embedding_model,
            feed_attachments=feed_attachments,
            index_mode=index_mode,
            media_types=media_types,
            polling=polling,
            polling_action=polling_action,
            polling_max_items=polling_max_items,
            retention=retention,
            url_id=url_id,
        )

        create_source_body.additional_properties = d
        return create_source_body

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
