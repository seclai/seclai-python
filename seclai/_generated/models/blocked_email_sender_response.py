from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BlockedEmailSenderResponse")


@_attrs_define
class BlockedEmailSenderResponse:
    """A single blocked inbound email sender.

    Attributes:
        created_at (str):
        id (UUID):
        match_type (str):
        note (None | str):
        sender_email (str):
        source (str):
    """

    created_at: str
    id: UUID
    match_type: str
    note: None | str
    sender_email: str
    source: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = str(self.id)

        match_type = self.match_type

        note: None | str
        note = self.note

        sender_email = self.sender_email

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "match_type": match_type,
                "note": note,
                "sender_email": sender_email,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        match_type = d.pop("match_type")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        sender_email = d.pop("sender_email")

        source = d.pop("source")

        blocked_email_sender_response = cls(
            created_at=created_at,
            id=id,
            match_type=match_type,
            note=note,
            sender_email=sender_email,
            source=source,
        )

        blocked_email_sender_response.additional_properties = d
        return blocked_email_sender_response

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
