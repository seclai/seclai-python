from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_source_rejection_response_auth_verdicts import (
        EmailSourceRejectionResponseAuthVerdicts,
    )


T = TypeVar("T", bound="EmailSourceRejectionResponse")


@_attrs_define
class EmailSourceRejectionResponse:
    """Mail an email content source refused: who sent it and why, never what
    it said.

        Attributes:
            authenticated (bool): Whether the message passed DMARC, which is what authenticates its From address. Adding an
                unauthenticated sender to the allowed senders does not let its mail in.
            created_at (str): When the mail was refused.
            id (str): Unique identifier of the refusal.
            reason (str): Why it was refused: sender_not_allowed, unauthenticated_sender, unreadable_from, sender_blocked,
                spam, virus, unsafe_content, rate_limited, account_not_chargeable or empty_message; or, for a message the source
                received before, what became of the earlier one: repeat_stored, repeat_held, repeat_deleted or
                repeat_in_progress.
            recipient (str): The source address it was sent to.
            sender (str): The envelope sender. For bulk mail this is the delivery provider's bounce address, not the From
                address.
            sender_ip (None | str): IP address the mail came from.
            auth_verdicts (EmailSourceRejectionResponseAuthVerdicts | Unset): The SPF, DKIM and DMARC verdicts reported for
                the message.
            from_address (None | str | Unset): The address in the message's From line, which the source's allowed senders
                are matched against. Null when no single From address could be read from the message unambiguously.
    """

    authenticated: bool
    created_at: str
    id: str
    reason: str
    recipient: str
    sender: str
    sender_ip: None | str
    auth_verdicts: EmailSourceRejectionResponseAuthVerdicts | Unset = UNSET
    from_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authenticated = self.authenticated

        created_at = self.created_at

        id = self.id

        reason = self.reason

        recipient = self.recipient

        sender = self.sender

        sender_ip: None | str
        sender_ip = self.sender_ip

        auth_verdicts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_verdicts, Unset):
            auth_verdicts = self.auth_verdicts.to_dict()

        from_address: None | str | Unset
        if isinstance(self.from_address, Unset):
            from_address = UNSET
        else:
            from_address = self.from_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authenticated": authenticated,
                "created_at": created_at,
                "id": id,
                "reason": reason,
                "recipient": recipient,
                "sender": sender,
                "sender_ip": sender_ip,
            }
        )
        if auth_verdicts is not UNSET:
            field_dict["auth_verdicts"] = auth_verdicts
        if from_address is not UNSET:
            field_dict["from_address"] = from_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_source_rejection_response_auth_verdicts import (
            EmailSourceRejectionResponseAuthVerdicts,
        )

        d = dict(src_dict)
        authenticated = d.pop("authenticated")

        created_at = d.pop("created_at")

        id = d.pop("id")

        reason = d.pop("reason")

        recipient = d.pop("recipient")

        sender = d.pop("sender")

        def _parse_sender_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sender_ip = _parse_sender_ip(d.pop("sender_ip"))

        _auth_verdicts = d.pop("auth_verdicts", UNSET)
        auth_verdicts: EmailSourceRejectionResponseAuthVerdicts | Unset
        if isinstance(_auth_verdicts, Unset):
            auth_verdicts = UNSET
        else:
            auth_verdicts = EmailSourceRejectionResponseAuthVerdicts.from_dict(
                _auth_verdicts
            )

        def _parse_from_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_address = _parse_from_address(d.pop("from_address", UNSET))

        email_source_rejection_response = cls(
            authenticated=authenticated,
            created_at=created_at,
            id=id,
            reason=reason,
            recipient=recipient,
            sender=sender,
            sender_ip=sender_ip,
            auth_verdicts=auth_verdicts,
            from_address=from_address,
        )

        email_source_rejection_response.additional_properties = d
        return email_source_rejection_response

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
