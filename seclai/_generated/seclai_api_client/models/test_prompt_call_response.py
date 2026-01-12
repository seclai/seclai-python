from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_prompt_call_response_result_type_0 import (
        TestPromptCallResponseResultType0,
    )


T = TypeVar("T", bound="TestPromptCallResponse")


@_attrs_define
class TestPromptCallResponse:
    """Response from testing prompt call operation.

    Attributes:
        success (bool): Whether the prompt call test was successful
        error (None | str | Unset): Error message if test failed
        result (None | TestPromptCallResponseResultType0 | Unset): Prompt call details (prompt, system, response,
            tokens)
    """

    success: bool
    error: None | str | Unset = UNSET
    result: None | TestPromptCallResponseResultType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_prompt_call_response_result_type_0 import (
            TestPromptCallResponseResultType0,
        )

        success = self.success

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, TestPromptCallResponseResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_prompt_call_response_result_type_0 import (
            TestPromptCallResponseResultType0,
        )

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_result(
            data: object,
        ) -> None | TestPromptCallResponseResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = TestPromptCallResponseResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestPromptCallResponseResultType0 | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        test_prompt_call_response = cls(
            success=success,
            error=error,
            result=result,
        )

        test_prompt_call_response.additional_properties = d
        return test_prompt_call_response

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
