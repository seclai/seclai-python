from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestS3WriteRequest")


@_attrs_define
class TestS3WriteRequest:
    """Request to test S3 write operation.

    Attributes:
        bucket_name (str): The S3 bucket name
        content (str): Content to write
        object_key (str): The S3 object key (path)
        test_input (str): The test input to use in template substitution
        content_type (str | Unset): Content-Type Default: 'text/plain'.
    """

    bucket_name: str
    content: str
    object_key: str
    test_input: str
    content_type: str | Unset = "text/plain"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_name = self.bucket_name

        content = self.content

        object_key = self.object_key

        test_input = self.test_input

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_name": bucket_name,
                "content": content,
                "object_key": object_key,
                "test_input": test_input,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_name = d.pop("bucket_name")

        content = d.pop("content")

        object_key = d.pop("object_key")

        test_input = d.pop("test_input")

        content_type = d.pop("content_type", UNSET)

        test_s3_write_request = cls(
            bucket_name=bucket_name,
            content=content,
            object_key=object_key,
            test_input=test_input,
            content_type=content_type,
        )

        test_s3_write_request.additional_properties = d
        return test_s3_write_request

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
