from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_import_preview_response_unresolved_refs_item import (
        AgentImportPreviewResponseUnresolvedRefsItem,
    )


T = TypeVar("T", bound="AgentImportPreviewResponse")


@_attrs_define
class AgentImportPreviewResponse:
    """Summary of a successfully validated import payload (no DB writes).

    Counts are derived from the validated payload as supplied — they
    reflect what was requested, not what would eventually be persisted
    (cross-account skips for recipients and KB names happen later, only
    on commit).

        Attributes:
            agent_name (None | str): Imported agent name, if any.
            alert_configs (int): Number of alert configs in the payload.
            description (None | str): Imported agent description, if any.
            evaluation_criteria (int): Number of evaluation criteria in the payload.
            governance_policies (int): Number of agent-scoped governance policies in the payload.
            ok (bool): Always true on a 200 response; failures use HTTP 422.
            schedules (int): Number of trigger schedules in the payload.
            step_count (int): Total number of steps in the workflow tree (recursive).
            payload_export_version (None | str | Unset): Export-format version the payload claims (or ``null`` for legacy
                payloads).  When this differs from ``supported_export_version``, fields may have been silently dropped or
                defaulted on import.
            solutions (int | Unset): Number of solutions the source agent belonged to. On import these are matched by name
                in the target account; unmatched names are silently skipped. Default: 0.
            supported_export_version (str | Unset): Export-format version this server understands.  Compare against
                ``payload_export_version`` to detect cross-version imports. Default: '2'.
            unresolved_refs (list[AgentImportPreviewResponseUnresolvedRefsItem] | Unset): Entity references in the imported
                workflow that don't exist in the target account.  Each entry: {category, ref_id, ref_name?,
                locations:[step:<id>], alternatives:[{id, name, description?}]}. Pass {source_uuid: target_uuid} as
                ``entity_remap`` on the create/update call to substitute these references before save.
    """

    agent_name: None | str
    alert_configs: int
    description: None | str
    evaluation_criteria: int
    governance_policies: int
    ok: bool
    schedules: int
    step_count: int
    payload_export_version: None | str | Unset = UNSET
    solutions: int | Unset = 0
    supported_export_version: str | Unset = "2"
    unresolved_refs: list[AgentImportPreviewResponseUnresolvedRefsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_name: None | str
        agent_name = self.agent_name

        alert_configs = self.alert_configs

        description: None | str
        description = self.description

        evaluation_criteria = self.evaluation_criteria

        governance_policies = self.governance_policies

        ok = self.ok

        schedules = self.schedules

        step_count = self.step_count

        payload_export_version: None | str | Unset
        if isinstance(self.payload_export_version, Unset):
            payload_export_version = UNSET
        else:
            payload_export_version = self.payload_export_version

        solutions = self.solutions

        supported_export_version = self.supported_export_version

        unresolved_refs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unresolved_refs, Unset):
            unresolved_refs = []
            for unresolved_refs_item_data in self.unresolved_refs:
                unresolved_refs_item = unresolved_refs_item_data.to_dict()
                unresolved_refs.append(unresolved_refs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_name": agent_name,
                "alert_configs": alert_configs,
                "description": description,
                "evaluation_criteria": evaluation_criteria,
                "governance_policies": governance_policies,
                "ok": ok,
                "schedules": schedules,
                "step_count": step_count,
            }
        )
        if payload_export_version is not UNSET:
            field_dict["payload_export_version"] = payload_export_version
        if solutions is not UNSET:
            field_dict["solutions"] = solutions
        if supported_export_version is not UNSET:
            field_dict["supported_export_version"] = supported_export_version
        if unresolved_refs is not UNSET:
            field_dict["unresolved_refs"] = unresolved_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_import_preview_response_unresolved_refs_item import (
            AgentImportPreviewResponseUnresolvedRefsItem,
        )

        d = dict(src_dict)

        def _parse_agent_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_name = _parse_agent_name(d.pop("agent_name"))

        alert_configs = d.pop("alert_configs")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        evaluation_criteria = d.pop("evaluation_criteria")

        governance_policies = d.pop("governance_policies")

        ok = d.pop("ok")

        schedules = d.pop("schedules")

        step_count = d.pop("step_count")

        def _parse_payload_export_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload_export_version = _parse_payload_export_version(
            d.pop("payload_export_version", UNSET)
        )

        solutions = d.pop("solutions", UNSET)

        supported_export_version = d.pop("supported_export_version", UNSET)

        _unresolved_refs = d.pop("unresolved_refs", UNSET)
        unresolved_refs: list[AgentImportPreviewResponseUnresolvedRefsItem] | Unset = (
            UNSET
        )
        if _unresolved_refs is not UNSET:
            unresolved_refs = []
            for unresolved_refs_item_data in _unresolved_refs:
                unresolved_refs_item = (
                    AgentImportPreviewResponseUnresolvedRefsItem.from_dict(
                        unresolved_refs_item_data
                    )
                )

                unresolved_refs.append(unresolved_refs_item)

        agent_import_preview_response = cls(
            agent_name=agent_name,
            alert_configs=alert_configs,
            description=description,
            evaluation_criteria=evaluation_criteria,
            governance_policies=governance_policies,
            ok=ok,
            schedules=schedules,
            step_count=step_count,
            payload_export_version=payload_export_version,
            solutions=solutions,
            supported_export_version=supported_export_version,
            unresolved_refs=unresolved_refs,
        )

        agent_import_preview_response.additional_properties = d
        return agent_import_preview_response

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
