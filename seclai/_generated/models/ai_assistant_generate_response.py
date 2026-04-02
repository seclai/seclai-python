from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_prompt import ExamplePrompt
    from ..models.proposed_action_response import ProposedActionResponse


T = TypeVar("T", bound="AiAssistantGenerateResponse")


@_attrs_define
class AiAssistantGenerateResponse:
    """Response from an AI assistant generate endpoint.

    Attributes:
        conversation_id (UUID): Conversation ID for accept/decline.
        note (str): AI-generated note about the plan.
        proposed_actions (list[ProposedActionResponse]): List of proposed actions.
        example_prompts (list[ExamplePrompt] | Unset): Example natural-language prompts that demonstrate the
            capabilities of this AI assistant.
        requires_delete_confirmation (bool | Unset): Whether destructive actions require explicit confirmation. Default:
            False.
        success (bool | Unset): Whether plan generation succeeded. Default: False.
    """

    conversation_id: UUID
    note: str
    proposed_actions: list[ProposedActionResponse]
    example_prompts: list[ExamplePrompt] | Unset = UNSET
    requires_delete_confirmation: bool | Unset = False
    success: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = str(self.conversation_id)

        note = self.note

        proposed_actions = []
        for proposed_actions_item_data in self.proposed_actions:
            proposed_actions_item = proposed_actions_item_data.to_dict()
            proposed_actions.append(proposed_actions_item)

        example_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.example_prompts, Unset):
            example_prompts = []
            for example_prompts_item_data in self.example_prompts:
                example_prompts_item = example_prompts_item_data.to_dict()
                example_prompts.append(example_prompts_item)

        requires_delete_confirmation = self.requires_delete_confirmation

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "note": note,
                "proposed_actions": proposed_actions,
            }
        )
        if example_prompts is not UNSET:
            field_dict["example_prompts"] = example_prompts
        if requires_delete_confirmation is not UNSET:
            field_dict["requires_delete_confirmation"] = requires_delete_confirmation
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_prompt import ExamplePrompt
        from ..models.proposed_action_response import ProposedActionResponse

        d = dict(src_dict)
        conversation_id = UUID(d.pop("conversation_id"))

        note = d.pop("note")

        proposed_actions = []
        _proposed_actions = d.pop("proposed_actions")
        for proposed_actions_item_data in _proposed_actions:
            proposed_actions_item = ProposedActionResponse.from_dict(
                proposed_actions_item_data
            )

            proposed_actions.append(proposed_actions_item)

        _example_prompts = d.pop("example_prompts", UNSET)
        example_prompts: list[ExamplePrompt] | Unset = UNSET
        if _example_prompts is not UNSET:
            example_prompts = []
            for example_prompts_item_data in _example_prompts:
                example_prompts_item = ExamplePrompt.from_dict(
                    example_prompts_item_data
                )

                example_prompts.append(example_prompts_item)

        requires_delete_confirmation = d.pop("requires_delete_confirmation", UNSET)

        success = d.pop("success", UNSET)

        ai_assistant_generate_response = cls(
            conversation_id=conversation_id,
            note=note,
            proposed_actions=proposed_actions,
            example_prompts=example_prompts,
            requires_delete_confirmation=requires_delete_confirmation,
            success=success,
        )

        ai_assistant_generate_response.additional_properties = d
        return ai_assistant_generate_response

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
