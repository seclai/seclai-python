from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExperimentSummaryResponse")


@_attrs_define
class ExperimentSummaryResponse:
    """
    Attributes:
        created_at (str):
        evaluation_complexity (str):
        evaluation_mode (str):
        id (str):
        selected_model_ids (list[str]):
        status (str):
    """

    created_at: str
    evaluation_complexity: str
    evaluation_mode: str
    id: str
    selected_model_ids: list[str]
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        evaluation_complexity = self.evaluation_complexity

        evaluation_mode = self.evaluation_mode

        id = self.id

        selected_model_ids = self.selected_model_ids

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "evaluation_complexity": evaluation_complexity,
                "evaluation_mode": evaluation_mode,
                "id": id,
                "selected_model_ids": selected_model_ids,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        evaluation_complexity = d.pop("evaluation_complexity")

        evaluation_mode = d.pop("evaluation_mode")

        id = d.pop("id")

        selected_model_ids = cast(list[str], d.pop("selected_model_ids"))

        status = d.pop("status")

        experiment_summary_response = cls(
            created_at=created_at,
            evaluation_complexity=evaluation_complexity,
            evaluation_mode=evaluation_mode,
            id=id,
            selected_model_ids=selected_model_ids,
            status=status,
        )

        experiment_summary_response.additional_properties = d
        return experiment_summary_response

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
