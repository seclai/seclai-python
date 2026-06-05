from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentRefsSourceApiSummary")


@_attrs_define
class AttachmentRefsSourceApiSummary:
    """Per-source attachment-reference summary.

    Attributes:
        exact_names (list[str] | Unset):
        indexes_max (int | None | Unset):
        kinds (list[str] | Unset):
        patterns (list[str] | Unset):
    """

    exact_names: list[str] | Unset = UNSET
    indexes_max: int | None | Unset = UNSET
    kinds: list[str] | Unset = UNSET
    patterns: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exact_names: list[str] | Unset = UNSET
        if not isinstance(self.exact_names, Unset):
            exact_names = self.exact_names

        indexes_max: int | None | Unset
        if isinstance(self.indexes_max, Unset):
            indexes_max = UNSET
        else:
            indexes_max = self.indexes_max

        kinds: list[str] | Unset = UNSET
        if not isinstance(self.kinds, Unset):
            kinds = self.kinds

        patterns: list[str] | Unset = UNSET
        if not isinstance(self.patterns, Unset):
            patterns = self.patterns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exact_names is not UNSET:
            field_dict["exact_names"] = exact_names
        if indexes_max is not UNSET:
            field_dict["indexes_max"] = indexes_max
        if kinds is not UNSET:
            field_dict["kinds"] = kinds
        if patterns is not UNSET:
            field_dict["patterns"] = patterns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exact_names = cast(list[str], d.pop("exact_names", UNSET))

        def _parse_indexes_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        indexes_max = _parse_indexes_max(d.pop("indexes_max", UNSET))

        kinds = cast(list[str], d.pop("kinds", UNSET))

        patterns = cast(list[str], d.pop("patterns", UNSET))

        attachment_refs_source_api_summary = cls(
            exact_names=exact_names,
            indexes_max=indexes_max,
            kinds=kinds,
            patterns=patterns,
        )

        attachment_refs_source_api_summary.additional_properties = d
        return attachment_refs_source_api_summary

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
