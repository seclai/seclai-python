from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
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
        max_conversation_length (int):
        max_tokens (int):
        model_id (str):
        name (str):
        provider (str):
        input_1h_cache_write_credits_per_1000_tokens (float | None | Unset):
        input_5m_cache_write_credits_per_1000_tokens (float | None | Unset):
        input_cache_hit_credits_per_1000_tokens (float | None | Unset):
        input_credits_per_1000_tokens (float | None | Unset):
        last_used (bool | Unset):  Default: False.
        output_credits_per_1000_tokens (float | None | Unset):
        schema_documentation_url (None | str | Unset):
        schema_notes (None | str | Unset):
        tools_disabled (list[PromptToolResponse] | Unset):
        tools_enabled (list[PromptToolResponse] | Unset):
        url (None | str | Unset):
        variants (list[VariantCategoryResponse] | None | Unset):
    """

    default: bool
    description: str
    enabled: bool
    id: str
    max_conversation_length: int
    max_tokens: int
    model_id: str
    name: str
    provider: str
    input_1h_cache_write_credits_per_1000_tokens: float | None | Unset = UNSET
    input_5m_cache_write_credits_per_1000_tokens: float | None | Unset = UNSET
    input_cache_hit_credits_per_1000_tokens: float | None | Unset = UNSET
    input_credits_per_1000_tokens: float | None | Unset = UNSET
    last_used: bool | Unset = False
    output_credits_per_1000_tokens: float | None | Unset = UNSET
    schema_documentation_url: None | str | Unset = UNSET
    schema_notes: None | str | Unset = UNSET
    tools_disabled: list[PromptToolResponse] | Unset = UNSET
    tools_enabled: list[PromptToolResponse] | Unset = UNSET
    url: None | str | Unset = UNSET
    variants: list[VariantCategoryResponse] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        description = self.description

        enabled = self.enabled

        id = self.id

        max_conversation_length = self.max_conversation_length

        max_tokens = self.max_tokens

        model_id = self.model_id

        name = self.name

        provider = self.provider

        input_1h_cache_write_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_1h_cache_write_credits_per_1000_tokens, Unset):
            input_1h_cache_write_credits_per_1000_tokens = UNSET
        else:
            input_1h_cache_write_credits_per_1000_tokens = self.input_1h_cache_write_credits_per_1000_tokens

        input_5m_cache_write_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_5m_cache_write_credits_per_1000_tokens, Unset):
            input_5m_cache_write_credits_per_1000_tokens = UNSET
        else:
            input_5m_cache_write_credits_per_1000_tokens = self.input_5m_cache_write_credits_per_1000_tokens

        input_cache_hit_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_cache_hit_credits_per_1000_tokens, Unset):
            input_cache_hit_credits_per_1000_tokens = UNSET
        else:
            input_cache_hit_credits_per_1000_tokens = self.input_cache_hit_credits_per_1000_tokens

        input_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_credits_per_1000_tokens, Unset):
            input_credits_per_1000_tokens = UNSET
        else:
            input_credits_per_1000_tokens = self.input_credits_per_1000_tokens

        last_used = self.last_used

        output_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.output_credits_per_1000_tokens, Unset):
            output_credits_per_1000_tokens = UNSET
        else:
            output_credits_per_1000_tokens = self.output_credits_per_1000_tokens

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
                "max_conversation_length": max_conversation_length,
                "max_tokens": max_tokens,
                "model_id": model_id,
                "name": name,
                "provider": provider,
            }
        )
        if input_1h_cache_write_credits_per_1000_tokens is not UNSET:
            field_dict["input_1h_cache_write_credits_per_1000_tokens"] = input_1h_cache_write_credits_per_1000_tokens
        if input_5m_cache_write_credits_per_1000_tokens is not UNSET:
            field_dict["input_5m_cache_write_credits_per_1000_tokens"] = input_5m_cache_write_credits_per_1000_tokens
        if input_cache_hit_credits_per_1000_tokens is not UNSET:
            field_dict["input_cache_hit_credits_per_1000_tokens"] = input_cache_hit_credits_per_1000_tokens
        if input_credits_per_1000_tokens is not UNSET:
            field_dict["input_credits_per_1000_tokens"] = input_credits_per_1000_tokens
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if output_credits_per_1000_tokens is not UNSET:
            field_dict["output_credits_per_1000_tokens"] = output_credits_per_1000_tokens
        if schema_documentation_url is not UNSET:
            field_dict["schema_documentation_url"] = schema_documentation_url
        if schema_notes is not UNSET:
            field_dict["schema_notes"] = schema_notes
        if tools_disabled is not UNSET:
            field_dict["tools_disabled"] = tools_disabled
        if tools_enabled is not UNSET:
            field_dict["tools_enabled"] = tools_enabled
        if url is not UNSET:
            field_dict["url"] = url
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_tool_response import PromptToolResponse
        from ..models.variant_category_response import VariantCategoryResponse

        d = dict(src_dict)
        default = d.pop("default")

        description = d.pop("description")

        enabled = d.pop("enabled")

        id = d.pop("id")

        max_conversation_length = d.pop("max_conversation_length")

        max_tokens = d.pop("max_tokens")

        model_id = d.pop("model_id")

        name = d.pop("name")

        provider = d.pop("provider")

        def _parse_input_1h_cache_write_credits_per_1000_tokens(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_1h_cache_write_credits_per_1000_tokens = _parse_input_1h_cache_write_credits_per_1000_tokens(
            d.pop("input_1h_cache_write_credits_per_1000_tokens", UNSET)
        )

        def _parse_input_5m_cache_write_credits_per_1000_tokens(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_5m_cache_write_credits_per_1000_tokens = _parse_input_5m_cache_write_credits_per_1000_tokens(
            d.pop("input_5m_cache_write_credits_per_1000_tokens", UNSET)
        )

        def _parse_input_cache_hit_credits_per_1000_tokens(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cache_hit_credits_per_1000_tokens = _parse_input_cache_hit_credits_per_1000_tokens(
            d.pop("input_cache_hit_credits_per_1000_tokens", UNSET)
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

        def _parse_schema_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_documentation_url = _parse_schema_documentation_url(d.pop("schema_documentation_url", UNSET))

        def _parse_schema_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_notes = _parse_schema_notes(d.pop("schema_notes", UNSET))

        _tools_disabled = d.pop("tools_disabled", UNSET)
        tools_disabled: list[PromptToolResponse] | Unset = UNSET
        if _tools_disabled is not UNSET:
            tools_disabled = []
            for tools_disabled_item_data in _tools_disabled:
                tools_disabled_item = PromptToolResponse.from_dict(tools_disabled_item_data)

                tools_disabled.append(tools_disabled_item)

        _tools_enabled = d.pop("tools_enabled", UNSET)
        tools_enabled: list[PromptToolResponse] | Unset = UNSET
        if _tools_enabled is not UNSET:
            tools_enabled = []
            for tools_enabled_item_data in _tools_enabled:
                tools_enabled_item = PromptToolResponse.from_dict(tools_enabled_item_data)

                tools_enabled.append(tools_enabled_item)

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
                    variants_type_0_item = VariantCategoryResponse.from_dict(variants_type_0_item_data)

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
            max_conversation_length=max_conversation_length,
            max_tokens=max_tokens,
            model_id=model_id,
            name=name,
            provider=provider,
            input_1h_cache_write_credits_per_1000_tokens=input_1h_cache_write_credits_per_1000_tokens,
            input_5m_cache_write_credits_per_1000_tokens=input_5m_cache_write_credits_per_1000_tokens,
            input_cache_hit_credits_per_1000_tokens=input_cache_hit_credits_per_1000_tokens,
            input_credits_per_1000_tokens=input_credits_per_1000_tokens,
            last_used=last_used,
            output_credits_per_1000_tokens=output_credits_per_1000_tokens,
            schema_documentation_url=schema_documentation_url,
            schema_notes=schema_notes,
            tools_disabled=tools_disabled,
            tools_enabled=tools_enabled,
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
