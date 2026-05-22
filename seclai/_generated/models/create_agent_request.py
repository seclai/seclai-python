from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_agent_request_agent_definition_type_0 import (
        CreateAgentRequestAgentDefinitionType0,
    )
    from ..models.create_agent_request_entity_remap_type_0 import (
        CreateAgentRequestEntityRemapType0,
    )


T = TypeVar("T", bound="CreateAgentRequest")


@_attrs_define
class CreateAgentRequest:
    """
    Attributes:
        name (str): Name for the new agent.
        agent_definition (CreateAgentRequestAgentDefinitionType0 | None | Unset): Optional payload in the same format
            produced by GET /agents/{id}/export. When provided, replaces any template-derived workflow and pre-fills
            metadata/trigger fields the request does not specify explicitly. Validation errors include line/column
            references against a canonical pretty-printed echo of the supplied payload.
        agent_template (None | str | Unset): Template to initialize the agent from. Values: blank, retrieval_example,
            simple_qa, summarizer, json_extractor, content_change_notifier, scheduled_report, webhook_pipeline.
        description (None | str | Unset): Optional description.
        entity_remap (CreateAgentRequestEntityRemapType0 | None | Unset): Optional UUID-substitution map applied to the
            imported workflow before save. Each key is a source-account UUID (as returned by /agents/preview-import's
            ``unresolved_refs``); each value is the target-account UUID to substitute. Used to relink knowledge bases,
            memory banks, source connections, and sub-agents on cross-account imports.
        trigger_type (str | Unset): Trigger type: dynamic_input, template_input, schedule, new_content. Default:
            'dynamic_input'.
    """

    name: str
    agent_definition: CreateAgentRequestAgentDefinitionType0 | None | Unset = UNSET
    agent_template: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    entity_remap: CreateAgentRequestEntityRemapType0 | None | Unset = UNSET
    trigger_type: str | Unset = "dynamic_input"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_request_agent_definition_type_0 import (
            CreateAgentRequestAgentDefinitionType0,
        )
        from ..models.create_agent_request_entity_remap_type_0 import (
            CreateAgentRequestEntityRemapType0,
        )

        name = self.name

        agent_definition: dict[str, Any] | None | Unset
        if isinstance(self.agent_definition, Unset):
            agent_definition = UNSET
        elif isinstance(self.agent_definition, CreateAgentRequestAgentDefinitionType0):
            agent_definition = self.agent_definition.to_dict()
        else:
            agent_definition = self.agent_definition

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

        entity_remap: dict[str, Any] | None | Unset
        if isinstance(self.entity_remap, Unset):
            entity_remap = UNSET
        elif isinstance(self.entity_remap, CreateAgentRequestEntityRemapType0):
            entity_remap = self.entity_remap.to_dict()
        else:
            entity_remap = self.entity_remap

        trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if agent_definition is not UNSET:
            field_dict["agent_definition"] = agent_definition
        if agent_template is not UNSET:
            field_dict["agent_template"] = agent_template
        if description is not UNSET:
            field_dict["description"] = description
        if entity_remap is not UNSET:
            field_dict["entity_remap"] = entity_remap
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_agent_request_agent_definition_type_0 import (
            CreateAgentRequestAgentDefinitionType0,
        )
        from ..models.create_agent_request_entity_remap_type_0 import (
            CreateAgentRequestEntityRemapType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_agent_definition(
            data: object,
        ) -> CreateAgentRequestAgentDefinitionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_definition_type_0 = (
                    CreateAgentRequestAgentDefinitionType0.from_dict(data)
                )

                return agent_definition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAgentRequestAgentDefinitionType0 | None | Unset, data)

        agent_definition = _parse_agent_definition(d.pop("agent_definition", UNSET))

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

        def _parse_entity_remap(
            data: object,
        ) -> CreateAgentRequestEntityRemapType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_remap_type_0 = CreateAgentRequestEntityRemapType0.from_dict(data)

                return entity_remap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAgentRequestEntityRemapType0 | None | Unset, data)

        entity_remap = _parse_entity_remap(d.pop("entity_remap", UNSET))

        trigger_type = d.pop("trigger_type", UNSET)

        create_agent_request = cls(
            name=name,
            agent_definition=agent_definition,
            agent_template=agent_template,
            description=description,
            entity_remap=entity_remap,
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
