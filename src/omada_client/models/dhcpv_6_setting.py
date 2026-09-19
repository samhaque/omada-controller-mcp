from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dhcpv6Setting")


@_attrs_define
class Dhcpv6Setting:
    """Dhcpv6 Setting

    Attributes:
        gateway (str | Unset): Gateway IPv6
        subnet (int | Unset): Netmask IPv6
        ipaddr_start (str | Unset): DHCP Range Start
        ipaddr_end (str | Unset): DHCP Range End
        leasetime (int | Unset): Leasetime should be within the range of 1-11520. Time unit: min(s)
        dnsv6 (int | Unset): DHCP Name Server, should be a value as follows: 0: "auto"; 1: "manual"
        pri_dns (str | Unset): When DNSv6 is 1: "manual", primary DNS Server
        snd_dns (str | Unset): When DNSv6 is 1: "manual", second DNS Server
    """

    gateway: str | Unset = UNSET
    subnet: int | Unset = UNSET
    ipaddr_start: str | Unset = UNSET
    ipaddr_end: str | Unset = UNSET
    leasetime: int | Unset = UNSET
    dnsv6: int | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        subnet = self.subnet

        ipaddr_start = self.ipaddr_start

        ipaddr_end = self.ipaddr_end

        leasetime = self.leasetime

        dnsv6 = self.dnsv6

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if ipaddr_start is not UNSET:
            field_dict["ipaddrStart"] = ipaddr_start
        if ipaddr_end is not UNSET:
            field_dict["ipaddrEnd"] = ipaddr_end
        if leasetime is not UNSET:
            field_dict["leasetime"] = leasetime
        if dnsv6 is not UNSET:
            field_dict["dnsv6"] = dnsv6
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gateway = d.pop("gateway", UNSET)

        subnet = d.pop("subnet", UNSET)

        ipaddr_start = d.pop("ipaddrStart", UNSET)

        ipaddr_end = d.pop("ipaddrEnd", UNSET)

        leasetime = d.pop("leasetime", UNSET)

        dnsv6 = d.pop("dnsv6", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        dhcpv_6_setting = cls(
            gateway=gateway,
            subnet=subnet,
            ipaddr_start=ipaddr_start,
            ipaddr_end=ipaddr_end,
            leasetime=leasetime,
            dnsv6=dnsv6,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
        )

        dhcpv_6_setting.additional_properties = d
        return dhcpv_6_setting

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
