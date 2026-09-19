from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_binding_vo import PortBindingVO


T = TypeVar("T", bound="SelectPortBindingVO")


@_attrs_define
class SelectPortBindingVO:
    """
    Attributes:
        vlan_type (int): Network type, It should be a value as follows : 0:single vlan 1:multi vlan
        assign_ip_device_type (int): Assign Ip Device Type. It should be a value as follows: 1: gateway 2: switch 0:
            third-party
        port_isolation_enable (bool | Unset): Enable Port Isolation, only valid when creating network.
        flow_control_enable (bool | Unset): Enable Flow Control, only valid when creating network.
        tag_ids (list[str] | Unset): Tag ID List
        device_list (list[PortBindingVO] | Unset): Device List
        internet_ports (list[str] | Unset): Internet Ports
        vlan (int | Unset): vlan, only valid when vlanType is 0 (single vlan)
        vlans (str | Unset): vlans, only valid when vlanType is 1 (multi vlan). VLAN format: 200, 1-100.
        assign_ip_device_mac (str | Unset): Assign Ip Device Mac.
        assign_ip_stack_id (str | Unset): Assign Ip Stack Id, only valid when assigned ip device is a stack.
    """

    vlan_type: int
    assign_ip_device_type: int
    port_isolation_enable: bool | Unset = UNSET
    flow_control_enable: bool | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    device_list: list[PortBindingVO] | Unset = UNSET
    internet_ports: list[str] | Unset = UNSET
    vlan: int | Unset = UNSET
    vlans: str | Unset = UNSET
    assign_ip_device_mac: str | Unset = UNSET
    assign_ip_stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan_type = self.vlan_type

        assign_ip_device_type = self.assign_ip_device_type

        port_isolation_enable = self.port_isolation_enable

        flow_control_enable = self.flow_control_enable

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        internet_ports: list[str] | Unset = UNSET
        if not isinstance(self.internet_ports, Unset):
            internet_ports = self.internet_ports

        vlan = self.vlan

        vlans = self.vlans

        assign_ip_device_mac = self.assign_ip_device_mac

        assign_ip_stack_id = self.assign_ip_stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vlanType": vlan_type,
                "assignIpDeviceType": assign_ip_device_type,
            }
        )
        if port_isolation_enable is not UNSET:
            field_dict["portIsolationEnable"] = port_isolation_enable
        if flow_control_enable is not UNSET:
            field_dict["flowControlEnable"] = flow_control_enable
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list
        if internet_ports is not UNSET:
            field_dict["internetPorts"] = internet_ports
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if assign_ip_device_mac is not UNSET:
            field_dict["assignIpDeviceMac"] = assign_ip_device_mac
        if assign_ip_stack_id is not UNSET:
            field_dict["assignIpStackId"] = assign_ip_stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_binding_vo import PortBindingVO

        d = dict(src_dict)
        vlan_type = d.pop("vlanType")

        assign_ip_device_type = d.pop("assignIpDeviceType")

        port_isolation_enable = d.pop("portIsolationEnable", UNSET)

        flow_control_enable = d.pop("flowControlEnable", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[PortBindingVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = PortBindingVO.from_dict(device_list_item_data)

                device_list.append(device_list_item)

        internet_ports = cast(list[str], d.pop("internetPorts", UNSET))

        vlan = d.pop("vlan", UNSET)

        vlans = d.pop("vlans", UNSET)

        assign_ip_device_mac = d.pop("assignIpDeviceMac", UNSET)

        assign_ip_stack_id = d.pop("assignIpStackId", UNSET)

        select_port_binding_vo = cls(
            vlan_type=vlan_type,
            assign_ip_device_type=assign_ip_device_type,
            port_isolation_enable=port_isolation_enable,
            flow_control_enable=flow_control_enable,
            tag_ids=tag_ids,
            device_list=device_list,
            internet_ports=internet_ports,
            vlan=vlan,
            vlans=vlans,
            assign_ip_device_mac=assign_ip_device_mac,
            assign_ip_stack_id=assign_ip_stack_id,
        )

        select_port_binding_vo.additional_properties = d
        return select_port_binding_vo

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
