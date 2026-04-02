from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_prompt import ExamplePrompt
    from ..models.generate_agent_steps_response_agent_config_type_0 import (
        GenerateAgentStepsResponseAgentConfigType0,
    )
    from ..models.generate_agent_steps_response_steps_item import (
        GenerateAgentStepsResponseStepsItem,
    )


T = TypeVar("T", bound="GenerateAgentStepsResponse")


@_attrs_define
class GenerateAgentStepsResponse:
    """
    Attributes:
        conversation_id (str): Conversation turn ID for tracking.
        note (str): AI explanation of the proposed workflow.
        steps (list[GenerateAgentStepsResponseStepsItem]): Generated agent steps.
        success (bool): Whether steps were successfully generated.
        agent_config (GenerateAgentStepsResponseAgentConfigType0 | None | Unset): Suggested agent-level configuration,
            if any.
        example_prompts (list[ExamplePrompt] | Unset): Example natural-language prompts that demonstrate the
            capabilities of this AI assistant for the given mode.
    """

    conversation_id: str
    note: str
    steps: list[GenerateAgentStepsResponseStepsItem]
    success: bool
    agent_config: GenerateAgentStepsResponseAgentConfigType0 | None | Unset = UNSET
    example_prompts: list[ExamplePrompt] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_agent_steps_response_agent_config_type_0 import (
            GenerateAgentStepsResponseAgentConfigType0,
        )

        conversation_id = self.conversation_id

        note = self.note

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        success = self.success

        agent_config: dict[str, Any] | None | Unset
        if isinstance(self.agent_config, Unset):
            agent_config = UNSET
        elif isinstance(self.agent_config, GenerateAgentStepsResponseAgentConfigType0):
            agent_config = self.agent_config.to_dict()
        else:
            agent_config = self.agent_config

        example_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.example_prompts, Unset):
            example_prompts = []
            for example_prompts_item_data in self.example_prompts:
                example_prompts_item = example_prompts_item_data.to_dict()
                example_prompts.append(example_prompts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "note": note,
                "steps": steps,
                "success": success,
            }
        )
        if agent_config is not UNSET:
            field_dict["agent_config"] = agent_config
        if example_prompts is not UNSET:
            field_dict["example_prompts"] = example_prompts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_prompt import ExamplePrompt
        from ..models.generate_agent_steps_response_agent_config_type_0 import (
            GenerateAgentStepsResponseAgentConfigType0,
        )
        from ..models.generate_agent_steps_response_steps_item import (
            GenerateAgentStepsResponseStepsItem,
        )

        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        note = d.pop("note")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = GenerateAgentStepsResponseStepsItem.from_dict(steps_item_data)

            steps.append(steps_item)

        success = d.pop("success")

        def _parse_agent_config(
            data: object,
        ) -> GenerateAgentStepsResponseAgentConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_config_type_0 = (
                    GenerateAgentStepsResponseAgentConfigType0.from_dict(data)
                )

                return agent_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenerateAgentStepsResponseAgentConfigType0 | None | Unset, data)

        agent_config = _parse_agent_config(d.pop("agent_config", UNSET))

        _example_prompts = d.pop("example_prompts", UNSET)
        example_prompts: list[ExamplePrompt] | Unset = UNSET
        if _example_prompts is not UNSET:
            example_prompts = []
            for example_prompts_item_data in _example_prompts:
                example_prompts_item = ExamplePrompt.from_dict(
                    example_prompts_item_data
                )

                example_prompts.append(example_prompts_item)

        generate_agent_steps_response = cls(
            conversation_id=conversation_id,
            note=note,
            steps=steps,
            success=success,
            agent_config=agent_config,
            example_prompts=example_prompts,
        )

        generate_agent_steps_response.additional_properties = d
        return generate_agent_steps_response

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
