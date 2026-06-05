from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRunToolCallResponse")


@_attrs_define
class AgentRunToolCallResponse:
    """A single LLM tool call made during a prompt_call step.

    Attributes:
        function_name (str): Name of the tool/function invoked.
        id (str): Tool call identifier.
        credits_used (float | Unset): Credits consumed by this tool call (0 for tools that don't bill). Default: 0.0.
        duration_seconds (float | None | Unset): Duration of the tool call in seconds.
        ended_at (None | str | Unset): Timestamp when the tool call ended.
        error (None | str | Unset): Error message when the tool call failed.
        input_ (None | str | Unset): JSON arguments the LLM passed to the tool, if persisted.
        output (None | str | Unset): JSON result the tool returned to the LLM, if persisted.
        round_index (int | Unset): 0-based tool-loop round this call belonged to. Default: 0.
        sequence (int | Unset): 0-based ordinal of this call within its step run. Default: 0.
        started_at (None | str | Unset): Timestamp when the tool call started.
        succeeded (bool | Unset): Whether the tool call completed without error. Default: True.
    """

    function_name: str
    id: str
    credits_used: float | Unset = 0.0
    duration_seconds: float | None | Unset = UNSET
    ended_at: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    input_: None | str | Unset = UNSET
    output: None | str | Unset = UNSET
    round_index: int | Unset = 0
    sequence: int | Unset = 0
    started_at: None | str | Unset = UNSET
    succeeded: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_name = self.function_name

        id = self.id

        credits_used = self.credits_used

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = self.ended_at

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        round_index = self.round_index

        sequence = self.sequence

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        succeeded = self.succeeded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function_name": function_name,
                "id": id,
            }
        )
        if credits_used is not UNSET:
            field_dict["credits_used"] = credits_used
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if error is not UNSET:
            field_dict["error"] = error
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if round_index is not UNSET:
            field_dict["round_index"] = round_index
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function_name = d.pop("function_name")

        id = d.pop("id")

        credits_used = d.pop("credits_used", UNSET)

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_ended_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        round_index = d.pop("round_index", UNSET)

        sequence = d.pop("sequence", UNSET)

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        succeeded = d.pop("succeeded", UNSET)

        agent_run_tool_call_response = cls(
            function_name=function_name,
            id=id,
            credits_used=credits_used,
            duration_seconds=duration_seconds,
            ended_at=ended_at,
            error=error,
            input_=input_,
            output=output,
            round_index=round_index,
            sequence=sequence,
            started_at=started_at,
            succeeded=succeeded,
        )

        agent_run_tool_call_response.additional_properties = d
        return agent_run_tool_call_response

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
