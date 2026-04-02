from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutedActionResponse")


@_attrs_define
class ExecutedActionResponse:
    """A single executed action result.

    Attributes:
        action_type (str): Type of the executed action.
        description (str): Human-readable description.
        error (None | str | Unset): Error message if failed.
        resource_id (None | str | Unset): ID of the affected resource.
        resource_type (None | str | Unset): Type of the affected resource.
        success (bool | Unset): Whether the action succeeded. Default: True.
    """

    action_type: str
    description: str
    error: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    resource_type: None | str | Unset = UNSET
    success: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        description = self.description

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "description": description,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = d.pop("action_type")

        description = d.pop("description")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resource_type", UNSET))

        success = d.pop("success", UNSET)

        executed_action_response = cls(
            action_type=action_type,
            description=description,
            error=error,
            resource_id=resource_id,
            resource_type=resource_type,
            success=success,
        )

        executed_action_response.additional_properties = d
        return executed_action_response

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
