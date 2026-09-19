from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgWanPortIpv6ConfigVO")


@_attrs_define
class OsgWanPortIpv6ConfigVO:
    """Wan ipv6 config

    Attributes:
        enable (int | Unset): IPv6 enable should be a value as follows: 0: disconnected; 1: connected
        proto (str | Unset):
        addr (str | Unset):
        gateway (str | Unset):
        pri_dns (str | Unset):
        snd_dns (str | Unset):
        internet_state (int | Unset): It should be a value as follows: 0: disconnected; 1: connected
        mac (str | Unset):
    """

    enable: int | Unset = UNSET
    proto: str | Unset = UNSET
    addr: str | Unset = UNSET
    gateway: str | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    internet_state: int | Unset = UNSET
    mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        proto = self.proto

        addr = self.addr

        gateway = self.gateway

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        internet_state = self.internet_state

        mac = self.mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if proto is not UNSET:
            field_dict["proto"] = proto
        if addr is not UNSET:
            field_dict["addr"] = addr
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state
        if mac is not UNSET:
            field_dict["mac"] = mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        proto = d.pop("proto", UNSET)

        addr = d.pop("addr", UNSET)

        gateway = d.pop("gateway", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        internet_state = d.pop("internetState", UNSET)

        mac = d.pop("mac", UNSET)

        osg_wan_port_ipv_6_config_vo = cls(
            enable=enable,
            proto=proto,
            addr=addr,
            gateway=gateway,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            internet_state=internet_state,
            mac=mac,
        )

        osg_wan_port_ipv_6_config_vo.additional_properties = d
        return osg_wan_port_ipv_6_config_vo

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
