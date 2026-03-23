from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_debug_run_request_manual_inputs import (
        StepDebugRunRequestManualInputs,
    )
    from ..models.step_debug_run_request_manual_metadata import (
        StepDebugRunRequestManualMetadata,
    )
    from ..models.step_debug_run_request_manual_outputs import (
        StepDebugRunRequestManualOutputs,
    )


T = TypeVar("T", bound="StepDebugRunRequest")


@_attrs_define
class StepDebugRunRequest:
    """
    Attributes:
        agent_input (None | str | Unset): Override for the original agent input
        manual_inputs (StepDebugRunRequestManualInputs | Unset): Manual overrides for {{step.<id>.input}}
        manual_metadata (StepDebugRunRequestManualMetadata | Unset): Manual metadata values
        manual_outputs (StepDebugRunRequestManualOutputs | Unset): Manual overrides for {{step.<id>.output}}
        source_agent_run_id (None | Unset | UUID): Optional agent run to use for default inputs
    """

    agent_input: None | str | Unset = UNSET
    manual_inputs: StepDebugRunRequestManualInputs | Unset = UNSET
    manual_metadata: StepDebugRunRequestManualMetadata | Unset = UNSET
    manual_outputs: StepDebugRunRequestManualOutputs | Unset = UNSET
    source_agent_run_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_input: None | str | Unset
        if isinstance(self.agent_input, Unset):
            agent_input = UNSET
        else:
            agent_input = self.agent_input

        manual_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manual_inputs, Unset):
            manual_inputs = self.manual_inputs.to_dict()

        manual_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manual_metadata, Unset):
            manual_metadata = self.manual_metadata.to_dict()

        manual_outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manual_outputs, Unset):
            manual_outputs = self.manual_outputs.to_dict()

        source_agent_run_id: None | str | Unset
        if isinstance(self.source_agent_run_id, Unset):
            source_agent_run_id = UNSET
        elif isinstance(self.source_agent_run_id, UUID):
            source_agent_run_id = str(self.source_agent_run_id)
        else:
            source_agent_run_id = self.source_agent_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_input is not UNSET:
            field_dict["agent_input"] = agent_input
        if manual_inputs is not UNSET:
            field_dict["manual_inputs"] = manual_inputs
        if manual_metadata is not UNSET:
            field_dict["manual_metadata"] = manual_metadata
        if manual_outputs is not UNSET:
            field_dict["manual_outputs"] = manual_outputs
        if source_agent_run_id is not UNSET:
            field_dict["source_agent_run_id"] = source_agent_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_debug_run_request_manual_inputs import (
            StepDebugRunRequestManualInputs,
        )
        from ..models.step_debug_run_request_manual_metadata import (
            StepDebugRunRequestManualMetadata,
        )
        from ..models.step_debug_run_request_manual_outputs import (
            StepDebugRunRequestManualOutputs,
        )

        d = dict(src_dict)

        def _parse_agent_input(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_input = _parse_agent_input(d.pop("agent_input", UNSET))

        _manual_inputs = d.pop("manual_inputs", UNSET)
        manual_inputs: StepDebugRunRequestManualInputs | Unset
        if isinstance(_manual_inputs, Unset):
            manual_inputs = UNSET
        else:
            manual_inputs = StepDebugRunRequestManualInputs.from_dict(_manual_inputs)

        _manual_metadata = d.pop("manual_metadata", UNSET)
        manual_metadata: StepDebugRunRequestManualMetadata | Unset
        if isinstance(_manual_metadata, Unset):
            manual_metadata = UNSET
        else:
            manual_metadata = StepDebugRunRequestManualMetadata.from_dict(
                _manual_metadata
            )

        _manual_outputs = d.pop("manual_outputs", UNSET)
        manual_outputs: StepDebugRunRequestManualOutputs | Unset
        if isinstance(_manual_outputs, Unset):
            manual_outputs = UNSET
        else:
            manual_outputs = StepDebugRunRequestManualOutputs.from_dict(_manual_outputs)

        def _parse_source_agent_run_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_agent_run_id_type_0 = UUID(data)

                return source_agent_run_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_agent_run_id = _parse_source_agent_run_id(
            d.pop("source_agent_run_id", UNSET)
        )

        step_debug_run_request = cls(
            agent_input=agent_input,
            manual_inputs=manual_inputs,
            manual_metadata=manual_metadata,
            manual_outputs=manual_outputs,
            source_agent_run_id=source_agent_run_id,
        )

        step_debug_run_request.additional_properties = d
        return step_debug_run_request

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
