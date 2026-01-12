from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    """

    batch_duration: float
    batch_size: int
    id: str
    text: str
    text_end: int
    text_start: int
    vector: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_duration = self.batch_duration

        batch_size = self.batch_size

        id = self.id

        text = self.text

        text_end = self.text_end

        text_start = self.text_start

        vector = self.vector

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

        content_embedding_response = cls(
            batch_duration=batch_duration,
            batch_size=batch_size,
            id=id,
            text=text,
            text_end=text_end,
            text_start=text_start,
            vector=vector,
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
