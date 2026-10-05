from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDriveRejectionResponseModel")


@_attrs_define
class CloudDriveRejectionResponseModel:
    """One file the connection deliberately did not process.

    Attributes:
        created_at (str): When the file was skipped.
        id (str): Rejection identifier.
        reason (str): `too_large`, `download_failed`, or `flood`.
        detail (None | str | Unset): Extra context, e.g. the cap that was hit.
        file_id (None | str | Unset): The provider's file id, when the file was known.
        file_path (None | str | Unset): Path of the skipped file, when known.
    """

    created_at: str
    id: str
    reason: str
    detail: None | str | Unset = UNSET
    file_id: None | str | Unset = UNSET
    file_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        reason = self.reason

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        else:
            file_id = self.file_id

        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "reason": reason,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_path is not UNSET:
            field_dict["file_path"] = file_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = d.pop("id")

        reason = d.pop("reason")

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_file_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("file_path", UNSET))

        cloud_drive_rejection_response_model = cls(
            created_at=created_at,
            id=id,
            reason=reason,
            detail=detail,
            file_id=file_id,
            file_path=file_path,
        )

        cloud_drive_rejection_response_model.additional_properties = d
        return cloud_drive_rejection_response_model

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
