from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompactionEvaluationModel")


@_attrs_define
class CompactionEvaluationModel:
    """Structured LLM-as-judge evaluation result.

    Attributes:
        reasoning (str): Explanation of the evaluation.
        score (int): Quality score from 1 to 5.
        verdict (str): 'pass' or 'fail'.
    """

    reasoning: str
    score: int
    verdict: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reasoning = self.reasoning

        score = self.score

        verdict = self.verdict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reasoning": reasoning,
                "score": score,
                "verdict": verdict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reasoning = d.pop("reasoning")

        score = d.pop("score")

        verdict = d.pop("verdict")

        compaction_evaluation_model = cls(
            reasoning=reasoning,
            score=score,
            verdict=verdict,
        )

        compaction_evaluation_model.additional_properties = d
        return compaction_evaluation_model

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
