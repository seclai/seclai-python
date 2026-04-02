from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposed_policy_action_response_params import (
        ProposedPolicyActionResponseParams,
    )


T = TypeVar("T", bound="ProposedPolicyActionResponse")


@_attrs_define
class ProposedPolicyActionResponse:
    """A single proposed governance policy action.

    Attributes:
        action_type (str): Type of action: create, update, delete, enable, or disable.
        description (str): Human-readable description of what this action will do.
        params (ProposedPolicyActionResponseParams): Parameters for the action (e.g. policy_document_id, thresholds).
    """

    action_type: str
    description: str
    params: ProposedPolicyActionResponseParams
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        description = self.description

        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "description": description,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposed_policy_action_response_params import (
            ProposedPolicyActionResponseParams,
        )

        d = dict(src_dict)
        action_type = d.pop("action_type")

        description = d.pop("description")

        params = ProposedPolicyActionResponseParams.from_dict(d.pop("params"))

        proposed_policy_action_response = cls(
            action_type=action_type,
            description=description,
            params=params,
        )

        proposed_policy_action_response.additional_properties = d
        return proposed_policy_action_response

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
