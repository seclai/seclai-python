from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_assistant_feedback_request_context_type_0 import (
        AiAssistantFeedbackRequestContextType0,
    )


T = TypeVar("T", bound="AiAssistantFeedbackRequest")


@_attrs_define
class AiAssistantFeedbackRequest:
    """Request body for submitting AI assistant feedback.

    Attributes:
        feature (str): Feature name (e.g. 'source', 'solution').
        rating (str): Rating: 'thumbs_up' or 'thumbs_down'.
        agent_conversation_id (None | Unset | UUID): Agent conversation ID, if applicable.
        comment (None | str | Unset): Optional comment.
        context (AiAssistantFeedbackRequestContextType0 | None | Unset): Additional context.
        conversation_id (None | Unset | UUID): Conversation ID for the interaction.
        prompt_call_id (None | Unset | UUID): Prompt call ID for credit tracking.
    """

    feature: str
    rating: str
    agent_conversation_id: None | Unset | UUID = UNSET
    comment: None | str | Unset = UNSET
    context: AiAssistantFeedbackRequestContextType0 | None | Unset = UNSET
    conversation_id: None | Unset | UUID = UNSET
    prompt_call_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_assistant_feedback_request_context_type_0 import (
            AiAssistantFeedbackRequestContextType0,
        )

        feature = self.feature

        rating = self.rating

        agent_conversation_id: None | str | Unset
        if isinstance(self.agent_conversation_id, Unset):
            agent_conversation_id = UNSET
        elif isinstance(self.agent_conversation_id, UUID):
            agent_conversation_id = str(self.agent_conversation_id)
        else:
            agent_conversation_id = self.agent_conversation_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, AiAssistantFeedbackRequestContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        elif isinstance(self.conversation_id, UUID):
            conversation_id = str(self.conversation_id)
        else:
            conversation_id = self.conversation_id

        prompt_call_id: None | str | Unset
        if isinstance(self.prompt_call_id, Unset):
            prompt_call_id = UNSET
        elif isinstance(self.prompt_call_id, UUID):
            prompt_call_id = str(self.prompt_call_id)
        else:
            prompt_call_id = self.prompt_call_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature": feature,
                "rating": rating,
            }
        )
        if agent_conversation_id is not UNSET:
            field_dict["agent_conversation_id"] = agent_conversation_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if context is not UNSET:
            field_dict["context"] = context
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if prompt_call_id is not UNSET:
            field_dict["prompt_call_id"] = prompt_call_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_assistant_feedback_request_context_type_0 import (
            AiAssistantFeedbackRequestContextType0,
        )

        d = dict(src_dict)
        feature = d.pop("feature")

        rating = d.pop("rating")

        def _parse_agent_conversation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_conversation_id_type_0 = UUID(data)

                return agent_conversation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_conversation_id = _parse_agent_conversation_id(
            d.pop("agent_conversation_id", UNSET)
        )

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_context(
            data: object,
        ) -> AiAssistantFeedbackRequestContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = AiAssistantFeedbackRequestContextType0.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AiAssistantFeedbackRequestContextType0 | None | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        def _parse_conversation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conversation_id_type_0 = UUID(data)

                return conversation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        conversation_id = _parse_conversation_id(d.pop("conversation_id", UNSET))

        def _parse_prompt_call_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prompt_call_id_type_0 = UUID(data)

                return prompt_call_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        prompt_call_id = _parse_prompt_call_id(d.pop("prompt_call_id", UNSET))

        ai_assistant_feedback_request = cls(
            feature=feature,
            rating=rating,
            agent_conversation_id=agent_conversation_id,
            comment=comment,
            context=context,
            conversation_id=conversation_id,
            prompt_call_id=prompt_call_id,
        )

        ai_assistant_feedback_request.additional_properties = d
        return ai_assistant_feedback_request

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
