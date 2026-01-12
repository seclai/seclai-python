from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_trigger_type import AgentTriggerType

if TYPE_CHECKING:
    from ..models.trigger_response_metadata_type_0 import TriggerResponseMetadataType0


T = TypeVar("T", bound="TriggerResponse")


@_attrs_define
class TriggerResponse:
    """Response model for agent trigger data

    Attributes:
        agent_id (UUID):
        branch_id (None | UUID):
        commit_id (None | UUID):
        created_at (str):
        id (UUID):
        input_ (None | str):
        knowledge_base_id (None | UUID):
        metadata (None | TriggerResponseMetadataType0):
        name (None | str):
        trigger_type (AgentTriggerType):
        updated_at (str):
    """

    agent_id: UUID
    branch_id: None | UUID
    commit_id: None | UUID
    created_at: str
    id: UUID
    input_: None | str
    knowledge_base_id: None | UUID
    metadata: None | TriggerResponseMetadataType0
    name: None | str
    trigger_type: AgentTriggerType
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trigger_response_metadata_type_0 import (
            TriggerResponseMetadataType0,
        )

        agent_id = str(self.agent_id)

        branch_id: None | str
        if isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        commit_id: None | str
        if isinstance(self.commit_id, UUID):
            commit_id = str(self.commit_id)
        else:
            commit_id = self.commit_id

        created_at = self.created_at

        id = str(self.id)

        input_: None | str
        input_ = self.input_

        knowledge_base_id: None | str
        if isinstance(self.knowledge_base_id, UUID):
            knowledge_base_id = str(self.knowledge_base_id)
        else:
            knowledge_base_id = self.knowledge_base_id

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, TriggerResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        name: None | str
        name = self.name

        trigger_type = self.trigger_type.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "branch_id": branch_id,
                "commit_id": commit_id,
                "created_at": created_at,
                "id": id,
                "input": input_,
                "knowledge_base_id": knowledge_base_id,
                "metadata_": metadata,
                "name": name,
                "trigger_type": trigger_type,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_response_metadata_type_0 import (
            TriggerResponseMetadataType0,
        )

        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        def _parse_branch_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)

                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id"))

        def _parse_commit_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                commit_id_type_0 = UUID(data)

                return commit_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        commit_id = _parse_commit_id(d.pop("commit_id"))

        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        def _parse_input_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_knowledge_base_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_base_id_type_0 = UUID(data)

                return knowledge_base_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        knowledge_base_id = _parse_knowledge_base_id(d.pop("knowledge_base_id"))

        def _parse_metadata(data: object) -> None | TriggerResponseMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TriggerResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerResponseMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata_"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        trigger_type = AgentTriggerType(d.pop("trigger_type"))

        updated_at = d.pop("updated_at")

        trigger_response = cls(
            agent_id=agent_id,
            branch_id=branch_id,
            commit_id=commit_id,
            created_at=created_at,
            id=id,
            input_=input_,
            knowledge_base_id=knowledge_base_id,
            metadata=metadata,
            name=name,
            trigger_type=trigger_type,
            updated_at=updated_at,
        )

        trigger_response.additional_properties = d
        return trigger_response

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
