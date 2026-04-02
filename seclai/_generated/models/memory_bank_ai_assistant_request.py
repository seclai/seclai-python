from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_bank_ai_assistant_request_current_config_type_0 import (
        MemoryBankAiAssistantRequestCurrentConfigType0,
    )


T = TypeVar("T", bound="MemoryBankAiAssistantRequest")


@_attrs_define
class MemoryBankAiAssistantRequest:
    """Request body for the memory bank AI assistant.

    Attributes:
        user_input (str): Natural-language description of the memory bank.
        conversation_id (None | str | Unset): Previous conversation ID to continue.
        current_config (MemoryBankAiAssistantRequestCurrentConfigType0 | None | Unset): Current configuration to refine,
            if any.
    """

    user_input: str
    conversation_id: None | str | Unset = UNSET
    current_config: MemoryBankAiAssistantRequestCurrentConfigType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_bank_ai_assistant_request_current_config_type_0 import (
            MemoryBankAiAssistantRequestCurrentConfigType0,
        )

        user_input = self.user_input

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        current_config: dict[str, Any] | None | Unset
        if isinstance(self.current_config, Unset):
            current_config = UNSET
        elif isinstance(
            self.current_config, MemoryBankAiAssistantRequestCurrentConfigType0
        ):
            current_config = self.current_config.to_dict()
        else:
            current_config = self.current_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_input": user_input,
            }
        )
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if current_config is not UNSET:
            field_dict["current_config"] = current_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_bank_ai_assistant_request_current_config_type_0 import (
            MemoryBankAiAssistantRequestCurrentConfigType0,
        )

        d = dict(src_dict)
        user_input = d.pop("user_input")

        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversation_id", UNSET))

        def _parse_current_config(
            data: object,
        ) -> MemoryBankAiAssistantRequestCurrentConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_config_type_0 = (
                    MemoryBankAiAssistantRequestCurrentConfigType0.from_dict(data)
                )

                return current_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MemoryBankAiAssistantRequestCurrentConfigType0 | None | Unset, data
            )

        current_config = _parse_current_config(d.pop("current_config", UNSET))

        memory_bank_ai_assistant_request = cls(
            user_input=user_input,
            conversation_id=conversation_id,
            current_config=current_config,
        )

        memory_bank_ai_assistant_request.additional_properties = d
        return memory_bank_ai_assistant_request

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
