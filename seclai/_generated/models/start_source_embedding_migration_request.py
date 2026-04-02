from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartSourceEmbeddingMigrationRequest")


@_attrs_define
class StartSourceEmbeddingMigrationRequest:
    """Request payload to start a source embedding migration.

    Attributes:
        target_dimensions (int): Target embedding dimensions
        target_embedding_model (str): Target embedding model enum
        chunk_language (None | str | Unset): Language-specific chunking language code
        chunk_overlap (int | None | Unset): Override chunk overlap (characters)
        chunk_regex_separators (bool | None | Unset): Whether chunk separators are regex patterns
        chunk_separators (None | str | Unset): Custom chunk separators (JSON-encoded list)
        chunk_size (int | None | Unset): Override chunk size (characters per chunk)
        notification_recipients (list[str] | None | Unset): Optional notification recipient emails
    """

    target_dimensions: int
    target_embedding_model: str
    chunk_language: None | str | Unset = UNSET
    chunk_overlap: int | None | Unset = UNSET
    chunk_regex_separators: bool | None | Unset = UNSET
    chunk_separators: None | str | Unset = UNSET
    chunk_size: int | None | Unset = UNSET
    notification_recipients: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_dimensions = self.target_dimensions

        target_embedding_model = self.target_embedding_model

        chunk_language: None | str | Unset
        if isinstance(self.chunk_language, Unset):
            chunk_language = UNSET
        else:
            chunk_language = self.chunk_language

        chunk_overlap: int | None | Unset
        if isinstance(self.chunk_overlap, Unset):
            chunk_overlap = UNSET
        else:
            chunk_overlap = self.chunk_overlap

        chunk_regex_separators: bool | None | Unset
        if isinstance(self.chunk_regex_separators, Unset):
            chunk_regex_separators = UNSET
        else:
            chunk_regex_separators = self.chunk_regex_separators

        chunk_separators: None | str | Unset
        if isinstance(self.chunk_separators, Unset):
            chunk_separators = UNSET
        else:
            chunk_separators = self.chunk_separators

        chunk_size: int | None | Unset
        if isinstance(self.chunk_size, Unset):
            chunk_size = UNSET
        else:
            chunk_size = self.chunk_size

        notification_recipients: list[str] | None | Unset
        if isinstance(self.notification_recipients, Unset):
            notification_recipients = UNSET
        elif isinstance(self.notification_recipients, list):
            notification_recipients = self.notification_recipients

        else:
            notification_recipients = self.notification_recipients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_dimensions": target_dimensions,
                "target_embedding_model": target_embedding_model,
            }
        )
        if chunk_language is not UNSET:
            field_dict["chunk_language"] = chunk_language
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap
        if chunk_regex_separators is not UNSET:
            field_dict["chunk_regex_separators"] = chunk_regex_separators
        if chunk_separators is not UNSET:
            field_dict["chunk_separators"] = chunk_separators
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if notification_recipients is not UNSET:
            field_dict["notification_recipients"] = notification_recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_dimensions = d.pop("target_dimensions")

        target_embedding_model = d.pop("target_embedding_model")

        def _parse_chunk_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chunk_language = _parse_chunk_language(d.pop("chunk_language", UNSET))

        def _parse_chunk_overlap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_overlap = _parse_chunk_overlap(d.pop("chunk_overlap", UNSET))

        def _parse_chunk_regex_separators(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        chunk_regex_separators = _parse_chunk_regex_separators(
            d.pop("chunk_regex_separators", UNSET)
        )

        def _parse_chunk_separators(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chunk_separators = _parse_chunk_separators(d.pop("chunk_separators", UNSET))

        def _parse_chunk_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_size = _parse_chunk_size(d.pop("chunk_size", UNSET))

        def _parse_notification_recipients(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_recipients_type_0 = cast(list[str], data)

                return notification_recipients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notification_recipients = _parse_notification_recipients(
            d.pop("notification_recipients", UNSET)
        )

        start_source_embedding_migration_request = cls(
            target_dimensions=target_dimensions,
            target_embedding_model=target_embedding_model,
            chunk_language=chunk_language,
            chunk_overlap=chunk_overlap,
            chunk_regex_separators=chunk_regex_separators,
            chunk_separators=chunk_separators,
            chunk_size=chunk_size,
            notification_recipients=notification_recipients,
        )

        start_source_embedding_migration_request.additional_properties = d
        return start_source_embedding_migration_request

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
