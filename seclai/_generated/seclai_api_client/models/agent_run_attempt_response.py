from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pending_processing_completed_failed_status import PendingProcessingCompletedFailedStatus

T = TypeVar("T", bound="AgentRunAttemptResponse")


@_attrs_define
class AgentRunAttemptResponse:
    """
    Attributes:
        duration (float | None): Duration of the attempt in seconds.
        ended_at (None | str): Timestamp when the attempt ended.
        error (None | str): Error message if the attempt failed.
        started_at (None | str): Timestamp when the attempt started.
        status (PendingProcessingCompletedFailedStatus):
    """

    duration: float | None
    ended_at: None | str
    error: None | str
    started_at: None | str
    status: PendingProcessingCompletedFailedStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration: float | None
        duration = self.duration

        ended_at: None | str
        ended_at = self.ended_at

        error: None | str
        error = self.error

        started_at: None | str
        started_at = self.started_at

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "ended_at": ended_at,
                "error": error,
                "started_at": started_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_duration(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration = _parse_duration(d.pop("duration"))

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

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = PendingProcessingCompletedFailedStatus(d.pop("status"))

        agent_run_attempt_response = cls(
            duration=duration,
            ended_at=ended_at,
            error=error,
            started_at=started_at,
            status=status,
        )

        agent_run_attempt_response.additional_properties = d
        return agent_run_attempt_response

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
