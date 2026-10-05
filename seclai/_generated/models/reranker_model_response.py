from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RerankerModelResponse")


@_attrs_define
class RerankerModelResponse:
    """Information about a reranker model.

    Attributes:
        credits_per_action (float): Credits charged per rerank action
        is_default (bool): Whether this is the platform default reranker
        model_type (str): Full model type identifier.  This is the value to send as reranker_model on a knowledge base;
            send "none" or an empty string to disable reranking.
        name (str): Human-readable model name
        description (None | str | Unset): Model description
        is_new (bool | Unset): Whether the model is newly released Default: False.
        max_input_tokens (int | None | Unset): Max input tokens per request
        provider (None | str | Unset): Model provider identifier
        supported_languages (list[str] | None | Unset): Supported languages
        url (None | str | Unset): Model documentation URL
    """

    credits_per_action: float
    is_default: bool
    model_type: str
    name: str
    description: None | str | Unset = UNSET
    is_new: bool | Unset = False
    max_input_tokens: int | None | Unset = UNSET
    provider: None | str | Unset = UNSET
    supported_languages: list[str] | None | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_per_action = self.credits_per_action

        is_default = self.is_default

        model_type = self.model_type

        name = self.name

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

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

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
                "credits_per_action": credits_per_action,
                "is_default": is_default,
                "model_type": model_type,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if max_input_tokens is not UNSET:
            field_dict["max_input_tokens"] = max_input_tokens
        if provider is not UNSET:
            field_dict["provider"] = provider
        if supported_languages is not UNSET:
            field_dict["supported_languages"] = supported_languages
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_per_action = d.pop("credits_per_action")

        is_default = d.pop("is_default")

        model_type = d.pop("model_type")

        name = d.pop("name")

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

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

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

        reranker_model_response = cls(
            credits_per_action=credits_per_action,
            is_default=is_default,
            model_type=model_type,
            name=name,
            description=description,
            is_new=is_new,
            max_input_tokens=max_input_tokens,
            provider=provider,
            supported_languages=supported_languages,
            url=url,
        )

        reranker_model_response.additional_properties = d
        return reranker_model_response

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
