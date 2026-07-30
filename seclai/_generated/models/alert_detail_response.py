from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_comment_response import AlertCommentResponse
    from ..models.alert_history_entry_response import AlertHistoryEntryResponse
    from ..models.alert_response import AlertResponse
    from ..models.alert_subscriber_response import AlertSubscriberResponse


T = TypeVar("T", bound="AlertDetailResponse")


@_attrs_define
class AlertDetailResponse:
    """
    Attributes:
        alert (AlertResponse):
        comments (list[AlertCommentResponse]):
        history (list[AlertHistoryEntryResponse]):
        subscribers (list[AlertSubscriberResponse]):
    """

    alert: AlertResponse
    comments: list[AlertCommentResponse]
    history: list[AlertHistoryEntryResponse]
    subscribers: list[AlertSubscriberResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert = self.alert.to_dict()

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        subscribers = []
        for subscribers_item_data in self.subscribers:
            subscribers_item = subscribers_item_data.to_dict()
            subscribers.append(subscribers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert": alert,
                "comments": comments,
                "history": history,
                "subscribers": subscribers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_comment_response import AlertCommentResponse
        from ..models.alert_history_entry_response import AlertHistoryEntryResponse
        from ..models.alert_response import AlertResponse
        from ..models.alert_subscriber_response import AlertSubscriberResponse

        d = dict(src_dict)
        alert = AlertResponse.from_dict(d.pop("alert"))

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = AlertCommentResponse.from_dict(comments_item_data)

            comments.append(comments_item)

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = AlertHistoryEntryResponse.from_dict(history_item_data)

            history.append(history_item)

        subscribers = []
        _subscribers = d.pop("subscribers")
        for subscribers_item_data in _subscribers:
            subscribers_item = AlertSubscriberResponse.from_dict(subscribers_item_data)

            subscribers.append(subscribers_item)

        alert_detail_response = cls(
            alert=alert,
            comments=comments,
            history=history,
            subscribers=subscribers,
        )

        alert_detail_response.additional_properties = d
        return alert_detail_response

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
