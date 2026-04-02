from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentTraceSearchRequest")


@_attrs_define
class AgentTraceSearchRequest:
    """
    Attributes:
        query (str): Search query text.
        agent_id (None | str | Unset): Filter by agent ID.
        run_status (None | str | Unset): Filter by run status.
        step_type (None | str | Unset): Filter by step type.
        top_n (int | Unset): Maximum number of results. Default: 10.
    """

    query: str
    agent_id: None | str | Unset = UNSET
    run_status: None | str | Unset = UNSET
    step_type: None | str | Unset = UNSET
    top_n: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        run_status: None | str | Unset
        if isinstance(self.run_status, Unset):
            run_status = UNSET
        else:
            run_status = self.run_status

        step_type: None | str | Unset
        if isinstance(self.step_type, Unset):
            step_type = UNSET
        else:
            step_type = self.step_type

        top_n = self.top_n

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if run_status is not UNSET:
            field_dict["run_status"] = run_status
        if step_type is not UNSET:
            field_dict["step_type"] = step_type
        if top_n is not UNSET:
            field_dict["top_n"] = top_n

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_agent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        def _parse_run_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_status = _parse_run_status(d.pop("run_status", UNSET))

        def _parse_step_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_type = _parse_step_type(d.pop("step_type", UNSET))

        top_n = d.pop("top_n", UNSET)

        agent_trace_search_request = cls(
            query=query,
            agent_id=agent_id,
            run_status=run_status,
            step_type=step_type,
            top_n=top_n,
        )

        agent_trace_search_request.additional_properties = d
        return agent_trace_search_request

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
