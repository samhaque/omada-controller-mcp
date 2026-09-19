from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vlan_network_device_port_support_vo import (
        VlanNetworkDevicePortSupportVO,
    )


T = TypeVar("T", bound="VlanNetworkDeviceSupportVO")


@_attrs_define
class VlanNetworkDeviceSupportVO:
    """The map key is device mac. The map value is the device info

    Attributes:
        mac (str | Unset): Device mac
        type_ (str | Unset): Device type.It should be a value as follows: gateway, switch, ap, olt
        port_list (list[VlanNetworkDevicePortSupportVO] | Unset): Port list
        stack_id (str | Unset): Stack ID, only valid when the device is stack
    """

    mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    port_list: list[VlanNetworkDevicePortSupportVO] | Unset = UNSET
    stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        type_ = self.type_

        port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()
                port_list.append(port_list_item)

        stack_id = self.stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vlan_network_device_port_support_vo import (
            VlanNetworkDevicePortSupportVO,
        )

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        _port_list = d.pop("portList", UNSET)
        port_list: list[VlanNetworkDevicePortSupportVO] | Unset = UNSET
        if _port_list is not UNSET:
            port_list = []
            for port_list_item_data in _port_list:
                port_list_item = VlanNetworkDevicePortSupportVO.from_dict(
                    port_list_item_data
                )

                port_list.append(port_list_item)

        stack_id = d.pop("stackId", UNSET)

        vlan_network_device_support_vo = cls(
            mac=mac,
            type_=type_,
            port_list=port_list,
            stack_id=stack_id,
        )

        vlan_network_device_support_vo.additional_properties = d
        return vlan_network_device_support_vo

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
