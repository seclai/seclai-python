from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposed_action_response_params import ProposedActionResponseParams
    from ..models.proposed_action_response_preview_type_0 import (
        ProposedActionResponsePreviewType0,
    )


T = TypeVar("T", bound="ProposedActionResponse")


@_attrs_define
class ProposedActionResponse:
    """A single proposed action.

    Attributes:
        action_type (str): Type of the proposed action.
        description (str): Human-readable description of the action.
        params (ProposedActionResponseParams): Parameters for the action.
        is_destructive (bool | Unset): Whether the action is destructive. Default: False.
        preview (None | ProposedActionResponsePreviewType0 | Unset): Planning-time dry-run preview attached by the
            solution AI assistant for create_agent / update_agent actions. Contains ``steps`` (the generated step tree),
            ``step_count``, ``warnings`` (a mix of heuristic structural issues — e.g. brittle JSONPath, pass-through
            ``regex_replace``, ``prompt_call`` missing a model — and deterministic resource-usage issues: every pre-bound
            knowledge base / memory bank must be referenced by at least one step, and no step may reference an unknown id),
            and ``skipped`` / ``skipped_reason`` when preview couldn't run (e.g. the action depends on resources created
            earlier in the same plan). ``None`` for non-agent actions or when generation failed.
    """

    action_type: str
    description: str
    params: ProposedActionResponseParams
    is_destructive: bool | Unset = False
    preview: None | ProposedActionResponsePreviewType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.proposed_action_response_preview_type_0 import (
            ProposedActionResponsePreviewType0,
        )

        action_type = self.action_type

        description = self.description

        params = self.params.to_dict()

        is_destructive = self.is_destructive

        preview: dict[str, Any] | None | Unset
        if isinstance(self.preview, Unset):
            preview = UNSET
        elif isinstance(self.preview, ProposedActionResponsePreviewType0):
            preview = self.preview.to_dict()
        else:
            preview = self.preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "description": description,
                "params": params,
            }
        )
        if is_destructive is not UNSET:
            field_dict["is_destructive"] = is_destructive
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposed_action_response_params import (
            ProposedActionResponseParams,
        )
        from ..models.proposed_action_response_preview_type_0 import (
            ProposedActionResponsePreviewType0,
        )

        d = dict(src_dict)
        action_type = d.pop("action_type")

        description = d.pop("description")

        params = ProposedActionResponseParams.from_dict(d.pop("params"))

        is_destructive = d.pop("is_destructive", UNSET)

        def _parse_preview(
            data: object,
        ) -> None | ProposedActionResponsePreviewType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preview_type_0 = ProposedActionResponsePreviewType0.from_dict(data)

                return preview_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProposedActionResponsePreviewType0 | Unset, data)

        preview = _parse_preview(d.pop("preview", UNSET))

        proposed_action_response = cls(
            action_type=action_type,
            description=description,
            params=params,
            is_destructive=is_destructive,
            preview=preview,
        )

        proposed_action_response.additional_properties = d
        return proposed_action_response

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
