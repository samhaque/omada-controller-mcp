from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanIpv4Connection2OpenApiVO")


@_attrs_define
class VirtualWanIpv4Connection2OpenApiVO:
    """VirtualWanIpv4Connection2OpenApiVO

    Attributes:
        proto (str): The second virtual WAN IPv4 proto type, use static, dhcp, pppoe.
        main_proto (str | Unset): The main virtual WAN IPv4 proto type, use static, dhcp, pppoe.
        server (str | Unset): VPN server IP/domain.
        ipaddr (str | Unset): IP address.
        netmask (str | Unset): Subnet mask.
        gateway (str | Unset): Gateway IP.
        dns1 (str | Unset): Primary DNS server.
        dns2 (str | Unset): Secondary DNS server.
    """

    proto: str
    main_proto: str | Unset = UNSET
    server: str | Unset = UNSET
    ipaddr: str | Unset = UNSET
    netmask: str | Unset = UNSET
    gateway: str | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proto = self.proto

        main_proto = self.main_proto

        server = self.server

        ipaddr = self.ipaddr

        netmask = self.netmask

        gateway = self.gateway

        dns1 = self.dns1

        dns2 = self.dns2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proto": proto,
            }
        )
        if main_proto is not UNSET:
            field_dict["mainProto"] = main_proto
        if server is not UNSET:
            field_dict["server"] = server
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        proto = d.pop("proto")

        main_proto = d.pop("mainProto", UNSET)

        server = d.pop("server", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        netmask = d.pop("netmask", UNSET)

        gateway = d.pop("gateway", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        virtual_wan_ipv_4_connection_2_open_api_vo = cls(
            proto=proto,
            main_proto=main_proto,
            server=server,
            ipaddr=ipaddr,
            netmask=netmask,
            gateway=gateway,
            dns1=dns1,
            dns2=dns2,
        )

        virtual_wan_ipv_4_connection_2_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_connection_2_open_api_vo

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
