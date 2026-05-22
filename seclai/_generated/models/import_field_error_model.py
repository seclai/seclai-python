from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImportFieldErrorModel")


@_attrs_define
class ImportFieldErrorModel:
    """Single agent_definition validation error with source position.

    Attributes:
        column (int): 1-indexed column in `source`.
        line (int): 1-indexed line in `source`.
        message (str): Human-readable description of the problem.
        path (str): Dotted path of the offending field, e.g. `agent.definition.child_steps[0].step_type`.
    """

    column: int
    line: int
    message: str
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        line = self.line

        message = self.message

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
                "line": line,
                "message": message,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        line = d.pop("line")

        message = d.pop("message")

        path = d.pop("path")

        import_field_error_model = cls(
            column=column,
            line=line,
            message=message,
            path=path,
        )

        import_field_error_model.additional_properties = d
        return import_field_error_model

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
