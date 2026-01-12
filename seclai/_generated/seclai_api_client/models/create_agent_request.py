from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_trigger_type import AgentTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_agent_request_metadata_type_0 import (
        CreateAgentRequestMetadataType0,
    )


T = TypeVar("T", bound="CreateAgentRequest")


@_attrs_define
class CreateAgentRequest:
    """Request model for creating/duplicating an agent

    Attributes:
        name (str): Agent name
        agent_template (None | str | Unset): Template to use for initial agent definition: 'blank' or
            'retrieval_example'
        description (None | str | Unset): Optional agent description
        input_ (None | str | Unset): Template input for agents with TEMPLATE_INPUT trigger type
        knowledge_base_id (None | Unset | UUID): Knowledge base to use when creating an initial agent definition
            template. Optional; if omitted, retrieval steps must be configured later.
        metadata (CreateAgentRequestMetadataType0 | None | Unset): Metadata available for string substitutions in the
            agent
        trigger_type (AgentTriggerType | None | Unset): The type of event that triggers this agent (optional for
            duplicate)
    """

    name: str
    agent_template: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    input_: None | str | Unset = UNSET
    knowledge_base_id: None | Unset | UUID = UNSET
    metadata: CreateAgentRequestMetadataType0 | None | Unset = UNSET
    trigger_type: AgentTriggerType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_request_metadata_type_0 import (
            CreateAgentRequestMetadataType0,
        )

        name = self.name

        agent_template: None | str | Unset
        if isinstance(self.agent_template, Unset):
            agent_template = UNSET
        else:
            agent_template = self.agent_template

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        knowledge_base_id: None | str | Unset
        if isinstance(self.knowledge_base_id, Unset):
            knowledge_base_id = UNSET
        elif isinstance(self.knowledge_base_id, UUID):
            knowledge_base_id = str(self.knowledge_base_id)
        else:
            knowledge_base_id = self.knowledge_base_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreateAgentRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        elif isinstance(self.trigger_type, AgentTriggerType):
            trigger_type = self.trigger_type.value
        else:
            trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if agent_template is not UNSET:
            field_dict["agent_template"] = agent_template
        if description is not UNSET:
            field_dict["description"] = description
        if input_ is not UNSET:
            field_dict["input"] = input_
        if knowledge_base_id is not UNSET:
            field_dict["knowledge_base_id"] = knowledge_base_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_agent_request_metadata_type_0 import (
            CreateAgentRequestMetadataType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_agent_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_template = _parse_agent_template(d.pop("agent_template", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_knowledge_base_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_base_id_type_0 = UUID(data)

                return knowledge_base_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        knowledge_base_id = _parse_knowledge_base_id(d.pop("knowledge_base_id", UNSET))

        def _parse_metadata(
            data: object,
        ) -> CreateAgentRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateAgentRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAgentRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_trigger_type(data: object) -> AgentTriggerType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_type_type_0 = AgentTriggerType(data)

                return trigger_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentTriggerType | None | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        create_agent_request = cls(
            name=name,
            agent_template=agent_template,
            description=description,
            input_=input_,
            knowledge_base_id=knowledge_base_id,
            metadata=metadata,
            trigger_type=trigger_type,
        )

        create_agent_request.additional_properties = d
        return create_agent_request

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
