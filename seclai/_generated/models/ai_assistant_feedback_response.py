from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiAssistantFeedbackResponse")


@_attrs_define
class AiAssistantFeedbackResponse:
    """Response after submitting feedback.

    Attributes:
        feedback_id (UUID):
        flagged (bool):
        flag_reason (None | str | Unset):
    """

    feedback_id: UUID
    flagged: bool
    flag_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feedback_id = str(self.feedback_id)

        flagged = self.flagged

        flag_reason: None | str | Unset
        if isinstance(self.flag_reason, Unset):
            flag_reason = UNSET
        else:
            flag_reason = self.flag_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedback_id": feedback_id,
                "flagged": flagged,
            }
        )
        if flag_reason is not UNSET:
            field_dict["flag_reason"] = flag_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedback_id = UUID(d.pop("feedback_id"))

        flagged = d.pop("flagged")

        def _parse_flag_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flag_reason = _parse_flag_reason(d.pop("flag_reason", UNSET))

        ai_assistant_feedback_response = cls(
            feedback_id=feedback_id,
            flagged=flagged,
            flag_reason=flag_reason,
        )

        ai_assistant_feedback_response.additional_properties = d
        return ai_assistant_feedback_response

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
