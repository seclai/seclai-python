from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMemoryBankBody")


@_attrs_define
class CreateMemoryBankBody:
    """Request body for creating a memory bank.

    Attributes:
        name (str): Memory bank name.
        chunk_overlap (int | None | Unset): Chunk overlap (custom mode only).
        chunk_size (int | None | Unset): Chunk size (custom mode only).
        compaction_prompt (None | str | Unset): Custom prompt used when compacting older entries. When set, entries that
            exceed a threshold are summarized into a new entry before being soft-deleted.
        description (None | str | Unset): Optional description of the bank's purpose.
        dimensions (int | None | Unset): Embedding dimensions (custom mode only).
        embedding_model (None | str | Unset): Custom embedding model (custom mode only).
        max_age_days (int | None | Unset): Max entry age in days before compaction. Checked inline after each write and
            by the hourly background sweep.
        max_size_tokens (int | None | Unset): Max total tokens (per partition) before compaction. Checked inline after
            each write and by the hourly background sweep.
        max_turns (int | None | Unset): Max conversation turns (per partition) before compaction. Checked inline after
            each write and by the hourly background sweep.
        mode (str | Unset): Embedding quality / cost trade-off. One of: fast_and_cheap, balanced, slow_and_thorough,
            custom. Default: 'fast_and_cheap'.
        retention_days (int | None | Unset): Content source retention in days. Default: 30.
        type_ (str | Unset): Bank type. 'conversation' for chat-turn data with conversation_key + speaker; 'general' for
            flat entries with optional group_key. Default: 'conversation'.
    """

    name: str
    chunk_overlap: int | None | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    compaction_prompt: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    dimensions: int | None | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    max_age_days: int | None | Unset = UNSET
    max_size_tokens: int | None | Unset = UNSET
    max_turns: int | None | Unset = UNSET
    mode: str | Unset = "fast_and_cheap"
    retention_days: int | None | Unset = 30
    type_: str | Unset = "conversation"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        mode = self.mode

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
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
        if mode is not UNSET:
            field_dict["mode"] = mode
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

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

        mode = d.pop("mode", UNSET)

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        type_ = d.pop("type", UNSET)

        create_memory_bank_body = cls(
            name=name,
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
            compaction_prompt=compaction_prompt,
            description=description,
            dimensions=dimensions,
            embedding_model=embedding_model,
            max_age_days=max_age_days,
            max_size_tokens=max_size_tokens,
            max_turns=max_turns,
            mode=mode,
            retention_days=retention_days,
            type_=type_,
        )

        create_memory_bank_body.additional_properties = d
        return create_memory_bank_body

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
