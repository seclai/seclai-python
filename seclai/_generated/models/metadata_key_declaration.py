from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.metadata_origin import MetadataOrigin
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataKeyDeclaration")


@_attrs_define
class MetadataKeyDeclaration:
    """
    Attributes:
        key (str): Steps reference the key as ``{{metadata.<key>}}``.
        origin (MetadataOrigin): Who writes a run metadata key (docs/architecture/run-metadata.md, Q2).
        required (bool | Unset): A caller-started run without this key is refused. Only a ``custom`` key can be
            required. Default: False.
    """

    key: str
    origin: MetadataOrigin
    required: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        origin = self.origin.value

        required = self.required

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "origin": origin,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        origin = MetadataOrigin(d.pop("origin"))

        required = d.pop("required", UNSET)

        metadata_key_declaration = cls(
            key=key,
            origin=origin,
            required=required,
        )

        return metadata_key_declaration
