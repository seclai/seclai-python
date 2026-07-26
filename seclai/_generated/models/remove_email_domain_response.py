from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveEmailDomainResponse")


@_attrs_define
class RemoveEmailDomainResponse:
    """
    Attributes:
        cleanup_note (None | str | Unset):
        removed (bool | Unset):  Default: True.
    """

    cleanup_note: None | str | Unset = UNSET
    removed: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cleanup_note: None | str | Unset
        if isinstance(self.cleanup_note, Unset):
            cleanup_note = UNSET
        else:
            cleanup_note = self.cleanup_note

        removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cleanup_note is not UNSET:
            field_dict["cleanup_note"] = cleanup_note
        if removed is not UNSET:
            field_dict["removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cleanup_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cleanup_note = _parse_cleanup_note(d.pop("cleanup_note", UNSET))

        removed = d.pop("removed", UNSET)

        remove_email_domain_response = cls(
            cleanup_note=cleanup_note,
            removed=removed,
        )

        remove_email_domain_response.additional_properties = d
        return remove_email_domain_response

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
