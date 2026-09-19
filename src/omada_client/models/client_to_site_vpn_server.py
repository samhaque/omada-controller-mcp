from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO
    from ..models.vpn_advanced_setting_open_api_vo import VpnAdvancedSettingOpenApiVO


T = TypeVar("T", bound="ClientToSiteVpnServer")


@_attrs_define
class ClientToSiteVpnServer:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        wan (list[str]): WAN list of the VPN. WAN port ID can be obtained from 'Get internet basic info' interface.
        client_vpn_type (int): Client Vpn type should be a value as follows: 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN.
        ip_pool (IPSubnetsVO): User remote subnets of the VPN user.
        id (str | Unset): ID of the VPN.
        status (bool | Unset): Status of the VPN.
        account_password (bool | Unset): Account password of the VPN, only for server OpenVPN.
        tunnel_mode (int | Unset): Tunnel mode(only for server OpenVPN)should be a value as follows: 0: split; 1: full.
        open_vpn_mode (int | Unset): OpenVPN mode should be a value as follows: 0: certification; 1:
            certification+account.
        remote_ip (str | Unset): Remote IP of the VPN
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[IPSubnetsVO] | Unset): Custom networks of the VPN.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        encryption (int | Unset): Encryption should be a value as follows: 0: Encrypted; 1: Unencrypted.
        ip_pool_type (int | Unset): IP pool type should be a value as follows: 0: Ip Address/Mask; 1: Ip Address Range.
        ip_pool_start (str | Unset): The start IP of the IP pool.
        ip_pool_end (str | Unset): The end IP of the IP pool.
        primary_dns (str | Unset): Primary DNS of the VPN.
        secondary_dns (str | Unset): Secondary DNS of the VPN.
        service_type (int | Unset): Service type of the VPN.
        service_port (int | Unset): Service port should be within the range of 1–65535.
        auth_mode (int | Unset): Authentication mode should be a value as follows: 0: Local; 1: LDAP.
        advanced_setting (VpnAdvancedSettingOpenApiVO | Unset): Advanced setting list of the VPN, only for IPSec type.
    """

    name: str
    wan: list[str]
    client_vpn_type: int
    ip_pool: IPSubnetsVO
    id: str | Unset = UNSET
    status: bool | Unset = UNSET
    account_password: bool | Unset = UNSET
    tunnel_mode: int | Unset = UNSET
    open_vpn_mode: int | Unset = UNSET
    remote_ip: str | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[IPSubnetsVO] | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    encryption: int | Unset = UNSET
    ip_pool_type: int | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    service_type: int | Unset = UNSET
    service_port: int | Unset = UNSET
    auth_mode: int | Unset = UNSET
    advanced_setting: VpnAdvancedSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        wan = self.wan

        client_vpn_type = self.client_vpn_type

        ip_pool = self.ip_pool.to_dict()

        id = self.id

        status = self.status

        account_password = self.account_password

        tunnel_mode = self.tunnel_mode

        open_vpn_mode = self.open_vpn_mode

        remote_ip = self.remote_ip

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

        pre_shared_key = self.pre_shared_key

        encryption = self.encryption

        ip_pool_type = self.ip_pool_type

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        service_type = self.service_type

        service_port = self.service_port

        auth_mode = self.auth_mode

        advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_setting, Unset):
            advanced_setting = self.advanced_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "wan": wan,
                "clientVpnType": client_vpn_type,
                "ipPool": ip_pool,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if account_password is not UNSET:
            field_dict["accountPassword"] = account_password
        if tunnel_mode is not UNSET:
            field_dict["tunnelMode"] = tunnel_mode
        if open_vpn_mode is not UNSET:
            field_dict["openVpnMode"] = open_vpn_mode
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if ip_pool_type is not UNSET:
            field_dict["ipPoolType"] = ip_pool_type
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if advanced_setting is not UNSET:
            field_dict["advancedSetting"] = advanced_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_vo import IPSubnetsVO
        from ..models.vpn_advanced_setting_open_api_vo import (
            VpnAdvancedSettingOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        wan = cast(list[str], d.pop("wan"))

        client_vpn_type = d.pop("clientVpnType")

        ip_pool = IPSubnetsVO.from_dict(d.pop("ipPool"))

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        account_password = d.pop("accountPassword", UNSET)

        tunnel_mode = d.pop("tunnelMode", UNSET)

        open_vpn_mode = d.pop("openVpnMode", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(list[str], d.pop("networkList", UNSET))

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[IPSubnetsVO] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = IPSubnetsVO.from_dict(custom_network_item_data)

                custom_network.append(custom_network_item)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        encryption = d.pop("encryption", UNSET)

        ip_pool_type = d.pop("ipPoolType", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        service_type = d.pop("serviceType", UNSET)

        service_port = d.pop("servicePort", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        _advanced_setting = d.pop("advancedSetting", UNSET)
        advanced_setting: VpnAdvancedSettingOpenApiVO | Unset
        if isinstance(_advanced_setting, Unset):
            advanced_setting = UNSET
        else:
            advanced_setting = VpnAdvancedSettingOpenApiVO.from_dict(_advanced_setting)

        client_to_site_vpn_server = cls(
            name=name,
            wan=wan,
            client_vpn_type=client_vpn_type,
            ip_pool=ip_pool,
            id=id,
            status=status,
            account_password=account_password,
            tunnel_mode=tunnel_mode,
            open_vpn_mode=open_vpn_mode,
            remote_ip=remote_ip,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            pre_shared_key=pre_shared_key,
            encryption=encryption,
            ip_pool_type=ip_pool_type,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            service_type=service_type,
            service_port=service_port,
            auth_mode=auth_mode,
            advanced_setting=advanced_setting,
        )

        client_to_site_vpn_server.additional_properties = d
        return client_to_site_vpn_server

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
