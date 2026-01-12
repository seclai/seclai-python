from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.related_account_response import RelatedAccountResponse


T = TypeVar("T", bound="AccountDetailsResponse")


@_attrs_define
class AccountDetailsResponse:
    """
    Attributes:
        account_credits (int | None | Unset):
        accounts (list[RelatedAccountResponse] | Unset):
        auto_purchase_overages (bool | None | Unset):
        days_until_content_deletion (int | None | Unset):
        id (None | str | Unset):
        knowledge_bases (int | None | Unset):
        name (None | str | Unset):
        pending_plan_monthly_credits (int | None | Unset):
        pending_plan_name (None | str | Unset):
        pending_subscription_start_date (None | str | Unset):
        plan_agent_version_control (bool | None | Unset):
        plan_api_access (bool | None | Unset):
        plan_crawl_session_page_limit (int | None | Unset):
        plan_max_agents (int | None | Unset):
        plan_max_organization_members (int | None | Unset):
        plan_max_organizations (int | None | Unset):
        plan_monthly_credits (int | None | Unset):
        plan_name (None | str | Unset):
        plan_support (None | str | Unset):
        readonly (bool | Unset):  Default: False.
        sources (int | None | Unset):
        status (None | str | Unset):
        subscription_period_credits (int | None | Unset):
        subscription_period_end (None | str | Unset):
        subscription_period_initial_credits (int | None | Unset):
        subscription_period_start (None | str | Unset):
        trial_days_available (int | None | Unset):
    """

    account_credits: int | None | Unset = UNSET
    accounts: list[RelatedAccountResponse] | Unset = UNSET
    auto_purchase_overages: bool | None | Unset = UNSET
    days_until_content_deletion: int | None | Unset = UNSET
    id: None | str | Unset = UNSET
    knowledge_bases: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    pending_plan_monthly_credits: int | None | Unset = UNSET
    pending_plan_name: None | str | Unset = UNSET
    pending_subscription_start_date: None | str | Unset = UNSET
    plan_agent_version_control: bool | None | Unset = UNSET
    plan_api_access: bool | None | Unset = UNSET
    plan_crawl_session_page_limit: int | None | Unset = UNSET
    plan_max_agents: int | None | Unset = UNSET
    plan_max_organization_members: int | None | Unset = UNSET
    plan_max_organizations: int | None | Unset = UNSET
    plan_monthly_credits: int | None | Unset = UNSET
    plan_name: None | str | Unset = UNSET
    plan_support: None | str | Unset = UNSET
    readonly: bool | Unset = False
    sources: int | None | Unset = UNSET
    status: None | str | Unset = UNSET
    subscription_period_credits: int | None | Unset = UNSET
    subscription_period_end: None | str | Unset = UNSET
    subscription_period_initial_credits: int | None | Unset = UNSET
    subscription_period_start: None | str | Unset = UNSET
    trial_days_available: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_credits: int | None | Unset
        if isinstance(self.account_credits, Unset):
            account_credits = UNSET
        else:
            account_credits = self.account_credits

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        auto_purchase_overages: bool | None | Unset
        if isinstance(self.auto_purchase_overages, Unset):
            auto_purchase_overages = UNSET
        else:
            auto_purchase_overages = self.auto_purchase_overages

        days_until_content_deletion: int | None | Unset
        if isinstance(self.days_until_content_deletion, Unset):
            days_until_content_deletion = UNSET
        else:
            days_until_content_deletion = self.days_until_content_deletion

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        knowledge_bases: int | None | Unset
        if isinstance(self.knowledge_bases, Unset):
            knowledge_bases = UNSET
        else:
            knowledge_bases = self.knowledge_bases

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pending_plan_monthly_credits: int | None | Unset
        if isinstance(self.pending_plan_monthly_credits, Unset):
            pending_plan_monthly_credits = UNSET
        else:
            pending_plan_monthly_credits = self.pending_plan_monthly_credits

        pending_plan_name: None | str | Unset
        if isinstance(self.pending_plan_name, Unset):
            pending_plan_name = UNSET
        else:
            pending_plan_name = self.pending_plan_name

        pending_subscription_start_date: None | str | Unset
        if isinstance(self.pending_subscription_start_date, Unset):
            pending_subscription_start_date = UNSET
        else:
            pending_subscription_start_date = self.pending_subscription_start_date

        plan_agent_version_control: bool | None | Unset
        if isinstance(self.plan_agent_version_control, Unset):
            plan_agent_version_control = UNSET
        else:
            plan_agent_version_control = self.plan_agent_version_control

        plan_api_access: bool | None | Unset
        if isinstance(self.plan_api_access, Unset):
            plan_api_access = UNSET
        else:
            plan_api_access = self.plan_api_access

        plan_crawl_session_page_limit: int | None | Unset
        if isinstance(self.plan_crawl_session_page_limit, Unset):
            plan_crawl_session_page_limit = UNSET
        else:
            plan_crawl_session_page_limit = self.plan_crawl_session_page_limit

        plan_max_agents: int | None | Unset
        if isinstance(self.plan_max_agents, Unset):
            plan_max_agents = UNSET
        else:
            plan_max_agents = self.plan_max_agents

        plan_max_organization_members: int | None | Unset
        if isinstance(self.plan_max_organization_members, Unset):
            plan_max_organization_members = UNSET
        else:
            plan_max_organization_members = self.plan_max_organization_members

        plan_max_organizations: int | None | Unset
        if isinstance(self.plan_max_organizations, Unset):
            plan_max_organizations = UNSET
        else:
            plan_max_organizations = self.plan_max_organizations

        plan_monthly_credits: int | None | Unset
        if isinstance(self.plan_monthly_credits, Unset):
            plan_monthly_credits = UNSET
        else:
            plan_monthly_credits = self.plan_monthly_credits

        plan_name: None | str | Unset
        if isinstance(self.plan_name, Unset):
            plan_name = UNSET
        else:
            plan_name = self.plan_name

        plan_support: None | str | Unset
        if isinstance(self.plan_support, Unset):
            plan_support = UNSET
        else:
            plan_support = self.plan_support

        readonly = self.readonly

        sources: int | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        else:
            sources = self.sources

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        subscription_period_credits: int | None | Unset
        if isinstance(self.subscription_period_credits, Unset):
            subscription_period_credits = UNSET
        else:
            subscription_period_credits = self.subscription_period_credits

        subscription_period_end: None | str | Unset
        if isinstance(self.subscription_period_end, Unset):
            subscription_period_end = UNSET
        else:
            subscription_period_end = self.subscription_period_end

        subscription_period_initial_credits: int | None | Unset
        if isinstance(self.subscription_period_initial_credits, Unset):
            subscription_period_initial_credits = UNSET
        else:
            subscription_period_initial_credits = self.subscription_period_initial_credits

        subscription_period_start: None | str | Unset
        if isinstance(self.subscription_period_start, Unset):
            subscription_period_start = UNSET
        else:
            subscription_period_start = self.subscription_period_start

        trial_days_available: int | None | Unset
        if isinstance(self.trial_days_available, Unset):
            trial_days_available = UNSET
        else:
            trial_days_available = self.trial_days_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_credits is not UNSET:
            field_dict["account_credits"] = account_credits
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if auto_purchase_overages is not UNSET:
            field_dict["auto_purchase_overages"] = auto_purchase_overages
        if days_until_content_deletion is not UNSET:
            field_dict["days_until_content_deletion"] = days_until_content_deletion
        if id is not UNSET:
            field_dict["id"] = id
        if knowledge_bases is not UNSET:
            field_dict["knowledge_bases"] = knowledge_bases
        if name is not UNSET:
            field_dict["name"] = name
        if pending_plan_monthly_credits is not UNSET:
            field_dict["pending_plan_monthly_credits"] = pending_plan_monthly_credits
        if pending_plan_name is not UNSET:
            field_dict["pending_plan_name"] = pending_plan_name
        if pending_subscription_start_date is not UNSET:
            field_dict["pending_subscription_start_date"] = pending_subscription_start_date
        if plan_agent_version_control is not UNSET:
            field_dict["plan_agent_version_control"] = plan_agent_version_control
        if plan_api_access is not UNSET:
            field_dict["plan_api_access"] = plan_api_access
        if plan_crawl_session_page_limit is not UNSET:
            field_dict["plan_crawl_session_page_limit"] = plan_crawl_session_page_limit
        if plan_max_agents is not UNSET:
            field_dict["plan_max_agents"] = plan_max_agents
        if plan_max_organization_members is not UNSET:
            field_dict["plan_max_organization_members"] = plan_max_organization_members
        if plan_max_organizations is not UNSET:
            field_dict["plan_max_organizations"] = plan_max_organizations
        if plan_monthly_credits is not UNSET:
            field_dict["plan_monthly_credits"] = plan_monthly_credits
        if plan_name is not UNSET:
            field_dict["plan_name"] = plan_name
        if plan_support is not UNSET:
            field_dict["plan_support"] = plan_support
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if sources is not UNSET:
            field_dict["sources"] = sources
        if status is not UNSET:
            field_dict["status"] = status
        if subscription_period_credits is not UNSET:
            field_dict["subscription_period_credits"] = subscription_period_credits
        if subscription_period_end is not UNSET:
            field_dict["subscription_period_end"] = subscription_period_end
        if subscription_period_initial_credits is not UNSET:
            field_dict["subscription_period_initial_credits"] = subscription_period_initial_credits
        if subscription_period_start is not UNSET:
            field_dict["subscription_period_start"] = subscription_period_start
        if trial_days_available is not UNSET:
            field_dict["trial_days_available"] = trial_days_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_account_response import RelatedAccountResponse

        d = dict(src_dict)

        def _parse_account_credits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_credits = _parse_account_credits(d.pop("account_credits", UNSET))

        _accounts = d.pop("accounts", UNSET)
        accounts: list[RelatedAccountResponse] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = RelatedAccountResponse.from_dict(accounts_item_data)

                accounts.append(accounts_item)

        def _parse_auto_purchase_overages(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_purchase_overages = _parse_auto_purchase_overages(d.pop("auto_purchase_overages", UNSET))

        def _parse_days_until_content_deletion(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_until_content_deletion = _parse_days_until_content_deletion(d.pop("days_until_content_deletion", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_knowledge_bases(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        knowledge_bases = _parse_knowledge_bases(d.pop("knowledge_bases", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_pending_plan_monthly_credits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pending_plan_monthly_credits = _parse_pending_plan_monthly_credits(d.pop("pending_plan_monthly_credits", UNSET))

        def _parse_pending_plan_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pending_plan_name = _parse_pending_plan_name(d.pop("pending_plan_name", UNSET))

        def _parse_pending_subscription_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pending_subscription_start_date = _parse_pending_subscription_start_date(
            d.pop("pending_subscription_start_date", UNSET)
        )

        def _parse_plan_agent_version_control(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        plan_agent_version_control = _parse_plan_agent_version_control(d.pop("plan_agent_version_control", UNSET))

        def _parse_plan_api_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        plan_api_access = _parse_plan_api_access(d.pop("plan_api_access", UNSET))

        def _parse_plan_crawl_session_page_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_crawl_session_page_limit = _parse_plan_crawl_session_page_limit(
            d.pop("plan_crawl_session_page_limit", UNSET)
        )

        def _parse_plan_max_agents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_max_agents = _parse_plan_max_agents(d.pop("plan_max_agents", UNSET))

        def _parse_plan_max_organization_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_max_organization_members = _parse_plan_max_organization_members(
            d.pop("plan_max_organization_members", UNSET)
        )

        def _parse_plan_max_organizations(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_max_organizations = _parse_plan_max_organizations(d.pop("plan_max_organizations", UNSET))

        def _parse_plan_monthly_credits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_monthly_credits = _parse_plan_monthly_credits(d.pop("plan_monthly_credits", UNSET))

        def _parse_plan_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_name = _parse_plan_name(d.pop("plan_name", UNSET))

        def _parse_plan_support(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_support = _parse_plan_support(d.pop("plan_support", UNSET))

        readonly = d.pop("readonly", UNSET)

        def _parse_sources(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_subscription_period_credits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subscription_period_credits = _parse_subscription_period_credits(d.pop("subscription_period_credits", UNSET))

        def _parse_subscription_period_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_period_end = _parse_subscription_period_end(d.pop("subscription_period_end", UNSET))

        def _parse_subscription_period_initial_credits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subscription_period_initial_credits = _parse_subscription_period_initial_credits(
            d.pop("subscription_period_initial_credits", UNSET)
        )

        def _parse_subscription_period_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_period_start = _parse_subscription_period_start(d.pop("subscription_period_start", UNSET))

        def _parse_trial_days_available(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        trial_days_available = _parse_trial_days_available(d.pop("trial_days_available", UNSET))

        account_details_response = cls(
            account_credits=account_credits,
            accounts=accounts,
            auto_purchase_overages=auto_purchase_overages,
            days_until_content_deletion=days_until_content_deletion,
            id=id,
            knowledge_bases=knowledge_bases,
            name=name,
            pending_plan_monthly_credits=pending_plan_monthly_credits,
            pending_plan_name=pending_plan_name,
            pending_subscription_start_date=pending_subscription_start_date,
            plan_agent_version_control=plan_agent_version_control,
            plan_api_access=plan_api_access,
            plan_crawl_session_page_limit=plan_crawl_session_page_limit,
            plan_max_agents=plan_max_agents,
            plan_max_organization_members=plan_max_organization_members,
            plan_max_organizations=plan_max_organizations,
            plan_monthly_credits=plan_monthly_credits,
            plan_name=plan_name,
            plan_support=plan_support,
            readonly=readonly,
            sources=sources,
            status=status,
            subscription_period_credits=subscription_period_credits,
            subscription_period_end=subscription_period_end,
            subscription_period_initial_credits=subscription_period_initial_credits,
            subscription_period_start=subscription_period_start,
            trial_days_available=trial_days_available,
        )

        account_details_response.additional_properties = d
        return account_details_response

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
