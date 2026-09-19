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


T = TypeVar("T", bound="SiteToSiteVpn")


@_attrs_define
class SiteToSiteVpn:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        site_vpn_type (int): Site VPN type should be a value as follows: 0: Auto IPSec; 1: Manual IPSec.
        status (bool): Status of the VPN.
        id (str | Unset): ID of the VPN.
        remote_site (str | Unset): Remote site of the VPN, only for Auto IPSec type.
        remote_ip (str | Unset): Remote IP of the VPN, only for Manual IPSec type.
        remote_subnet (list[IPSubnetsVO] | Unset): Remote subnet of the VPN, only for Manual IPSec type.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN, only for Manual IPSec type. Network can be created
            using 'Create LAN network' interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[IPSubnetsVO] | Unset): Custom networks of the VPN, only for Manual IPSec type.
        pre_shared_key (str | Unset): Pre-shared key of the VPN, only for Manual IPSec type.
        wan (list[str] | Unset): WAN list of the VPN, only for Manual IPSec type. WAN port ID can be obtained from 'Get
            internet basic info' interface.
        advanced_setting (VpnAdvancedSettingOpenApiVO | Unset): Advanced setting list of the VPN, only for IPSec type.
    """

    name: str
    site_vpn_type: int
    status: bool
    id: str | Unset = UNSET
    remote_site: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    remote_subnet: list[IPSubnetsVO] | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[IPSubnetsVO] | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    wan: list[str] | Unset = UNSET
    advanced_setting: VpnAdvancedSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        site_vpn_type = self.site_vpn_type

        status = self.status

        id = self.id

        remote_site = self.remote_site

        remote_ip = self.remote_ip

        remote_subnet: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remote_subnet, Unset):
            remote_subnet = []
            for remote_subnet_item_data in self.remote_subnet:
                remote_subnet_item = remote_subnet_item_data.to_dict()
                remote_subnet.append(remote_subnet_item)

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

        wan: list[str] | Unset = UNSET
        if not isinstance(self.wan, Unset):
            wan = self.wan

        advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_setting, Unset):
            advanced_setting = self.advanced_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "siteVpnType": site_vpn_type,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if remote_site is not UNSET:
            field_dict["remoteSite"] = remote_site
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if wan is not UNSET:
            field_dict["wan"] = wan
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

        site_vpn_type = d.pop("siteVpnType")

        status = d.pop("status")

        id = d.pop("id", UNSET)

        remote_site = d.pop("remoteSite", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        _remote_subnet = d.pop("remoteSubnet", UNSET)
        remote_subnet: list[IPSubnetsVO] | Unset = UNSET
        if _remote_subnet is not UNSET:
            remote_subnet = []
            for remote_subnet_item_data in _remote_subnet:
                remote_subnet_item = IPSubnetsVO.from_dict(remote_subnet_item_data)

                remote_subnet.append(remote_subnet_item)

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

        wan = cast(list[str], d.pop("wan", UNSET))

        _advanced_setting = d.pop("advancedSetting", UNSET)
        advanced_setting: VpnAdvancedSettingOpenApiVO | Unset
        if isinstance(_advanced_setting, Unset):
            advanced_setting = UNSET
        else:
            advanced_setting = VpnAdvancedSettingOpenApiVO.from_dict(_advanced_setting)

        site_to_site_vpn = cls(
            name=name,
            site_vpn_type=site_vpn_type,
            status=status,
            id=id,
            remote_site=remote_site,
            remote_ip=remote_ip,
            remote_subnet=remote_subnet,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            pre_shared_key=pre_shared_key,
            wan=wan,
            advanced_setting=advanced_setting,
        )

        site_to_site_vpn.additional_properties = d
        return site_to_site_vpn

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
