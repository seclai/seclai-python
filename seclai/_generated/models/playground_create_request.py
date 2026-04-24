from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.playground_create_request_evaluation_complexity import (
    PlaygroundCreateRequestEvaluationComplexity,
)
from ..models.playground_create_request_evaluation_mode import (
    PlaygroundCreateRequestEvaluationMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaygroundCreateRequest")


@_attrs_define
class PlaygroundCreateRequest:
    """Create a model playground experiment via the public API.

    Attributes:
        model_ids (list[str]): Selected model IDs (1-10).
        prompt (str): Prompt text for the experiment.
        evaluation_complexity (PlaygroundCreateRequestEvaluationComplexity | Unset): simple, medium, or complex Default:
            PlaygroundCreateRequestEvaluationComplexity.MEDIUM.
        evaluation_mode (PlaygroundCreateRequestEvaluationMode | Unset): manual or prompt Default:
            PlaygroundCreateRequestEvaluationMode.MANUAL.
        evaluator_model_id (None | str | Unset): Evaluator model ID when evaluation_mode is prompt.
        include_step_output_in_evaluation (bool | Unset): Whether to include selected step output as evaluator context.
            Default: False.
        json_template (None | str | Unset): Optional JSON template for advanced mode.
        selected_step_output (None | str | Unset): Optional step output text for evaluator context.
        system_prompt (str | Unset): Optional system prompt. Default: ''.
    """

    model_ids: list[str]
    prompt: str
    evaluation_complexity: PlaygroundCreateRequestEvaluationComplexity | Unset = (
        PlaygroundCreateRequestEvaluationComplexity.MEDIUM
    )
    evaluation_mode: PlaygroundCreateRequestEvaluationMode | Unset = (
        PlaygroundCreateRequestEvaluationMode.MANUAL
    )
    evaluator_model_id: None | str | Unset = UNSET
    include_step_output_in_evaluation: bool | Unset = False
    json_template: None | str | Unset = UNSET
    selected_step_output: None | str | Unset = UNSET
    system_prompt: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_ids = self.model_ids

        prompt = self.prompt

        evaluation_complexity: str | Unset = UNSET
        if not isinstance(self.evaluation_complexity, Unset):
            evaluation_complexity = self.evaluation_complexity.value

        evaluation_mode: str | Unset = UNSET
        if not isinstance(self.evaluation_mode, Unset):
            evaluation_mode = self.evaluation_mode.value

        evaluator_model_id: None | str | Unset
        if isinstance(self.evaluator_model_id, Unset):
            evaluator_model_id = UNSET
        else:
            evaluator_model_id = self.evaluator_model_id

        include_step_output_in_evaluation = self.include_step_output_in_evaluation

        json_template: None | str | Unset
        if isinstance(self.json_template, Unset):
            json_template = UNSET
        else:
            json_template = self.json_template

        selected_step_output: None | str | Unset
        if isinstance(self.selected_step_output, Unset):
            selected_step_output = UNSET
        else:
            selected_step_output = self.selected_step_output

        system_prompt = self.system_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_ids": model_ids,
                "prompt": prompt,
            }
        )
        if evaluation_complexity is not UNSET:
            field_dict["evaluation_complexity"] = evaluation_complexity
        if evaluation_mode is not UNSET:
            field_dict["evaluation_mode"] = evaluation_mode
        if evaluator_model_id is not UNSET:
            field_dict["evaluator_model_id"] = evaluator_model_id
        if include_step_output_in_evaluation is not UNSET:
            field_dict["include_step_output_in_evaluation"] = (
                include_step_output_in_evaluation
            )
        if json_template is not UNSET:
            field_dict["json_template"] = json_template
        if selected_step_output is not UNSET:
            field_dict["selected_step_output"] = selected_step_output
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_ids = cast(list[str], d.pop("model_ids"))

        prompt = d.pop("prompt")

        _evaluation_complexity = d.pop("evaluation_complexity", UNSET)
        evaluation_complexity: PlaygroundCreateRequestEvaluationComplexity | Unset
        if isinstance(_evaluation_complexity, Unset):
            evaluation_complexity = UNSET
        else:
            evaluation_complexity = PlaygroundCreateRequestEvaluationComplexity(
                _evaluation_complexity
            )

        _evaluation_mode = d.pop("evaluation_mode", UNSET)
        evaluation_mode: PlaygroundCreateRequestEvaluationMode | Unset
        if isinstance(_evaluation_mode, Unset):
            evaluation_mode = UNSET
        else:
            evaluation_mode = PlaygroundCreateRequestEvaluationMode(_evaluation_mode)

        def _parse_evaluator_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evaluator_model_id = _parse_evaluator_model_id(
            d.pop("evaluator_model_id", UNSET)
        )

        include_step_output_in_evaluation = d.pop(
            "include_step_output_in_evaluation", UNSET
        )

        def _parse_json_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        json_template = _parse_json_template(d.pop("json_template", UNSET))

        def _parse_selected_step_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        selected_step_output = _parse_selected_step_output(
            d.pop("selected_step_output", UNSET)
        )

        system_prompt = d.pop("system_prompt", UNSET)

        playground_create_request = cls(
            model_ids=model_ids,
            prompt=prompt,
            evaluation_complexity=evaluation_complexity,
            evaluation_mode=evaluation_mode,
            evaluator_model_id=evaluator_model_id,
            include_step_output_in_evaluation=include_step_output_in_evaluation,
            json_template=json_template,
            selected_step_output=selected_step_output,
            system_prompt=system_prompt,
        )

        playground_create_request.additional_properties = d
        return playground_create_request

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
