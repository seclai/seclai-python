from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_step_config_request_agent_steps_type_0_item import (
        GenerateStepConfigRequestAgentStepsType0Item,
    )
    from ..models.generate_step_config_request_current_config_type_0 import (
        GenerateStepConfigRequestCurrentConfigType0,
    )


T = TypeVar("T", bound="GenerateStepConfigRequest")


@_attrs_define
class GenerateStepConfigRequest:
    """
    Attributes:
        step_type (str): The step type to generate config for (e.g. 'transform', 'gate', 'text', 'prompt_call',
            'retrieval').
        user_input (str): Natural language description of what the step should do.
        agent_steps (list[GenerateStepConfigRequestAgentStepsType0Item] | None | Unset): Current agent step hierarchy
            for context.
        current_config (GenerateStepConfigRequestCurrentConfigType0 | None | Unset): Current step configuration to
            refine, if any.
        step_id (None | str | Unset): ID of the specific step to refine. Omit for new steps.
    """

    step_type: str
    user_input: str
    agent_steps: list[GenerateStepConfigRequestAgentStepsType0Item] | None | Unset = (
        UNSET
    )
    current_config: GenerateStepConfigRequestCurrentConfigType0 | None | Unset = UNSET
    step_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_step_config_request_current_config_type_0 import (
            GenerateStepConfigRequestCurrentConfigType0,
        )

        step_type = self.step_type

        user_input = self.user_input

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

        current_config: dict[str, Any] | None | Unset
        if isinstance(self.current_config, Unset):
            current_config = UNSET
        elif isinstance(
            self.current_config, GenerateStepConfigRequestCurrentConfigType0
        ):
            current_config = self.current_config.to_dict()
        else:
            current_config = self.current_config

        step_id: None | str | Unset
        if isinstance(self.step_id, Unset):
            step_id = UNSET
        else:
            step_id = self.step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_type": step_type,
                "user_input": user_input,
            }
        )
        if agent_steps is not UNSET:
            field_dict["agent_steps"] = agent_steps
        if current_config is not UNSET:
            field_dict["current_config"] = current_config
        if step_id is not UNSET:
            field_dict["step_id"] = step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_step_config_request_agent_steps_type_0_item import (
            GenerateStepConfigRequestAgentStepsType0Item,
        )
        from ..models.generate_step_config_request_current_config_type_0 import (
            GenerateStepConfigRequestCurrentConfigType0,
        )

        d = dict(src_dict)
        step_type = d.pop("step_type")

        user_input = d.pop("user_input")

        def _parse_agent_steps(
            data: object,
        ) -> list[GenerateStepConfigRequestAgentStepsType0Item] | None | Unset:
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
                        GenerateStepConfigRequestAgentStepsType0Item.from_dict(
                            agent_steps_type_0_item_data
                        )
                    )

                    agent_steps_type_0.append(agent_steps_type_0_item)

                return agent_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[GenerateStepConfigRequestAgentStepsType0Item] | None | Unset, data
            )

        agent_steps = _parse_agent_steps(d.pop("agent_steps", UNSET))

        def _parse_current_config(
            data: object,
        ) -> GenerateStepConfigRequestCurrentConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_config_type_0 = (
                    GenerateStepConfigRequestCurrentConfigType0.from_dict(data)
                )

                return current_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GenerateStepConfigRequestCurrentConfigType0 | None | Unset, data
            )

        current_config = _parse_current_config(d.pop("current_config", UNSET))

        def _parse_step_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_id = _parse_step_id(d.pop("step_id", UNSET))

        generate_step_config_request = cls(
            step_type=step_type,
            user_input=user_input,
            agent_steps=agent_steps,
            current_config=current_config,
            step_id=step_id,
        )

        generate_step_config_request.additional_properties = d
        return generate_step_config_request

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
