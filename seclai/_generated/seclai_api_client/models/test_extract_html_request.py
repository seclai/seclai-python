from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestExtractHtmlRequest")


@_attrs_define
class TestExtractHtmlRequest:
    """Request to test HTML extraction.

    Attributes:
        test_input (str): The test input text to parse as HTML
        expected_tag (None | str | Unset): Optional tag name to extract (e.g., 'div', 'body')
    """

    test_input: str
    expected_tag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_input = self.test_input

        expected_tag: None | str | Unset
        if isinstance(self.expected_tag, Unset):
            expected_tag = UNSET
        else:
            expected_tag = self.expected_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_input": test_input,
            }
        )
        if expected_tag is not UNSET:
            field_dict["expected_tag"] = expected_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_input = d.pop("test_input")

        def _parse_expected_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_tag = _parse_expected_tag(d.pop("expected_tag", UNSET))

        test_extract_html_request = cls(
            test_input=test_input,
            expected_tag=expected_tag,
        )

        test_extract_html_request.additional_properties = d
        return test_extract_html_request

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
