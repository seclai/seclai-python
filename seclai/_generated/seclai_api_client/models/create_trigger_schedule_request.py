from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_trigger_frequency import AgentTriggerFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTriggerScheduleRequest")


@_attrs_define
class CreateTriggerScheduleRequest:
    """Request model for creating an agent trigger schedule

    Attributes:
        frequency (AgentTriggerFrequency):
        day_of_month (int | None | Unset): Day of month (1-31, or negative for counting from end: -1=last day)
        day_of_week (int | None | Unset): Day of week (0=Monday, 6=Sunday) for weekly schedules
        hour_of_day (int | None | Unset): Hour of day (0-23) for daily/weekly/monthly schedules
        minute_of_hour (int | None | Unset): Minute of hour (0-59) for all schedules
        repeat_interval (int | Unset): How often to repeat (e.g., every 2 days) Default: 1.
        weekday_of_month (int | None | Unset): Weekday of month (0=first Monday, 8=second Tuesday, etc.) for monthly
            schedules
    """

    frequency: AgentTriggerFrequency
    day_of_month: int | None | Unset = UNSET
    day_of_week: int | None | Unset = UNSET
    hour_of_day: int | None | Unset = UNSET
    minute_of_hour: int | None | Unset = UNSET
    repeat_interval: int | Unset = 1
    weekday_of_month: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequency = self.frequency.value

        day_of_month: int | None | Unset
        if isinstance(self.day_of_month, Unset):
            day_of_month = UNSET
        else:
            day_of_month = self.day_of_month

        day_of_week: int | None | Unset
        if isinstance(self.day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = self.day_of_week

        hour_of_day: int | None | Unset
        if isinstance(self.hour_of_day, Unset):
            hour_of_day = UNSET
        else:
            hour_of_day = self.hour_of_day

        minute_of_hour: int | None | Unset
        if isinstance(self.minute_of_hour, Unset):
            minute_of_hour = UNSET
        else:
            minute_of_hour = self.minute_of_hour

        repeat_interval = self.repeat_interval

        weekday_of_month: int | None | Unset
        if isinstance(self.weekday_of_month, Unset):
            weekday_of_month = UNSET
        else:
            weekday_of_month = self.weekday_of_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
            }
        )
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week
        if hour_of_day is not UNSET:
            field_dict["hour_of_day"] = hour_of_day
        if minute_of_hour is not UNSET:
            field_dict["minute_of_hour"] = minute_of_hour
        if repeat_interval is not UNSET:
            field_dict["repeat_interval"] = repeat_interval
        if weekday_of_month is not UNSET:
            field_dict["weekday_of_month"] = weekday_of_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequency = AgentTriggerFrequency(d.pop("frequency"))

        def _parse_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_of_month = _parse_day_of_month(d.pop("day_of_month", UNSET))

        def _parse_day_of_week(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_of_week = _parse_day_of_week(d.pop("day_of_week", UNSET))

        def _parse_hour_of_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hour_of_day = _parse_hour_of_day(d.pop("hour_of_day", UNSET))

        def _parse_minute_of_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minute_of_hour = _parse_minute_of_hour(d.pop("minute_of_hour", UNSET))

        repeat_interval = d.pop("repeat_interval", UNSET)

        def _parse_weekday_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weekday_of_month = _parse_weekday_of_month(d.pop("weekday_of_month", UNSET))

        create_trigger_schedule_request = cls(
            frequency=frequency,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            hour_of_day=hour_of_day,
            minute_of_hour=minute_of_hour,
            repeat_interval=repeat_interval,
            weekday_of_month=weekday_of_month,
        )

        create_trigger_schedule_request.additional_properties = d
        return create_trigger_schedule_request

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
