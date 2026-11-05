from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slack_reply_visibility import SlackReplyVisibility
from ..models.slack_trigger_activation import SlackTriggerActivation
from ..models.slack_trigger_scope import SlackTriggerScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_slack_trigger_config_api_request_form_type_0_item import (
        SetSlackTriggerConfigApiRequestFormType0Item,
    )


T = TypeVar("T", bound="SetSlackTriggerConfigApiRequest")


@_attrs_define
class SetSlackTriggerConfigApiRequest:
    """Omitted fields are left unchanged.

    Attributes:
        activation (None | SlackTriggerActivation | Unset): `everywhere` in scope, or `channel_opt_in`.
        alias (None | str | Unset): The name people type after `/seclai` to run this agent: lowercase letters, digits
            and hyphens, starting with a letter, unique in the Slack workspace. Generated from the agent's name when not set
            or empty.
        allow_dms (bool | None | Unset): Runnable in the app's own DMs.
        channel_ids (list[str] | None | Unset):
        form (list[SetSlackTriggerConfigApiRequestFormType0Item] | None | Unset): Form fields `{key, label, type,
            required, hint, choices, max_length}`. `type`: short_text, long_text, number, single_choice, multi_choice,
            yes_no, date, slack_user or slack_channel. Each value reaches the run as `{{metadata.<key>}}`, not in the run's
            input, which is the text after `/seclai <alias>` or the message the shortcut was used on, and its files.
        include_invoker_email (bool | None | Unset):
        max_turns (int | None | Unset):
        mcp_client_id (None | Unset | UUID): The account's connected Slack (Bot) MCP client.
        notify_failure_after_answer (bool | None | Unset):
        scope (None | SlackTriggerScope | Unset): `selected_channels` (see `channel_ids`) or `bot_channels`.
        start_without_form (bool | None | Unset):
        turns_anyone (bool | None | Unset):
        turns_enabled (bool | None | Unset):
        visibility (None | SlackReplyVisibility | Unset): `channel`, or `private` (replies in the person's DM).
    """

    activation: None | SlackTriggerActivation | Unset = UNSET
    alias: None | str | Unset = UNSET
    allow_dms: bool | None | Unset = UNSET
    channel_ids: list[str] | None | Unset = UNSET
    form: list[SetSlackTriggerConfigApiRequestFormType0Item] | None | Unset = UNSET
    include_invoker_email: bool | None | Unset = UNSET
    max_turns: int | None | Unset = UNSET
    mcp_client_id: None | Unset | UUID = UNSET
    notify_failure_after_answer: bool | None | Unset = UNSET
    scope: None | SlackTriggerScope | Unset = UNSET
    start_without_form: bool | None | Unset = UNSET
    turns_anyone: bool | None | Unset = UNSET
    turns_enabled: bool | None | Unset = UNSET
    visibility: None | SlackReplyVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activation: None | str | Unset
        if isinstance(self.activation, Unset):
            activation = UNSET
        elif isinstance(self.activation, SlackTriggerActivation):
            activation = self.activation.value
        else:
            activation = self.activation

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        allow_dms: bool | None | Unset
        if isinstance(self.allow_dms, Unset):
            allow_dms = UNSET
        else:
            allow_dms = self.allow_dms

        channel_ids: list[str] | None | Unset
        if isinstance(self.channel_ids, Unset):
            channel_ids = UNSET
        elif isinstance(self.channel_ids, list):
            channel_ids = self.channel_ids

        else:
            channel_ids = self.channel_ids

        form: list[dict[str, Any]] | None | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        elif isinstance(self.form, list):
            form = []
            for form_type_0_item_data in self.form:
                form_type_0_item = form_type_0_item_data.to_dict()
                form.append(form_type_0_item)

        else:
            form = self.form

        include_invoker_email: bool | None | Unset
        if isinstance(self.include_invoker_email, Unset):
            include_invoker_email = UNSET
        else:
            include_invoker_email = self.include_invoker_email

        max_turns: int | None | Unset
        if isinstance(self.max_turns, Unset):
            max_turns = UNSET
        else:
            max_turns = self.max_turns

        mcp_client_id: None | str | Unset
        if isinstance(self.mcp_client_id, Unset):
            mcp_client_id = UNSET
        elif isinstance(self.mcp_client_id, UUID):
            mcp_client_id = str(self.mcp_client_id)
        else:
            mcp_client_id = self.mcp_client_id

        notify_failure_after_answer: bool | None | Unset
        if isinstance(self.notify_failure_after_answer, Unset):
            notify_failure_after_answer = UNSET
        else:
            notify_failure_after_answer = self.notify_failure_after_answer

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, SlackTriggerScope):
            scope = self.scope.value
        else:
            scope = self.scope

        start_without_form: bool | None | Unset
        if isinstance(self.start_without_form, Unset):
            start_without_form = UNSET
        else:
            start_without_form = self.start_without_form

        turns_anyone: bool | None | Unset
        if isinstance(self.turns_anyone, Unset):
            turns_anyone = UNSET
        else:
            turns_anyone = self.turns_anyone

        turns_enabled: bool | None | Unset
        if isinstance(self.turns_enabled, Unset):
            turns_enabled = UNSET
        else:
            turns_enabled = self.turns_enabled

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        elif isinstance(self.visibility, SlackReplyVisibility):
            visibility = self.visibility.value
        else:
            visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activation is not UNSET:
            field_dict["activation"] = activation
        if alias is not UNSET:
            field_dict["alias"] = alias
        if allow_dms is not UNSET:
            field_dict["allow_dms"] = allow_dms
        if channel_ids is not UNSET:
            field_dict["channel_ids"] = channel_ids
        if form is not UNSET:
            field_dict["form"] = form
        if include_invoker_email is not UNSET:
            field_dict["include_invoker_email"] = include_invoker_email
        if max_turns is not UNSET:
            field_dict["max_turns"] = max_turns
        if mcp_client_id is not UNSET:
            field_dict["mcp_client_id"] = mcp_client_id
        if notify_failure_after_answer is not UNSET:
            field_dict["notify_failure_after_answer"] = notify_failure_after_answer
        if scope is not UNSET:
            field_dict["scope"] = scope
        if start_without_form is not UNSET:
            field_dict["start_without_form"] = start_without_form
        if turns_anyone is not UNSET:
            field_dict["turns_anyone"] = turns_anyone
        if turns_enabled is not UNSET:
            field_dict["turns_enabled"] = turns_enabled
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_slack_trigger_config_api_request_form_type_0_item import (
            SetSlackTriggerConfigApiRequestFormType0Item,
        )

        d = dict(src_dict)

        def _parse_activation(data: object) -> None | SlackTriggerActivation | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_type_0 = SlackTriggerActivation(data)

                return activation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlackTriggerActivation | Unset, data)

        activation = _parse_activation(d.pop("activation", UNSET))

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_allow_dms(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_dms = _parse_allow_dms(d.pop("allow_dms", UNSET))

        def _parse_channel_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channel_ids_type_0 = cast(list[str], data)

                return channel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        channel_ids = _parse_channel_ids(d.pop("channel_ids", UNSET))

        def _parse_form(
            data: object,
        ) -> list[SetSlackTriggerConfigApiRequestFormType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                form_type_0 = []
                _form_type_0 = data
                for form_type_0_item_data in _form_type_0:
                    form_type_0_item = (
                        SetSlackTriggerConfigApiRequestFormType0Item.from_dict(
                            form_type_0_item_data
                        )
                    )

                    form_type_0.append(form_type_0_item)

                return form_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SetSlackTriggerConfigApiRequestFormType0Item] | None | Unset, data
            )

        form = _parse_form(d.pop("form", UNSET))

        def _parse_include_invoker_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_invoker_email = _parse_include_invoker_email(
            d.pop("include_invoker_email", UNSET)
        )

        def _parse_max_turns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_turns = _parse_max_turns(d.pop("max_turns", UNSET))

        def _parse_mcp_client_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mcp_client_id_type_0 = UUID(data)

                return mcp_client_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        mcp_client_id = _parse_mcp_client_id(d.pop("mcp_client_id", UNSET))

        def _parse_notify_failure_after_answer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_failure_after_answer = _parse_notify_failure_after_answer(
            d.pop("notify_failure_after_answer", UNSET)
        )

        def _parse_scope(data: object) -> None | SlackTriggerScope | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scope_type_0 = SlackTriggerScope(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlackTriggerScope | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_start_without_form(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        start_without_form = _parse_start_without_form(
            d.pop("start_without_form", UNSET)
        )

        def _parse_turns_anyone(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        turns_anyone = _parse_turns_anyone(d.pop("turns_anyone", UNSET))

        def _parse_turns_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        turns_enabled = _parse_turns_enabled(d.pop("turns_enabled", UNSET))

        def _parse_visibility(data: object) -> None | SlackReplyVisibility | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visibility_type_0 = SlackReplyVisibility(data)

                return visibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlackReplyVisibility | Unset, data)

        visibility = _parse_visibility(d.pop("visibility", UNSET))

        set_slack_trigger_config_api_request = cls(
            activation=activation,
            alias=alias,
            allow_dms=allow_dms,
            channel_ids=channel_ids,
            form=form,
            include_invoker_email=include_invoker_email,
            max_turns=max_turns,
            mcp_client_id=mcp_client_id,
            notify_failure_after_answer=notify_failure_after_answer,
            scope=scope,
            start_without_form=start_without_form,
            turns_anyone=turns_anyone,
            turns_enabled=turns_enabled,
            visibility=visibility,
        )

        set_slack_trigger_config_api_request.additional_properties = d
        return set_slack_trigger_config_api_request

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
