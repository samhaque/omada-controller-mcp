from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OspfInterfaceConfigOpenApiVO")


@_attrs_define
class OspfInterfaceConfigOpenApiVO:
    """
    Attributes:
        device_name (str): Device Name
        mac (str): Device Mac
        cost (int): The link cost. OSPF uses this value in computing shortest paths. It should be within the range of
            1–65535.
        type_ (int | Unset): OSPF Interface type, 0: VLAN interface; 1: Loopback interface. If null, defaults to VLAN
            interface (0).
        vlan_interface_id (str | Unset): Vlan Interface ID. Not Null when type is 0.
        vlan_interface_name (str | Unset): Vlan Interface Name. Not Null when type is 0.
        vlan_id (int | Unset): Vlan ID should be within the range of 1–4094. Not Null when type is 0.
        loopback_interface_id (str | Unset): Loopback Interface ID. Not Null when type is 1.
        loopback_id (int | Unset): Loopback ID should be within the range of 1-64. Not Null when type is 1.
        network_type (int | Unset): Network Type. Not Null when type is 0. It should be a value as follows: 0:
            Broadcast, 1: Non-Broadcast, 2: Point-to-Multipoint, 3: Point-to-Point. The default network type for Ethernet
            interfaces is broadcast.
        passive_enable (bool | Unset): enable passive interface.
        hello_interval (int | Unset): The hello interval for the specified interface in seconds. Not Null when type is
            0. This parameter must be the same for all routers attached to a network. It should be within the range of
            1-65535 seconds and the default is 10 seconds.
        dead_interval (int | Unset): The dead interval for the specified interface in seconds. This specifies how long a
            router will wait to see a neighbor router's Hello packets before declaring that the router is down. This
            parameter must be the same for all routers attached to a network. It should be within the range of 1-65535
            seconds and the default is 40.
        authentication_type (int | Unset): Authentication Type. Not Null when type is 0. It should be a value as
            follows: 0: None, 1: Simple, 2: MD5.
        simple_key (str | Unset): Displays the key used for simple authentication, its value should be within the range
            of 1-8.
        md_5_key_id (int | Unset): Displays the key ID used for md5 authentication, its value should be within the range
            of 1-255.
        md_5_key (str | Unset): Displays the key used for md5 authentication, its value should be within the range of
            1-16.
    """

    device_name: str
    mac: str
    cost: int
    type_: int | Unset = UNSET
    vlan_interface_id: str | Unset = UNSET
    vlan_interface_name: str | Unset = UNSET
    vlan_id: int | Unset = UNSET
    loopback_interface_id: str | Unset = UNSET
    loopback_id: int | Unset = UNSET
    network_type: int | Unset = UNSET
    passive_enable: bool | Unset = UNSET
    hello_interval: int | Unset = UNSET
    dead_interval: int | Unset = UNSET
    authentication_type: int | Unset = UNSET
    simple_key: str | Unset = UNSET
    md_5_key_id: int | Unset = UNSET
    md_5_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        mac = self.mac

        cost = self.cost

        type_ = self.type_

        vlan_interface_id = self.vlan_interface_id

        vlan_interface_name = self.vlan_interface_name

        vlan_id = self.vlan_id

        loopback_interface_id = self.loopback_interface_id

        loopback_id = self.loopback_id

        network_type = self.network_type

        passive_enable = self.passive_enable

        hello_interval = self.hello_interval

        dead_interval = self.dead_interval

        authentication_type = self.authentication_type

        simple_key = self.simple_key

        md_5_key_id = self.md_5_key_id

        md_5_key = self.md_5_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceName": device_name,
                "mac": mac,
                "cost": cost,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vlan_interface_id is not UNSET:
            field_dict["vlanInterfaceId"] = vlan_interface_id
        if vlan_interface_name is not UNSET:
            field_dict["vlanInterfaceName"] = vlan_interface_name
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if loopback_interface_id is not UNSET:
            field_dict["loopbackInterfaceId"] = loopback_interface_id
        if loopback_id is not UNSET:
            field_dict["loopbackId"] = loopback_id
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if passive_enable is not UNSET:
            field_dict["passiveEnable"] = passive_enable
        if hello_interval is not UNSET:
            field_dict["helloInterval"] = hello_interval
        if dead_interval is not UNSET:
            field_dict["deadInterval"] = dead_interval
        if authentication_type is not UNSET:
            field_dict["authenticationType"] = authentication_type
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

        cost = d.pop("cost")

        type_ = d.pop("type", UNSET)

        vlan_interface_id = d.pop("vlanInterfaceId", UNSET)

        vlan_interface_name = d.pop("vlanInterfaceName", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        loopback_interface_id = d.pop("loopbackInterfaceId", UNSET)

        loopback_id = d.pop("loopbackId", UNSET)

        network_type = d.pop("networkType", UNSET)

        passive_enable = d.pop("passiveEnable", UNSET)

        hello_interval = d.pop("helloInterval", UNSET)

        dead_interval = d.pop("deadInterval", UNSET)

        authentication_type = d.pop("authenticationType", UNSET)

        simple_key = d.pop("simpleKey", UNSET)

        md_5_key_id = d.pop("md5KeyId", UNSET)

        md_5_key = d.pop("md5Key", UNSET)

        ospf_interface_config_open_api_vo = cls(
            device_name=device_name,
            mac=mac,
            cost=cost,
            type_=type_,
            vlan_interface_id=vlan_interface_id,
            vlan_interface_name=vlan_interface_name,
            vlan_id=vlan_id,
            loopback_interface_id=loopback_interface_id,
            loopback_id=loopback_id,
            network_type=network_type,
            passive_enable=passive_enable,
            hello_interval=hello_interval,
            dead_interval=dead_interval,
            authentication_type=authentication_type,
            simple_key=simple_key,
            md_5_key_id=md_5_key_id,
            md_5_key=md_5_key,
        )

        ospf_interface_config_open_api_vo.additional_properties = d
        return ospf_interface_config_open_api_vo

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
