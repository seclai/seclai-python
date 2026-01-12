from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimateRequest")


@_attrs_define
class CostEstimateRequest:
    """Request model for cost estimation.

    Attributes:
        chunk_overlap (int | Unset): Chunk overlap in characters Default: 200.
        chunk_size (int | Unset): Chunk size in characters Default: 1000.
        episodes_per_day (float | None | Unset): Number of episodes per day
        num_pages (int | None | Unset): Number of pages
        retention_months (int | None | Unset): Retention period in months
        source_type (None | str | Unset): Source type: 'rss_feed' or 'website'. If not provided, will be inferred from
            other fields.
        words_per_episode (int | None | Unset): Number of words per episode
        words_per_page (int | None | Unset): Average words per page
    """

    chunk_overlap: int | Unset = 200
    chunk_size: int | Unset = 1000
    episodes_per_day: float | None | Unset = UNSET
    num_pages: int | None | Unset = UNSET
    retention_months: int | None | Unset = UNSET
    source_type: None | str | Unset = UNSET
    words_per_episode: int | None | Unset = UNSET
    words_per_page: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunk_overlap = self.chunk_overlap

        chunk_size = self.chunk_size

        episodes_per_day: float | None | Unset
        if isinstance(self.episodes_per_day, Unset):
            episodes_per_day = UNSET
        else:
            episodes_per_day = self.episodes_per_day

        num_pages: int | None | Unset
        if isinstance(self.num_pages, Unset):
            num_pages = UNSET
        else:
            num_pages = self.num_pages

        retention_months: int | None | Unset
        if isinstance(self.retention_months, Unset):
            retention_months = UNSET
        else:
            retention_months = self.retention_months

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        words_per_episode: int | None | Unset
        if isinstance(self.words_per_episode, Unset):
            words_per_episode = UNSET
        else:
            words_per_episode = self.words_per_episode

        words_per_page: int | None | Unset
        if isinstance(self.words_per_page, Unset):
            words_per_page = UNSET
        else:
            words_per_page = self.words_per_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if episodes_per_day is not UNSET:
            field_dict["episodes_per_day"] = episodes_per_day
        if num_pages is not UNSET:
            field_dict["num_pages"] = num_pages
        if retention_months is not UNSET:
            field_dict["retention_months"] = retention_months
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if words_per_episode is not UNSET:
            field_dict["words_per_episode"] = words_per_episode
        if words_per_page is not UNSET:
            field_dict["words_per_page"] = words_per_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_overlap = d.pop("chunk_overlap", UNSET)

        chunk_size = d.pop("chunk_size", UNSET)

        def _parse_episodes_per_day(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        episodes_per_day = _parse_episodes_per_day(d.pop("episodes_per_day", UNSET))

        def _parse_num_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_pages = _parse_num_pages(d.pop("num_pages", UNSET))

        def _parse_retention_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_months = _parse_retention_months(d.pop("retention_months", UNSET))

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_words_per_episode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        words_per_episode = _parse_words_per_episode(d.pop("words_per_episode", UNSET))

        def _parse_words_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        words_per_page = _parse_words_per_page(d.pop("words_per_page", UNSET))

        cost_estimate_request = cls(
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
            episodes_per_day=episodes_per_day,
            num_pages=num_pages,
            retention_months=retention_months,
            source_type=source_type,
            words_per_episode=words_per_episode,
            words_per_page=words_per_page,
        )

        cost_estimate_request.additional_properties = d
        return cost_estimate_request

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
