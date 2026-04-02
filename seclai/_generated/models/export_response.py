from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_response_metadata_filter_type_0 import (
        ExportResponseMetadataFilterType0,
    )


T = TypeVar("T", bound="ExportResponse")


@_attrs_define
class ExportResponse:
    """Status and metadata for a content source export job.

    Attributes:
        account_id (str): Owning account ID.
        created_at (str): Creation time.
        destination (str): Storage destination.
        format_ (str): Output format.
        id (str): Export job ID.
        source_connection_id (str): Source connection ID.
        status (str): Job status.
        updated_at (str): Last update time.
        completed_at (None | str | Unset): Completion time.
        date_from (None | str | Unset): Date-from filter applied to this export.
        date_to (None | str | Unset): Date-to filter applied to this export.
        error (None | str | Unset): Error message if failed.
        estimated_size_bytes (int | None | Unset): Pre-run size estimate.
        expires_at (None | str | Unset): Download expiry time.
        file_size_bytes (int | None | Unset): File size in bytes.
        item_count (int | None | Unset): Items exported.
        metadata_filter (ExportResponseMetadataFilterType0 | None | Unset): Metadata filter applied to this export.
        progress_current (int | None | Unset): Items processed so far.
        progress_total (int | None | Unset): Total items to process.
        query_filter (None | str | Unset): Query filter applied to this export.
        requested_by_user_id (None | str | Unset): ID of the user who requested this export.
        requested_by_user_name (None | str | Unset): Name of the user who requested this export.
        started_at (None | str | Unset): Processing start time.
        storage_key (None | str | Unset): S3 key of exported file.
    """

    account_id: str
    created_at: str
    destination: str
    format_: str
    id: str
    source_connection_id: str
    status: str
    updated_at: str
    completed_at: None | str | Unset = UNSET
    date_from: None | str | Unset = UNSET
    date_to: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    estimated_size_bytes: int | None | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    file_size_bytes: int | None | Unset = UNSET
    item_count: int | None | Unset = UNSET
    metadata_filter: ExportResponseMetadataFilterType0 | None | Unset = UNSET
    progress_current: int | None | Unset = UNSET
    progress_total: int | None | Unset = UNSET
    query_filter: None | str | Unset = UNSET
    requested_by_user_id: None | str | Unset = UNSET
    requested_by_user_name: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    storage_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_response_metadata_filter_type_0 import (
            ExportResponseMetadataFilterType0,
        )

        account_id = self.account_id

        created_at = self.created_at

        destination = self.destination

        format_ = self.format_

        id = self.id

        source_connection_id = self.source_connection_id

        status = self.status

        updated_at = self.updated_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        else:
            date_to = self.date_to

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        estimated_size_bytes: int | None | Unset
        if isinstance(self.estimated_size_bytes, Unset):
            estimated_size_bytes = UNSET
        else:
            estimated_size_bytes = self.estimated_size_bytes

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        item_count: int | None | Unset
        if isinstance(self.item_count, Unset):
            item_count = UNSET
        else:
            item_count = self.item_count

        metadata_filter: dict[str, Any] | None | Unset
        if isinstance(self.metadata_filter, Unset):
            metadata_filter = UNSET
        elif isinstance(self.metadata_filter, ExportResponseMetadataFilterType0):
            metadata_filter = self.metadata_filter.to_dict()
        else:
            metadata_filter = self.metadata_filter

        progress_current: int | None | Unset
        if isinstance(self.progress_current, Unset):
            progress_current = UNSET
        else:
            progress_current = self.progress_current

        progress_total: int | None | Unset
        if isinstance(self.progress_total, Unset):
            progress_total = UNSET
        else:
            progress_total = self.progress_total

        query_filter: None | str | Unset
        if isinstance(self.query_filter, Unset):
            query_filter = UNSET
        else:
            query_filter = self.query_filter

        requested_by_user_id: None | str | Unset
        if isinstance(self.requested_by_user_id, Unset):
            requested_by_user_id = UNSET
        else:
            requested_by_user_id = self.requested_by_user_id

        requested_by_user_name: None | str | Unset
        if isinstance(self.requested_by_user_name, Unset):
            requested_by_user_name = UNSET
        else:
            requested_by_user_name = self.requested_by_user_name

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        storage_key: None | str | Unset
        if isinstance(self.storage_key, Unset):
            storage_key = UNSET
        else:
            storage_key = self.storage_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "created_at": created_at,
                "destination": destination,
                "format": format_,
                "id": id,
                "source_connection_id": source_connection_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if error is not UNSET:
            field_dict["error"] = error
        if estimated_size_bytes is not UNSET:
            field_dict["estimated_size_bytes"] = estimated_size_bytes
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if metadata_filter is not UNSET:
            field_dict["metadata_filter"] = metadata_filter
        if progress_current is not UNSET:
            field_dict["progress_current"] = progress_current
        if progress_total is not UNSET:
            field_dict["progress_total"] = progress_total
        if query_filter is not UNSET:
            field_dict["query_filter"] = query_filter
        if requested_by_user_id is not UNSET:
            field_dict["requested_by_user_id"] = requested_by_user_id
        if requested_by_user_name is not UNSET:
            field_dict["requested_by_user_name"] = requested_by_user_name
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if storage_key is not UNSET:
            field_dict["storage_key"] = storage_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_response_metadata_filter_type_0 import (
            ExportResponseMetadataFilterType0,
        )

        d = dict(src_dict)
        account_id = d.pop("account_id")

        created_at = d.pop("created_at")

        destination = d.pop("destination")

        format_ = d.pop("format")

        id = d.pop("id")

        source_connection_id = d.pop("source_connection_id")

        status = d.pop("status")

        updated_at = d.pop("updated_at")

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_date_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_estimated_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_size_bytes = _parse_estimated_size_bytes(
            d.pop("estimated_size_bytes", UNSET)
        )

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

        def _parse_item_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        item_count = _parse_item_count(d.pop("item_count", UNSET))

        def _parse_metadata_filter(
            data: object,
        ) -> ExportResponseMetadataFilterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_filter_type_0 = ExportResponseMetadataFilterType0.from_dict(
                    data
                )

                return metadata_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportResponseMetadataFilterType0 | None | Unset, data)

        metadata_filter = _parse_metadata_filter(d.pop("metadata_filter", UNSET))

        def _parse_progress_current(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_current = _parse_progress_current(d.pop("progress_current", UNSET))

        def _parse_progress_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_total = _parse_progress_total(d.pop("progress_total", UNSET))

        def _parse_query_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query_filter = _parse_query_filter(d.pop("query_filter", UNSET))

        def _parse_requested_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by_user_id = _parse_requested_by_user_id(
            d.pop("requested_by_user_id", UNSET)
        )

        def _parse_requested_by_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by_user_name = _parse_requested_by_user_name(
            d.pop("requested_by_user_name", UNSET)
        )

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_key = _parse_storage_key(d.pop("storage_key", UNSET))

        export_response = cls(
            account_id=account_id,
            created_at=created_at,
            destination=destination,
            format_=format_,
            id=id,
            source_connection_id=source_connection_id,
            status=status,
            updated_at=updated_at,
            completed_at=completed_at,
            date_from=date_from,
            date_to=date_to,
            error=error,
            estimated_size_bytes=estimated_size_bytes,
            expires_at=expires_at,
            file_size_bytes=file_size_bytes,
            item_count=item_count,
            metadata_filter=metadata_filter,
            progress_current=progress_current,
            progress_total=progress_total,
            query_filter=query_filter,
            requested_by_user_id=requested_by_user_id,
            requested_by_user_name=requested_by_user_name,
            started_at=started_at,
            storage_key=storage_key,
        )

        export_response.additional_properties = d
        return export_response

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
