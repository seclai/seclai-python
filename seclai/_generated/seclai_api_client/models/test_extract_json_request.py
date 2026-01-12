from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_type import JsonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestExtractJsonRequest")


@_attrs_define
class TestExtractJsonRequest:
    """Request to test JSON extraction.

    Attributes:
        expected_type (JsonType): JSON types for extraction.
        test_input (str): The test input text containing JSON
        json_path (None | str | Unset): Optional JSONPath query to apply after extraction
    """

    expected_type: JsonType
    test_input: str
    json_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_type = self.expected_type.value

        test_input = self.test_input

        json_path: None | str | Unset
        if isinstance(self.json_path, Unset):
            json_path = UNSET
        else:
            json_path = self.json_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expected_type": expected_type,
                "test_input": test_input,
            }
        )
        if json_path is not UNSET:
            field_dict["json_path"] = json_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_type = JsonType(d.pop("expected_type"))

        test_input = d.pop("test_input")

        def _parse_json_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        json_path = _parse_json_path(d.pop("json_path", UNSET))

        test_extract_json_request = cls(
            expected_type=expected_type,
            test_input=test_input,
            json_path=json_path,
        )

        test_extract_json_request.additional_properties = d
        return test_extract_json_request

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
