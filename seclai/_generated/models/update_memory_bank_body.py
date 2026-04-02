from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMemoryBankBody")


@_attrs_define
class UpdateMemoryBankBody:
    """Request body for updating a memory bank.

    Omitted fields are left unchanged.  To **clear** a field back to null,
    send a zero-value sentinel: ``0`` for integers, ``""`` for strings.

        Attributes:
            compaction_prompt (None | str | Unset): Custom prompt used when compacting older entries. When set, entries that
                exceed a threshold are summarized into a new entry before being soft-deleted. Send empty string "" to clear and
                disable summarisation.
            description (None | str | Unset): Optional description. Send empty string "" to clear.
            max_age_days (int | None | Unset): Max entry age in days before compaction. Checked inline after each write and
                by the hourly background sweep. Send 0 to disable.
            max_size_tokens (int | None | Unset): Max total tokens (per partition) before compaction. Checked inline after
                each write and by the hourly background sweep. Send 0 to disable.
            max_turns (int | None | Unset): Max conversation turns (per partition) before compaction. Checked inline after
                each write and by the hourly background sweep. Send 0 to disable.
            name (None | str | Unset): New name.
            retention_days (int | None | Unset): Content source retention in days. Send 0 to clear (indefinite).
    """

    compaction_prompt: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    max_age_days: int | None | Unset = UNSET
    max_size_tokens: int | None | Unset = UNSET
    max_turns: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compaction_prompt is not UNSET:
            field_dict["compaction_prompt"] = compaction_prompt
        if description is not UNSET:
            field_dict["description"] = description
        if max_age_days is not UNSET:
            field_dict["max_age_days"] = max_age_days
        if max_size_tokens is not UNSET:
            field_dict["max_size_tokens"] = max_size_tokens
        if max_turns is not UNSET:
            field_dict["max_turns"] = max_turns
        if name is not UNSET:
            field_dict["name"] = name
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        update_memory_bank_body = cls(
            compaction_prompt=compaction_prompt,
            description=description,
            max_age_days=max_age_days,
            max_size_tokens=max_size_tokens,
            max_turns=max_turns,
            name=name,
            retention_days=retention_days,
        )

        update_memory_bank_body.additional_properties = d
        return update_memory_bank_body

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
