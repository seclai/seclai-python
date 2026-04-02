from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SolutionKnowledgeBaseResponse")


@_attrs_define
class SolutionKnowledgeBaseResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        source_connection_ids (list[UUID] | Unset): Source connection IDs linked to this knowledge base.
    """

    id: UUID
    name: str
    source_connection_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        source_connection_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_connection_ids, Unset):
            source_connection_ids = []
            for source_connection_ids_item_data in self.source_connection_ids:
                source_connection_ids_item = str(source_connection_ids_item_data)
                source_connection_ids.append(source_connection_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if source_connection_ids is not UNSET:
            field_dict["source_connection_ids"] = source_connection_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        _source_connection_ids = d.pop("source_connection_ids", UNSET)
        source_connection_ids: list[UUID] | Unset = UNSET
        if _source_connection_ids is not UNSET:
            source_connection_ids = []
            for source_connection_ids_item_data in _source_connection_ids:
                source_connection_ids_item = UUID(source_connection_ids_item_data)

                source_connection_ids.append(source_connection_ids_item)

        solution_knowledge_base_response = cls(
            id=id,
            name=name,
            source_connection_ids=source_connection_ids,
        )

        solution_knowledge_base_response.additional_properties = d
        return solution_knowledge_base_response

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
