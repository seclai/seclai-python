from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ConversationData")


@_attrs_define
class ConversationData:
    """
    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        knowledge_base_id (UUID):
        title (None | str):
        updated_at (datetime.datetime):
        user_id (UUID):
    """

    created_at: datetime.datetime
    id: UUID
    knowledge_base_id: UUID
    title: None | str
    updated_at: datetime.datetime
    user_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        knowledge_base_id = str(self.knowledge_base_id)

        title: None | str
        title = self.title

        updated_at = self.updated_at.isoformat()

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "knowledge_base_id": knowledge_base_id,
                "title": title,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        id = UUID(d.pop("id"))

        knowledge_base_id = UUID(d.pop("knowledge_base_id"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        updated_at = isoparse(d.pop("updated_at"))

        user_id = UUID(d.pop("user_id"))

        conversation_data = cls(
            created_at=created_at,
            id=id,
            knowledge_base_id=knowledge_base_id,
            title=title,
            updated_at=updated_at,
            user_id=user_id,
        )

        conversation_data.additional_properties = d
        return conversation_data

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
