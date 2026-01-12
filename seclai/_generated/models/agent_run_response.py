from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pending_processing_completed_failed_status import PendingProcessingCompletedFailedStatus

if TYPE_CHECKING:
    from ..models.agent_run_attempt_response import AgentRunAttemptResponse


T = TypeVar("T", bound="AgentRunResponse")


@_attrs_define
class AgentRunResponse:
    """
    Attributes:
        attempts (list[AgentRunAttemptResponse]): List of attempts made for this agent run.
        credits_ (float | None): Credits consumed by the agent run, if applicable.
        error_count (int): Number of errors encountered during the run.
        input_ (None | str): Input provided to the agent for this run.
        output (None | str): Output produced by the agent run.
        priority (bool): Indicates if the run was treated as a priority execution.
        run_id (str): Unique identifier for the agent run.
        status (PendingProcessingCompletedFailedStatus):
    """

    attempts: list[AgentRunAttemptResponse]
    credits_: float | None
    error_count: int
    input_: None | str
    output: None | str
    priority: bool
    run_id: str
    status: PendingProcessingCompletedFailedStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempts = []
        for attempts_item_data in self.attempts:
            attempts_item = attempts_item_data.to_dict()
            attempts.append(attempts_item)

        credits_: float | None
        credits_ = self.credits_

        error_count = self.error_count

        input_: None | str
        input_ = self.input_

        output: None | str
        output = self.output

        priority = self.priority

        run_id = self.run_id

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "credits": credits_,
                "error_count": error_count,
                "input": input_,
                "output": output,
                "priority": priority,
                "run_id": run_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_attempt_response import AgentRunAttemptResponse

        d = dict(src_dict)
        attempts = []
        _attempts = d.pop("attempts")
        for attempts_item_data in _attempts:
            attempts_item = AgentRunAttemptResponse.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        def _parse_credits_(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        credits_ = _parse_credits_(d.pop("credits"))

        error_count = d.pop("error_count")

        def _parse_input_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_output(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output = _parse_output(d.pop("output"))

        priority = d.pop("priority")

        run_id = d.pop("run_id")

        status = PendingProcessingCompletedFailedStatus(d.pop("status"))

        agent_run_response = cls(
            attempts=attempts,
            credits_=credits_,
            error_count=error_count,
            input_=input_,
            output=output,
            priority=priority,
            run_id=run_id,
            status=status,
        )

        agent_run_response.additional_properties = d
        return agent_run_response

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
