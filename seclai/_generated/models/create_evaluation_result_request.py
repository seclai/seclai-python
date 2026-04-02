from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evaluation_status import EvaluationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_evaluation_result_request_details_type_0 import (
        CreateEvaluationResultRequestDetailsType0,
    )


T = TypeVar("T", bound="CreateEvaluationResultRequest")


@_attrs_define
class CreateEvaluationResultRequest:
    """Request body for recording an evaluation result.

    Attributes:
        agent_run_id (UUID):
        status (EvaluationStatus): Result status of a single evaluation run.
        agent_step_run_id (None | Unset | UUID):
        details (CreateEvaluationResultRequestDetailsType0 | None | Unset):
        flagged (bool | Unset):  Default: False.
        retry_count (int | Unset):  Default: 0.
        retry_triggered (bool | Unset):  Default: False.
        score (float | None | Unset):
    """

    agent_run_id: UUID
    status: EvaluationStatus
    agent_step_run_id: None | Unset | UUID = UNSET
    details: CreateEvaluationResultRequestDetailsType0 | None | Unset = UNSET
    flagged: bool | Unset = False
    retry_count: int | Unset = 0
    retry_triggered: bool | Unset = False
    score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_evaluation_result_request_details_type_0 import (
            CreateEvaluationResultRequestDetailsType0,
        )

        agent_run_id = str(self.agent_run_id)

        status = self.status.value

        agent_step_run_id: None | str | Unset
        if isinstance(self.agent_step_run_id, Unset):
            agent_step_run_id = UNSET
        elif isinstance(self.agent_step_run_id, UUID):
            agent_step_run_id = str(self.agent_step_run_id)
        else:
            agent_step_run_id = self.agent_step_run_id

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, CreateEvaluationResultRequestDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        flagged = self.flagged

        retry_count = self.retry_count

        retry_triggered = self.retry_triggered

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
                "status": status,
            }
        )
        if agent_step_run_id is not UNSET:
            field_dict["agent_step_run_id"] = agent_step_run_id
        if details is not UNSET:
            field_dict["details"] = details
        if flagged is not UNSET:
            field_dict["flagged"] = flagged
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if retry_triggered is not UNSET:
            field_dict["retry_triggered"] = retry_triggered
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_evaluation_result_request_details_type_0 import (
            CreateEvaluationResultRequestDetailsType0,
        )

        d = dict(src_dict)
        agent_run_id = UUID(d.pop("agent_run_id"))

        status = EvaluationStatus(d.pop("status"))

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

        def _parse_details(
            data: object,
        ) -> CreateEvaluationResultRequestDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = CreateEvaluationResultRequestDetailsType0.from_dict(
                    data
                )

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateEvaluationResultRequestDetailsType0 | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        flagged = d.pop("flagged", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        retry_triggered = d.pop("retry_triggered", UNSET)

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        create_evaluation_result_request = cls(
            agent_run_id=agent_run_id,
            status=status,
            agent_step_run_id=agent_step_run_id,
            details=details,
            flagged=flagged,
            retry_count=retry_count,
            retry_triggered=retry_triggered,
            score=score,
        )

        create_evaluation_result_request.additional_properties = d
        return create_evaluation_result_request

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
