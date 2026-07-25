from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.blocked_email_sender_response import BlockedEmailSenderResponse


T = TypeVar("T", bound="BlockedEmailSenderListResponse")


@_attrs_define
class BlockedEmailSenderListResponse:
    """A page of blocked senders + the account's auto-block mode.

    Attributes:
        auto_block_mode (str):
        items (list[BlockedEmailSenderResponse]):
        total (int):
    """

    auto_block_mode: str
    items: list[BlockedEmailSenderResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_block_mode = self.auto_block_mode

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auto_block_mode": auto_block_mode,
                "items": items,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blocked_email_sender_response import BlockedEmailSenderResponse

        d = dict(src_dict)
        auto_block_mode = d.pop("auto_block_mode")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = BlockedEmailSenderResponse.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        blocked_email_sender_list_response = cls(
            auto_block_mode=auto_block_mode,
            items=items,
            total=total,
        )

        blocked_email_sender_list_response.additional_properties = d
        return blocked_email_sender_list_response

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
