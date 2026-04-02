from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ai_conversation_turn_response import AiConversationTurnResponse


T = TypeVar("T", bound="AiConversationHistoryResponse")


@_attrs_define
class AiConversationHistoryResponse:
    """
    Attributes:
        total (int): Total number of conversation turns available.
        turns (list[AiConversationTurnResponse]): Conversation turns, ordered oldest first.
    """

    total: int
    turns: list[AiConversationTurnResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        turns = []
        for turns_item_data in self.turns:
            turns_item = turns_item_data.to_dict()
            turns.append(turns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "turns": turns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_conversation_turn_response import AiConversationTurnResponse

        d = dict(src_dict)
        total = d.pop("total")

        turns = []
        _turns = d.pop("turns")
        for turns_item_data in _turns:
            turns_item = AiConversationTurnResponse.from_dict(turns_item_data)

            turns.append(turns_item)

        ai_conversation_history_response = cls(
            total=total,
            turns=turns,
        )

        ai_conversation_history_response.additional_properties = d
        return ai_conversation_history_response

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
