from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evaluation_status import EvaluationStatus

T = TypeVar("T", bound="TestDraftEvaluationResponse")


@_attrs_define
class TestDraftEvaluationResponse:
    """Response for an ephemeral evaluation test.

    Attributes:
        explanation (None | str):
        passed (bool):
        score (float):
        status (EvaluationStatus): Result status of a single evaluation run.
    """

    explanation: None | str
    passed: bool
    score: float
    status: EvaluationStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        explanation: None | str
        explanation = self.explanation

        passed = self.passed

        score = self.score

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "explanation": explanation,
                "passed": passed,
                "score": score,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_explanation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        explanation = _parse_explanation(d.pop("explanation"))

        passed = d.pop("passed")

        score = d.pop("score")

        status = EvaluationStatus(d.pop("status"))

        test_draft_evaluation_response = cls(
            explanation=explanation,
            passed=passed,
            score=score,
            status=status,
        )

        test_draft_evaluation_response.additional_properties = d
        return test_draft_evaluation_response

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
