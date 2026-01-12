from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pending_completed_failed_status import PendingCompletedFailedStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatResponse")


@_attrs_define
class ChatResponse:
    """Response model for chat messages

    Attributes:
        assistant_response (None | str):
        conversation_id (str):
        message_id (str):
        prompt_model_id (str):
        status (PendingCompletedFailedStatus):
        user_prompt (str):
        error (None | str | Unset):
    """

    assistant_response: None | str
    conversation_id: str
    message_id: str
    prompt_model_id: str
    status: PendingCompletedFailedStatus
    user_prompt: str
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_response: None | str
        assistant_response = self.assistant_response

        conversation_id = self.conversation_id

        message_id = self.message_id

        prompt_model_id = self.prompt_model_id

        status = self.status.value

        user_prompt = self.user_prompt

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_response": assistant_response,
                "conversation_id": conversation_id,
                "message_id": message_id,
                "prompt_model_id": prompt_model_id,
                "status": status,
                "user_prompt": user_prompt,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assistant_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assistant_response = _parse_assistant_response(d.pop("assistant_response"))

        conversation_id = d.pop("conversation_id")

        message_id = d.pop("message_id")

        prompt_model_id = d.pop("prompt_model_id")

        status = PendingCompletedFailedStatus(d.pop("status"))

        user_prompt = d.pop("user_prompt")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        chat_response = cls(
            assistant_response=assistant_response,
            conversation_id=conversation_id,
            message_id=message_id,
            prompt_model_id=prompt_model_id,
            status=status,
            user_prompt=user_prompt,
            error=error,
        )

        chat_response.additional_properties = d
        return chat_response

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
