from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accepted_attachment_slot import AcceptedAttachmentSlot
    from ..models.update_agent_definition_request_definition import (
        UpdateAgentDefinitionRequestDefinition,
    )


T = TypeVar("T", bound="UpdateAgentDefinitionRequest")


@_attrs_define
class UpdateAgentDefinitionRequest:
    """
    Attributes:
        definition (UpdateAgentDefinitionRequestDefinition): The full agent definition (name, description, tags, steps).
            Steps form a tree workflow. Each step has a `step_type`, `id`, `name`, and type-specific config. Content
            enrichment steps (write_metadata, write_content_attachment, load_content_attachment, load_content) require
            content-triggered agents.
        expected_change_id (str): The change_id from the last GET, for optimistic locking.
        accepted_attachments (list[AcceptedAttachmentSlot] | None | Unset): When given, declared on the main branch's
            file-taking triggers in the same save, so the steps may read its slots as `{{agent.attachments.<slot>}}`;
            omitted, the triggers keep theirs.
    """

    definition: UpdateAgentDefinitionRequestDefinition
    expected_change_id: str
    accepted_attachments: list[AcceptedAttachmentSlot] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        definition = self.definition.to_dict()

        expected_change_id = self.expected_change_id

        accepted_attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.accepted_attachments, Unset):
            accepted_attachments = UNSET
        elif isinstance(self.accepted_attachments, list):
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
                "definition": definition,
                "expected_change_id": expected_change_id,
            }
        )
        if accepted_attachments is not UNSET:
            field_dict["accepted_attachments"] = accepted_attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accepted_attachment_slot import AcceptedAttachmentSlot
        from ..models.update_agent_definition_request_definition import (
            UpdateAgentDefinitionRequestDefinition,
        )

        d = dict(src_dict)
        definition = UpdateAgentDefinitionRequestDefinition.from_dict(
            d.pop("definition")
        )

        expected_change_id = d.pop("expected_change_id")

        def _parse_accepted_attachments(
            data: object,
        ) -> list[AcceptedAttachmentSlot] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(list[AcceptedAttachmentSlot] | None | Unset, data)

        accepted_attachments = _parse_accepted_attachments(
            d.pop("accepted_attachments", UNSET)
        )

        update_agent_definition_request = cls(
            definition=definition,
            expected_change_id=expected_change_id,
            accepted_attachments=accepted_attachments,
        )

        update_agent_definition_request.additional_properties = d
        return update_agent_definition_request

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
