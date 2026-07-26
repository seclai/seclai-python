from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetEmailTriggerConfigRequest")


@_attrs_define
class SetEmailTriggerConfigRequest:
    """Alias and/or sender allowlist for an EMAIL_RECEIVED trigger.

    A field omitted is left unchanged; passing ``null`` (or ``""`` for
    ``alias``) clears it.

        Attributes:
            alias (None | str | Unset): Custom alias for the address `<alias>.<accountID>@agent.seclai.com` (alphanumeric
                plus '+', '.', '-'; 1–32 chars; not starting/ending with '+', '.', '-'; not UUID-shaped). Pass null/empty to
                clear.
            allowed_senders (list[str] | None | Unset): Allowlist of full sender addresses and/or bare domains (a bare
                domain also matches sub-domains). Empty/null accepts any sender.
            ignore_auto_generated (bool | None | Unset): When true (default for new triggers), machine-generated inbound
                mail (auto-replies, bulk/list mail, bounces) is dropped before a run to prevent auto-reply loops. Set false to
                process automated mail.
            queue_on_quota (bool | None | Unset): When true (default false), inbound mail that exceeds the account's hourly
                email-trigger rate is parked in a QUEUED run and drained later by the catch-up sweep instead of being failed;
                when false, over-rate mail fails immediately.
            require_sender_auth (bool | None | Unset): When true (default for new triggers), the envelope sender must pass
                SPF or DMARC even on an open inbox (no allowlist); unauthenticated, spoofable mail is rejected. Set false to
                accept fully unauthenticated mail on an open inbox.
    """

    alias: None | str | Unset = UNSET
    allowed_senders: list[str] | None | Unset = UNSET
    ignore_auto_generated: bool | None | Unset = UNSET
    queue_on_quota: bool | None | Unset = UNSET
    require_sender_auth: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        allowed_senders: list[str] | None | Unset
        if isinstance(self.allowed_senders, Unset):
            allowed_senders = UNSET
        elif isinstance(self.allowed_senders, list):
            allowed_senders = self.allowed_senders

        else:
            allowed_senders = self.allowed_senders

        ignore_auto_generated: bool | None | Unset
        if isinstance(self.ignore_auto_generated, Unset):
            ignore_auto_generated = UNSET
        else:
            ignore_auto_generated = self.ignore_auto_generated

        queue_on_quota: bool | None | Unset
        if isinstance(self.queue_on_quota, Unset):
            queue_on_quota = UNSET
        else:
            queue_on_quota = self.queue_on_quota

        require_sender_auth: bool | None | Unset
        if isinstance(self.require_sender_auth, Unset):
            require_sender_auth = UNSET
        else:
            require_sender_auth = self.require_sender_auth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if allowed_senders is not UNSET:
            field_dict["allowed_senders"] = allowed_senders
        if ignore_auto_generated is not UNSET:
            field_dict["ignore_auto_generated"] = ignore_auto_generated
        if queue_on_quota is not UNSET:
            field_dict["queue_on_quota"] = queue_on_quota
        if require_sender_auth is not UNSET:
            field_dict["require_sender_auth"] = require_sender_auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_allowed_senders(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_senders_type_0 = cast(list[str], data)

                return allowed_senders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_senders = _parse_allowed_senders(d.pop("allowed_senders", UNSET))

        def _parse_ignore_auto_generated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_auto_generated = _parse_ignore_auto_generated(
            d.pop("ignore_auto_generated", UNSET)
        )

        def _parse_queue_on_quota(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        queue_on_quota = _parse_queue_on_quota(d.pop("queue_on_quota", UNSET))

        def _parse_require_sender_auth(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_sender_auth = _parse_require_sender_auth(
            d.pop("require_sender_auth", UNSET)
        )

        set_email_trigger_config_request = cls(
            alias=alias,
            allowed_senders=allowed_senders,
            ignore_auto_generated=ignore_auto_generated,
            queue_on_quota=queue_on_quota,
            require_sender_auth=require_sender_auth,
        )

        set_email_trigger_config_request.additional_properties = d
        return set_email_trigger_config_request

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
