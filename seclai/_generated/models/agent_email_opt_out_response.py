from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentEmailOptOutResponse")


@_attrs_define
class AgentEmailOptOutResponse:
    """A recipient's opt-out from an account's agent emails (one agent or all).

    Attributes:
        agent_id (None | UUID):
        agent_name (None | str):
        comment (None | str):
        created_at (str):
        id (UUID):
        reason (None | str):
        recipient_email (str):
    """

    agent_id: None | UUID
    agent_name: None | str
    comment: None | str
    created_at: str
    id: UUID
    reason: None | str
    recipient_email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id: None | str
        if isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        agent_name: None | str
        agent_name = self.agent_name

        comment: None | str
        comment = self.comment

        created_at = self.created_at

        id = str(self.id)

        reason: None | str
        reason = self.reason

        recipient_email = self.recipient_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_name": agent_name,
                "comment": comment,
                "created_at": created_at,
                "id": id,
                "reason": reason,
                "recipient_email": recipient_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)

                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        def _parse_agent_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_name = _parse_agent_name(d.pop("agent_name"))

        def _parse_comment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        comment = _parse_comment(d.pop("comment"))

        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        recipient_email = d.pop("recipient_email")

        agent_email_opt_out_response = cls(
            agent_id=agent_id,
            agent_name=agent_name,
            comment=comment,
            created_at=created_at,
            id=id,
            reason=reason,
            recipient_email=recipient_email,
        )

        agent_email_opt_out_response.additional_properties = d
        return agent_email_opt_out_response

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
