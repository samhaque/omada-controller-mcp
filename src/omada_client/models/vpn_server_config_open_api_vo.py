from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO
    from ..models.lock_setting_open_api_vo import LockSettingOpenApiVO
    from ..models.radius_auth_setting_open_api_vo import RadiusAuthSettingOpenApiVO
    from ..models.server_wire_guard_clients_config_vo import (
        ServerWireGuardClientsConfigVO,
    )
    from ..models.vpn_advanced_setting_open_api_vo import VpnAdvancedSettingOpenApiVO
    from ..models.vpn_base_auth_setting_open_api_vo import VpnBaseAuthSettingOpenApiVO
    from ..models.vpn_ip_subnets_open_api_vo import VpnIPSubnetsOpenApiVO


T = TypeVar("T", bound="VpnServerConfigOpenApiVO")


@_attrs_define
class VpnServerConfigOpenApiVO:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        status (bool): Status of the VPN.
        vpn_type (int): Vpn type should be a value as follows: 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN; 4: WireGuard; 5:
            SSL VPN.
        wans (list[str]): WAN list of the VPN. WAN port ID can be obtained from 'Get internet basic info' interface.
        service_port (int): Service port should be within the range of 1–65535.
        mtu (int): The MTU of WireGuard VPN should be within the range of 576-1440.
        keep_alive (int): The keepalive second of WireGuard peer should be within the range of 0-65535.
        private_key (str): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        service_type (int): Service type of the Open VPN should be a value as follows: 0: UDP; 1: TCP.
        remote_ip (str): Remote IP of the VPN.
        pre_shared_key (str): Pre-shared key of the VPN.
        advanced_setting (VpnAdvancedSettingOpenApiVO): Advanced setting list of the VPN, only for IPSec type.
        name_lock_setting (LockSettingOpenApiVO): IP lock config. It is required when parameter [status] is true.
        ip_lock_setting (LockSettingOpenApiVO): IP lock config. It is required when parameter [status] is true.
        exit_at_idle (bool): Whether to exit when idle.  It is required when parameter [status] is true.
        vpn_user_list (list[str]): VPN user ID list.
        custom_server (bool | Unset): Enable custom server.
        custom_server_address (str | Unset): When parameter [customServer] is enable, parameter [customServerAddress]
            should be IPv4 address or FQDN.
        ip_pool_type (int | Unset): IP pool type should be a value as follows: 0: Ip Address/Mask; 1: Ip Address Range.
        ip_pool_start (str | Unset): The start IP of the IP pool.
        ip_pool_end (str | Unset): The end IP of the IP pool.
        ip_pool (IPSubnetsVO | Unset): User remote subnets of the VPN user.
        dns_status (bool | Unset): Dns auto status.
        dns1 (str | Unset): Primary DNS of the VPN.
        dns2 (str | Unset): Secondary DNS of the VPN.
        clients (list[ServerWireGuardClientsConfigVO] | Unset): WireGuard clients.
        tunnel_mode (int | Unset): Tunnel mode(only for server OpenVPN) should be a value as follows: 0: split; 1: full.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[VpnIPSubnetsOpenApiVO] | Unset): Custom networks of the VPN.
        account_auth (bool | Unset): Whether enable account password of the VPN, only for server OpenVPN.
        auth_mode (int | Unset): Authentication mode should be a value as follows: 0: Local; 1: LDAP; 2:RADIUS.
        radius_setting (RadiusAuthSettingOpenApiVO | Unset): It is required for SSL VPN when parameter [authType] is 2.
        ldap_setting (VpnBaseAuthSettingOpenApiVO | Unset): It is required for SSL VPN when parameter [authType] is 1.
        ldap_profile (str | Unset): It is required when parameter [authType] is 1.
        encryption (int | Unset): Encryption should be a value as follows: 0: Encrypted; 1: Unencrypted; 2: Auto.
        exit_time (int | Unset): Exit time should be within the range of 5–3600(s). It is required when parameter
            [exitAtIdle] is true.
        total_traffic (bool | Unset): Whether to proxy all traffic. It is required when parameter [status] is true.
    """

    name: str
    status: bool
    vpn_type: int
    wans: list[str]
    service_port: int
    mtu: int
    keep_alive: int
    private_key: str
    service_type: int
    remote_ip: str
    pre_shared_key: str
    advanced_setting: VpnAdvancedSettingOpenApiVO
    name_lock_setting: LockSettingOpenApiVO
    ip_lock_setting: LockSettingOpenApiVO
    exit_at_idle: bool
    vpn_user_list: list[str]
    custom_server: bool | Unset = UNSET
    custom_server_address: str | Unset = UNSET
    ip_pool_type: int | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    ip_pool: IPSubnetsVO | Unset = UNSET
    dns_status: bool | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    clients: list[ServerWireGuardClientsConfigVO] | Unset = UNSET
    tunnel_mode: int | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
    account_auth: bool | Unset = UNSET
    auth_mode: int | Unset = UNSET
    radius_setting: RadiusAuthSettingOpenApiVO | Unset = UNSET
    ldap_setting: VpnBaseAuthSettingOpenApiVO | Unset = UNSET
    ldap_profile: str | Unset = UNSET
    encryption: int | Unset = UNSET
    exit_time: int | Unset = UNSET
    total_traffic: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        wans = self.wans

        service_port = self.service_port

        mtu = self.mtu

        keep_alive = self.keep_alive

        private_key = self.private_key

        service_type = self.service_type

        remote_ip = self.remote_ip

        pre_shared_key = self.pre_shared_key

        advanced_setting = self.advanced_setting.to_dict()

        name_lock_setting = self.name_lock_setting.to_dict()

        ip_lock_setting = self.ip_lock_setting.to_dict()

        exit_at_idle = self.exit_at_idle

        vpn_user_list = self.vpn_user_list

        custom_server = self.custom_server

        custom_server_address = self.custom_server_address

        ip_pool_type = self.ip_pool_type

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        ip_pool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_pool, Unset):
            ip_pool = self.ip_pool.to_dict()

        dns_status = self.dns_status

        dns1 = self.dns1

        dns2 = self.dns2

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        tunnel_mode = self.tunnel_mode

        network_type = self.network_type

        network_list: list[str] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        custom_network: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_network, Unset):
            custom_network = []
            for custom_network_item_data in self.custom_network:
                custom_network_item = custom_network_item_data.to_dict()
                custom_network.append(custom_network_item)

        account_auth = self.account_auth

        auth_mode = self.auth_mode

        radius_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_setting, Unset):
            radius_setting = self.radius_setting.to_dict()

        ldap_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_setting, Unset):
            ldap_setting = self.ldap_setting.to_dict()

        ldap_profile = self.ldap_profile

        encryption = self.encryption

        exit_time = self.exit_time

        total_traffic = self.total_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "vpnType": vpn_type,
                "wans": wans,
                "servicePort": service_port,
                "mtu": mtu,
                "keepAlive": keep_alive,
                "privateKey": private_key,
                "serviceType": service_type,
                "remoteIp": remote_ip,
                "preSharedKey": pre_shared_key,
                "advancedSetting": advanced_setting,
                "nameLockSetting": name_lock_setting,
                "ipLockSetting": ip_lock_setting,
                "exitAtIdle": exit_at_idle,
                "vpnUserList": vpn_user_list,
            }
        )
        if custom_server is not UNSET:
            field_dict["customServer"] = custom_server
        if custom_server_address is not UNSET:
            field_dict["customServerAddress"] = custom_server_address
        if ip_pool_type is not UNSET:
            field_dict["ipPoolType"] = ip_pool_type
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if ip_pool is not UNSET:
            field_dict["ipPool"] = ip_pool
        if dns_status is not UNSET:
            field_dict["dnsStatus"] = dns_status
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if clients is not UNSET:
            field_dict["clients"] = clients
        if tunnel_mode is not UNSET:
            field_dict["tunnelMode"] = tunnel_mode
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if account_auth is not UNSET:
            field_dict["accountAuth"] = account_auth
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if radius_setting is not UNSET:
            field_dict["radiusSetting"] = radius_setting
        if ldap_setting is not UNSET:
            field_dict["ldapSetting"] = ldap_setting
        if ldap_profile is not UNSET:
            field_dict["ldapProfile"] = ldap_profile
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if exit_time is not UNSET:
            field_dict["exitTime"] = exit_time
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_vo import IPSubnetsVO
        from ..models.lock_setting_open_api_vo import (
            LockSettingOpenApiVO,
        )
        from ..models.radius_auth_setting_open_api_vo import (
            RadiusAuthSettingOpenApiVO,
        )
        from ..models.server_wire_guard_clients_config_vo import (
            ServerWireGuardClientsConfigVO,
        )
        from ..models.vpn_advanced_setting_open_api_vo import (
            VpnAdvancedSettingOpenApiVO,
        )
        from ..models.vpn_base_auth_setting_open_api_vo import (
            VpnBaseAuthSettingOpenApiVO,
        )
        from ..models.vpn_ip_subnets_open_api_vo import (
            VpnIPSubnetsOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        vpn_type = d.pop("vpnType")

        wans = cast(list[str], d.pop("wans"))

        service_port = d.pop("servicePort")

        mtu = d.pop("mtu")

        keep_alive = d.pop("keepAlive")

        private_key = d.pop("privateKey")

        service_type = d.pop("serviceType")

        remote_ip = d.pop("remoteIp")

        pre_shared_key = d.pop("preSharedKey")

        advanced_setting = VpnAdvancedSettingOpenApiVO.from_dict(
            d.pop("advancedSetting")
        )

        name_lock_setting = LockSettingOpenApiVO.from_dict(d.pop("nameLockSetting"))

        ip_lock_setting = LockSettingOpenApiVO.from_dict(d.pop("ipLockSetting"))

        exit_at_idle = d.pop("exitAtIdle")

        vpn_user_list = cast(list[str], d.pop("vpnUserList"))

        custom_server = d.pop("customServer", UNSET)

        custom_server_address = d.pop("customServerAddress", UNSET)

        ip_pool_type = d.pop("ipPoolType", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        _ip_pool = d.pop("ipPool", UNSET)
        ip_pool: IPSubnetsVO | Unset
        if isinstance(_ip_pool, Unset):
            ip_pool = UNSET
        else:
            ip_pool = IPSubnetsVO.from_dict(_ip_pool)

        dns_status = d.pop("dnsStatus", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        _clients = d.pop("clients", UNSET)
        clients: list[ServerWireGuardClientsConfigVO] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = ServerWireGuardClientsConfigVO.from_dict(
                    clients_item_data
                )

                clients.append(clients_item)

        tunnel_mode = d.pop("tunnelMode", UNSET)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(list[str], d.pop("networkList", UNSET))

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = VpnIPSubnetsOpenApiVO.from_dict(
                    custom_network_item_data
                )

                custom_network.append(custom_network_item)

        account_auth = d.pop("accountAuth", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        _radius_setting = d.pop("radiusSetting", UNSET)
        radius_setting: RadiusAuthSettingOpenApiVO | Unset
        if isinstance(_radius_setting, Unset):
            radius_setting = UNSET
        else:
            radius_setting = RadiusAuthSettingOpenApiVO.from_dict(_radius_setting)

        _ldap_setting = d.pop("ldapSetting", UNSET)
        ldap_setting: VpnBaseAuthSettingOpenApiVO | Unset
        if isinstance(_ldap_setting, Unset):
            ldap_setting = UNSET
        else:
            ldap_setting = VpnBaseAuthSettingOpenApiVO.from_dict(_ldap_setting)

        ldap_profile = d.pop("ldapProfile", UNSET)

        encryption = d.pop("encryption", UNSET)

        exit_time = d.pop("exitTime", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        vpn_server_config_open_api_vo = cls(
            name=name,
            status=status,
            vpn_type=vpn_type,
            wans=wans,
            service_port=service_port,
            mtu=mtu,
            keep_alive=keep_alive,
            private_key=private_key,
            service_type=service_type,
            remote_ip=remote_ip,
            pre_shared_key=pre_shared_key,
            advanced_setting=advanced_setting,
            name_lock_setting=name_lock_setting,
            ip_lock_setting=ip_lock_setting,
            exit_at_idle=exit_at_idle,
            vpn_user_list=vpn_user_list,
            custom_server=custom_server,
            custom_server_address=custom_server_address,
            ip_pool_type=ip_pool_type,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            ip_pool=ip_pool,
            dns_status=dns_status,
            dns1=dns1,
            dns2=dns2,
            clients=clients,
            tunnel_mode=tunnel_mode,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            account_auth=account_auth,
            auth_mode=auth_mode,
            radius_setting=radius_setting,
            ldap_setting=ldap_setting,
            ldap_profile=ldap_profile,
            encryption=encryption,
            exit_time=exit_time,
            total_traffic=total_traffic,
        )

        vpn_server_config_open_api_vo.additional_properties = d
        return vpn_server_config_open_api_vo

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
