from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRunStatusResponse")


@_attrs_define
class AgentRunStatusResponse:
    """Response model for agent run status and optional display output.

    Attributes:
        agent_id (UUID):
        run_id (UUID):
        status (str):
        steps_completed (int):
        steps_total (int):
        credits_used (float | None | Unset):
        error (None | str | Unset):
        output (None | str | Unset):
    """

    agent_id: UUID
    run_id: UUID
    status: str
    steps_completed: int
    steps_total: int
    credits_used: float | None | Unset = UNSET
    error: None | str | Unset = UNSET
    output: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        run_id = str(self.run_id)

        status = self.status

        steps_completed = self.steps_completed

        steps_total = self.steps_total

        credits_used: float | None | Unset
        if isinstance(self.credits_used, Unset):
            credits_used = UNSET
        else:
            credits_used = self.credits_used

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "run_id": run_id,
                "status": status,
                "steps_completed": steps_completed,
                "steps_total": steps_total,
            }
        )
        if credits_used is not UNSET:
            field_dict["credits_used"] = credits_used
        if error is not UNSET:
            field_dict["error"] = error
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        run_id = UUID(d.pop("run_id"))

        status = d.pop("status")

        steps_completed = d.pop("steps_completed")

        steps_total = d.pop("steps_total")

        def _parse_credits_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_used = _parse_credits_used(d.pop("credits_used", UNSET))

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

        agent_run_status_response = cls(
            agent_id=agent_id,
            run_id=run_id,
            status=status,
            steps_completed=steps_completed,
            steps_total=steps_total,
            credits_used=credits_used,
            error=error,
            output=output,
        )

        agent_run_status_response.additional_properties = d
        return agent_run_status_response

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
