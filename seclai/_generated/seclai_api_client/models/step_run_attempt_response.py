from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StepRunAttemptResponse")


@_attrs_define
class StepRunAttemptResponse:
    """Response model for a single step run attempt

    Attributes:
        agent_step_run_id (UUID):
        created_at (str):
        ended_at (None | str):
        error (None | str):
        id (UUID):
        started_at (None | str):
        status (str):
        updated_at (str):
    """

    agent_step_run_id: UUID
    created_at: str
    ended_at: None | str
    error: None | str
    id: UUID
    started_at: None | str
    status: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_step_run_id = str(self.agent_step_run_id)

        created_at = self.created_at

        ended_at: None | str
        ended_at = self.ended_at

        error: None | str
        error = self.error

        id = str(self.id)

        started_at: None | str
        started_at = self.started_at

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_step_run_id": agent_step_run_id,
                "created_at": created_at,
                "ended_at": ended_at,
                "error": error,
                "id": id,
                "started_at": started_at,
                "status": status,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_step_run_id = UUID(d.pop("agent_step_run_id"))

        created_at = d.pop("created_at")

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

        id = UUID(d.pop("id"))

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = d.pop("status")

        updated_at = d.pop("updated_at")

        step_run_attempt_response = cls(
            agent_step_run_id=agent_step_run_id,
            created_at=created_at,
            ended_at=ended_at,
            error=error,
            id=id,
            started_at=started_at,
            status=status,
            updated_at=updated_at,
        )

        step_run_attempt_response.additional_properties = d
        return step_run_attempt_response

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
