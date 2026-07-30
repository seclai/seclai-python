from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelRecommendationResponse")


@_attrs_define
class ModelRecommendationResponse:
    """
    Attributes:
        description (str):
        id (str):
        max_context_tokens (int):
        max_output_tokens (int):
        model_id (str):
        name (str):
        provider (str):
        reason (str):
        recommendation_type (str):
        supports_openai_arguments (bool):
        supports_streaming (bool):
        supports_structured_output (bool):
        supports_thinking (bool):
        supports_tool_use (bool):
        deprecated_at (None | str | Unset):
        family (None | str | Unset):
        family_generation (float | None | Unset):
        released_at (None | str | Unset):
        sunset_at (None | str | Unset):
    """

    description: str
    id: str
    max_context_tokens: int
    max_output_tokens: int
    model_id: str
    name: str
    provider: str
    reason: str
    recommendation_type: str
    supports_openai_arguments: bool
    supports_streaming: bool
    supports_structured_output: bool
    supports_thinking: bool
    supports_tool_use: bool
    deprecated_at: None | str | Unset = UNSET
    family: None | str | Unset = UNSET
    family_generation: float | None | Unset = UNSET
    released_at: None | str | Unset = UNSET
    sunset_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        max_context_tokens = self.max_context_tokens

        max_output_tokens = self.max_output_tokens

        model_id = self.model_id

        name = self.name

        provider = self.provider

        reason = self.reason

        recommendation_type = self.recommendation_type

        supports_openai_arguments = self.supports_openai_arguments

        supports_streaming = self.supports_streaming

        supports_structured_output = self.supports_structured_output

        supports_thinking = self.supports_thinking

        supports_tool_use = self.supports_tool_use

        deprecated_at: None | str | Unset
        if isinstance(self.deprecated_at, Unset):
            deprecated_at = UNSET
        else:
            deprecated_at = self.deprecated_at

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        family_generation: float | None | Unset
        if isinstance(self.family_generation, Unset):
            family_generation = UNSET
        else:
            family_generation = self.family_generation

        released_at: None | str | Unset
        if isinstance(self.released_at, Unset):
            released_at = UNSET
        else:
            released_at = self.released_at

        sunset_at: None | str | Unset
        if isinstance(self.sunset_at, Unset):
            sunset_at = UNSET
        else:
            sunset_at = self.sunset_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "max_context_tokens": max_context_tokens,
                "max_output_tokens": max_output_tokens,
                "model_id": model_id,
                "name": name,
                "provider": provider,
                "reason": reason,
                "recommendation_type": recommendation_type,
                "supports_openai_arguments": supports_openai_arguments,
                "supports_streaming": supports_streaming,
                "supports_structured_output": supports_structured_output,
                "supports_thinking": supports_thinking,
                "supports_tool_use": supports_tool_use,
            }
        )
        if deprecated_at is not UNSET:
            field_dict["deprecated_at"] = deprecated_at
        if family is not UNSET:
            field_dict["family"] = family
        if family_generation is not UNSET:
            field_dict["family_generation"] = family_generation
        if released_at is not UNSET:
            field_dict["released_at"] = released_at
        if sunset_at is not UNSET:
            field_dict["sunset_at"] = sunset_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        max_context_tokens = d.pop("max_context_tokens")

        max_output_tokens = d.pop("max_output_tokens")

        model_id = d.pop("model_id")

        name = d.pop("name")

        provider = d.pop("provider")

        reason = d.pop("reason")

        recommendation_type = d.pop("recommendation_type")

        supports_openai_arguments = d.pop("supports_openai_arguments")

        supports_streaming = d.pop("supports_streaming")

        supports_structured_output = d.pop("supports_structured_output")

        supports_thinking = d.pop("supports_thinking")

        supports_tool_use = d.pop("supports_tool_use")

        def _parse_deprecated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deprecated_at = _parse_deprecated_at(d.pop("deprecated_at", UNSET))

        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))

        def _parse_family_generation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        family_generation = _parse_family_generation(d.pop("family_generation", UNSET))

        def _parse_released_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        released_at = _parse_released_at(d.pop("released_at", UNSET))

        def _parse_sunset_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sunset_at = _parse_sunset_at(d.pop("sunset_at", UNSET))

        model_recommendation_response = cls(
            description=description,
            id=id,
            max_context_tokens=max_context_tokens,
            max_output_tokens=max_output_tokens,
            model_id=model_id,
            name=name,
            provider=provider,
            reason=reason,
            recommendation_type=recommendation_type,
            supports_openai_arguments=supports_openai_arguments,
            supports_streaming=supports_streaming,
            supports_structured_output=supports_structured_output,
            supports_thinking=supports_thinking,
            supports_tool_use=supports_tool_use,
            deprecated_at=deprecated_at,
            family=family,
            family_generation=family_generation,
            released_at=released_at,
            sunset_at=sunset_at,
        )

        model_recommendation_response.additional_properties = d
        return model_recommendation_response

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
