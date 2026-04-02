from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.knowledge_base import KnowledgeBase


T = TypeVar("T", bound="KnowledgeBaseListResponseModel")


@_attrs_define
class KnowledgeBaseListResponseModel:
    """Paginated list of knowledge bases.

    Attributes:
        knowledge_bases (list[KnowledgeBase]): List of knowledge bases on this page.
        limit (int): Items per page.
        page (int): Current page number (1-based).
        total (int): Total number of knowledge bases.
    """

    knowledge_bases: list[KnowledgeBase]
    limit: int
    page: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_bases = []
        for knowledge_bases_item_data in self.knowledge_bases:
            knowledge_bases_item = knowledge_bases_item_data.to_dict()
            knowledge_bases.append(knowledge_bases_item)

        limit = self.limit

        page = self.page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_bases": knowledge_bases,
                "limit": limit,
                "page": page,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_base import KnowledgeBase

        d = dict(src_dict)
        knowledge_bases = []
        _knowledge_bases = d.pop("knowledge_bases")
        for knowledge_bases_item_data in _knowledge_bases:
            knowledge_bases_item = KnowledgeBase.from_dict(knowledge_bases_item_data)

            knowledge_bases.append(knowledge_bases_item)

        limit = d.pop("limit")

        page = d.pop("page")

        total = d.pop("total")

        knowledge_base_list_response_model = cls(
            knowledge_bases=knowledge_bases,
            limit=limit,
            page=page,
            total=total,
        )

        knowledge_base_list_response_model.additional_properties = d
        return knowledge_base_list_response_model

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
