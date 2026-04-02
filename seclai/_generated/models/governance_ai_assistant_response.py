from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_prompt import ExamplePrompt
    from ..models.proposed_policy_action_response import ProposedPolicyActionResponse


T = TypeVar("T", bound="GovernanceAiAssistantResponse")


@_attrs_define
class GovernanceAiAssistantResponse:
    """Response from the governance AI assistant generate endpoint.

    Attributes:
        conversation_id (str): Conversation ID to accept or decline this plan.
        note (str): AI-generated summary of the proposed changes.
        proposed_actions (list[ProposedPolicyActionResponse]): Ordered list of policy actions the AI proposes to
            execute.
        success (bool): Whether the plan was generated successfully.
        example_prompts (list[ExamplePrompt] | Unset): Example natural-language prompts that demonstrate the
            capabilities of the governance AI assistant.
        prompt_call_id (None | str | Unset): Prompt call ID for credit tracking, or null.
    """

    conversation_id: str
    note: str
    proposed_actions: list[ProposedPolicyActionResponse]
    success: bool
    example_prompts: list[ExamplePrompt] | Unset = UNSET
    prompt_call_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        note = self.note

        proposed_actions = []
        for proposed_actions_item_data in self.proposed_actions:
            proposed_actions_item = proposed_actions_item_data.to_dict()
            proposed_actions.append(proposed_actions_item)

        success = self.success

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "note": note,
                "proposed_actions": proposed_actions,
                "success": success,
            }
        )
        if example_prompts is not UNSET:
            field_dict["example_prompts"] = example_prompts
        if prompt_call_id is not UNSET:
            field_dict["prompt_call_id"] = prompt_call_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_prompt import ExamplePrompt
        from ..models.proposed_policy_action_response import (
            ProposedPolicyActionResponse,
        )

        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        note = d.pop("note")

        proposed_actions = []
        _proposed_actions = d.pop("proposed_actions")
        for proposed_actions_item_data in _proposed_actions:
            proposed_actions_item = ProposedPolicyActionResponse.from_dict(
                proposed_actions_item_data
            )

            proposed_actions.append(proposed_actions_item)

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

        def _parse_prompt_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_call_id = _parse_prompt_call_id(d.pop("prompt_call_id", UNSET))

        governance_ai_assistant_response = cls(
            conversation_id=conversation_id,
            note=note,
            proposed_actions=proposed_actions,
            success=success,
            example_prompts=example_prompts,
            prompt_call_id=prompt_call_id,
        )

        governance_ai_assistant_response.additional_properties = d
        return governance_ai_assistant_response

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
