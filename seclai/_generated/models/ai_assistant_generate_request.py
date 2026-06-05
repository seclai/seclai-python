from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiAssistantGenerateRequest")


@_attrs_define
class AiAssistantGenerateRequest:
    """Request body for AI assistant generate endpoints.

    Attributes:
        user_input (str): User input describing what to do
        history_since (datetime.datetime | None | Unset): Optional ISO 8601 timestamp.  When set, only conversation
            turns created at or after this timestamp are loaded as context, scoping history to the current session so the
            assistant remembers earlier turns in a create flow.
    """

    user_input: str
    history_since: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_input = self.user_input

        history_since: None | str | Unset
        if isinstance(self.history_since, Unset):
            history_since = UNSET
        elif isinstance(self.history_since, datetime.datetime):
            history_since = self.history_since.isoformat()
        else:
            history_since = self.history_since

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_input": user_input,
            }
        )
        if history_since is not UNSET:
            field_dict["history_since"] = history_since

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_input = d.pop("user_input")

        def _parse_history_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                history_since_type_0 = isoparse(data)

                return history_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        history_since = _parse_history_since(d.pop("history_since", UNSET))

        ai_assistant_generate_request = cls(
            user_input=user_input,
            history_since=history_since,
        )

        ai_assistant_generate_request.additional_properties = d
        return ai_assistant_generate_request

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
