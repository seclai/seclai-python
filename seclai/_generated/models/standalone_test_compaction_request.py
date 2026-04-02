from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StandaloneTestCompactionRequest")


@_attrs_define
class StandaloneTestCompactionRequest:
    """Request body for testing a compaction prompt *without* an existing bank.

    Used on the create-memory-bank page where no bank ID exists yet.
    ``compaction_prompt`` is required (no bank to fall back to).
    Content must come from ``sample_entries`` or ``generate_direction``
    (no existing entries to fetch).

        Attributes:
            compaction_prompt (str): Compaction prompt to test.
            bank_type (str | Unset): Memory bank type ('conversation' or 'general') — controls the style of generated
                entries. Default: 'conversation'.
            entry_count (int | Unset): Number of entries to generate when using generate_direction. Default: 5.
            generate_direction (None | str | Unset): Direction for the LLM to generate sample entries.
            sample_entries (list[str] | None | Unset): Explicit sample entries to compact.
    """

    compaction_prompt: str
    bank_type: str | Unset = "conversation"
    entry_count: int | Unset = 5
    generate_direction: None | str | Unset = UNSET
    sample_entries: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compaction_prompt = self.compaction_prompt

        bank_type = self.bank_type

        entry_count = self.entry_count

        generate_direction: None | str | Unset
        if isinstance(self.generate_direction, Unset):
            generate_direction = UNSET
        else:
            generate_direction = self.generate_direction

        sample_entries: list[str] | None | Unset
        if isinstance(self.sample_entries, Unset):
            sample_entries = UNSET
        elif isinstance(self.sample_entries, list):
            sample_entries = self.sample_entries

        else:
            sample_entries = self.sample_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compaction_prompt": compaction_prompt,
            }
        )
        if bank_type is not UNSET:
            field_dict["bank_type"] = bank_type
        if entry_count is not UNSET:
            field_dict["entry_count"] = entry_count
        if generate_direction is not UNSET:
            field_dict["generate_direction"] = generate_direction
        if sample_entries is not UNSET:
            field_dict["sample_entries"] = sample_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        compaction_prompt = d.pop("compaction_prompt")

        bank_type = d.pop("bank_type", UNSET)

        entry_count = d.pop("entry_count", UNSET)

        def _parse_generate_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generate_direction = _parse_generate_direction(
            d.pop("generate_direction", UNSET)
        )

        def _parse_sample_entries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sample_entries_type_0 = cast(list[str], data)

                return sample_entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sample_entries = _parse_sample_entries(d.pop("sample_entries", UNSET))

        standalone_test_compaction_request = cls(
            compaction_prompt=compaction_prompt,
            bank_type=bank_type,
            entry_count=entry_count,
            generate_direction=generate_direction,
            sample_entries=sample_entries,
        )

        standalone_test_compaction_request.additional_properties = d
        return standalone_test_compaction_request

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
