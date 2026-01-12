from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConversationMessageResponse")


@_attrs_define
class ConversationMessageResponse:
    """Response model for conversation message data

    Attributes:
        assistant_response (None | str):
        created_at (str):
        id (UUID):
        status (str):
        updated_at (str):
        user_prompt (str):
    """

    assistant_response: None | str
    created_at: str
    id: UUID
    status: str
    updated_at: str
    user_prompt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_response: None | str
        assistant_response = self.assistant_response

        created_at = self.created_at

        id = str(self.id)

        status = self.status

        updated_at = self.updated_at

        user_prompt = self.user_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_response": assistant_response,
                "created_at": created_at,
                "id": id,
                "status": status,
                "updated_at": updated_at,
                "user_prompt": user_prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assistant_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assistant_response = _parse_assistant_response(d.pop("assistant_response"))

        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        status = d.pop("status")

        updated_at = d.pop("updated_at")

        user_prompt = d.pop("user_prompt")

        conversation_message_response = cls(
            assistant_response=assistant_response,
            created_at=created_at,
            id=id,
            status=status,
            updated_at=updated_at,
            user_prompt=user_prompt,
        )

        conversation_message_response.additional_properties = d
        return conversation_message_response

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
