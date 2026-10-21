from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.accepted_attachment_slot import AcceptedAttachmentSlot


T = TypeVar("T", bound="SetAcceptedAttachmentsRequest")


@_attrs_define
class SetAcceptedAttachmentsRequest:
    """
    Attributes:
        accepted_attachments (list[AcceptedAttachmentSlot] | None): The input attachments the trigger accepts; ``null``
            accepts any files (one attachment named ``files``). Only ``dynamic_input`` and ``email_received`` triggers take
            files.
    """

    accepted_attachments: list[AcceptedAttachmentSlot] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_attachments: list[dict[str, Any]] | None
        if isinstance(self.accepted_attachments, list):
            accepted_attachments = []
            for accepted_attachments_type_0_item_data in self.accepted_attachments:
                accepted_attachments_type_0_item = (
                    accepted_attachments_type_0_item_data.to_dict()
                )
                accepted_attachments.append(accepted_attachments_type_0_item)

        else:
            accepted_attachments = self.accepted_attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted_attachments": accepted_attachments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accepted_attachment_slot import AcceptedAttachmentSlot

        d = dict(src_dict)

        def _parse_accepted_attachments(
            data: object,
        ) -> list[AcceptedAttachmentSlot] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accepted_attachments_type_0 = []
                _accepted_attachments_type_0 = data
                for (
                    accepted_attachments_type_0_item_data
                ) in _accepted_attachments_type_0:
                    accepted_attachments_type_0_item = AcceptedAttachmentSlot.from_dict(
                        accepted_attachments_type_0_item_data
                    )

                    accepted_attachments_type_0.append(accepted_attachments_type_0_item)

                return accepted_attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AcceptedAttachmentSlot] | None, data)

        accepted_attachments = _parse_accepted_attachments(
            d.pop("accepted_attachments")
        )

        set_accepted_attachments_request = cls(
            accepted_attachments=accepted_attachments,
        )

        set_accepted_attachments_request.additional_properties = d
        return set_accepted_attachments_request

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
