from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.compatible_run_response import CompatibleRunResponse


T = TypeVar("T", bound="CompatibleRunListResponse")


@_attrs_define
class CompatibleRunListResponse:
    """Paginated list of compatible runs.

    Attributes:
        data (list[CompatibleRunResponse]):
        limit (int):
        page (int):
        total (int):
    """

    data: list[CompatibleRunResponse]
    limit: int
    page: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        limit = self.limit

        page = self.page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "limit": limit,
                "page": page,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compatible_run_response import CompatibleRunResponse

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CompatibleRunResponse.from_dict(data_item_data)

            data.append(data_item)

        limit = d.pop("limit")

        page = d.pop("page")

        total = d.pop("total")

        compatible_run_list_response = cls(
            data=data,
            limit=limit,
            page=page,
            total=total,
        )

        compatible_run_list_response.additional_properties = d
        return compatible_run_list_response

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
