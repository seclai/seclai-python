from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiAssistantAcceptRequest")


@_attrs_define
class AiAssistantAcceptRequest:
    """Request body for accepting a proposed plan.

    Attributes:
        confirm_deletions (bool | Unset): Must be true when the plan contains destructive actions Default: False.
        solution_description (None | str | Unset): When running in standalone mode (no pre-existing solution), provide a
            description for the auto-created solution.
        solution_name (None | str | Unset): When running in standalone mode (no pre-existing solution), provide a name
            to auto-create a solution and link resources.
    """

    confirm_deletions: bool | Unset = False
    solution_description: None | str | Unset = UNSET
    solution_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirm_deletions = self.confirm_deletions

        solution_description: None | str | Unset
        if isinstance(self.solution_description, Unset):
            solution_description = UNSET
        else:
            solution_description = self.solution_description

        solution_name: None | str | Unset
        if isinstance(self.solution_name, Unset):
            solution_name = UNSET
        else:
            solution_name = self.solution_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirm_deletions is not UNSET:
            field_dict["confirm_deletions"] = confirm_deletions
        if solution_description is not UNSET:
            field_dict["solution_description"] = solution_description
        if solution_name is not UNSET:
            field_dict["solution_name"] = solution_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirm_deletions = d.pop("confirm_deletions", UNSET)

        def _parse_solution_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        solution_description = _parse_solution_description(
            d.pop("solution_description", UNSET)
        )

        def _parse_solution_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        solution_name = _parse_solution_name(d.pop("solution_name", UNSET))

        ai_assistant_accept_request = cls(
            confirm_deletions=confirm_deletions,
            solution_description=solution_description,
            solution_name=solution_name,
        )

        ai_assistant_accept_request.additional_properties = d
        return ai_assistant_accept_request

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
