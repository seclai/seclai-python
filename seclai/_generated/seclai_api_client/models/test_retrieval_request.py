from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_retrieval_request_metadata_filter_type_0 import TestRetrievalRequestMetadataFilterType0


T = TypeVar("T", bound="TestRetrievalRequest")


@_attrs_define
class TestRetrievalRequest:
    """Request to test retrieval step.

    Attributes:
        knowledge_base_id (UUID): The knowledge base ID to retrieve content from
        query (str): The query string for retrieval
        added_after (None | str | Unset): Optional ISO 8601 datetime string for added_after filter
        added_before (None | str | Unset): Optional ISO 8601 datetime string for added_before filter
        agent_id (None | Unset | UUID): Optional agent id to attribute the retrieval test usage to. If provided, usage
            is linked via agent_usages so it appears in the agent usage report.
        content_type (str | Unset): Output content type (text/html, application/json, text/plain, application/xml)
            Default: 'text/xml'.
        metadata_filter (None | TestRetrievalRequestMetadataFilterType0 | Unset): Optional metadata filter
        reranker_model (None | str | Unset): Optional reranker model
        top_k (int | None | Unset): Number of results after reranking
        top_n (int | Unset): Number of results to retrieve Default: 20.
    """

    knowledge_base_id: UUID
    query: str
    added_after: None | str | Unset = UNSET
    added_before: None | str | Unset = UNSET
    agent_id: None | Unset | UUID = UNSET
    content_type: str | Unset = "text/xml"
    metadata_filter: None | TestRetrievalRequestMetadataFilterType0 | Unset = UNSET
    reranker_model: None | str | Unset = UNSET
    top_k: int | None | Unset = UNSET
    top_n: int | Unset = 20
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_retrieval_request_metadata_filter_type_0 import TestRetrievalRequestMetadataFilterType0

        knowledge_base_id = str(self.knowledge_base_id)

        query = self.query

        added_after: None | str | Unset
        if isinstance(self.added_after, Unset):
            added_after = UNSET
        else:
            added_after = self.added_after

        added_before: None | str | Unset
        if isinstance(self.added_before, Unset):
            added_before = UNSET
        else:
            added_before = self.added_before

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        elif isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        content_type = self.content_type

        metadata_filter: dict[str, Any] | None | Unset
        if isinstance(self.metadata_filter, Unset):
            metadata_filter = UNSET
        elif isinstance(self.metadata_filter, TestRetrievalRequestMetadataFilterType0):
            metadata_filter = self.metadata_filter.to_dict()
        else:
            metadata_filter = self.metadata_filter

        reranker_model: None | str | Unset
        if isinstance(self.reranker_model, Unset):
            reranker_model = UNSET
        else:
            reranker_model = self.reranker_model

        top_k: int | None | Unset
        if isinstance(self.top_k, Unset):
            top_k = UNSET
        else:
            top_k = self.top_k

        top_n = self.top_n

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_base_id": knowledge_base_id,
                "query": query,
            }
        )
        if added_after is not UNSET:
            field_dict["added_after"] = added_after
        if added_before is not UNSET:
            field_dict["added_before"] = added_before
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if metadata_filter is not UNSET:
            field_dict["metadata_filter"] = metadata_filter
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if top_n is not UNSET:
            field_dict["top_n"] = top_n

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_retrieval_request_metadata_filter_type_0 import TestRetrievalRequestMetadataFilterType0

        d = dict(src_dict)
        knowledge_base_id = UUID(d.pop("knowledge_base_id"))

        query = d.pop("query")

        def _parse_added_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_after = _parse_added_after(d.pop("added_after", UNSET))

        def _parse_added_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_before = _parse_added_before(d.pop("added_before", UNSET))

        def _parse_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)

                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        content_type = d.pop("content_type", UNSET)

        def _parse_metadata_filter(data: object) -> None | TestRetrievalRequestMetadataFilterType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_filter_type_0 = TestRetrievalRequestMetadataFilterType0.from_dict(data)

                return metadata_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestRetrievalRequestMetadataFilterType0 | Unset, data)

        metadata_filter = _parse_metadata_filter(d.pop("metadata_filter", UNSET))

        def _parse_reranker_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reranker_model = _parse_reranker_model(d.pop("reranker_model", UNSET))

        def _parse_top_k(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        top_k = _parse_top_k(d.pop("top_k", UNSET))

        top_n = d.pop("top_n", UNSET)

        test_retrieval_request = cls(
            knowledge_base_id=knowledge_base_id,
            query=query,
            added_after=added_after,
            added_before=added_before,
            agent_id=agent_id,
            content_type=content_type,
            metadata_filter=metadata_filter,
            reranker_model=reranker_model,
            top_k=top_k,
            top_n=top_n,
        )

        test_retrieval_request.additional_properties = d
        return test_retrieval_request

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
