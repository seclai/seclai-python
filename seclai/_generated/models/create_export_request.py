from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.export_format import ExportFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_export_request_metadata_filter_type_0 import (
        CreateExportRequestMetadataFilterType0,
    )


T = TypeVar("T", bound="CreateExportRequest")


@_attrs_define
class CreateExportRequest:
    """Parameters for creating a new export job.

    Attributes:
        format_ (ExportFormat): Supported export file formats.
        date_from (datetime.datetime | None | Unset): Only include content created on or after this timestamp.
        date_to (datetime.datetime | None | Unset): Only include content created on or before this timestamp.
        metadata_filter (CreateExportRequestMetadataFilterType0 | None | Unset): JSONB containment filter applied to
            content metadata.
        query_filter (None | str | Unset): Title substring filter (case-insensitive ILIKE).
    """

    format_: ExportFormat
    date_from: datetime.datetime | None | Unset = UNSET
    date_to: datetime.datetime | None | Unset = UNSET
    metadata_filter: CreateExportRequestMetadataFilterType0 | None | Unset = UNSET
    query_filter: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_export_request_metadata_filter_type_0 import (
            CreateExportRequestMetadataFilterType0,
        )

        format_ = self.format_.value

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.datetime):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.datetime):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        metadata_filter: dict[str, Any] | None | Unset
        if isinstance(self.metadata_filter, Unset):
            metadata_filter = UNSET
        elif isinstance(self.metadata_filter, CreateExportRequestMetadataFilterType0):
            metadata_filter = self.metadata_filter.to_dict()
        else:
            metadata_filter = self.metadata_filter

        query_filter: None | str | Unset
        if isinstance(self.query_filter, Unset):
            query_filter = UNSET
        else:
            query_filter = self.query_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
            }
        )
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if metadata_filter is not UNSET:
            field_dict["metadata_filter"] = metadata_filter
        if query_filter is not UNSET:
            field_dict["query_filter"] = query_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_export_request_metadata_filter_type_0 import (
            CreateExportRequestMetadataFilterType0,
        )

        d = dict(src_dict)
        format_ = ExportFormat(d.pop("format"))

        def _parse_date_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = isoparse(data)

                return date_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = isoparse(data)

                return date_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_metadata_filter(
            data: object,
        ) -> CreateExportRequestMetadataFilterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_filter_type_0 = (
                    CreateExportRequestMetadataFilterType0.from_dict(data)
                )

                return metadata_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateExportRequestMetadataFilterType0 | None | Unset, data)

        metadata_filter = _parse_metadata_filter(d.pop("metadata_filter", UNSET))

        def _parse_query_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query_filter = _parse_query_filter(d.pop("query_filter", UNSET))

        create_export_request = cls(
            format_=format_,
            date_from=date_from,
            date_to=date_to,
            metadata_filter=metadata_filter,
            query_filter=query_filter,
        )

        create_export_request.additional_properties = d
        return create_export_request

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
