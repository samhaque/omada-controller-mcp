from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticIpSettingEntity")


@_attrs_define
class StaticIpSettingEntity:
    """Static IP setting

    Attributes:
        config_ip (str | Unset): Static IP address
        config_mask (str | Unset): Subnet mask
        config_gate (str | Unset): Gateway IP address
        preferred_dns (str | Unset): Primary DNS server
        alternate_dns (str | Unset): Secondary DNS server
    """

    config_ip: str | Unset = UNSET
    config_mask: str | Unset = UNSET
    config_gate: str | Unset = UNSET
    preferred_dns: str | Unset = UNSET
    alternate_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_ip = self.config_ip

        config_mask = self.config_mask

        config_gate = self.config_gate

        preferred_dns = self.preferred_dns

        alternate_dns = self.alternate_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_ip is not UNSET:
            field_dict["configIp"] = config_ip
        if config_mask is not UNSET:
            field_dict["configMask"] = config_mask
        if config_gate is not UNSET:
            field_dict["configGate"] = config_gate
        if preferred_dns is not UNSET:
            field_dict["preferredDNS"] = preferred_dns
        if alternate_dns is not UNSET:
            field_dict["alternateDNS"] = alternate_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        config_ip = d.pop("configIp", UNSET)

        config_mask = d.pop("configMask", UNSET)

        config_gate = d.pop("configGate", UNSET)

        preferred_dns = d.pop("preferredDNS", UNSET)

        alternate_dns = d.pop("alternateDNS", UNSET)

        static_ip_setting_entity = cls(
            config_ip=config_ip,
            config_mask=config_mask,
            config_gate=config_gate,
            preferred_dns=preferred_dns,
            alternate_dns=alternate_dns,
        )

        static_ip_setting_entity.additional_properties = d
        return static_ip_setting_entity

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
