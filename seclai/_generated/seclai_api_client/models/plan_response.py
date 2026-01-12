from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan_response_prices import PlanResponsePrices


T = TypeVar("T", bound="PlanResponse")


@_attrs_define
class PlanResponse:
    """Response model for plan information.

    Attributes:
        api_access (bool):
        available_at (None | str):
        crawl_session_page_limit (int | None):
        default (bool):
        expires_at (None | str):
        id (str):
        max_agents (int | None):
        max_organization_members (int | None):
        max_organizations (int | None):
        monthly_credits (int):
        name (str):
        prices (PlanResponsePrices):
        support (str):
        trial_duration_days (int):
    """

    api_access: bool
    available_at: None | str
    crawl_session_page_limit: int | None
    default: bool
    expires_at: None | str
    id: str
    max_agents: int | None
    max_organization_members: int | None
    max_organizations: int | None
    monthly_credits: int
    name: str
    prices: PlanResponsePrices
    support: str
    trial_duration_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_access = self.api_access

        available_at: None | str
        available_at = self.available_at

        crawl_session_page_limit: int | None
        crawl_session_page_limit = self.crawl_session_page_limit

        default = self.default

        expires_at: None | str
        expires_at = self.expires_at

        id = self.id

        max_agents: int | None
        max_agents = self.max_agents

        max_organization_members: int | None
        max_organization_members = self.max_organization_members

        max_organizations: int | None
        max_organizations = self.max_organizations

        monthly_credits = self.monthly_credits

        name = self.name

        prices = self.prices.to_dict()

        support = self.support

        trial_duration_days = self.trial_duration_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_access": api_access,
                "available_at": available_at,
                "crawl_session_page_limit": crawl_session_page_limit,
                "default": default,
                "expires_at": expires_at,
                "id": id,
                "max_agents": max_agents,
                "max_organization_members": max_organization_members,
                "max_organizations": max_organizations,
                "monthly_credits": monthly_credits,
                "name": name,
                "prices": prices,
                "support": support,
                "trial_duration_days": trial_duration_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_response_prices import PlanResponsePrices

        d = dict(src_dict)
        api_access = d.pop("api_access")

        def _parse_available_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        available_at = _parse_available_at(d.pop("available_at"))

        def _parse_crawl_session_page_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        crawl_session_page_limit = _parse_crawl_session_page_limit(d.pop("crawl_session_page_limit"))

        default = d.pop("default")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        id = d.pop("id")

        def _parse_max_agents(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_agents = _parse_max_agents(d.pop("max_agents"))

        def _parse_max_organization_members(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_organization_members = _parse_max_organization_members(d.pop("max_organization_members"))

        def _parse_max_organizations(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_organizations = _parse_max_organizations(d.pop("max_organizations"))

        monthly_credits = d.pop("monthly_credits")

        name = d.pop("name")

        prices = PlanResponsePrices.from_dict(d.pop("prices"))

        support = d.pop("support")

        trial_duration_days = d.pop("trial_duration_days")

        plan_response = cls(
            api_access=api_access,
            available_at=available_at,
            crawl_session_page_limit=crawl_session_page_limit,
            default=default,
            expires_at=expires_at,
            id=id,
            max_agents=max_agents,
            max_organization_members=max_organization_members,
            max_organizations=max_organizations,
            monthly_credits=monthly_credits,
            name=name,
            prices=prices,
            support=support,
            trial_duration_days=trial_duration_days,
        )

        plan_response.additional_properties = d
        return plan_response

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
