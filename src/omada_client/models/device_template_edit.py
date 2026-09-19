from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTemplateEdit")


@_attrs_define
class DeviceTemplateEdit:
    """
    Attributes:
        template_name (str | Unset): The name of device template.
        auto_bind (bool | Unset): Devices will automatically bind the template and use template configurations.
        status (int | Unset): The status of device template. 0:completed ; 1:draft
    """

    template_name: str | Unset = UNSET
    auto_bind: bool | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_name = self.template_name

        auto_bind = self.auto_bind

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if auto_bind is not UNSET:
            field_dict["autoBind"] = auto_bind
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        template_name = d.pop("templateName", UNSET)

        auto_bind = d.pop("autoBind", UNSET)

        status = d.pop("status", UNSET)

        device_template_edit = cls(
            template_name=template_name,
            auto_bind=auto_bind,
            status=status,
        )

        device_template_edit.additional_properties = d
        return device_template_edit

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
