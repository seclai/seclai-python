from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimateResponse")


@_attrs_define
class CostEstimateResponse:
    """Response model for cost estimation.

    Attributes:
        default_dimension (int): Default dimension size
        default_model_name (str): Name of the default embedding model
        chunks_per_episode (int | None | Unset): Number of chunks per episode
        cost_per_episode (float | None | Unset): Total cost per episode (processing + indexing + storage for 1 month)
        cost_per_month (float | None | Unset): Total cost per month at current episode frequency
        episodes_per_day (float | None | Unset): Episodes per day
        feed_processing_cost_per_episode (float | None | Unset): Cost in credits for processing feed per episode
        indexing_cost (float | None | Unset): Total cost for embedding generation
        indexing_cost_per_episode (float | None | Unset): Cost in credits for indexing per episode
        num_chunks (int | None | Unset): Total number of chunks
        page_processing_cost (float | None | Unset): Total cost for processing all pages
        storage_cost (float | None | Unset): Total storage cost for retention period
        storage_cost_per_chunk_per_month (float | None | Unset): Cost in credits for storing one chunk for one month
        total_cost (float | None | Unset): Total estimated cost
    """

    default_dimension: int
    default_model_name: str
    chunks_per_episode: int | None | Unset = UNSET
    cost_per_episode: float | None | Unset = UNSET
    cost_per_month: float | None | Unset = UNSET
    episodes_per_day: float | None | Unset = UNSET
    feed_processing_cost_per_episode: float | None | Unset = UNSET
    indexing_cost: float | None | Unset = UNSET
    indexing_cost_per_episode: float | None | Unset = UNSET
    num_chunks: int | None | Unset = UNSET
    page_processing_cost: float | None | Unset = UNSET
    storage_cost: float | None | Unset = UNSET
    storage_cost_per_chunk_per_month: float | None | Unset = UNSET
    total_cost: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_dimension = self.default_dimension

        default_model_name = self.default_model_name

        chunks_per_episode: int | None | Unset
        if isinstance(self.chunks_per_episode, Unset):
            chunks_per_episode = UNSET
        else:
            chunks_per_episode = self.chunks_per_episode

        cost_per_episode: float | None | Unset
        if isinstance(self.cost_per_episode, Unset):
            cost_per_episode = UNSET
        else:
            cost_per_episode = self.cost_per_episode

        cost_per_month: float | None | Unset
        if isinstance(self.cost_per_month, Unset):
            cost_per_month = UNSET
        else:
            cost_per_month = self.cost_per_month

        episodes_per_day: float | None | Unset
        if isinstance(self.episodes_per_day, Unset):
            episodes_per_day = UNSET
        else:
            episodes_per_day = self.episodes_per_day

        feed_processing_cost_per_episode: float | None | Unset
        if isinstance(self.feed_processing_cost_per_episode, Unset):
            feed_processing_cost_per_episode = UNSET
        else:
            feed_processing_cost_per_episode = self.feed_processing_cost_per_episode

        indexing_cost: float | None | Unset
        if isinstance(self.indexing_cost, Unset):
            indexing_cost = UNSET
        else:
            indexing_cost = self.indexing_cost

        indexing_cost_per_episode: float | None | Unset
        if isinstance(self.indexing_cost_per_episode, Unset):
            indexing_cost_per_episode = UNSET
        else:
            indexing_cost_per_episode = self.indexing_cost_per_episode

        num_chunks: int | None | Unset
        if isinstance(self.num_chunks, Unset):
            num_chunks = UNSET
        else:
            num_chunks = self.num_chunks

        page_processing_cost: float | None | Unset
        if isinstance(self.page_processing_cost, Unset):
            page_processing_cost = UNSET
        else:
            page_processing_cost = self.page_processing_cost

        storage_cost: float | None | Unset
        if isinstance(self.storage_cost, Unset):
            storage_cost = UNSET
        else:
            storage_cost = self.storage_cost

        storage_cost_per_chunk_per_month: float | None | Unset
        if isinstance(self.storage_cost_per_chunk_per_month, Unset):
            storage_cost_per_chunk_per_month = UNSET
        else:
            storage_cost_per_chunk_per_month = self.storage_cost_per_chunk_per_month

        total_cost: float | None | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_dimension": default_dimension,
                "default_model_name": default_model_name,
            }
        )
        if chunks_per_episode is not UNSET:
            field_dict["chunks_per_episode"] = chunks_per_episode
        if cost_per_episode is not UNSET:
            field_dict["cost_per_episode"] = cost_per_episode
        if cost_per_month is not UNSET:
            field_dict["cost_per_month"] = cost_per_month
        if episodes_per_day is not UNSET:
            field_dict["episodes_per_day"] = episodes_per_day
        if feed_processing_cost_per_episode is not UNSET:
            field_dict["feed_processing_cost_per_episode"] = feed_processing_cost_per_episode
        if indexing_cost is not UNSET:
            field_dict["indexing_cost"] = indexing_cost
        if indexing_cost_per_episode is not UNSET:
            field_dict["indexing_cost_per_episode"] = indexing_cost_per_episode
        if num_chunks is not UNSET:
            field_dict["num_chunks"] = num_chunks
        if page_processing_cost is not UNSET:
            field_dict["page_processing_cost"] = page_processing_cost
        if storage_cost is not UNSET:
            field_dict["storage_cost"] = storage_cost
        if storage_cost_per_chunk_per_month is not UNSET:
            field_dict["storage_cost_per_chunk_per_month"] = storage_cost_per_chunk_per_month
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_dimension = d.pop("default_dimension")

        default_model_name = d.pop("default_model_name")

        def _parse_chunks_per_episode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunks_per_episode = _parse_chunks_per_episode(d.pop("chunks_per_episode", UNSET))

        def _parse_cost_per_episode(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_per_episode = _parse_cost_per_episode(d.pop("cost_per_episode", UNSET))

        def _parse_cost_per_month(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_per_month = _parse_cost_per_month(d.pop("cost_per_month", UNSET))

        def _parse_episodes_per_day(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        episodes_per_day = _parse_episodes_per_day(d.pop("episodes_per_day", UNSET))

        def _parse_feed_processing_cost_per_episode(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        feed_processing_cost_per_episode = _parse_feed_processing_cost_per_episode(
            d.pop("feed_processing_cost_per_episode", UNSET)
        )

        def _parse_indexing_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        indexing_cost = _parse_indexing_cost(d.pop("indexing_cost", UNSET))

        def _parse_indexing_cost_per_episode(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        indexing_cost_per_episode = _parse_indexing_cost_per_episode(d.pop("indexing_cost_per_episode", UNSET))

        def _parse_num_chunks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_chunks = _parse_num_chunks(d.pop("num_chunks", UNSET))

        def _parse_page_processing_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        page_processing_cost = _parse_page_processing_cost(d.pop("page_processing_cost", UNSET))

        def _parse_storage_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage_cost = _parse_storage_cost(d.pop("storage_cost", UNSET))

        def _parse_storage_cost_per_chunk_per_month(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage_cost_per_chunk_per_month = _parse_storage_cost_per_chunk_per_month(
            d.pop("storage_cost_per_chunk_per_month", UNSET)
        )

        def _parse_total_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_cost = _parse_total_cost(d.pop("total_cost", UNSET))

        cost_estimate_response = cls(
            default_dimension=default_dimension,
            default_model_name=default_model_name,
            chunks_per_episode=chunks_per_episode,
            cost_per_episode=cost_per_episode,
            cost_per_month=cost_per_month,
            episodes_per_day=episodes_per_day,
            feed_processing_cost_per_episode=feed_processing_cost_per_episode,
            indexing_cost=indexing_cost,
            indexing_cost_per_episode=indexing_cost_per_episode,
            num_chunks=num_chunks,
            page_processing_cost=page_processing_cost,
            storage_cost=storage_cost,
            storage_cost_per_chunk_per_month=storage_cost_per_chunk_per_month,
            total_cost=total_cost,
        )

        cost_estimate_response.additional_properties = d
        return cost_estimate_response

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
