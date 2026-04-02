from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_evaluation_tier import AgentEvaluationTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_evaluation_criteria_request_expectation_config_type_0 import (
        CreateEvaluationCriteriaRequestExpectationConfigType0,
    )


T = TypeVar("T", bound="CreateEvaluationCriteriaRequest")


@_attrs_define
class CreateEvaluationCriteriaRequest:
    """Request body for creating an evaluation criteria.

    The evaluation mode, retry settings, and sample frequency are set at the
    agent level, not per-criteria.

        Attributes:
            step_id (str):
            description (None | str | Unset):
            enabled (bool | Unset):  Default: True.
            evaluation_prompt (None | str | Unset):
            evaluation_tier (AgentEvaluationTier | None | Unset):
            expectation_config (CreateEvaluationCriteriaRequestExpectationConfigType0 | None | Unset):
            pass_threshold (float | Unset):  Default: 0.5.
    """

    step_id: str
    description: None | str | Unset = UNSET
    enabled: bool | Unset = True
    evaluation_prompt: None | str | Unset = UNSET
    evaluation_tier: AgentEvaluationTier | None | Unset = UNSET
    expectation_config: (
        CreateEvaluationCriteriaRequestExpectationConfigType0 | None | Unset
    ) = UNSET
    pass_threshold: float | Unset = 0.5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_evaluation_criteria_request_expectation_config_type_0 import (
            CreateEvaluationCriteriaRequestExpectationConfigType0,
        )

        step_id = self.step_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        evaluation_prompt: None | str | Unset
        if isinstance(self.evaluation_prompt, Unset):
            evaluation_prompt = UNSET
        else:
            evaluation_prompt = self.evaluation_prompt

        evaluation_tier: None | str | Unset
        if isinstance(self.evaluation_tier, Unset):
            evaluation_tier = UNSET
        elif isinstance(self.evaluation_tier, AgentEvaluationTier):
            evaluation_tier = self.evaluation_tier.value
        else:
            evaluation_tier = self.evaluation_tier

        expectation_config: dict[str, Any] | None | Unset
        if isinstance(self.expectation_config, Unset):
            expectation_config = UNSET
        elif isinstance(
            self.expectation_config,
            CreateEvaluationCriteriaRequestExpectationConfigType0,
        ):
            expectation_config = self.expectation_config.to_dict()
        else:
            expectation_config = self.expectation_config

        pass_threshold = self.pass_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_id": step_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if evaluation_prompt is not UNSET:
            field_dict["evaluation_prompt"] = evaluation_prompt
        if evaluation_tier is not UNSET:
            field_dict["evaluation_tier"] = evaluation_tier
        if expectation_config is not UNSET:
            field_dict["expectation_config"] = expectation_config
        if pass_threshold is not UNSET:
            field_dict["pass_threshold"] = pass_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_evaluation_criteria_request_expectation_config_type_0 import (
            CreateEvaluationCriteriaRequestExpectationConfigType0,
        )

        d = dict(src_dict)
        step_id = d.pop("step_id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_evaluation_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evaluation_prompt = _parse_evaluation_prompt(d.pop("evaluation_prompt", UNSET))

        def _parse_evaluation_tier(data: object) -> AgentEvaluationTier | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                evaluation_tier_type_0 = AgentEvaluationTier(data)

                return evaluation_tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentEvaluationTier | None | Unset, data)

        evaluation_tier = _parse_evaluation_tier(d.pop("evaluation_tier", UNSET))

        def _parse_expectation_config(
            data: object,
        ) -> CreateEvaluationCriteriaRequestExpectationConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expectation_config_type_0 = (
                    CreateEvaluationCriteriaRequestExpectationConfigType0.from_dict(
                        data
                    )
                )

                return expectation_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateEvaluationCriteriaRequestExpectationConfigType0 | None | Unset,
                data,
            )

        expectation_config = _parse_expectation_config(
            d.pop("expectation_config", UNSET)
        )

        pass_threshold = d.pop("pass_threshold", UNSET)

        create_evaluation_criteria_request = cls(
            step_id=step_id,
            description=description,
            enabled=enabled,
            evaluation_prompt=evaluation_prompt,
            evaluation_tier=evaluation_tier,
            expectation_config=expectation_config,
            pass_threshold=pass_threshold,
        )

        create_evaluation_criteria_request.additional_properties = d
        return create_evaluation_criteria_request

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
