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
        source_type (str): Source type: rss, website, or custom_index. The legacy value 'file_uploads' is accepted as an
            alias for custom_index.
        chunk_overlap (int | None | Unset): Chunk overlap for content processing.
        chunk_size (int | None | Unset): Chunk size for content processing.
        content_filter (None | str | Unset): Content filter type.
        dimensions (int | None | Unset): Embedding dimensions override.
        embedding_model (None | str | Unset): Embedding model override.
        index_mode (None | SourceIndexMode | Unset): Index mode for custom_index sources: fast_and_cheap (default),
            balanced, slow_and_thorough, or custom.
        polling (None | str | Unset): Polling interval (e.g. hourly, daily).
        polling_action (None | str | Unset): Polling action.
        polling_max_items (int | None | Unset): Max items per poll.
        retention (int | None | Unset): Retention period in days.
        url_id (None | str | Unset): URL record ID (required for rss/website sources).
    """

    name: str
    source_type: str
    chunk_overlap: int | None | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    content_filter: None | str | Unset = UNSET
    dimensions: int | None | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    index_mode: None | SourceIndexMode | Unset = UNSET
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

        embedding_model: None | str | Unset
        if isinstance(self.embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = self.embedding_model

        index_mode: None | str | Unset
        if isinstance(self.index_mode, Unset):
            index_mode = UNSET
        elif isinstance(self.index_mode, SourceIndexMode):
            index_mode = self.index_mode.value
        else:
            index_mode = self.index_mode

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
        if content_filter is not UNSET:
            field_dict["content_filter"] = content_filter
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if index_mode is not UNSET:
            field_dict["index_mode"] = index_mode
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

        def _parse_embedding_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model = _parse_embedding_model(d.pop("embedding_model", UNSET))

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
            content_filter=content_filter,
            dimensions=dimensions,
            embedding_model=embedding_model,
            index_mode=index_mode,
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
