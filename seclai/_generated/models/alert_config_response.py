from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_config_response_threshold_type_0 import (
        AlertConfigResponseThresholdType0,
    )


T = TypeVar("T", bound="AlertConfigResponse")


@_attrs_define
class AlertConfigResponse:
    """
    Attributes:
        account_id (str):
        agent_id (None | str):
        alert_type (str):
        cooldown_minutes (int):
        created_at (None | str):
        distribution_type (str):
        enabled (bool):
        id (str):
        last_alerted_at (None | str):
        recipient_user_ids (list[str]):
        source_connection_id (None | str):
        threshold (AlertConfigResponseThresholdType0 | None):
        updated_at (None | str):
    """

    account_id: str
    agent_id: None | str
    alert_type: str
    cooldown_minutes: int
    created_at: None | str
    distribution_type: str
    enabled: bool
    id: str
    last_alerted_at: None | str
    recipient_user_ids: list[str]
    source_connection_id: None | str
    threshold: AlertConfigResponseThresholdType0 | None
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_config_response_threshold_type_0 import (
            AlertConfigResponseThresholdType0,
        )

        account_id = self.account_id

        agent_id: None | str
        agent_id = self.agent_id

        alert_type = self.alert_type

        cooldown_minutes = self.cooldown_minutes

        created_at: None | str
        created_at = self.created_at

        distribution_type = self.distribution_type

        enabled = self.enabled

        id = self.id

        last_alerted_at: None | str
        last_alerted_at = self.last_alerted_at

        recipient_user_ids = self.recipient_user_ids

        source_connection_id: None | str
        source_connection_id = self.source_connection_id

        threshold: dict[str, Any] | None
        if isinstance(self.threshold, AlertConfigResponseThresholdType0):
            threshold = self.threshold.to_dict()
        else:
            threshold = self.threshold

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "agent_id": agent_id,
                "alert_type": alert_type,
                "cooldown_minutes": cooldown_minutes,
                "created_at": created_at,
                "distribution_type": distribution_type,
                "enabled": enabled,
                "id": id,
                "last_alerted_at": last_alerted_at,
                "recipient_user_ids": recipient_user_ids,
                "source_connection_id": source_connection_id,
                "threshold": threshold,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_config_response_threshold_type_0 import (
            AlertConfigResponseThresholdType0,
        )

        d = dict(src_dict)
        account_id = d.pop("account_id")

        def _parse_agent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        alert_type = d.pop("alert_type")

        cooldown_minutes = d.pop("cooldown_minutes")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        distribution_type = d.pop("distribution_type")

        enabled = d.pop("enabled")

        id = d.pop("id")

        def _parse_last_alerted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_alerted_at = _parse_last_alerted_at(d.pop("last_alerted_at"))

        recipient_user_ids = cast(list[str], d.pop("recipient_user_ids"))

        def _parse_source_connection_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_connection_id = _parse_source_connection_id(
            d.pop("source_connection_id")
        )

        def _parse_threshold(data: object) -> AlertConfigResponseThresholdType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                threshold_type_0 = AlertConfigResponseThresholdType0.from_dict(data)

                return threshold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertConfigResponseThresholdType0 | None, data)

        threshold = _parse_threshold(d.pop("threshold"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        alert_config_response = cls(
            account_id=account_id,
            agent_id=agent_id,
            alert_type=alert_type,
            cooldown_minutes=cooldown_minutes,
            created_at=created_at,
            distribution_type=distribution_type,
            enabled=enabled,
            id=id,
            last_alerted_at=last_alerted_at,
            recipient_user_ids=recipient_user_ids,
            source_connection_id=source_connection_id,
            threshold=threshold,
            updated_at=updated_at,
        )

        alert_config_response.additional_properties = d
        return alert_config_response

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
