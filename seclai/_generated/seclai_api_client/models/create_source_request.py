from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_filter_type import ContentFilterType
from ..models.polling_action import PollingAction
from ..models.polling_type import PollingType
from ..models.seed_type import SeedType
from ..models.source_type import SourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSourceRequest")


@_attrs_define
class CreateSourceRequest:
    """Request model for creating a new source

    Attributes:
        source_type (SourceType):
        chunk_language (None | str | Unset): Language for language-specific text splitting
        chunk_overlap (int | None | Unset): Chunk overlap for text splitting
        chunk_regex_separators (bool | None | Unset): Whether to treat separators as regex patterns
        chunk_separators (None | str | Unset): Custom chunk separators as JSON array string
        chunk_size (int | None | Unset): Chunk size for text splitting
        content_filter (ContentFilterType | None | Unset): Content filtering strategy
        dimensions (int | None | Unset): Embedding dimensions
        embedding_model (None | str | Unset): Embedding model ID
        latest_n (int | None | Unset): Number of latest items for seeding
        name (None | str | Unset): Name of the source
        polling (None | PollingType | Unset): Polling frequency: once, hourly, daily, weekly
        polling_action (None | PollingAction | Unset): Polling action to take
        polling_max_items (int | None | Unset): Maximum items to fetch per poll
        retention (int | None | Unset): Retention period in days (null for infinite)
        seed (None | SeedType | Unset): Seeding type: full_history, selected_items, latest_n
        selected_items (list[str] | None | Unset): List of selected item IDs for seeding
        url (None | str | Unset): URL of the source (alternative to url_id)
        url_id (None | str | Unset): ID of the URL (alternative to url)
    """

    source_type: SourceType
    chunk_language: None | str | Unset = UNSET
    chunk_overlap: int | None | Unset = UNSET
    chunk_regex_separators: bool | None | Unset = UNSET
    chunk_separators: None | str | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    content_filter: ContentFilterType | None | Unset = UNSET
    dimensions: int | None | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    latest_n: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    polling: None | PollingType | Unset = UNSET
    polling_action: None | PollingAction | Unset = UNSET
    polling_max_items: int | None | Unset = UNSET
    retention: int | None | Unset = UNSET
    seed: None | SeedType | Unset = UNSET
    selected_items: list[str] | None | Unset = UNSET
    url: None | str | Unset = UNSET
    url_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type.value

        chunk_language: None | str | Unset
        if isinstance(self.chunk_language, Unset):
            chunk_language = UNSET
        else:
            chunk_language = self.chunk_language

        chunk_overlap: int | None | Unset
        if isinstance(self.chunk_overlap, Unset):
            chunk_overlap = UNSET
        else:
            chunk_overlap = self.chunk_overlap

        chunk_regex_separators: bool | None | Unset
        if isinstance(self.chunk_regex_separators, Unset):
            chunk_regex_separators = UNSET
        else:
            chunk_regex_separators = self.chunk_regex_separators

        chunk_separators: None | str | Unset
        if isinstance(self.chunk_separators, Unset):
            chunk_separators = UNSET
        else:
            chunk_separators = self.chunk_separators

        chunk_size: int | None | Unset
        if isinstance(self.chunk_size, Unset):
            chunk_size = UNSET
        else:
            chunk_size = self.chunk_size

        content_filter: None | str | Unset
        if isinstance(self.content_filter, Unset):
            content_filter = UNSET
        elif isinstance(self.content_filter, ContentFilterType):
            content_filter = self.content_filter.value
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

        latest_n: int | None | Unset
        if isinstance(self.latest_n, Unset):
            latest_n = UNSET
        else:
            latest_n = self.latest_n

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        polling: None | str | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        elif isinstance(self.polling, PollingType):
            polling = self.polling.value
        else:
            polling = self.polling

        polling_action: None | str | Unset
        if isinstance(self.polling_action, Unset):
            polling_action = UNSET
        elif isinstance(self.polling_action, PollingAction):
            polling_action = self.polling_action.value
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

        seed: None | str | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        elif isinstance(self.seed, SeedType):
            seed = self.seed.value
        else:
            seed = self.seed

        selected_items: list[str] | None | Unset
        if isinstance(self.selected_items, Unset):
            selected_items = UNSET
        elif isinstance(self.selected_items, list):
            selected_items = self.selected_items

        else:
            selected_items = self.selected_items

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        url_id: None | str | Unset
        if isinstance(self.url_id, Unset):
            url_id = UNSET
        else:
            url_id = self.url_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
            }
        )
        if chunk_language is not UNSET:
            field_dict["chunk_language"] = chunk_language
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap
        if chunk_regex_separators is not UNSET:
            field_dict["chunk_regex_separators"] = chunk_regex_separators
        if chunk_separators is not UNSET:
            field_dict["chunk_separators"] = chunk_separators
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if content_filter is not UNSET:
            field_dict["content_filter"] = content_filter
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if latest_n is not UNSET:
            field_dict["latest_n"] = latest_n
        if name is not UNSET:
            field_dict["name"] = name
        if polling is not UNSET:
            field_dict["polling"] = polling
        if polling_action is not UNSET:
            field_dict["polling_action"] = polling_action
        if polling_max_items is not UNSET:
            field_dict["polling_max_items"] = polling_max_items
        if retention is not UNSET:
            field_dict["retention"] = retention
        if seed is not UNSET:
            field_dict["seed"] = seed
        if selected_items is not UNSET:
            field_dict["selected_items"] = selected_items
        if url is not UNSET:
            field_dict["url"] = url
        if url_id is not UNSET:
            field_dict["url_id"] = url_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_type = SourceType(d.pop("source_type"))

        def _parse_chunk_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chunk_language = _parse_chunk_language(d.pop("chunk_language", UNSET))

        def _parse_chunk_overlap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_overlap = _parse_chunk_overlap(d.pop("chunk_overlap", UNSET))

        def _parse_chunk_regex_separators(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        chunk_regex_separators = _parse_chunk_regex_separators(
            d.pop("chunk_regex_separators", UNSET)
        )

        def _parse_chunk_separators(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chunk_separators = _parse_chunk_separators(d.pop("chunk_separators", UNSET))

        def _parse_chunk_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_size = _parse_chunk_size(d.pop("chunk_size", UNSET))

        def _parse_content_filter(data: object) -> ContentFilterType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                content_filter_type_0 = ContentFilterType(data)

                return content_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContentFilterType | None | Unset, data)

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

        def _parse_latest_n(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_n = _parse_latest_n(d.pop("latest_n", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_polling(data: object) -> None | PollingType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                polling_type_0 = PollingType(data)

                return polling_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollingType | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        def _parse_polling_action(data: object) -> None | PollingAction | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                polling_action_type_0 = PollingAction(data)

                return polling_action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollingAction | Unset, data)

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

        def _parse_seed(data: object) -> None | SeedType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seed_type_0 = SeedType(data)

                return seed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SeedType | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_selected_items(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_items_type_0 = cast(list[str], data)

                return selected_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        selected_items = _parse_selected_items(d.pop("selected_items", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_url_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_id = _parse_url_id(d.pop("url_id", UNSET))

        create_source_request = cls(
            source_type=source_type,
            chunk_language=chunk_language,
            chunk_overlap=chunk_overlap,
            chunk_regex_separators=chunk_regex_separators,
            chunk_separators=chunk_separators,
            chunk_size=chunk_size,
            content_filter=content_filter,
            dimensions=dimensions,
            embedding_model=embedding_model,
            latest_n=latest_n,
            name=name,
            polling=polling,
            polling_action=polling_action,
            polling_max_items=polling_max_items,
            retention=retention,
            seed=seed,
            selected_items=selected_items,
            url=url,
            url_id=url_id,
        )

        create_source_request.additional_properties = d
        return create_source_request

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
