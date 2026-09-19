from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanNetworkBrief")


@_attrs_define
class LanNetworkBrief:
    """A list of lan network info for SdWan Member.

    Attributes:
        id (str | Unset): The ID of the lan network
        site_id (str | Unset): The site ID of the lan network
        name (str | Unset): The name of the lan network
        vlan (int | Unset): The vlan number of the lan network
        vlans (str | Unset): Batch Vlan IDS.
        purpose (str | Unset): The purpose of the lan network
        interface_ids (list[str] | Unset): A list of the Interface ID for the lan network
        vlan_type (int | Unset): The type of vlan of the lan network
        gateway_subnet (str | Unset): The Gateway Subnet of the lan network
        primary (bool | Unset): Whether is default lan
        begin_ip_long (int | Unset): The long value of the beginning IP of gatewaySubnet
        end_ip_long (int | Unset): The long value of the ending IP of gatewaySubnet
        ipaddr_start (str | Unset): The starting host IP address of gatewaySubnet
        ipaddr_end (str | Unset): The ending host IP address of gatewaySubnet
        ip_range_start (int | Unset): The long value of ipaddrStart
        ip_range_end (int | Unset): The long value of ipaddrEnd
    """

    id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    vlans: str | Unset = UNSET
    purpose: str | Unset = UNSET
    interface_ids: list[str] | Unset = UNSET
    vlan_type: int | Unset = UNSET
    gateway_subnet: str | Unset = UNSET
    primary: bool | Unset = UNSET
    begin_ip_long: int | Unset = UNSET
    end_ip_long: int | Unset = UNSET
    ipaddr_start: str | Unset = UNSET
    ipaddr_end: str | Unset = UNSET
    ip_range_start: int | Unset = UNSET
    ip_range_end: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        site_id = self.site_id

        name = self.name

        vlan = self.vlan

        vlans = self.vlans

        purpose = self.purpose

        interface_ids: list[str] | Unset = UNSET
        if not isinstance(self.interface_ids, Unset):
            interface_ids = self.interface_ids

        vlan_type = self.vlan_type

        gateway_subnet = self.gateway_subnet

        primary = self.primary

        begin_ip_long = self.begin_ip_long

        end_ip_long = self.end_ip_long

        ipaddr_start = self.ipaddr_start

        ipaddr_end = self.ipaddr_end

        ip_range_start = self.ip_range_start

        ip_range_end = self.ip_range_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if interface_ids is not UNSET:
            field_dict["interfaceIds"] = interface_ids
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if gateway_subnet is not UNSET:
            field_dict["gatewaySubnet"] = gateway_subnet
        if primary is not UNSET:
            field_dict["primary"] = primary
        if begin_ip_long is not UNSET:
            field_dict["beginIpLong"] = begin_ip_long
        if end_ip_long is not UNSET:
            field_dict["endIpLong"] = end_ip_long
        if ipaddr_start is not UNSET:
            field_dict["ipaddrStart"] = ipaddr_start
        if ipaddr_end is not UNSET:
            field_dict["ipaddrEnd"] = ipaddr_end
        if ip_range_start is not UNSET:
            field_dict["ipRangeStart"] = ip_range_start
        if ip_range_end is not UNSET:
            field_dict["ipRangeEnd"] = ip_range_end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        site_id = d.pop("siteId", UNSET)

        name = d.pop("name", UNSET)

        vlan = d.pop("vlan", UNSET)

        vlans = d.pop("vlans", UNSET)

        purpose = d.pop("purpose", UNSET)

        interface_ids = cast(list[str], d.pop("interfaceIds", UNSET))

        vlan_type = d.pop("vlanType", UNSET)

        gateway_subnet = d.pop("gatewaySubnet", UNSET)

        primary = d.pop("primary", UNSET)

        begin_ip_long = d.pop("beginIpLong", UNSET)

        end_ip_long = d.pop("endIpLong", UNSET)

        ipaddr_start = d.pop("ipaddrStart", UNSET)

        ipaddr_end = d.pop("ipaddrEnd", UNSET)

        ip_range_start = d.pop("ipRangeStart", UNSET)

        ip_range_end = d.pop("ipRangeEnd", UNSET)

        lan_network_brief = cls(
            id=id,
            site_id=site_id,
            name=name,
            vlan=vlan,
            vlans=vlans,
            purpose=purpose,
            interface_ids=interface_ids,
            vlan_type=vlan_type,
            gateway_subnet=gateway_subnet,
            primary=primary,
            begin_ip_long=begin_ip_long,
            end_ip_long=end_ip_long,
            ipaddr_start=ipaddr_start,
            ipaddr_end=ipaddr_end,
            ip_range_start=ip_range_start,
            ip_range_end=ip_range_end,
        )

        lan_network_brief.additional_properties = d
        return lan_network_brief

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
