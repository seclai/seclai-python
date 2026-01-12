from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceConnectionResponse")


@_attrs_define
class SourceConnectionResponse:
    """Response model for source connection information

    Attributes:
        id (UUID):
        name (str):
        source_type (str):
        url (str):
        polling (None | str | Unset):
    """

    id: UUID
    name: str
    source_type: str
    url: str
    polling: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        source_type = self.source_type

        url = self.url

        polling: None | str | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        else:
            polling = self.polling

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "source_type": source_type,
                "url": url,
            }
        )
        if polling is not UNSET:
            field_dict["polling"] = polling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        source_type = d.pop("source_type")

        url = d.pop("url")

        def _parse_polling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        source_connection_response = cls(
            id=id,
            name=name,
            source_type=source_type,
            url=url,
            polling=polling,
        )

        source_connection_response.additional_properties = d
        return source_connection_response

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
