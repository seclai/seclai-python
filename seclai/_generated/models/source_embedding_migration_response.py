from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SourceEmbeddingMigrationResponse")


@_attrs_define
class SourceEmbeddingMigrationResponse:
    """Response model for source embedding migration status.

    Attributes:
        completed_at (None | str):
        created_at (str):
        failure_message (None | str):
        id (str):
        notification_recipients (list[str] | None):
        phase (str):
        progress_current (int):
        progress_message (None | str):
        progress_total (int):
        source_connection_id (str):
        source_id_new (str):
        source_id_old (str):
        started_at (None | str):
        status (str):
        target_dimensions (int):
        target_embedding_model (str):
        task_execution_id (None | str):
        updated_at (str):
    """

    completed_at: None | str
    created_at: str
    failure_message: None | str
    id: str
    notification_recipients: list[str] | None
    phase: str
    progress_current: int
    progress_message: None | str
    progress_total: int
    source_connection_id: str
    source_id_new: str
    source_id_old: str
    started_at: None | str
    status: str
    target_dimensions: int
    target_embedding_model: str
    task_execution_id: None | str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_at: None | str
        completed_at = self.completed_at

        created_at = self.created_at

        failure_message: None | str
        failure_message = self.failure_message

        id = self.id

        notification_recipients: list[str] | None
        if isinstance(self.notification_recipients, list):
            notification_recipients = self.notification_recipients

        else:
            notification_recipients = self.notification_recipients

        phase = self.phase

        progress_current = self.progress_current

        progress_message: None | str
        progress_message = self.progress_message

        progress_total = self.progress_total

        source_connection_id = self.source_connection_id

        source_id_new = self.source_id_new

        source_id_old = self.source_id_old

        started_at: None | str
        started_at = self.started_at

        status = self.status

        target_dimensions = self.target_dimensions

        target_embedding_model = self.target_embedding_model

        task_execution_id: None | str
        task_execution_id = self.task_execution_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completed_at": completed_at,
                "created_at": created_at,
                "failure_message": failure_message,
                "id": id,
                "notification_recipients": notification_recipients,
                "phase": phase,
                "progress_current": progress_current,
                "progress_message": progress_message,
                "progress_total": progress_total,
                "source_connection_id": source_connection_id,
                "source_id_new": source_id_new,
                "source_id_old": source_id_old,
                "started_at": started_at,
                "status": status,
                "target_dimensions": target_dimensions,
                "target_embedding_model": target_embedding_model,
                "task_execution_id": task_execution_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        created_at = d.pop("created_at")

        def _parse_failure_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure_message = _parse_failure_message(d.pop("failure_message"))

        id = d.pop("id")

        def _parse_notification_recipients(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_recipients_type_0 = cast(list[str], data)

                return notification_recipients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        notification_recipients = _parse_notification_recipients(
            d.pop("notification_recipients")
        )

        phase = d.pop("phase")

        progress_current = d.pop("progress_current")

        def _parse_progress_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        progress_message = _parse_progress_message(d.pop("progress_message"))

        progress_total = d.pop("progress_total")

        source_connection_id = d.pop("source_connection_id")

        source_id_new = d.pop("source_id_new")

        source_id_old = d.pop("source_id_old")

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = d.pop("status")

        target_dimensions = d.pop("target_dimensions")

        target_embedding_model = d.pop("target_embedding_model")

        def _parse_task_execution_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        task_execution_id = _parse_task_execution_id(d.pop("task_execution_id"))

        updated_at = d.pop("updated_at")

        source_embedding_migration_response = cls(
            completed_at=completed_at,
            created_at=created_at,
            failure_message=failure_message,
            id=id,
            notification_recipients=notification_recipients,
            phase=phase,
            progress_current=progress_current,
            progress_message=progress_message,
            progress_total=progress_total,
            source_connection_id=source_connection_id,
            source_id_new=source_id_new,
            source_id_old=source_id_old,
            started_at=started_at,
            status=status,
            target_dimensions=target_dimensions,
            target_embedding_model=target_embedding_model,
            task_execution_id=task_execution_id,
            updated_at=updated_at,
        )

        source_embedding_migration_response.additional_properties = d
        return source_embedding_migration_response

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
