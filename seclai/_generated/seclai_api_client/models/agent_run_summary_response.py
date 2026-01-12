from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRunSummaryResponse")


@_attrs_define
class AgentRunSummaryResponse:
    """Response model for a single agent run summary

    Attributes:
        agent_id (UUID):
        created_at (str):
        id (UUID):
        mode (str):
        status (str):
        updated_at (str):
        completed_at (None | str | Unset):
        credits_used (float | None | Unset):
        started_at (None | str | Unset):
        steps_completed (int | Unset):  Default: 0.
        steps_total (int | Unset):  Default: 0.
    """

    agent_id: UUID
    created_at: str
    id: UUID
    mode: str
    status: str
    updated_at: str
    completed_at: None | str | Unset = UNSET
    credits_used: float | None | Unset = UNSET
    started_at: None | str | Unset = UNSET
    steps_completed: int | Unset = 0
    steps_total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        created_at = self.created_at

        id = str(self.id)

        mode = self.mode

        status = self.status

        updated_at = self.updated_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        credits_used: float | None | Unset
        if isinstance(self.credits_used, Unset):
            credits_used = UNSET
        else:
            credits_used = self.credits_used

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        steps_completed = self.steps_completed

        steps_total = self.steps_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "created_at": created_at,
                "id": id,
                "mode": mode,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if credits_used is not UNSET:
            field_dict["credits_used"] = credits_used
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if steps_completed is not UNSET:
            field_dict["steps_completed"] = steps_completed
        if steps_total is not UNSET:
            field_dict["steps_total"] = steps_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        mode = d.pop("mode")

        status = d.pop("status")

        updated_at = d.pop("updated_at")

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_credits_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_used = _parse_credits_used(d.pop("credits_used", UNSET))

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        steps_completed = d.pop("steps_completed", UNSET)

        steps_total = d.pop("steps_total", UNSET)

        agent_run_summary_response = cls(
            agent_id=agent_id,
            created_at=created_at,
            id=id,
            mode=mode,
            status=status,
            updated_at=updated_at,
            completed_at=completed_at,
            credits_used=credits_used,
            started_at=started_at,
            steps_completed=steps_completed,
            steps_total=steps_total,
        )

        agent_run_summary_response.additional_properties = d
        return agent_run_summary_response

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
