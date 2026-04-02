from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inline_text_replace_request_metadata_type_0 import (
        InlineTextReplaceRequestMetadataType0,
    )


T = TypeVar("T", bound="InlineTextReplaceRequest")


@_attrs_define
class InlineTextReplaceRequest:
    """Request model for inline text content replacement.

    Attributes:
        text (str): Text content to upload
        content_type (None | str | Unset): MIME type for the text content Default: 'text/plain'.
        metadata (InlineTextReplaceRequestMetadataType0 | None | Unset): Optional metadata object
        title (None | str | Unset): Optional title
    """

    text: str
    content_type: None | str | Unset = "text/plain"
    metadata: InlineTextReplaceRequestMetadataType0 | None | Unset = UNSET
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inline_text_replace_request_metadata_type_0 import (
            InlineTextReplaceRequestMetadataType0,
        )

        text = self.text

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InlineTextReplaceRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inline_text_replace_request_metadata_type_0 import (
            InlineTextReplaceRequestMetadataType0,
        )

        d = dict(src_dict)
        text = d.pop("text")

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        def _parse_metadata(
            data: object,
        ) -> InlineTextReplaceRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InlineTextReplaceRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InlineTextReplaceRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        inline_text_replace_request = cls(
            text=text,
            content_type=content_type,
            metadata=metadata,
            title=title,
        )

        inline_text_replace_request.additional_properties = d
        return inline_text_replace_request

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
