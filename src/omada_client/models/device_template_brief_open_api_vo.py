from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTemplateBriefOpenApiVO")


@_attrs_define
class DeviceTemplateBriefOpenApiVO:
    """
    Attributes:
        id (str | Unset): The ID of device template.
        template_name (str | Unset): The name of device template.
        device_type (str | Unset): The type of device.
        show_model (str | Unset): The model name of device.
    """

    id: str | Unset = UNSET
    template_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    show_model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_name = self.template_name

        device_type = self.device_type

        show_model = self.show_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["ID"] = id
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if show_model is not UNSET:
            field_dict["showModel"] = show_model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("ID", UNSET)

        template_name = d.pop("templateName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        show_model = d.pop("showModel", UNSET)

        device_template_brief_open_api_vo = cls(
            id=id,
            template_name=template_name,
            device_type=device_type,
            show_model=show_model,
        )

        device_template_brief_open_api_vo.additional_properties = d
        return device_template_brief_open_api_vo

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
