from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_prompt_call_request_json_template_type_0 import (
        TestPromptCallRequestJsonTemplateType0,
    )
    from ..models.test_prompt_call_request_manual_inputs_type_0 import (
        TestPromptCallRequestManualInputsType0,
    )


T = TypeVar("T", bound="TestPromptCallRequest")


@_attrs_define
class TestPromptCallRequest:
    """Request to test prompt call operation.

    Attributes:
        model (str): The model identifier
        test_input (str): The original agent input ({{agent.input}})
        agent_id (None | Unset | UUID): Optional agent id to attribute recorded usage to. When provided, prompt-call
            usage is linked via agent_usages for reporting.
        current_step_input (None | str | Unset): The previous step output ({{input}})
        json_template (None | TestPromptCallRequestJsonTemplateType0 | Unset): JSON template (JSON format)
        manual_inputs (None | TestPromptCallRequestManualInputsType0 | Unset): Manual inputs for step outputs and other
            substitutions
        max_tokens (int | None | Unset): Max tokens setting
        model_variant (None | str | Unset): Optional model variant
        prompt_template (None | str | Unset): User prompt template (simple format)
        simple_format (bool | Unset): Whether using simple text format (vs JSON) Default: True.
        system_template (None | str | Unset): System prompt template (simple format)
        temperature (float | None | Unset): Temperature setting
    """

    model: str
    test_input: str
    agent_id: None | Unset | UUID = UNSET
    current_step_input: None | str | Unset = UNSET
    json_template: None | TestPromptCallRequestJsonTemplateType0 | Unset = UNSET
    manual_inputs: None | TestPromptCallRequestManualInputsType0 | Unset = UNSET
    max_tokens: int | None | Unset = UNSET
    model_variant: None | str | Unset = UNSET
    prompt_template: None | str | Unset = UNSET
    simple_format: bool | Unset = True
    system_template: None | str | Unset = UNSET
    temperature: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_prompt_call_request_json_template_type_0 import (
            TestPromptCallRequestJsonTemplateType0,
        )
        from ..models.test_prompt_call_request_manual_inputs_type_0 import (
            TestPromptCallRequestManualInputsType0,
        )

        model = self.model

        test_input = self.test_input

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        elif isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        current_step_input: None | str | Unset
        if isinstance(self.current_step_input, Unset):
            current_step_input = UNSET
        else:
            current_step_input = self.current_step_input

        json_template: dict[str, Any] | None | Unset
        if isinstance(self.json_template, Unset):
            json_template = UNSET
        elif isinstance(self.json_template, TestPromptCallRequestJsonTemplateType0):
            json_template = self.json_template.to_dict()
        else:
            json_template = self.json_template

        manual_inputs: dict[str, Any] | None | Unset
        if isinstance(self.manual_inputs, Unset):
            manual_inputs = UNSET
        elif isinstance(self.manual_inputs, TestPromptCallRequestManualInputsType0):
            manual_inputs = self.manual_inputs.to_dict()
        else:
            manual_inputs = self.manual_inputs

        max_tokens: int | None | Unset
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        model_variant: None | str | Unset
        if isinstance(self.model_variant, Unset):
            model_variant = UNSET
        else:
            model_variant = self.model_variant

        prompt_template: None | str | Unset
        if isinstance(self.prompt_template, Unset):
            prompt_template = UNSET
        else:
            prompt_template = self.prompt_template

        simple_format = self.simple_format

        system_template: None | str | Unset
        if isinstance(self.system_template, Unset):
            system_template = UNSET
        else:
            system_template = self.system_template

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "test_input": test_input,
            }
        )
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if current_step_input is not UNSET:
            field_dict["current_step_input"] = current_step_input
        if json_template is not UNSET:
            field_dict["json_template"] = json_template
        if manual_inputs is not UNSET:
            field_dict["manual_inputs"] = manual_inputs
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if model_variant is not UNSET:
            field_dict["model_variant"] = model_variant
        if prompt_template is not UNSET:
            field_dict["prompt_template"] = prompt_template
        if simple_format is not UNSET:
            field_dict["simple_format"] = simple_format
        if system_template is not UNSET:
            field_dict["system_template"] = system_template
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_prompt_call_request_json_template_type_0 import (
            TestPromptCallRequestJsonTemplateType0,
        )
        from ..models.test_prompt_call_request_manual_inputs_type_0 import (
            TestPromptCallRequestManualInputsType0,
        )

        d = dict(src_dict)
        model = d.pop("model")

        test_input = d.pop("test_input")

        def _parse_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)

                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        def _parse_current_step_input(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_step_input = _parse_current_step_input(
            d.pop("current_step_input", UNSET)
        )

        def _parse_json_template(
            data: object,
        ) -> None | TestPromptCallRequestJsonTemplateType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                json_template_type_0 = TestPromptCallRequestJsonTemplateType0.from_dict(
                    data
                )

                return json_template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestPromptCallRequestJsonTemplateType0 | Unset, data)

        json_template = _parse_json_template(d.pop("json_template", UNSET))

        def _parse_manual_inputs(
            data: object,
        ) -> None | TestPromptCallRequestManualInputsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manual_inputs_type_0 = TestPromptCallRequestManualInputsType0.from_dict(
                    data
                )

                return manual_inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestPromptCallRequestManualInputsType0 | Unset, data)

        manual_inputs = _parse_manual_inputs(d.pop("manual_inputs", UNSET))

        def _parse_max_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        def _parse_model_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_variant = _parse_model_variant(d.pop("model_variant", UNSET))

        def _parse_prompt_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_template = _parse_prompt_template(d.pop("prompt_template", UNSET))

        simple_format = d.pop("simple_format", UNSET)

        def _parse_system_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_template = _parse_system_template(d.pop("system_template", UNSET))

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        test_prompt_call_request = cls(
            model=model,
            test_input=test_input,
            agent_id=agent_id,
            current_step_input=current_step_input,
            json_template=json_template,
            manual_inputs=manual_inputs,
            max_tokens=max_tokens,
            model_variant=model_variant,
            prompt_template=prompt_template,
            simple_format=simple_format,
            system_template=system_template,
            temperature=temperature,
        )

        test_prompt_call_request.additional_properties = d
        return test_prompt_call_request

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
