from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_run_stream_request_metadata_type_0 import (
        AgentRunStreamRequestMetadataType0,
    )


T = TypeVar("T", bound="AgentRunStreamRequest")


@_attrs_define
class AgentRunStreamRequest:
    """
    Attributes:
        input_ (None | str | Unset): Input to provide to the agent upon running for agents with dynamic triggers.
        input_upload_id (None | Unset | UUID): ID of a previously uploaded file (via POST /{agent_id}/upload-input) to
            use as the run input for dynamic-input triggers. Mutually exclusive with the 'input' field.
        metadata (AgentRunStreamRequestMetadataType0 | None | Unset): Metadata to make available for string substitution
            expressions in agent tasks.
    """

    input_: None | str | Unset = UNSET
    input_upload_id: None | Unset | UUID = UNSET
    metadata: AgentRunStreamRequestMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_stream_request_metadata_type_0 import (
            AgentRunStreamRequestMetadataType0,
        )

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        input_upload_id: None | str | Unset
        if isinstance(self.input_upload_id, Unset):
            input_upload_id = UNSET
        elif isinstance(self.input_upload_id, UUID):
            input_upload_id = str(self.input_upload_id)
        else:
            input_upload_id = self.input_upload_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AgentRunStreamRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if input_upload_id is not UNSET:
            field_dict["input_upload_id"] = input_upload_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_stream_request_metadata_type_0 import (
            AgentRunStreamRequestMetadataType0,
        )

        d = dict(src_dict)

        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_input_upload_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                input_upload_id_type_0 = UUID(data)

                return input_upload_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        input_upload_id = _parse_input_upload_id(d.pop("input_upload_id", UNSET))

        def _parse_metadata(
            data: object,
        ) -> AgentRunStreamRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentRunStreamRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentRunStreamRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        agent_run_stream_request = cls(
            input_=input_,
            input_upload_id=input_upload_id,
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
