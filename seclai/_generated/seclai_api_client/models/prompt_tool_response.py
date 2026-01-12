from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_tool_response_headers_type_0 import (
        PromptToolResponseHeadersType0,
    )


T = TypeVar("T", bound="PromptToolResponse")


@_attrs_define
class PromptToolResponse:
    """Response model for a prompt tool.

    Attributes:
        id (str):
        name (str):
        tool_type (str):
        description (None | str | Unset):
        documentation_url (None | str | Unset):
        example (None | str | Unset):
        headers (None | PromptToolResponseHeadersType0 | Unset):
        notes (None | str | Unset):
        tool_name (None | str | Unset):
        tool_type_pattern (None | str | Unset):
    """

    id: str
    name: str
    tool_type: str
    description: None | str | Unset = UNSET
    documentation_url: None | str | Unset = UNSET
    example: None | str | Unset = UNSET
    headers: None | PromptToolResponseHeadersType0 | Unset = UNSET
    notes: None | str | Unset = UNSET
    tool_name: None | str | Unset = UNSET
    tool_type_pattern: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_tool_response_headers_type_0 import (
            PromptToolResponseHeadersType0,
        )

        id = self.id

        name = self.name

        tool_type = self.tool_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        example: None | str | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, PromptToolResponseHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        tool_name: None | str | Unset
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        tool_type_pattern: None | str | Unset
        if isinstance(self.tool_type_pattern, Unset):
            tool_type_pattern = UNSET
        else:
            tool_type_pattern = self.tool_type_pattern

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "tool_type": tool_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if example is not UNSET:
            field_dict["example"] = example
        if headers is not UNSET:
            field_dict["headers"] = headers
        if notes is not UNSET:
            field_dict["notes"] = notes
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
        if tool_type_pattern is not UNSET:
            field_dict["tool_type_pattern"] = tool_type_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_tool_response_headers_type_0 import (
            PromptToolResponseHeadersType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        tool_type = d.pop("tool_type")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

        def _parse_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example = _parse_example(d.pop("example", UNSET))

        def _parse_headers(
            data: object,
        ) -> None | PromptToolResponseHeadersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = PromptToolResponseHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptToolResponseHeadersType0 | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_tool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))

        def _parse_tool_type_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_type_pattern = _parse_tool_type_pattern(d.pop("tool_type_pattern", UNSET))

        prompt_tool_response = cls(
            id=id,
            name=name,
            tool_type=tool_type,
            description=description,
            documentation_url=documentation_url,
            example=example,
            headers=headers,
            notes=notes,
            tool_name=tool_name,
            tool_type_pattern=tool_type_pattern,
        )

        prompt_tool_response.additional_properties = d
        return prompt_tool_response

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
