from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_run_stream_request_metadata_type_0 import AgentRunStreamRequestMetadataType0


T = TypeVar("T", bound="AgentRunStreamRequest")


@_attrs_define
class AgentRunStreamRequest:
    """
    Attributes:
        input_ (None | str): Input to provide to the agent upon running for agents with dynamic triggers.
        metadata (AgentRunStreamRequestMetadataType0 | None): Metadata to make available for string substitution
            expressions in agent tasks.
    """

    input_: None | str
    metadata: AgentRunStreamRequestMetadataType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_stream_request_metadata_type_0 import AgentRunStreamRequestMetadataType0

        input_: None | str
        input_ = self.input_

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, AgentRunStreamRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_stream_request_metadata_type_0 import AgentRunStreamRequestMetadataType0

        d = dict(src_dict)

        def _parse_input_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_metadata(data: object) -> AgentRunStreamRequestMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentRunStreamRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentRunStreamRequestMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        agent_run_stream_request = cls(
            input_=input_,
            metadata=metadata,
        )

        agent_run_stream_request.additional_properties = d
        return agent_run_stream_request

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
