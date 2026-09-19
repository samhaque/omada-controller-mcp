from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_select_device_for_vlan_vo import AutoSelectDeviceForVlanVO


T = TypeVar("T", bound="AutoSelectDevicesForVlanVO")


@_attrs_define
class AutoSelectDevicesForVlanVO:
    """
    Attributes:
        device_list (list[AutoSelectDeviceForVlanVO] | Unset): Auto select device list.
    """

    device_list: list[AutoSelectDeviceForVlanVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auto_select_device_for_vlan_vo import (
            AutoSelectDeviceForVlanVO,
        )

        d = dict(src_dict)
        _device_list = d.pop("deviceList", UNSET)
        device_list: list[AutoSelectDeviceForVlanVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = AutoSelectDeviceForVlanVO.from_dict(
                    device_list_item_data
                )

                device_list.append(device_list_item)

        auto_select_devices_for_vlan_vo = cls(
            device_list=device_list,
        )

        auto_select_devices_for_vlan_vo.additional_properties = d
        return auto_select_devices_for_vlan_vo

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
