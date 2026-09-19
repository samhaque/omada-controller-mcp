from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO
    from ..models.i_psec_failover_setting_open_api_vo import (
        IPsecFailoverSettingOpenApiVO,
    )
    from ..models.ip_subnets_vo import IPSubnetsVO
    from ..models.site_to_site_manual_wg_peer_config_vo import (
        SiteToSiteManualWgPeerConfigVO,
    )
    from ..models.vpn_advanced_setting_open_api_vo import VpnAdvancedSettingOpenApiVO


T = TypeVar("T", bound="VpnSiteToSiteDetailOpenApiVO")


@_attrs_define
class VpnSiteToSiteDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): ID of the VPN.
        name (str | Unset): VPN name.
        status (bool | Unset): Status of the VPN.
        vpn_type (int | Unset): Server Vpn type. 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN; 4: WireGuard; 5: SSL VPN.
        site_vpn_type (int | Unset): Site VPN type of the VPN. 0: Auto; 1: Manual.
        remote_site (str | Unset): Remote site of the VPN.
        remote_site_name (str | Unset): Remote site name of the VPN.
        mtu (int | Unset): The MTU of WireGuard VPN should be within the range of 576-1440.
        tunnel_ip (str | Unset): IP address.
        private_key (str | Unset): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        public_key (str | Unset): The public key of WireGuard VPN must have 44 character of base64 and end with '='.
        service_port (int | Unset): Service port for VPN.
        wans (list[str] | Unset): WAN list of the VPN, only for Manual IPSec type. WAN port ID can be obtained from 'Get
            internet basic info' interface.
        failover_setting (IPsecFailoverSettingOpenApiVO | Unset): Setting of the IPSec failover.
        remote_ip (str | Unset): Remote IP of the VPN.
        remote_subnet (list[str] | Unset): Remote subnet of the VPN.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[IPSubnetsVO] | Unset): Custom networks of the VPN.
        advanced_setting (VpnAdvancedSettingOpenApiVO | Unset): Advanced setting list of the VPN, only for IPSec type.
        peers (list[SiteToSiteManualWgPeerConfigVO] | Unset): List of Site-To-Site manual WireGuard peer Configuration.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    vpn_type: int | Unset = UNSET
    site_vpn_type: int | Unset = UNSET
    remote_site: str | Unset = UNSET
    remote_site_name: str | Unset = UNSET
    mtu: int | Unset = UNSET
    tunnel_ip: str | Unset = UNSET
    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    service_port: int | Unset = UNSET
    wans: list[str] | Unset = UNSET
    failover_setting: IPsecFailoverSettingOpenApiVO | Unset = UNSET
    remote_ip: str | Unset = UNSET
    remote_subnet: list[str] | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[IPSubnetsVO] | Unset = UNSET
    advanced_setting: VpnAdvancedSettingOpenApiVO | Unset = UNSET
    peers: list[SiteToSiteManualWgPeerConfigVO] | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        site_vpn_type = self.site_vpn_type

        remote_site = self.remote_site

        remote_site_name = self.remote_site_name

        mtu = self.mtu

        tunnel_ip = self.tunnel_ip

        private_key = self.private_key

        public_key = self.public_key

        service_port = self.service_port

        wans: list[str] | Unset = UNSET
        if not isinstance(self.wans, Unset):
            wans = self.wans

        failover_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failover_setting, Unset):
            failover_setting = self.failover_setting.to_dict()

        remote_ip = self.remote_ip

        remote_subnet: list[str] | Unset = UNSET
        if not isinstance(self.remote_subnet, Unset):
            remote_subnet = self.remote_subnet

        pre_shared_key = self.pre_shared_key

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

        advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_setting, Unset):
            advanced_setting = self.advanced_setting.to_dict()

        peers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.peers, Unset):
            peers = []
            for peers_item_data in self.peers:
                peers_item = peers_item_data.to_dict()
                peers.append(peers_item)

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
        if site_vpn_type is not UNSET:
            field_dict["siteVpnType"] = site_vpn_type
        if remote_site is not UNSET:
            field_dict["remoteSite"] = remote_site
        if remote_site_name is not UNSET:
            field_dict["remoteSiteName"] = remote_site_name
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if tunnel_ip is not UNSET:
            field_dict["tunnelIp"] = tunnel_ip
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if wans is not UNSET:
            field_dict["wans"] = wans
        if failover_setting is not UNSET:
            field_dict["failoverSetting"] = failover_setting
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if advanced_setting is not UNSET:
            field_dict["advancedSetting"] = advanced_setting
        if peers is not UNSET:
            field_dict["peers"] = peers
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO
        from ..models.i_psec_failover_setting_open_api_vo import (
            IPsecFailoverSettingOpenApiVO,
        )
        from ..models.ip_subnets_vo import IPSubnetsVO
        from ..models.site_to_site_manual_wg_peer_config_vo import (
            SiteToSiteManualWgPeerConfigVO,
        )
        from ..models.vpn_advanced_setting_open_api_vo import (
            VpnAdvancedSettingOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        site_vpn_type = d.pop("siteVpnType", UNSET)

        remote_site = d.pop("remoteSite", UNSET)

        remote_site_name = d.pop("remoteSiteName", UNSET)

        mtu = d.pop("mtu", UNSET)

        tunnel_ip = d.pop("tunnelIp", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        service_port = d.pop("servicePort", UNSET)

        wans = cast(list[str], d.pop("wans", UNSET))

        _failover_setting = d.pop("failoverSetting", UNSET)
        failover_setting: IPsecFailoverSettingOpenApiVO | Unset
        if isinstance(_failover_setting, Unset):
            failover_setting = UNSET
        else:
            failover_setting = IPsecFailoverSettingOpenApiVO.from_dict(
                _failover_setting
            )

        remote_ip = d.pop("remoteIp", UNSET)

        remote_subnet = cast(list[str], d.pop("remoteSubnet", UNSET))

        pre_shared_key = d.pop("preSharedKey", UNSET)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(list[str], d.pop("networkList", UNSET))

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[IPSubnetsVO] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = IPSubnetsVO.from_dict(custom_network_item_data)

                custom_network.append(custom_network_item)

        _advanced_setting = d.pop("advancedSetting", UNSET)
        advanced_setting: VpnAdvancedSettingOpenApiVO | Unset
        if isinstance(_advanced_setting, Unset):
            advanced_setting = UNSET
        else:
            advanced_setting = VpnAdvancedSettingOpenApiVO.from_dict(_advanced_setting)

        _peers = d.pop("peers", UNSET)
        peers: list[SiteToSiteManualWgPeerConfigVO] | Unset = UNSET
        if _peers is not UNSET:
            peers = []
            for peers_item_data in _peers:
                peers_item = SiteToSiteManualWgPeerConfigVO.from_dict(peers_item_data)

                peers.append(peers_item)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        vpn_site_to_site_detail_open_api_vo = cls(
            id=id,
            name=name,
            status=status,
            vpn_type=vpn_type,
            site_vpn_type=site_vpn_type,
            remote_site=remote_site,
            remote_site_name=remote_site_name,
            mtu=mtu,
            tunnel_ip=tunnel_ip,
            private_key=private_key,
            public_key=public_key,
            service_port=service_port,
            wans=wans,
            failover_setting=failover_setting,
            remote_ip=remote_ip,
            remote_subnet=remote_subnet,
            pre_shared_key=pre_shared_key,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            advanced_setting=advanced_setting,
            peers=peers,
            feature_description=feature_description,
        )

        vpn_site_to_site_detail_open_api_vo.additional_properties = d
        return vpn_site_to_site_detail_open_api_vo

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
