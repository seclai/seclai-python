from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cloud_drive_access_level_response_model import (
        CloudDriveAccessLevelResponseModel,
    )
    from ..models.cloud_drive_scope_response_model import CloudDriveScopeResponseModel


T = TypeVar("T", bound="CloudDriveProviderResponseModel")


@_attrs_define
class CloudDriveProviderResponseModel:
    """
    Attributes:
        access_levels (list[CloudDriveAccessLevelResponseModel]): Mutually-exclusive permission bundles offered when
            connecting. Connecting happens in the app, so this is informational here — it explains what a connection's
            `access_level` can be.
        display_name (str): Human-readable provider name.
        key (str): Provider key used as `provider` on a connection.
        scopes (list[CloudDriveScopeResponseModel]): OAuth permissions this provider can request.
    """

    access_levels: list[CloudDriveAccessLevelResponseModel]
    display_name: str
    key: str
    scopes: list[CloudDriveScopeResponseModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_levels = []
        for access_levels_item_data in self.access_levels:
            access_levels_item = access_levels_item_data.to_dict()
            access_levels.append(access_levels_item)

        display_name = self.display_name

        key = self.key

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_levels": access_levels,
                "display_name": display_name,
                "key": key,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_drive_access_level_response_model import (
            CloudDriveAccessLevelResponseModel,
        )
        from ..models.cloud_drive_scope_response_model import (
            CloudDriveScopeResponseModel,
        )

        d = dict(src_dict)
        access_levels = []
        _access_levels = d.pop("access_levels")
        for access_levels_item_data in _access_levels:
            access_levels_item = CloudDriveAccessLevelResponseModel.from_dict(
                access_levels_item_data
            )

            access_levels.append(access_levels_item)

        display_name = d.pop("display_name")

        key = d.pop("key")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = CloudDriveScopeResponseModel.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        cloud_drive_provider_response_model = cls(
            access_levels=access_levels,
            display_name=display_name,
            key=key,
            scopes=scopes,
        )

        cloud_drive_provider_response_model.additional_properties = d
        return cloud_drive_provider_response_model

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
