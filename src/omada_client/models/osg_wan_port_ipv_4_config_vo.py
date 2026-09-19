from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgWanPortIpv4ConfigVO")


@_attrs_define
class OsgWanPortIpv4ConfigVO:
    """Wan ipv4 config

    Attributes:
        ip (str | Unset):
        netmask (str | Unset):
        ip2 (str | Unset):
        gateway (str | Unset):
        gateway2 (str | Unset):
        pri_dns (str | Unset):
        snd_dns (str | Unset):
        pri_dns_2 (str | Unset):
        snd_dns_2 (str | Unset):
        mac (str | Unset):
    """

    ip: str | Unset = UNSET
    netmask: str | Unset = UNSET
    ip2: str | Unset = UNSET
    gateway: str | Unset = UNSET
    gateway2: str | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    pri_dns_2: str | Unset = UNSET
    snd_dns_2: str | Unset = UNSET
    mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        netmask = self.netmask

        ip2 = self.ip2

        gateway = self.gateway

        gateway2 = self.gateway2

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        pri_dns_2 = self.pri_dns_2

        snd_dns_2 = self.snd_dns_2

        mac = self.mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if ip2 is not UNSET:
            field_dict["ip2"] = ip2
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if gateway2 is not UNSET:
            field_dict["gateway2"] = gateway2
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if pri_dns_2 is not UNSET:
            field_dict["priDns2"] = pri_dns_2
        if snd_dns_2 is not UNSET:
            field_dict["sndDns2"] = snd_dns_2
        if mac is not UNSET:
            field_dict["mac"] = mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip = d.pop("ip", UNSET)

        netmask = d.pop("netmask", UNSET)

        ip2 = d.pop("ip2", UNSET)

        gateway = d.pop("gateway", UNSET)

        gateway2 = d.pop("gateway2", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        pri_dns_2 = d.pop("priDns2", UNSET)

        snd_dns_2 = d.pop("sndDns2", UNSET)

        mac = d.pop("mac", UNSET)

        osg_wan_port_ipv_4_config_vo = cls(
            ip=ip,
            netmask=netmask,
            ip2=ip2,
            gateway=gateway,
            gateway2=gateway2,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            pri_dns_2=pri_dns_2,
            snd_dns_2=snd_dns_2,
            mac=mac,
        )

        osg_wan_port_ipv_4_config_vo.additional_properties = d
        return osg_wan_port_ipv_4_config_vo

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
