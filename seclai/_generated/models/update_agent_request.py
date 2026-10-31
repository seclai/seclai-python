from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_model_auto_upgrade_strategy import PromptModelAutoUpgradeStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_agent_request_agent_definition_type_0 import (
        UpdateAgentRequestAgentDefinitionType0,
    )
    from ..models.update_agent_request_entity_remap_type_0 import (
        UpdateAgentRequestEntityRemapType0,
    )
    from ..models.update_agent_request_sampling_config_type_0 import (
        UpdateAgentRequestSamplingConfigType0,
    )


T = TypeVar("T", bound="UpdateAgentRequest")


@_attrs_define
class UpdateAgentRequest:
    """
    Attributes:
        agent_definition (None | Unset | UpdateAgentRequestAgentDefinitionType0): Optional payload in the same format
            produced by GET /agents/{id}/export. When provided, agent metadata fields the request does not set explicitly
            are taken from the payload, and the agent's workflow is replaced from `agent.definition`. The previous version
            is preserved in history. Validation errors include line/column references against a canonical pretty-printed
            echo of the supplied payload.
        apply_import_run_limits (bool | Unset): With `agent_definition`, also replace the agent's run limits with the
            payload's (a null there removes a limit). Off by default: the agent keeps its limits. Default: False.
        default_evaluation_tier (None | str | Unset): Default evaluation tier: 'fast', 'balanced', or 'thorough'.
        description (None | str | Unset): New description for the agent.
        entity_remap (None | Unset | UpdateAgentRequestEntityRemapType0): Optional UUID-substitution map applied to the
            imported workflow before save (same shape as on POST /agents).
        evaluation_mode (None | str | Unset): Evaluation mode: 'output_expectation', 'eval_and_retry', or
            'sample_and_flag'.
        max_credits_per_period (float | None | Unset): Credit limit per billing period of the paying account: once
            reached, runs stop at their next step and new runs are refused.
        max_credits_per_run (float | None | Unset): Credit limit per run: a run that reaches it is stopped before its
            next step.
        max_retries (int | None | Unset): Max retries for eval_and_retry mode (1-10).
        max_runs_per_day (int | None | Unset): Runs per day; at most the plan's run quota.
        max_runs_per_hour (int | None | Unset): Runs per hour; at most the plan's run quota.
        max_runs_total (int | None | Unset): Runs in total; once reached, new runs are refused.
        name (None | str | Unset): New name for the agent.
        prompt_model_auto_rollback_enabled (bool | None | Unset): Enable or disable automatic rollback for upgraded
            models.
        prompt_model_auto_rollback_triggers (list[str] | None | Unset): Failure signals that trigger rollback:
            agent_eval_fail, governance_flag, governance_block, agent_run_failed.
        prompt_model_auto_upgrade_strategy (None | PromptModelAutoUpgradeStrategy | Unset): Auto-upgrade strategy: none,
            early_adopter, middle_of_road, cautious_adopter.
        retry_on_failure (bool | None | Unset): Whether to retry on evaluation failure.
        sampling_config (None | Unset | UpdateAgentRequestSamplingConfigType0): Sampling configuration for
            sample_and_flag mode. Format: {combinator: 'and'|'or', rules: [...]}.
        set_default_evaluation_tier (bool | Unset): When true and default_evaluation_tier is omitted, clears the tier to
            null (system default). Default: False.
        set_max_credits_per_period (bool | Unset): When true and max_credits_per_period is omitted, removes the limit.
            Default: False.
        set_max_credits_per_run (bool | Unset): When true and max_credits_per_run is omitted, removes the limit.
            Default: False.
        set_max_runs_per_day (bool | Unset): When true and max_runs_per_day is omitted, removes the limit. Default:
            False.
        set_max_runs_per_hour (bool | Unset): When true and max_runs_per_hour is omitted, removes the limit. Default:
            False.
        set_max_runs_total (bool | Unset): When true and max_runs_total is omitted, removes the limit. Default: False.
        set_prompt_model_auto_rollback_triggers (bool | Unset): When true and prompt_model_auto_rollback_triggers is
            omitted, clears the list to null (revert to system defaults). Default: False.
        set_sampling_config (bool | Unset): When true and sampling_config is omitted, clears the config to null.
            Default: False.
    """

    agent_definition: None | Unset | UpdateAgentRequestAgentDefinitionType0 = UNSET
    apply_import_run_limits: bool | Unset = False
    default_evaluation_tier: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    entity_remap: None | Unset | UpdateAgentRequestEntityRemapType0 = UNSET
    evaluation_mode: None | str | Unset = UNSET
    max_credits_per_period: float | None | Unset = UNSET
    max_credits_per_run: float | None | Unset = UNSET
    max_retries: int | None | Unset = UNSET
    max_runs_per_day: int | None | Unset = UNSET
    max_runs_per_hour: int | None | Unset = UNSET
    max_runs_total: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    prompt_model_auto_rollback_enabled: bool | None | Unset = UNSET
    prompt_model_auto_rollback_triggers: list[str] | None | Unset = UNSET
    prompt_model_auto_upgrade_strategy: (
        None | PromptModelAutoUpgradeStrategy | Unset
    ) = UNSET
    retry_on_failure: bool | None | Unset = UNSET
    sampling_config: None | Unset | UpdateAgentRequestSamplingConfigType0 = UNSET
    set_default_evaluation_tier: bool | Unset = False
    set_max_credits_per_period: bool | Unset = False
    set_max_credits_per_run: bool | Unset = False
    set_max_runs_per_day: bool | Unset = False
    set_max_runs_per_hour: bool | Unset = False
    set_max_runs_total: bool | Unset = False
    set_prompt_model_auto_rollback_triggers: bool | Unset = False
    set_sampling_config: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_agent_request_agent_definition_type_0 import (
            UpdateAgentRequestAgentDefinitionType0,
        )
        from ..models.update_agent_request_entity_remap_type_0 import (
            UpdateAgentRequestEntityRemapType0,
        )
        from ..models.update_agent_request_sampling_config_type_0 import (
            UpdateAgentRequestSamplingConfigType0,
        )

        agent_definition: dict[str, Any] | None | Unset
        if isinstance(self.agent_definition, Unset):
            agent_definition = UNSET
        elif isinstance(self.agent_definition, UpdateAgentRequestAgentDefinitionType0):
            agent_definition = self.agent_definition.to_dict()
        else:
            agent_definition = self.agent_definition

        apply_import_run_limits = self.apply_import_run_limits

        default_evaluation_tier: None | str | Unset
        if isinstance(self.default_evaluation_tier, Unset):
            default_evaluation_tier = UNSET
        else:
            default_evaluation_tier = self.default_evaluation_tier

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        entity_remap: dict[str, Any] | None | Unset
        if isinstance(self.entity_remap, Unset):
            entity_remap = UNSET
        elif isinstance(self.entity_remap, UpdateAgentRequestEntityRemapType0):
            entity_remap = self.entity_remap.to_dict()
        else:
            entity_remap = self.entity_remap

        evaluation_mode: None | str | Unset
        if isinstance(self.evaluation_mode, Unset):
            evaluation_mode = UNSET
        else:
            evaluation_mode = self.evaluation_mode

        max_credits_per_period: float | None | Unset
        if isinstance(self.max_credits_per_period, Unset):
            max_credits_per_period = UNSET
        else:
            max_credits_per_period = self.max_credits_per_period

        max_credits_per_run: float | None | Unset
        if isinstance(self.max_credits_per_run, Unset):
            max_credits_per_run = UNSET
        else:
            max_credits_per_run = self.max_credits_per_run

        max_retries: int | None | Unset
        if isinstance(self.max_retries, Unset):
            max_retries = UNSET
        else:
            max_retries = self.max_retries

        max_runs_per_day: int | None | Unset
        if isinstance(self.max_runs_per_day, Unset):
            max_runs_per_day = UNSET
        else:
            max_runs_per_day = self.max_runs_per_day

        max_runs_per_hour: int | None | Unset
        if isinstance(self.max_runs_per_hour, Unset):
            max_runs_per_hour = UNSET
        else:
            max_runs_per_hour = self.max_runs_per_hour

        max_runs_total: int | None | Unset
        if isinstance(self.max_runs_total, Unset):
            max_runs_total = UNSET
        else:
            max_runs_total = self.max_runs_total

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        prompt_model_auto_rollback_enabled: bool | None | Unset
        if isinstance(self.prompt_model_auto_rollback_enabled, Unset):
            prompt_model_auto_rollback_enabled = UNSET
        else:
            prompt_model_auto_rollback_enabled = self.prompt_model_auto_rollback_enabled

        prompt_model_auto_rollback_triggers: list[str] | None | Unset
        if isinstance(self.prompt_model_auto_rollback_triggers, Unset):
            prompt_model_auto_rollback_triggers = UNSET
        elif isinstance(self.prompt_model_auto_rollback_triggers, list):
            prompt_model_auto_rollback_triggers = (
                self.prompt_model_auto_rollback_triggers
            )

        else:
            prompt_model_auto_rollback_triggers = (
                self.prompt_model_auto_rollback_triggers
            )

        prompt_model_auto_upgrade_strategy: None | str | Unset
        if isinstance(self.prompt_model_auto_upgrade_strategy, Unset):
            prompt_model_auto_upgrade_strategy = UNSET
        elif isinstance(
            self.prompt_model_auto_upgrade_strategy, PromptModelAutoUpgradeStrategy
        ):
            prompt_model_auto_upgrade_strategy = (
                self.prompt_model_auto_upgrade_strategy.value
            )
        else:
            prompt_model_auto_upgrade_strategy = self.prompt_model_auto_upgrade_strategy

        retry_on_failure: bool | None | Unset
        if isinstance(self.retry_on_failure, Unset):
            retry_on_failure = UNSET
        else:
            retry_on_failure = self.retry_on_failure

        sampling_config: dict[str, Any] | None | Unset
        if isinstance(self.sampling_config, Unset):
            sampling_config = UNSET
        elif isinstance(self.sampling_config, UpdateAgentRequestSamplingConfigType0):
            sampling_config = self.sampling_config.to_dict()
        else:
            sampling_config = self.sampling_config

        set_default_evaluation_tier = self.set_default_evaluation_tier

        set_max_credits_per_period = self.set_max_credits_per_period

        set_max_credits_per_run = self.set_max_credits_per_run

        set_max_runs_per_day = self.set_max_runs_per_day

        set_max_runs_per_hour = self.set_max_runs_per_hour

        set_max_runs_total = self.set_max_runs_total

        set_prompt_model_auto_rollback_triggers = (
            self.set_prompt_model_auto_rollback_triggers
        )

        set_sampling_config = self.set_sampling_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_definition is not UNSET:
            field_dict["agent_definition"] = agent_definition
        if apply_import_run_limits is not UNSET:
            field_dict["apply_import_run_limits"] = apply_import_run_limits
        if default_evaluation_tier is not UNSET:
            field_dict["default_evaluation_tier"] = default_evaluation_tier
        if description is not UNSET:
            field_dict["description"] = description
        if entity_remap is not UNSET:
            field_dict["entity_remap"] = entity_remap
        if evaluation_mode is not UNSET:
            field_dict["evaluation_mode"] = evaluation_mode
        if max_credits_per_period is not UNSET:
            field_dict["max_credits_per_period"] = max_credits_per_period
        if max_credits_per_run is not UNSET:
            field_dict["max_credits_per_run"] = max_credits_per_run
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if max_runs_per_day is not UNSET:
            field_dict["max_runs_per_day"] = max_runs_per_day
        if max_runs_per_hour is not UNSET:
            field_dict["max_runs_per_hour"] = max_runs_per_hour
        if max_runs_total is not UNSET:
            field_dict["max_runs_total"] = max_runs_total
        if name is not UNSET:
            field_dict["name"] = name
        if prompt_model_auto_rollback_enabled is not UNSET:
            field_dict["prompt_model_auto_rollback_enabled"] = (
                prompt_model_auto_rollback_enabled
            )
        if prompt_model_auto_rollback_triggers is not UNSET:
            field_dict["prompt_model_auto_rollback_triggers"] = (
                prompt_model_auto_rollback_triggers
            )
        if prompt_model_auto_upgrade_strategy is not UNSET:
            field_dict["prompt_model_auto_upgrade_strategy"] = (
                prompt_model_auto_upgrade_strategy
            )
        if retry_on_failure is not UNSET:
            field_dict["retry_on_failure"] = retry_on_failure
        if sampling_config is not UNSET:
            field_dict["sampling_config"] = sampling_config
        if set_default_evaluation_tier is not UNSET:
            field_dict["set_default_evaluation_tier"] = set_default_evaluation_tier
        if set_max_credits_per_period is not UNSET:
            field_dict["set_max_credits_per_period"] = set_max_credits_per_period
        if set_max_credits_per_run is not UNSET:
            field_dict["set_max_credits_per_run"] = set_max_credits_per_run
        if set_max_runs_per_day is not UNSET:
            field_dict["set_max_runs_per_day"] = set_max_runs_per_day
        if set_max_runs_per_hour is not UNSET:
            field_dict["set_max_runs_per_hour"] = set_max_runs_per_hour
        if set_max_runs_total is not UNSET:
            field_dict["set_max_runs_total"] = set_max_runs_total
        if set_prompt_model_auto_rollback_triggers is not UNSET:
            field_dict["set_prompt_model_auto_rollback_triggers"] = (
                set_prompt_model_auto_rollback_triggers
            )
        if set_sampling_config is not UNSET:
            field_dict["set_sampling_config"] = set_sampling_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_agent_request_agent_definition_type_0 import (
            UpdateAgentRequestAgentDefinitionType0,
        )
        from ..models.update_agent_request_entity_remap_type_0 import (
            UpdateAgentRequestEntityRemapType0,
        )
        from ..models.update_agent_request_sampling_config_type_0 import (
            UpdateAgentRequestSamplingConfigType0,
        )

        d = dict(src_dict)

        def _parse_agent_definition(
            data: object,
        ) -> None | Unset | UpdateAgentRequestAgentDefinitionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_definition_type_0 = (
                    UpdateAgentRequestAgentDefinitionType0.from_dict(data)
                )

                return agent_definition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentRequestAgentDefinitionType0, data)

        agent_definition = _parse_agent_definition(d.pop("agent_definition", UNSET))

        apply_import_run_limits = d.pop("apply_import_run_limits", UNSET)

        def _parse_default_evaluation_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_evaluation_tier = _parse_default_evaluation_tier(
            d.pop("default_evaluation_tier", UNSET)
        )

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_entity_remap(
            data: object,
        ) -> None | Unset | UpdateAgentRequestEntityRemapType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_remap_type_0 = UpdateAgentRequestEntityRemapType0.from_dict(data)

                return entity_remap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentRequestEntityRemapType0, data)

        entity_remap = _parse_entity_remap(d.pop("entity_remap", UNSET))

        def _parse_evaluation_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evaluation_mode = _parse_evaluation_mode(d.pop("evaluation_mode", UNSET))

        def _parse_max_credits_per_period(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_credits_per_period = _parse_max_credits_per_period(
            d.pop("max_credits_per_period", UNSET)
        )

        def _parse_max_credits_per_run(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_credits_per_run = _parse_max_credits_per_run(
            d.pop("max_credits_per_run", UNSET)
        )

        def _parse_max_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_retries = _parse_max_retries(d.pop("max_retries", UNSET))

        def _parse_max_runs_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_runs_per_day = _parse_max_runs_per_day(d.pop("max_runs_per_day", UNSET))

        def _parse_max_runs_per_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_runs_per_hour = _parse_max_runs_per_hour(d.pop("max_runs_per_hour", UNSET))

        def _parse_max_runs_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_runs_total = _parse_max_runs_total(d.pop("max_runs_total", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_prompt_model_auto_rollback_enabled(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prompt_model_auto_rollback_enabled = _parse_prompt_model_auto_rollback_enabled(
            d.pop("prompt_model_auto_rollback_enabled", UNSET)
        )

        def _parse_prompt_model_auto_rollback_triggers(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prompt_model_auto_rollback_triggers_type_0 = cast(list[str], data)

                return prompt_model_auto_rollback_triggers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        prompt_model_auto_rollback_triggers = (
            _parse_prompt_model_auto_rollback_triggers(
                d.pop("prompt_model_auto_rollback_triggers", UNSET)
            )
        )

        def _parse_prompt_model_auto_upgrade_strategy(
            data: object,
        ) -> None | PromptModelAutoUpgradeStrategy | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prompt_model_auto_upgrade_strategy_type_0 = (
                    PromptModelAutoUpgradeStrategy(data)
                )

                return prompt_model_auto_upgrade_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptModelAutoUpgradeStrategy | Unset, data)

        prompt_model_auto_upgrade_strategy = _parse_prompt_model_auto_upgrade_strategy(
            d.pop("prompt_model_auto_upgrade_strategy", UNSET)
        )

        def _parse_retry_on_failure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        retry_on_failure = _parse_retry_on_failure(d.pop("retry_on_failure", UNSET))

        def _parse_sampling_config(
            data: object,
        ) -> None | Unset | UpdateAgentRequestSamplingConfigType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sampling_config_type_0 = (
                    UpdateAgentRequestSamplingConfigType0.from_dict(data)
                )

                return sampling_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentRequestSamplingConfigType0, data)

        sampling_config = _parse_sampling_config(d.pop("sampling_config", UNSET))

        set_default_evaluation_tier = d.pop("set_default_evaluation_tier", UNSET)

        set_max_credits_per_period = d.pop("set_max_credits_per_period", UNSET)

        set_max_credits_per_run = d.pop("set_max_credits_per_run", UNSET)

        set_max_runs_per_day = d.pop("set_max_runs_per_day", UNSET)

        set_max_runs_per_hour = d.pop("set_max_runs_per_hour", UNSET)

        set_max_runs_total = d.pop("set_max_runs_total", UNSET)

        set_prompt_model_auto_rollback_triggers = d.pop(
            "set_prompt_model_auto_rollback_triggers", UNSET
        )

        set_sampling_config = d.pop("set_sampling_config", UNSET)

        update_agent_request = cls(
            agent_definition=agent_definition,
            apply_import_run_limits=apply_import_run_limits,
            default_evaluation_tier=default_evaluation_tier,
            description=description,
            entity_remap=entity_remap,
            evaluation_mode=evaluation_mode,
            max_credits_per_period=max_credits_per_period,
            max_credits_per_run=max_credits_per_run,
            max_retries=max_retries,
            max_runs_per_day=max_runs_per_day,
            max_runs_per_hour=max_runs_per_hour,
            max_runs_total=max_runs_total,
            name=name,
            prompt_model_auto_rollback_enabled=prompt_model_auto_rollback_enabled,
            prompt_model_auto_rollback_triggers=prompt_model_auto_rollback_triggers,
            prompt_model_auto_upgrade_strategy=prompt_model_auto_upgrade_strategy,
            retry_on_failure=retry_on_failure,
            sampling_config=sampling_config,
            set_default_evaluation_tier=set_default_evaluation_tier,
            set_max_credits_per_period=set_max_credits_per_period,
            set_max_credits_per_run=set_max_credits_per_run,
            set_max_runs_per_day=set_max_runs_per_day,
            set_max_runs_per_hour=set_max_runs_per_hour,
            set_max_runs_total=set_max_runs_total,
            set_prompt_model_auto_rollback_triggers=set_prompt_model_auto_rollback_triggers,
            set_sampling_config=set_sampling_config,
        )

        update_agent_request.additional_properties = d
        return update_agent_request

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
