from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_import_preview_request_agent_definition import (
        AgentImportPreviewRequestAgentDefinition,
    )


T = TypeVar("T", bound="AgentImportPreviewRequest")


@_attrs_define
class AgentImportPreviewRequest:
    """Dry-run import request — same payload shape as the export endpoint.

    Attributes:
        agent_definition (AgentImportPreviewRequestAgentDefinition): Payload in the same shape as GET
            /api/agents/{agent_id}/export.
    """

    agent_definition: AgentImportPreviewRequestAgentDefinition
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_definition = self.agent_definition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_definition": agent_definition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_import_preview_request_agent_definition import (
            AgentImportPreviewRequestAgentDefinition,
        )

        d = dict(src_dict)
        agent_definition = AgentImportPreviewRequestAgentDefinition.from_dict(
            d.pop("agent_definition")
        )

        agent_import_preview_request = cls(
            agent_definition=agent_definition,
        )

        agent_import_preview_request.additional_properties = d
        return agent_import_preview_request

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
