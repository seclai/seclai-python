from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_filter_type import ContentFilterType
from ..models.polling_action import PollingAction
from ..models.polling_type import PollingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSourceRequest")


@_attrs_define
class UpdateSourceRequest:
    """Request model for updating an existing source

    Attributes:
        content_filter (ContentFilterType | None | Unset): Content filtering strategy
        name (None | str | Unset): Name of the source
        polling (None | PollingType | Unset): Polling frequency: once, hourly, daily, weekly Default: PollingType.DAILY.
        polling_action (None | PollingAction | Unset): Polling action to take
        polling_max_items (int | None | Unset): Maximum items to fetch per poll
        retention_days (int | None | Unset): Retention period in days (null for infinite)
    """

    content_filter: ContentFilterType | None | Unset = UNSET
    name: None | str | Unset = UNSET
    polling: None | PollingType | Unset = PollingType.DAILY
    polling_action: None | PollingAction | Unset = UNSET
    polling_max_items: int | None | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_filter: None | str | Unset
        if isinstance(self.content_filter, Unset):
            content_filter = UNSET
        elif isinstance(self.content_filter, ContentFilterType):
            content_filter = self.content_filter.value
        else:
            content_filter = self.content_filter

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        polling: None | str | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        elif isinstance(self.polling, PollingType):
            polling = self.polling.value
        else:
            polling = self.polling

        polling_action: None | str | Unset
        if isinstance(self.polling_action, Unset):
            polling_action = UNSET
        elif isinstance(self.polling_action, PollingAction):
            polling_action = self.polling_action.value
        else:
            polling_action = self.polling_action

        polling_max_items: int | None | Unset
        if isinstance(self.polling_max_items, Unset):
            polling_max_items = UNSET
        else:
            polling_max_items = self.polling_max_items

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_filter is not UNSET:
            field_dict["content_filter"] = content_filter
        if name is not UNSET:
            field_dict["name"] = name
        if polling is not UNSET:
            field_dict["polling"] = polling
        if polling_action is not UNSET:
            field_dict["polling_action"] = polling_action
        if polling_max_items is not UNSET:
            field_dict["polling_max_items"] = polling_max_items
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content_filter(data: object) -> ContentFilterType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                content_filter_type_0 = ContentFilterType(data)

                return content_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContentFilterType | None | Unset, data)

        content_filter = _parse_content_filter(d.pop("content_filter", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_polling(data: object) -> None | PollingType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                polling_type_0 = PollingType(data)

                return polling_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollingType | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        def _parse_polling_action(data: object) -> None | PollingAction | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                polling_action_type_0 = PollingAction(data)

                return polling_action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollingAction | Unset, data)

        polling_action = _parse_polling_action(d.pop("polling_action", UNSET))

        def _parse_polling_max_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        polling_max_items = _parse_polling_max_items(d.pop("polling_max_items", UNSET))

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        update_source_request = cls(
            content_filter=content_filter,
            name=name,
            polling=polling,
            polling_action=polling_action,
            polling_max_items=polling_max_items,
            retention_days=retention_days,
        )

        update_source_request.additional_properties = d
        return update_source_request

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
