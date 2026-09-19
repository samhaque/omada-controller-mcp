from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynamicIpv6SettingEntity")


@_attrs_define
class DynamicIpv6SettingEntity:
    """Dynamic Ipv6 Setting(SLAAC/DHCPv6)

    Attributes:
        dns_mode (int): only for "dynamic" mode (0: Get Dynamic DNS; 1: Use the Following DNS Addresses)
        pri_dns (str | Unset): primary DNS address, pattern: ipv6 address. This value is required when dnsMode is 1.
        snd_dns (str | Unset): secondary DNS address, pattern: ipv6 address. This value is optional when dnsMode is 1.
    """

    dns_mode: int
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns_mode = self.dns_mode

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dnsMode": dns_mode,
            }
        )
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dns_mode = d.pop("dnsMode")

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        dynamic_ipv_6_setting_entity = cls(
            dns_mode=dns_mode,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
        )

        dynamic_ipv_6_setting_entity.additional_properties = d
        return dynamic_ipv_6_setting_entity

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
