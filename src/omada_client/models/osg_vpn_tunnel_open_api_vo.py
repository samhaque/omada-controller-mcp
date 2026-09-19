from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgVpnTunnelOpenApiVO")


@_attrs_define
class OsgVpnTunnelOpenApiVO:
    """
    Attributes:
        vpn_id (int | Unset): VPN Item Id.
        vpn_name (str | Unset): VPN Item Name.
        user_id (int | Unset): User Id.
        user_name (str | Unset): Peer Username.
        interface_name (str | Unset): Interface Name.
        server_type (int | Unset): Client-To-Site VPN Type First-level cascade selection 0:VPN Server 1:VPN Client.
        vpn_type (int | Unset): Client-To-Site VPN Type Second-level cascade selection 0：L2TP 1: PPTP 2: IPSec 3:
            OpenVPN.
        client_mode (str | Unset): Client Mode: Client or NEM(Network Extension Mode).
        local_ip (str | Unset): The local Server IP of the tunnel.
        remote_ip (str | Unset): The IP address of the peer VPN User.
        down_pkts (int | Unset): Number of packets in the downlink.
        down_bytes (int | Unset): Downlink traffic in bytes.
        up_pkts (int | Unset): The amount of uplink packets.
        up_bytes (int | Unset): Uplink traffic in bytes.
        uptime (str | Unset): VPN tunnel effective time, it starts from the connection calculation, accurate to the
            minute.
        dns (str | Unset): DNS for the peer VPN.
    """

    vpn_id: int | Unset = UNSET
    vpn_name: str | Unset = UNSET
    user_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    interface_name: str | Unset = UNSET
    server_type: int | Unset = UNSET
    vpn_type: int | Unset = UNSET
    client_mode: str | Unset = UNSET
    local_ip: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    down_pkts: int | Unset = UNSET
    down_bytes: int | Unset = UNSET
    up_pkts: int | Unset = UNSET
    up_bytes: int | Unset = UNSET
    uptime: str | Unset = UNSET
    dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_id = self.vpn_id

        vpn_name = self.vpn_name

        user_id = self.user_id

        user_name = self.user_name

        interface_name = self.interface_name

        server_type = self.server_type

        vpn_type = self.vpn_type

        client_mode = self.client_mode

        local_ip = self.local_ip

        remote_ip = self.remote_ip

        down_pkts = self.down_pkts

        down_bytes = self.down_bytes

        up_pkts = self.up_pkts

        up_bytes = self.up_bytes

        uptime = self.uptime

        dns = self.dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_id is not UNSET:
            field_dict["vpnId"] = vpn_id
        if vpn_name is not UNSET:
            field_dict["vpnName"] = vpn_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if vpn_type is not UNSET:
            field_dict["vpnType"] = vpn_type
        if client_mode is not UNSET:
            field_dict["clientMode"] = client_mode
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if down_pkts is not UNSET:
            field_dict["downPkts"] = down_pkts
        if down_bytes is not UNSET:
            field_dict["downBytes"] = down_bytes
        if up_pkts is not UNSET:
            field_dict["upPkts"] = up_pkts
        if up_bytes is not UNSET:
            field_dict["upBytes"] = up_bytes
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if dns is not UNSET:
            field_dict["dns"] = dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vpn_id = d.pop("vpnId", UNSET)

        vpn_name = d.pop("vpnName", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        server_type = d.pop("serverType", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        client_mode = d.pop("clientMode", UNSET)

        local_ip = d.pop("localIp", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        down_pkts = d.pop("downPkts", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_pkts = d.pop("upPkts", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        uptime = d.pop("uptime", UNSET)

        dns = d.pop("dns", UNSET)

        osg_vpn_tunnel_open_api_vo = cls(
            vpn_id=vpn_id,
            vpn_name=vpn_name,
            user_id=user_id,
            user_name=user_name,
            interface_name=interface_name,
            server_type=server_type,
            vpn_type=vpn_type,
            client_mode=client_mode,
            local_ip=local_ip,
            remote_ip=remote_ip,
            down_pkts=down_pkts,
            down_bytes=down_bytes,
            up_pkts=up_pkts,
            up_bytes=up_bytes,
            uptime=uptime,
            dns=dns,
        )

        osg_vpn_tunnel_open_api_vo.additional_properties = d
        return osg_vpn_tunnel_open_api_vo

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
