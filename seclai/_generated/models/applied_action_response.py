from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppliedActionResponse")


@_attrs_define
class AppliedActionResponse:
    """Result of a single executed governance action.

    Attributes:
        action_type (str): Type of action that was executed.
        description (str): Human-readable description of the executed action.
        success (bool): Whether this individual action succeeded.
        error (None | str | Unset): Error message if this action failed, or null.
        policy_id (None | str | Unset): ID of the policy that was created or modified, or null.
    """

    action_type: str
    description: str
    success: bool
    error: None | str | Unset = UNSET
    policy_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        description = self.description

        success = self.success

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        policy_id: None | str | Unset
        if isinstance(self.policy_id, Unset):
            policy_id = UNSET
        else:
            policy_id = self.policy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "description": description,
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = d.pop("action_type")

        description = d.pop("description")

        success = d.pop("success")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_policy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_id = _parse_policy_id(d.pop("policy_id", UNSET))

        applied_action_response = cls(
            action_type=action_type,
            description=description,
            success=success,
            error=error,
            policy_id=policy_id,
        )

        applied_action_response.additional_properties = d
        return applied_action_response

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
