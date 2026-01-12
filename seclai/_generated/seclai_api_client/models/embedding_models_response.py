from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.default_chunking_config import DefaultChunkingConfig
    from ..models.embedding_model_info import EmbeddingModelInfo
    from ..models.embedding_storage_credits import EmbeddingStorageCredits
    from ..models.language_option import LanguageOption


T = TypeVar("T", bound="EmbeddingModelsResponse")


@_attrs_define
class EmbeddingModelsResponse:
    """Response model for embedding models list

    Attributes:
        default_chunking (DefaultChunkingConfig): Default chunking configuration
        file_processing_credits_per_mb (float): Credits per MB for file processing
        language_options (list[LanguageOption]): Available programming languages for language-specific chunking
        models (list[EmbeddingModelInfo]): List of available embedding models
        storage_credits (list[EmbeddingStorageCredits]): Storage credits information for embedding dimensions
        default_dimension (int | None | Unset): Default dimension for the default model
        default_model_type (None | str | Unset): Default model type (full enum value)
    """

    default_chunking: DefaultChunkingConfig
    file_processing_credits_per_mb: float
    language_options: list[LanguageOption]
    models: list[EmbeddingModelInfo]
    storage_credits: list[EmbeddingStorageCredits]
    default_dimension: int | None | Unset = UNSET
    default_model_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_chunking = self.default_chunking.to_dict()

        file_processing_credits_per_mb = self.file_processing_credits_per_mb

        language_options = []
        for language_options_item_data in self.language_options:
            language_options_item = language_options_item_data.to_dict()
            language_options.append(language_options_item)

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
                "default_chunking": default_chunking,
                "file_processing_credits_per_mb": file_processing_credits_per_mb,
                "language_options": language_options,
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
        from ..models.default_chunking_config import DefaultChunkingConfig
        from ..models.embedding_model_info import EmbeddingModelInfo
        from ..models.embedding_storage_credits import EmbeddingStorageCredits
        from ..models.language_option import LanguageOption

        d = dict(src_dict)
        default_chunking = DefaultChunkingConfig.from_dict(d.pop("default_chunking"))

        file_processing_credits_per_mb = d.pop("file_processing_credits_per_mb")

        language_options = []
        _language_options = d.pop("language_options")
        for language_options_item_data in _language_options:
            language_options_item = LanguageOption.from_dict(language_options_item_data)

            language_options.append(language_options_item)

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = EmbeddingModelInfo.from_dict(models_item_data)

            models.append(models_item)

        storage_credits = []
        _storage_credits = d.pop("storage_credits")
        for storage_credits_item_data in _storage_credits:
            storage_credits_item = EmbeddingStorageCredits.from_dict(
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

        embedding_models_response = cls(
            default_chunking=default_chunking,
            file_processing_credits_per_mb=file_processing_credits_per_mb,
            language_options=language_options,
            models=models,
            storage_credits=storage_credits,
            default_dimension=default_dimension,
            default_model_type=default_model_type,
        )

        embedding_models_response.additional_properties = d
        return embedding_models_response

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
