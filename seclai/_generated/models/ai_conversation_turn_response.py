from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ai_conversation_turn_response_resulting_config_type_0 import (
        AiConversationTurnResponseResultingConfigType0,
    )


T = TypeVar("T", bound="AiConversationTurnResponse")


@_attrs_define
class AiConversationTurnResponse:
    """
    Attributes:
        accepted (bool | None): Whether the user accepted this proposal (null if pending).
        ai_note (None | str): AI explanation from this turn.
        conversation_id (str): Unique conversation turn ID.
        resulting_config (AiConversationTurnResponseResultingConfigType0 | None): The proposed configuration from this
            turn.
        step_id (None | str): Step ID for this conversation.
        step_type (None | str): Step type for this conversation.
        user_input (str): User input for this turn.
    """

    accepted: bool | None
    ai_note: None | str
    conversation_id: str
    resulting_config: AiConversationTurnResponseResultingConfigType0 | None
    step_id: None | str
    step_type: None | str
    user_input: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_conversation_turn_response_resulting_config_type_0 import (
            AiConversationTurnResponseResultingConfigType0,
        )

        accepted: bool | None
        accepted = self.accepted

        ai_note: None | str
        ai_note = self.ai_note

        conversation_id = self.conversation_id

        resulting_config: dict[str, Any] | None
        if isinstance(
            self.resulting_config, AiConversationTurnResponseResultingConfigType0
        ):
            resulting_config = self.resulting_config.to_dict()
        else:
            resulting_config = self.resulting_config

        step_id: None | str
        step_id = self.step_id

        step_type: None | str
        step_type = self.step_type

        user_input = self.user_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "ai_note": ai_note,
                "conversation_id": conversation_id,
                "resulting_config": resulting_config,
                "step_id": step_id,
                "step_type": step_type,
                "user_input": user_input,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_conversation_turn_response_resulting_config_type_0 import (
            AiConversationTurnResponseResultingConfigType0,
        )

        d = dict(src_dict)

        def _parse_accepted(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        accepted = _parse_accepted(d.pop("accepted"))

        def _parse_ai_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ai_note = _parse_ai_note(d.pop("ai_note"))

        conversation_id = d.pop("conversation_id")

        def _parse_resulting_config(
            data: object,
        ) -> AiConversationTurnResponseResultingConfigType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resulting_config_type_0 = (
                    AiConversationTurnResponseResultingConfigType0.from_dict(data)
                )

                return resulting_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AiConversationTurnResponseResultingConfigType0 | None, data)

        resulting_config = _parse_resulting_config(d.pop("resulting_config"))

        def _parse_step_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        step_id = _parse_step_id(d.pop("step_id"))

        def _parse_step_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        step_type = _parse_step_type(d.pop("step_type"))

        user_input = d.pop("user_input")

        ai_conversation_turn_response = cls(
            accepted=accepted,
            ai_note=ai_note,
            conversation_id=conversation_id,
            resulting_config=resulting_config,
            step_id=step_id,
            step_type=step_type,
            user_input=user_input,
        )

        ai_conversation_turn_response.additional_properties = d
        return ai_conversation_turn_response

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
