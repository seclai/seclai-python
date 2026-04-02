from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_alert_config_request_threshold_type_0 import (
        CreateAlertConfigRequestThresholdType0,
    )


T = TypeVar("T", bound="CreateAlertConfigRequest")


@_attrs_define
class CreateAlertConfigRequest:
    """
    Attributes:
        alert_type (str): Alert type
        agent_id (None | str | Unset): Agent ID (for agent alerts)
        cooldown_minutes (int | Unset): Cooldown period in minutes Default: 60.
        distribution_type (str | Unset): Distribution type (owner, owner_admins, selected_members) Default: 'owner'.
        enabled (bool | Unset): Whether the alert config is enabled Default: True.
        recipient_user_ids (list[str] | None | Unset): User IDs for selected_members distribution
        source_connection_id (None | str | Unset): Source connection ID (for source alerts)
        threshold (CreateAlertConfigRequestThresholdType0 | None | Unset): Threshold configuration
    """

    alert_type: str
    agent_id: None | str | Unset = UNSET
    cooldown_minutes: int | Unset = 60
    distribution_type: str | Unset = "owner"
    enabled: bool | Unset = True
    recipient_user_ids: list[str] | None | Unset = UNSET
    source_connection_id: None | str | Unset = UNSET
    threshold: CreateAlertConfigRequestThresholdType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_alert_config_request_threshold_type_0 import (
            CreateAlertConfigRequestThresholdType0,
        )

        alert_type = self.alert_type

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        cooldown_minutes = self.cooldown_minutes

        distribution_type = self.distribution_type

        enabled = self.enabled

        recipient_user_ids: list[str] | None | Unset
        if isinstance(self.recipient_user_ids, Unset):
            recipient_user_ids = UNSET
        elif isinstance(self.recipient_user_ids, list):
            recipient_user_ids = self.recipient_user_ids

        else:
            recipient_user_ids = self.recipient_user_ids

        source_connection_id: None | str | Unset
        if isinstance(self.source_connection_id, Unset):
            source_connection_id = UNSET
        else:
            source_connection_id = self.source_connection_id

        threshold: dict[str, Any] | None | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        elif isinstance(self.threshold, CreateAlertConfigRequestThresholdType0):
            threshold = self.threshold.to_dict()
        else:
            threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_type": alert_type,
            }
        )
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if cooldown_minutes is not UNSET:
            field_dict["cooldown_minutes"] = cooldown_minutes
        if distribution_type is not UNSET:
            field_dict["distribution_type"] = distribution_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if recipient_user_ids is not UNSET:
            field_dict["recipient_user_ids"] = recipient_user_ids
        if source_connection_id is not UNSET:
            field_dict["source_connection_id"] = source_connection_id
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_alert_config_request_threshold_type_0 import (
            CreateAlertConfigRequestThresholdType0,
        )

        d = dict(src_dict)
        alert_type = d.pop("alert_type")

        def _parse_agent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        cooldown_minutes = d.pop("cooldown_minutes", UNSET)

        distribution_type = d.pop("distribution_type", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_recipient_user_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipient_user_ids_type_0 = cast(list[str], data)

                return recipient_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recipient_user_ids = _parse_recipient_user_ids(
            d.pop("recipient_user_ids", UNSET)
        )

        def _parse_source_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_connection_id = _parse_source_connection_id(
            d.pop("source_connection_id", UNSET)
        )

        def _parse_threshold(
            data: object,
        ) -> CreateAlertConfigRequestThresholdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                threshold_type_0 = CreateAlertConfigRequestThresholdType0.from_dict(
                    data
                )

                return threshold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAlertConfigRequestThresholdType0 | None | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))

        create_alert_config_request = cls(
            alert_type=alert_type,
            agent_id=agent_id,
            cooldown_minutes=cooldown_minutes,
            distribution_type=distribution_type,
            enabled=enabled,
            recipient_user_ids=recipient_user_ids,
            source_connection_id=source_connection_id,
            threshold=threshold,
        )

        create_alert_config_request.additional_properties = d
        return create_alert_config_request

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
