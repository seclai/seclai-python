from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestDisplayResultRequest")


@_attrs_define
class TestDisplayResultRequest:
    """Request to test display result template.

    Attributes:
        test_input (str): The test input to use in template substitution
        html_format (bool | Unset): Whether to format as HTML or plain text Default: True.
        template (None | str | Unset): Template string with substitution variables like {{input}}
    """

    test_input: str
    html_format: bool | Unset = True
    template: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_input = self.test_input

        html_format = self.html_format

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_input": test_input,
            }
        )
        if html_format is not UNSET:
            field_dict["html_format"] = html_format
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_input = d.pop("test_input")

        html_format = d.pop("html_format", UNSET)

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        test_display_result_request = cls(
            test_input=test_input,
            html_format=html_format,
            template=template,
        )

        test_display_result_request.additional_properties = d
        return test_display_result_request

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
