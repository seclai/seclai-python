from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_conversation_turn_request_actions_taken_type_0 import (
        AddConversationTurnRequestActionsTakenType0,
    )


T = TypeVar("T", bound="AddConversationTurnRequest")


@_attrs_define
class AddConversationTurnRequest:
    """
    Attributes:
        user_input (str): User input text
        actions_taken (AddConversationTurnRequestActionsTakenType0 | None | Unset): Actions taken by the AI
        ai_response (None | str | Unset): AI response text
    """

    user_input: str
    actions_taken: AddConversationTurnRequestActionsTakenType0 | None | Unset = UNSET
    ai_response: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_conversation_turn_request_actions_taken_type_0 import (
            AddConversationTurnRequestActionsTakenType0,
        )

        user_input = self.user_input

        actions_taken: dict[str, Any] | None | Unset
        if isinstance(self.actions_taken, Unset):
            actions_taken = UNSET
        elif isinstance(
            self.actions_taken, AddConversationTurnRequestActionsTakenType0
        ):
            actions_taken = self.actions_taken.to_dict()
        else:
            actions_taken = self.actions_taken

        ai_response: None | str | Unset
        if isinstance(self.ai_response, Unset):
            ai_response = UNSET
        else:
            ai_response = self.ai_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_input": user_input,
            }
        )
        if actions_taken is not UNSET:
            field_dict["actions_taken"] = actions_taken
        if ai_response is not UNSET:
            field_dict["ai_response"] = ai_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_conversation_turn_request_actions_taken_type_0 import (
            AddConversationTurnRequestActionsTakenType0,
        )

        d = dict(src_dict)
        user_input = d.pop("user_input")

        def _parse_actions_taken(
            data: object,
        ) -> AddConversationTurnRequestActionsTakenType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actions_taken_type_0 = (
                    AddConversationTurnRequestActionsTakenType0.from_dict(data)
                )

                return actions_taken_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AddConversationTurnRequestActionsTakenType0 | None | Unset, data
            )

        actions_taken = _parse_actions_taken(d.pop("actions_taken", UNSET))

        def _parse_ai_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_response = _parse_ai_response(d.pop("ai_response", UNSET))

        add_conversation_turn_request = cls(
            user_input=user_input,
            actions_taken=actions_taken,
            ai_response=ai_response,
        )

        add_conversation_turn_request.additional_properties = d
        return add_conversation_turn_request

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
