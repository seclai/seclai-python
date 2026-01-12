from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_transform_request_placeholder_values import TestTransformRequestPlaceholderValues
    from ..models.transform_rule_test import TransformRuleTest


T = TypeVar("T", bound="TestTransformRequest")


@_attrs_define
class TestTransformRequest:
    """Request to test transform rules.

    Attributes:
        rules (list[TransformRuleTest]): List of transformation rules to apply sequentially
        test_input (str): The test input text to transform
        placeholder_values (TestTransformRequestPlaceholderValues | Unset): Values for {{...}} placeholders in the
            substitution strings
    """

    rules: list[TransformRuleTest]
    test_input: str
    placeholder_values: TestTransformRequestPlaceholderValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        test_input = self.test_input

        placeholder_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.placeholder_values, Unset):
            placeholder_values = self.placeholder_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
                "test_input": test_input,
            }
        )
        if placeholder_values is not UNSET:
            field_dict["placeholder_values"] = placeholder_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_transform_request_placeholder_values import TestTransformRequestPlaceholderValues
        from ..models.transform_rule_test import TransformRuleTest

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = TransformRuleTest.from_dict(rules_item_data)

            rules.append(rules_item)

        test_input = d.pop("test_input")

        _placeholder_values = d.pop("placeholder_values", UNSET)
        placeholder_values: TestTransformRequestPlaceholderValues | Unset
        if isinstance(_placeholder_values, Unset):
            placeholder_values = UNSET
        else:
            placeholder_values = TestTransformRequestPlaceholderValues.from_dict(_placeholder_values)

        test_transform_request = cls(
            rules=rules,
            test_input=test_input,
            placeholder_values=placeholder_values,
        )

        test_transform_request.additional_properties = d
        return test_transform_request

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
