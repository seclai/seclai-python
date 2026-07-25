from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InboundEmailRejectionResponse")


@_attrs_define
class InboundEmailRejectionResponse:
    """An inbound email that was discarded without running an agent.

    Attributes:
        agent_id (None | UUID):
        created_at (str):
        id (UUID):
        message_id (None | str):
        reason (str):
        recipient (str):
        sender (str):
        sender_ip (None | str):
        subject (None | str):
    """

    agent_id: None | UUID
    created_at: str
    id: UUID
    message_id: None | str
    reason: str
    recipient: str
    sender: str
    sender_ip: None | str
    subject: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id: None | str
        if isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        created_at = self.created_at

        id = str(self.id)

        message_id: None | str
        message_id = self.message_id

        reason = self.reason

        recipient = self.recipient

        sender = self.sender

        sender_ip: None | str
        sender_ip = self.sender_ip

        subject: None | str
        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "created_at": created_at,
                "id": id,
                "message_id": message_id,
                "reason": reason,
                "recipient": recipient,
                "sender": sender,
                "sender_ip": sender_ip,
                "subject": subject,
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

        created_at = d.pop("created_at")

        id = UUID(d.pop("id"))

        def _parse_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message_id = _parse_message_id(d.pop("message_id"))

        reason = d.pop("reason")

        recipient = d.pop("recipient")

        sender = d.pop("sender")

        def _parse_sender_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sender_ip = _parse_sender_ip(d.pop("sender_ip"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        inbound_email_rejection_response = cls(
            agent_id=agent_id,
            created_at=created_at,
            id=id,
            message_id=message_id,
            reason=reason,
            recipient=recipient,
            sender=sender,
            sender_ip=sender_ip,
            subject=subject,
        )

        inbound_email_rejection_response.additional_properties = d
        return inbound_email_rejection_response

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
