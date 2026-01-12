from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKnowledgeBaseRequest")


@_attrs_define
class UpdateKnowledgeBaseRequest:
    """Request model for updating a knowledge base

    Attributes:
        description (None | str | Unset): New description for the knowledge base
        keyword_search_enabled (bool | None | Unset): Whether keyword search is enabled
        knowledge_base_enabled (bool | None | Unset): Whether the knowledge base chat functionality is enabled
        mcp_server_enabled (bool | None | Unset): Whether the MCP server functionality is enabled
        name (None | str | Unset): New name for the knowledge base
        reranker_model (None | str | Unset): Reranker model to use (empty string or null for no reranking)
        semantic_search_enabled (bool | None | Unset): Whether semantic search is enabled
        source_ids (list[UUID] | None | Unset): New list of source connection IDs to associate with the knowledge base
    """

    description: None | str | Unset = UNSET
    keyword_search_enabled: bool | None | Unset = UNSET
    knowledge_base_enabled: bool | None | Unset = UNSET
    mcp_server_enabled: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    reranker_model: None | str | Unset = UNSET
    semantic_search_enabled: bool | None | Unset = UNSET
    source_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        keyword_search_enabled: bool | None | Unset
        if isinstance(self.keyword_search_enabled, Unset):
            keyword_search_enabled = UNSET
        else:
            keyword_search_enabled = self.keyword_search_enabled

        knowledge_base_enabled: bool | None | Unset
        if isinstance(self.knowledge_base_enabled, Unset):
            knowledge_base_enabled = UNSET
        else:
            knowledge_base_enabled = self.knowledge_base_enabled

        mcp_server_enabled: bool | None | Unset
        if isinstance(self.mcp_server_enabled, Unset):
            mcp_server_enabled = UNSET
        else:
            mcp_server_enabled = self.mcp_server_enabled

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        reranker_model: None | str | Unset
        if isinstance(self.reranker_model, Unset):
            reranker_model = UNSET
        else:
            reranker_model = self.reranker_model

        semantic_search_enabled: bool | None | Unset
        if isinstance(self.semantic_search_enabled, Unset):
            semantic_search_enabled = UNSET
        else:
            semantic_search_enabled = self.semantic_search_enabled

        source_ids: list[str] | None | Unset
        if isinstance(self.source_ids, Unset):
            source_ids = UNSET
        elif isinstance(self.source_ids, list):
            source_ids = []
            for source_ids_type_0_item_data in self.source_ids:
                source_ids_type_0_item = str(source_ids_type_0_item_data)
                source_ids.append(source_ids_type_0_item)

        else:
            source_ids = self.source_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if keyword_search_enabled is not UNSET:
            field_dict["keyword_search_enabled"] = keyword_search_enabled
        if knowledge_base_enabled is not UNSET:
            field_dict["knowledge_base_enabled"] = knowledge_base_enabled
        if mcp_server_enabled is not UNSET:
            field_dict["mcp_server_enabled"] = mcp_server_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model
        if semantic_search_enabled is not UNSET:
            field_dict["semantic_search_enabled"] = semantic_search_enabled
        if source_ids is not UNSET:
            field_dict["source_ids"] = source_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_keyword_search_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keyword_search_enabled = _parse_keyword_search_enabled(
            d.pop("keyword_search_enabled", UNSET)
        )

        def _parse_knowledge_base_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        knowledge_base_enabled = _parse_knowledge_base_enabled(
            d.pop("knowledge_base_enabled", UNSET)
        )

        def _parse_mcp_server_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mcp_server_enabled = _parse_mcp_server_enabled(
            d.pop("mcp_server_enabled", UNSET)
        )

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_reranker_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reranker_model = _parse_reranker_model(d.pop("reranker_model", UNSET))

        def _parse_semantic_search_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        semantic_search_enabled = _parse_semantic_search_enabled(
            d.pop("semantic_search_enabled", UNSET)
        )

        def _parse_source_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_ids_type_0 = []
                _source_ids_type_0 = data
                for source_ids_type_0_item_data in _source_ids_type_0:
                    source_ids_type_0_item = UUID(source_ids_type_0_item_data)

                    source_ids_type_0.append(source_ids_type_0_item)

                return source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        source_ids = _parse_source_ids(d.pop("source_ids", UNSET))

        update_knowledge_base_request = cls(
            description=description,
            keyword_search_enabled=keyword_search_enabled,
            knowledge_base_enabled=knowledge_base_enabled,
            mcp_server_enabled=mcp_server_enabled,
            name=name,
            reranker_model=reranker_model,
            semantic_search_enabled=semantic_search_enabled,
            source_ids=source_ids,
        )

        update_knowledge_base_request.additional_properties = d
        return update_knowledge_base_request

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
