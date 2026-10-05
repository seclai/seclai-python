from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceContentStatusResponse")


@_attrs_define
class SourceContentStatusResponse:
    """Response model for one content item's indexing status.

    Attributes:
        content_status (str): Indexing status: pending, fetching, transcribing, scanning, indexing, completed, or
            failed.
        content_token_count (int | None): Extracted token count.
        content_type (str): Content type group: text, audio, video, image, or document.
        content_url (None | str): Internal URL identifying the item. Uploaded files use a `file-upload://` URL.
        content_version_id (str): ID of the content version. This is the `content_version_id` returned by the upload
            endpoints, so it is what you match an upload against.
        content_word_count (int | None): Extracted word count.
        error (None | str): Why the item failed, when `content_status` is `failed`.
        indexed_at (None | str): Timestamp when the item finished indexing and became retrievable. `null` until then.
        mime_type (None | str): MIME type the item was ingested as, when known.
        published_at (None | str): Publication timestamp of the item, when known.
        pulled_at (str): Timestamp when the item was uploaded or pulled.
        source_connection_content_version_id (None | str): ID to pass to `GET /contents/{id}`. `null` until the item has
            finished indexing — an item that is still processing, or that failed, has no retrievable content and keeps this
            `null`.
        title (None | str): Title of the content item.
        awaiting_reindex (bool | Unset): True when the item is linked and reports completed but its content is not yet
            embedded under the index the source connection currently uses, because it still sits under the index that
            connection used before an embedding migration switched it. Anything ingested while a migration ran can land in
            this state. Semantic and content search will not match it until it is re-embedded; a title keyword match can
            still return it, so the item may appear in results while its body is unsearchable. It clears on its own — a
            reconciliation pass re-embeds the item under the current index, typically within minutes of the migration
            finishing, and a daily sweep retries whatever is still outstanding, so a large backlog can take more than one
            sweep to drain. The re-embedding is not charged to your account: nothing you did caused it, so Seclai absorbs
            the cost. Never true for an item that is simply still indexing; content_status covers that. Default: False.
        extracted_media_capped (bool | Unset): True when extraction stopped with media still unread, so the item
            references more media than was indexed and media search will not match anything past the cut. Two causes: a web
            page that ran out of the budget for fetching remote assets, or a container that could not be read to the end (a
            truncated or hostile archive). An uploaded document that reads cleanly is never capped, however much media it
            holds — there is no limit on that. Default: False.
        extracted_media_count (int | None | Unset): Number of embedded images / videos extracted from inside this item
            and indexed as their own chunks. There is no limit on this — a document contributes as many as it holds. Null
            when there is no media record for the item: the extraction pass has not run, does not apply to this container,
            or found nothing. Treat null as 'unknown', never as zero.
        extracted_media_limit (int | None | Unset): The bound that was reached, when extracted_media_capped is true and
            the stop was a bound — a number of fetch attempts, or a number of seconds. Null when extraction was not capped,
            or when it stopped because the container could not be read rather than because a bound fired.
    """

    content_status: str
    content_token_count: int | None
    content_type: str
    content_url: None | str
    content_version_id: str
    content_word_count: int | None
    error: None | str
    indexed_at: None | str
    mime_type: None | str
    published_at: None | str
    pulled_at: str
    source_connection_content_version_id: None | str
    title: None | str
    awaiting_reindex: bool | Unset = False
    extracted_media_capped: bool | Unset = False
    extracted_media_count: int | None | Unset = UNSET
    extracted_media_limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_status = self.content_status

        content_token_count: int | None
        content_token_count = self.content_token_count

        content_type = self.content_type

        content_url: None | str
        content_url = self.content_url

        content_version_id = self.content_version_id

        content_word_count: int | None
        content_word_count = self.content_word_count

        error: None | str
        error = self.error

        indexed_at: None | str
        indexed_at = self.indexed_at

        mime_type: None | str
        mime_type = self.mime_type

        published_at: None | str
        published_at = self.published_at

        pulled_at = self.pulled_at

        source_connection_content_version_id: None | str
        source_connection_content_version_id = self.source_connection_content_version_id

        title: None | str
        title = self.title

        awaiting_reindex = self.awaiting_reindex

        extracted_media_capped = self.extracted_media_capped

        extracted_media_count: int | None | Unset
        if isinstance(self.extracted_media_count, Unset):
            extracted_media_count = UNSET
        else:
            extracted_media_count = self.extracted_media_count

        extracted_media_limit: int | None | Unset
        if isinstance(self.extracted_media_limit, Unset):
            extracted_media_limit = UNSET
        else:
            extracted_media_limit = self.extracted_media_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_status": content_status,
                "content_token_count": content_token_count,
                "content_type": content_type,
                "content_url": content_url,
                "content_version_id": content_version_id,
                "content_word_count": content_word_count,
                "error": error,
                "indexed_at": indexed_at,
                "mime_type": mime_type,
                "published_at": published_at,
                "pulled_at": pulled_at,
                "source_connection_content_version_id": source_connection_content_version_id,
                "title": title,
            }
        )
        if awaiting_reindex is not UNSET:
            field_dict["awaiting_reindex"] = awaiting_reindex
        if extracted_media_capped is not UNSET:
            field_dict["extracted_media_capped"] = extracted_media_capped
        if extracted_media_count is not UNSET:
            field_dict["extracted_media_count"] = extracted_media_count
        if extracted_media_limit is not UNSET:
            field_dict["extracted_media_limit"] = extracted_media_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_status = d.pop("content_status")

        def _parse_content_token_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        content_token_count = _parse_content_token_count(d.pop("content_token_count"))

        content_type = d.pop("content_type")

        def _parse_content_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_url = _parse_content_url(d.pop("content_url"))

        content_version_id = d.pop("content_version_id")

        def _parse_content_word_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        content_word_count = _parse_content_word_count(d.pop("content_word_count"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        def _parse_indexed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        indexed_at = _parse_indexed_at(d.pop("indexed_at"))

        def _parse_mime_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mime_type = _parse_mime_type(d.pop("mime_type"))

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        pulled_at = d.pop("pulled_at")

        def _parse_source_connection_content_version_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_connection_content_version_id = (
            _parse_source_connection_content_version_id(
                d.pop("source_connection_content_version_id")
            )
        )

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        awaiting_reindex = d.pop("awaiting_reindex", UNSET)

        extracted_media_capped = d.pop("extracted_media_capped", UNSET)

        def _parse_extracted_media_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        extracted_media_count = _parse_extracted_media_count(
            d.pop("extracted_media_count", UNSET)
        )

        def _parse_extracted_media_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        extracted_media_limit = _parse_extracted_media_limit(
            d.pop("extracted_media_limit", UNSET)
        )

        source_content_status_response = cls(
            content_status=content_status,
            content_token_count=content_token_count,
            content_type=content_type,
            content_url=content_url,
            content_version_id=content_version_id,
            content_word_count=content_word_count,
            error=error,
            indexed_at=indexed_at,
            mime_type=mime_type,
            published_at=published_at,
            pulled_at=pulled_at,
            source_connection_content_version_id=source_connection_content_version_id,
            title=title,
            awaiting_reindex=awaiting_reindex,
            extracted_media_capped=extracted_media_capped,
            extracted_media_count=extracted_media_count,
            extracted_media_limit=extracted_media_limit,
        )

        source_content_status_response.additional_properties = d
        return source_content_status_response

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
