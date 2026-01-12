from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRunStepDetailsResponse")


@_attrs_define
class AgentRunStepDetailsResponse:
    """Response model for detailed per-step run information.

    Attributes:
        agent_step_id (str):
        credits_used (float | None):
        duration_seconds (float | None):
        ended_at (None | str):
        error (None | str):
        input_ (None | str):
        output (None | str):
        started_at (None | str):
        status (str):
        step_type (None | str | Unset):
    """

    agent_step_id: str
    credits_used: float | None
    duration_seconds: float | None
    ended_at: None | str
    error: None | str
    input_: None | str
    output: None | str
    started_at: None | str
    status: str
    step_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_step_id = self.agent_step_id

        credits_used: float | None
        credits_used = self.credits_used

        duration_seconds: float | None
        duration_seconds = self.duration_seconds

        ended_at: None | str
        ended_at = self.ended_at

        error: None | str
        error = self.error

        input_: None | str
        input_ = self.input_

        output: None | str
        output = self.output

        started_at: None | str
        started_at = self.started_at

        status = self.status

        step_type: None | str | Unset
        if isinstance(self.step_type, Unset):
            step_type = UNSET
        else:
            step_type = self.step_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_step_id": agent_step_id,
                "credits_used": credits_used,
                "duration_seconds": duration_seconds,
                "ended_at": ended_at,
                "error": error,
                "input": input_,
                "output": output,
                "started_at": started_at,
                "status": status,
            }
        )
        if step_type is not UNSET:
            field_dict["step_type"] = step_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_step_id = d.pop("agent_step_id")

        def _parse_credits_used(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        credits_used = _parse_credits_used(d.pop("credits_used"))

        def _parse_duration_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds"))

        def _parse_ended_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ended_at = _parse_ended_at(d.pop("ended_at"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        def _parse_input_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_output(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output = _parse_output(d.pop("output"))

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = d.pop("status")

        def _parse_step_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_type = _parse_step_type(d.pop("step_type", UNSET))

        agent_run_step_details_response = cls(
            agent_step_id=agent_step_id,
            credits_used=credits_used,
            duration_seconds=duration_seconds,
            ended_at=ended_at,
            error=error,
            input_=input_,
            output=output,
            started_at=started_at,
            status=status,
            step_type=step_type,
        )

        agent_run_step_details_response.additional_properties = d
        return agent_run_step_details_response

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
