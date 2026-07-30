from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiVersionResponse")


@_attrs_define
class ApiVersionResponse:
    """
    Attributes:
        default_version (str): Baseline for an unpinned, header-less caller.
        effective_version (str): The version THIS request resolved to (header > pin > default).
        known_versions (list[str]): All dated versions, oldest first.
        latest_version (str): Newest version the server knows about.
        pinned_version (None | str): The account's sticky pinned version, or null when unpinned (the account resolves to
            the default). Applies to header-less requests.
    """

    default_version: str
    effective_version: str
    known_versions: list[str]
    latest_version: str
    pinned_version: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_version = self.default_version

        effective_version = self.effective_version

        known_versions = self.known_versions

        latest_version = self.latest_version

        pinned_version: None | str
        pinned_version = self.pinned_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_version": default_version,
                "effective_version": effective_version,
                "known_versions": known_versions,
                "latest_version": latest_version,
                "pinned_version": pinned_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_version = d.pop("default_version")

        effective_version = d.pop("effective_version")

        known_versions = cast(list[str], d.pop("known_versions"))

        latest_version = d.pop("latest_version")

        def _parse_pinned_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pinned_version = _parse_pinned_version(d.pop("pinned_version"))

        api_version_response = cls(
            default_version=default_version,
            effective_version=effective_version,
            known_versions=known_versions,
            latest_version=latest_version,
            pinned_version=pinned_version,
        )

        api_version_response.additional_properties = d
        return api_version_response

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
