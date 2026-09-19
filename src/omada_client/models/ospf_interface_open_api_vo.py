from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OspfInterfaceOpenApiVO")


@_attrs_define
class OspfInterfaceOpenApiVO:
    """
    Attributes:
        device_name (str): Device Name
        mac (str): Device Mac
        vlan_interface_id (str): Vlan Interface ID
        vlan_interface_name (str): Vlan Interface Name
        vlan_id (int): Vlan ID should be within the range of 1–4094.
        cost (int): The link cost. OSPF uses this value in computing shortest paths. cost should be within the range of
            1 to 65535.
        network_type (int): Network Type, it should be a value as follows: 0: Broadcast, 1: Non-Broadcast, 2: Point-to-
            Multipoint, 3: Point-to-Point. The default network type for Ethernet interfaces is broadcast.
        hello_interval (int): The hello interval for the specified interface in seconds. This parameter must be the same
            for all routers attached to a network. It should be within the range of 1-65535 seconds and the default is 10
            seconds.
        authentication_type (int): Authentication Type, it should be a value as follows: 0: None, 1: Simple, 2: MD5.
        id (str | Unset): OSPF Interface ID
        is_stack (bool | Unset): Indicates whether the device is a stack member device.
        type_ (int | Unset): OSPF Interface type, 0: VLAN interface; 1: Loopback interface. If null, defaults to VLAN
            interface (0).
        stack_id (str | Unset): Stack ID, used for backend verification, there is no need to transmit values, and it has
            value when the mac is master.
        loopback_interface_id (str | Unset): Loopback Interface ID. Not Null when type is 1.
        loopback_id (int | Unset): Loopback ID should be within the range of 1-64. Not Null when type is 1.
        passive_enable (bool | Unset): enable passive interface.
        dead_interval (int | Unset): The dead interval for the specified interface in seconds. This specifies how long a
            router will wait to see a neighbor router's Hello packets before declaring that the router is down. This
            parameter must be the same for all routers attached to a network. It should be within the range of 1-65535
            seconds and the default is 40.
        simple_key (str | Unset): Displays the key used for simple authentication, its value should be within the range
            of 1-8.
        md_5_key_id (int | Unset): Displays the key ID used for md5 authentication, its value should be within the range
            of 1-255.
        md_5_key (str | Unset): Displays the key used for md5 authentication, its value should be within the range of
            1-16.
    """

    device_name: str
    mac: str
    vlan_interface_id: str
    vlan_interface_name: str
    vlan_id: int
    cost: int
    network_type: int
    hello_interval: int
    authentication_type: int
    id: str | Unset = UNSET
    is_stack: bool | Unset = UNSET
    type_: int | Unset = UNSET
    stack_id: str | Unset = UNSET
    loopback_interface_id: str | Unset = UNSET
    loopback_id: int | Unset = UNSET
    passive_enable: bool | Unset = UNSET
    dead_interval: int | Unset = UNSET
    simple_key: str | Unset = UNSET
    md_5_key_id: int | Unset = UNSET
    md_5_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        mac = self.mac

        vlan_interface_id = self.vlan_interface_id

        vlan_interface_name = self.vlan_interface_name

        vlan_id = self.vlan_id

        cost = self.cost

        network_type = self.network_type

        hello_interval = self.hello_interval

        authentication_type = self.authentication_type

        id = self.id

        is_stack = self.is_stack

        type_ = self.type_

        stack_id = self.stack_id

        loopback_interface_id = self.loopback_interface_id

        loopback_id = self.loopback_id

        passive_enable = self.passive_enable

        dead_interval = self.dead_interval

        simple_key = self.simple_key

        md_5_key_id = self.md_5_key_id

        md_5_key = self.md_5_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceName": device_name,
                "mac": mac,
                "vlanInterfaceId": vlan_interface_id,
                "vlanInterfaceName": vlan_interface_name,
                "vlanId": vlan_id,
                "cost": cost,
                "networkType": network_type,
                "helloInterval": hello_interval,
                "authenticationType": authentication_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_stack is not UNSET:
            field_dict["isStack"] = is_stack
        if type_ is not UNSET:
            field_dict["type"] = type_
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if loopback_interface_id is not UNSET:
            field_dict["loopbackInterfaceId"] = loopback_interface_id
        if loopback_id is not UNSET:
            field_dict["loopbackId"] = loopback_id
        if passive_enable is not UNSET:
            field_dict["passiveEnable"] = passive_enable
        if dead_interval is not UNSET:
            field_dict["deadInterval"] = dead_interval
        if simple_key is not UNSET:
            field_dict["simpleKey"] = simple_key
        if md_5_key_id is not UNSET:
            field_dict["md5KeyId"] = md_5_key_id
        if md_5_key is not UNSET:
            field_dict["md5Key"] = md_5_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_name = d.pop("deviceName")

        mac = d.pop("mac")

        vlan_interface_id = d.pop("vlanInterfaceId")

        vlan_interface_name = d.pop("vlanInterfaceName")

        vlan_id = d.pop("vlanId")

        cost = d.pop("cost")

        network_type = d.pop("networkType")

        hello_interval = d.pop("helloInterval")

        authentication_type = d.pop("authenticationType")

        id = d.pop("id", UNSET)

        is_stack = d.pop("isStack", UNSET)

        type_ = d.pop("type", UNSET)

        stack_id = d.pop("stackId", UNSET)

        loopback_interface_id = d.pop("loopbackInterfaceId", UNSET)

        loopback_id = d.pop("loopbackId", UNSET)

        passive_enable = d.pop("passiveEnable", UNSET)

        dead_interval = d.pop("deadInterval", UNSET)

        simple_key = d.pop("simpleKey", UNSET)

        md_5_key_id = d.pop("md5KeyId", UNSET)

        md_5_key = d.pop("md5Key", UNSET)

        ospf_interface_open_api_vo = cls(
            device_name=device_name,
            mac=mac,
            vlan_interface_id=vlan_interface_id,
            vlan_interface_name=vlan_interface_name,
            vlan_id=vlan_id,
            cost=cost,
            network_type=network_type,
            hello_interval=hello_interval,
            authentication_type=authentication_type,
            id=id,
            is_stack=is_stack,
            type_=type_,
            stack_id=stack_id,
            loopback_interface_id=loopback_interface_id,
            loopback_id=loopback_id,
            passive_enable=passive_enable,
            dead_interval=dead_interval,
            simple_key=simple_key,
            md_5_key_id=md_5_key_id,
            md_5_key=md_5_key,
        )

        ospf_interface_open_api_vo.additional_properties = d
        return ospf_interface_open_api_vo

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
