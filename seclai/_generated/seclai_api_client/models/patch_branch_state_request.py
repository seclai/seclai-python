from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_branch_state_request_data_type_0 import PatchBranchStateRequestDataType0


T = TypeVar("T", bound="PatchBranchStateRequest")


@_attrs_define
class PatchBranchStateRequest:
    """Request model for patching a branch's current state

    Attributes:
        action (str): The operation to perform: 'update_fields', 'insert_between', 'add_sibling', 'delete', or
            'delete_and_move_children_up'
        change_id (UUID): The expected current change_id (for optimistic locking)
        step_path (str): JSON path to the target location (e.g., 'agent', 'agent.steps[0]')
        data (None | PatchBranchStateRequestDataType0 | Unset): The data for the operation (required for update_fields,
            insert_between, add_sibling)
    """

    action: str
    change_id: UUID
    step_path: str
    data: None | PatchBranchStateRequestDataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_branch_state_request_data_type_0 import PatchBranchStateRequestDataType0

        action = self.action

        change_id = str(self.change_id)

        step_path = self.step_path

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, PatchBranchStateRequestDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "change_id": change_id,
                "step_path": step_path,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_branch_state_request_data_type_0 import PatchBranchStateRequestDataType0

        d = dict(src_dict)
        action = d.pop("action")

        change_id = UUID(d.pop("change_id"))

        step_path = d.pop("step_path")

        def _parse_data(data: object) -> None | PatchBranchStateRequestDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = PatchBranchStateRequestDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchBranchStateRequestDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        patch_branch_state_request = cls(
            action=action,
            change_id=change_id,
            step_path=step_path,
            data=data,
        )

        patch_branch_state_request.additional_properties = d
        return patch_branch_state_request

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
