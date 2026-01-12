from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_agent_request_metadata_type_0 import RunAgentRequestMetadataType0


T = TypeVar("T", bound="RunAgentRequest")


@_attrs_define
class RunAgentRequest:
    """Request model for running an agent

    Attributes:
        content_version_id (None | Unset | UUID): ContentVersion id for content-based triggers (CONTENT_ADDED /
            CONTENT_UPDATED).
        input_ (None | str | Unset): Input for agents with DYNAMIC_INPUT trigger type
        metadata (None | RunAgentRequestMetadataType0 | Unset): Metadata for string substitutions
        priority (bool | Unset): If true, run in priority mode (worker instance) Default: False.
    """

    content_version_id: None | Unset | UUID = UNSET
    input_: None | str | Unset = UNSET
    metadata: None | RunAgentRequestMetadataType0 | Unset = UNSET
    priority: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.run_agent_request_metadata_type_0 import RunAgentRequestMetadataType0

        content_version_id: None | str | Unset
        if isinstance(self.content_version_id, Unset):
            content_version_id = UNSET
        elif isinstance(self.content_version_id, UUID):
            content_version_id = str(self.content_version_id)
        else:
            content_version_id = self.content_version_id

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, RunAgentRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_version_id is not UNSET:
            field_dict["content_version_id"] = content_version_id
        if input_ is not UNSET:
            field_dict["input"] = input_
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_agent_request_metadata_type_0 import RunAgentRequestMetadataType0

        d = dict(src_dict)

        def _parse_content_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                content_version_id_type_0 = UUID(data)

                return content_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        content_version_id = _parse_content_version_id(d.pop("content_version_id", UNSET))

        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_metadata(data: object) -> None | RunAgentRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = RunAgentRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunAgentRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        priority = d.pop("priority", UNSET)

        run_agent_request = cls(
            content_version_id=content_version_id,
            input_=input_,
            metadata=metadata,
            priority=priority,
        )

        run_agent_request.additional_properties = d
        return run_agent_request

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
