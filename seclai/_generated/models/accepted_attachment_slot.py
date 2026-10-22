from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptedAttachmentSlot")


@_attrs_define
class AcceptedAttachmentSlot:
    """
    Attributes:
        name (str): Lowercase letters, digits and underscores, starting with a letter. Steps reference the files as
            ``{{agent.attachments.<name>}}``.
        content_types (list[str] | Unset): Accepted types, e.g. ``application/pdf`` or ``image/*``; empty accepts any
            type.
        label (None | str | Unset): Shown to people.
        max_ (int | None | Unset): Most files a run may include; empty is no limit.
        min_ (int | Unset): Fewest files a run must include; fewer refuses the run, except on an email trigger set to
            run anyway, which lists the shortfall. Default: 0.
        name_pattern (None | str | Unset): Filename glob a file must also match, ignoring case.
    """

    name: str
    content_types: list[str] | Unset = UNSET
    label: None | str | Unset = UNSET
    max_: int | None | Unset = UNSET
    min_: int | Unset = 0
    name_pattern: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        content_types: list[str] | Unset = UNSET
        if not isinstance(self.content_types, Unset):
            content_types = self.content_types

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_ = self.min_

        name_pattern: None | str | Unset
        if isinstance(self.name_pattern, Unset):
            name_pattern = UNSET
        else:
            name_pattern = self.name_pattern

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if content_types is not UNSET:
            field_dict["content_types"] = content_types
        if label is not UNSET:
            field_dict["label"] = label
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name_pattern is not UNSET:
            field_dict["name_pattern"] = name_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        content_types = cast(list[str], d.pop("content_types", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        min_ = d.pop("min", UNSET)

        def _parse_name_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_pattern = _parse_name_pattern(d.pop("name_pattern", UNSET))

        accepted_attachment_slot = cls(
            name=name,
            content_types=content_types,
            label=label,
            max_=max_,
            min_=min_,
            name_pattern=name_pattern,
        )

        return accepted_attachment_slot
