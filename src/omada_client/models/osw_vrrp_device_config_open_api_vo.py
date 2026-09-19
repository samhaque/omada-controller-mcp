from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswVrrpDeviceConfigOpenApiVO")


@_attrs_define
class OswVrrpDeviceConfigOpenApiVO:
    """Up to 8 entries are allowed for the deviceList, and it cannot be empty.

    Attributes:
        name (str): The name of the device
        mac (str): Device Mac
        priority (int): The device priority should be within the range of 1-254.
        vlan_interface (int): The Vlan Interface should be within the range of 1-4094.
        networks (list[str]): Store the IPv4 and IPv6 network segments corresponding to the VLAN interface, up to 2
            entries are allowed for the networks.
        type_ (str): Device Type
        tracked_interface (int | Unset): The TrackedInterface should be within the range of 1-4094.
        reduced_priority (int | Unset): The ReducedPriority should be within the range of 1-254.
        stack_id (str | Unset): ID of stack group
    """

    name: str
    mac: str
    priority: int
    vlan_interface: int
    networks: list[str]
    type_: str
    tracked_interface: int | Unset = UNSET
    reduced_priority: int | Unset = UNSET
    stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        priority = self.priority

        vlan_interface = self.vlan_interface

        networks = self.networks

        type_ = self.type_

        tracked_interface = self.tracked_interface

        reduced_priority = self.reduced_priority

        stack_id = self.stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mac": mac,
                "priority": priority,
                "vlanInterface": vlan_interface,
                "networks": networks,
                "type": type_,
            }
        )
        if tracked_interface is not UNSET:
            field_dict["trackedInterface"] = tracked_interface
        if reduced_priority is not UNSET:
            field_dict["reducedPriority"] = reduced_priority
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        mac = d.pop("mac")

        priority = d.pop("priority")

        vlan_interface = d.pop("vlanInterface")

        networks = cast(list[str], d.pop("networks"))

        type_ = d.pop("type")

        tracked_interface = d.pop("trackedInterface", UNSET)

        reduced_priority = d.pop("reducedPriority", UNSET)

        stack_id = d.pop("stackId", UNSET)

        osw_vrrp_device_config_open_api_vo = cls(
            name=name,
            mac=mac,
            priority=priority,
            vlan_interface=vlan_interface,
            networks=networks,
            type_=type_,
            tracked_interface=tracked_interface,
            reduced_priority=reduced_priority,
            stack_id=stack_id,
        )

        osw_vrrp_device_config_open_api_vo.additional_properties = d
        return osw_vrrp_device_config_open_api_vo

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
