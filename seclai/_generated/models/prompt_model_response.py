from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_model_response_payload_schema_type_0 import (
        PromptModelResponsePayloadSchemaType0,
    )
    from ..models.prompt_tool_response import PromptToolResponse
    from ..models.variant_category_response import VariantCategoryResponse


T = TypeVar("T", bound="PromptModelResponse")


@_attrs_define
class PromptModelResponse:
    """Response model for prompt model data

    Attributes:
        default (bool):
        description (str):
        enabled (bool):
        id (str):
        max_context_tokens (int):
        max_conversation_length (int):
        max_output_tokens (int):
        model_id (str):
        name (str):
        provider (str):
        deprecated_at (datetime.datetime | None | Unset):
        family (None | str | Unset):
        family_generation (float | None | Unset):
        input_1h_cache_write_credits_per_1000_tokens (float | None | Unset):
        input_5m_cache_write_credits_per_1000_tokens (float | None | Unset):
        input_cache_hit_credits_per_1000_tokens (float | None | Unset):
        input_credits_per_1000_tokens (float | None | Unset):
        is_new (bool | Unset):  Default: False.
        last_used (bool | Unset):  Default: False.
        output_credits_per_1000_tokens (float | None | Unset):
        payload_schema (None | PromptModelResponsePayloadSchemaType0 | Unset): Model-specific JSON schema for advanced
            prompt_call json_template payloads.
        payload_schema_source_url (None | str | Unset): Source URL used to derive payload_schema guidance for this
            model.
        released_at (datetime.datetime | None | Unset):
        schema_documentation_url (None | str | Unset): Model documentation URL with request/response payload details.
        schema_notes (None | str | Unset): Human-readable notes about request payload compatibility.
        successor_model_id (None | str | Unset):
        sunset_at (datetime.datetime | None | Unset):
        supported_input_media (list[str] | None | Unset):
        supported_languages (list[str] | None | Unset):
        supports_openai_arguments (bool | Unset):  Default: False.
        supports_streaming (bool | Unset):  Default: False.
        supports_structured_output (bool | Unset):  Default: True.
        supports_thinking (bool | Unset):  Default: False.
        supports_tool_use (bool | Unset):  Default: True.
        tools_disabled (list[PromptToolResponse] | Unset):
        tools_enabled (list[PromptToolResponse] | Unset):
        training_cutoff_at (datetime.datetime | None | Unset):
        url (None | str | Unset):
        variants (list[VariantCategoryResponse] | None | Unset):
    """

    default: bool
    description: str
    enabled: bool
    id: str
    max_context_tokens: int
    max_conversation_length: int
    max_output_tokens: int
    model_id: str
    name: str
    provider: str
    deprecated_at: datetime.datetime | None | Unset = UNSET
    family: None | str | Unset = UNSET
    family_generation: float | None | Unset = UNSET
    input_1h_cache_write_credits_per_1000_tokens: float | None | Unset = UNSET
    input_5m_cache_write_credits_per_1000_tokens: float | None | Unset = UNSET
    input_cache_hit_credits_per_1000_tokens: float | None | Unset = UNSET
    input_credits_per_1000_tokens: float | None | Unset = UNSET
    is_new: bool | Unset = False
    last_used: bool | Unset = False
    output_credits_per_1000_tokens: float | None | Unset = UNSET
    payload_schema: None | PromptModelResponsePayloadSchemaType0 | Unset = UNSET
    payload_schema_source_url: None | str | Unset = UNSET
    released_at: datetime.datetime | None | Unset = UNSET
    schema_documentation_url: None | str | Unset = UNSET
    schema_notes: None | str | Unset = UNSET
    successor_model_id: None | str | Unset = UNSET
    sunset_at: datetime.datetime | None | Unset = UNSET
    supported_input_media: list[str] | None | Unset = UNSET
    supported_languages: list[str] | None | Unset = UNSET
    supports_openai_arguments: bool | Unset = False
    supports_streaming: bool | Unset = False
    supports_structured_output: bool | Unset = True
    supports_thinking: bool | Unset = False
    supports_tool_use: bool | Unset = True
    tools_disabled: list[PromptToolResponse] | Unset = UNSET
    tools_enabled: list[PromptToolResponse] | Unset = UNSET
    training_cutoff_at: datetime.datetime | None | Unset = UNSET
    url: None | str | Unset = UNSET
    variants: list[VariantCategoryResponse] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_model_response_payload_schema_type_0 import (
            PromptModelResponsePayloadSchemaType0,
        )

        default = self.default

        description = self.description

        enabled = self.enabled

        id = self.id

        max_context_tokens = self.max_context_tokens

        max_conversation_length = self.max_conversation_length

        max_output_tokens = self.max_output_tokens

        model_id = self.model_id

        name = self.name

        provider = self.provider

        deprecated_at: None | str | Unset
        if isinstance(self.deprecated_at, Unset):
            deprecated_at = UNSET
        elif isinstance(self.deprecated_at, datetime.datetime):
            deprecated_at = self.deprecated_at.isoformat()
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

        input_1h_cache_write_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_1h_cache_write_credits_per_1000_tokens, Unset):
            input_1h_cache_write_credits_per_1000_tokens = UNSET
        else:
            input_1h_cache_write_credits_per_1000_tokens = (
                self.input_1h_cache_write_credits_per_1000_tokens
            )

        input_5m_cache_write_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_5m_cache_write_credits_per_1000_tokens, Unset):
            input_5m_cache_write_credits_per_1000_tokens = UNSET
        else:
            input_5m_cache_write_credits_per_1000_tokens = (
                self.input_5m_cache_write_credits_per_1000_tokens
            )

        input_cache_hit_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_cache_hit_credits_per_1000_tokens, Unset):
            input_cache_hit_credits_per_1000_tokens = UNSET
        else:
            input_cache_hit_credits_per_1000_tokens = (
                self.input_cache_hit_credits_per_1000_tokens
            )

        input_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_credits_per_1000_tokens, Unset):
            input_credits_per_1000_tokens = UNSET
        else:
            input_credits_per_1000_tokens = self.input_credits_per_1000_tokens

        is_new = self.is_new

        last_used = self.last_used

        output_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.output_credits_per_1000_tokens, Unset):
            output_credits_per_1000_tokens = UNSET
        else:
            output_credits_per_1000_tokens = self.output_credits_per_1000_tokens

        payload_schema: dict[str, Any] | None | Unset
        if isinstance(self.payload_schema, Unset):
            payload_schema = UNSET
        elif isinstance(self.payload_schema, PromptModelResponsePayloadSchemaType0):
            payload_schema = self.payload_schema.to_dict()
        else:
            payload_schema = self.payload_schema

        payload_schema_source_url: None | str | Unset
        if isinstance(self.payload_schema_source_url, Unset):
            payload_schema_source_url = UNSET
        else:
            payload_schema_source_url = self.payload_schema_source_url

        released_at: None | str | Unset
        if isinstance(self.released_at, Unset):
            released_at = UNSET
        elif isinstance(self.released_at, datetime.datetime):
            released_at = self.released_at.isoformat()
        else:
            released_at = self.released_at

        schema_documentation_url: None | str | Unset
        if isinstance(self.schema_documentation_url, Unset):
            schema_documentation_url = UNSET
        else:
            schema_documentation_url = self.schema_documentation_url

        schema_notes: None | str | Unset
        if isinstance(self.schema_notes, Unset):
            schema_notes = UNSET
        else:
            schema_notes = self.schema_notes

        successor_model_id: None | str | Unset
        if isinstance(self.successor_model_id, Unset):
            successor_model_id = UNSET
        else:
            successor_model_id = self.successor_model_id

        sunset_at: None | str | Unset
        if isinstance(self.sunset_at, Unset):
            sunset_at = UNSET
        elif isinstance(self.sunset_at, datetime.datetime):
            sunset_at = self.sunset_at.isoformat()
        else:
            sunset_at = self.sunset_at

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

        supports_openai_arguments = self.supports_openai_arguments

        supports_streaming = self.supports_streaming

        supports_structured_output = self.supports_structured_output

        supports_thinking = self.supports_thinking

        supports_tool_use = self.supports_tool_use

        tools_disabled: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools_disabled, Unset):
            tools_disabled = []
            for tools_disabled_item_data in self.tools_disabled:
                tools_disabled_item = tools_disabled_item_data.to_dict()
                tools_disabled.append(tools_disabled_item)

        tools_enabled: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools_enabled, Unset):
            tools_enabled = []
            for tools_enabled_item_data in self.tools_enabled:
                tools_enabled_item = tools_enabled_item_data.to_dict()
                tools_enabled.append(tools_enabled_item)

        training_cutoff_at: None | str | Unset
        if isinstance(self.training_cutoff_at, Unset):
            training_cutoff_at = UNSET
        elif isinstance(self.training_cutoff_at, datetime.datetime):
            training_cutoff_at = self.training_cutoff_at.isoformat()
        else:
            training_cutoff_at = self.training_cutoff_at

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        variants: list[dict[str, Any]] | None | Unset
        if isinstance(self.variants, Unset):
            variants = UNSET
        elif isinstance(self.variants, list):
            variants = []
            for variants_type_0_item_data in self.variants:
                variants_type_0_item = variants_type_0_item_data.to_dict()
                variants.append(variants_type_0_item)

        else:
            variants = self.variants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "description": description,
                "enabled": enabled,
                "id": id,
                "max_context_tokens": max_context_tokens,
                "max_conversation_length": max_conversation_length,
                "max_output_tokens": max_output_tokens,
                "model_id": model_id,
                "name": name,
                "provider": provider,
            }
        )
        if deprecated_at is not UNSET:
            field_dict["deprecated_at"] = deprecated_at
        if family is not UNSET:
            field_dict["family"] = family
        if family_generation is not UNSET:
            field_dict["family_generation"] = family_generation
        if input_1h_cache_write_credits_per_1000_tokens is not UNSET:
            field_dict["input_1h_cache_write_credits_per_1000_tokens"] = (
                input_1h_cache_write_credits_per_1000_tokens
            )
        if input_5m_cache_write_credits_per_1000_tokens is not UNSET:
            field_dict["input_5m_cache_write_credits_per_1000_tokens"] = (
                input_5m_cache_write_credits_per_1000_tokens
            )
        if input_cache_hit_credits_per_1000_tokens is not UNSET:
            field_dict["input_cache_hit_credits_per_1000_tokens"] = (
                input_cache_hit_credits_per_1000_tokens
            )
        if input_credits_per_1000_tokens is not UNSET:
            field_dict["input_credits_per_1000_tokens"] = input_credits_per_1000_tokens
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if output_credits_per_1000_tokens is not UNSET:
            field_dict["output_credits_per_1000_tokens"] = (
                output_credits_per_1000_tokens
            )
        if payload_schema is not UNSET:
            field_dict["payload_schema"] = payload_schema
        if payload_schema_source_url is not UNSET:
            field_dict["payload_schema_source_url"] = payload_schema_source_url
        if released_at is not UNSET:
            field_dict["released_at"] = released_at
        if schema_documentation_url is not UNSET:
            field_dict["schema_documentation_url"] = schema_documentation_url
        if schema_notes is not UNSET:
            field_dict["schema_notes"] = schema_notes
        if successor_model_id is not UNSET:
            field_dict["successor_model_id"] = successor_model_id
        if sunset_at is not UNSET:
            field_dict["sunset_at"] = sunset_at
        if supported_input_media is not UNSET:
            field_dict["supported_input_media"] = supported_input_media
        if supported_languages is not UNSET:
            field_dict["supported_languages"] = supported_languages
        if supports_openai_arguments is not UNSET:
            field_dict["supports_openai_arguments"] = supports_openai_arguments
        if supports_streaming is not UNSET:
            field_dict["supports_streaming"] = supports_streaming
        if supports_structured_output is not UNSET:
            field_dict["supports_structured_output"] = supports_structured_output
        if supports_thinking is not UNSET:
            field_dict["supports_thinking"] = supports_thinking
        if supports_tool_use is not UNSET:
            field_dict["supports_tool_use"] = supports_tool_use
        if tools_disabled is not UNSET:
            field_dict["tools_disabled"] = tools_disabled
        if tools_enabled is not UNSET:
            field_dict["tools_enabled"] = tools_enabled
        if training_cutoff_at is not UNSET:
            field_dict["training_cutoff_at"] = training_cutoff_at
        if url is not UNSET:
            field_dict["url"] = url
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_model_response_payload_schema_type_0 import (
            PromptModelResponsePayloadSchemaType0,
        )
        from ..models.prompt_tool_response import PromptToolResponse
        from ..models.variant_category_response import VariantCategoryResponse

        d = dict(src_dict)
        default = d.pop("default")

        description = d.pop("description")

        enabled = d.pop("enabled")

        id = d.pop("id")

        max_context_tokens = d.pop("max_context_tokens")

        max_conversation_length = d.pop("max_conversation_length")

        max_output_tokens = d.pop("max_output_tokens")

        model_id = d.pop("model_id")

        name = d.pop("name")

        provider = d.pop("provider")

        def _parse_deprecated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deprecated_at_type_0 = isoparse(data)

                return deprecated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

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

        def _parse_input_1h_cache_write_credits_per_1000_tokens(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_1h_cache_write_credits_per_1000_tokens = (
            _parse_input_1h_cache_write_credits_per_1000_tokens(
                d.pop("input_1h_cache_write_credits_per_1000_tokens", UNSET)
            )
        )

        def _parse_input_5m_cache_write_credits_per_1000_tokens(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_5m_cache_write_credits_per_1000_tokens = (
            _parse_input_5m_cache_write_credits_per_1000_tokens(
                d.pop("input_5m_cache_write_credits_per_1000_tokens", UNSET)
            )
        )

        def _parse_input_cache_hit_credits_per_1000_tokens(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cache_hit_credits_per_1000_tokens = (
            _parse_input_cache_hit_credits_per_1000_tokens(
                d.pop("input_cache_hit_credits_per_1000_tokens", UNSET)
            )
        )

        def _parse_input_credits_per_1000_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_credits_per_1000_tokens = _parse_input_credits_per_1000_tokens(
            d.pop("input_credits_per_1000_tokens", UNSET)
        )

        is_new = d.pop("is_new", UNSET)

        last_used = d.pop("last_used", UNSET)

        def _parse_output_credits_per_1000_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_credits_per_1000_tokens = _parse_output_credits_per_1000_tokens(
            d.pop("output_credits_per_1000_tokens", UNSET)
        )

        def _parse_payload_schema(
            data: object,
        ) -> None | PromptModelResponsePayloadSchemaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_schema_type_0 = PromptModelResponsePayloadSchemaType0.from_dict(
                    data
                )

                return payload_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptModelResponsePayloadSchemaType0 | Unset, data)

        payload_schema = _parse_payload_schema(d.pop("payload_schema", UNSET))

        def _parse_payload_schema_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload_schema_source_url = _parse_payload_schema_source_url(
            d.pop("payload_schema_source_url", UNSET)
        )

        def _parse_released_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_at_type_0 = isoparse(data)

                return released_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        released_at = _parse_released_at(d.pop("released_at", UNSET))

        def _parse_schema_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_documentation_url = _parse_schema_documentation_url(
            d.pop("schema_documentation_url", UNSET)
        )

        def _parse_schema_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_notes = _parse_schema_notes(d.pop("schema_notes", UNSET))

        def _parse_successor_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        successor_model_id = _parse_successor_model_id(
            d.pop("successor_model_id", UNSET)
        )

        def _parse_sunset_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sunset_at_type_0 = isoparse(data)

                return sunset_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sunset_at = _parse_sunset_at(d.pop("sunset_at", UNSET))

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

        supports_openai_arguments = d.pop("supports_openai_arguments", UNSET)

        supports_streaming = d.pop("supports_streaming", UNSET)

        supports_structured_output = d.pop("supports_structured_output", UNSET)

        supports_thinking = d.pop("supports_thinking", UNSET)

        supports_tool_use = d.pop("supports_tool_use", UNSET)

        _tools_disabled = d.pop("tools_disabled", UNSET)
        tools_disabled: list[PromptToolResponse] | Unset = UNSET
        if _tools_disabled is not UNSET:
            tools_disabled = []
            for tools_disabled_item_data in _tools_disabled:
                tools_disabled_item = PromptToolResponse.from_dict(
                    tools_disabled_item_data
                )

                tools_disabled.append(tools_disabled_item)

        _tools_enabled = d.pop("tools_enabled", UNSET)
        tools_enabled: list[PromptToolResponse] | Unset = UNSET
        if _tools_enabled is not UNSET:
            tools_enabled = []
            for tools_enabled_item_data in _tools_enabled:
                tools_enabled_item = PromptToolResponse.from_dict(
                    tools_enabled_item_data
                )

                tools_enabled.append(tools_enabled_item)

        def _parse_training_cutoff_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                training_cutoff_at_type_0 = isoparse(data)

                return training_cutoff_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        training_cutoff_at = _parse_training_cutoff_at(
            d.pop("training_cutoff_at", UNSET)
        )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_variants(
            data: object,
        ) -> list[VariantCategoryResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variants_type_0 = []
                _variants_type_0 = data
                for variants_type_0_item_data in _variants_type_0:
                    variants_type_0_item = VariantCategoryResponse.from_dict(
                        variants_type_0_item_data
                    )

                    variants_type_0.append(variants_type_0_item)

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VariantCategoryResponse] | None | Unset, data)

        variants = _parse_variants(d.pop("variants", UNSET))

        prompt_model_response = cls(
            default=default,
            description=description,
            enabled=enabled,
            id=id,
            max_context_tokens=max_context_tokens,
            max_conversation_length=max_conversation_length,
            max_output_tokens=max_output_tokens,
            model_id=model_id,
            name=name,
            provider=provider,
            deprecated_at=deprecated_at,
            family=family,
            family_generation=family_generation,
            input_1h_cache_write_credits_per_1000_tokens=input_1h_cache_write_credits_per_1000_tokens,
            input_5m_cache_write_credits_per_1000_tokens=input_5m_cache_write_credits_per_1000_tokens,
            input_cache_hit_credits_per_1000_tokens=input_cache_hit_credits_per_1000_tokens,
            input_credits_per_1000_tokens=input_credits_per_1000_tokens,
            is_new=is_new,
            last_used=last_used,
            output_credits_per_1000_tokens=output_credits_per_1000_tokens,
            payload_schema=payload_schema,
            payload_schema_source_url=payload_schema_source_url,
            released_at=released_at,
            schema_documentation_url=schema_documentation_url,
            schema_notes=schema_notes,
            successor_model_id=successor_model_id,
            sunset_at=sunset_at,
            supported_input_media=supported_input_media,
            supported_languages=supported_languages,
            supports_openai_arguments=supports_openai_arguments,
            supports_streaming=supports_streaming,
            supports_structured_output=supports_structured_output,
            supports_thinking=supports_thinking,
            supports_tool_use=supports_tool_use,
            tools_disabled=tools_disabled,
            tools_enabled=tools_enabled,
            training_cutoff_at=training_cutoff_at,
            url=url,
            variants=variants,
        )

        prompt_model_response.additional_properties = d
        return prompt_model_response

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
