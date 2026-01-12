from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubstitutionDependencies")


@_attrs_define
class SubstitutionDependencies:
    """Dependencies found in templates.

    Attributes:
        agent_input_required (bool): Whether {{agent.input}} is used (original agent input)
        current_step_input_required (bool): Whether {{input}} is used (previous step output)
        metadata_fields (list[str]): Metadata fields referenced
        step_inputs (list[str]): Step IDs referenced for input
        step_outputs (list[str]): Step IDs referenced for output
    """

    agent_input_required: bool
    current_step_input_required: bool
    metadata_fields: list[str]
    step_inputs: list[str]
    step_outputs: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_input_required = self.agent_input_required

        current_step_input_required = self.current_step_input_required

        metadata_fields = self.metadata_fields

        step_inputs = self.step_inputs

        step_outputs = self.step_outputs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_input_required": agent_input_required,
                "current_step_input_required": current_step_input_required,
                "metadata_fields": metadata_fields,
                "step_inputs": step_inputs,
                "step_outputs": step_outputs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_input_required = d.pop("agent_input_required")

        current_step_input_required = d.pop("current_step_input_required")

        metadata_fields = cast(list[str], d.pop("metadata_fields"))

        step_inputs = cast(list[str], d.pop("step_inputs"))

        step_outputs = cast(list[str], d.pop("step_outputs"))

        substitution_dependencies = cls(
            agent_input_required=agent_input_required,
            current_step_input_required=current_step_input_required,
            metadata_fields=metadata_fields,
            step_inputs=step_inputs,
            step_outputs=step_outputs,
        )

        substitution_dependencies.additional_properties = d
        return substitution_dependencies

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
