from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertHistoryEntryResponse")


@_attrs_define
class AlertHistoryEntryResponse:
    """
    Attributes:
        changed_by_name (None | str):
        changed_by_user_id (None | str):
        created_at (None | str):
        id (str):
        new_status (str):
        note (None | str):
        previous_status (None | str):
    """

    changed_by_name: None | str
    changed_by_user_id: None | str
    created_at: None | str
    id: str
    new_status: str
    note: None | str
    previous_status: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed_by_name: None | str
        changed_by_name = self.changed_by_name

        changed_by_user_id: None | str
        changed_by_user_id = self.changed_by_user_id

        created_at: None | str
        created_at = self.created_at

        id = self.id

        new_status = self.new_status

        note: None | str
        note = self.note

        previous_status: None | str
        previous_status = self.previous_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed_by_name": changed_by_name,
                "changed_by_user_id": changed_by_user_id,
                "created_at": created_at,
                "id": id,
                "new_status": new_status,
                "note": note,
                "previous_status": previous_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_changed_by_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        changed_by_name = _parse_changed_by_name(d.pop("changed_by_name"))

        def _parse_changed_by_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        changed_by_user_id = _parse_changed_by_user_id(d.pop("changed_by_user_id"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        id = d.pop("id")

        new_status = d.pop("new_status")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        def _parse_previous_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous_status = _parse_previous_status(d.pop("previous_status"))

        alert_history_entry_response = cls(
            changed_by_name=changed_by_name,
            changed_by_user_id=changed_by_user_id,
            created_at=created_at,
            id=id,
            new_status=new_status,
            note=note,
            previous_status=previous_status,
        )

        alert_history_entry_response.additional_properties = d
        return alert_history_entry_response

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
