from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_response import PaginationResponse
    from ..models.source_response import SourceResponse


T = TypeVar("T", bound="SourceListResponse")


@_attrs_define
class SourceListResponse:
    """Response model for paginated source list

    Attributes:
        data (list[SourceResponse]):
        pagination (PaginationResponse): Pagination information.
    """

    data: list[SourceResponse]
    pagination: PaginationResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_response import PaginationResponse
        from ..models.source_response import SourceResponse

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SourceResponse.from_dict(data_item_data)

            data.append(data_item)

        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        source_list_response = cls(
            data=data,
            pagination=pagination,
        )

        source_list_response.additional_properties = d
        return source_list_response

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
