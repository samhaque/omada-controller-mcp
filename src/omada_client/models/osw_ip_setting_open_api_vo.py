from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswIpSettingOpenApiVO")


@_attrs_define
class OswIpSettingOpenApiVO:
    """Network IP setting.

    Attributes:
        mode (int): IP Setting mode. Static:0, DHCP:1
        ip (str | Unset): Static IP for mode 0, like 192.168.0.1
        gateway (str | Unset): Gateway, like 192.168.137.1
        netmask (str | Unset): IP Mask, like 255.255.255.0
        pre_dns (str | Unset): Primary DNS Server, like 127.0.0.1
        sec_dns (str | Unset): Second DNS Server, link 127.0.0.1
        fallback (bool | Unset): The switch of fallback ip for mode 1.
        fallback_ip (str | Unset): Fallback ip for dhcp mode when fallback is enabled.
        fallback_mask (str | Unset): Fallback mask for dhcp mode when fallback is enabled.
        fallback_gate (str | Unset): Fallback gateway for dhcp mode when fallback is enabled.
        option12 (str | Unset): option12
        use_fixed_addr (bool | Unset): The switch of Address reservation for dhcp mode.
        net_id (str | Unset): The LAN Network for Address reservation when useFixedAddr is enabled. Obtain the id from
            "Get LAN network list"
        dhcp_ip (str | Unset): The IP for Address reservation when useFixedAddr is enabled.
        server_type (str | Unset): The Type of DHCP Server for Address reservation when useFixedAddr is enabled.
        server_mac (str | Unset): The Mac of DHCP Server for Address reservation when useFixedAddr is enabled.
        server_stack_id (str | Unset): The Stack ID of DHCP Server for Address reservation when useFixedAddr is enabled.
        confirm_conflict (bool | Unset): Enable IP-MAC Conflict Detection or not.
    """

    mode: int
    ip: str | Unset = UNSET
    gateway: str | Unset = UNSET
    netmask: str | Unset = UNSET
    pre_dns: str | Unset = UNSET
    sec_dns: str | Unset = UNSET
    fallback: bool | Unset = UNSET
    fallback_ip: str | Unset = UNSET
    fallback_mask: str | Unset = UNSET
    fallback_gate: str | Unset = UNSET
    option12: str | Unset = UNSET
    use_fixed_addr: bool | Unset = UNSET
    net_id: str | Unset = UNSET
    dhcp_ip: str | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    confirm_conflict: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        ip = self.ip

        gateway = self.gateway

        netmask = self.netmask

        pre_dns = self.pre_dns

        sec_dns = self.sec_dns

        fallback = self.fallback

        fallback_ip = self.fallback_ip

        fallback_mask = self.fallback_mask

        fallback_gate = self.fallback_gate

        option12 = self.option12

        use_fixed_addr = self.use_fixed_addr

        net_id = self.net_id

        dhcp_ip = self.dhcp_ip

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        confirm_conflict = self.confirm_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if pre_dns is not UNSET:
            field_dict["preDns"] = pre_dns
        if sec_dns is not UNSET:
            field_dict["secDns"] = sec_dns
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if fallback_ip is not UNSET:
            field_dict["fallbackIp"] = fallback_ip
        if fallback_mask is not UNSET:
            field_dict["fallbackMask"] = fallback_mask
        if fallback_gate is not UNSET:
            field_dict["fallbackGate"] = fallback_gate
        if option12 is not UNSET:
            field_dict["option12"] = option12
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
        if confirm_conflict is not UNSET:
            field_dict["confirmConflict"] = confirm_conflict

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        ip = d.pop("ip", UNSET)

        gateway = d.pop("gateway", UNSET)

        netmask = d.pop("netmask", UNSET)

        pre_dns = d.pop("preDns", UNSET)

        sec_dns = d.pop("secDns", UNSET)

        fallback = d.pop("fallback", UNSET)

        fallback_ip = d.pop("fallbackIp", UNSET)

        fallback_mask = d.pop("fallbackMask", UNSET)

        fallback_gate = d.pop("fallbackGate", UNSET)

        option12 = d.pop("option12", UNSET)

        use_fixed_addr = d.pop("useFixedAddr", UNSET)

        net_id = d.pop("netId", UNSET)

        dhcp_ip = d.pop("dhcpIp", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        confirm_conflict = d.pop("confirmConflict", UNSET)

        osw_ip_setting_open_api_vo = cls(
            mode=mode,
            ip=ip,
            gateway=gateway,
            netmask=netmask,
            pre_dns=pre_dns,
            sec_dns=sec_dns,
            fallback=fallback,
            fallback_ip=fallback_ip,
            fallback_mask=fallback_mask,
            fallback_gate=fallback_gate,
            option12=option12,
            use_fixed_addr=use_fixed_addr,
            net_id=net_id,
            dhcp_ip=dhcp_ip,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
            confirm_conflict=confirm_conflict,
        )

        osw_ip_setting_open_api_vo.additional_properties = d
        return osw_ip_setting_open_api_vo

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
