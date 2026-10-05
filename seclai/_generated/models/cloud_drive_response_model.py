from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDriveResponseModel")


@_attrs_define
class CloudDriveResponseModel:
    """A cloud-drive connection, without any secret material.

    Attributes:
        connected (bool): True when the connection is usable.
        created_at (str): When the connection was created.
        drive_name_stale (bool): True when `drive_name` could not be re-confirmed (the drive was deleted, access was
            lost, or the provider was unreachable). The last known name is still reported — treat it as possibly out of date
            rather than current.
        folder_path (str): Watched folder; empty string means the drive root. A folder on a shared drive is written
            `/Shared drives/<drive name>/<folder>`.
        id (str): Connection identifier.
        provider (str): Provider key, e.g. `dropbox` or `google_drive`.
        realtime_updates (bool): True when changes arrive via the provider's push notifications. False means the drive
            still syncs, but only on the scheduled backstop sweep rather than within seconds of a change.
        status (str): One of `active`, `pending_auth`, `error`, `disconnected`.
        updated_at (str): When the connection was last modified.
        access_level (None | str | Unset): The permission bundle the granted scopes correspond to — `read_write` or
            `read_only`. Null when the grant matches no level the provider currently offers; treat that as unknown rather
            than assuming write access.
        drive_id (None | str | Unset): Opaque id of the shared drive the folder resolves to, or null for the user's own
            drive. Stable across renames — compare on this rather than on the name in `folder_path`.
        drive_name (None | str | Unset): Display name the shared drive last resolved to. Presentation only; never match
            on it.
        external_account_id (None | str | Unset): The provider's own opaque account identifier (never an email).
        last_error (None | str | Unset): Most recent sync or authorization error, if any.
        last_synced_at (None | str | Unset): When the connection last synced successfully.
        name (None | str | Unset): Human-readable name.
        oauth_scopes (None | str | Unset): Space-separated OAuth scopes granted to this connection.
    """

    connected: bool
    created_at: str
    drive_name_stale: bool
    folder_path: str
    id: str
    provider: str
    realtime_updates: bool
    status: str
    updated_at: str
    access_level: None | str | Unset = UNSET
    drive_id: None | str | Unset = UNSET
    drive_name: None | str | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    last_error: None | str | Unset = UNSET
    last_synced_at: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    oauth_scopes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected = self.connected

        created_at = self.created_at

        drive_name_stale = self.drive_name_stale

        folder_path = self.folder_path

        id = self.id

        provider = self.provider

        realtime_updates = self.realtime_updates

        status = self.status

        updated_at = self.updated_at

        access_level: None | str | Unset
        if isinstance(self.access_level, Unset):
            access_level = UNSET
        else:
            access_level = self.access_level

        drive_id: None | str | Unset
        if isinstance(self.drive_id, Unset):
            drive_id = UNSET
        else:
            drive_id = self.drive_id

        drive_name: None | str | Unset
        if isinstance(self.drive_name, Unset):
            drive_name = UNSET
        else:
            drive_name = self.drive_name

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = self.last_synced_at

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        oauth_scopes: None | str | Unset
        if isinstance(self.oauth_scopes, Unset):
            oauth_scopes = UNSET
        else:
            oauth_scopes = self.oauth_scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connected": connected,
                "created_at": created_at,
                "drive_name_stale": drive_name_stale,
                "folder_path": folder_path,
                "id": id,
                "provider": provider,
                "realtime_updates": realtime_updates,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if access_level is not UNSET:
            field_dict["access_level"] = access_level
        if drive_id is not UNSET:
            field_dict["drive_id"] = drive_id
        if drive_name is not UNSET:
            field_dict["drive_name"] = drive_name
        if external_account_id is not UNSET:
            field_dict["external_account_id"] = external_account_id
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if name is not UNSET:
            field_dict["name"] = name
        if oauth_scopes is not UNSET:
            field_dict["oauth_scopes"] = oauth_scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected = d.pop("connected")

        created_at = d.pop("created_at")

        drive_name_stale = d.pop("drive_name_stale")

        folder_path = d.pop("folder_path")

        id = d.pop("id")

        provider = d.pop("provider")

        realtime_updates = d.pop("realtime_updates")

        status = d.pop("status")

        updated_at = d.pop("updated_at")

        def _parse_access_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_level = _parse_access_level(d.pop("access_level", UNSET))

        def _parse_drive_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drive_id = _parse_drive_id(d.pop("drive_id", UNSET))

        def _parse_drive_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drive_name = _parse_drive_name(d.pop("drive_name", UNSET))

        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(
            d.pop("external_account_id", UNSET)
        )

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        def _parse_last_synced_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_oauth_scopes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oauth_scopes = _parse_oauth_scopes(d.pop("oauth_scopes", UNSET))

        cloud_drive_response_model = cls(
            connected=connected,
            created_at=created_at,
            drive_name_stale=drive_name_stale,
            folder_path=folder_path,
            id=id,
            provider=provider,
            realtime_updates=realtime_updates,
            status=status,
            updated_at=updated_at,
            access_level=access_level,
            drive_id=drive_id,
            drive_name=drive_name,
            external_account_id=external_account_id,
            last_error=last_error,
            last_synced_at=last_synced_at,
            name=name,
            oauth_scopes=oauth_scopes,
        )

        cloud_drive_response_model.additional_properties = d
        return cloud_drive_response_model

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
