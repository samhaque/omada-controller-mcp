from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_template_open_api_vo import AvailableTemplateOpenApiVO


T = TypeVar("T", bound="DeviceAvailableTemplateOpenApiVO")


@_attrs_define
class DeviceAvailableTemplateOpenApiVO:
    """
    Attributes:
        model (str | Unset): The model name of device.
        model_version (str | Unset): The model version of device.
        mac (str | Unset): The mac of device.
        name (str | Unset): The name of device, default value is mac.
        valid_templates (list[AvailableTemplateOpenApiVO] | Unset): The available templates of device.
    """

    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    valid_templates: list[AvailableTemplateOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        model_version = self.model_version

        mac = self.mac

        name = self.name

        valid_templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.valid_templates, Unset):
            valid_templates = []
            for valid_templates_item_data in self.valid_templates:
                valid_templates_item = valid_templates_item_data.to_dict()
                valid_templates.append(valid_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if valid_templates is not UNSET:
            field_dict["validTemplates"] = valid_templates

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.available_template_open_api_vo import (
            AvailableTemplateOpenApiVO,
        )

        d = dict(src_dict)
        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        _valid_templates = d.pop("validTemplates", UNSET)
        valid_templates: list[AvailableTemplateOpenApiVO] | Unset = UNSET
        if _valid_templates is not UNSET:
            valid_templates = []
            for valid_templates_item_data in _valid_templates:
                valid_templates_item = AvailableTemplateOpenApiVO.from_dict(
                    valid_templates_item_data
                )

                valid_templates.append(valid_templates_item)

        device_available_template_open_api_vo = cls(
            model=model,
            model_version=model_version,
            mac=mac,
            name=name,
            valid_templates=valid_templates,
        )

        device_available_template_open_api_vo.additional_properties = d
        return device_available_template_open_api_vo

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
