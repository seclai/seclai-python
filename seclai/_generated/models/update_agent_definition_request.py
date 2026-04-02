from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_agent_definition_request_definition import (
        UpdateAgentDefinitionRequestDefinition,
    )


T = TypeVar("T", bound="UpdateAgentDefinitionRequest")


@_attrs_define
class UpdateAgentDefinitionRequest:
    """
    Attributes:
        definition (UpdateAgentDefinitionRequestDefinition): The full agent definition (name, description, tags, steps).
            Steps form a tree workflow. Each step has a `step_type`, `id`, `name`, and type-specific config. Content
            enrichment steps (write_metadata, write_content_attachment, load_content_attachment, load_content) require
            content-triggered agents.
        expected_change_id (str): The change_id from the last GET, for optimistic locking.
    """

    definition: UpdateAgentDefinitionRequestDefinition
    expected_change_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        definition = self.definition.to_dict()

        expected_change_id = self.expected_change_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "definition": definition,
                "expected_change_id": expected_change_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_agent_definition_request_definition import (
            UpdateAgentDefinitionRequestDefinition,
        )

        d = dict(src_dict)
        definition = UpdateAgentDefinitionRequestDefinition.from_dict(
            d.pop("definition")
        )

        expected_change_id = d.pop("expected_change_id")

        update_agent_definition_request = cls(
            definition=definition,
            expected_change_id=expected_change_id,
        )

        update_agent_definition_request.additional_properties = d
        return update_agent_definition_request

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
