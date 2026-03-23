from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_item import FeedItem
    from ..models.page_link import PageLink
    from ..models.rss_content_option import RSSContentOption


T = TypeVar("T", bound="DetectSourceResponse")


@_attrs_define
class DetectSourceResponse:
    """Response model for detection results

    Attributes:
        source_type (str): Detected type: 'website' or 'rss_feed'
        avg_episodes_per_month (float | None | Unset): Average number of episodes published per month
        avg_words_per_episode (int | None | Unset): Average word count per episode
        content_type (None | str | Unset): HTTP Content-Type observed during detection
        error (None | str | Unset): Error message if detection failed
        estimated_episodes_per_day (float | None | Unset): Estimated number of episodes per day based on RSS feed
            publication dates
        example_words_per_episode (int | Unset): Example word count if no historical data available Default: 500.
        existing_source_name (None | str | Unset): Name of the existing source if user already has it
        feed_items (list[FeedItem] | None | Unset): List of detected feed items
        feed_title (None | str | Unset): Detected feed title
        final_url (None | str | Unset): Final resolved URL after redirects (if any)
        has_historical_data (bool | Unset): Whether we have historical data for this feed Default: False.
        page_links (list[PageLink] | None | Unset): List of discovered subpages for websites
        rss_content_default (None | str | Unset): Recommended default RSS content selection
        rss_content_options (list[RSSContentOption] | None | Unset): Available RSS content selection options
        title (None | str | Unset): Detected page/feed title
        url_id (None | str | Unset): ID of the URL
    """

    source_type: str
    avg_episodes_per_month: float | None | Unset = UNSET
    avg_words_per_episode: int | None | Unset = UNSET
    content_type: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    estimated_episodes_per_day: float | None | Unset = UNSET
    example_words_per_episode: int | Unset = 500
    existing_source_name: None | str | Unset = UNSET
    feed_items: list[FeedItem] | None | Unset = UNSET
    feed_title: None | str | Unset = UNSET
    final_url: None | str | Unset = UNSET
    has_historical_data: bool | Unset = False
    page_links: list[PageLink] | None | Unset = UNSET
    rss_content_default: None | str | Unset = UNSET
    rss_content_options: list[RSSContentOption] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    url_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type

        avg_episodes_per_month: float | None | Unset
        if isinstance(self.avg_episodes_per_month, Unset):
            avg_episodes_per_month = UNSET
        else:
            avg_episodes_per_month = self.avg_episodes_per_month

        avg_words_per_episode: int | None | Unset
        if isinstance(self.avg_words_per_episode, Unset):
            avg_words_per_episode = UNSET
        else:
            avg_words_per_episode = self.avg_words_per_episode

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        estimated_episodes_per_day: float | None | Unset
        if isinstance(self.estimated_episodes_per_day, Unset):
            estimated_episodes_per_day = UNSET
        else:
            estimated_episodes_per_day = self.estimated_episodes_per_day

        example_words_per_episode = self.example_words_per_episode

        existing_source_name: None | str | Unset
        if isinstance(self.existing_source_name, Unset):
            existing_source_name = UNSET
        else:
            existing_source_name = self.existing_source_name

        feed_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.feed_items, Unset):
            feed_items = UNSET
        elif isinstance(self.feed_items, list):
            feed_items = []
            for feed_items_type_0_item_data in self.feed_items:
                feed_items_type_0_item = feed_items_type_0_item_data.to_dict()
                feed_items.append(feed_items_type_0_item)

        else:
            feed_items = self.feed_items

        feed_title: None | str | Unset
        if isinstance(self.feed_title, Unset):
            feed_title = UNSET
        else:
            feed_title = self.feed_title

        final_url: None | str | Unset
        if isinstance(self.final_url, Unset):
            final_url = UNSET
        else:
            final_url = self.final_url

        has_historical_data = self.has_historical_data

        page_links: list[dict[str, Any]] | None | Unset
        if isinstance(self.page_links, Unset):
            page_links = UNSET
        elif isinstance(self.page_links, list):
            page_links = []
            for page_links_type_0_item_data in self.page_links:
                page_links_type_0_item = page_links_type_0_item_data.to_dict()
                page_links.append(page_links_type_0_item)

        else:
            page_links = self.page_links

        rss_content_default: None | str | Unset
        if isinstance(self.rss_content_default, Unset):
            rss_content_default = UNSET
        else:
            rss_content_default = self.rss_content_default

        rss_content_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.rss_content_options, Unset):
            rss_content_options = UNSET
        elif isinstance(self.rss_content_options, list):
            rss_content_options = []
            for rss_content_options_type_0_item_data in self.rss_content_options:
                rss_content_options_type_0_item = (
                    rss_content_options_type_0_item_data.to_dict()
                )
                rss_content_options.append(rss_content_options_type_0_item)

        else:
            rss_content_options = self.rss_content_options

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url_id: None | str | Unset
        if isinstance(self.url_id, Unset):
            url_id = UNSET
        else:
            url_id = self.url_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
            }
        )
        if avg_episodes_per_month is not UNSET:
            field_dict["avg_episodes_per_month"] = avg_episodes_per_month
        if avg_words_per_episode is not UNSET:
            field_dict["avg_words_per_episode"] = avg_words_per_episode
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if error is not UNSET:
            field_dict["error"] = error
        if estimated_episodes_per_day is not UNSET:
            field_dict["estimated_episodes_per_day"] = estimated_episodes_per_day
        if example_words_per_episode is not UNSET:
            field_dict["example_words_per_episode"] = example_words_per_episode
        if existing_source_name is not UNSET:
            field_dict["existing_source_name"] = existing_source_name
        if feed_items is not UNSET:
            field_dict["feed_items"] = feed_items
        if feed_title is not UNSET:
            field_dict["feed_title"] = feed_title
        if final_url is not UNSET:
            field_dict["final_url"] = final_url
        if has_historical_data is not UNSET:
            field_dict["has_historical_data"] = has_historical_data
        if page_links is not UNSET:
            field_dict["page_links"] = page_links
        if rss_content_default is not UNSET:
            field_dict["rss_content_default"] = rss_content_default
        if rss_content_options is not UNSET:
            field_dict["rss_content_options"] = rss_content_options
        if title is not UNSET:
            field_dict["title"] = title
        if url_id is not UNSET:
            field_dict["url_id"] = url_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feed_item import FeedItem
        from ..models.page_link import PageLink
        from ..models.rss_content_option import RSSContentOption

        d = dict(src_dict)
        source_type = d.pop("source_type")

        def _parse_avg_episodes_per_month(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_episodes_per_month = _parse_avg_episodes_per_month(
            d.pop("avg_episodes_per_month", UNSET)
        )

        def _parse_avg_words_per_episode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg_words_per_episode = _parse_avg_words_per_episode(
            d.pop("avg_words_per_episode", UNSET)
        )

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_estimated_episodes_per_day(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_episodes_per_day = _parse_estimated_episodes_per_day(
            d.pop("estimated_episodes_per_day", UNSET)
        )

        example_words_per_episode = d.pop("example_words_per_episode", UNSET)

        def _parse_existing_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        existing_source_name = _parse_existing_source_name(
            d.pop("existing_source_name", UNSET)
        )

        def _parse_feed_items(data: object) -> list[FeedItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                feed_items_type_0 = []
                _feed_items_type_0 = data
                for feed_items_type_0_item_data in _feed_items_type_0:
                    feed_items_type_0_item = FeedItem.from_dict(
                        feed_items_type_0_item_data
                    )

                    feed_items_type_0.append(feed_items_type_0_item)

                return feed_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FeedItem] | None | Unset, data)

        feed_items = _parse_feed_items(d.pop("feed_items", UNSET))

        def _parse_feed_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feed_title = _parse_feed_title(d.pop("feed_title", UNSET))

        def _parse_final_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        final_url = _parse_final_url(d.pop("final_url", UNSET))

        has_historical_data = d.pop("has_historical_data", UNSET)

        def _parse_page_links(data: object) -> list[PageLink] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                page_links_type_0 = []
                _page_links_type_0 = data
                for page_links_type_0_item_data in _page_links_type_0:
                    page_links_type_0_item = PageLink.from_dict(
                        page_links_type_0_item_data
                    )

                    page_links_type_0.append(page_links_type_0_item)

                return page_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PageLink] | None | Unset, data)

        page_links = _parse_page_links(d.pop("page_links", UNSET))

        def _parse_rss_content_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rss_content_default = _parse_rss_content_default(
            d.pop("rss_content_default", UNSET)
        )

        def _parse_rss_content_options(
            data: object,
        ) -> list[RSSContentOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rss_content_options_type_0 = []
                _rss_content_options_type_0 = data
                for rss_content_options_type_0_item_data in _rss_content_options_type_0:
                    rss_content_options_type_0_item = RSSContentOption.from_dict(
                        rss_content_options_type_0_item_data
                    )

                    rss_content_options_type_0.append(rss_content_options_type_0_item)

                return rss_content_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RSSContentOption] | None | Unset, data)

        rss_content_options = _parse_rss_content_options(
            d.pop("rss_content_options", UNSET)
        )

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_url_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_id = _parse_url_id(d.pop("url_id", UNSET))

        detect_source_response = cls(
            source_type=source_type,
            avg_episodes_per_month=avg_episodes_per_month,
            avg_words_per_episode=avg_words_per_episode,
            content_type=content_type,
            error=error,
            estimated_episodes_per_day=estimated_episodes_per_day,
            example_words_per_episode=example_words_per_episode,
            existing_source_name=existing_source_name,
            feed_items=feed_items,
            feed_title=feed_title,
            final_url=final_url,
            has_historical_data=has_historical_data,
            page_links=page_links,
            rss_content_default=rss_content_default,
            rss_content_options=rss_content_options,
            title=title,
            url_id=url_id,
        )

        detect_source_response.additional_properties = d
        return detect_source_response

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
