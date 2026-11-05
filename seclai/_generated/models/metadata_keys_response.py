from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.declarable_metadata_key import DeclarableMetadataKey
    from ..models.metadata_key_declaration import MetadataKeyDeclaration


T = TypeVar("T", bound="MetadataKeysResponse")


@_attrs_define
class MetadataKeysResponse:
    """
    Attributes:
        accepts_any_source_key (bool): True for content triggers, which may declare any item-metadata key.
        agent_id (UUID):
        declarable_keys (list[DeclarableMetadataKey]): The system and source keys this trigger's type can declare.
        metadata_keys (list[MetadataKeyDeclaration]): The keys the agent's steps may reference. Static trigger metadata
            and Slack form fields are declared custom keys too, and are not repeated here.
        trigger_id (UUID):
        warnings (list[str] | Unset): Set by a PUT that changes the declaration: agents whose `call_agent` mapping no
            longer fits it. Always empty on GET.
    """

    accepts_any_source_key: bool
    agent_id: UUID
    declarable_keys: list[DeclarableMetadataKey]
    metadata_keys: list[MetadataKeyDeclaration]
    trigger_id: UUID
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepts_any_source_key = self.accepts_any_source_key

        agent_id = str(self.agent_id)

        declarable_keys = []
        for declarable_keys_item_data in self.declarable_keys:
            declarable_keys_item = declarable_keys_item_data.to_dict()
            declarable_keys.append(declarable_keys_item)

        metadata_keys = []
        for metadata_keys_item_data in self.metadata_keys:
            metadata_keys_item = metadata_keys_item_data.to_dict()
            metadata_keys.append(metadata_keys_item)

        trigger_id = str(self.trigger_id)

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepts_any_source_key": accepts_any_source_key,
                "agent_id": agent_id,
                "declarable_keys": declarable_keys,
                "metadata_keys": metadata_keys,
                "trigger_id": trigger_id,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.declarable_metadata_key import DeclarableMetadataKey
        from ..models.metadata_key_declaration import MetadataKeyDeclaration

        d = dict(src_dict)
        accepts_any_source_key = d.pop("accepts_any_source_key")

        agent_id = UUID(d.pop("agent_id"))

        declarable_keys = []
        _declarable_keys = d.pop("declarable_keys")
        for declarable_keys_item_data in _declarable_keys:
            declarable_keys_item = DeclarableMetadataKey.from_dict(
                declarable_keys_item_data
            )

            declarable_keys.append(declarable_keys_item)

        metadata_keys = []
        _metadata_keys = d.pop("metadata_keys")
        for metadata_keys_item_data in _metadata_keys:
            metadata_keys_item = MetadataKeyDeclaration.from_dict(
                metadata_keys_item_data
            )

            metadata_keys.append(metadata_keys_item)

        trigger_id = UUID(d.pop("trigger_id"))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        metadata_keys_response = cls(
            accepts_any_source_key=accepts_any_source_key,
            agent_id=agent_id,
            declarable_keys=declarable_keys,
            metadata_keys=metadata_keys,
            trigger_id=trigger_id,
            warnings=warnings,
        )

        metadata_keys_response.additional_properties = d
        return metadata_keys_response

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
