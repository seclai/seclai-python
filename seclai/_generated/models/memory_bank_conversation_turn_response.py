from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_bank_conversation_turn_response_resulting_config_type_0 import (
        MemoryBankConversationTurnResponseResultingConfigType0,
    )


T = TypeVar("T", bound="MemoryBankConversationTurnResponse")


@_attrs_define
class MemoryBankConversationTurnResponse:
    """A single turn of memory bank AI assistant conversation.

    Attributes:
        conversation_id (str): Unique ID for this conversation turn.
        user_input (str): User input for this turn.
        accepted (bool | None | Unset): Whether the user accepted this proposal.
        ai_note (None | str | Unset): AI note from this turn.
        resulting_config (MemoryBankConversationTurnResponseResultingConfigType0 | None | Unset): The proposed
            configuration from this turn.
    """

    conversation_id: str
    user_input: str
    accepted: bool | None | Unset = UNSET
    ai_note: None | str | Unset = UNSET
    resulting_config: (
        MemoryBankConversationTurnResponseResultingConfigType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_bank_conversation_turn_response_resulting_config_type_0 import (
            MemoryBankConversationTurnResponseResultingConfigType0,
        )

        conversation_id = self.conversation_id

        user_input = self.user_input

        accepted: bool | None | Unset
        if isinstance(self.accepted, Unset):
            accepted = UNSET
        else:
            accepted = self.accepted

        ai_note: None | str | Unset
        if isinstance(self.ai_note, Unset):
            ai_note = UNSET
        else:
            ai_note = self.ai_note

        resulting_config: dict[str, Any] | None | Unset
        if isinstance(self.resulting_config, Unset):
            resulting_config = UNSET
        elif isinstance(
            self.resulting_config,
            MemoryBankConversationTurnResponseResultingConfigType0,
        ):
            resulting_config = self.resulting_config.to_dict()
        else:
            resulting_config = self.resulting_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "user_input": user_input,
            }
        )
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if ai_note is not UNSET:
            field_dict["ai_note"] = ai_note
        if resulting_config is not UNSET:
            field_dict["resulting_config"] = resulting_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_bank_conversation_turn_response_resulting_config_type_0 import (
            MemoryBankConversationTurnResponseResultingConfigType0,
        )

        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        user_input = d.pop("user_input")

        def _parse_accepted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        accepted = _parse_accepted(d.pop("accepted", UNSET))

        def _parse_ai_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_note = _parse_ai_note(d.pop("ai_note", UNSET))

        def _parse_resulting_config(
            data: object,
        ) -> MemoryBankConversationTurnResponseResultingConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resulting_config_type_0 = (
                    MemoryBankConversationTurnResponseResultingConfigType0.from_dict(
                        data
                    )
                )

                return resulting_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MemoryBankConversationTurnResponseResultingConfigType0 | None | Unset,
                data,
            )

        resulting_config = _parse_resulting_config(d.pop("resulting_config", UNSET))

        memory_bank_conversation_turn_response = cls(
            conversation_id=conversation_id,
            user_input=user_input,
            accepted=accepted,
            ai_note=ai_note,
            resulting_config=resulting_config,
        )

        memory_bank_conversation_turn_response.additional_properties = d
        return memory_bank_conversation_turn_response

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
