from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticIpv6SettingEntity")


@_attrs_define
class StaticIpv6SettingEntity:
    """Static Ipv6 Setting

    Attributes:
        ipv_6_addr (str): ipv6 address, only required for static mode
        prefix_len (int): prefixLen of the ipv6 address, only required for static mode
        default_gate (str | Unset): default gateway, only for static mode
        pri_dns (str | Unset): primary DNS address, pattern: ipv6 address.
        snd_dns (str | Unset): secondary DNS address, pattern: ipv6 address.
    """

    ipv_6_addr: str
    prefix_len: int
    default_gate: str | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_6_addr = self.ipv_6_addr

        prefix_len = self.prefix_len

        default_gate = self.default_gate

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv6Addr": ipv_6_addr,
                "prefixLen": prefix_len,
            }
        )
        if default_gate is not UNSET:
            field_dict["defaultGate"] = default_gate
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ipv_6_addr = d.pop("ipv6Addr")

        prefix_len = d.pop("prefixLen")

        default_gate = d.pop("defaultGate", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        static_ipv_6_setting_entity = cls(
            ipv_6_addr=ipv_6_addr,
            prefix_len=prefix_len,
            default_gate=default_gate,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
        )

        static_ipv_6_setting_entity.additional_properties = d
        return static_ipv_6_setting_entity

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
