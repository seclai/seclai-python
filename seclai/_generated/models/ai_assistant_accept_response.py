from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.executed_action_response import ExecutedActionResponse


T = TypeVar("T", bound="AiAssistantAcceptResponse")


@_attrs_define
class AiAssistantAcceptResponse:
    """Response from accepting and executing a plan.

    Attributes:
        conversation_id (UUID): Conversation ID.
        executed_actions (list[ExecutedActionResponse]): Results of each executed action.
        error (None | str | Unset): Error message if failed.
        solution_id (None | Unset | UUID): Solution ID when a new solution was auto-created.
        success (bool | Unset): Whether execution succeeded. Default: True.
    """

    conversation_id: UUID
    executed_actions: list[ExecutedActionResponse]
    error: None | str | Unset = UNSET
    solution_id: None | Unset | UUID = UNSET
    success: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = str(self.conversation_id)

        executed_actions = []
        for executed_actions_item_data in self.executed_actions:
            executed_actions_item = executed_actions_item_data.to_dict()
            executed_actions.append(executed_actions_item)

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        solution_id: None | str | Unset
        if isinstance(self.solution_id, Unset):
            solution_id = UNSET
        elif isinstance(self.solution_id, UUID):
            solution_id = str(self.solution_id)
        else:
            solution_id = self.solution_id

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "executed_actions": executed_actions,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if solution_id is not UNSET:
            field_dict["solution_id"] = solution_id
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.executed_action_response import ExecutedActionResponse

        d = dict(src_dict)
        conversation_id = UUID(d.pop("conversation_id"))

        executed_actions = []
        _executed_actions = d.pop("executed_actions")
        for executed_actions_item_data in _executed_actions:
            executed_actions_item = ExecutedActionResponse.from_dict(
                executed_actions_item_data
            )

            executed_actions.append(executed_actions_item)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_solution_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                solution_id_type_0 = UUID(data)

                return solution_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        solution_id = _parse_solution_id(d.pop("solution_id", UNSET))

        success = d.pop("success", UNSET)

        ai_assistant_accept_response = cls(
            conversation_id=conversation_id,
            executed_actions=executed_actions,
            error=error,
            solution_id=solution_id,
            success=success,
        )

        ai_assistant_accept_response.additional_properties = d
        return ai_assistant_accept_response

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
