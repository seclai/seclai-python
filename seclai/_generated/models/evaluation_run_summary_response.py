from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EvaluationRunSummaryResponse")


@_attrs_define
class EvaluationRunSummaryResponse:
    """Per-run evaluation summary with pass/fail/error breakdown.

    Attributes:
        agent_run_id (UUID):
        error_count (int):
        failed_count (int):
        flagged_count (int):
        passed_count (int):
        run_created_at (str):
        run_status (str): Status of the agent run (processing, completed, failed).
        skipped_count (int):
        total_evaluations (int):
    """

    agent_run_id: UUID
    error_count: int
    failed_count: int
    flagged_count: int
    passed_count: int
    run_created_at: str
    run_status: str
    skipped_count: int
    total_evaluations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_run_id = str(self.agent_run_id)

        error_count = self.error_count

        failed_count = self.failed_count

        flagged_count = self.flagged_count

        passed_count = self.passed_count

        run_created_at = self.run_created_at

        run_status = self.run_status

        skipped_count = self.skipped_count

        total_evaluations = self.total_evaluations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_run_id": agent_run_id,
                "error_count": error_count,
                "failed_count": failed_count,
                "flagged_count": flagged_count,
                "passed_count": passed_count,
                "run_created_at": run_created_at,
                "run_status": run_status,
                "skipped_count": skipped_count,
                "total_evaluations": total_evaluations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_run_id = UUID(d.pop("agent_run_id"))

        error_count = d.pop("error_count")

        failed_count = d.pop("failed_count")

        flagged_count = d.pop("flagged_count")

        passed_count = d.pop("passed_count")

        run_created_at = d.pop("run_created_at")

        run_status = d.pop("run_status")

        skipped_count = d.pop("skipped_count")

        total_evaluations = d.pop("total_evaluations")

        evaluation_run_summary_response = cls(
            agent_run_id=agent_run_id,
            error_count=error_count,
            failed_count=failed_count,
            flagged_count=flagged_count,
            passed_count=passed_count,
            run_created_at=run_created_at,
            run_status=run_status,
            skipped_count=skipped_count,
            total_evaluations=total_evaluations,
        )

        evaluation_run_summary_response.additional_properties = d
        return evaluation_run_summary_response

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
