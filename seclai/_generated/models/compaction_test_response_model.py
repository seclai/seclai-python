from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.compaction_evaluation_model import CompactionEvaluationModel


T = TypeVar("T", bound="CompactionTestResponseModel")


@_attrs_define
class CompactionTestResponseModel:
    """Response from a compaction prompt test.

    Attributes:
        compaction_summary (None | str): The generated compaction summary.
        evaluation (CompactionEvaluationModel): Structured LLM-as-judge evaluation result.
        generated (bool): True when entries were LLM-generated rather than real.
        original_entries (list[str]): Entries fed into the compactor.
        surviving_entries (list[str]): Entries that survived after compaction.
    """

    compaction_summary: None | str
    evaluation: CompactionEvaluationModel
    generated: bool
    original_entries: list[str]
    surviving_entries: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compaction_summary: None | str
        compaction_summary = self.compaction_summary

        evaluation = self.evaluation.to_dict()

        generated = self.generated

        original_entries = self.original_entries

        surviving_entries = self.surviving_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compaction_summary": compaction_summary,
                "evaluation": evaluation,
                "generated": generated,
                "original_entries": original_entries,
                "surviving_entries": surviving_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compaction_evaluation_model import CompactionEvaluationModel

        d = dict(src_dict)

        def _parse_compaction_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        compaction_summary = _parse_compaction_summary(d.pop("compaction_summary"))

        evaluation = CompactionEvaluationModel.from_dict(d.pop("evaluation"))

        generated = d.pop("generated")

        original_entries = cast(list[str], d.pop("original_entries"))

        surviving_entries = cast(list[str], d.pop("surviving_entries"))

        compaction_test_response_model = cls(
            compaction_summary=compaction_summary,
            evaluation=evaluation,
            generated=generated,
            original_entries=original_entries,
            surviving_entries=surviving_entries,
        )

        compaction_test_response_model.additional_properties = d
        return compaction_test_response_model

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
