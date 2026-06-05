from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.insufficient_credits_detail import InsufficientCreditsDetail


T = TypeVar("T", bound="InsufficientCreditsResponse")


@_attrs_define
class InsufficientCreditsResponse:
    """402 envelope returned when the account has exhausted its credits.

    Attributes:
        detail (InsufficientCreditsDetail): ``detail`` body for a 402 ``insufficient_credits`` response.
    """

    detail: InsufficientCreditsDetail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insufficient_credits_detail import InsufficientCreditsDetail

        d = dict(src_dict)
        detail = InsufficientCreditsDetail.from_dict(d.pop("detail"))

        insufficient_credits_response = cls(
            detail=detail,
        )

        insufficient_credits_response.additional_properties = d
        return insufficient_credits_response

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
