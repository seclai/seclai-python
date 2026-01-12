from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RunAgentResponse")


@_attrs_define
class RunAgentResponse:
    """Response model for agent run

    Attributes:
        agent_id (UUID):
        message (str):
        run_id (UUID):
        status (str):
    """

    agent_id: UUID
    message: str
    run_id: UUID
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        message = self.message

        run_id = str(self.run_id)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "message": message,
                "run_id": run_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        message = d.pop("message")

        run_id = UUID(d.pop("run_id"))

        status = d.pop("status")

        run_agent_response = cls(
            agent_id=agent_id,
            message=message,
            run_id=run_id,
            status=status,
        )

        run_agent_response.additional_properties = d
        return run_agent_response

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
