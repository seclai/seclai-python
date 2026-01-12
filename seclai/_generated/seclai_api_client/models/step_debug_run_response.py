from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StepDebugRunResponse")


@_attrs_define
class StepDebugRunResponse:
    """
    Attributes:
        success (bool): Whether the debug run succeeded
        error (None | str | Unset): Error message when the run fails
        output (None | str | Unset): Rendered output captured from the step
        step_run_id (None | Unset | UUID): ID of the temporary step run
    """

    success: bool
    error: None | str | Unset = UNSET
    output: None | str | Unset = UNSET
    step_run_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        step_run_id: None | str | Unset
        if isinstance(self.step_run_id, Unset):
            step_run_id = UNSET
        elif isinstance(self.step_run_id, UUID):
            step_run_id = str(self.step_run_id)
        else:
            step_run_id = self.step_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if output is not UNSET:
            field_dict["output"] = output
        if step_run_id is not UNSET:
            field_dict["step_run_id"] = step_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        def _parse_step_run_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_run_id_type_0 = UUID(data)

                return step_run_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        step_run_id = _parse_step_run_id(d.pop("step_run_id", UNSET))

        step_debug_run_response = cls(
            success=success,
            error=error,
            output=output,
            step_run_id=step_run_id,
        )

        step_debug_run_response.additional_properties = d
        return step_debug_run_response

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
