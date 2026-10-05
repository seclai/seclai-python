from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_unavailable_error_error import ServiceUnavailableErrorError


T = TypeVar("T", bound="ServiceUnavailableError")


@_attrs_define
class ServiceUnavailableError:
    """
    Attributes:
        error (ServiceUnavailableErrorError):
    """

    error: ServiceUnavailableErrorError
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_unavailable_error_error import (
            ServiceUnavailableErrorError,
        )

        d = dict(src_dict)
        error = ServiceUnavailableErrorError.from_dict(d.pop("error"))

        service_unavailable_error = cls(
            error=error,
        )

        service_unavailable_error.additional_properties = d
        return service_unavailable_error

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
