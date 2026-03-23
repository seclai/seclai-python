from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestTransformResponse")


@_attrs_define
class TestTransformResponse:
    """Response from testing a transform rule.

    Attributes:
        success (bool): Whether the transformation was successful
        error (None | str | Unset): Error message if transformation failed
        intermediate_outputs (list[str] | None | Unset): List of outputs after each rule is applied (for multi-rule
            testing)
        matched (bool | None | Unset): Whether the pattern matched the input
        output (None | str | Unset): The transformed output text
        required_placeholders (list[str] | Unset): List of placeholder names found in the substitution string
        rule_matches (list[bool] | None | Unset): List of boolean values indicating whether each rule matched (in order)
    """

    success: bool
    error: None | str | Unset = UNSET
    intermediate_outputs: list[str] | None | Unset = UNSET
    matched: bool | None | Unset = UNSET
    output: None | str | Unset = UNSET
    required_placeholders: list[str] | Unset = UNSET
    rule_matches: list[bool] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        intermediate_outputs: list[str] | None | Unset
        if isinstance(self.intermediate_outputs, Unset):
            intermediate_outputs = UNSET
        elif isinstance(self.intermediate_outputs, list):
            intermediate_outputs = self.intermediate_outputs

        else:
            intermediate_outputs = self.intermediate_outputs

        matched: bool | None | Unset
        if isinstance(self.matched, Unset):
            matched = UNSET
        else:
            matched = self.matched

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        required_placeholders: list[str] | Unset = UNSET
        if not isinstance(self.required_placeholders, Unset):
            required_placeholders = self.required_placeholders

        rule_matches: list[bool] | None | Unset
        if isinstance(self.rule_matches, Unset):
            rule_matches = UNSET
        elif isinstance(self.rule_matches, list):
            rule_matches = self.rule_matches

        else:
            rule_matches = self.rule_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if intermediate_outputs is not UNSET:
            field_dict["intermediate_outputs"] = intermediate_outputs
        if matched is not UNSET:
            field_dict["matched"] = matched
        if output is not UNSET:
            field_dict["output"] = output
        if required_placeholders is not UNSET:
            field_dict["required_placeholders"] = required_placeholders
        if rule_matches is not UNSET:
            field_dict["rule_matches"] = rule_matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_intermediate_outputs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                intermediate_outputs_type_0 = cast(list[str], data)

                return intermediate_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        intermediate_outputs = _parse_intermediate_outputs(
            d.pop("intermediate_outputs", UNSET)
        )

        def _parse_matched(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        matched = _parse_matched(d.pop("matched", UNSET))

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        required_placeholders = cast(list[str], d.pop("required_placeholders", UNSET))

        def _parse_rule_matches(data: object) -> list[bool] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rule_matches_type_0 = cast(list[bool], data)

                return rule_matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool] | None | Unset, data)

        rule_matches = _parse_rule_matches(d.pop("rule_matches", UNSET))

        test_transform_response = cls(
            success=success,
            error=error,
            intermediate_outputs=intermediate_outputs,
            matched=matched,
            output=output,
            required_placeholders=required_placeholders,
            rule_matches=rule_matches,
        )

        test_transform_response.additional_properties = d
        return test_transform_response

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
