from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_branch_state_request_definition import UpdateBranchStateRequestDefinition


T = TypeVar("T", bound="UpdateBranchStateRequest")


@_attrs_define
class UpdateBranchStateRequest:
    """Request model for updating a branch's current state

    Attributes:
        change_id (UUID): The expected current change_id (for optimistic locking)
        definition (UpdateBranchStateRequestDefinition): The new agent definition
    """

    change_id: UUID
    definition: UpdateBranchStateRequestDefinition
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = str(self.change_id)

        definition = self.definition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "change_id": change_id,
                "definition": definition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_branch_state_request_definition import UpdateBranchStateRequestDefinition

        d = dict(src_dict)
        change_id = UUID(d.pop("change_id"))

        definition = UpdateBranchStateRequestDefinition.from_dict(d.pop("definition"))

        update_branch_state_request = cls(
            change_id=change_id,
            definition=definition,
        )

        update_branch_state_request.additional_properties = d
        return update_branch_state_request

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
