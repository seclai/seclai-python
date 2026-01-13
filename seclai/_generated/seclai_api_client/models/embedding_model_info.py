from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingModelInfo")


@_attrs_define
class EmbeddingModelInfo:
    """Information about an embedding model

    Attributes:
        credits_ (float): Estimated credits per 1,000 English words
        dimensions (list[int]): Dimensions options
        model_id (str): Model identifier
        model_type (str): Full model type identifier (enum value)
        description (None | str | Unset): Model description
        mteb_retrieval_score (float | None | Unset): MTEB retrieval score
        name (None | str | Unset): Human-readable model name
        speed (None | str | Unset): Model processing speed
        url (None | str | Unset): Model documentation URL
    """

    credits_: float
    dimensions: list[int]
    model_id: str
    model_type: str
    description: None | str | Unset = UNSET
    mteb_retrieval_score: float | None | Unset = UNSET
    name: None | str | Unset = UNSET
    speed: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        dimensions = self.dimensions

        model_id = self.model_id

        model_type = self.model_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mteb_retrieval_score: float | None | Unset
        if isinstance(self.mteb_retrieval_score, Unset):
            mteb_retrieval_score = UNSET
        else:
            mteb_retrieval_score = self.mteb_retrieval_score

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        speed: None | str | Unset
        if isinstance(self.speed, Unset):
            speed = UNSET
        else:
            speed = self.speed

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
                "dimensions": dimensions,
                "model_id": model_id,
                "model_type": model_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if mteb_retrieval_score is not UNSET:
            field_dict["mteb_retrieval_score"] = mteb_retrieval_score
        if name is not UNSET:
            field_dict["name"] = name
        if speed is not UNSET:
            field_dict["speed"] = speed
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        dimensions = cast(list[int], d.pop("dimensions"))

        model_id = d.pop("model_id")

        model_type = d.pop("model_type")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_mteb_retrieval_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mteb_retrieval_score = _parse_mteb_retrieval_score(d.pop("mteb_retrieval_score", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_speed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        speed = _parse_speed(d.pop("speed", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        embedding_model_info = cls(
            credits_=credits_,
            dimensions=dimensions,
            model_id=model_id,
            model_type=model_type,
            description=description,
            mteb_retrieval_score=mteb_retrieval_score,
            name=name,
            speed=speed,
            url=url,
        )

        embedding_model_info.additional_properties = d
        return embedding_model_info

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
