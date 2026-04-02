from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_model_auto_upgrade_strategy import PromptModelAutoUpgradeStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_agent_request_sampling_config_type_0 import (
        UpdateAgentRequestSamplingConfigType0,
    )


T = TypeVar("T", bound="UpdateAgentRequest")


@_attrs_define
class UpdateAgentRequest:
    """
    Attributes:
        default_evaluation_tier (None | str | Unset): Default evaluation tier: 'fast', 'balanced', or 'thorough'.
        description (None | str | Unset): New description for the agent.
        evaluation_mode (None | str | Unset): Evaluation mode: 'output_expectation', 'eval_and_retry', or
            'sample_and_flag'.
        max_retries (int | None | Unset): Max retries for eval_and_retry mode (1-10).
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
        set_prompt_model_auto_rollback_triggers (bool | Unset): When true and prompt_model_auto_rollback_triggers is
            omitted, clears the list to null (revert to system defaults). Default: False.
        set_sampling_config (bool | Unset): When true and sampling_config is omitted, clears the config to null.
            Default: False.
    """

    default_evaluation_tier: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    evaluation_mode: None | str | Unset = UNSET
    max_retries: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    prompt_model_auto_rollback_enabled: bool | None | Unset = UNSET
    prompt_model_auto_rollback_triggers: list[str] | None | Unset = UNSET
    prompt_model_auto_upgrade_strategy: (
        None | PromptModelAutoUpgradeStrategy | Unset
    ) = UNSET
    retry_on_failure: bool | None | Unset = UNSET
    sampling_config: None | Unset | UpdateAgentRequestSamplingConfigType0 = UNSET
    set_default_evaluation_tier: bool | Unset = False
    set_prompt_model_auto_rollback_triggers: bool | Unset = False
    set_sampling_config: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_agent_request_sampling_config_type_0 import (
            UpdateAgentRequestSamplingConfigType0,
        )

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

        evaluation_mode: None | str | Unset
        if isinstance(self.evaluation_mode, Unset):
            evaluation_mode = UNSET
        else:
            evaluation_mode = self.evaluation_mode

        max_retries: int | None | Unset
        if isinstance(self.max_retries, Unset):
            max_retries = UNSET
        else:
            max_retries = self.max_retries

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

        set_prompt_model_auto_rollback_triggers = (
            self.set_prompt_model_auto_rollback_triggers
        )

        set_sampling_config = self.set_sampling_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_evaluation_tier is not UNSET:
            field_dict["default_evaluation_tier"] = default_evaluation_tier
        if description is not UNSET:
            field_dict["description"] = description
        if evaluation_mode is not UNSET:
            field_dict["evaluation_mode"] = evaluation_mode
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
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
        if set_prompt_model_auto_rollback_triggers is not UNSET:
            field_dict["set_prompt_model_auto_rollback_triggers"] = (
                set_prompt_model_auto_rollback_triggers
            )
        if set_sampling_config is not UNSET:
            field_dict["set_sampling_config"] = set_sampling_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_agent_request_sampling_config_type_0 import (
            UpdateAgentRequestSamplingConfigType0,
        )

        d = dict(src_dict)

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

        def _parse_evaluation_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evaluation_mode = _parse_evaluation_mode(d.pop("evaluation_mode", UNSET))

        def _parse_max_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_retries = _parse_max_retries(d.pop("max_retries", UNSET))

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

        set_prompt_model_auto_rollback_triggers = d.pop(
            "set_prompt_model_auto_rollback_triggers", UNSET
        )

        set_sampling_config = d.pop("set_sampling_config", UNSET)

        update_agent_request = cls(
            default_evaluation_tier=default_evaluation_tier,
            description=description,
            evaluation_mode=evaluation_mode,
            max_retries=max_retries,
            name=name,
            prompt_model_auto_rollback_enabled=prompt_model_auto_rollback_enabled,
            prompt_model_auto_rollback_triggers=prompt_model_auto_rollback_triggers,
            prompt_model_auto_upgrade_strategy=prompt_model_auto_upgrade_strategy,
            retry_on_failure=retry_on_failure,
            sampling_config=sampling_config,
            set_default_evaluation_tier=set_default_evaluation_tier,
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
