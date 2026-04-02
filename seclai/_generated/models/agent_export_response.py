from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_export_response_agent import AgentExportResponseAgent
    from ..models.agent_export_response_alert_configs_type_0_item import (
        AgentExportResponseAlertConfigsType0Item,
    )
    from ..models.agent_export_response_dependencies_type_0 import (
        AgentExportResponseDependenciesType0,
    )
    from ..models.agent_export_response_evaluation_criteria_type_0_item import (
        AgentExportResponseEvaluationCriteriaType0Item,
    )
    from ..models.agent_export_response_governance_policies_type_0_item import (
        AgentExportResponseGovernancePoliciesType0Item,
    )
    from ..models.agent_export_response_trigger_type_0 import (
        AgentExportResponseTriggerType0,
    )


T = TypeVar("T", bound="AgentExportResponse")


@_attrs_define
class AgentExportResponse:
    """Portable JSON snapshot of an agent definition.

    Attributes:
        agent (AgentExportResponseAgent): Agent metadata and full definition. Keys: name, description, schema_version,
            definition, default_evaluation_tier, evaluation_mode, sampling_config, max_retries, retry_on_failure,
            prompt_model_auto_upgrade_strategy, prompt_model_auto_rollback_enabled, prompt_model_auto_rollback_triggers,
            created_at, updated_at.
        export_version (str): Schema version of the export format (currently "2").
        exported_at (str): ISO-8601 timestamp of when the export was generated.
        software_version (str): Application version that produced this export.
        alert_configs (list[AgentExportResponseAlertConfigsType0Item] | None | Unset): Alert configurations.
        dependencies (AgentExportResponseDependenciesType0 | None | Unset): Resolved dependency manifest. Keys:
            knowledge_bases, memory_banks, source_connections, agents, users — each a list of {id, name, description, …}.
        evaluation_criteria (list[AgentExportResponseEvaluationCriteriaType0Item] | None | Unset): Evaluation criteria
            for agent steps.
        governance_policies (list[AgentExportResponseGovernancePoliciesType0Item] | None | Unset): Agent-scoped
            governance policies.
        trigger (AgentExportResponseTriggerType0 | None | Unset): Trigger configuration with schedules.
    """

    agent: AgentExportResponseAgent
    export_version: str
    exported_at: str
    software_version: str
    alert_configs: list[AgentExportResponseAlertConfigsType0Item] | None | Unset = UNSET
    dependencies: AgentExportResponseDependenciesType0 | None | Unset = UNSET
    evaluation_criteria: (
        list[AgentExportResponseEvaluationCriteriaType0Item] | None | Unset
    ) = UNSET
    governance_policies: (
        list[AgentExportResponseGovernancePoliciesType0Item] | None | Unset
    ) = UNSET
    trigger: AgentExportResponseTriggerType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_export_response_dependencies_type_0 import (
            AgentExportResponseDependenciesType0,
        )
        from ..models.agent_export_response_trigger_type_0 import (
            AgentExportResponseTriggerType0,
        )

        agent = self.agent.to_dict()

        export_version = self.export_version

        exported_at = self.exported_at

        software_version = self.software_version

        alert_configs: list[dict[str, Any]] | None | Unset
        if isinstance(self.alert_configs, Unset):
            alert_configs = UNSET
        elif isinstance(self.alert_configs, list):
            alert_configs = []
            for alert_configs_type_0_item_data in self.alert_configs:
                alert_configs_type_0_item = alert_configs_type_0_item_data.to_dict()
                alert_configs.append(alert_configs_type_0_item)

        else:
            alert_configs = self.alert_configs

        dependencies: dict[str, Any] | None | Unset
        if isinstance(self.dependencies, Unset):
            dependencies = UNSET
        elif isinstance(self.dependencies, AgentExportResponseDependenciesType0):
            dependencies = self.dependencies.to_dict()
        else:
            dependencies = self.dependencies

        evaluation_criteria: list[dict[str, Any]] | None | Unset
        if isinstance(self.evaluation_criteria, Unset):
            evaluation_criteria = UNSET
        elif isinstance(self.evaluation_criteria, list):
            evaluation_criteria = []
            for evaluation_criteria_type_0_item_data in self.evaluation_criteria:
                evaluation_criteria_type_0_item = (
                    evaluation_criteria_type_0_item_data.to_dict()
                )
                evaluation_criteria.append(evaluation_criteria_type_0_item)

        else:
            evaluation_criteria = self.evaluation_criteria

        governance_policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.governance_policies, Unset):
            governance_policies = UNSET
        elif isinstance(self.governance_policies, list):
            governance_policies = []
            for governance_policies_type_0_item_data in self.governance_policies:
                governance_policies_type_0_item = (
                    governance_policies_type_0_item_data.to_dict()
                )
                governance_policies.append(governance_policies_type_0_item)

        else:
            governance_policies = self.governance_policies

        trigger: dict[str, Any] | None | Unset
        if isinstance(self.trigger, Unset):
            trigger = UNSET
        elif isinstance(self.trigger, AgentExportResponseTriggerType0):
            trigger = self.trigger.to_dict()
        else:
            trigger = self.trigger

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "export_version": export_version,
                "exported_at": exported_at,
                "software_version": software_version,
            }
        )
        if alert_configs is not UNSET:
            field_dict["alert_configs"] = alert_configs
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if evaluation_criteria is not UNSET:
            field_dict["evaluation_criteria"] = evaluation_criteria
        if governance_policies is not UNSET:
            field_dict["governance_policies"] = governance_policies
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_export_response_agent import AgentExportResponseAgent
        from ..models.agent_export_response_alert_configs_type_0_item import (
            AgentExportResponseAlertConfigsType0Item,
        )
        from ..models.agent_export_response_dependencies_type_0 import (
            AgentExportResponseDependenciesType0,
        )
        from ..models.agent_export_response_evaluation_criteria_type_0_item import (
            AgentExportResponseEvaluationCriteriaType0Item,
        )
        from ..models.agent_export_response_governance_policies_type_0_item import (
            AgentExportResponseGovernancePoliciesType0Item,
        )
        from ..models.agent_export_response_trigger_type_0 import (
            AgentExportResponseTriggerType0,
        )

        d = dict(src_dict)
        agent = AgentExportResponseAgent.from_dict(d.pop("agent"))

        export_version = d.pop("export_version")

        exported_at = d.pop("exported_at")

        software_version = d.pop("software_version")

        def _parse_alert_configs(
            data: object,
        ) -> list[AgentExportResponseAlertConfigsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_configs_type_0 = []
                _alert_configs_type_0 = data
                for alert_configs_type_0_item_data in _alert_configs_type_0:
                    alert_configs_type_0_item = (
                        AgentExportResponseAlertConfigsType0Item.from_dict(
                            alert_configs_type_0_item_data
                        )
                    )

                    alert_configs_type_0.append(alert_configs_type_0_item)

                return alert_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AgentExportResponseAlertConfigsType0Item] | None | Unset, data
            )

        alert_configs = _parse_alert_configs(d.pop("alert_configs", UNSET))

        def _parse_dependencies(
            data: object,
        ) -> AgentExportResponseDependenciesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dependencies_type_0 = AgentExportResponseDependenciesType0.from_dict(
                    data
                )

                return dependencies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExportResponseDependenciesType0 | None | Unset, data)

        dependencies = _parse_dependencies(d.pop("dependencies", UNSET))

        def _parse_evaluation_criteria(
            data: object,
        ) -> list[AgentExportResponseEvaluationCriteriaType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evaluation_criteria_type_0 = []
                _evaluation_criteria_type_0 = data
                for evaluation_criteria_type_0_item_data in _evaluation_criteria_type_0:
                    evaluation_criteria_type_0_item = (
                        AgentExportResponseEvaluationCriteriaType0Item.from_dict(
                            evaluation_criteria_type_0_item_data
                        )
                    )

                    evaluation_criteria_type_0.append(evaluation_criteria_type_0_item)

                return evaluation_criteria_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AgentExportResponseEvaluationCriteriaType0Item] | None | Unset,
                data,
            )

        evaluation_criteria = _parse_evaluation_criteria(
            d.pop("evaluation_criteria", UNSET)
        )

        def _parse_governance_policies(
            data: object,
        ) -> list[AgentExportResponseGovernancePoliciesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                governance_policies_type_0 = []
                _governance_policies_type_0 = data
                for governance_policies_type_0_item_data in _governance_policies_type_0:
                    governance_policies_type_0_item = (
                        AgentExportResponseGovernancePoliciesType0Item.from_dict(
                            governance_policies_type_0_item_data
                        )
                    )

                    governance_policies_type_0.append(governance_policies_type_0_item)

                return governance_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AgentExportResponseGovernancePoliciesType0Item] | None | Unset,
                data,
            )

        governance_policies = _parse_governance_policies(
            d.pop("governance_policies", UNSET)
        )

        def _parse_trigger(
            data: object,
        ) -> AgentExportResponseTriggerType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trigger_type_0 = AgentExportResponseTriggerType0.from_dict(data)

                return trigger_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExportResponseTriggerType0 | None | Unset, data)

        trigger = _parse_trigger(d.pop("trigger", UNSET))

        agent_export_response = cls(
            agent=agent,
            export_version=export_version,
            exported_at=exported_at,
            software_version=software_version,
            alert_configs=alert_configs,
            dependencies=dependencies,
            evaluation_criteria=evaluation_criteria,
            governance_policies=governance_policies,
            trigger=trigger,
        )

        agent_export_response.additional_properties = d
        return agent_export_response

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
