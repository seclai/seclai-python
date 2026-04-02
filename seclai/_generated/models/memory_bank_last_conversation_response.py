from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_bank_conversation_turn_response import (
        MemoryBankConversationTurnResponse,
    )


T = TypeVar("T", bound="MemoryBankLastConversationResponse")


@_attrs_define
class MemoryBankLastConversationResponse:
    """Response for fetching memory bank conversation history.

    Attributes:
        accepted (bool | None | Unset): Whether the user accepted the last proposal.
        ai_note (None | str | Unset): AI note from the most recent turn.
        total (int | Unset): Total conversation turns. Default: 0.
        turns (list[MemoryBankConversationTurnResponse] | Unset): Recent conversation turns (oldest first).
        user_input (None | str | Unset): Most recent user input.
    """

    accepted: bool | None | Unset = UNSET
    ai_note: None | str | Unset = UNSET
    total: int | Unset = 0
    turns: list[MemoryBankConversationTurnResponse] | Unset = UNSET
    user_input: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        total = self.total

        turns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.turns, Unset):
            turns = []
            for turns_item_data in self.turns:
                turns_item = turns_item_data.to_dict()
                turns.append(turns_item)

        user_input: None | str | Unset
        if isinstance(self.user_input, Unset):
            user_input = UNSET
        else:
            user_input = self.user_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if ai_note is not UNSET:
            field_dict["ai_note"] = ai_note
        if total is not UNSET:
            field_dict["total"] = total
        if turns is not UNSET:
            field_dict["turns"] = turns
        if user_input is not UNSET:
            field_dict["user_input"] = user_input

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_bank_conversation_turn_response import (
            MemoryBankConversationTurnResponse,
        )

        d = dict(src_dict)

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

        total = d.pop("total", UNSET)

        _turns = d.pop("turns", UNSET)
        turns: list[MemoryBankConversationTurnResponse] | Unset = UNSET
        if _turns is not UNSET:
            turns = []
            for turns_item_data in _turns:
                turns_item = MemoryBankConversationTurnResponse.from_dict(
                    turns_item_data
                )

                turns.append(turns_item)

        def _parse_user_input(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_input = _parse_user_input(d.pop("user_input", UNSET))

        memory_bank_last_conversation_response = cls(
            accepted=accepted,
            ai_note=ai_note,
            total=total,
            turns=turns,
            user_input=user_input,
        )

        memory_bank_last_conversation_response.additional_properties = d
        return memory_bank_last_conversation_response

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
