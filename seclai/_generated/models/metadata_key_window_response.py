from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.metadata_key_window_response_window import MetadataKeyWindowResponseWindow

if TYPE_CHECKING:
    from ..models.metadata_key_count_response import MetadataKeyCountResponse


T = TypeVar("T", bound="MetadataKeyWindowResponse")


@_attrs_define
class MetadataKeyWindowResponse:
    """
    Attributes:
        keys (list[MetadataKeyCountResponse]): Keys seen in the window, most frequent first.
        since (datetime.datetime | None): The window's start; null for all time.
        total_items (int): Items in the window.
        window (MetadataKeyWindowResponseWindow):
    """

    keys: list[MetadataKeyCountResponse]
    since: datetime.datetime | None
    total_items: int
    window: MetadataKeyWindowResponseWindow
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)

        since: None | str
        if isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since

        total_items = self.total_items

        window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
                "since": since,
                "total_items": total_items,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_key_count_response import MetadataKeyCountResponse

        d = dict(src_dict)
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = MetadataKeyCountResponse.from_dict(keys_item_data)

            keys.append(keys_item)

        def _parse_since(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = isoparse(data)

                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        since = _parse_since(d.pop("since"))

        total_items = d.pop("total_items")

        window = MetadataKeyWindowResponseWindow(d.pop("window"))

        metadata_key_window_response = cls(
            keys=keys,
            since=since,
            total_items=total_items,
            window=window,
        )

        metadata_key_window_response.additional_properties = d
        return metadata_key_window_response

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
