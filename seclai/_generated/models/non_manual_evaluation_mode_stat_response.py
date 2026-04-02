from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NonManualEvaluationModeStatResponse")


@_attrs_define
class NonManualEvaluationModeStatResponse:
    """Per-mode rollup for evaluation activity.

    Attributes:
        failed (int):
        failure_rate (float):
        flagged (int):
        mode (str):
        pass_rate (float):
        passed (int):
        total (int):
    """

    failed: int
    failure_rate: float
    flagged: int
    mode: str
    pass_rate: float
    passed: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed = self.failed

        failure_rate = self.failure_rate

        flagged = self.flagged

        mode = self.mode

        pass_rate = self.pass_rate

        passed = self.passed

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failed": failed,
                "failure_rate": failure_rate,
                "flagged": flagged,
                "mode": mode,
                "pass_rate": pass_rate,
                "passed": passed,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed = d.pop("failed")

        failure_rate = d.pop("failure_rate")

        flagged = d.pop("flagged")

        mode = d.pop("mode")

        pass_rate = d.pop("pass_rate")

        passed = d.pop("passed")

        total = d.pop("total")

        non_manual_evaluation_mode_stat_response = cls(
            failed=failed,
            failure_rate=failure_rate,
            flagged=flagged,
            mode=mode,
            pass_rate=pass_rate,
            passed=passed,
            total=total,
        )

        non_manual_evaluation_mode_stat_response.additional_properties = d
        return non_manual_evaluation_mode_stat_response

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
