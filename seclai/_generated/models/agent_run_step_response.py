from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pending_processing_completed_failed_status import (
    PendingProcessingCompletedFailedStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_run_file_response import AgentRunFileResponse
    from ..models.agent_run_tool_call_response import AgentRunToolCallResponse


T = TypeVar("T", bound="AgentRunStepResponse")


@_attrs_define
class AgentRunStepResponse:
    """
    Attributes:
        agent_step_id (str): Agent step identifier.
        credits_used (float): Credits consumed by this step across every attempt it made. Some charges made outside any
            step, such as governance screening of the run's input, count toward the run's total but no step's. The
            timestamps above and the tool calls below describe the latest attempt only.
        duration_seconds (float | None): Duration of the step attempt in seconds.
        ended_at (None | str): Timestamp when the step attempt ended.
        input_ (None | str): Input text provided to the step, if any.  Below `Seclai-Version: 2026-09-30`, the manifest
            JSON when the step that produced it output files and is not a `for_each`.
        output (None | str): Output text produced by the step, if any; its files are in `attachments`.  Below `Seclai-
            Version: 2026-09-30`, the manifest JSON when the step output files and is not a `for_each`.
        output_content_type (None | str): Content type of the step output, if any.
        started_at (None | str): Timestamp when the step attempt started.
        status (PendingProcessingCompletedFailedStatus):
        step_type (str): Type of the agent step.
        attachments (list[AgentRunFileResponse] | Unset): Files in this step's output, in order. Empty for steps that
            produced none, for steps run before files were listed here, and once the run's trace is purged.
        tool_calls (list[AgentRunToolCallResponse] | Unset): LLM tool calls made during this step (prompt_call steps
            only), ordered by execution. Empty for steps that invoked no tools.
        warnings (list[str] | None | Unset): Authoring problems the step ran into, whether or not it then failed, such
            as a file name selector that matched none of its source's files.
    """

    agent_step_id: str
    credits_used: float
    duration_seconds: float | None
    ended_at: None | str
    input_: None | str
    output: None | str
    output_content_type: None | str
    started_at: None | str
    status: PendingProcessingCompletedFailedStatus
    step_type: str
    attachments: list[AgentRunFileResponse] | Unset = UNSET
    tool_calls: list[AgentRunToolCallResponse] | Unset = UNSET
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_step_id = self.agent_step_id

        credits_used = self.credits_used

        duration_seconds: float | None
        duration_seconds = self.duration_seconds

        ended_at: None | str
        ended_at = self.ended_at

        input_: None | str
        input_ = self.input_

        output: None | str
        output = self.output

        output_content_type: None | str
        output_content_type = self.output_content_type

        started_at: None | str
        started_at = self.started_at

        status = self.status.value

        step_type = self.step_type

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        tool_calls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = []
            for tool_calls_item_data in self.tool_calls:
                tool_calls_item = tool_calls_item_data.to_dict()
                tool_calls.append(tool_calls_item)

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_step_id": agent_step_id,
                "credits_used": credits_used,
                "duration_seconds": duration_seconds,
                "ended_at": ended_at,
                "input": input_,
                "output": output,
                "output_content_type": output_content_type,
                "started_at": started_at,
                "status": status,
                "step_type": step_type,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_file_response import AgentRunFileResponse
        from ..models.agent_run_tool_call_response import AgentRunToolCallResponse

        d = dict(src_dict)
        agent_step_id = d.pop("agent_step_id")

        credits_used = d.pop("credits_used")

        def _parse_duration_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds"))

        def _parse_ended_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ended_at = _parse_ended_at(d.pop("ended_at"))

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

        def _parse_output_content_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output_content_type = _parse_output_content_type(d.pop("output_content_type"))

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = PendingProcessingCompletedFailedStatus(d.pop("status"))

        step_type = d.pop("step_type")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[AgentRunFileResponse] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = AgentRunFileResponse.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        _tool_calls = d.pop("tool_calls", UNSET)
        tool_calls: list[AgentRunToolCallResponse] | Unset = UNSET
        if _tool_calls is not UNSET:
            tool_calls = []
            for tool_calls_item_data in _tool_calls:
                tool_calls_item = AgentRunToolCallResponse.from_dict(
                    tool_calls_item_data
                )

                tool_calls.append(tool_calls_item)

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        agent_run_step_response = cls(
            agent_step_id=agent_step_id,
            credits_used=credits_used,
            duration_seconds=duration_seconds,
            ended_at=ended_at,
            input_=input_,
            output=output,
            output_content_type=output_content_type,
            started_at=started_at,
            status=status,
            step_type=step_type,
            attachments=attachments,
            tool_calls=tool_calls,
            warnings=warnings,
        )

        agent_run_step_response.additional_properties = d
        return agent_run_step_response

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
