from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SolutionSummaryResponse")


@_attrs_define
class SolutionSummaryResponse:
    """Response model for solution summary.

    Attributes:
        agent_count (int): Number of linked agents.
        created_at (str): Timestamp when the solution was created.
        description (str): Description of the solution.
        id (UUID): Unique identifier for the solution.
        knowledge_base_count (int): Number of linked knowledge bases.
        memory_bank_count (int): Number of linked memory banks.
        name (str): Name of the solution.
        source_connection_count (int): Number of linked source connections.
        updated_at (str): Timestamp when the solution was last updated.
    """

    agent_count: int
    created_at: str
    description: str
    id: UUID
    knowledge_base_count: int
    memory_bank_count: int
    name: str
    source_connection_count: int
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_count = self.agent_count

        created_at = self.created_at

        description = self.description

        id = str(self.id)

        knowledge_base_count = self.knowledge_base_count

        memory_bank_count = self.memory_bank_count

        name = self.name

        source_connection_count = self.source_connection_count

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_count": agent_count,
                "created_at": created_at,
                "description": description,
                "id": id,
                "knowledge_base_count": knowledge_base_count,
                "memory_bank_count": memory_bank_count,
                "name": name,
                "source_connection_count": source_connection_count,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_count = d.pop("agent_count")

        created_at = d.pop("created_at")

        description = d.pop("description")

        id = UUID(d.pop("id"))

        knowledge_base_count = d.pop("knowledge_base_count")

        memory_bank_count = d.pop("memory_bank_count")

        name = d.pop("name")

        source_connection_count = d.pop("source_connection_count")

        updated_at = d.pop("updated_at")

        solution_summary_response = cls(
            agent_count=agent_count,
            created_at=created_at,
            description=description,
            id=id,
            knowledge_base_count=knowledge_base_count,
            memory_bank_count=memory_bank_count,
            name=name,
            source_connection_count=source_connection_count,
            updated_at=updated_at,
        )

        solution_summary_response.additional_properties = d
        return solution_summary_response

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
