from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.governance_conversation_response_proposed_actions_type_0 import (
        GovernanceConversationResponseProposedActionsType0,
    )


T = TypeVar("T", bound="GovernanceConversationResponse")


@_attrs_define
class GovernanceConversationResponse:
    """A governance AI assistant conversation entry.

    Attributes:
        accepted (bool | None): True if accepted, false if declined, null if pending.
        ai_response (None | str): The AI assistant's response note, or null.
        created_at (str): ISO 8601 creation timestamp.
        id (str): Conversation ID.
        proposed_actions (GovernanceConversationResponseProposedActionsType0 | None): JSON of proposed actions, or null.
        user_input (str): The original user request.
    """

    accepted: bool | None
    ai_response: None | str
    created_at: str
    id: str
    proposed_actions: GovernanceConversationResponseProposedActionsType0 | None
    user_input: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.governance_conversation_response_proposed_actions_type_0 import (
            GovernanceConversationResponseProposedActionsType0,
        )

        accepted: bool | None
        accepted = self.accepted

        ai_response: None | str
        ai_response = self.ai_response

        created_at = self.created_at

        id = self.id

        proposed_actions: dict[str, Any] | None
        if isinstance(
            self.proposed_actions, GovernanceConversationResponseProposedActionsType0
        ):
            proposed_actions = self.proposed_actions.to_dict()
        else:
            proposed_actions = self.proposed_actions

        user_input = self.user_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "ai_response": ai_response,
                "created_at": created_at,
                "id": id,
                "proposed_actions": proposed_actions,
                "user_input": user_input,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.governance_conversation_response_proposed_actions_type_0 import (
            GovernanceConversationResponseProposedActionsType0,
        )

        d = dict(src_dict)

        def _parse_accepted(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        accepted = _parse_accepted(d.pop("accepted"))

        def _parse_ai_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ai_response = _parse_ai_response(d.pop("ai_response"))

        created_at = d.pop("created_at")

        id = d.pop("id")

        def _parse_proposed_actions(
            data: object,
        ) -> GovernanceConversationResponseProposedActionsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                proposed_actions_type_0 = (
                    GovernanceConversationResponseProposedActionsType0.from_dict(data)
                )

                return proposed_actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GovernanceConversationResponseProposedActionsType0 | None, data)

        proposed_actions = _parse_proposed_actions(d.pop("proposed_actions"))

        user_input = d.pop("user_input")

        governance_conversation_response = cls(
            accepted=accepted,
            ai_response=ai_response,
            created_at=created_at,
            id=id,
            proposed_actions=proposed_actions,
            user_input=user_input,
        )

        governance_conversation_response.additional_properties = d
        return governance_conversation_response

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
