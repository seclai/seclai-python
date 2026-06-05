from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_refs_source_api_summary import (
        AttachmentRefsSourceApiSummary,
    )


T = TypeVar("T", bound="AgentAttachmentRefsApiResponse")


@_attrs_define
class AgentAttachmentRefsApiResponse:
    """Static attachment-reference contract for an agent.

    Mirrors the MCP ``get_agent_attachment_references`` tool: returns
    what files (if any) an agent's templates expect on a run so API
    consumers can stage uploads correctly before calling
    ``POST /agents/{id}/runs``.

        Attributes:
            requires_uploads (bool): When ``false`` the agent's definition does NOT reference any uploaded attachments —
                ``POST /agents/{id}/upload-input`` will reject with HTTP 400. When ``true`` the ``agent`` block lists the
                specific selectors a run-time batch must satisfy.
            agent (AttachmentRefsSourceApiSummary | Unset): Per-source attachment-reference summary.
    """

    requires_uploads: bool
    agent: AttachmentRefsSourceApiSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requires_uploads = self.requires_uploads

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
        if agent is not UNSET:
            field_dict["agent"] = agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_refs_source_api_summary import (
            AttachmentRefsSourceApiSummary,
        )

        d = dict(src_dict)
        requires_uploads = d.pop("requires_uploads")

        _agent = d.pop("agent", UNSET)
        agent: AttachmentRefsSourceApiSummary | Unset
        if isinstance(_agent, Unset):
            agent = UNSET
        else:
            agent = AttachmentRefsSourceApiSummary.from_dict(_agent)

        agent_attachment_refs_api_response = cls(
            requires_uploads=requires_uploads,
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
