from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswDeviceTemplateIdListVO")


@_attrs_define
class OswDeviceTemplateIdListVO:
    """
    Attributes:
        switch_device_template_id_list (list[str] | Unset):
    """

    switch_device_template_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        switch_device_template_id_list: list[str] | Unset = UNSET
        if not isinstance(self.switch_device_template_id_list, Unset):
            switch_device_template_id_list = self.switch_device_template_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switch_device_template_id_list is not UNSET:
            field_dict["switchDeviceTemplateIdList"] = switch_device_template_id_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        switch_device_template_id_list = cast(
            list[str], d.pop("switchDeviceTemplateIdList", UNSET)
        )

        osw_device_template_id_list_vo = cls(
            switch_device_template_id_list=switch_device_template_id_list,
        )

        osw_device_template_id_list_vo.additional_properties = d
        return osw_device_template_id_list_vo

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
