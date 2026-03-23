from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_cancelation_reason import SubscriptionCancelationReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitFeedbackRequest")


@_attrs_define
class SubmitFeedbackRequest:
    """
    Attributes:
        reason (SubscriptionCancelationReason): Predefined reasons for subscription cancellation
        better_service (None | str | Unset):
        comments (None | str | Unset):
        desired_content_source_type (None | str | Unset):
        other (None | str | Unset):
        use_case_missing (None | str | Unset):
        website_url (None | str | Unset):
    """

    reason: SubscriptionCancelationReason
    better_service: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    desired_content_source_type: None | str | Unset = UNSET
    other: None | str | Unset = UNSET
    use_case_missing: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        better_service: None | str | Unset
        if isinstance(self.better_service, Unset):
            better_service = UNSET
        else:
            better_service = self.better_service

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        desired_content_source_type: None | str | Unset
        if isinstance(self.desired_content_source_type, Unset):
            desired_content_source_type = UNSET
        else:
            desired_content_source_type = self.desired_content_source_type

        other: None | str | Unset
        if isinstance(self.other, Unset):
            other = UNSET
        else:
            other = self.other

        use_case_missing: None | str | Unset
        if isinstance(self.use_case_missing, Unset):
            use_case_missing = UNSET
        else:
            use_case_missing = self.use_case_missing

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if better_service is not UNSET:
            field_dict["better_service"] = better_service
        if comments is not UNSET:
            field_dict["comments"] = comments
        if desired_content_source_type is not UNSET:
            field_dict["desired_content_source_type"] = desired_content_source_type
        if other is not UNSET:
            field_dict["other"] = other
        if use_case_missing is not UNSET:
            field_dict["use_case_missing"] = use_case_missing
        if website_url is not UNSET:
            field_dict["website_url"] = website_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = SubscriptionCancelationReason(d.pop("reason"))

        def _parse_better_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        better_service = _parse_better_service(d.pop("better_service", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_desired_content_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desired_content_source_type = _parse_desired_content_source_type(
            d.pop("desired_content_source_type", UNSET)
        )

        def _parse_other(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other = _parse_other(d.pop("other", UNSET))

        def _parse_use_case_missing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_case_missing = _parse_use_case_missing(d.pop("use_case_missing", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        submit_feedback_request = cls(
            reason=reason,
            better_service=better_service,
            comments=comments,
            desired_content_source_type=desired_content_source_type,
            other=other,
            use_case_missing=use_case_missing,
            website_url=website_url,
        )

        submit_feedback_request.additional_properties = d
        return submit_feedback_request

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
