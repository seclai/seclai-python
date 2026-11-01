from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accepted_attachment_slot import AcceptedAttachmentSlot
    from ..models.create_agent_request_agent_definition_type_0 import (
        CreateAgentRequestAgentDefinitionType0,
    )
    from ..models.create_agent_request_entity_remap_type_0 import (
        CreateAgentRequestEntityRemapType0,
    )
    from ..models.create_agent_request_resource_bindings_type_0 import (
        CreateAgentRequestResourceBindingsType0,
    )


T = TypeVar("T", bound="CreateAgentRequest")


@_attrs_define
class CreateAgentRequest:
    """
    Attributes:
        name (str): Name for the new agent.
        accepted_attachments (list[AcceptedAttachmentSlot] | None | Unset): The input attachments the trigger accepts.
            Omitted, the ``agent_definition`` trigger's declaration is kept when the export carries one and both trigger
            types take files; otherwise a dynamic_input or email_received trigger accepts any files (one attachment named
            ``files``), and any other trigger none.
        agent_definition (CreateAgentRequestAgentDefinitionType0 | None | Unset): Optional payload in the same format
            produced by GET /agents/{id}/export. When provided, replaces any template-derived workflow and pre-fills
            metadata/trigger fields the request does not specify explicitly. Validation errors include line/column
            references against a canonical pretty-printed echo of the supplied payload.
        agent_template (None | str | Unset): Agent gallery entry to start from: a `key` from GET /agents/examples, or
            `blank`. The keys retrieval_example and simple_qa remain accepted for their gallery entries.
        create_missing_resources (bool | Unset): For an `agent_template`: create each creatable resource slot left out
            of `resource_bindings`, and group the agent with them in a new solution. When false, an unbound slot the
            template needs is an error. Default: False.
        description (None | str | Unset): Optional description.
        entity_remap (CreateAgentRequestEntityRemapType0 | None | Unset): Optional UUID-substitution map applied to the
            imported workflow before save. Each key is a source-account UUID (as returned by /agents/preview-import's
            ``unresolved_refs``); each value is the target-account UUID to substitute. Used to relink knowledge bases,
            memory banks, source connections, and sub-agents on cross-account imports.
        resource_bindings (CreateAgentRequestResourceBindingsType0 | None | Unset): For an `agent_template`: the
            existing resource to use for each of the template's resource slots, as {slot: resource_id}. GET /agents/examples
            lists each template's slots.
        trigger_type (None | str | Unset): Defaults to dynamic_input, or to the template's own trigger type for an
            `agent_template` without `agent_definition`.
    """

    name: str
    accepted_attachments: list[AcceptedAttachmentSlot] | None | Unset = UNSET
    agent_definition: CreateAgentRequestAgentDefinitionType0 | None | Unset = UNSET
    agent_template: None | str | Unset = UNSET
    create_missing_resources: bool | Unset = False
    description: None | str | Unset = UNSET
    entity_remap: CreateAgentRequestEntityRemapType0 | None | Unset = UNSET
    resource_bindings: CreateAgentRequestResourceBindingsType0 | None | Unset = UNSET
    trigger_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_request_agent_definition_type_0 import (
            CreateAgentRequestAgentDefinitionType0,
        )
        from ..models.create_agent_request_entity_remap_type_0 import (
            CreateAgentRequestEntityRemapType0,
        )
        from ..models.create_agent_request_resource_bindings_type_0 import (
            CreateAgentRequestResourceBindingsType0,
        )

        name = self.name

        accepted_attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.accepted_attachments, Unset):
            accepted_attachments = UNSET
        elif isinstance(self.accepted_attachments, list):
            accepted_attachments = []
            for accepted_attachments_type_0_item_data in self.accepted_attachments:
                accepted_attachments_type_0_item = (
                    accepted_attachments_type_0_item_data.to_dict()
                )
                accepted_attachments.append(accepted_attachments_type_0_item)

        else:
            accepted_attachments = self.accepted_attachments

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

        create_missing_resources = self.create_missing_resources

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

        resource_bindings: dict[str, Any] | None | Unset
        if isinstance(self.resource_bindings, Unset):
            resource_bindings = UNSET
        elif isinstance(
            self.resource_bindings, CreateAgentRequestResourceBindingsType0
        ):
            resource_bindings = self.resource_bindings.to_dict()
        else:
            resource_bindings = self.resource_bindings

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if accepted_attachments is not UNSET:
            field_dict["accepted_attachments"] = accepted_attachments
        if agent_definition is not UNSET:
            field_dict["agent_definition"] = agent_definition
        if agent_template is not UNSET:
            field_dict["agent_template"] = agent_template
        if create_missing_resources is not UNSET:
            field_dict["create_missing_resources"] = create_missing_resources
        if description is not UNSET:
            field_dict["description"] = description
        if entity_remap is not UNSET:
            field_dict["entity_remap"] = entity_remap
        if resource_bindings is not UNSET:
            field_dict["resource_bindings"] = resource_bindings
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accepted_attachment_slot import AcceptedAttachmentSlot
        from ..models.create_agent_request_agent_definition_type_0 import (
            CreateAgentRequestAgentDefinitionType0,
        )
        from ..models.create_agent_request_entity_remap_type_0 import (
            CreateAgentRequestEntityRemapType0,
        )
        from ..models.create_agent_request_resource_bindings_type_0 import (
            CreateAgentRequestResourceBindingsType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_accepted_attachments(
            data: object,
        ) -> list[AcceptedAttachmentSlot] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accepted_attachments_type_0 = []
                _accepted_attachments_type_0 = data
                for (
                    accepted_attachments_type_0_item_data
                ) in _accepted_attachments_type_0:
                    accepted_attachments_type_0_item = AcceptedAttachmentSlot.from_dict(
                        accepted_attachments_type_0_item_data
                    )

                    accepted_attachments_type_0.append(accepted_attachments_type_0_item)

                return accepted_attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AcceptedAttachmentSlot] | None | Unset, data)

        accepted_attachments = _parse_accepted_attachments(
            d.pop("accepted_attachments", UNSET)
        )

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

        create_missing_resources = d.pop("create_missing_resources", UNSET)

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

        def _parse_resource_bindings(
            data: object,
        ) -> CreateAgentRequestResourceBindingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resource_bindings_type_0 = (
                    CreateAgentRequestResourceBindingsType0.from_dict(data)
                )

                return resource_bindings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAgentRequestResourceBindingsType0 | None | Unset, data)

        resource_bindings = _parse_resource_bindings(d.pop("resource_bindings", UNSET))

        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        create_agent_request = cls(
            name=name,
            accepted_attachments=accepted_attachments,
            agent_definition=agent_definition,
            agent_template=agent_template,
            create_missing_resources=create_missing_resources,
            description=description,
            entity_remap=entity_remap,
            resource_bindings=resource_bindings,
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
