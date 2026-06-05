from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_field_error_model import ImportFieldErrorModel


T = TypeVar("T", bound="AgentDefinitionImportErrorResponse")


@_attrs_define
class AgentDefinitionImportErrorResponse:
    """422 body for invalid `agent_definition` payloads.

    Mirrors `AgentDefinitionImportError.to_response_dict`.

        Attributes:
            error (Literal['invalid_agent_definition']): Stable machine-readable error code.
            errors (list[ImportFieldErrorModel]):
            message (str):
            source (str): Canonical pretty-printed echo of the supplied payload — error line/column refer to this string.
    """

    error: Literal["invalid_agent_definition"]
    errors: list[ImportFieldErrorModel]
    message: str
    source: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        message = self.message

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "errors": errors,
                "message": message,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_field_error_model import ImportFieldErrorModel

        d = dict(src_dict)
        error = cast(Literal["invalid_agent_definition"], d.pop("error"))
        if error != "invalid_agent_definition":
            raise ValueError(
                f"error must match const 'invalid_agent_definition', got '{error}'"
            )

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = ImportFieldErrorModel.from_dict(errors_item_data)

            errors.append(errors_item)

        message = d.pop("message")

        source = d.pop("source")

        agent_definition_import_error_response = cls(
            error=error,
            errors=errors,
            message=message,
            source=source,
        )

        agent_definition_import_error_response.additional_properties = d
        return agent_definition_import_error_response

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
