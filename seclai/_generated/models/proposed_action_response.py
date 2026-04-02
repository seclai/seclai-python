from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposed_action_response_params import ProposedActionResponseParams


T = TypeVar("T", bound="ProposedActionResponse")


@_attrs_define
class ProposedActionResponse:
    """A single proposed action.

    Attributes:
        action_type (str): Type of the proposed action.
        description (str): Human-readable description of the action.
        params (ProposedActionResponseParams): Parameters for the action.
        is_destructive (bool | Unset): Whether the action is destructive. Default: False.
    """

    action_type: str
    description: str
    params: ProposedActionResponseParams
    is_destructive: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        description = self.description

        params = self.params.to_dict()

        is_destructive = self.is_destructive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "description": description,
                "params": params,
            }
        )
        if is_destructive is not UNSET:
            field_dict["is_destructive"] = is_destructive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposed_action_response_params import (
            ProposedActionResponseParams,
        )

        d = dict(src_dict)
        action_type = d.pop("action_type")

        description = d.pop("description")

        params = ProposedActionResponseParams.from_dict(d.pop("params"))

        is_destructive = d.pop("is_destructive", UNSET)

        proposed_action_response = cls(
            action_type=action_type,
            description=description,
            params=params,
            is_destructive=is_destructive,
        )

        proposed_action_response.additional_properties = d
        return proposed_action_response

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
