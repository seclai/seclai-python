from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.solution_conversation_response_actions_taken_type_0 import (
        SolutionConversationResponseActionsTakenType0,
    )


T = TypeVar("T", bound="SolutionConversationResponse")


@_attrs_define
class SolutionConversationResponse:
    """Response model for a conversation turn.

    Attributes:
        accepted (bool | None): Whether the suggestion was accepted or declined.
        actions_taken (None | SolutionConversationResponseActionsTakenType0): Actions taken by the AI.
        ai_response (None | str): AI response text.
        created_at (str): Timestamp when the conversation was created.
        id (UUID): Unique identifier for the conversation turn.
        user_input (str): User input text.
    """

    accepted: bool | None
    actions_taken: None | SolutionConversationResponseActionsTakenType0
    ai_response: None | str
    created_at: str
    id: UUID
    user_input: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.solution_conversation_response_actions_taken_type_0 import (
            SolutionConversationResponseActionsTakenType0,
        )

        accepted: bool | None
        accepted = self.accepted

        actions_taken: dict[str, Any] | None
        if isinstance(
            self.actions_taken, SolutionConversationResponseActionsTakenType0
        ):
            actions_taken = self.actions_taken.to_dict()
        else:
            actions_taken = self.actions_taken

        ai_response: None | str
        ai_response = self.ai_response

        created_at = self.created_at

        id = str(self.id)

        user_input = self.user_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "actions_taken": actions_taken,
                "ai_response": ai_response,
                "created_at": created_at,
                "id": id,
                "user_input": user_input,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.solution_conversation_response_actions_taken_type_0 import (
            SolutionConversationResponseActionsTakenType0,
        )

        d = dict(src_dict)

        def _parse_accepted(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        accepted = _parse_accepted(d.pop("accepted"))

        def _parse_actions_taken(
            data: object,
        ) -> None | SolutionConversationResponseActionsTakenType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actions_taken_type_0 = (
                    SolutionConversationResponseActionsTakenType0.from_dict(data)
                )

                return actions_taken_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SolutionConversationResponseActionsTakenType0, data)

        actions_taken = _parse_actions_taken(d.pop("actions_taken"))

        def _parse_ai_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ai_response = _parse_ai_response(d.pop("ai_response"))

        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        user_input = d.pop("user_input")

        solution_conversation_response = cls(
            accepted=accepted,
            actions_taken=actions_taken,
            ai_response=ai_response,
            created_at=created_at,
            id=id,
            user_input=user_input,
        )

        solution_conversation_response.additional_properties = d
        return solution_conversation_response

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
