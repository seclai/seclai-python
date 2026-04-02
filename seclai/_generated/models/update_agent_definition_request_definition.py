from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAgentDefinitionRequestDefinition")


@_attrs_define
class UpdateAgentDefinitionRequestDefinition:
    """The full agent definition (name, description, tags, steps). Steps form a tree workflow. Each step has a `step_type`,
    `id`, `name`, and type-specific config. Content enrichment steps (write_metadata, write_content_attachment,
    load_content_attachment, load_content) require content-triggered agents.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        update_agent_definition_request_definition = cls()

        update_agent_definition_request_definition.additional_properties = d
        return update_agent_definition_request_definition

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
