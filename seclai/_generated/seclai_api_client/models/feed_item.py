from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FeedItem")


@_attrs_define
class FeedItem:
    """Information about a single feed item.

    Attributes:
        guid (str):
        published_at (None | str):
        title (None | str):
    """

    guid: str
    published_at: None | str
    title: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        published_at: None | str
        published_at = self.published_at

        title: None | str
        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guid": guid,
                "published_at": published_at,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guid = d.pop("guid")

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        feed_item = cls(
            guid=guid,
            published_at=published_at,
            title=title,
        )

        feed_item.additional_properties = d
        return feed_item

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
