from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_evaluation_tier import AgentEvaluationTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_draft_evaluation_request_expectation_config_type_0 import (
        TestDraftEvaluationRequestExpectationConfigType0,
    )


T = TypeVar("T", bound="TestDraftEvaluationRequest")


@_attrs_define
class TestDraftEvaluationRequest:
    """Request body for ephemeral (non-persisted) evaluation testing.

    Provide either ``step_output`` (raw text) **or** ``agent_step_run_id``
    (to load output from storage).  Exactly one must be supplied.

        Attributes:
            agent_input (None | str | Unset): The original agent run input for context.  When agent_step_run_id is supplied
                this is loaded automatically from the parent run if omitted.
            agent_step_run_id (None | Unset | UUID): Load step output from this completed step run instead of supplying
                text.
            evaluation_prompt (None | str | Unset):
            evaluation_tier (AgentEvaluationTier | None | Unset):
            expectation_config (None | TestDraftEvaluationRequestExpectationConfigType0 | Unset):
            pass_threshold (float | Unset):  Default: 0.5.
            step_output (None | str | Unset): The step output text to evaluate.  Omit if agent_step_run_id is supplied.
    """

    agent_input: None | str | Unset = UNSET
    agent_step_run_id: None | Unset | UUID = UNSET
    evaluation_prompt: None | str | Unset = UNSET
    evaluation_tier: AgentEvaluationTier | None | Unset = UNSET
    expectation_config: (
        None | TestDraftEvaluationRequestExpectationConfigType0 | Unset
    ) = UNSET
    pass_threshold: float | Unset = 0.5
    step_output: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_draft_evaluation_request_expectation_config_type_0 import (
            TestDraftEvaluationRequestExpectationConfigType0,
        )

        agent_input: None | str | Unset
        if isinstance(self.agent_input, Unset):
            agent_input = UNSET
        else:
            agent_input = self.agent_input

        agent_step_run_id: None | str | Unset
        if isinstance(self.agent_step_run_id, Unset):
            agent_step_run_id = UNSET
        elif isinstance(self.agent_step_run_id, UUID):
            agent_step_run_id = str(self.agent_step_run_id)
        else:
            agent_step_run_id = self.agent_step_run_id

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
            self.expectation_config, TestDraftEvaluationRequestExpectationConfigType0
        ):
            expectation_config = self.expectation_config.to_dict()
        else:
            expectation_config = self.expectation_config

        pass_threshold = self.pass_threshold

        step_output: None | str | Unset
        if isinstance(self.step_output, Unset):
            step_output = UNSET
        else:
            step_output = self.step_output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_input is not UNSET:
            field_dict["agent_input"] = agent_input
        if agent_step_run_id is not UNSET:
            field_dict["agent_step_run_id"] = agent_step_run_id
        if evaluation_prompt is not UNSET:
            field_dict["evaluation_prompt"] = evaluation_prompt
        if evaluation_tier is not UNSET:
            field_dict["evaluation_tier"] = evaluation_tier
        if expectation_config is not UNSET:
            field_dict["expectation_config"] = expectation_config
        if pass_threshold is not UNSET:
            field_dict["pass_threshold"] = pass_threshold
        if step_output is not UNSET:
            field_dict["step_output"] = step_output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_draft_evaluation_request_expectation_config_type_0 import (
            TestDraftEvaluationRequestExpectationConfigType0,
        )

        d = dict(src_dict)

        def _parse_agent_input(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_input = _parse_agent_input(d.pop("agent_input", UNSET))

        def _parse_agent_step_run_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_step_run_id_type_0 = UUID(data)

                return agent_step_run_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_step_run_id = _parse_agent_step_run_id(d.pop("agent_step_run_id", UNSET))

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
        ) -> None | TestDraftEvaluationRequestExpectationConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expectation_config_type_0 = (
                    TestDraftEvaluationRequestExpectationConfigType0.from_dict(data)
                )

                return expectation_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TestDraftEvaluationRequestExpectationConfigType0 | Unset, data
            )

        expectation_config = _parse_expectation_config(
            d.pop("expectation_config", UNSET)
        )

        pass_threshold = d.pop("pass_threshold", UNSET)

        def _parse_step_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_output = _parse_step_output(d.pop("step_output", UNSET))

        test_draft_evaluation_request = cls(
            agent_input=agent_input,
            agent_step_run_id=agent_step_run_id,
            evaluation_prompt=evaluation_prompt,
            evaluation_tier=evaluation_tier,
            expectation_config=expectation_config,
            pass_threshold=pass_threshold,
            step_output=step_output,
        )

        test_draft_evaluation_request.additional_properties = d
        return test_draft_evaluation_request

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
