from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slack_trigger_config_api_response_form_item import (
        SlackTriggerConfigApiResponseFormItem,
    )


T = TypeVar("T", bound="SlackTriggerConfigApiResponse")


@_attrs_define
class SlackTriggerConfigApiResponse:
    """
    Attributes:
        activation (str):
        agent_id (UUID):
        allow_dms (bool):
        channel_ids (list[str]):
        form (list[SlackTriggerConfigApiResponseFormItem]):
        include_invoker_email (bool):
        max_turns (int | None):
        mcp_client_id (None | UUID):
        missing_scopes (list[str]): Scopes the Slack connection lacks for optional features.
        notify_failure_after_answer (bool):
        scope (str):
        slack_team_id (None | str):
        start_without_form (bool):
        trigger_id (UUID):
        turns_anyone (bool):
        turns_enabled (bool):
        visibility (str):
        alias (None | str | Unset): The name people type after `/seclai` to run this agent.
    """

    activation: str
    agent_id: UUID
    allow_dms: bool
    channel_ids: list[str]
    form: list[SlackTriggerConfigApiResponseFormItem]
    include_invoker_email: bool
    max_turns: int | None
    mcp_client_id: None | UUID
    missing_scopes: list[str]
    notify_failure_after_answer: bool
    scope: str
    slack_team_id: None | str
    start_without_form: bool
    trigger_id: UUID
    turns_anyone: bool
    turns_enabled: bool
    visibility: str
    alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activation = self.activation

        agent_id = str(self.agent_id)

        allow_dms = self.allow_dms

        channel_ids = self.channel_ids

        form = []
        for form_item_data in self.form:
            form_item = form_item_data.to_dict()
            form.append(form_item)

        include_invoker_email = self.include_invoker_email

        max_turns: int | None
        max_turns = self.max_turns

        mcp_client_id: None | str
        if isinstance(self.mcp_client_id, UUID):
            mcp_client_id = str(self.mcp_client_id)
        else:
            mcp_client_id = self.mcp_client_id

        missing_scopes = self.missing_scopes

        notify_failure_after_answer = self.notify_failure_after_answer

        scope = self.scope

        slack_team_id: None | str
        slack_team_id = self.slack_team_id

        start_without_form = self.start_without_form

        trigger_id = str(self.trigger_id)

        turns_anyone = self.turns_anyone

        turns_enabled = self.turns_enabled

        visibility = self.visibility

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activation": activation,
                "agent_id": agent_id,
                "allow_dms": allow_dms,
                "channel_ids": channel_ids,
                "form": form,
                "include_invoker_email": include_invoker_email,
                "max_turns": max_turns,
                "mcp_client_id": mcp_client_id,
                "missing_scopes": missing_scopes,
                "notify_failure_after_answer": notify_failure_after_answer,
                "scope": scope,
                "slack_team_id": slack_team_id,
                "start_without_form": start_without_form,
                "trigger_id": trigger_id,
                "turns_anyone": turns_anyone,
                "turns_enabled": turns_enabled,
                "visibility": visibility,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slack_trigger_config_api_response_form_item import (
            SlackTriggerConfigApiResponseFormItem,
        )

        d = dict(src_dict)
        activation = d.pop("activation")

        agent_id = UUID(d.pop("agent_id"))

        allow_dms = d.pop("allow_dms")

        channel_ids = cast(list[str], d.pop("channel_ids"))

        form = []
        _form = d.pop("form")
        for form_item_data in _form:
            form_item = SlackTriggerConfigApiResponseFormItem.from_dict(form_item_data)

            form.append(form_item)

        include_invoker_email = d.pop("include_invoker_email")

        def _parse_max_turns(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_turns = _parse_max_turns(d.pop("max_turns"))

        def _parse_mcp_client_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mcp_client_id_type_0 = UUID(data)

                return mcp_client_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        mcp_client_id = _parse_mcp_client_id(d.pop("mcp_client_id"))

        missing_scopes = cast(list[str], d.pop("missing_scopes"))

        notify_failure_after_answer = d.pop("notify_failure_after_answer")

        scope = d.pop("scope")

        def _parse_slack_team_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slack_team_id = _parse_slack_team_id(d.pop("slack_team_id"))

        start_without_form = d.pop("start_without_form")

        trigger_id = UUID(d.pop("trigger_id"))

        turns_anyone = d.pop("turns_anyone")

        turns_enabled = d.pop("turns_enabled")

        visibility = d.pop("visibility")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        slack_trigger_config_api_response = cls(
            activation=activation,
            agent_id=agent_id,
            allow_dms=allow_dms,
            channel_ids=channel_ids,
            form=form,
            include_invoker_email=include_invoker_email,
            max_turns=max_turns,
            mcp_client_id=mcp_client_id,
            missing_scopes=missing_scopes,
            notify_failure_after_answer=notify_failure_after_answer,
            scope=scope,
            slack_team_id=slack_team_id,
            start_without_form=start_without_form,
            trigger_id=trigger_id,
            turns_anyone=turns_anyone,
            turns_enabled=turns_enabled,
            visibility=visibility,
            alias=alias,
        )

        slack_trigger_config_api_response.additional_properties = d
        return slack_trigger_config_api_response

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
