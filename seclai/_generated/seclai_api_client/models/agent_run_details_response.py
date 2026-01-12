from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_run_details_response_metadata_type_0 import AgentRunDetailsResponseMetadataType0
    from ..models.agent_run_step_details_response import AgentRunStepDetailsResponse


T = TypeVar("T", bound="AgentRunDetailsResponse")


@_attrs_define
class AgentRunDetailsResponse:
    """Response model for agent run details used by the run history details view.

    Attributes:
        agent_id (UUID):
        input_ (None | str):
        metadata (AgentRunDetailsResponseMetadataType0 | None):
        mode (str):
        run_id (UUID):
        status (str):
        steps (list[AgentRunStepDetailsResponse]):
    """

    agent_id: UUID
    input_: None | str
    metadata: AgentRunDetailsResponseMetadataType0 | None
    mode: str
    run_id: UUID
    status: str
    steps: list[AgentRunStepDetailsResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_details_response_metadata_type_0 import AgentRunDetailsResponseMetadataType0

        agent_id = str(self.agent_id)

        input_: None | str
        input_ = self.input_

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, AgentRunDetailsResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        mode = self.mode

        run_id = str(self.run_id)

        status = self.status

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "input": input_,
                "metadata": metadata,
                "mode": mode,
                "run_id": run_id,
                "status": status,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_details_response_metadata_type_0 import AgentRunDetailsResponseMetadataType0
        from ..models.agent_run_step_details_response import AgentRunStepDetailsResponse

        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        def _parse_input_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_metadata(data: object) -> AgentRunDetailsResponseMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentRunDetailsResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentRunDetailsResponseMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        mode = d.pop("mode")

        run_id = UUID(d.pop("run_id"))

        status = d.pop("status")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = AgentRunStepDetailsResponse.from_dict(steps_item_data)

            steps.append(steps_item)

        agent_run_details_response = cls(
            agent_id=agent_id,
            input_=input_,
            metadata=metadata,
            mode=mode,
            run_id=run_id,
            status=status,
            steps=steps,
        )

        agent_run_details_response.additional_properties = d
        return agent_run_details_response

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
