from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.substitution_dependencies import SubstitutionDependencies


T = TypeVar("T", bound="AnalyzeSubstitutionsResponse")


@_attrs_define
class AnalyzeSubstitutionsResponse:
    """Response with analyzed substitution dependencies.

    Attributes:
        dependencies (SubstitutionDependencies): Dependencies found in templates.
    """

    dependencies: SubstitutionDependencies
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dependencies = self.dependencies.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dependencies": dependencies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.substitution_dependencies import SubstitutionDependencies

        d = dict(src_dict)
        dependencies = SubstitutionDependencies.from_dict(d.pop("dependencies"))

        analyze_substitutions_response = cls(
            dependencies=dependencies,
        )

        analyze_substitutions_response.additional_properties = d
        return analyze_substitutions_response

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
