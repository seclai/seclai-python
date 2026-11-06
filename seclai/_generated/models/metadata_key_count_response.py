from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_value_count_response import MetadataValueCountResponse


T = TypeVar("T", bound="MetadataKeyCountResponse")


@_attrs_define
class MetadataKeyCountResponse:
    """
    Attributes:
        distinct_values (int): How many different values it takes.
        items (int): Items in the window carrying the key.
        key (str): The item-metadata key.
        top_values (list[MetadataValueCountResponse]): Its 5 most frequent values, most frequent first.
    """

    distinct_values: int
    items: int
    key: str
    top_values: list[MetadataValueCountResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distinct_values = self.distinct_values

        items = self.items

        key = self.key

        top_values = []
        for top_values_item_data in self.top_values:
            top_values_item = top_values_item_data.to_dict()
            top_values.append(top_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "distinct_values": distinct_values,
                "items": items,
                "key": key,
                "top_values": top_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_value_count_response import MetadataValueCountResponse

        d = dict(src_dict)
        distinct_values = d.pop("distinct_values")

        items = d.pop("items")

        key = d.pop("key")

        top_values = []
        _top_values = d.pop("top_values")
        for top_values_item_data in _top_values:
            top_values_item = MetadataValueCountResponse.from_dict(top_values_item_data)

            top_values.append(top_values_item)

        metadata_key_count_response = cls(
            distinct_values=distinct_values,
            items=items,
            key=key,
            top_values=top_values,
        )

        metadata_key_count_response.additional_properties = d
        return metadata_key_count_response

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
