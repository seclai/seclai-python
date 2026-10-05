from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDriveUpdateRequest")


@_attrs_define
class CloudDriveUpdateRequest:
    """
    Attributes:
        folder_path (None | str | Unset): New watched folder; empty means the whole drive. A folder on a shared drive is
            written `/Shared drives/<drive name>/<folder>`. Changing it resets the sync cursor, so files already in the new
            folder are NOT replayed as triggers — only subsequent changes fire, matching connect-time behaviour. Rejected
            when the new folder would make an agent that writes there re-trigger itself.
        name (None | str | Unset): New display name for the connection.
    """

    folder_path: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder_path: None | str | Unset
        if isinstance(self.folder_path, Unset):
            folder_path = UNSET
        else:
            folder_path = self.folder_path

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder_path is not UNSET:
            field_dict["folder_path"] = folder_path
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_folder_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_path = _parse_folder_path(d.pop("folder_path", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        cloud_drive_update_request = cls(
            folder_path=folder_path,
            name=name,
        )

        cloud_drive_update_request.additional_properties = d
        return cloud_drive_update_request

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
