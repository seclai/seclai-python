from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.solution_agent_response import SolutionAgentResponse
    from ..models.solution_knowledge_base_response import SolutionKnowledgeBaseResponse
    from ..models.solution_source_connection_response import (
        SolutionSourceConnectionResponse,
    )


T = TypeVar("T", bound="SolutionResponse")


@_attrs_define
class SolutionResponse:
    """Response model for solution data.

    Attributes:
        agents (list[SolutionAgentResponse]): Agents linked to the solution.
        created_at (str): Timestamp when the solution was created.
        description (str): Description of the solution.
        id (UUID): Unique identifier for the solution.
        knowledge_bases (list[SolutionKnowledgeBaseResponse]): Knowledge bases linked to the solution.
        name (str): Name of the solution.
        source_connections (list[SolutionSourceConnectionResponse]): Source connections linked to the solution.
        updated_at (str): Timestamp when the solution was last updated.
    """

    agents: list[SolutionAgentResponse]
    created_at: str
    description: str
    id: UUID
    knowledge_bases: list[SolutionKnowledgeBaseResponse]
    name: str
    source_connections: list[SolutionSourceConnectionResponse]
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        created_at = self.created_at

        description = self.description

        id = str(self.id)

        knowledge_bases = []
        for knowledge_bases_item_data in self.knowledge_bases:
            knowledge_bases_item = knowledge_bases_item_data.to_dict()
            knowledge_bases.append(knowledge_bases_item)

        name = self.name

        source_connections = []
        for source_connections_item_data in self.source_connections:
            source_connections_item = source_connections_item_data.to_dict()
            source_connections.append(source_connections_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agents": agents,
                "created_at": created_at,
                "description": description,
                "id": id,
                "knowledge_bases": knowledge_bases,
                "name": name,
                "source_connections": source_connections,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.solution_agent_response import SolutionAgentResponse
        from ..models.solution_knowledge_base_response import (
            SolutionKnowledgeBaseResponse,
        )
        from ..models.solution_source_connection_response import (
            SolutionSourceConnectionResponse,
        )

        d = dict(src_dict)
        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = SolutionAgentResponse.from_dict(agents_item_data)

            agents.append(agents_item)

        created_at = d.pop("created_at")

        description = d.pop("description")

        id = UUID(d.pop("id"))

        knowledge_bases = []
        _knowledge_bases = d.pop("knowledge_bases")
        for knowledge_bases_item_data in _knowledge_bases:
            knowledge_bases_item = SolutionKnowledgeBaseResponse.from_dict(
                knowledge_bases_item_data
            )

            knowledge_bases.append(knowledge_bases_item)

        name = d.pop("name")

        source_connections = []
        _source_connections = d.pop("source_connections")
        for source_connections_item_data in _source_connections:
            source_connections_item = SolutionSourceConnectionResponse.from_dict(
                source_connections_item_data
            )

            source_connections.append(source_connections_item)

        updated_at = d.pop("updated_at")

        solution_response = cls(
            agents=agents,
            created_at=created_at,
            description=description,
            id=id,
            knowledge_bases=knowledge_bases,
            name=name,
            source_connections=source_connections,
            updated_at=updated_at,
        )

        solution_response.additional_properties = d
        return solution_response

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
