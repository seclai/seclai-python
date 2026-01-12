from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KnowledgeBaseContentVersionResponse")


@_attrs_define
class KnowledgeBaseContentVersionResponse:
    """
    Attributes:
        id (UUID):
        published_at (None | str):
        source_name (str):
        status (str):
        title (None | str):
        url (None | str):
    """

    id: UUID
    published_at: None | str
    source_name: str
    status: str
    title: None | str
    url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        published_at: None | str
        published_at = self.published_at

        source_name = self.source_name

        status = self.status

        title: None | str
        title = self.title

        url: None | str
        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "published_at": published_at,
                "source_name": source_name,
                "status": status,
                "title": title,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        source_name = d.pop("source_name")

        status = d.pop("status")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        knowledge_base_content_version_response = cls(
            id=id,
            published_at=published_at,
            source_name=source_name,
            status=status,
            title=title,
            url=url,
        )

        knowledge_base_content_version_response.additional_properties = d
        return knowledge_base_content_version_response

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
