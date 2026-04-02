from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluation_result_with_criteria_response_details_type_0 import (
        EvaluationResultWithCriteriaResponseDetailsType0,
    )


T = TypeVar("T", bound="EvaluationResultWithCriteriaResponse")


@_attrs_define
class EvaluationResultWithCriteriaResponse:
    """Evaluation result including criteria context for aggregated listing.

    Attributes:
        agent_run_id (UUID):
        agent_step_run_id (None | UUID):
        created_at (str):
        criteria_description (None | str):
        criteria_id (UUID):
        evaluated_at (str):
        flagged (bool): True when the result was flagged for human review.
        id (UUID):
        retry_count (int):
        retry_triggered (bool):
        status (str): Outcome status: pending, passed, failed, skipped, or error.
        step_id (None | str):
        details (EvaluationResultWithCriteriaResponseDetailsType0 | None | Unset): Evaluation details including
            explanation and raw LLM response.
        score (float | None | Unset): LLM-assigned quality score between 0.0 (worst) and 1.0 (best).
    """

    agent_run_id: UUID
    agent_step_run_id: None | UUID
    created_at: str
    criteria_description: None | str
    criteria_id: UUID
    evaluated_at: str
    flagged: bool
    id: UUID
    retry_count: int
    retry_triggered: bool
    status: str
    step_id: None | str
    details: EvaluationResultWithCriteriaResponseDetailsType0 | None | Unset = UNSET
    score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluation_result_with_criteria_response_details_type_0 import (
            EvaluationResultWithCriteriaResponseDetailsType0,
        )

        agent_run_id = str(self.agent_run_id)

        agent_step_run_id: None | str
        if isinstance(self.agent_step_run_id, UUID):
            agent_step_run_id = str(self.agent_step_run_id)
        else:
            agent_step_run_id = self.agent_step_run_id

        created_at = self.created_at

        criteria_description: None | str
        criteria_description = self.criteria_description

        criteria_id = str(self.criteria_id)

        evaluated_at = self.evaluated_at

        flagged = self.flagged

        id = str(self.id)

        retry_count = self.retry_count

        retry_triggered = self.retry_triggered

        status = self.status

        step_id: None | str
        step_id = self.step_id

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, EvaluationResultWithCriteriaResponseDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_run_id": agent_run_id,
                "agent_step_run_id": agent_step_run_id,
                "created_at": created_at,
                "criteria_description": criteria_description,
                "criteria_id": criteria_id,
                "evaluated_at": evaluated_at,
                "flagged": flagged,
                "id": id,
                "retry_count": retry_count,
                "retry_triggered": retry_triggered,
                "status": status,
                "step_id": step_id,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluation_result_with_criteria_response_details_type_0 import (
            EvaluationResultWithCriteriaResponseDetailsType0,
        )

        d = dict(src_dict)
        agent_run_id = UUID(d.pop("agent_run_id"))

        def _parse_agent_step_run_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_step_run_id_type_0 = UUID(data)

                return agent_step_run_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_step_run_id = _parse_agent_step_run_id(d.pop("agent_step_run_id"))

        created_at = d.pop("created_at")

        def _parse_criteria_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        criteria_description = _parse_criteria_description(
            d.pop("criteria_description")
        )

        criteria_id = UUID(d.pop("criteria_id"))

        evaluated_at = d.pop("evaluated_at")

        flagged = d.pop("flagged")

        id = UUID(d.pop("id"))

        retry_count = d.pop("retry_count")

        retry_triggered = d.pop("retry_triggered")

        status = d.pop("status")

        def _parse_step_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        step_id = _parse_step_id(d.pop("step_id"))

        def _parse_details(
            data: object,
        ) -> EvaluationResultWithCriteriaResponseDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = (
                    EvaluationResultWithCriteriaResponseDetailsType0.from_dict(data)
                )

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EvaluationResultWithCriteriaResponseDetailsType0 | None | Unset, data
            )

        details = _parse_details(d.pop("details", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        evaluation_result_with_criteria_response = cls(
            agent_run_id=agent_run_id,
            agent_step_run_id=agent_step_run_id,
            created_at=created_at,
            criteria_description=criteria_description,
            criteria_id=criteria_id,
            evaluated_at=evaluated_at,
            flagged=flagged,
            id=id,
            retry_count=retry_count,
            retry_triggered=retry_triggered,
            status=status,
            step_id=step_id,
            details=details,
            score=score,
        )

        evaluation_result_with_criteria_response.additional_properties = d
        return evaluation_result_with_criteria_response

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
