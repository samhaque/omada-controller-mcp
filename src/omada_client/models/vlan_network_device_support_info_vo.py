from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vlan_network_device_support_info_vo_device_port_support_vlan import (
        VlanNetworkDeviceSupportInfoVODevicePortSupportVlan,
    )


T = TypeVar("T", bound="VlanNetworkDeviceSupportInfoVO")


@_attrs_define
class VlanNetworkDeviceSupportInfoVO:
    """
    Attributes:
        device_port_support_vlan (VlanNetworkDeviceSupportInfoVODevicePortSupportVlan | Unset): The map key is device
            mac. The map value is the device info
    """

    device_port_support_vlan: (
        VlanNetworkDeviceSupportInfoVODevicePortSupportVlan | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_port_support_vlan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_port_support_vlan, Unset):
            device_port_support_vlan = self.device_port_support_vlan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_port_support_vlan is not UNSET:
            field_dict["devicePortSupportVlan"] = device_port_support_vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vlan_network_device_support_info_vo_device_port_support_vlan import (
            VlanNetworkDeviceSupportInfoVODevicePortSupportVlan,
        )

        d = dict(src_dict)
        _device_port_support_vlan = d.pop("devicePortSupportVlan", UNSET)
        device_port_support_vlan: (
            VlanNetworkDeviceSupportInfoVODevicePortSupportVlan | Unset
        )
        if isinstance(_device_port_support_vlan, Unset):
            device_port_support_vlan = UNSET
        else:
            device_port_support_vlan = (
                VlanNetworkDeviceSupportInfoVODevicePortSupportVlan.from_dict(
                    _device_port_support_vlan
                )
            )

        vlan_network_device_support_info_vo = cls(
            device_port_support_vlan=device_port_support_vlan,
        )

        vlan_network_device_support_info_vo.additional_properties = d
        return vlan_network_device_support_info_vo

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
