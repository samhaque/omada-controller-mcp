from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpSettingVO")


@_attrs_define
class IpSettingVO:
    """Ip Setting

    Attributes:
        mode (str): IpSetting parameter [mode] should be "static" or "dhcp"
        config_ip (str | Unset): Config IP
        config_mask (str | Unset): Config Mask
        config_gate (str | Unset): Config Gate
        fallback (bool | Unset): Fallback, only for "dhcp" mode
        fallback_ip (str | Unset): Fallback IP, only for "dhcp" mode
        fallback_mask (str | Unset): Fallback Mask, only for "dhcp" mode
        fallback_gate (str | Unset): Fallback Gate, only for "dhcp" mode
        use_foxed_addr (bool | Unset): Use Fixed Address, only for "dhcp" mode
        net_id (str | Unset): Net ID, only for "dhcp" mode
        dhcp_ip (str | Unset): DHCP IP, only for "dhcp" mode
        server_type (str | Unset): DHCP Server Type, only for "dhcp" mode
        server_mac (str | Unset): DHCP Server Mac, only for "dhcp" mode
        server_stack_id (str | Unset): DHCP Server Stack ID, only for "dhcp" mode
        preferred_dns (str | Unset): Preferred DNS, only for "static" mode
        alternate_dns (str | Unset): Alternate DNS, only for "static" mode
        confirm_conflict (bool | Unset): Confirm Conflict
    """

    mode: str
    config_ip: str | Unset = UNSET
    config_mask: str | Unset = UNSET
    config_gate: str | Unset = UNSET
    fallback: bool | Unset = UNSET
    fallback_ip: str | Unset = UNSET
    fallback_mask: str | Unset = UNSET
    fallback_gate: str | Unset = UNSET
    use_foxed_addr: bool | Unset = UNSET
    net_id: str | Unset = UNSET
    dhcp_ip: str | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    preferred_dns: str | Unset = UNSET
    alternate_dns: str | Unset = UNSET
    confirm_conflict: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        config_ip = self.config_ip

        config_mask = self.config_mask

        config_gate = self.config_gate

        fallback = self.fallback

        fallback_ip = self.fallback_ip

        fallback_mask = self.fallback_mask

        fallback_gate = self.fallback_gate

        use_foxed_addr = self.use_foxed_addr

        net_id = self.net_id

        dhcp_ip = self.dhcp_ip

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        preferred_dns = self.preferred_dns

        alternate_dns = self.alternate_dns

        confirm_conflict = self.confirm_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if config_ip is not UNSET:
            field_dict["configIp"] = config_ip
        if config_mask is not UNSET:
            field_dict["configMask"] = config_mask
        if config_gate is not UNSET:
            field_dict["configGate"] = config_gate
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if fallback_ip is not UNSET:
            field_dict["fallbackIp"] = fallback_ip
        if fallback_mask is not UNSET:
            field_dict["fallbackMask"] = fallback_mask
        if fallback_gate is not UNSET:
            field_dict["fallbackGate"] = fallback_gate
        if use_foxed_addr is not UNSET:
            field_dict["useFoxedAddr"] = use_foxed_addr
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if dhcp_ip is not UNSET:
            field_dict["dhcpIp"] = dhcp_ip
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id
        if preferred_dns is not UNSET:
            field_dict["preferredDNS"] = preferred_dns
        if alternate_dns is not UNSET:
            field_dict["alternateDNS"] = alternate_dns
        if confirm_conflict is not UNSET:
            field_dict["confirmConflict"] = confirm_conflict

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        config_ip = d.pop("configIp", UNSET)

        config_mask = d.pop("configMask", UNSET)

        config_gate = d.pop("configGate", UNSET)

        fallback = d.pop("fallback", UNSET)

        fallback_ip = d.pop("fallbackIp", UNSET)

        fallback_mask = d.pop("fallbackMask", UNSET)

        fallback_gate = d.pop("fallbackGate", UNSET)

        use_foxed_addr = d.pop("useFoxedAddr", UNSET)

        net_id = d.pop("netId", UNSET)

        dhcp_ip = d.pop("dhcpIp", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        preferred_dns = d.pop("preferredDNS", UNSET)

        alternate_dns = d.pop("alternateDNS", UNSET)

        confirm_conflict = d.pop("confirmConflict", UNSET)

        ip_setting_vo = cls(
            mode=mode,
            config_ip=config_ip,
            config_mask=config_mask,
            config_gate=config_gate,
            fallback=fallback,
            fallback_ip=fallback_ip,
            fallback_mask=fallback_mask,
            fallback_gate=fallback_gate,
            use_foxed_addr=use_foxed_addr,
            net_id=net_id,
            dhcp_ip=dhcp_ip,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
            preferred_dns=preferred_dns,
            alternate_dns=alternate_dns,
            confirm_conflict=confirm_conflict,
        )

        ip_setting_vo.additional_properties = d
        return ip_setting_vo

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
