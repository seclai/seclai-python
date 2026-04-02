from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadAgentInputApiResponse")


@_attrs_define
class UploadAgentInputApiResponse:
    """
    Attributes:
        content_type (str): Resolved MIME type.
        file_size (int): Size in bytes.
        filename (str): Original filename.
        id (str): Unique identifier for the upload.
        status (str): processing, ready, or failed.
        error (None | str | Unset): Error message if status is failed.
    """

    content_type: str
    file_size: int
    filename: str
    id: str
    status: str
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        file_size = self.file_size

        filename = self.filename

        id = self.id

        status = self.status

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "file_size": file_size,
                "filename": filename,
                "id": id,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type")

        file_size = d.pop("file_size")

        filename = d.pop("filename")

        id = d.pop("id")

        status = d.pop("status")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        upload_agent_input_api_response = cls(
            content_type=content_type,
            file_size=file_size,
            filename=filename,
            id=id,
            status=status,
            error=error,
        )

        upload_agent_input_api_response.additional_properties = d
        return upload_agent_input_api_response

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
