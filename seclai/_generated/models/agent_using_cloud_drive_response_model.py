from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentUsingCloudDriveResponseModel")


@_attrs_define
class AgentUsingCloudDriveResponseModel:
    """
    Attributes:
        agent_id (str): Agent identifier.
        agent_name (str): Agent name.
        trigger_types (list[str]): File-change trigger types bound to this drive.
        via_prompt_tool (bool): Uses a prompt_call cloud-drive tool.
        via_step (bool): Uses a list/read/write cloud-drive step.
    """

    agent_id: str
    agent_name: str
    trigger_types: list[str]
    via_prompt_tool: bool
    via_step: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_name = self.agent_name

        trigger_types = self.trigger_types

        via_prompt_tool = self.via_prompt_tool

        via_step = self.via_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_name": agent_name,
                "trigger_types": trigger_types,
                "via_prompt_tool": via_prompt_tool,
                "via_step": via_step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_name = d.pop("agent_name")

        trigger_types = cast(list[str], d.pop("trigger_types"))

        via_prompt_tool = d.pop("via_prompt_tool")

        via_step = d.pop("via_step")

        agent_using_cloud_drive_response_model = cls(
            agent_id=agent_id,
            agent_name=agent_name,
            trigger_types=trigger_types,
            via_prompt_tool=via_prompt_tool,
            via_step=via_step,
        )

        agent_using_cloud_drive_response_model.additional_properties = d
        return agent_using_cloud_drive_response_model

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
