from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_skip_response_details import ImportSkipResponseDetails


T = TypeVar("T", bound="ImportSkipResponse")


@_attrs_define
class ImportSkipResponse:
    """One item that was not applied during an agent import.

    Used as the element type for ``import_warnings`` on every
    response model that accepts an ``agent_definition`` payload.
    See :py:class:`services.agent_definition_import.AgentImportSkip`
    for the full category list.

    Lives here (not on each router) so the authenticated and public
    API responses share one definition — keeping the shape that
    clients (UI modal, MCP, OpenAPI consumers) depend on aligned.

        Attributes:
            category (str): The kind of item that was skipped or substituted: 'schedule', 'evaluation_criteria',
                'alert_config', 'alert_recipient', 'governance_policy', 'governance_kb_link', 'solution_link'.
            message (str): Human-readable explanation of what was skipped and why.
            details (ImportSkipResponseDetails | Unset): Category-specific identifiers for the skipped item (step_id,
                alert_type, kb_name, etc.).  Stable keys per category; absent keys are simply not applicable.
    """

    category: str
    message: str
    details: ImportSkipResponseDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        message = self.message

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_skip_response_details import ImportSkipResponseDetails

        d = dict(src_dict)
        category = d.pop("category")

        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: ImportSkipResponseDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ImportSkipResponseDetails.from_dict(_details)

        import_skip_response = cls(
            category=category,
            message=message,
            details=details,
        )

        import_skip_response.additional_properties = d
        return import_skip_response

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
