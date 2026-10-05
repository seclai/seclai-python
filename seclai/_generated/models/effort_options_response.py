from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EffortOptionsResponse")


@_attrs_define
class EffortOptionsResponse:
    """The reasoning-effort values a model accepts.

    Attributes:
        kind (str): `levels` today: `values` lists them.
        default (None | str | Unset): The vendor's default level, when known.
        values (list[str] | Unset): Accepted values, weakest first.
    """

    kind: str
    default: None | str | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        default: None | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        def _parse_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        values = cast(list[str], d.pop("values", UNSET))

        effort_options_response = cls(
            kind=kind,
            default=default,
            values=values,
        )

        effort_options_response.additional_properties = d
        return effort_options_response

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
