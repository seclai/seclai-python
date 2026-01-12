from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_trigger_type import AgentTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_trigger_request_metadata_type_0 import UpdateTriggerRequestMetadataType0


T = TypeVar("T", bound="UpdateTriggerRequest")


@_attrs_define
class UpdateTriggerRequest:
    """Request model for updating an agent trigger

    Attributes:
        input_ (None | str | Unset): Template input for TEMPLATE_INPUT trigger type
        knowledge_base_id (None | Unset | UUID): Knowledge base for content triggers
        metadata (None | Unset | UpdateTriggerRequestMetadataType0): Metadata for string substitutions
        name (None | str | Unset): Trigger name
        trigger_type (AgentTriggerType | None | Unset): The type of trigger
    """

    input_: None | str | Unset = UNSET
    knowledge_base_id: None | Unset | UUID = UNSET
    metadata: None | Unset | UpdateTriggerRequestMetadataType0 = UNSET
    name: None | str | Unset = UNSET
    trigger_type: AgentTriggerType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_trigger_request_metadata_type_0 import UpdateTriggerRequestMetadataType0

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        knowledge_base_id: None | str | Unset
        if isinstance(self.knowledge_base_id, Unset):
            knowledge_base_id = UNSET
        elif isinstance(self.knowledge_base_id, UUID):
            knowledge_base_id = str(self.knowledge_base_id)
        else:
            knowledge_base_id = self.knowledge_base_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateTriggerRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        elif isinstance(self.trigger_type, AgentTriggerType):
            trigger_type = self.trigger_type.value
        else:
            trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if knowledge_base_id is not UNSET:
            field_dict["knowledge_base_id"] = knowledge_base_id
        if metadata is not UNSET:
            field_dict["metadata_"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_trigger_request_metadata_type_0 import UpdateTriggerRequestMetadataType0

        d = dict(src_dict)

        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_knowledge_base_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_base_id_type_0 = UUID(data)

                return knowledge_base_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        knowledge_base_id = _parse_knowledge_base_id(d.pop("knowledge_base_id", UNSET))

        def _parse_metadata(data: object) -> None | Unset | UpdateTriggerRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateTriggerRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTriggerRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata_", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_trigger_type(data: object) -> AgentTriggerType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_type_type_0 = AgentTriggerType(data)

                return trigger_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentTriggerType | None | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        update_trigger_request = cls(
            input_=input_,
            knowledge_base_id=knowledge_base_id,
            metadata=metadata,
            name=name,
            trigger_type=trigger_type,
        )

        update_trigger_request.additional_properties = d
        return update_trigger_request

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
