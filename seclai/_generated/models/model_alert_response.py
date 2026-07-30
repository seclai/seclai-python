from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelAlertResponse")


@_attrs_define
class ModelAlertResponse:
    """
    Attributes:
        account_id (str):
        agent_id (None | str):
        alert_type (str):
        created_at (str):
        id (str):
        message (str):
        model_name (str):
        prompt_model_id (str):
        read_at (None | str):
        successor_model_name (None | str):
    """

    account_id: str
    agent_id: None | str
    alert_type: str
    created_at: str
    id: str
    message: str
    model_name: str
    prompt_model_id: str
    read_at: None | str
    successor_model_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        agent_id: None | str
        agent_id = self.agent_id

        alert_type = self.alert_type

        created_at = self.created_at

        id = self.id

        message = self.message

        model_name = self.model_name

        prompt_model_id = self.prompt_model_id

        read_at: None | str
        read_at = self.read_at

        successor_model_name: None | str
        successor_model_name = self.successor_model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "agent_id": agent_id,
                "alert_type": alert_type,
                "created_at": created_at,
                "id": id,
                "message": message,
                "model_name": model_name,
                "prompt_model_id": prompt_model_id,
                "read_at": read_at,
                "successor_model_name": successor_model_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        def _parse_agent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        alert_type = d.pop("alert_type")

        created_at = d.pop("created_at")

        id = d.pop("id")

        message = d.pop("message")

        model_name = d.pop("model_name")

        prompt_model_id = d.pop("prompt_model_id")

        def _parse_read_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        read_at = _parse_read_at(d.pop("read_at"))

        def _parse_successor_model_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        successor_model_name = _parse_successor_model_name(
            d.pop("successor_model_name")
        )

        model_alert_response = cls(
            account_id=account_id,
            agent_id=agent_id,
            alert_type=alert_type,
            created_at=created_at,
            id=id,
            message=message,
            model_name=model_name,
            prompt_model_id=prompt_model_id,
            read_at=read_at,
            successor_model_name=successor_model_name,
        )

        model_alert_response.additional_properties = d
        return model_alert_response

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
