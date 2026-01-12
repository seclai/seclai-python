from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_size import CompanySize
from ..models.use_case_type import UseCaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnboardingRequest")


@_attrs_define
class OnboardingRequest:
    """Request model for completing onboarding.

    Attributes:
        account_type (str): The account type the user selected to start with
        first_name (str): User's first name
        last_name (str): User's last name
        company_size (CompanySize | None | Unset): Size of the user's company
        other_use_case (None | str | Unset): Other use case if 'Other' is selected
        use_cases (list[UseCaseType] | None | Unset): List of primary use cases for the user
    """

    account_type: str
    first_name: str
    last_name: str
    company_size: CompanySize | None | Unset = UNSET
    other_use_case: None | str | Unset = UNSET
    use_cases: list[UseCaseType] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type = self.account_type

        first_name = self.first_name

        last_name = self.last_name

        company_size: None | str | Unset
        if isinstance(self.company_size, Unset):
            company_size = UNSET
        elif isinstance(self.company_size, CompanySize):
            company_size = self.company_size.value
        else:
            company_size = self.company_size

        other_use_case: None | str | Unset
        if isinstance(self.other_use_case, Unset):
            other_use_case = UNSET
        else:
            other_use_case = self.other_use_case

        use_cases: list[str] | None | Unset
        if isinstance(self.use_cases, Unset):
            use_cases = UNSET
        elif isinstance(self.use_cases, list):
            use_cases = []
            for use_cases_type_0_item_data in self.use_cases:
                use_cases_type_0_item = use_cases_type_0_item_data.value
                use_cases.append(use_cases_type_0_item)

        else:
            use_cases = self.use_cases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_type": account_type,
                "first_name": first_name,
                "last_name": last_name,
            }
        )
        if company_size is not UNSET:
            field_dict["company_size"] = company_size
        if other_use_case is not UNSET:
            field_dict["other_use_case"] = other_use_case
        if use_cases is not UNSET:
            field_dict["use_cases"] = use_cases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_type = d.pop("account_type")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        def _parse_company_size(data: object) -> CompanySize | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_size_type_0 = CompanySize(data)

                return company_size_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanySize | None | Unset, data)

        company_size = _parse_company_size(d.pop("company_size", UNSET))

        def _parse_other_use_case(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_use_case = _parse_other_use_case(d.pop("other_use_case", UNSET))

        def _parse_use_cases(data: object) -> list[UseCaseType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                use_cases_type_0 = []
                _use_cases_type_0 = data
                for use_cases_type_0_item_data in _use_cases_type_0:
                    use_cases_type_0_item = UseCaseType(use_cases_type_0_item_data)

                    use_cases_type_0.append(use_cases_type_0_item)

                return use_cases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UseCaseType] | None | Unset, data)

        use_cases = _parse_use_cases(d.pop("use_cases", UNSET))

        onboarding_request = cls(
            account_type=account_type,
            first_name=first_name,
            last_name=last_name,
            company_size=company_size,
            other_use_case=other_use_case,
            use_cases=use_cases,
        )

        onboarding_request.additional_properties = d
        return onboarding_request

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
