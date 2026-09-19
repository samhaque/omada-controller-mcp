from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswIpv6SettingOpenApiVO")


@_attrs_define
class OswIpv6SettingOpenApiVO:
    """Network IPV6 setting.

    Attributes:
        mode (str): Ipv6Setting parameter [mode] should be "dynamic" or "static"
        dns_mode (int | Unset): DNS mode for dynamic mode, 0: Get Dynamic DNS, 1: Use the Following DNS Addresses.
        pri_dns (str | Unset): Primary DNS, like 2001:4860:4860::8888
        snd_dns (str | Unset): Second DNS, like 2001:4860:4860::8844
        ipv_6_addr (str | Unset): IPv6 Address for static mode, like 2001:4860:4860::8888
        prefix_len (int | Unset): Prefix Length for static mode, which should be within the range of 1–128
    """

    mode: str
    dns_mode: int | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    ipv_6_addr: str | Unset = UNSET
    prefix_len: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        dns_mode = self.dns_mode

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        ipv_6_addr = self.ipv_6_addr

        prefix_len = self.prefix_len

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if dns_mode is not UNSET:
            field_dict["dnsMode"] = dns_mode
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if ipv_6_addr is not UNSET:
            field_dict["ipv6Addr"] = ipv_6_addr
        if prefix_len is not UNSET:
            field_dict["prefixLen"] = prefix_len

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        dns_mode = d.pop("dnsMode", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        ipv_6_addr = d.pop("ipv6Addr", UNSET)

        prefix_len = d.pop("prefixLen", UNSET)

        osw_ipv_6_setting_open_api_vo = cls(
            mode=mode,
            dns_mode=dns_mode,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            ipv_6_addr=ipv_6_addr,
            prefix_len=prefix_len,
        )

        osw_ipv_6_setting_open_api_vo.additional_properties = d
        return osw_ipv_6_setting_open_api_vo

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
