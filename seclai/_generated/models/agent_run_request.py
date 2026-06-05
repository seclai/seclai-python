from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_run_request_metadata_type_0 import AgentRunRequestMetadataType0


T = TypeVar("T", bound="AgentRunRequest")


@_attrs_define
class AgentRunRequest:
    """
    Attributes:
        input_ (None | str | Unset): Input to provide to the agent upon running for agents with dynamic triggers.
        input_upload_id (None | Unset | UUID): ID of a previously uploaded file (via POST /{agent_id}/upload-input) to
            use as the run input for dynamic-input triggers. Mutually exclusive with the 'input' field. Use
            ``input_upload_ids`` to attach multiple files.

            **Attachment visibility:** a step only sees the upload when its template references the input — via
            ``{{input}}`` / ``{{agent.input}}`` / ``{{step.<id>.input|output}}`` (implicit, all attachments) or the
            ``{{attachments[…]}}`` family (explicit narrowing — e.g. ``{{attachments[0]}}``, ``{{attachments[*.pdf]}}``).

            **Per-batch validation:** every selector the agent's definition declares must be satisfied or the run is
            rejected with HTTP 400. Exact-name selectors require that filename to be present; indexed selectors require at
            least N+1 files; glob patterns require at least one matching filename.
        input_upload_ids (list[UUID] | None | Unset): IDs of multiple previously uploaded files. Each upload's extracted
            text is concatenated under a heading; each upload's binary is surfaced as a separate ``MediaAttachment`` so
            multi-modal prompt steps reason over all files at once. Steps narrow visibility via ``{{attachments[…]}}``
            selectors (by index, filename, or fnmatch glob). The batch must satisfy every selector the agent declares —
            exact names, indexed references (length must exceed the highest index), and glob patterns (each pattern needs at
            least one match). Mismatches return HTTP 400 with the unmet requirements listed.  Mutually exclusive with
            ``input`` and ``input_upload_id`` — pass exactly one of the three. Max 20 uploads per run.
        metadata (AgentRunRequestMetadataType0 | None | Unset): Metadata to make available for string substitution
            expressions in agent tasks.
        priority (bool | Unset): If true, the agent run will be treated as priority execution. Default: False.
        replay_of_run_id (None | Unset | UUID): Re-run this agent reusing a prior run's uploaded input files. The files
            are re-resolved server-side from the source run (which must belong to this account and agent) — you do not re-
            upload them. Combine with ``input`` to change the text while keeping the files. A fresh upload batch
            (``input_upload_id(s)``) takes precedence and disables replay. Binaries swept by retention fall back to their
            extracted text.
    """

    input_: None | str | Unset = UNSET
    input_upload_id: None | Unset | UUID = UNSET
    input_upload_ids: list[UUID] | None | Unset = UNSET
    metadata: AgentRunRequestMetadataType0 | None | Unset = UNSET
    priority: bool | Unset = False
    replay_of_run_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_request_metadata_type_0 import (
            AgentRunRequestMetadataType0,
        )

        input_: None | str | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        input_upload_id: None | str | Unset
        if isinstance(self.input_upload_id, Unset):
            input_upload_id = UNSET
        elif isinstance(self.input_upload_id, UUID):
            input_upload_id = str(self.input_upload_id)
        else:
            input_upload_id = self.input_upload_id

        input_upload_ids: list[str] | None | Unset
        if isinstance(self.input_upload_ids, Unset):
            input_upload_ids = UNSET
        elif isinstance(self.input_upload_ids, list):
            input_upload_ids = []
            for input_upload_ids_type_0_item_data in self.input_upload_ids:
                input_upload_ids_type_0_item = str(input_upload_ids_type_0_item_data)
                input_upload_ids.append(input_upload_ids_type_0_item)

        else:
            input_upload_ids = self.input_upload_ids

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AgentRunRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        priority = self.priority

        replay_of_run_id: None | str | Unset
        if isinstance(self.replay_of_run_id, Unset):
            replay_of_run_id = UNSET
        elif isinstance(self.replay_of_run_id, UUID):
            replay_of_run_id = str(self.replay_of_run_id)
        else:
            replay_of_run_id = self.replay_of_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if input_upload_id is not UNSET:
            field_dict["input_upload_id"] = input_upload_id
        if input_upload_ids is not UNSET:
            field_dict["input_upload_ids"] = input_upload_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if priority is not UNSET:
            field_dict["priority"] = priority
        if replay_of_run_id is not UNSET:
            field_dict["replay_of_run_id"] = replay_of_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_request_metadata_type_0 import (
            AgentRunRequestMetadataType0,
        )

        d = dict(src_dict)

        def _parse_input_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_input_upload_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                input_upload_id_type_0 = UUID(data)

                return input_upload_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        input_upload_id = _parse_input_upload_id(d.pop("input_upload_id", UNSET))

        def _parse_input_upload_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_upload_ids_type_0 = []
                _input_upload_ids_type_0 = data
                for input_upload_ids_type_0_item_data in _input_upload_ids_type_0:
                    input_upload_ids_type_0_item = UUID(
                        input_upload_ids_type_0_item_data
                    )

                    input_upload_ids_type_0.append(input_upload_ids_type_0_item)

                return input_upload_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        input_upload_ids = _parse_input_upload_ids(d.pop("input_upload_ids", UNSET))

        def _parse_metadata(
            data: object,
        ) -> AgentRunRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentRunRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentRunRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_replay_of_run_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                replay_of_run_id_type_0 = UUID(data)

                return replay_of_run_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        replay_of_run_id = _parse_replay_of_run_id(d.pop("replay_of_run_id", UNSET))

        agent_run_request = cls(
            input_=input_,
            input_upload_id=input_upload_id,
            input_upload_ids=input_upload_ids,
            metadata=metadata,
            priority=priority,
            replay_of_run_id=replay_of_run_id,
        )

        agent_run_request.additional_properties = d
        return agent_run_request

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
