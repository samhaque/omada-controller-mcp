from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_query_open_api_v3vo import LanNetworkQueryOpenApiV3VO


T = TypeVar("T", bound="LanNetworkOpenApiV3GridVOLanNetworkQueryOpenApiV3VO")


@_attrs_define
class LanNetworkOpenApiV3GridVOLanNetworkQueryOpenApiV3VO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[LanNetworkQueryOpenApiV3VO] | Unset):
        support_multi_vlan (bool | Unset): Whether multi vlan configuration is supported of the lan netowrk.
        support_ra (bool | Unset): Whether Router Advertisement configuration is supported of the lan netowrk.
        support_custom_dhcp_option (bool | Unset): Whether custom DHCP option configuration is supported of the lan
            netowrk.
        combined_gateway (bool | Unset): Whether the current site is combined gateway
        dhcp_range_pool_size (int | Unset): The size of DHCP range pool supported by the lan network DHCP.
        interface_num (int | Unset): The number of interface supported by current gateway.
        support_default (bool | Unset): Whether to allow the selection of Default VLAN.
        osg_support_igmp_snooping (list[str] | Unset): The name of the model that supports IgmpSnooping under site.
        support_dhcp_next_server (bool | Unset): Whether DHCP Next Server is supported of the lan network.
        vlan_nums (int | Unset): The vlan num of the site.
        support_arp_detection (bool | Unset): Whether ARP Detection is supported of the lan network.
        support_network_isolation (bool | Unset): Whether it supports isolate network.
        support_lan_ipv_6 (bool | Unset): Whether it supports lan Ipv6.
        support_lan_ipv_6_pass_through (bool | Unset): Whether it supports Pass Through.
        support_max_vlan_num (int | Unset): The number of vlan supported by current gateway.
        support_pd_on_dhcp (bool | Unset): Whether it supports "Get from Prefix Delegation" when disable Prefix
            Delegation on the corresponding WAN interface page.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[LanNetworkQueryOpenApiV3VO] | Unset = UNSET
    support_multi_vlan: bool | Unset = UNSET
    support_ra: bool | Unset = UNSET
    support_custom_dhcp_option: bool | Unset = UNSET
    combined_gateway: bool | Unset = UNSET
    dhcp_range_pool_size: int | Unset = UNSET
    interface_num: int | Unset = UNSET
    support_default: bool | Unset = UNSET
    osg_support_igmp_snooping: list[str] | Unset = UNSET
    support_dhcp_next_server: bool | Unset = UNSET
    vlan_nums: int | Unset = UNSET
    support_arp_detection: bool | Unset = UNSET
    support_network_isolation: bool | Unset = UNSET
    support_lan_ipv_6: bool | Unset = UNSET
    support_lan_ipv_6_pass_through: bool | Unset = UNSET
    support_max_vlan_num: int | Unset = UNSET
    support_pd_on_dhcp: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        support_multi_vlan = self.support_multi_vlan

        support_ra = self.support_ra

        support_custom_dhcp_option = self.support_custom_dhcp_option

        combined_gateway = self.combined_gateway

        dhcp_range_pool_size = self.dhcp_range_pool_size

        interface_num = self.interface_num

        support_default = self.support_default

        osg_support_igmp_snooping: list[str] | Unset = UNSET
        if not isinstance(self.osg_support_igmp_snooping, Unset):
            osg_support_igmp_snooping = self.osg_support_igmp_snooping

        support_dhcp_next_server = self.support_dhcp_next_server

        vlan_nums = self.vlan_nums

        support_arp_detection = self.support_arp_detection

        support_network_isolation = self.support_network_isolation

        support_lan_ipv_6 = self.support_lan_ipv_6

        support_lan_ipv_6_pass_through = self.support_lan_ipv_6_pass_through

        support_max_vlan_num = self.support_max_vlan_num

        support_pd_on_dhcp = self.support_pd_on_dhcp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if support_multi_vlan is not UNSET:
            field_dict["supportMultiVlan"] = support_multi_vlan
        if support_ra is not UNSET:
            field_dict["supportRA"] = support_ra
        if support_custom_dhcp_option is not UNSET:
            field_dict["supportCustomDhcpOption"] = support_custom_dhcp_option
        if combined_gateway is not UNSET:
            field_dict["combinedGateway"] = combined_gateway
        if dhcp_range_pool_size is not UNSET:
            field_dict["dhcpRangePoolSize"] = dhcp_range_pool_size
        if interface_num is not UNSET:
            field_dict["interfaceNum"] = interface_num
        if support_default is not UNSET:
            field_dict["supportDefault"] = support_default
        if osg_support_igmp_snooping is not UNSET:
            field_dict["osgSupportIgmpSnooping"] = osg_support_igmp_snooping
        if support_dhcp_next_server is not UNSET:
            field_dict["supportDhcpNextServer"] = support_dhcp_next_server
        if vlan_nums is not UNSET:
            field_dict["vlanNums"] = vlan_nums
        if support_arp_detection is not UNSET:
            field_dict["supportArpDetection"] = support_arp_detection
        if support_network_isolation is not UNSET:
            field_dict["supportNetworkIsolation"] = support_network_isolation
        if support_lan_ipv_6 is not UNSET:
            field_dict["supportLanIpv6"] = support_lan_ipv_6
        if support_lan_ipv_6_pass_through is not UNSET:
            field_dict["supportLanIpv6PassThrough"] = support_lan_ipv_6_pass_through
        if support_max_vlan_num is not UNSET:
            field_dict["supportMaxVlanNum"] = support_max_vlan_num
        if support_pd_on_dhcp is not UNSET:
            field_dict["supportPdOnDhcp"] = support_pd_on_dhcp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_query_open_api_v3vo import (
            LanNetworkQueryOpenApiV3VO,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[LanNetworkQueryOpenApiV3VO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = LanNetworkQueryOpenApiV3VO.from_dict(data_item_data)

                data.append(data_item)

        support_multi_vlan = d.pop("supportMultiVlan", UNSET)

        support_ra = d.pop("supportRA", UNSET)

        support_custom_dhcp_option = d.pop("supportCustomDhcpOption", UNSET)

        combined_gateway = d.pop("combinedGateway", UNSET)

        dhcp_range_pool_size = d.pop("dhcpRangePoolSize", UNSET)

        interface_num = d.pop("interfaceNum", UNSET)

        support_default = d.pop("supportDefault", UNSET)

        osg_support_igmp_snooping = cast(
            list[str], d.pop("osgSupportIgmpSnooping", UNSET)
        )

        support_dhcp_next_server = d.pop("supportDhcpNextServer", UNSET)

        vlan_nums = d.pop("vlanNums", UNSET)

        support_arp_detection = d.pop("supportArpDetection", UNSET)

        support_network_isolation = d.pop("supportNetworkIsolation", UNSET)

        support_lan_ipv_6 = d.pop("supportLanIpv6", UNSET)

        support_lan_ipv_6_pass_through = d.pop("supportLanIpv6PassThrough", UNSET)

        support_max_vlan_num = d.pop("supportMaxVlanNum", UNSET)

        support_pd_on_dhcp = d.pop("supportPdOnDhcp", UNSET)

        lan_network_open_api_v3_grid_vo_lan_network_query_open_api_v3vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_multi_vlan=support_multi_vlan,
            support_ra=support_ra,
            support_custom_dhcp_option=support_custom_dhcp_option,
            combined_gateway=combined_gateway,
            dhcp_range_pool_size=dhcp_range_pool_size,
            interface_num=interface_num,
            support_default=support_default,
            osg_support_igmp_snooping=osg_support_igmp_snooping,
            support_dhcp_next_server=support_dhcp_next_server,
            vlan_nums=vlan_nums,
            support_arp_detection=support_arp_detection,
            support_network_isolation=support_network_isolation,
            support_lan_ipv_6=support_lan_ipv_6,
            support_lan_ipv_6_pass_through=support_lan_ipv_6_pass_through,
            support_max_vlan_num=support_max_vlan_num,
            support_pd_on_dhcp=support_pd_on_dhcp,
        )

        lan_network_open_api_v3_grid_vo_lan_network_query_open_api_v3vo.additional_properties = d
        return lan_network_open_api_v3_grid_vo_lan_network_query_open_api_v3vo

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
