from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnTunnelStatusVO")


@_attrs_define
class VpnTunnelStatusVO:
    """
    Attributes:
        id (str | Unset):
        vpn_id (str | Unset):
        spi (int | Unset):
        name (str | Unset):
        direction (str | Unset):
        local_peer_ip (str | Unset):
        remote_peer_ip (str | Unset):
        local_ip (str | Unset):
        remote_ip (str | Unset):
        local_sa (str | Unset):
        remote_sa (str | Unset):
        protocol (str | Unset):
        ah_authentication (str | Unset):
        esp_authentication (str | Unset):
        esp_encryption (str | Unset):
        user_id (int | Unset):
        user_name (str | Unset):
        interface_name (str | Unset):
        server_type (int | Unset):
        vpn_type (int | Unset):
        client_mode (int | Unset):
        down_pkts (int | Unset):
        down_bytes (int | Unset):
        up_pkts (int | Unset):
        up_bytes (int | Unset):
        uptime (str | Unset):
        dns (str | Unset):
        auth_type (int | Unset):
        login_time (int | Unset):
        login_ip (str | Unset):
        virtual_ip (str | Unset):
        ip_pool_type (int | Unset):
        ip_pool_start (str | Unset):
        ip_pool_end (str | Unset):
        ip_pool (str | Unset):
        port (int | Unset):
        service_port (int | Unset):
        connected_num (int | Unset):
        disconnected_num (int | Unset):
        total_remote_num (int | Unset):
        status (int | Unset):
    """

    id: str | Unset = UNSET
    vpn_id: str | Unset = UNSET
    spi: int | Unset = UNSET
    name: str | Unset = UNSET
    direction: str | Unset = UNSET
    local_peer_ip: str | Unset = UNSET
    remote_peer_ip: str | Unset = UNSET
    local_ip: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    local_sa: str | Unset = UNSET
    remote_sa: str | Unset = UNSET
    protocol: str | Unset = UNSET
    ah_authentication: str | Unset = UNSET
    esp_authentication: str | Unset = UNSET
    esp_encryption: str | Unset = UNSET
    user_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    interface_name: str | Unset = UNSET
    server_type: int | Unset = UNSET
    vpn_type: int | Unset = UNSET
    client_mode: int | Unset = UNSET
    down_pkts: int | Unset = UNSET
    down_bytes: int | Unset = UNSET
    up_pkts: int | Unset = UNSET
    up_bytes: int | Unset = UNSET
    uptime: str | Unset = UNSET
    dns: str | Unset = UNSET
    auth_type: int | Unset = UNSET
    login_time: int | Unset = UNSET
    login_ip: str | Unset = UNSET
    virtual_ip: str | Unset = UNSET
    ip_pool_type: int | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    ip_pool: str | Unset = UNSET
    port: int | Unset = UNSET
    service_port: int | Unset = UNSET
    connected_num: int | Unset = UNSET
    disconnected_num: int | Unset = UNSET
    total_remote_num: int | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        vpn_id = self.vpn_id

        spi = self.spi

        name = self.name

        direction = self.direction

        local_peer_ip = self.local_peer_ip

        remote_peer_ip = self.remote_peer_ip

        local_ip = self.local_ip

        remote_ip = self.remote_ip

        local_sa = self.local_sa

        remote_sa = self.remote_sa

        protocol = self.protocol

        ah_authentication = self.ah_authentication

        esp_authentication = self.esp_authentication

        esp_encryption = self.esp_encryption

        user_id = self.user_id

        user_name = self.user_name

        interface_name = self.interface_name

        server_type = self.server_type

        vpn_type = self.vpn_type

        client_mode = self.client_mode

        down_pkts = self.down_pkts

        down_bytes = self.down_bytes

        up_pkts = self.up_pkts

        up_bytes = self.up_bytes

        uptime = self.uptime

        dns = self.dns

        auth_type = self.auth_type

        login_time = self.login_time

        login_ip = self.login_ip

        virtual_ip = self.virtual_ip

        ip_pool_type = self.ip_pool_type

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        ip_pool = self.ip_pool

        port = self.port

        service_port = self.service_port

        connected_num = self.connected_num

        disconnected_num = self.disconnected_num

        total_remote_num = self.total_remote_num

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if vpn_id is not UNSET:
            field_dict["vpnId"] = vpn_id
        if spi is not UNSET:
            field_dict["spi"] = spi
        if name is not UNSET:
            field_dict["name"] = name
        if direction is not UNSET:
            field_dict["direction"] = direction
        if local_peer_ip is not UNSET:
            field_dict["localPeerIp"] = local_peer_ip
        if remote_peer_ip is not UNSET:
            field_dict["remotePeerIp"] = remote_peer_ip
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if local_sa is not UNSET:
            field_dict["localSa"] = local_sa
        if remote_sa is not UNSET:
            field_dict["remoteSa"] = remote_sa
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if ah_authentication is not UNSET:
            field_dict["ahAuthentication"] = ah_authentication
        if esp_authentication is not UNSET:
            field_dict["espAuthentication"] = esp_authentication
        if esp_encryption is not UNSET:
            field_dict["espEncryption"] = esp_encryption
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
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if login_time is not UNSET:
            field_dict["loginTime"] = login_time
        if login_ip is not UNSET:
            field_dict["loginIp"] = login_ip
        if virtual_ip is not UNSET:
            field_dict["virtualIp"] = virtual_ip
        if ip_pool_type is not UNSET:
            field_dict["ipPoolType"] = ip_pool_type
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if ip_pool is not UNSET:
            field_dict["ipPool"] = ip_pool
        if port is not UNSET:
            field_dict["port"] = port
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if connected_num is not UNSET:
            field_dict["connectedNum"] = connected_num
        if disconnected_num is not UNSET:
            field_dict["disconnectedNum"] = disconnected_num
        if total_remote_num is not UNSET:
            field_dict["totalRemoteNum"] = total_remote_num
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        vpn_id = d.pop("vpnId", UNSET)

        spi = d.pop("spi", UNSET)

        name = d.pop("name", UNSET)

        direction = d.pop("direction", UNSET)

        local_peer_ip = d.pop("localPeerIp", UNSET)

        remote_peer_ip = d.pop("remotePeerIp", UNSET)

        local_ip = d.pop("localIp", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        local_sa = d.pop("localSa", UNSET)

        remote_sa = d.pop("remoteSa", UNSET)

        protocol = d.pop("protocol", UNSET)

        ah_authentication = d.pop("ahAuthentication", UNSET)

        esp_authentication = d.pop("espAuthentication", UNSET)

        esp_encryption = d.pop("espEncryption", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        server_type = d.pop("serverType", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        client_mode = d.pop("clientMode", UNSET)

        down_pkts = d.pop("downPkts", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_pkts = d.pop("upPkts", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        uptime = d.pop("uptime", UNSET)

        dns = d.pop("dns", UNSET)

        auth_type = d.pop("authType", UNSET)

        login_time = d.pop("loginTime", UNSET)

        login_ip = d.pop("loginIp", UNSET)

        virtual_ip = d.pop("virtualIp", UNSET)

        ip_pool_type = d.pop("ipPoolType", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        ip_pool = d.pop("ipPool", UNSET)

        port = d.pop("port", UNSET)

        service_port = d.pop("servicePort", UNSET)

        connected_num = d.pop("connectedNum", UNSET)

        disconnected_num = d.pop("disconnectedNum", UNSET)

        total_remote_num = d.pop("totalRemoteNum", UNSET)

        status = d.pop("status", UNSET)

        vpn_tunnel_status_vo = cls(
            id=id,
            vpn_id=vpn_id,
            spi=spi,
            name=name,
            direction=direction,
            local_peer_ip=local_peer_ip,
            remote_peer_ip=remote_peer_ip,
            local_ip=local_ip,
            remote_ip=remote_ip,
            local_sa=local_sa,
            remote_sa=remote_sa,
            protocol=protocol,
            ah_authentication=ah_authentication,
            esp_authentication=esp_authentication,
            esp_encryption=esp_encryption,
            user_id=user_id,
            user_name=user_name,
            interface_name=interface_name,
            server_type=server_type,
            vpn_type=vpn_type,
            client_mode=client_mode,
            down_pkts=down_pkts,
            down_bytes=down_bytes,
            up_pkts=up_pkts,
            up_bytes=up_bytes,
            uptime=uptime,
            dns=dns,
            auth_type=auth_type,
            login_time=login_time,
            login_ip=login_ip,
            virtual_ip=virtual_ip,
            ip_pool_type=ip_pool_type,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            ip_pool=ip_pool,
            port=port,
            service_port=service_port,
            connected_num=connected_num,
            disconnected_num=disconnected_num,
            total_remote_num=total_remote_num,
            status=status,
        )

        vpn_tunnel_status_vo.additional_properties = d
        return vpn_tunnel_status_vo

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
