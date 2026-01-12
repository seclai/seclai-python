from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BranchSummaryResponse")


@_attrs_define
class BranchSummaryResponse:
    """Response model for branch summary data

    Attributes:
        id (UUID):
        most_recent_change_at (None | str):
        most_recent_commit_at (None | str):
        name (str):
    """

    id: UUID
    most_recent_change_at: None | str
    most_recent_commit_at: None | str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        most_recent_change_at: None | str
        most_recent_change_at = self.most_recent_change_at

        most_recent_commit_at: None | str
        most_recent_commit_at = self.most_recent_commit_at

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "most_recent_change_at": most_recent_change_at,
                "most_recent_commit_at": most_recent_commit_at,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_most_recent_change_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        most_recent_change_at = _parse_most_recent_change_at(d.pop("most_recent_change_at"))

        def _parse_most_recent_commit_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        most_recent_commit_at = _parse_most_recent_commit_at(d.pop("most_recent_commit_at"))

        name = d.pop("name")

        branch_summary_response = cls(
            id=id,
            most_recent_change_at=most_recent_change_at,
            most_recent_commit_at=most_recent_commit_at,
            name=name,
        )

        branch_summary_response.additional_properties = d
        return branch_summary_response

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
