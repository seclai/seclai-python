from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_send_email_response_result_type_0 import (
        TestSendEmailResponseResultType0,
    )


T = TypeVar("T", bound="TestSendEmailResponse")


@_attrs_define
class TestSendEmailResponse:
    """Response from testing send email operation.

    Attributes:
        success (bool): Whether the send email test was successful
        error (None | str | Unset): Error message if test failed
        result (None | TestSendEmailResponseResultType0 | Unset): Email details (subject, html_body, text_body, sizes)
    """

    success: bool
    error: None | str | Unset = UNSET
    result: None | TestSendEmailResponseResultType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_send_email_response_result_type_0 import (
            TestSendEmailResponseResultType0,
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
        elif isinstance(self.result, TestSendEmailResponseResultType0):
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
        from ..models.test_send_email_response_result_type_0 import (
            TestSendEmailResponseResultType0,
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
        ) -> None | TestSendEmailResponseResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = TestSendEmailResponseResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestSendEmailResponseResultType0 | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        test_send_email_response = cls(
            success=success,
            error=error,
            result=result,
        )

        test_send_email_response.additional_properties = d
        return test_send_email_response

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
