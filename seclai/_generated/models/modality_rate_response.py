from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModalityRateResponse")


@_attrs_define
class ModalityRateResponse:
    """Per-modality rate for an LLM that prices image/audio/video output
    (or input) at a rate distinct from the default text rate.

    Example: Gemini 3.1 Flash Image charges $3/1M output tokens for
    text but $60/1M output tokens for generated images.  The image rate
    surfaces here with ``modality="image"`` and ``output_credits_per_1000_tokens``
    set; the default text rate stays on the parent model fields.

        Attributes:
            modality (str):
            input_credits_per_1000_tokens (float | None | Unset):
            output_credits_per_1000_tokens (float | None | Unset):
    """

    modality: str
    input_credits_per_1000_tokens: float | None | Unset = UNSET
    output_credits_per_1000_tokens: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modality = self.modality

        input_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.input_credits_per_1000_tokens, Unset):
            input_credits_per_1000_tokens = UNSET
        else:
            input_credits_per_1000_tokens = self.input_credits_per_1000_tokens

        output_credits_per_1000_tokens: float | None | Unset
        if isinstance(self.output_credits_per_1000_tokens, Unset):
            output_credits_per_1000_tokens = UNSET
        else:
            output_credits_per_1000_tokens = self.output_credits_per_1000_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modality": modality,
            }
        )
        if input_credits_per_1000_tokens is not UNSET:
            field_dict["input_credits_per_1000_tokens"] = input_credits_per_1000_tokens
        if output_credits_per_1000_tokens is not UNSET:
            field_dict["output_credits_per_1000_tokens"] = (
                output_credits_per_1000_tokens
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        modality = d.pop("modality")

        def _parse_input_credits_per_1000_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_credits_per_1000_tokens = _parse_input_credits_per_1000_tokens(
            d.pop("input_credits_per_1000_tokens", UNSET)
        )

        def _parse_output_credits_per_1000_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_credits_per_1000_tokens = _parse_output_credits_per_1000_tokens(
            d.pop("output_credits_per_1000_tokens", UNSET)
        )

        modality_rate_response = cls(
            modality=modality,
            input_credits_per_1000_tokens=input_credits_per_1000_tokens,
            output_credits_per_1000_tokens=output_credits_per_1000_tokens,
        )

        modality_rate_response.additional_properties = d
        return modality_rate_response

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
