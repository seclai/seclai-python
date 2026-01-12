from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentWarningModel")


@_attrs_define
class AgentWarningModel:
    """Warning about potential issues in an agent

    Attributes:
        message (str):
        step_path (str):
        severity (str | Unset):  Default: 'warning'.
    """

    message: str
    step_path: str
    severity: str | Unset = "warning"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        step_path = self.step_path

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "step_path": step_path,
            }
        )
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        step_path = d.pop("step_path")

        severity = d.pop("severity", UNSET)

        agent_warning_model = cls(
            message=message,
            step_path=step_path,
            severity=severity,
        )

        agent_warning_model.additional_properties = d
        return agent_warning_model

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
