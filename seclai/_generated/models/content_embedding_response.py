from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentEmbeddingResponse")


@_attrs_define
class ContentEmbeddingResponse:
    """Response model for content embedding.

    Attributes:
        batch_duration (float):
        batch_size (int):
        id (str):
        text (str):
        text_end (int):
        text_start (int):
        vector (list[float]):
        media_name (None | str | Unset):
        page_number (int | None | Unset):
        source_mime (None | str | Unset):
        source_url (None | str | Unset):
    """

    batch_duration: float
    batch_size: int
    id: str
    text: str
    text_end: int
    text_start: int
    vector: list[float]
    media_name: None | str | Unset = UNSET
    page_number: int | None | Unset = UNSET
    source_mime: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_duration = self.batch_duration

        batch_size = self.batch_size

        id = self.id

        text = self.text

        text_end = self.text_end

        text_start = self.text_start

        vector = self.vector

        media_name: None | str | Unset
        if isinstance(self.media_name, Unset):
            media_name = UNSET
        else:
            media_name = self.media_name

        page_number: int | None | Unset
        if isinstance(self.page_number, Unset):
            page_number = UNSET
        else:
            page_number = self.page_number

        source_mime: None | str | Unset
        if isinstance(self.source_mime, Unset):
            source_mime = UNSET
        else:
            source_mime = self.source_mime

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_duration": batch_duration,
                "batch_size": batch_size,
                "id": id,
                "text": text,
                "text_end": text_end,
                "text_start": text_start,
                "vector": vector,
            }
        )
        if media_name is not UNSET:
            field_dict["media_name"] = media_name
        if page_number is not UNSET:
            field_dict["page_number"] = page_number
        if source_mime is not UNSET:
            field_dict["source_mime"] = source_mime
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_duration = d.pop("batch_duration")

        batch_size = d.pop("batch_size")

        id = d.pop("id")

        text = d.pop("text")

        text_end = d.pop("text_end")

        text_start = d.pop("text_start")

        vector = cast(list[float], d.pop("vector"))

        def _parse_media_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_name = _parse_media_name(d.pop("media_name", UNSET))

        def _parse_page_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_number = _parse_page_number(d.pop("page_number", UNSET))

        def _parse_source_mime(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_mime = _parse_source_mime(d.pop("source_mime", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        content_embedding_response = cls(
            batch_duration=batch_duration,
            batch_size=batch_size,
            id=id,
            text=text,
            text_end=text_end,
            text_start=text_start,
            vector=vector,
            media_name=media_name,
            page_number=page_number,
            source_mime=source_mime,
            source_url=source_url,
        )

        content_embedding_response.additional_properties = d
        return content_embedding_response

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
