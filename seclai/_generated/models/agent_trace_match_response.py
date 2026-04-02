from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentTraceMatchResponse")


@_attrs_define
class AgentTraceMatchResponse:
    """
    Attributes:
        agent_id (None | str): Agent ID.
        agent_run_id (None | str): Agent run ID.
        agent_run_status (None | str): Status of the agent run.
        agent_step_id (None | str): Step identifier.
        agent_step_run_id (None | str): Agent step run ID.
        agent_step_type (None | str): Type of the step.
        score (float): Similarity score (0-1, higher is better).
        text (str): Matching text chunk.
        title (None | str): Title of the indexed entry.
    """

    agent_id: None | str
    agent_run_id: None | str
    agent_run_status: None | str
    agent_step_id: None | str
    agent_step_run_id: None | str
    agent_step_type: None | str
    score: float
    text: str
    title: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id: None | str
        agent_id = self.agent_id

        agent_run_id: None | str
        agent_run_id = self.agent_run_id

        agent_run_status: None | str
        agent_run_status = self.agent_run_status

        agent_step_id: None | str
        agent_step_id = self.agent_step_id

        agent_step_run_id: None | str
        agent_step_run_id = self.agent_step_run_id

        agent_step_type: None | str
        agent_step_type = self.agent_step_type

        score = self.score

        text = self.text

        title: None | str
        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_run_id": agent_run_id,
                "agent_run_status": agent_run_status,
                "agent_step_id": agent_step_id,
                "agent_step_run_id": agent_step_run_id,
                "agent_step_type": agent_step_type,
                "score": score,
                "text": text,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_agent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        def _parse_agent_run_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_run_id = _parse_agent_run_id(d.pop("agent_run_id"))

        def _parse_agent_run_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_run_status = _parse_agent_run_status(d.pop("agent_run_status"))

        def _parse_agent_step_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_step_id = _parse_agent_step_id(d.pop("agent_step_id"))

        def _parse_agent_step_run_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_step_run_id = _parse_agent_step_run_id(d.pop("agent_step_run_id"))

        def _parse_agent_step_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_step_type = _parse_agent_step_type(d.pop("agent_step_type"))

        score = d.pop("score")

        text = d.pop("text")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        agent_trace_match_response = cls(
            agent_id=agent_id,
            agent_run_id=agent_run_id,
            agent_run_status=agent_run_status,
            agent_step_id=agent_step_id,
            agent_step_run_id=agent_step_run_id,
            agent_step_type=agent_step_type,
            score=score,
            text=text,
            title=title,
        )

        agent_trace_match_response.additional_properties = d
        return agent_trace_match_response

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
