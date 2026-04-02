from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_agent_steps_request_agent_steps_type_0_item import (
        GenerateAgentStepsRequestAgentStepsType0Item,
    )


T = TypeVar("T", bound="GenerateAgentStepsRequest")


@_attrs_define
class GenerateAgentStepsRequest:
    """
    Attributes:
        user_input (str): Natural language description of the desired agent workflow.
        agent_description (None | str | Unset): Agent description for additional AI context.
        agent_steps (list[GenerateAgentStepsRequestAgentStepsType0Item] | None | Unset): Current agent step hierarchy
            for context when modifying.
        mode (str | Unset): 'generate_full' to create from scratch, 'modify_workflow' to refine. Default:
            'generate_full'.
        trigger_type (None | str | Unset): Agent trigger type for context (e.g. 'dynamic_input', 'content_added').
    """

    user_input: str
    agent_description: None | str | Unset = UNSET
    agent_steps: list[GenerateAgentStepsRequestAgentStepsType0Item] | None | Unset = (
        UNSET
    )
    mode: str | Unset = "generate_full"
    trigger_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_input = self.user_input

        agent_description: None | str | Unset
        if isinstance(self.agent_description, Unset):
            agent_description = UNSET
        else:
            agent_description = self.agent_description

        agent_steps: list[dict[str, Any]] | None | Unset
        if isinstance(self.agent_steps, Unset):
            agent_steps = UNSET
        elif isinstance(self.agent_steps, list):
            agent_steps = []
            for agent_steps_type_0_item_data in self.agent_steps:
                agent_steps_type_0_item = agent_steps_type_0_item_data.to_dict()
                agent_steps.append(agent_steps_type_0_item)

        else:
            agent_steps = self.agent_steps

        mode = self.mode

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_input": user_input,
            }
        )
        if agent_description is not UNSET:
            field_dict["agent_description"] = agent_description
        if agent_steps is not UNSET:
            field_dict["agent_steps"] = agent_steps
        if mode is not UNSET:
            field_dict["mode"] = mode
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_agent_steps_request_agent_steps_type_0_item import (
            GenerateAgentStepsRequestAgentStepsType0Item,
        )

        d = dict(src_dict)
        user_input = d.pop("user_input")

        def _parse_agent_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_description = _parse_agent_description(d.pop("agent_description", UNSET))

        def _parse_agent_steps(
            data: object,
        ) -> list[GenerateAgentStepsRequestAgentStepsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_steps_type_0 = []
                _agent_steps_type_0 = data
                for agent_steps_type_0_item_data in _agent_steps_type_0:
                    agent_steps_type_0_item = (
                        GenerateAgentStepsRequestAgentStepsType0Item.from_dict(
                            agent_steps_type_0_item_data
                        )
                    )

                    agent_steps_type_0.append(agent_steps_type_0_item)

                return agent_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[GenerateAgentStepsRequestAgentStepsType0Item] | None | Unset, data
            )

        agent_steps = _parse_agent_steps(d.pop("agent_steps", UNSET))

        mode = d.pop("mode", UNSET)

        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        generate_agent_steps_request = cls(
            user_input=user_input,
            agent_description=agent_description,
            agent_steps=agent_steps,
            mode=mode,
            trigger_type=trigger_type,
        )

        generate_agent_steps_request.additional_properties = d
        return generate_agent_steps_request

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
