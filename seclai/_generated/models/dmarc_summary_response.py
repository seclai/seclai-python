from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dmarc_failing_source_response import DmarcFailingSourceResponse
    from ..models.dmarc_summary_response_dispositions import (
        DmarcSummaryResponseDispositions,
    )


T = TypeVar("T", bound="DmarcSummaryResponse")


@_attrs_define
class DmarcSummaryResponse:
    """
    Attributes:
        failed_messages (int):
        passed_messages (int):
        report_count (int):
        total_messages (int):
        window_days (int):
        dispositions (DmarcSummaryResponseDispositions | Unset):
        monitored (bool | Unset):  Default: True.
        pass_rate (float | None | Unset):
        top_failing_sources (list[DmarcFailingSourceResponse] | Unset):
    """

    failed_messages: int
    passed_messages: int
    report_count: int
    total_messages: int
    window_days: int
    dispositions: DmarcSummaryResponseDispositions | Unset = UNSET
    monitored: bool | Unset = True
    pass_rate: float | None | Unset = UNSET
    top_failing_sources: list[DmarcFailingSourceResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_messages = self.failed_messages

        passed_messages = self.passed_messages

        report_count = self.report_count

        total_messages = self.total_messages

        window_days = self.window_days

        dispositions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dispositions, Unset):
            dispositions = self.dispositions.to_dict()

        monitored = self.monitored

        pass_rate: float | None | Unset
        if isinstance(self.pass_rate, Unset):
            pass_rate = UNSET
        else:
            pass_rate = self.pass_rate

        top_failing_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_failing_sources, Unset):
            top_failing_sources = []
            for top_failing_sources_item_data in self.top_failing_sources:
                top_failing_sources_item = top_failing_sources_item_data.to_dict()
                top_failing_sources.append(top_failing_sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failed_messages": failed_messages,
                "passed_messages": passed_messages,
                "report_count": report_count,
                "total_messages": total_messages,
                "window_days": window_days,
            }
        )
        if dispositions is not UNSET:
            field_dict["dispositions"] = dispositions
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if pass_rate is not UNSET:
            field_dict["pass_rate"] = pass_rate
        if top_failing_sources is not UNSET:
            field_dict["top_failing_sources"] = top_failing_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dmarc_failing_source_response import DmarcFailingSourceResponse
        from ..models.dmarc_summary_response_dispositions import (
            DmarcSummaryResponseDispositions,
        )

        d = dict(src_dict)
        failed_messages = d.pop("failed_messages")

        passed_messages = d.pop("passed_messages")

        report_count = d.pop("report_count")

        total_messages = d.pop("total_messages")

        window_days = d.pop("window_days")

        _dispositions = d.pop("dispositions", UNSET)
        dispositions: DmarcSummaryResponseDispositions | Unset
        if isinstance(_dispositions, Unset):
            dispositions = UNSET
        else:
            dispositions = DmarcSummaryResponseDispositions.from_dict(_dispositions)

        monitored = d.pop("monitored", UNSET)

        def _parse_pass_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pass_rate = _parse_pass_rate(d.pop("pass_rate", UNSET))

        _top_failing_sources = d.pop("top_failing_sources", UNSET)
        top_failing_sources: list[DmarcFailingSourceResponse] | Unset = UNSET
        if _top_failing_sources is not UNSET:
            top_failing_sources = []
            for top_failing_sources_item_data in _top_failing_sources:
                top_failing_sources_item = DmarcFailingSourceResponse.from_dict(
                    top_failing_sources_item_data
                )

                top_failing_sources.append(top_failing_sources_item)

        dmarc_summary_response = cls(
            failed_messages=failed_messages,
            passed_messages=passed_messages,
            report_count=report_count,
            total_messages=total_messages,
            window_days=window_days,
            dispositions=dispositions,
            monitored=monitored,
            pass_rate=pass_rate,
            top_failing_sources=top_failing_sources,
        )

        dmarc_summary_response.additional_properties = d
        return dmarc_summary_response

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
