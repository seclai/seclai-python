from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompatibleRunResponse")


@_attrs_define
class CompatibleRunResponse:
    """A run that has a completed step matching a criteria's step_id.

    Attributes:
        agent_run_id (UUID):
        agent_step_run_id (UUID):
        completed_at (None | str):
        output_storage_key (None | str):
        input_preview (None | str | Unset):
        run_status (None | str | Unset):
        started_at (None | str | Unset):
    """

    agent_run_id: UUID
    agent_step_run_id: UUID
    completed_at: None | str
    output_storage_key: None | str
    input_preview: None | str | Unset = UNSET
    run_status: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_run_id = str(self.agent_run_id)

        agent_step_run_id = str(self.agent_step_run_id)

        completed_at: None | str
        completed_at = self.completed_at

        output_storage_key: None | str
        output_storage_key = self.output_storage_key

        input_preview: None | str | Unset
        if isinstance(self.input_preview, Unset):
            input_preview = UNSET
        else:
            input_preview = self.input_preview

        run_status: None | str | Unset
        if isinstance(self.run_status, Unset):
            run_status = UNSET
        else:
            run_status = self.run_status

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_run_id": agent_run_id,
                "agent_step_run_id": agent_step_run_id,
                "completed_at": completed_at,
                "output_storage_key": output_storage_key,
            }
        )
        if input_preview is not UNSET:
            field_dict["input_preview"] = input_preview
        if run_status is not UNSET:
            field_dict["run_status"] = run_status
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_run_id = UUID(d.pop("agent_run_id"))

        agent_step_run_id = UUID(d.pop("agent_step_run_id"))

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        def _parse_output_storage_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output_storage_key = _parse_output_storage_key(d.pop("output_storage_key"))

        def _parse_input_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_preview = _parse_input_preview(d.pop("input_preview", UNSET))

        def _parse_run_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_status = _parse_run_status(d.pop("run_status", UNSET))

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        compatible_run_response = cls(
            agent_run_id=agent_run_id,
            agent_step_run_id=agent_step_run_id,
            completed_at=completed_at,
            output_storage_key=output_storage_key,
            input_preview=input_preview,
            run_status=run_status,
            started_at=started_at,
        )

        compatible_run_response.additional_properties = d
        return compatible_run_response

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
