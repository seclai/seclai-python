from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_webhook_call_response_request_type_0 import TestWebhookCallResponseRequestType0
    from ..models.test_webhook_call_response_response_type_0 import TestWebhookCallResponseResponseType0


T = TypeVar("T", bound="TestWebhookCallResponse")


@_attrs_define
class TestWebhookCallResponse:
    """Response from testing webhook call.

    Attributes:
        success (bool): Whether the webhook call was successful
        error (None | str | Unset): Error message if call failed
        request (None | TestWebhookCallResponseRequestType0 | Unset): Request details (url, method, headers, body)
        response (None | TestWebhookCallResponseResponseType0 | Unset): Response details (status_code, headers, body)
    """

    success: bool
    error: None | str | Unset = UNSET
    request: None | TestWebhookCallResponseRequestType0 | Unset = UNSET
    response: None | TestWebhookCallResponseResponseType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_webhook_call_response_request_type_0 import TestWebhookCallResponseRequestType0
        from ..models.test_webhook_call_response_response_type_0 import TestWebhookCallResponseResponseType0

        success = self.success

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        request: dict[str, Any] | None | Unset
        if isinstance(self.request, Unset):
            request = UNSET
        elif isinstance(self.request, TestWebhookCallResponseRequestType0):
            request = self.request.to_dict()
        else:
            request = self.request

        response: dict[str, Any] | None | Unset
        if isinstance(self.response, Unset):
            response = UNSET
        elif isinstance(self.response, TestWebhookCallResponseResponseType0):
            response = self.response.to_dict()
        else:
            response = self.response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if request is not UNSET:
            field_dict["request"] = request
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_webhook_call_response_request_type_0 import TestWebhookCallResponseRequestType0
        from ..models.test_webhook_call_response_response_type_0 import TestWebhookCallResponseResponseType0

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_request(data: object) -> None | TestWebhookCallResponseRequestType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_type_0 = TestWebhookCallResponseRequestType0.from_dict(data)

                return request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestWebhookCallResponseRequestType0 | Unset, data)

        request = _parse_request(d.pop("request", UNSET))

        def _parse_response(data: object) -> None | TestWebhookCallResponseResponseType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_0 = TestWebhookCallResponseResponseType0.from_dict(data)

                return response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestWebhookCallResponseResponseType0 | Unset, data)

        response = _parse_response(d.pop("response", UNSET))

        test_webhook_call_response = cls(
            success=success,
            error=error,
            request=request,
            response=response,
        )

        test_webhook_call_response.additional_properties = d
        return test_webhook_call_response

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
