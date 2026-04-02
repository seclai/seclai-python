from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.evaluation_criteria_response_expectation_config_type_0 import (
        EvaluationCriteriaResponseExpectationConfigType0,
    )
    from ..models.evaluation_criteria_response_result_summary import (
        EvaluationCriteriaResponseResultSummary,
    )


T = TypeVar("T", bound="EvaluationCriteriaResponse")


@_attrs_define
class EvaluationCriteriaResponse:
    """Response schema for evaluation criteria.

    Attributes:
        account_id (UUID):
        agent_id (UUID):
        created_at (str):
        description (None | str):
        enabled (bool):
        evaluation_mode (str): Runtime behavior mode. output_expectation (manual validation), eval_and_retry (every run
            + retry), sample_and_flag (sampled monitoring).
        evaluation_prompt (None | str):
        evaluation_tier (None | str):
        expectation_config (EvaluationCriteriaResponseExpectationConfigType0 | None):
        id (UUID):
        max_retries (int):
        pass_threshold (float): Score cutoff for pass/fail, inclusive (0.0 to 1.0).
        result_summary (EvaluationCriteriaResponseResultSummary):
        retry_on_failure (bool):
        step_id (None | str):
        updated_at (str):
    """

    account_id: UUID
    agent_id: UUID
    created_at: str
    description: None | str
    enabled: bool
    evaluation_mode: str
    evaluation_prompt: None | str
    evaluation_tier: None | str
    expectation_config: EvaluationCriteriaResponseExpectationConfigType0 | None
    id: UUID
    max_retries: int
    pass_threshold: float
    result_summary: EvaluationCriteriaResponseResultSummary
    retry_on_failure: bool
    step_id: None | str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluation_criteria_response_expectation_config_type_0 import (
            EvaluationCriteriaResponseExpectationConfigType0,
        )

        account_id = str(self.account_id)

        agent_id = str(self.agent_id)

        created_at = self.created_at

        description: None | str
        description = self.description

        enabled = self.enabled

        evaluation_mode = self.evaluation_mode

        evaluation_prompt: None | str
        evaluation_prompt = self.evaluation_prompt

        evaluation_tier: None | str
        evaluation_tier = self.evaluation_tier

        expectation_config: dict[str, Any] | None
        if isinstance(
            self.expectation_config, EvaluationCriteriaResponseExpectationConfigType0
        ):
            expectation_config = self.expectation_config.to_dict()
        else:
            expectation_config = self.expectation_config

        id = str(self.id)

        max_retries = self.max_retries

        pass_threshold = self.pass_threshold

        result_summary = self.result_summary.to_dict()

        retry_on_failure = self.retry_on_failure

        step_id: None | str
        step_id = self.step_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "agent_id": agent_id,
                "created_at": created_at,
                "description": description,
                "enabled": enabled,
                "evaluation_mode": evaluation_mode,
                "evaluation_prompt": evaluation_prompt,
                "evaluation_tier": evaluation_tier,
                "expectation_config": expectation_config,
                "id": id,
                "max_retries": max_retries,
                "pass_threshold": pass_threshold,
                "result_summary": result_summary,
                "retry_on_failure": retry_on_failure,
                "step_id": step_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluation_criteria_response_expectation_config_type_0 import (
            EvaluationCriteriaResponseExpectationConfigType0,
        )
        from ..models.evaluation_criteria_response_result_summary import (
            EvaluationCriteriaResponseResultSummary,
        )

        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        agent_id = UUID(d.pop("agent_id"))

        created_at = d.pop("created_at")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        enabled = d.pop("enabled")

        evaluation_mode = d.pop("evaluation_mode")

        def _parse_evaluation_prompt(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        evaluation_prompt = _parse_evaluation_prompt(d.pop("evaluation_prompt"))

        def _parse_evaluation_tier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        evaluation_tier = _parse_evaluation_tier(d.pop("evaluation_tier"))

        def _parse_expectation_config(
            data: object,
        ) -> EvaluationCriteriaResponseExpectationConfigType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expectation_config_type_0 = (
                    EvaluationCriteriaResponseExpectationConfigType0.from_dict(data)
                )

                return expectation_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvaluationCriteriaResponseExpectationConfigType0 | None, data)

        expectation_config = _parse_expectation_config(d.pop("expectation_config"))

        id = UUID(d.pop("id"))

        max_retries = d.pop("max_retries")

        pass_threshold = d.pop("pass_threshold")

        result_summary = EvaluationCriteriaResponseResultSummary.from_dict(
            d.pop("result_summary")
        )

        retry_on_failure = d.pop("retry_on_failure")

        def _parse_step_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        step_id = _parse_step_id(d.pop("step_id"))

        updated_at = d.pop("updated_at")

        evaluation_criteria_response = cls(
            account_id=account_id,
            agent_id=agent_id,
            created_at=created_at,
            description=description,
            enabled=enabled,
            evaluation_mode=evaluation_mode,
            evaluation_prompt=evaluation_prompt,
            evaluation_tier=evaluation_tier,
            expectation_config=expectation_config,
            id=id,
            max_retries=max_retries,
            pass_threshold=pass_threshold,
            result_summary=result_summary,
            retry_on_failure=retry_on_failure,
            step_id=step_id,
            updated_at=updated_at,
        )

        evaluation_criteria_response.additional_properties = d
        return evaluation_criteria_response

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
