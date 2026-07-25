from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailTriggerConfigResponse")


@_attrs_define
class EmailTriggerConfigResponse:
    """An EMAIL_RECEIVED trigger's resolved address(es) and config.

    Attributes:
        agent_id (UUID):
        trigger_id (UUID):
        trigger_type (str):
        email_addresses (list[str] | Unset):
        email_alias (None | str | Unset):
        email_allowed_senders (list[str] | None | Unset):
        email_ignore_auto_generated (bool | Unset):  Default: True.
        email_queue_on_quota (bool | Unset):  Default: False.
        email_require_sender_auth (bool | Unset):  Default: True.
    """

    agent_id: UUID
    trigger_id: UUID
    trigger_type: str
    email_addresses: list[str] | Unset = UNSET
    email_alias: None | str | Unset = UNSET
    email_allowed_senders: list[str] | None | Unset = UNSET
    email_ignore_auto_generated: bool | Unset = True
    email_queue_on_quota: bool | Unset = False
    email_require_sender_auth: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        trigger_id = str(self.trigger_id)

        trigger_type = self.trigger_type

        email_addresses: list[str] | Unset = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = self.email_addresses

        email_alias: None | str | Unset
        if isinstance(self.email_alias, Unset):
            email_alias = UNSET
        else:
            email_alias = self.email_alias

        email_allowed_senders: list[str] | None | Unset
        if isinstance(self.email_allowed_senders, Unset):
            email_allowed_senders = UNSET
        elif isinstance(self.email_allowed_senders, list):
            email_allowed_senders = self.email_allowed_senders

        else:
            email_allowed_senders = self.email_allowed_senders

        email_ignore_auto_generated = self.email_ignore_auto_generated

        email_queue_on_quota = self.email_queue_on_quota

        email_require_sender_auth = self.email_require_sender_auth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "trigger_id": trigger_id,
                "trigger_type": trigger_type,
            }
        )
        if email_addresses is not UNSET:
            field_dict["email_addresses"] = email_addresses
        if email_alias is not UNSET:
            field_dict["email_alias"] = email_alias
        if email_allowed_senders is not UNSET:
            field_dict["email_allowed_senders"] = email_allowed_senders
        if email_ignore_auto_generated is not UNSET:
            field_dict["email_ignore_auto_generated"] = email_ignore_auto_generated
        if email_queue_on_quota is not UNSET:
            field_dict["email_queue_on_quota"] = email_queue_on_quota
        if email_require_sender_auth is not UNSET:
            field_dict["email_require_sender_auth"] = email_require_sender_auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        trigger_id = UUID(d.pop("trigger_id"))

        trigger_type = d.pop("trigger_type")

        email_addresses = cast(list[str], d.pop("email_addresses", UNSET))

        def _parse_email_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_alias = _parse_email_alias(d.pop("email_alias", UNSET))

        def _parse_email_allowed_senders(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                email_allowed_senders_type_0 = cast(list[str], data)

                return email_allowed_senders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        email_allowed_senders = _parse_email_allowed_senders(
            d.pop("email_allowed_senders", UNSET)
        )

        email_ignore_auto_generated = d.pop("email_ignore_auto_generated", UNSET)

        email_queue_on_quota = d.pop("email_queue_on_quota", UNSET)

        email_require_sender_auth = d.pop("email_require_sender_auth", UNSET)

        email_trigger_config_response = cls(
            agent_id=agent_id,
            trigger_id=trigger_id,
            trigger_type=trigger_type,
            email_addresses=email_addresses,
            email_alias=email_alias,
            email_allowed_senders=email_allowed_senders,
            email_ignore_auto_generated=email_ignore_auto_generated,
            email_queue_on_quota=email_queue_on_quota,
            email_require_sender_auth=email_require_sender_auth,
        )

        email_trigger_config_response.additional_properties = d
        return email_trigger_config_response

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
