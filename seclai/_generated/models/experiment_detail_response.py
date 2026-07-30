from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.experiment_detail_response_result_data_type_0 import (
        ExperimentDetailResponseResultDataType0,
    )


T = TypeVar("T", bound="ExperimentDetailResponse")


@_attrs_define
class ExperimentDetailResponse:
    """
    Attributes:
        completed_at (None | str):
        created_at (str):
        error_message (None | str):
        evaluation_complexity (str):
        evaluation_mode (str):
        evaluator_model_id (None | str):
        id (str):
        include_step_output_in_evaluation (bool):
        json_template (None | str):
        progress_current (int | None):
        progress_message (None | str):
        progress_total (int | None):
        prompt (str):
        result_data (ExperimentDetailResponseResultDataType0 | None):
        selected_model_ids (list[str]):
        selected_step_output (None | str):
        started_at (None | str):
        status (str):
        system_prompt (str):
    """

    completed_at: None | str
    created_at: str
    error_message: None | str
    evaluation_complexity: str
    evaluation_mode: str
    evaluator_model_id: None | str
    id: str
    include_step_output_in_evaluation: bool
    json_template: None | str
    progress_current: int | None
    progress_message: None | str
    progress_total: int | None
    prompt: str
    result_data: ExperimentDetailResponseResultDataType0 | None
    selected_model_ids: list[str]
    selected_step_output: None | str
    started_at: None | str
    status: str
    system_prompt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_detail_response_result_data_type_0 import (
            ExperimentDetailResponseResultDataType0,
        )

        completed_at: None | str
        completed_at = self.completed_at

        created_at = self.created_at

        error_message: None | str
        error_message = self.error_message

        evaluation_complexity = self.evaluation_complexity

        evaluation_mode = self.evaluation_mode

        evaluator_model_id: None | str
        evaluator_model_id = self.evaluator_model_id

        id = self.id

        include_step_output_in_evaluation = self.include_step_output_in_evaluation

        json_template: None | str
        json_template = self.json_template

        progress_current: int | None
        progress_current = self.progress_current

        progress_message: None | str
        progress_message = self.progress_message

        progress_total: int | None
        progress_total = self.progress_total

        prompt = self.prompt

        result_data: dict[str, Any] | None
        if isinstance(self.result_data, ExperimentDetailResponseResultDataType0):
            result_data = self.result_data.to_dict()
        else:
            result_data = self.result_data

        selected_model_ids = self.selected_model_ids

        selected_step_output: None | str
        selected_step_output = self.selected_step_output

        started_at: None | str
        started_at = self.started_at

        status = self.status

        system_prompt = self.system_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completed_at": completed_at,
                "created_at": created_at,
                "error_message": error_message,
                "evaluation_complexity": evaluation_complexity,
                "evaluation_mode": evaluation_mode,
                "evaluator_model_id": evaluator_model_id,
                "id": id,
                "include_step_output_in_evaluation": include_step_output_in_evaluation,
                "json_template": json_template,
                "progress_current": progress_current,
                "progress_message": progress_message,
                "progress_total": progress_total,
                "prompt": prompt,
                "result_data": result_data,
                "selected_model_ids": selected_model_ids,
                "selected_step_output": selected_step_output,
                "started_at": started_at,
                "status": status,
                "system_prompt": system_prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_detail_response_result_data_type_0 import (
            ExperimentDetailResponseResultDataType0,
        )

        d = dict(src_dict)

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        created_at = d.pop("created_at")

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        evaluation_complexity = d.pop("evaluation_complexity")

        evaluation_mode = d.pop("evaluation_mode")

        def _parse_evaluator_model_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        evaluator_model_id = _parse_evaluator_model_id(d.pop("evaluator_model_id"))

        id = d.pop("id")

        include_step_output_in_evaluation = d.pop("include_step_output_in_evaluation")

        def _parse_json_template(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        json_template = _parse_json_template(d.pop("json_template"))

        def _parse_progress_current(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        progress_current = _parse_progress_current(d.pop("progress_current"))

        def _parse_progress_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        progress_message = _parse_progress_message(d.pop("progress_message"))

        def _parse_progress_total(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        progress_total = _parse_progress_total(d.pop("progress_total"))

        prompt = d.pop("prompt")

        def _parse_result_data(
            data: object,
        ) -> ExperimentDetailResponseResultDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_data_type_0 = ExperimentDetailResponseResultDataType0.from_dict(
                    data
                )

                return result_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentDetailResponseResultDataType0 | None, data)

        result_data = _parse_result_data(d.pop("result_data"))

        selected_model_ids = cast(list[str], d.pop("selected_model_ids"))

        def _parse_selected_step_output(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        selected_step_output = _parse_selected_step_output(
            d.pop("selected_step_output")
        )

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = d.pop("status")

        system_prompt = d.pop("system_prompt")

        experiment_detail_response = cls(
            completed_at=completed_at,
            created_at=created_at,
            error_message=error_message,
            evaluation_complexity=evaluation_complexity,
            evaluation_mode=evaluation_mode,
            evaluator_model_id=evaluator_model_id,
            id=id,
            include_step_output_in_evaluation=include_step_output_in_evaluation,
            json_template=json_template,
            progress_current=progress_current,
            progress_message=progress_message,
            progress_total=progress_total,
            prompt=prompt,
            result_data=result_data,
            selected_model_ids=selected_model_ids,
            selected_step_output=selected_step_output,
            started_at=started_at,
            status=status,
            system_prompt=system_prompt,
        )

        experiment_detail_response.additional_properties = d
        return experiment_detail_response

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
