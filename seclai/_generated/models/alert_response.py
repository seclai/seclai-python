from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertResponse")


@_attrs_define
class AlertResponse:
    """
    Attributes:
        account_id (str):
        agent_id (None | str):
        agent_run_id (None | str):
        alert_config_id (None | str):
        alert_type (str):
        comment_count (int):
        created_at (None | str):
        description (None | str):
        id (str):
        is_subscribed (bool):
        mcp_client_id (None | str):
        source_connection_id (None | str):
        source_connection_pull_id (None | str):
        status (str):
        subscriber_count (int):
        title (str):
        updated_at (None | str):
        details (Any | Unset):
    """

    account_id: str
    agent_id: None | str
    agent_run_id: None | str
    alert_config_id: None | str
    alert_type: str
    comment_count: int
    created_at: None | str
    description: None | str
    id: str
    is_subscribed: bool
    mcp_client_id: None | str
    source_connection_id: None | str
    source_connection_pull_id: None | str
    status: str
    subscriber_count: int
    title: str
    updated_at: None | str
    details: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        agent_id: None | str
        agent_id = self.agent_id

        agent_run_id: None | str
        agent_run_id = self.agent_run_id

        alert_config_id: None | str
        alert_config_id = self.alert_config_id

        alert_type = self.alert_type

        comment_count = self.comment_count

        created_at: None | str
        created_at = self.created_at

        description: None | str
        description = self.description

        id = self.id

        is_subscribed = self.is_subscribed

        mcp_client_id: None | str
        mcp_client_id = self.mcp_client_id

        source_connection_id: None | str
        source_connection_id = self.source_connection_id

        source_connection_pull_id: None | str
        source_connection_pull_id = self.source_connection_pull_id

        status = self.status

        subscriber_count = self.subscriber_count

        title = self.title

        updated_at: None | str
        updated_at = self.updated_at

        details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "agent_id": agent_id,
                "agent_run_id": agent_run_id,
                "alert_config_id": alert_config_id,
                "alert_type": alert_type,
                "comment_count": comment_count,
                "created_at": created_at,
                "description": description,
                "id": id,
                "is_subscribed": is_subscribed,
                "mcp_client_id": mcp_client_id,
                "source_connection_id": source_connection_id,
                "source_connection_pull_id": source_connection_pull_id,
                "status": status,
                "subscriber_count": subscriber_count,
                "title": title,
                "updated_at": updated_at,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

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

        def _parse_agent_run_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_run_id = _parse_agent_run_id(d.pop("agent_run_id"))

        def _parse_alert_config_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        alert_config_id = _parse_alert_config_id(d.pop("alert_config_id"))

        alert_type = d.pop("alert_type")

        comment_count = d.pop("comment_count")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = d.pop("id")

        is_subscribed = d.pop("is_subscribed")

        def _parse_mcp_client_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mcp_client_id = _parse_mcp_client_id(d.pop("mcp_client_id"))

        def _parse_source_connection_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_connection_id = _parse_source_connection_id(
            d.pop("source_connection_id")
        )

        def _parse_source_connection_pull_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_connection_pull_id = _parse_source_connection_pull_id(
            d.pop("source_connection_pull_id")
        )

        status = d.pop("status")

        subscriber_count = d.pop("subscriber_count")

        title = d.pop("title")

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        details = d.pop("details", UNSET)

        alert_response = cls(
            account_id=account_id,
            agent_id=agent_id,
            agent_run_id=agent_run_id,
            alert_config_id=alert_config_id,
            alert_type=alert_type,
            comment_count=comment_count,
            created_at=created_at,
            description=description,
            id=id,
            is_subscribed=is_subscribed,
            mcp_client_id=mcp_client_id,
            source_connection_id=source_connection_id,
            source_connection_pull_id=source_connection_pull_id,
            status=status,
            subscriber_count=subscriber_count,
            title=title,
            updated_at=updated_at,
            details=details,
        )

        alert_response.additional_properties = d
        return alert_response

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
