from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_webhook_call_request_headers_type_0 import (
        TestWebhookCallRequestHeadersType0,
    )


T = TypeVar("T", bound="TestWebhookCallRequest")


@_attrs_define
class TestWebhookCallRequest:
    """Request to test webhook call.

    Attributes:
        test_input (str): The test input to use in template substitution
        url (str): The webhook URL to call
        content_type (str | Unset): Content-Type header value Default: 'application/json'.
        headers (None | TestWebhookCallRequestHeadersType0 | Unset): Optional additional headers
        method (str | Unset): HTTP method (POST or PUT) Default: 'POST'.
        payload (None | str | Unset): Optional request payload template
    """

    test_input: str
    url: str
    content_type: str | Unset = "application/json"
    headers: None | TestWebhookCallRequestHeadersType0 | Unset = UNSET
    method: str | Unset = "POST"
    payload: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_webhook_call_request_headers_type_0 import (
            TestWebhookCallRequestHeadersType0,
        )

        test_input = self.test_input

        url = self.url

        content_type = self.content_type

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, TestWebhookCallRequestHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        method = self.method

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_input": test_input,
                "url": url,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_webhook_call_request_headers_type_0 import (
            TestWebhookCallRequestHeadersType0,
        )

        d = dict(src_dict)
        test_input = d.pop("test_input")

        url = d.pop("url")

        content_type = d.pop("content_type", UNSET)

        def _parse_headers(
            data: object,
        ) -> None | TestWebhookCallRequestHeadersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = TestWebhookCallRequestHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestWebhookCallRequestHeadersType0 | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        method = d.pop("method", UNSET)

        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))

        test_webhook_call_request = cls(
            test_input=test_input,
            url=url,
            content_type=content_type,
            headers=headers,
            method=method,
            payload=payload,
        )

        test_webhook_call_request.additional_properties = d
        return test_webhook_call_request

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
