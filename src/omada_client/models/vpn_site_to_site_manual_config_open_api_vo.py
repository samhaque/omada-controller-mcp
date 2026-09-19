from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_psec_failover_setting_open_api_vo import (
        IPsecFailoverSettingOpenApiVO,
    )
    from ..models.site_to_site_manual_wg_peer_config_vo import (
        SiteToSiteManualWgPeerConfigVO,
    )
    from ..models.vpn_advanced_setting_open_api_vo import VpnAdvancedSettingOpenApiVO
    from ..models.vpn_ip_subnets_open_api_vo import VpnIPSubnetsOpenApiVO


T = TypeVar("T", bound="VpnSiteToSiteManualConfigOpenApiVO")


@_attrs_define
class VpnSiteToSiteManualConfigOpenApiVO:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        status (bool): Status of the VPN.
        vpn_type (int): Vpn type should be a value as follows: 2: IPSec; 4: WireGuard.
        mtu (int): The MTU of WireGuard VPN should be within the range of 576-1440.
        service_port (int): Service port should be within the range of 1–65535.
        tunnel_ip (str): IP address.
        private_key (str): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        wans (list[str]): WAN list of the VPN, only for Manual IPSec type. WAN port ID can be obtained from 'Get
            internet basic info' interface.
        remote_ip (str): Remote IP of the VPN.
        remote_subnet (list[str]): Remote subnet of the VPN.
        pre_shared_key (str): Pre-shared key of the VPN.
        advanced_setting (VpnAdvancedSettingOpenApiVO): Advanced setting list of the VPN, only for IPSec type.
        peers (list[SiteToSiteManualWgPeerConfigVO] | Unset): List of Site-To-Site manual WireGuard peer Configuration.
        failover_setting (IPsecFailoverSettingOpenApiVO | Unset): Setting of the IPSec failover.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[VpnIPSubnetsOpenApiVO] | Unset): Custom networks of the VPN.
        exist_custom_network (bool | Unset): Whether Local Network Type is Custom.
    """

    name: str
    status: bool
    vpn_type: int
    mtu: int
    service_port: int
    tunnel_ip: str
    private_key: str
    wans: list[str]
    remote_ip: str
    remote_subnet: list[str]
    pre_shared_key: str
    advanced_setting: VpnAdvancedSettingOpenApiVO
    peers: list[SiteToSiteManualWgPeerConfigVO] | Unset = UNSET
    failover_setting: IPsecFailoverSettingOpenApiVO | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
    exist_custom_network: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        mtu = self.mtu

        service_port = self.service_port

        tunnel_ip = self.tunnel_ip

        private_key = self.private_key

        wans = self.wans

        remote_ip = self.remote_ip

        remote_subnet = self.remote_subnet

        pre_shared_key = self.pre_shared_key

        advanced_setting = self.advanced_setting.to_dict()

        peers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.peers, Unset):
            peers = []
            for peers_item_data in self.peers:
                peers_item = peers_item_data.to_dict()
                peers.append(peers_item)

        failover_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failover_setting, Unset):
            failover_setting = self.failover_setting.to_dict()

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

        exist_custom_network = self.exist_custom_network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "vpnType": vpn_type,
                "mtu": mtu,
                "servicePort": service_port,
                "tunnelIp": tunnel_ip,
                "privateKey": private_key,
                "wans": wans,
                "remoteIp": remote_ip,
                "remoteSubnet": remote_subnet,
                "preSharedKey": pre_shared_key,
                "advancedSetting": advanced_setting,
            }
        )
        if peers is not UNSET:
            field_dict["peers"] = peers
        if failover_setting is not UNSET:
            field_dict["failoverSetting"] = failover_setting
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if exist_custom_network is not UNSET:
            field_dict["existCustomNetwork"] = exist_custom_network

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.i_psec_failover_setting_open_api_vo import (
            IPsecFailoverSettingOpenApiVO,
        )
        from ..models.site_to_site_manual_wg_peer_config_vo import (
            SiteToSiteManualWgPeerConfigVO,
        )
        from ..models.vpn_advanced_setting_open_api_vo import (
            VpnAdvancedSettingOpenApiVO,
        )
        from ..models.vpn_ip_subnets_open_api_vo import (
            VpnIPSubnetsOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        vpn_type = d.pop("vpnType")

        mtu = d.pop("mtu")

        service_port = d.pop("servicePort")

        tunnel_ip = d.pop("tunnelIp")

        private_key = d.pop("privateKey")

        wans = cast(list[str], d.pop("wans"))

        remote_ip = d.pop("remoteIp")

        remote_subnet = cast(list[str], d.pop("remoteSubnet"))

        pre_shared_key = d.pop("preSharedKey")

        advanced_setting = VpnAdvancedSettingOpenApiVO.from_dict(
            d.pop("advancedSetting")
        )

        _peers = d.pop("peers", UNSET)
        peers: list[SiteToSiteManualWgPeerConfigVO] | Unset = UNSET
        if _peers is not UNSET:
            peers = []
            for peers_item_data in _peers:
                peers_item = SiteToSiteManualWgPeerConfigVO.from_dict(peers_item_data)

                peers.append(peers_item)

        _failover_setting = d.pop("failoverSetting", UNSET)
        failover_setting: IPsecFailoverSettingOpenApiVO | Unset
        if isinstance(_failover_setting, Unset):
            failover_setting = UNSET
        else:
            failover_setting = IPsecFailoverSettingOpenApiVO.from_dict(
                _failover_setting
            )

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

        exist_custom_network = d.pop("existCustomNetwork", UNSET)

        vpn_site_to_site_manual_config_open_api_vo = cls(
            name=name,
            status=status,
            vpn_type=vpn_type,
            mtu=mtu,
            service_port=service_port,
            tunnel_ip=tunnel_ip,
            private_key=private_key,
            wans=wans,
            remote_ip=remote_ip,
            remote_subnet=remote_subnet,
            pre_shared_key=pre_shared_key,
            advanced_setting=advanced_setting,
            peers=peers,
            failover_setting=failover_setting,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            exist_custom_network=exist_custom_network,
        )

        vpn_site_to_site_manual_config_open_api_vo.additional_properties = d
        return vpn_site_to_site_manual_config_open_api_vo

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
