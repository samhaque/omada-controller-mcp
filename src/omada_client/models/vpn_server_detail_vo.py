from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO
    from ..models.ip_subnets_vo import IPSubnetsVO
    from ..models.ldap_setting_open_api_vo import LdapSettingOpenApiVO
    from ..models.lock_setting_open_api_vo import LockSettingOpenApiVO
    from ..models.radius_auth_setting_open_api_vo import RadiusAuthSettingOpenApiVO
    from ..models.server_wire_guard_clients_vo import ServerWireGuardClientsVO
    from ..models.vpn_advanced_setting_open_api_vo import VpnAdvancedSettingOpenApiVO
    from ..models.vpn_ip_subnets_open_api_vo import VpnIPSubnetsOpenApiVO


T = TypeVar("T", bound="VpnServerDetailVO")


@_attrs_define
class VpnServerDetailVO:
    """
    Attributes:
        id (str | Unset): ID of the VPN.
        name (str | Unset): VPN name.
        status (bool | Unset): Status of the VPN.
        vpn_type (int | Unset): Server Vpn type. 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN; 4: WireGuard; 5: SSL VPN.
        wans (list[str] | Unset): WAN port ID.
        service_port (int | Unset): Service port for VPN server.
        custom_server (bool | Unset): Whether enable custom server.
        custom_server_address (str | Unset): IPv4 Address or FQDN.
        ip_pool_type (int | Unset): IP pool type should be a value as follows: 0: Ip Address/Mask; 1: Ip Address Range.
        ip_pool_start (str | Unset): The start IP of the IP pool.
        ip_pool_end (str | Unset): The end IP of the IP pool.
        ip_pool (IPSubnetsVO | Unset): User remote subnets of the VPN user.
        mtu (int | Unset): The MTU of WireGuard VPN should be within the range of 576-1440.
        keep_alive (int | Unset): The keepalive second of WireGuard peer should be within the range of 0-65535.
        private_key (str | Unset): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        public_key (str | Unset): The public key of WireGuard VPN must have 44 character of base64 and end with '='.
        dns_status (bool | Unset): Dns auto status.
        dns1 (str | Unset): Primary DNS of the VPN.
        dns2 (str | Unset): Secondary DNS of the VPN.
        clients (list[ServerWireGuardClientsVO] | Unset): WireGuard clients.
        tunnel_mode (int | Unset): OpenVPN tunnel mode should be a value as follows: 0: split; 1: full.
        network_type (int | Unset): Network type. 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN.
        custom_network (list[VpnIPSubnetsOpenApiVO] | Unset): Custom networks of the VPN.
        account_auth (bool | Unset): Account auth of the VPN, only for server OpenVPN.
        auth_mode (int | Unset): Authentication mode. 0: Local; 1: LDAP.
        service_type (int | Unset): Service type of the VPN.
        remote_ip (str | Unset): Remote IP of the VPN.
        encryption (int | Unset): Encryption type. Only L2TP can configure auto type. 0: Encrypted; 1: Unencrypted; 2:
            Auto.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        advanced_setting (VpnAdvancedSettingOpenApiVO | Unset): Advanced setting list of the VPN, only for IPSec type.
        ldap_profile (str | Unset):
        ldap_setting (LdapSettingOpenApiVO | Unset): It is required when parameter [authType] is 2.
        radius_setting (RadiusAuthSettingOpenApiVO | Unset): It is required for SSL VPN when parameter [authType] is 2.
        name_lock_setting (LockSettingOpenApiVO | Unset): IP lock config. It is required when parameter [status] is
            true.
        ip_lock_setting (LockSettingOpenApiVO | Unset): IP lock config. It is required when parameter [status] is true.
        exit_at_idle (bool | Unset): Whether to exit when idle.
        exit_time (int | Unset): Exit time should be within the range of 5–3600(s). It is required when parameter
            [exitAtIdle] is true.
        total_traffic (bool | Unset): Whether to proxy all traffic.
        vpn_user_list (list[str] | Unset): VPN user id list.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    vpn_type: int | Unset = UNSET
    wans: list[str] | Unset = UNSET
    service_port: int | Unset = UNSET
    custom_server: bool | Unset = UNSET
    custom_server_address: str | Unset = UNSET
    ip_pool_type: int | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    ip_pool: IPSubnetsVO | Unset = UNSET
    mtu: int | Unset = UNSET
    keep_alive: int | Unset = UNSET
    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    dns_status: bool | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    clients: list[ServerWireGuardClientsVO] | Unset = UNSET
    tunnel_mode: int | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
    account_auth: bool | Unset = UNSET
    auth_mode: int | Unset = UNSET
    service_type: int | Unset = UNSET
    remote_ip: str | Unset = UNSET
    encryption: int | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    advanced_setting: VpnAdvancedSettingOpenApiVO | Unset = UNSET
    ldap_profile: str | Unset = UNSET
    ldap_setting: LdapSettingOpenApiVO | Unset = UNSET
    radius_setting: RadiusAuthSettingOpenApiVO | Unset = UNSET
    name_lock_setting: LockSettingOpenApiVO | Unset = UNSET
    ip_lock_setting: LockSettingOpenApiVO | Unset = UNSET
    exit_at_idle: bool | Unset = UNSET
    exit_time: int | Unset = UNSET
    total_traffic: bool | Unset = UNSET
    vpn_user_list: list[str] | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        wans: list[str] | Unset = UNSET
        if not isinstance(self.wans, Unset):
            wans = self.wans

        service_port = self.service_port

        custom_server = self.custom_server

        custom_server_address = self.custom_server_address

        ip_pool_type = self.ip_pool_type

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        ip_pool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_pool, Unset):
            ip_pool = self.ip_pool.to_dict()

        mtu = self.mtu

        keep_alive = self.keep_alive

        private_key = self.private_key

        public_key = self.public_key

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

        service_type = self.service_type

        remote_ip = self.remote_ip

        encryption = self.encryption

        pre_shared_key = self.pre_shared_key

        advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_setting, Unset):
            advanced_setting = self.advanced_setting.to_dict()

        ldap_profile = self.ldap_profile

        ldap_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_setting, Unset):
            ldap_setting = self.ldap_setting.to_dict()

        radius_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_setting, Unset):
            radius_setting = self.radius_setting.to_dict()

        name_lock_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_lock_setting, Unset):
            name_lock_setting = self.name_lock_setting.to_dict()

        ip_lock_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_lock_setting, Unset):
            ip_lock_setting = self.ip_lock_setting.to_dict()

        exit_at_idle = self.exit_at_idle

        exit_time = self.exit_time

        total_traffic = self.total_traffic

        vpn_user_list: list[str] | Unset = UNSET
        if not isinstance(self.vpn_user_list, Unset):
            vpn_user_list = self.vpn_user_list

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if vpn_type is not UNSET:
            field_dict["vpnType"] = vpn_type
        if wans is not UNSET:
            field_dict["wans"] = wans
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
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
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
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
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if advanced_setting is not UNSET:
            field_dict["advancedSetting"] = advanced_setting
        if ldap_profile is not UNSET:
            field_dict["ldapProfile"] = ldap_profile
        if ldap_setting is not UNSET:
            field_dict["LDAPSetting"] = ldap_setting
        if radius_setting is not UNSET:
            field_dict["radiusSetting"] = radius_setting
        if name_lock_setting is not UNSET:
            field_dict["nameLockSetting"] = name_lock_setting
        if ip_lock_setting is not UNSET:
            field_dict["ipLockSetting"] = ip_lock_setting
        if exit_at_idle is not UNSET:
            field_dict["exitAtIdle"] = exit_at_idle
        if exit_time is not UNSET:
            field_dict["exitTime"] = exit_time
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if vpn_user_list is not UNSET:
            field_dict["vpnUserList"] = vpn_user_list
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO
        from ..models.ip_subnets_vo import IPSubnetsVO
        from ..models.ldap_setting_open_api_vo import (
            LdapSettingOpenApiVO,
        )
        from ..models.lock_setting_open_api_vo import (
            LockSettingOpenApiVO,
        )
        from ..models.radius_auth_setting_open_api_vo import (
            RadiusAuthSettingOpenApiVO,
        )
        from ..models.server_wire_guard_clients_vo import (
            ServerWireGuardClientsVO,
        )
        from ..models.vpn_advanced_setting_open_api_vo import (
            VpnAdvancedSettingOpenApiVO,
        )
        from ..models.vpn_ip_subnets_open_api_vo import (
            VpnIPSubnetsOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        wans = cast(list[str], d.pop("wans", UNSET))

        service_port = d.pop("servicePort", UNSET)

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

        mtu = d.pop("mtu", UNSET)

        keep_alive = d.pop("keepAlive", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        dns_status = d.pop("dnsStatus", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        _clients = d.pop("clients", UNSET)
        clients: list[ServerWireGuardClientsVO] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = ServerWireGuardClientsVO.from_dict(clients_item_data)

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

        service_type = d.pop("serviceType", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        encryption = d.pop("encryption", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        _advanced_setting = d.pop("advancedSetting", UNSET)
        advanced_setting: VpnAdvancedSettingOpenApiVO | Unset
        if isinstance(_advanced_setting, Unset):
            advanced_setting = UNSET
        else:
            advanced_setting = VpnAdvancedSettingOpenApiVO.from_dict(_advanced_setting)

        ldap_profile = d.pop("ldapProfile", UNSET)

        _ldap_setting = d.pop("LDAPSetting", UNSET)
        ldap_setting: LdapSettingOpenApiVO | Unset
        if isinstance(_ldap_setting, Unset):
            ldap_setting = UNSET
        else:
            ldap_setting = LdapSettingOpenApiVO.from_dict(_ldap_setting)

        _radius_setting = d.pop("radiusSetting", UNSET)
        radius_setting: RadiusAuthSettingOpenApiVO | Unset
        if isinstance(_radius_setting, Unset):
            radius_setting = UNSET
        else:
            radius_setting = RadiusAuthSettingOpenApiVO.from_dict(_radius_setting)

        _name_lock_setting = d.pop("nameLockSetting", UNSET)
        name_lock_setting: LockSettingOpenApiVO | Unset
        if isinstance(_name_lock_setting, Unset):
            name_lock_setting = UNSET
        else:
            name_lock_setting = LockSettingOpenApiVO.from_dict(_name_lock_setting)

        _ip_lock_setting = d.pop("ipLockSetting", UNSET)
        ip_lock_setting: LockSettingOpenApiVO | Unset
        if isinstance(_ip_lock_setting, Unset):
            ip_lock_setting = UNSET
        else:
            ip_lock_setting = LockSettingOpenApiVO.from_dict(_ip_lock_setting)

        exit_at_idle = d.pop("exitAtIdle", UNSET)

        exit_time = d.pop("exitTime", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        vpn_user_list = cast(list[str], d.pop("vpnUserList", UNSET))

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        vpn_server_detail_vo = cls(
            id=id,
            name=name,
            status=status,
            vpn_type=vpn_type,
            wans=wans,
            service_port=service_port,
            custom_server=custom_server,
            custom_server_address=custom_server_address,
            ip_pool_type=ip_pool_type,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            ip_pool=ip_pool,
            mtu=mtu,
            keep_alive=keep_alive,
            private_key=private_key,
            public_key=public_key,
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
            service_type=service_type,
            remote_ip=remote_ip,
            encryption=encryption,
            pre_shared_key=pre_shared_key,
            advanced_setting=advanced_setting,
            ldap_profile=ldap_profile,
            ldap_setting=ldap_setting,
            radius_setting=radius_setting,
            name_lock_setting=name_lock_setting,
            ip_lock_setting=ip_lock_setting,
            exit_at_idle=exit_at_idle,
            exit_time=exit_time,
            total_traffic=total_traffic,
            vpn_user_list=vpn_user_list,
            feature_description=feature_description,
        )

        vpn_server_detail_vo.additional_properties = d
        return vpn_server_detail_vo

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
