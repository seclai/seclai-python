from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_field_error import ValidationFieldError


T = TypeVar("T", bound="ValidationErrorResponse")


@_attrs_define
class ValidationErrorResponse:
    """Response model for validation errors

    Attributes:
        error (str):
        validation_errors (list[ValidationFieldError]):
        success (bool | Unset):  Default: False.
    """

    error: str
    validation_errors: list[ValidationFieldError]
    success: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        validation_errors = []
        for validation_errors_item_data in self.validation_errors:
            validation_errors_item = validation_errors_item_data.to_dict()
            validation_errors.append(validation_errors_item)

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "validation_errors": validation_errors,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_field_error import ValidationFieldError

        d = dict(src_dict)
        error = d.pop("error")

        validation_errors = []
        _validation_errors = d.pop("validation_errors")
        for validation_errors_item_data in _validation_errors:
            validation_errors_item = ValidationFieldError.from_dict(validation_errors_item_data)

            validation_errors.append(validation_errors_item)

        success = d.pop("success", UNSET)

        validation_error_response = cls(
            error=error,
            validation_errors=validation_errors,
            success=success,
        )

        validation_error_response.additional_properties = d
        return validation_error_response

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
