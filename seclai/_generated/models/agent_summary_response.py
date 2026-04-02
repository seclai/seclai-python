from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_summary_response_sampling_config_type_0 import (
        AgentSummaryResponseSamplingConfigType0,
    )


T = TypeVar("T", bound="AgentSummaryResponse")


@_attrs_define
class AgentSummaryResponse:
    """
    Attributes:
        created_at (str): ISO 8601 creation timestamp.
        description (None | str): Agent description.
        id (str): Unique agent identifier.
        name (str): Agent name.
        trigger_type (None | str): Trigger type for the agent.
        updated_at (str): ISO 8601 last-updated timestamp.
        default_evaluation_tier (None | str | Unset): Default evaluation tier: fast, balanced, or thorough.
        evaluation_mode (str | Unset): Evaluation mode: output_expectation, eval_and_retry, or sample_and_flag. Default:
            'eval_and_retry'.
        max_retries (int | Unset): Max retries for eval_and_retry mode. Default: 3.
        prompt_model_auto_rollback_enabled (bool | Unset): Whether automatic rollback is enabled for upgraded models.
            Default: False.
        prompt_model_auto_rollback_triggers (list[str] | None | Unset): Failure signals that trigger rollback. Defaults
            to agent_eval_fail, governance_block, agent_run_failed when null.
        prompt_model_auto_upgrade_strategy (str | Unset): Auto-upgrade strategy: none, early_adopter, middle_of_road,
            cautious_adopter. Default: 'none'.
        retry_on_failure (bool | Unset): Whether to retry on evaluation failure. Default: True.
        sampling_config (AgentSummaryResponseSamplingConfigType0 | None | Unset): Sampling configuration for
            sample_and_flag mode.
    """

    created_at: str
    description: None | str
    id: str
    name: str
    trigger_type: None | str
    updated_at: str
    default_evaluation_tier: None | str | Unset = UNSET
    evaluation_mode: str | Unset = "eval_and_retry"
    max_retries: int | Unset = 3
    prompt_model_auto_rollback_enabled: bool | Unset = False
    prompt_model_auto_rollback_triggers: list[str] | None | Unset = UNSET
    prompt_model_auto_upgrade_strategy: str | Unset = "none"
    retry_on_failure: bool | Unset = True
    sampling_config: AgentSummaryResponseSamplingConfigType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_summary_response_sampling_config_type_0 import (
            AgentSummaryResponseSamplingConfigType0,
        )

        created_at = self.created_at

        description: None | str
        description = self.description

        id = self.id

        name = self.name

        trigger_type: None | str
        trigger_type = self.trigger_type

        updated_at = self.updated_at

        default_evaluation_tier: None | str | Unset
        if isinstance(self.default_evaluation_tier, Unset):
            default_evaluation_tier = UNSET
        else:
            default_evaluation_tier = self.default_evaluation_tier

        evaluation_mode = self.evaluation_mode

        max_retries = self.max_retries

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

        prompt_model_auto_upgrade_strategy = self.prompt_model_auto_upgrade_strategy

        retry_on_failure = self.retry_on_failure

        sampling_config: dict[str, Any] | None | Unset
        if isinstance(self.sampling_config, Unset):
            sampling_config = UNSET
        elif isinstance(self.sampling_config, AgentSummaryResponseSamplingConfigType0):
            sampling_config = self.sampling_config.to_dict()
        else:
            sampling_config = self.sampling_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "trigger_type": trigger_type,
                "updated_at": updated_at,
            }
        )
        if default_evaluation_tier is not UNSET:
            field_dict["default_evaluation_tier"] = default_evaluation_tier
        if evaluation_mode is not UNSET:
            field_dict["evaluation_mode"] = evaluation_mode
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_summary_response_sampling_config_type_0 import (
            AgentSummaryResponseSamplingConfigType0,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = d.pop("id")

        name = d.pop("name")

        def _parse_trigger_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type"))

        updated_at = d.pop("updated_at")

        def _parse_default_evaluation_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_evaluation_tier = _parse_default_evaluation_tier(
            d.pop("default_evaluation_tier", UNSET)
        )

        evaluation_mode = d.pop("evaluation_mode", UNSET)

        max_retries = d.pop("max_retries", UNSET)

        prompt_model_auto_rollback_enabled = d.pop(
            "prompt_model_auto_rollback_enabled", UNSET
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

        prompt_model_auto_upgrade_strategy = d.pop(
            "prompt_model_auto_upgrade_strategy", UNSET
        )

        retry_on_failure = d.pop("retry_on_failure", UNSET)

        def _parse_sampling_config(
            data: object,
        ) -> AgentSummaryResponseSamplingConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sampling_config_type_0 = (
                    AgentSummaryResponseSamplingConfigType0.from_dict(data)
                )

                return sampling_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentSummaryResponseSamplingConfigType0 | None | Unset, data)

        sampling_config = _parse_sampling_config(d.pop("sampling_config", UNSET))

        agent_summary_response = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            trigger_type=trigger_type,
            updated_at=updated_at,
            default_evaluation_tier=default_evaluation_tier,
            evaluation_mode=evaluation_mode,
            max_retries=max_retries,
            prompt_model_auto_rollback_enabled=prompt_model_auto_rollback_enabled,
            prompt_model_auto_rollback_triggers=prompt_model_auto_rollback_triggers,
            prompt_model_auto_upgrade_strategy=prompt_model_auto_upgrade_strategy,
            retry_on_failure=retry_on_failure,
            sampling_config=sampling_config,
        )

        agent_summary_response.additional_properties = d
        return agent_summary_response

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
