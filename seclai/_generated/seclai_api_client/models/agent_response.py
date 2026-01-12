from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch_summary_response import BranchSummaryResponse


T = TypeVar("T", bound="AgentResponse")


@_attrs_define
class AgentResponse:
    """Response model for agent data

    Attributes:
        branches (list[BranchSummaryResponse]):
        created_at (str):
        description (None | str):
        id (UUID):
        name (str):
        updated_at (str):
        has_scheduled_runs (bool | Unset):  Default: False.
        trigger_type (None | str | Unset):
    """

    branches: list[BranchSummaryResponse]
    created_at: str
    description: None | str
    id: UUID
    name: str
    updated_at: str
    has_scheduled_runs: bool | Unset = False
    trigger_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)

        created_at = self.created_at

        description: None | str
        description = self.description

        id = str(self.id)

        name = self.name

        updated_at = self.updated_at

        has_scheduled_runs = self.has_scheduled_runs

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branches": branches,
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )
        if has_scheduled_runs is not UNSET:
            field_dict["has_scheduled_runs"] = has_scheduled_runs
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch_summary_response import BranchSummaryResponse

        d = dict(src_dict)
        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = BranchSummaryResponse.from_dict(branches_item_data)

            branches.append(branches_item)

        created_at = d.pop("created_at")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        updated_at = d.pop("updated_at")

        has_scheduled_runs = d.pop("has_scheduled_runs", UNSET)

        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        agent_response = cls(
            branches=branches,
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            updated_at=updated_at,
            has_scheduled_runs=has_scheduled_runs,
            trigger_type=trigger_type,
        )

        agent_response.additional_properties = d
        return agent_response

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
