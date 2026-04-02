from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.memory_bank import MemoryBank


T = TypeVar("T", bound="MemoryBankListResponseModel")


@_attrs_define
class MemoryBankListResponseModel:
    """Paginated list of memory banks.

    Attributes:
        limit (int): Items per page.
        memory_banks (list[MemoryBank]): List of memory banks on this page.
        page (int): Current page number (1-based).
        total (int): Total number of memory banks.
    """

    limit: int
    memory_banks: list[MemoryBank]
    page: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        memory_banks = []
        for memory_banks_item_data in self.memory_banks:
            memory_banks_item = memory_banks_item_data.to_dict()
            memory_banks.append(memory_banks_item)

        page = self.page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "memory_banks": memory_banks,
                "page": page,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_bank import MemoryBank

        d = dict(src_dict)
        limit = d.pop("limit")

        memory_banks = []
        _memory_banks = d.pop("memory_banks")
        for memory_banks_item_data in _memory_banks:
            memory_banks_item = MemoryBank.from_dict(memory_banks_item_data)

            memory_banks.append(memory_banks_item)

        page = d.pop("page")

        total = d.pop("total")

        memory_bank_list_response_model = cls(
            limit=limit,
            memory_banks=memory_banks,
            page=page,
            total=total,
        )

        memory_bank_list_response_model.additional_properties = d
        return memory_bank_list_response_model

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
