from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_provider_response import DnsProviderResponse
    from ..models.dns_record_response import DnsRecordResponse


T = TypeVar("T", bound="EmailDomainResponse")


@_attrs_define
class EmailDomainResponse:
    """
    Attributes:
        domain (str):
        id (UUID):
        is_primary (bool):
        kind (str):
        status (str):
        delegated (bool | Unset):  Default: False.
        dns_records (list[DnsRecordResponse] | Unset):
        error_message (None | str | Unset):
        last_checked_at (datetime.datetime | None | Unset):
        provider (DnsProviderResponse | None | Unset):
        regressing (bool | Unset):  Default: False.
        verified (bool | Unset):  Default: False.
        verified_at (datetime.datetime | None | Unset):
        zone_apex (str | Unset):  Default: ''.
    """

    domain: str
    id: UUID
    is_primary: bool
    kind: str
    status: str
    delegated: bool | Unset = False
    dns_records: list[DnsRecordResponse] | Unset = UNSET
    error_message: None | str | Unset = UNSET
    last_checked_at: datetime.datetime | None | Unset = UNSET
    provider: DnsProviderResponse | None | Unset = UNSET
    regressing: bool | Unset = False
    verified: bool | Unset = False
    verified_at: datetime.datetime | None | Unset = UNSET
    zone_apex: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dns_provider_response import DnsProviderResponse

        domain = self.domain

        id = str(self.id)

        is_primary = self.is_primary

        kind = self.kind

        status = self.status

        delegated = self.delegated

        dns_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_records, Unset):
            dns_records = []
            for dns_records_item_data in self.dns_records:
                dns_records_item = dns_records_item_data.to_dict()
                dns_records.append(dns_records_item)

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        last_checked_at: None | str | Unset
        if isinstance(self.last_checked_at, Unset):
            last_checked_at = UNSET
        elif isinstance(self.last_checked_at, datetime.datetime):
            last_checked_at = self.last_checked_at.isoformat()
        else:
            last_checked_at = self.last_checked_at

        provider: dict[str, Any] | None | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, DnsProviderResponse):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        regressing = self.regressing

        verified = self.verified

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        zone_apex = self.zone_apex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "id": id,
                "is_primary": is_primary,
                "kind": kind,
                "status": status,
            }
        )
        if delegated is not UNSET:
            field_dict["delegated"] = delegated
        if dns_records is not UNSET:
            field_dict["dns_records"] = dns_records
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if last_checked_at is not UNSET:
            field_dict["last_checked_at"] = last_checked_at
        if provider is not UNSET:
            field_dict["provider"] = provider
        if regressing is not UNSET:
            field_dict["regressing"] = regressing
        if verified is not UNSET:
            field_dict["verified"] = verified
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if zone_apex is not UNSET:
            field_dict["zone_apex"] = zone_apex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_provider_response import DnsProviderResponse
        from ..models.dns_record_response import DnsRecordResponse

        d = dict(src_dict)
        domain = d.pop("domain")

        id = UUID(d.pop("id"))

        is_primary = d.pop("is_primary")

        kind = d.pop("kind")

        status = d.pop("status")

        delegated = d.pop("delegated", UNSET)

        _dns_records = d.pop("dns_records", UNSET)
        dns_records: list[DnsRecordResponse] | Unset = UNSET
        if _dns_records is not UNSET:
            dns_records = []
            for dns_records_item_data in _dns_records:
                dns_records_item = DnsRecordResponse.from_dict(dns_records_item_data)

                dns_records.append(dns_records_item)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_last_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_checked_at_type_0 = isoparse(data)

                return last_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_checked_at = _parse_last_checked_at(d.pop("last_checked_at", UNSET))

        def _parse_provider(data: object) -> DnsProviderResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_0 = DnsProviderResponse.from_dict(data)

                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DnsProviderResponse | None | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        regressing = d.pop("regressing", UNSET)

        verified = d.pop("verified", UNSET)

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = isoparse(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        zone_apex = d.pop("zone_apex", UNSET)

        email_domain_response = cls(
            domain=domain,
            id=id,
            is_primary=is_primary,
            kind=kind,
            status=status,
            delegated=delegated,
            dns_records=dns_records,
            error_message=error_message,
            last_checked_at=last_checked_at,
            provider=provider,
            regressing=regressing,
            verified=verified,
            verified_at=verified_at,
            zone_apex=zone_apex,
        )

        email_domain_response.additional_properties = d
        return email_domain_response

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
