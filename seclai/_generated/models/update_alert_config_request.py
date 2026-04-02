from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_config_request_threshold_type_0 import (
        UpdateAlertConfigRequestThresholdType0,
    )


T = TypeVar("T", bound="UpdateAlertConfigRequest")


@_attrs_define
class UpdateAlertConfigRequest:
    """
    Attributes:
        cooldown_minutes (int | None | Unset): Cooldown period in minutes
        distribution_type (None | str | Unset): Distribution type
        enabled (bool | None | Unset): Whether the alert config is enabled
        recipient_user_ids (list[str] | None | Unset): User IDs for selected_members distribution
        threshold (None | Unset | UpdateAlertConfigRequestThresholdType0): Threshold configuration
    """

    cooldown_minutes: int | None | Unset = UNSET
    distribution_type: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    recipient_user_ids: list[str] | None | Unset = UNSET
    threshold: None | Unset | UpdateAlertConfigRequestThresholdType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_alert_config_request_threshold_type_0 import (
            UpdateAlertConfigRequestThresholdType0,
        )

        cooldown_minutes: int | None | Unset
        if isinstance(self.cooldown_minutes, Unset):
            cooldown_minutes = UNSET
        else:
            cooldown_minutes = self.cooldown_minutes

        distribution_type: None | str | Unset
        if isinstance(self.distribution_type, Unset):
            distribution_type = UNSET
        else:
            distribution_type = self.distribution_type

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        recipient_user_ids: list[str] | None | Unset
        if isinstance(self.recipient_user_ids, Unset):
            recipient_user_ids = UNSET
        elif isinstance(self.recipient_user_ids, list):
            recipient_user_ids = self.recipient_user_ids

        else:
            recipient_user_ids = self.recipient_user_ids

        threshold: dict[str, Any] | None | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        elif isinstance(self.threshold, UpdateAlertConfigRequestThresholdType0):
            threshold = self.threshold.to_dict()
        else:
            threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cooldown_minutes is not UNSET:
            field_dict["cooldown_minutes"] = cooldown_minutes
        if distribution_type is not UNSET:
            field_dict["distribution_type"] = distribution_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if recipient_user_ids is not UNSET:
            field_dict["recipient_user_ids"] = recipient_user_ids
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_alert_config_request_threshold_type_0 import (
            UpdateAlertConfigRequestThresholdType0,
        )

        d = dict(src_dict)

        def _parse_cooldown_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cooldown_minutes = _parse_cooldown_minutes(d.pop("cooldown_minutes", UNSET))

        def _parse_distribution_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distribution_type = _parse_distribution_type(d.pop("distribution_type", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

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

        def _parse_threshold(
            data: object,
        ) -> None | Unset | UpdateAlertConfigRequestThresholdType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                threshold_type_0 = UpdateAlertConfigRequestThresholdType0.from_dict(
                    data
                )

                return threshold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAlertConfigRequestThresholdType0, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))

        update_alert_config_request = cls(
            cooldown_minutes=cooldown_minutes,
            distribution_type=distribution_type,
            enabled=enabled,
            recipient_user_ids=recipient_user_ids,
            threshold=threshold,
        )

        update_alert_config_request.additional_properties = d
        return update_alert_config_request

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
