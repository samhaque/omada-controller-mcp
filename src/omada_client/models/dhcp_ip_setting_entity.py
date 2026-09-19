from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpIpSettingEntity")


@_attrs_define
class DhcpIpSettingEntity:
    """DHCP IP setting

    Attributes:
        fallback (bool | Unset): Enable/Disable fallback(if false, other params is not required)
        fallback_ip (str | Unset): Fallback IP address
        fallback_mask (str | Unset): Fallback IP mask
        fallback_gate (str | Unset): Fallback gateway IP address
        use_fixed_addr (bool | Unset): Enable reserved address(Gateway required)
        net_id (str | Unset): Network ID
        dhcp_ip (str | Unset): Reserved IP address
        server_type (str | Unset): DHCP Server Type
        server_mac (str | Unset): DHCP Server Mac
        server_stack_id (str | Unset): DHCP Server Stack ID
    """

    fallback: bool | Unset = UNSET
    fallback_ip: str | Unset = UNSET
    fallback_mask: str | Unset = UNSET
    fallback_gate: str | Unset = UNSET
    use_fixed_addr: bool | Unset = UNSET
    net_id: str | Unset = UNSET
    dhcp_ip: str | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fallback = self.fallback

        fallback_ip = self.fallback_ip

        fallback_mask = self.fallback_mask

        fallback_gate = self.fallback_gate

        use_fixed_addr = self.use_fixed_addr

        net_id = self.net_id

        dhcp_ip = self.dhcp_ip

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if fallback_ip is not UNSET:
            field_dict["fallbackIp"] = fallback_ip
        if fallback_mask is not UNSET:
            field_dict["fallbackMask"] = fallback_mask
        if fallback_gate is not UNSET:
            field_dict["fallbackGate"] = fallback_gate
        if use_fixed_addr is not UNSET:
            field_dict["useFixedAddr"] = use_fixed_addr
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fallback = d.pop("fallback", UNSET)

        fallback_ip = d.pop("fallbackIp", UNSET)

        fallback_mask = d.pop("fallbackMask", UNSET)

        fallback_gate = d.pop("fallbackGate", UNSET)

        use_fixed_addr = d.pop("useFixedAddr", UNSET)

        net_id = d.pop("netId", UNSET)

        dhcp_ip = d.pop("dhcpIp", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        dhcp_ip_setting_entity = cls(
            fallback=fallback,
            fallback_ip=fallback_ip,
            fallback_mask=fallback_mask,
            fallback_gate=fallback_gate,
            use_fixed_addr=use_fixed_addr,
            net_id=net_id,
            dhcp_ip=dhcp_ip,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
        )

        dhcp_ip_setting_entity.additional_properties = d
        return dhcp_ip_setting_entity

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
