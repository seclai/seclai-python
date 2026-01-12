from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_trigger_frequency import AgentTriggerFrequency

T = TypeVar("T", bound="TriggerScheduleResponse")


@_attrs_define
class TriggerScheduleResponse:
    """Response model for agent trigger schedule data

    Attributes:
        agent_trigger_id (UUID):
        created_at (str):
        day_of_month (int | None):
        day_of_week (int | None):
        frequency (AgentTriggerFrequency):
        hour_of_day (int | None):
        id (UUID):
        minute_of_hour (int | None):
        repeat_interval (int):
        updated_at (str):
        weekday_of_month (int | None):
    """

    agent_trigger_id: UUID
    created_at: str
    day_of_month: int | None
    day_of_week: int | None
    frequency: AgentTriggerFrequency
    hour_of_day: int | None
    id: UUID
    minute_of_hour: int | None
    repeat_interval: int
    updated_at: str
    weekday_of_month: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_trigger_id = str(self.agent_trigger_id)

        created_at = self.created_at

        day_of_month: int | None
        day_of_month = self.day_of_month

        day_of_week: int | None
        day_of_week = self.day_of_week

        frequency = self.frequency.value

        hour_of_day: int | None
        hour_of_day = self.hour_of_day

        id = str(self.id)

        minute_of_hour: int | None
        minute_of_hour = self.minute_of_hour

        repeat_interval = self.repeat_interval

        updated_at = self.updated_at

        weekday_of_month: int | None
        weekday_of_month = self.weekday_of_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_trigger_id": agent_trigger_id,
                "created_at": created_at,
                "day_of_month": day_of_month,
                "day_of_week": day_of_week,
                "frequency": frequency,
                "hour_of_day": hour_of_day,
                "id": id,
                "minute_of_hour": minute_of_hour,
                "repeat_interval": repeat_interval,
                "updated_at": updated_at,
                "weekday_of_month": weekday_of_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_trigger_id = UUID(d.pop("agent_trigger_id"))

        created_at = d.pop("created_at")

        def _parse_day_of_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        day_of_month = _parse_day_of_month(d.pop("day_of_month"))

        def _parse_day_of_week(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        day_of_week = _parse_day_of_week(d.pop("day_of_week"))

        frequency = AgentTriggerFrequency(d.pop("frequency"))

        def _parse_hour_of_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hour_of_day = _parse_hour_of_day(d.pop("hour_of_day"))

        id = UUID(d.pop("id"))

        def _parse_minute_of_hour(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        minute_of_hour = _parse_minute_of_hour(d.pop("minute_of_hour"))

        repeat_interval = d.pop("repeat_interval")

        updated_at = d.pop("updated_at")

        def _parse_weekday_of_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weekday_of_month = _parse_weekday_of_month(d.pop("weekday_of_month"))

        trigger_schedule_response = cls(
            agent_trigger_id=agent_trigger_id,
            created_at=created_at,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            frequency=frequency,
            hour_of_day=hour_of_day,
            id=id,
            minute_of_hour=minute_of_hour,
            repeat_interval=repeat_interval,
            updated_at=updated_at,
            weekday_of_month=weekday_of_month,
        )

        trigger_schedule_response.additional_properties = d
        return trigger_schedule_response

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
