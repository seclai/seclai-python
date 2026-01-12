from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceResponse")


@_attrs_define
class SourceResponse:
    """Response model for source data.

    Attributes:
        account_id (UUID): Account ID associated with the source.
        content_filter (str): Content filter for the source connection.
        created_at (str): Timestamp when the source connection was created.
        id (str): Unique identifier for the source connection.
        name (str): Name of the source connection.
        next_poll_at (None | str): Timestamp for the next scheduled poll.
        polling (None | str): Polling configuration for the source connection.
        polling_action (None | str): Polling action for the source connection.
        polling_max_items (int | None): Maximum items to poll for the source connection.
        pulled_at (None | str): Timestamp when content was last pulled.
        retention (int | None): Retention period for the source connection.
        source_type (str): Type of the source connection.
        updated_at (str): Timestamp when the source connection was last updated.
        url (None | str): URL of the source connection.
        avg_episodes_per_month (float | None | Unset): Average number of episodes per month.
        avg_words_per_episode (int | None | Unset): Average number of words per episode.
        chunk_language (None | str | Unset): Language used for chunking content.
        chunk_overlap (int | None | Unset): Chunk overlap for content processing.
        chunk_regex_separators (bool | None | Unset): Indicates if chunk separators are regex patterns.
        chunk_separators (None | str | Unset): Chunk separators used for content processing.
        chunk_size (int | None | Unset): Chunk size for content processing.
        content_count (int | Unset): Number of content items associated with the source connection. Default: 0.
        dimensions (int | None | Unset): Dimensions of the embedding model.
        embedding_model (None | str | Unset): Embedding model used for the source connection.
        embedding_model_type (None | str | Unset): Type of the embedding model.
        has_historical_data (bool | Unset): Indicates if the source connection has historical data. Default: False.
        readonly (bool | Unset): Indicates if the source connection is read-only. Default: False.
    """

    account_id: UUID
    content_filter: str
    created_at: str
    id: str
    name: str
    next_poll_at: None | str
    polling: None | str
    polling_action: None | str
    polling_max_items: int | None
    pulled_at: None | str
    retention: int | None
    source_type: str
    updated_at: str
    url: None | str
    avg_episodes_per_month: float | None | Unset = UNSET
    avg_words_per_episode: int | None | Unset = UNSET
    chunk_language: None | str | Unset = UNSET
    chunk_overlap: int | None | Unset = UNSET
    chunk_regex_separators: bool | None | Unset = UNSET
    chunk_separators: None | str | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    content_count: int | Unset = 0
    dimensions: int | None | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    embedding_model_type: None | str | Unset = UNSET
    has_historical_data: bool | Unset = False
    readonly: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        content_filter = self.content_filter

        created_at = self.created_at

        id = self.id

        name = self.name

        next_poll_at: None | str
        next_poll_at = self.next_poll_at

        polling: None | str
        polling = self.polling

        polling_action: None | str
        polling_action = self.polling_action

        polling_max_items: int | None
        polling_max_items = self.polling_max_items

        pulled_at: None | str
        pulled_at = self.pulled_at

        retention: int | None
        retention = self.retention

        source_type = self.source_type

        updated_at = self.updated_at

        url: None | str
        url = self.url

        avg_episodes_per_month: float | None | Unset
        if isinstance(self.avg_episodes_per_month, Unset):
            avg_episodes_per_month = UNSET
        else:
            avg_episodes_per_month = self.avg_episodes_per_month

        avg_words_per_episode: int | None | Unset
        if isinstance(self.avg_words_per_episode, Unset):
            avg_words_per_episode = UNSET
        else:
            avg_words_per_episode = self.avg_words_per_episode

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

        content_count = self.content_count

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

        embedding_model_type: None | str | Unset
        if isinstance(self.embedding_model_type, Unset):
            embedding_model_type = UNSET
        else:
            embedding_model_type = self.embedding_model_type

        has_historical_data = self.has_historical_data

        readonly = self.readonly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "content_filter": content_filter,
                "created_at": created_at,
                "id": id,
                "name": name,
                "next_poll_at": next_poll_at,
                "polling": polling,
                "polling_action": polling_action,
                "polling_max_items": polling_max_items,
                "pulled_at": pulled_at,
                "retention": retention,
                "source_type": source_type,
                "updated_at": updated_at,
                "url": url,
            }
        )
        if avg_episodes_per_month is not UNSET:
            field_dict["avg_episodes_per_month"] = avg_episodes_per_month
        if avg_words_per_episode is not UNSET:
            field_dict["avg_words_per_episode"] = avg_words_per_episode
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
        if content_count is not UNSET:
            field_dict["content_count"] = content_count
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if embedding_model_type is not UNSET:
            field_dict["embedding_model_type"] = embedding_model_type
        if has_historical_data is not UNSET:
            field_dict["has_historical_data"] = has_historical_data
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        content_filter = d.pop("content_filter")

        created_at = d.pop("created_at")

        id = d.pop("id")

        name = d.pop("name")

        def _parse_next_poll_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_poll_at = _parse_next_poll_at(d.pop("next_poll_at"))

        def _parse_polling(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        polling = _parse_polling(d.pop("polling"))

        def _parse_polling_action(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        polling_action = _parse_polling_action(d.pop("polling_action"))

        def _parse_polling_max_items(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        polling_max_items = _parse_polling_max_items(d.pop("polling_max_items"))

        def _parse_pulled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pulled_at = _parse_pulled_at(d.pop("pulled_at"))

        def _parse_retention(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        retention = _parse_retention(d.pop("retention"))

        source_type = d.pop("source_type")

        updated_at = d.pop("updated_at")

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_avg_episodes_per_month(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_episodes_per_month = _parse_avg_episodes_per_month(d.pop("avg_episodes_per_month", UNSET))

        def _parse_avg_words_per_episode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg_words_per_episode = _parse_avg_words_per_episode(d.pop("avg_words_per_episode", UNSET))

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

        chunk_regex_separators = _parse_chunk_regex_separators(d.pop("chunk_regex_separators", UNSET))

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

        content_count = d.pop("content_count", UNSET)

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

        def _parse_embedding_model_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model_type = _parse_embedding_model_type(d.pop("embedding_model_type", UNSET))

        has_historical_data = d.pop("has_historical_data", UNSET)

        readonly = d.pop("readonly", UNSET)

        source_response = cls(
            account_id=account_id,
            content_filter=content_filter,
            created_at=created_at,
            id=id,
            name=name,
            next_poll_at=next_poll_at,
            polling=polling,
            polling_action=polling_action,
            polling_max_items=polling_max_items,
            pulled_at=pulled_at,
            retention=retention,
            source_type=source_type,
            updated_at=updated_at,
            url=url,
            avg_episodes_per_month=avg_episodes_per_month,
            avg_words_per_episode=avg_words_per_episode,
            chunk_language=chunk_language,
            chunk_overlap=chunk_overlap,
            chunk_regex_separators=chunk_regex_separators,
            chunk_separators=chunk_separators,
            chunk_size=chunk_size,
            content_count=content_count,
            dimensions=dimensions,
            embedding_model=embedding_model,
            embedding_model_type=embedding_model_type,
            has_historical_data=has_historical_data,
            readonly=readonly,
        )

        source_response.additional_properties = d
        return source_response

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
