from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_prompt import ExamplePrompt
    from ..models.generate_step_config_response_resulting_config_type_0 import (
        GenerateStepConfigResponseResultingConfigType0,
    )


T = TypeVar("T", bound="GenerateStepConfigResponse")


@_attrs_define
class GenerateStepConfigResponse:
    """
    Attributes:
        conversation_id (str): Conversation turn ID for tracking.
        note (str): AI explanation of the proposed configuration.
        step_type (str): The step type that was generated.
        success (bool): Whether a valid configuration was generated.
        example_prompts (list[ExamplePrompt] | Unset): Example natural-language prompts that demonstrate the
            capabilities of this AI assistant for the given step type.
        resulting_config (GenerateStepConfigResponseResultingConfigType0 | None | Unset): The proposed step
            configuration.
    """

    conversation_id: str
    note: str
    step_type: str
    success: bool
    example_prompts: list[ExamplePrompt] | Unset = UNSET
    resulting_config: GenerateStepConfigResponseResultingConfigType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_step_config_response_resulting_config_type_0 import (
            GenerateStepConfigResponseResultingConfigType0,
        )

        conversation_id = self.conversation_id

        note = self.note

        step_type = self.step_type

        success = self.success

        example_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.example_prompts, Unset):
            example_prompts = []
            for example_prompts_item_data in self.example_prompts:
                example_prompts_item = example_prompts_item_data.to_dict()
                example_prompts.append(example_prompts_item)

        resulting_config: dict[str, Any] | None | Unset
        if isinstance(self.resulting_config, Unset):
            resulting_config = UNSET
        elif isinstance(
            self.resulting_config, GenerateStepConfigResponseResultingConfigType0
        ):
            resulting_config = self.resulting_config.to_dict()
        else:
            resulting_config = self.resulting_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "note": note,
                "step_type": step_type,
                "success": success,
            }
        )
        if example_prompts is not UNSET:
            field_dict["example_prompts"] = example_prompts
        if resulting_config is not UNSET:
            field_dict["resulting_config"] = resulting_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_prompt import ExamplePrompt
        from ..models.generate_step_config_response_resulting_config_type_0 import (
            GenerateStepConfigResponseResultingConfigType0,
        )

        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        note = d.pop("note")

        step_type = d.pop("step_type")

        success = d.pop("success")

        _example_prompts = d.pop("example_prompts", UNSET)
        example_prompts: list[ExamplePrompt] | Unset = UNSET
        if _example_prompts is not UNSET:
            example_prompts = []
            for example_prompts_item_data in _example_prompts:
                example_prompts_item = ExamplePrompt.from_dict(
                    example_prompts_item_data
                )

                example_prompts.append(example_prompts_item)

        def _parse_resulting_config(
            data: object,
        ) -> GenerateStepConfigResponseResultingConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resulting_config_type_0 = (
                    GenerateStepConfigResponseResultingConfigType0.from_dict(data)
                )

                return resulting_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GenerateStepConfigResponseResultingConfigType0 | None | Unset, data
            )

        resulting_config = _parse_resulting_config(d.pop("resulting_config", UNSET))

        generate_step_config_response = cls(
            conversation_id=conversation_id,
            note=note,
            step_type=step_type,
            success=success,
            example_prompts=example_prompts,
            resulting_config=resulting_config,
        )

        generate_step_config_response.additional_properties = d
        return generate_step_config_response

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
