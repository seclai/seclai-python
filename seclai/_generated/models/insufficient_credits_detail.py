from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InsufficientCreditsDetail")


@_attrs_define
class InsufficientCreditsDetail:
    """``detail`` body for a 402 ``insufficient_credits`` response.

    Attributes:
        account_id (str): UUID of the account that ran out of credits.
        error (Literal['insufficient_credits']): Stable machine-readable error code.
        message (str): Human-readable explanation.
    """

    account_id: str
    error: Literal["insufficient_credits"]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        error = self.error

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "error": error,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        error = cast(Literal["insufficient_credits"], d.pop("error"))
        if error != "insufficient_credits":
            raise ValueError(
                f"error must match const 'insufficient_credits', got '{error}'"
            )

        message = d.pop("message")

        insufficient_credits_detail = cls(
            account_id=account_id,
            error=error,
            message=message,
        )

        insufficient_credits_detail.additional_properties = d
        return insufficient_credits_detail

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
