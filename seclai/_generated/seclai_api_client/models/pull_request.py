from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.seed_type import SeedType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequest")


@_attrs_define
class PullRequest:
    """Manual pull request for a source.

    Attributes:
        seed (SeedType):
        latest_n (int | None | Unset): Number of latest items to pull (required if seed=latest_n)
        selected_items (list[str] | None | Unset): List of selected item GUIDs (required if seed=selected_items)
    """

    seed: SeedType
    latest_n: int | None | Unset = UNSET
    selected_items: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seed = self.seed.value

        latest_n: int | None | Unset
        if isinstance(self.latest_n, Unset):
            latest_n = UNSET
        else:
            latest_n = self.latest_n

        selected_items: list[str] | None | Unset
        if isinstance(self.selected_items, Unset):
            selected_items = UNSET
        elif isinstance(self.selected_items, list):
            selected_items = self.selected_items

        else:
            selected_items = self.selected_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seed": seed,
            }
        )
        if latest_n is not UNSET:
            field_dict["latest_n"] = latest_n
        if selected_items is not UNSET:
            field_dict["selected_items"] = selected_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seed = SeedType(d.pop("seed"))

        def _parse_latest_n(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_n = _parse_latest_n(d.pop("latest_n", UNSET))

        def _parse_selected_items(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_items_type_0 = cast(list[str], data)

                return selected_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        selected_items = _parse_selected_items(d.pop("selected_items", UNSET))

        pull_request = cls(
            seed=seed,
            latest_n=latest_n,
            selected_items=selected_items,
        )

        pull_request.additional_properties = d
        return pull_request

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
