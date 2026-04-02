from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAgentRequest")


@_attrs_define
class CreateAgentRequest:
    """
    Attributes:
        name (str): Name for the new agent.
        agent_template (None | str | Unset): Template to initialize the agent from. Values: blank, retrieval_example,
            simple_qa, summarizer, json_extractor, content_change_notifier, scheduled_report, webhook_pipeline.
        description (None | str | Unset): Optional description.
        trigger_type (str | Unset): Trigger type: dynamic_input, template_input, schedule, new_content. Default:
            'dynamic_input'.
    """

    name: str
    agent_template: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    trigger_type: str | Unset = "dynamic_input"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        trigger_type = d.pop("trigger_type", UNSET)

        create_agent_request = cls(
            name=name,
            agent_template=agent_template,
            description=description,
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
