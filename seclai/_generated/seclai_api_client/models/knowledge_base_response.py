from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_response import AccountResponse
    from ..models.source_connection_response import SourceConnectionResponse


T = TypeVar("T", bound="KnowledgeBaseResponse")


@_attrs_define
class KnowledgeBaseResponse:
    """Response model for knowledge base data

    Attributes:
        accounts (list[AccountResponse]):
        created_at (str):
        description (None | str):
        id (UUID):
        keyword_search_enabled (bool):
        knowledge_base_enabled (bool):
        mcp_server_enabled (bool):
        name (str):
        semantic_search_enabled (bool):
        sources (list[SourceConnectionResponse]):
        updated_at (str):
        readonly (bool | Unset):  Default: False.
    """

    accounts: list[AccountResponse]
    created_at: str
    description: None | str
    id: UUID
    keyword_search_enabled: bool
    knowledge_base_enabled: bool
    mcp_server_enabled: bool
    name: str
    semantic_search_enabled: bool
    sources: list[SourceConnectionResponse]
    updated_at: str
    readonly: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        created_at = self.created_at

        description: None | str
        description = self.description

        id = str(self.id)

        keyword_search_enabled = self.keyword_search_enabled

        knowledge_base_enabled = self.knowledge_base_enabled

        mcp_server_enabled = self.mcp_server_enabled

        name = self.name

        semantic_search_enabled = self.semantic_search_enabled

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        updated_at = self.updated_at

        readonly = self.readonly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "created_at": created_at,
                "description": description,
                "id": id,
                "keyword_search_enabled": keyword_search_enabled,
                "knowledge_base_enabled": knowledge_base_enabled,
                "mcp_server_enabled": mcp_server_enabled,
                "name": name,
                "semantic_search_enabled": semantic_search_enabled,
                "sources": sources,
                "updated_at": updated_at,
            }
        )
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_response import AccountResponse
        from ..models.source_connection_response import SourceConnectionResponse

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = AccountResponse.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        created_at = d.pop("created_at")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = UUID(d.pop("id"))

        keyword_search_enabled = d.pop("keyword_search_enabled")

        knowledge_base_enabled = d.pop("knowledge_base_enabled")

        mcp_server_enabled = d.pop("mcp_server_enabled")

        name = d.pop("name")

        semantic_search_enabled = d.pop("semantic_search_enabled")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceConnectionResponse.from_dict(sources_item_data)

            sources.append(sources_item)

        updated_at = d.pop("updated_at")

        readonly = d.pop("readonly", UNSET)

        knowledge_base_response = cls(
            accounts=accounts,
            created_at=created_at,
            description=description,
            id=id,
            keyword_search_enabled=keyword_search_enabled,
            knowledge_base_enabled=knowledge_base_enabled,
            mcp_server_enabled=mcp_server_enabled,
            name=name,
            semantic_search_enabled=semantic_search_enabled,
            sources=sources,
            updated_at=updated_at,
            readonly=readonly,
        )

        knowledge_base_response.additional_properties = d
        return knowledge_base_response

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
