from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.non_manual_evaluation_mode_stat_response import (
        NonManualEvaluationModeStatResponse,
    )


T = TypeVar("T", bound="NonManualEvaluationSummaryResponse")


@_attrs_define
class NonManualEvaluationSummaryResponse:
    """Account-level summary for evaluations.

    Attributes:
        by_mode (list[NonManualEvaluationModeStatResponse]):
        failed (int):
        failure_rate (float):
        flagged (int):
        pass_rate (float):
        passed (int):
        total (int):
    """

    by_mode: list[NonManualEvaluationModeStatResponse]
    failed: int
    failure_rate: float
    flagged: int
    pass_rate: float
    passed: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_mode = []
        for by_mode_item_data in self.by_mode:
            by_mode_item = by_mode_item_data.to_dict()
            by_mode.append(by_mode_item)

        failed = self.failed

        failure_rate = self.failure_rate

        flagged = self.flagged

        pass_rate = self.pass_rate

        passed = self.passed

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "by_mode": by_mode,
                "failed": failed,
                "failure_rate": failure_rate,
                "flagged": flagged,
                "pass_rate": pass_rate,
                "passed": passed,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.non_manual_evaluation_mode_stat_response import (
            NonManualEvaluationModeStatResponse,
        )

        d = dict(src_dict)
        by_mode = []
        _by_mode = d.pop("by_mode")
        for by_mode_item_data in _by_mode:
            by_mode_item = NonManualEvaluationModeStatResponse.from_dict(
                by_mode_item_data
            )

            by_mode.append(by_mode_item)

        failed = d.pop("failed")

        failure_rate = d.pop("failure_rate")

        flagged = d.pop("flagged")

        pass_rate = d.pop("pass_rate")

        passed = d.pop("passed")

        total = d.pop("total")

        non_manual_evaluation_summary_response = cls(
            by_mode=by_mode,
            failed=failed,
            failure_rate=failure_rate,
            flagged=flagged,
            pass_rate=pass_rate,
            passed=passed,
            total=total,
        )

        non_manual_evaluation_summary_response.additional_properties = d
        return non_manual_evaluation_summary_response

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
