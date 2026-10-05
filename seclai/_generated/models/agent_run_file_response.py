from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentRunFileResponse")


@_attrs_define
class AgentRunFileResponse:
    """A file in a run's or a step's output.

    Attributes:
        bytes_ (int | None): Size of the file in bytes, when known.
        download_url (str): `GET` URL that streams the file; accepts an API key or OAuth token.
        id (UUID): File identifier, used to download it.
        mime (str): MIME type of the file.
        name (None | str): The file's name in this run, as sent to email recipients and webhooks and matched by
            `{{attachments[...]}}` selectors.
    """

    bytes_: int | None
    download_url: str
    id: UUID
    mime: str
    name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_: int | None
        bytes_ = self.bytes_

        download_url = self.download_url

        id = str(self.id)

        mime = self.mime

        name: None | str
        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bytes": bytes_,
                "download_url": download_url,
                "id": id,
                "mime": mime,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bytes_(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        bytes_ = _parse_bytes_(d.pop("bytes"))

        download_url = d.pop("download_url")

        id = UUID(d.pop("id"))

        mime = d.pop("mime")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        agent_run_file_response = cls(
            bytes_=bytes_,
            download_url=download_url,
            id=id,
            mime=mime,
            name=name,
        )

        agent_run_file_response.additional_properties = d
        return agent_run_file_response

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
