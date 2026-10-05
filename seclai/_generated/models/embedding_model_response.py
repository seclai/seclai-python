from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedding_modality_rate_response import EmbeddingModalityRateResponse


T = TypeVar("T", bound="EmbeddingModelResponse")


@_attrs_define
class EmbeddingModelResponse:
    """Information about an embedding model.

    Attributes:
        credits_ (float): Estimated credits per 1,000 English words
        dimensions (list[int]): Dimensions options
        model_id (str): Model identifier
        model_type (str): Full model type identifier (enum value).  This is the value to send as embedding_model when
            creating a source.
        description (None | str | Unset): Model description
        is_new (bool | Unset): Whether the model is newly released Default: False.
        max_input_tokens (int | None | Unset): Max input tokens per request
        mteb_retrieval_score (float | None | Unset): MTEB retrieval score
        name (None | str | Unset): Human-readable model name
        per_modality_rates (list[EmbeddingModalityRateResponse] | Unset): Non-text rates the vendor charges for this
            embedder (image, video, audio).  Empty for text-only embedders.
        provider (None | str | Unset): Model provider identifier
        speed (None | str | Unset): Model processing speed
        supported_input_media (list[str] | None | Unset): Modalities the embedder accepts on input (short kinds like
            text / image / video, or full MIMEs).  null means text-only.  A source only honours a media_types entry its
            embedder lists here.
        supported_languages (list[str] | None | Unset): Supported languages
        url (None | str | Unset): Model documentation URL
    """

    credits_: float
    dimensions: list[int]
    model_id: str
    model_type: str
    description: None | str | Unset = UNSET
    is_new: bool | Unset = False
    max_input_tokens: int | None | Unset = UNSET
    mteb_retrieval_score: float | None | Unset = UNSET
    name: None | str | Unset = UNSET
    per_modality_rates: list[EmbeddingModalityRateResponse] | Unset = UNSET
    provider: None | str | Unset = UNSET
    speed: None | str | Unset = UNSET
    supported_input_media: list[str] | None | Unset = UNSET
    supported_languages: list[str] | None | Unset = UNSET
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

        is_new = self.is_new

        max_input_tokens: int | None | Unset
        if isinstance(self.max_input_tokens, Unset):
            max_input_tokens = UNSET
        else:
            max_input_tokens = self.max_input_tokens

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

        per_modality_rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.per_modality_rates, Unset):
            per_modality_rates = []
            for per_modality_rates_item_data in self.per_modality_rates:
                per_modality_rates_item = per_modality_rates_item_data.to_dict()
                per_modality_rates.append(per_modality_rates_item)

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        speed: None | str | Unset
        if isinstance(self.speed, Unset):
            speed = UNSET
        else:
            speed = self.speed

        supported_input_media: list[str] | None | Unset
        if isinstance(self.supported_input_media, Unset):
            supported_input_media = UNSET
        elif isinstance(self.supported_input_media, list):
            supported_input_media = self.supported_input_media

        else:
            supported_input_media = self.supported_input_media

        supported_languages: list[str] | None | Unset
        if isinstance(self.supported_languages, Unset):
            supported_languages = UNSET
        elif isinstance(self.supported_languages, list):
            supported_languages = self.supported_languages

        else:
            supported_languages = self.supported_languages

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
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if max_input_tokens is not UNSET:
            field_dict["max_input_tokens"] = max_input_tokens
        if mteb_retrieval_score is not UNSET:
            field_dict["mteb_retrieval_score"] = mteb_retrieval_score
        if name is not UNSET:
            field_dict["name"] = name
        if per_modality_rates is not UNSET:
            field_dict["per_modality_rates"] = per_modality_rates
        if provider is not UNSET:
            field_dict["provider"] = provider
        if speed is not UNSET:
            field_dict["speed"] = speed
        if supported_input_media is not UNSET:
            field_dict["supported_input_media"] = supported_input_media
        if supported_languages is not UNSET:
            field_dict["supported_languages"] = supported_languages
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedding_modality_rate_response import (
            EmbeddingModalityRateResponse,
        )

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

        is_new = d.pop("is_new", UNSET)

        def _parse_max_input_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_input_tokens = _parse_max_input_tokens(d.pop("max_input_tokens", UNSET))

        def _parse_mteb_retrieval_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mteb_retrieval_score = _parse_mteb_retrieval_score(
            d.pop("mteb_retrieval_score", UNSET)
        )

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _per_modality_rates = d.pop("per_modality_rates", UNSET)
        per_modality_rates: list[EmbeddingModalityRateResponse] | Unset = UNSET
        if _per_modality_rates is not UNSET:
            per_modality_rates = []
            for per_modality_rates_item_data in _per_modality_rates:
                per_modality_rates_item = EmbeddingModalityRateResponse.from_dict(
                    per_modality_rates_item_data
                )

                per_modality_rates.append(per_modality_rates_item)

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_speed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        speed = _parse_speed(d.pop("speed", UNSET))

        def _parse_supported_input_media(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_input_media_type_0 = cast(list[str], data)

                return supported_input_media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_input_media = _parse_supported_input_media(
            d.pop("supported_input_media", UNSET)
        )

        def _parse_supported_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_languages_type_0 = cast(list[str], data)

                return supported_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_languages = _parse_supported_languages(
            d.pop("supported_languages", UNSET)
        )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        embedding_model_response = cls(
            credits_=credits_,
            dimensions=dimensions,
            model_id=model_id,
            model_type=model_type,
            description=description,
            is_new=is_new,
            max_input_tokens=max_input_tokens,
            mteb_retrieval_score=mteb_retrieval_score,
            name=name,
            per_modality_rates=per_modality_rates,
            provider=provider,
            speed=speed,
            supported_input_media=supported_input_media,
            supported_languages=supported_languages,
            url=url,
        )

        embedding_model_response.additional_properties = d
        return embedding_model_response

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
