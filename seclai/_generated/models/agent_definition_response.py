from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_definition_response_definition import (
        AgentDefinitionResponseDefinition,
    )
    from ..models.agent_definition_response_warnings_type_0_item import (
        AgentDefinitionResponseWarningsType0Item,
    )


T = TypeVar("T", bound="AgentDefinitionResponse")


@_attrs_define
class AgentDefinitionResponse:
    """
    Attributes:
        change_id (str): Current change ID (use as expected_change_id when updating).
        definition (AgentDefinitionResponseDefinition): The agent definition containing name, description, tags, and
            step workflow tree. Step types include prompt_call, retrieval, regex_replace, gate, retry, evaluate_step,
            extract_data, extract_content, add_chat_turn, load_chat_history, add_memory, search_memory, load_memory,
            streaming_result, send_email, webhook_call, call_agent, write_metadata, write_content_attachment,
            load_content_attachment, load_content, display_result, merge, for_each, and others.
        schema_version (str): Agent schema version.
        warnings (list[AgentDefinitionResponseWarningsType0Item] | None | Unset): Validation warnings, if any.
    """

    change_id: str
    definition: AgentDefinitionResponseDefinition
    schema_version: str
    warnings: list[AgentDefinitionResponseWarningsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = self.change_id

        definition = self.definition.to_dict()

        schema_version = self.schema_version

        warnings: list[dict[str, Any]] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "change_id": change_id,
                "definition": definition,
                "schema_version": schema_version,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_definition_response_definition import (
            AgentDefinitionResponseDefinition,
        )
        from ..models.agent_definition_response_warnings_type_0_item import (
            AgentDefinitionResponseWarningsType0Item,
        )

        d = dict(src_dict)
        change_id = d.pop("change_id")

        definition = AgentDefinitionResponseDefinition.from_dict(d.pop("definition"))

        schema_version = d.pop("schema_version")

        def _parse_warnings(
            data: object,
        ) -> list[AgentDefinitionResponseWarningsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in _warnings_type_0:
                    warnings_type_0_item = (
                        AgentDefinitionResponseWarningsType0Item.from_dict(
                            warnings_type_0_item_data
                        )
                    )

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AgentDefinitionResponseWarningsType0Item] | None | Unset, data
            )

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        agent_definition_response = cls(
            change_id=change_id,
            definition=definition,
            schema_version=schema_version,
            warnings=warnings,
        )

        agent_definition_response.additional_properties = d
        return agent_definition_response

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
