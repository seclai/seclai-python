from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryBank")


@_attrs_define
class MemoryBank:
    """Response model for a single memory bank.

    Attributes:
        created_at (str): ISO-8601 creation timestamp.
        id (str): Unique memory bank identifier.
        mode (str): Embedding mode: fast_and_cheap, balanced, slow_and_thorough, or custom.
        name (str): Human-readable name.
        type_ (str): Bank type: conversation (chat-turn with speaker) or general (flat entries).
        updated_at (str): ISO-8601 last-update timestamp.
        chunk_overlap (int | None | Unset): Character overlap between chunks.
        chunk_size (int | None | Unset): Characters per chunk.
        compaction_prompt (None | str | Unset): Custom prompt used when compacting older entries. When set, entries that
            exceed a threshold are summarized into a new entry before being soft-deleted.
        description (None | str | Unset): Optional description of the memory bank's purpose.
        dimensions (int | None | Unset): Vector embedding dimensions.
        embedding_model (None | str | Unset): Embedding model identifier.
        max_age_days (int | None | Unset): Max entry age in days before compaction. Checked both inline after each write
            and by the hourly background sweep.
        max_size_tokens (int | None | Unset): Max total tokens (per partition) before compaction. Checked both inline
            after each write and by the hourly background sweep.
        max_turns (int | None | Unset): Max conversation turns (per partition) before compaction. Checked both inline
            after each write and by the hourly background sweep.
        retention_days (int | None | Unset): Content retention period in days (null = indefinite).
        source_connection_id (None | str | Unset): Linked content source ID (null if not yet provisioned).
    """

    created_at: str
    id: str
    mode: str
    name: str
    type_: str
    updated_at: str
    chunk_overlap: int | None | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    compaction_prompt: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    dimensions: int | None | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    max_age_days: int | None | Unset = UNSET
    max_size_tokens: int | None | Unset = UNSET
    max_turns: int | None | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    source_connection_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        mode = self.mode

        name = self.name

        type_ = self.type_

        updated_at = self.updated_at

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

        compaction_prompt: None | str | Unset
        if isinstance(self.compaction_prompt, Unset):
            compaction_prompt = UNSET
        else:
            compaction_prompt = self.compaction_prompt

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        max_age_days: int | None | Unset
        if isinstance(self.max_age_days, Unset):
            max_age_days = UNSET
        else:
            max_age_days = self.max_age_days

        max_size_tokens: int | None | Unset
        if isinstance(self.max_size_tokens, Unset):
            max_size_tokens = UNSET
        else:
            max_size_tokens = self.max_size_tokens

        max_turns: int | None | Unset
        if isinstance(self.max_turns, Unset):
            max_turns = UNSET
        else:
            max_turns = self.max_turns

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        source_connection_id: None | str | Unset
        if isinstance(self.source_connection_id, Unset):
            source_connection_id = UNSET
        else:
            source_connection_id = self.source_connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "mode": mode,
                "name": name,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if compaction_prompt is not UNSET:
            field_dict["compaction_prompt"] = compaction_prompt
        if description is not UNSET:
            field_dict["description"] = description
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if max_age_days is not UNSET:
            field_dict["max_age_days"] = max_age_days
        if max_size_tokens is not UNSET:
            field_dict["max_size_tokens"] = max_size_tokens
        if max_turns is not UNSET:
            field_dict["max_turns"] = max_turns
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if source_connection_id is not UNSET:
            field_dict["source_connection_id"] = source_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = d.pop("id")

        mode = d.pop("mode")

        name = d.pop("name")

        type_ = d.pop("type")

        updated_at = d.pop("updated_at")

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

        def _parse_compaction_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compaction_prompt = _parse_compaction_prompt(d.pop("compaction_prompt", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_max_age_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_age_days = _parse_max_age_days(d.pop("max_age_days", UNSET))

        def _parse_max_size_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_size_tokens = _parse_max_size_tokens(d.pop("max_size_tokens", UNSET))

        def _parse_max_turns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_turns = _parse_max_turns(d.pop("max_turns", UNSET))

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        def _parse_source_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_connection_id = _parse_source_connection_id(
            d.pop("source_connection_id", UNSET)
        )

        memory_bank = cls(
            created_at=created_at,
            id=id,
            mode=mode,
            name=name,
            type_=type_,
            updated_at=updated_at,
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
            compaction_prompt=compaction_prompt,
            description=description,
            dimensions=dimensions,
            embedding_model=embedding_model,
            max_age_days=max_age_days,
            max_size_tokens=max_size_tokens,
            max_turns=max_turns,
            retention_days=retention_days,
            source_connection_id=source_connection_id,
        )

        memory_bank.additional_properties = d
        return memory_bank

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
