from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvaluationResultSummaryResponse")


@_attrs_define
class EvaluationResultSummaryResponse:
    """Aggregated pass/fail/error counts and average score for a criteria.

    Attributes:
        error (int):
        failed (int):
        flagged (int):
        passed (int):
        total (int):
        average_score (float | None | Unset): Mean score across all evaluated results, or null if none.
    """

    error: int
    failed: int
    flagged: int
    passed: int
    total: int
    average_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        failed = self.failed

        flagged = self.flagged

        passed = self.passed

        total = self.total

        average_score: float | None | Unset
        if isinstance(self.average_score, Unset):
            average_score = UNSET
        else:
            average_score = self.average_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "failed": failed,
                "flagged": flagged,
                "passed": passed,
                "total": total,
            }
        )
        if average_score is not UNSET:
            field_dict["average_score"] = average_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        failed = d.pop("failed")

        flagged = d.pop("flagged")

        passed = d.pop("passed")

        total = d.pop("total")

        def _parse_average_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_score = _parse_average_score(d.pop("average_score", UNSET))

        evaluation_result_summary_response = cls(
            error=error,
            failed=failed,
            flagged=flagged,
            passed=passed,
            total=total,
            average_score=average_score,
        )

        evaluation_result_summary_response.additional_properties = d
        return evaluation_result_summary_response

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
