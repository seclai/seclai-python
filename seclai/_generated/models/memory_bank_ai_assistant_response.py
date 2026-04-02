from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_prompt import ExamplePrompt
    from ..models.memory_bank_config_response import MemoryBankConfigResponse


T = TypeVar("T", bound="MemoryBankAiAssistantResponse")


@_attrs_define
class MemoryBankAiAssistantResponse:
    """Response from the memory bank AI assistant.

    Attributes:
        conversation_id (str): Conversation ID for follow-up.
        note (str): AI-generated explanation.
        config (MemoryBankConfigResponse | None | Unset): Proposed configuration, or null.
        example_prompts (list[ExamplePrompt] | Unset): Example natural-language prompts that demonstrate the
            capabilities of the memory bank AI assistant.
        prompt_call_id (None | str | Unset): Prompt call ID for credit tracking.
        success (bool | Unset): Whether generation succeeded. Default: False.
    """

    conversation_id: str
    note: str
    config: MemoryBankConfigResponse | None | Unset = UNSET
    example_prompts: list[ExamplePrompt] | Unset = UNSET
    prompt_call_id: None | str | Unset = UNSET
    success: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_bank_config_response import MemoryBankConfigResponse

        conversation_id = self.conversation_id

        note = self.note

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, MemoryBankConfigResponse):
            config = self.config.to_dict()
        else:
            config = self.config

        example_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.example_prompts, Unset):
            example_prompts = []
            for example_prompts_item_data in self.example_prompts:
                example_prompts_item = example_prompts_item_data.to_dict()
                example_prompts.append(example_prompts_item)

        prompt_call_id: None | str | Unset
        if isinstance(self.prompt_call_id, Unset):
            prompt_call_id = UNSET
        else:
            prompt_call_id = self.prompt_call_id

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "note": note,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if example_prompts is not UNSET:
            field_dict["example_prompts"] = example_prompts
        if prompt_call_id is not UNSET:
            field_dict["prompt_call_id"] = prompt_call_id
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_prompt import ExamplePrompt
        from ..models.memory_bank_config_response import MemoryBankConfigResponse

        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        note = d.pop("note")

        def _parse_config(data: object) -> MemoryBankConfigResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = MemoryBankConfigResponse.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryBankConfigResponse | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        _example_prompts = d.pop("example_prompts", UNSET)
        example_prompts: list[ExamplePrompt] | Unset = UNSET
        if _example_prompts is not UNSET:
            example_prompts = []
            for example_prompts_item_data in _example_prompts:
                example_prompts_item = ExamplePrompt.from_dict(
                    example_prompts_item_data
                )

                example_prompts.append(example_prompts_item)

        def _parse_prompt_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_call_id = _parse_prompt_call_id(d.pop("prompt_call_id", UNSET))

        success = d.pop("success", UNSET)

        memory_bank_ai_assistant_response = cls(
            conversation_id=conversation_id,
            note=note,
            config=config,
            example_prompts=example_prompts,
            prompt_call_id=prompt_call_id,
            success=success,
        )

        memory_bank_ai_assistant_response.additional_properties = d
        return memory_bank_ai_assistant_response

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
