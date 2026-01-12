from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.processing_phase_response import ProcessingPhaseResponse


T = TypeVar("T", bound="SourcePullProgressResponse")


@_attrs_define
class SourcePullProgressResponse:
    """Response model for source processing progress

    Attributes:
        failed (int | None): Total items failed
        phases (list[ProcessingPhaseResponse] | None): List of processing phases
        ratio (float | None): Overall completion ratio
        status (str): Processing status
        total (int | None): Total items being processed
    """

    failed: int | None
    phases: list[ProcessingPhaseResponse] | None
    ratio: float | None
    status: str
    total: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed: int | None
        failed = self.failed

        phases: list[dict[str, Any]] | None
        if isinstance(self.phases, list):
            phases = []
            for phases_type_0_item_data in self.phases:
                phases_type_0_item = phases_type_0_item_data.to_dict()
                phases.append(phases_type_0_item)

        else:
            phases = self.phases

        ratio: float | None
        ratio = self.ratio

        status = self.status

        total: int | None
        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failed": failed,
                "phases": phases,
                "ratio": ratio,
                "status": status,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_phase_response import ProcessingPhaseResponse

        d = dict(src_dict)

        def _parse_failed(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        failed = _parse_failed(d.pop("failed"))

        def _parse_phases(data: object) -> list[ProcessingPhaseResponse] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phases_type_0 = []
                _phases_type_0 = data
                for phases_type_0_item_data in _phases_type_0:
                    phases_type_0_item = ProcessingPhaseResponse.from_dict(phases_type_0_item_data)

                    phases_type_0.append(phases_type_0_item)

                return phases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProcessingPhaseResponse] | None, data)

        phases = _parse_phases(d.pop("phases"))

        def _parse_ratio(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        ratio = _parse_ratio(d.pop("ratio"))

        status = d.pop("status")

        def _parse_total(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total = _parse_total(d.pop("total"))

        source_pull_progress_response = cls(
            failed=failed,
            phases=phases,
            ratio=ratio,
            status=status,
            total=total,
        )

        source_pull_progress_response.additional_properties = d
        return source_pull_progress_response

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
