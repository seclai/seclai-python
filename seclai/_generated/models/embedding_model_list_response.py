from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedding_model_response import EmbeddingModelResponse
    from ..models.embedding_storage_credits_response import (
        EmbeddingStorageCreditsResponse,
    )


T = TypeVar("T", bound="EmbeddingModelListResponse")


@_attrs_define
class EmbeddingModelListResponse:
    """Legacy (header-less) response shape for the embedder catalog.

    Attributes:
        file_processing_credits_per_mb (float): Credits per MB for file processing at ingest
        models (list[EmbeddingModelResponse]): Available embedding models
        storage_credits (list[EmbeddingStorageCreditsResponse]): Monthly storage credits per dimension count
        default_dimension (int | None | Unset): Dimensions used with the default embedding model
        default_model_type (None | str | Unset): Embedding model used when a source does not override it
    """

    file_processing_credits_per_mb: float
    models: list[EmbeddingModelResponse]
    storage_credits: list[EmbeddingStorageCreditsResponse]
    default_dimension: int | None | Unset = UNSET
    default_model_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_processing_credits_per_mb = self.file_processing_credits_per_mb

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        storage_credits = []
        for storage_credits_item_data in self.storage_credits:
            storage_credits_item = storage_credits_item_data.to_dict()
            storage_credits.append(storage_credits_item)

        default_dimension: int | None | Unset
        if isinstance(self.default_dimension, Unset):
            default_dimension = UNSET
        else:
            default_dimension = self.default_dimension

        default_model_type: None | str | Unset
        if isinstance(self.default_model_type, Unset):
            default_model_type = UNSET
        else:
            default_model_type = self.default_model_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_processing_credits_per_mb": file_processing_credits_per_mb,
                "models": models,
                "storage_credits": storage_credits,
            }
        )
        if default_dimension is not UNSET:
            field_dict["default_dimension"] = default_dimension
        if default_model_type is not UNSET:
            field_dict["default_model_type"] = default_model_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedding_model_response import EmbeddingModelResponse
        from ..models.embedding_storage_credits_response import (
            EmbeddingStorageCreditsResponse,
        )

        d = dict(src_dict)
        file_processing_credits_per_mb = d.pop("file_processing_credits_per_mb")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = EmbeddingModelResponse.from_dict(models_item_data)

            models.append(models_item)

        storage_credits = []
        _storage_credits = d.pop("storage_credits")
        for storage_credits_item_data in _storage_credits:
            storage_credits_item = EmbeddingStorageCreditsResponse.from_dict(
                storage_credits_item_data
            )

            storage_credits.append(storage_credits_item)

        def _parse_default_dimension(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_dimension = _parse_default_dimension(d.pop("default_dimension", UNSET))

        def _parse_default_model_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_model_type = _parse_default_model_type(
            d.pop("default_model_type", UNSET)
        )

        embedding_model_list_response = cls(
            file_processing_credits_per_mb=file_processing_credits_per_mb,
            models=models,
            storage_credits=storage_credits,
            default_dimension=default_dimension,
            default_model_type=default_model_type,
        )

        embedding_model_list_response.additional_properties = d
        return embedding_model_list_response

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
