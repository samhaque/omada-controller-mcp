from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO
    from ..models.i_psec_failover_status_open_api_vo import IPsecFailoverStatusOpenApiVO
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="VpnSummaryVO")


@_attrs_define
class VpnSummaryVO:
    """
    Attributes:
        id (str | Unset): ID of the VPN.
        name (str | Unset): VPN name.
        status (bool | Unset): Status of the VPN.
        vpn_type (int | Unset): Server Vpn type. 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN; 4: WireGuard; 5: SSL VPN.
        site_vpn_type (int | Unset): Site VPN type of the VPN. 0: Auto; 1: Manual.
        wans (list[str] | Unset): WAN port ID.
        failover_setting (IPsecFailoverStatusOpenApiVO | Unset): Setting of the IPSec failover.
        network_type (int | Unset): Network type. 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN.
        custom_network (list[IPSubnetsVO] | Unset): Custom networks of the VPN.
        group_id (str | Unset): Default group ID of SSL VPN server.
        user_count (int | Unset): User number of the VPN.
        active_clients (int | Unset): Active clients number of the VPN.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    vpn_type: int | Unset = UNSET
    site_vpn_type: int | Unset = UNSET
    wans: list[str] | Unset = UNSET
    failover_setting: IPsecFailoverStatusOpenApiVO | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[IPSubnetsVO] | Unset = UNSET
    group_id: str | Unset = UNSET
    user_count: int | Unset = UNSET
    active_clients: int | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        site_vpn_type = self.site_vpn_type

        wans: list[str] | Unset = UNSET
        if not isinstance(self.wans, Unset):
            wans = self.wans

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

        group_id = self.group_id

        user_count = self.user_count

        active_clients = self.active_clients

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
        if wans is not UNSET:
            field_dict["wans"] = wans
        if failover_setting is not UNSET:
            field_dict["failoverSetting"] = failover_setting
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if active_clients is not UNSET:
            field_dict["activeClients"] = active_clients
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO
        from ..models.i_psec_failover_status_open_api_vo import (
            IPsecFailoverStatusOpenApiVO,
        )
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        site_vpn_type = d.pop("siteVpnType", UNSET)

        wans = cast(list[str], d.pop("wans", UNSET))

        _failover_setting = d.pop("failoverSetting", UNSET)
        failover_setting: IPsecFailoverStatusOpenApiVO | Unset
        if isinstance(_failover_setting, Unset):
            failover_setting = UNSET
        else:
            failover_setting = IPsecFailoverStatusOpenApiVO.from_dict(_failover_setting)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(list[str], d.pop("networkList", UNSET))

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[IPSubnetsVO] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = IPSubnetsVO.from_dict(custom_network_item_data)

                custom_network.append(custom_network_item)

        group_id = d.pop("groupId", UNSET)

        user_count = d.pop("userCount", UNSET)

        active_clients = d.pop("activeClients", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        vpn_summary_vo = cls(
            id=id,
            name=name,
            status=status,
            vpn_type=vpn_type,
            site_vpn_type=site_vpn_type,
            wans=wans,
            failover_setting=failover_setting,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            group_id=group_id,
            user_count=user_count,
            active_clients=active_clients,
            feature_description=feature_description,
        )

        vpn_summary_vo.additional_properties = d
        return vpn_summary_vo

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
