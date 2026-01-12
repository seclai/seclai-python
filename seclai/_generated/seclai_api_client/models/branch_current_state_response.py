from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_warning_model import AgentWarningModel
    from ..models.branch_current_state_response_definition import BranchCurrentStateResponseDefinition
    from ..models.branch_current_state_response_dependencies_type_0 import BranchCurrentStateResponseDependenciesType0


T = TypeVar("T", bound="BranchCurrentStateResponse")


@_attrs_define
class BranchCurrentStateResponse:
    """Response model for branch current state data

    Attributes:
        branch_id (UUID):
        branch_name (str):
        change_id (UUID):
        created_at (str):
        definition (BranchCurrentStateResponseDefinition):
        schema_version (str):
        user_id (UUID):
        user_name (None | str):
        dependencies (BranchCurrentStateResponseDependenciesType0 | None | Unset):
        success (bool | Unset):  Default: True.
        trigger_type (None | str | Unset):
        warnings (list[AgentWarningModel] | None | Unset):
    """

    branch_id: UUID
    branch_name: str
    change_id: UUID
    created_at: str
    definition: BranchCurrentStateResponseDefinition
    schema_version: str
    user_id: UUID
    user_name: None | str
    dependencies: BranchCurrentStateResponseDependenciesType0 | None | Unset = UNSET
    success: bool | Unset = True
    trigger_type: None | str | Unset = UNSET
    warnings: list[AgentWarningModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.branch_current_state_response_dependencies_type_0 import (
            BranchCurrentStateResponseDependenciesType0,
        )

        branch_id = str(self.branch_id)

        branch_name = self.branch_name

        change_id = str(self.change_id)

        created_at = self.created_at

        definition = self.definition.to_dict()

        schema_version = self.schema_version

        user_id = str(self.user_id)

        user_name: None | str
        user_name = self.user_name

        dependencies: dict[str, Any] | None | Unset
        if isinstance(self.dependencies, Unset):
            dependencies = UNSET
        elif isinstance(self.dependencies, BranchCurrentStateResponseDependenciesType0):
            dependencies = self.dependencies.to_dict()
        else:
            dependencies = self.dependencies

        success = self.success

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type

        warnings: list[dict[str, Any]] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch_id": branch_id,
                "branch_name": branch_name,
                "change_id": change_id,
                "created_at": created_at,
                "definition": definition,
                "schema_version": schema_version,
                "user_id": user_id,
                "user_name": user_name,
            }
        )
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if success is not UNSET:
            field_dict["success"] = success
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_warning_model import AgentWarningModel
        from ..models.branch_current_state_response_definition import BranchCurrentStateResponseDefinition
        from ..models.branch_current_state_response_dependencies_type_0 import (
            BranchCurrentStateResponseDependenciesType0,
        )

        d = dict(src_dict)
        branch_id = UUID(d.pop("branch_id"))

        branch_name = d.pop("branch_name")

        change_id = UUID(d.pop("change_id"))

        created_at = d.pop("created_at")

        definition = BranchCurrentStateResponseDefinition.from_dict(d.pop("definition"))

        schema_version = d.pop("schema_version")

        user_id = UUID(d.pop("user_id"))

        def _parse_user_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_name = _parse_user_name(d.pop("user_name"))

        def _parse_dependencies(data: object) -> BranchCurrentStateResponseDependenciesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dependencies_type_0 = BranchCurrentStateResponseDependenciesType0.from_dict(data)

                return dependencies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BranchCurrentStateResponseDependenciesType0 | None | Unset, data)

        dependencies = _parse_dependencies(d.pop("dependencies", UNSET))

        success = d.pop("success", UNSET)

        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        def _parse_warnings(data: object) -> list[AgentWarningModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in _warnings_type_0:
                    warnings_type_0_item = AgentWarningModel.from_dict(warnings_type_0_item_data)

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentWarningModel] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        branch_current_state_response = cls(
            branch_id=branch_id,
            branch_name=branch_name,
            change_id=change_id,
            created_at=created_at,
            definition=definition,
            schema_version=schema_version,
            user_id=user_id,
            user_name=user_name,
            dependencies=dependencies,
            success=success,
            trigger_type=trigger_type,
            warnings=warnings,
        )

        branch_current_state_response.additional_properties = d
        return branch_current_state_response

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
