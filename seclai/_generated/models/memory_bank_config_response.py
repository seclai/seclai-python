from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryBankConfigResponse")


@_attrs_define
class MemoryBankConfigResponse:
    """Suggested memory bank configuration from the AI assistant.

    Attributes:
        mode (str): Memory bank mode.
        name (str): Suggested name.
        type_ (str): Memory bank type: conversation or general.
        compaction_prompt (None | str | Unset): Suggested compaction prompt.
        description (None | str | Unset): Suggested description.
        max_age_days (int | None | Unset): Max age in days.
        max_size_tokens (int | None | Unset): Max size in tokens.
        max_turns (int | None | Unset): Max conversation turns.
        retention_days (int | None | Unset): Retention in days.
    """

    mode: str
    name: str
    type_: str
    compaction_prompt: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    max_age_days: int | None | Unset = UNSET
    max_size_tokens: int | None | Unset = UNSET
    max_turns: int | None | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        name = self.name

        type_ = self.type_

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

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "name": name,
                "type": type_,
            }
        )
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
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = d.pop("mode")

        name = d.pop("name")

        type_ = d.pop("type")

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

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        memory_bank_config_response = cls(
            mode=mode,
            name=name,
            type_=type_,
            compaction_prompt=compaction_prompt,
            description=description,
            max_age_days=max_age_days,
            max_size_tokens=max_size_tokens,
            max_turns=max_turns,
            retention_days=retention_days,
        )

        memory_bank_config_response.additional_properties = d
        return memory_bank_config_response

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
