from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableTemplateOpenApiVO")


@_attrs_define
class AvailableTemplateOpenApiVO:
    """The available templates of device.

    Attributes:
        template_name (str | Unset): The name of template.
        template_id (str | Unset): The id of template.
        multi_bind (bool | Unset): whether to bind multiple devices.
        model (str | Unset): The model name of template.
        model_version (str | Unset): The model version of template.For example: 1.0
    """

    template_name: str | Unset = UNSET
    template_id: str | Unset = UNSET
    multi_bind: bool | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_name = self.template_name

        template_id = self.template_id

        multi_bind = self.multi_bind

        model = self.model

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if multi_bind is not UNSET:
            field_dict["multiBind"] = multi_bind
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        template_name = d.pop("templateName", UNSET)

        template_id = d.pop("templateId", UNSET)

        multi_bind = d.pop("multiBind", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        available_template_open_api_vo = cls(
            template_name=template_name,
            template_id=template_id,
            multi_bind=multi_bind,
            model=model,
            model_version=model_version,
        )

        available_template_open_api_vo.additional_properties = d
        return available_template_open_api_vo

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
