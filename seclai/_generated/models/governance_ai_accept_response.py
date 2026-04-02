from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.applied_action_response import AppliedActionResponse


T = TypeVar("T", bound="GovernanceAiAcceptResponse")


@_attrs_define
class GovernanceAiAcceptResponse:
    """Response from accepting a governance AI assistant plan.

    Attributes:
        actions_applied (list[AppliedActionResponse]): Results of each action that was executed.
        conversation_id (str): Conversation ID that was accepted.
        success (bool): Whether all actions were applied successfully.
        error (None | str | Unset): Overall error message if the plan failed, or null.
    """

    actions_applied: list[AppliedActionResponse]
    conversation_id: str
    success: bool
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions_applied = []
        for actions_applied_item_data in self.actions_applied:
            actions_applied_item = actions_applied_item_data.to_dict()
            actions_applied.append(actions_applied_item)

        conversation_id = self.conversation_id

        success = self.success

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions_applied": actions_applied,
                "conversation_id": conversation_id,
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.applied_action_response import AppliedActionResponse

        d = dict(src_dict)
        actions_applied = []
        _actions_applied = d.pop("actions_applied")
        for actions_applied_item_data in _actions_applied:
            actions_applied_item = AppliedActionResponse.from_dict(
                actions_applied_item_data
            )

            actions_applied.append(actions_applied_item)

        conversation_id = d.pop("conversation_id")

        success = d.pop("success")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        governance_ai_accept_response = cls(
            actions_applied=actions_applied,
            conversation_id=conversation_id,
            success=success,
            error=error,
        )

        governance_ai_accept_response.additional_properties = d
        return governance_ai_accept_response

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
