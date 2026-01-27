from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pending_processing_completed_failed_status import PendingProcessingCompletedFailedStatus

T = TypeVar("T", bound="AgentRunStepResponse")


@_attrs_define
class AgentRunStepResponse:
    """
    Attributes:
        agent_step_id (str): Agent step identifier.
        credits_used (float): Credits consumed by the step attempt, if applicable.
        duration_seconds (float | None): Duration of the step attempt in seconds.
        ended_at (None | str): Timestamp when the step attempt ended.
        output (None | str): Output produced by the step, if any.
        output_content_type (None | str): Content type of the step output, if any.
        started_at (None | str): Timestamp when the step attempt started.
        status (PendingProcessingCompletedFailedStatus):
        step_type (str): Type of the agent step.
    """

    agent_step_id: str
    credits_used: float
    duration_seconds: float | None
    ended_at: None | str
    output: None | str
    output_content_type: None | str
    started_at: None | str
    status: PendingProcessingCompletedFailedStatus
    step_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_step_id = self.agent_step_id

        credits_used = self.credits_used

        duration_seconds: float | None
        duration_seconds = self.duration_seconds

        ended_at: None | str
        ended_at = self.ended_at

        output: None | str
        output = self.output

        output_content_type: None | str
        output_content_type = self.output_content_type

        started_at: None | str
        started_at = self.started_at

        status = self.status.value

        step_type = self.step_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_step_id": agent_step_id,
                "credits_used": credits_used,
                "duration_seconds": duration_seconds,
                "ended_at": ended_at,
                "output": output,
                "output_content_type": output_content_type,
                "started_at": started_at,
                "status": status,
                "step_type": step_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_step_id = d.pop("agent_step_id")

        credits_used = d.pop("credits_used")

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

        def _parse_output(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output = _parse_output(d.pop("output"))

        def _parse_output_content_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output_content_type = _parse_output_content_type(d.pop("output_content_type"))

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = PendingProcessingCompletedFailedStatus(d.pop("status"))

        step_type = d.pop("step_type")

        agent_run_step_response = cls(
            agent_step_id=agent_step_id,
            credits_used=credits_used,
            duration_seconds=duration_seconds,
            ended_at=ended_at,
            output=output,
            output_content_type=output_content_type,
            started_at=started_at,
            status=status,
            step_type=step_type,
        )

        agent_run_step_response.additional_properties = d
        return agent_run_step_response

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
