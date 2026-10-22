from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.skipped_attachment_reason import SkippedAttachmentReason

T = TypeVar("T", bound="SkippedAttachmentResponse")


@_attrs_define
class SkippedAttachmentResponse:
    """A part of an email that was not stored as an attachment.

    Attributes:
        content_type (str): The part's declared media type.
        filename (None | str): The file name the part is listed under; null when it had none.
        reason (SkippedAttachmentReason):
        size_bytes (int | None): Decoded size in bytes.
    """

    content_type: str
    filename: None | str
    reason: SkippedAttachmentReason
    size_bytes: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        filename: None | str
        filename = self.filename

        reason = self.reason.value

        size_bytes: int | None
        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "filename": filename,
                "reason": reason,
                "size_bytes": size_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type")

        def _parse_filename(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        filename = _parse_filename(d.pop("filename"))

        reason = SkippedAttachmentReason(d.pop("reason"))

        def _parse_size_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes"))

        skipped_attachment_response = cls(
            content_type=content_type,
            filename=filename,
            reason=reason,
            size_bytes=size_bytes,
        )

        skipped_attachment_response.additional_properties = d
        return skipped_attachment_response

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
