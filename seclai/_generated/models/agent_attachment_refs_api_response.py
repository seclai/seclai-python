from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accepted_attachment_slot import AcceptedAttachmentSlot
    from ..models.attachment_refs_source_api_summary import (
        AttachmentRefsSourceApiSummary,
    )


T = TypeVar("T", bound="AgentAttachmentRefsApiResponse")


@_attrs_define
class AgentAttachmentRefsApiResponse:
    """The input attachments an agent's trigger declares.

    Mirrors the MCP ``get_agent_attachment_references`` tool, so API
    consumers can stage uploads that fit before calling
    ``POST /agents/{id}/runs``.

        Attributes:
            requires_uploads (bool): When ``false`` the agent takes no files through the API — it has no ``dynamic_input``
                trigger, or that trigger declares no attachments — and ``POST /agents/{id}/upload-input`` will reject with HTTP
                400. When ``true`` ``accepted_attachments`` lists what a run's files must fit.
            accepted_attachments (list[AcceptedAttachmentSlot] | Unset): The attachments the agent's trigger declares. A
                run's files are each assigned to one; a file none accepts, or an attachment with fewer files than its ``min``,
                rejects the run with HTTP 400. Steps reference one as ``{{agent.attachments.<name>}}``.
            agent (AttachmentRefsSourceApiSummary | Unset): Per-source attachment-reference summary.
    """

    requires_uploads: bool
    accepted_attachments: list[AcceptedAttachmentSlot] | Unset = UNSET
    agent: AttachmentRefsSourceApiSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requires_uploads = self.requires_uploads

        accepted_attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accepted_attachments, Unset):
            accepted_attachments = []
            for accepted_attachments_item_data in self.accepted_attachments:
                accepted_attachments_item = accepted_attachments_item_data.to_dict()
                accepted_attachments.append(accepted_attachments_item)

        agent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agent, Unset):
            agent = self.agent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requires_uploads": requires_uploads,
            }
        )
        if accepted_attachments is not UNSET:
            field_dict["accepted_attachments"] = accepted_attachments
        if agent is not UNSET:
            field_dict["agent"] = agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accepted_attachment_slot import AcceptedAttachmentSlot
        from ..models.attachment_refs_source_api_summary import (
            AttachmentRefsSourceApiSummary,
        )

        d = dict(src_dict)
        requires_uploads = d.pop("requires_uploads")

        _accepted_attachments = d.pop("accepted_attachments", UNSET)
        accepted_attachments: list[AcceptedAttachmentSlot] | Unset = UNSET
        if _accepted_attachments is not UNSET:
            accepted_attachments = []
            for accepted_attachments_item_data in _accepted_attachments:
                accepted_attachments_item = AcceptedAttachmentSlot.from_dict(
                    accepted_attachments_item_data
                )

                accepted_attachments.append(accepted_attachments_item)

        _agent = d.pop("agent", UNSET)
        agent: AttachmentRefsSourceApiSummary | Unset
        if isinstance(_agent, Unset):
            agent = UNSET
        else:
            agent = AttachmentRefsSourceApiSummary.from_dict(_agent)

        agent_attachment_refs_api_response = cls(
            requires_uploads=requires_uploads,
            accepted_attachments=accepted_attachments,
            agent=agent,
        )

        agent_attachment_refs_api_response.additional_properties = d
        return agent_attachment_refs_api_response

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
