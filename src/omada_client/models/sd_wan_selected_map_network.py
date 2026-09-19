from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_lan_network_nat_req import SdWanLanNetworkNatReq
    from ..models.sd_wan_member_selected import SdWanMemberSelected


T = TypeVar("T", bound="SdWanSelectedMapNetwork")


@_attrs_define
class SdWanSelectedMapNetwork:
    """
    Attributes:
        lan_networks (list[SdWanLanNetworkNatReq] | Unset): A list of original lan network
        custom_network (list[SdWanLanNetworkNatReq] | Unset): A list of original custom route
        map_network_list (list[str] | Unset): A list of map network range
        member_list (list[SdWanMemberSelected] | Unset): A list of members of the SD-WAN group
        group_id (str | Unset): The SD-WAN group ID.
    """

    lan_networks: list[SdWanLanNetworkNatReq] | Unset = UNSET
    custom_network: list[SdWanLanNetworkNatReq] | Unset = UNSET
    map_network_list: list[str] | Unset = UNSET
    member_list: list[SdWanMemberSelected] | Unset = UNSET
    group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_networks, Unset):
            lan_networks = []
            for lan_networks_item_data in self.lan_networks:
                lan_networks_item = lan_networks_item_data.to_dict()
                lan_networks.append(lan_networks_item)

        custom_network: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_network, Unset):
            custom_network = []
            for custom_network_item_data in self.custom_network:
                custom_network_item = custom_network_item_data.to_dict()
                custom_network.append(custom_network_item)

        map_network_list: list[str] | Unset = UNSET
        if not isinstance(self.map_network_list, Unset):
            map_network_list = self.map_network_list

        member_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member_list, Unset):
            member_list = []
            for member_list_item_data in self.member_list:
                member_list_item = member_list_item_data.to_dict()
                member_list.append(member_list_item)

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_networks is not UNSET:
            field_dict["lanNetworks"] = lan_networks
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if map_network_list is not UNSET:
            field_dict["mapNetworkList"] = map_network_list
        if member_list is not UNSET:
            field_dict["memberList"] = member_list
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_lan_network_nat_req import (
            SdWanLanNetworkNatReq,
        )
        from ..models.sd_wan_member_selected import SdWanMemberSelected

        d = dict(src_dict)
        _lan_networks = d.pop("lanNetworks", UNSET)
        lan_networks: list[SdWanLanNetworkNatReq] | Unset = UNSET
        if _lan_networks is not UNSET:
            lan_networks = []
            for lan_networks_item_data in _lan_networks:
                lan_networks_item = SdWanLanNetworkNatReq.from_dict(
                    lan_networks_item_data
                )

                lan_networks.append(lan_networks_item)

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[SdWanLanNetworkNatReq] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = SdWanLanNetworkNatReq.from_dict(
                    custom_network_item_data
                )

                custom_network.append(custom_network_item)

        map_network_list = cast(list[str], d.pop("mapNetworkList", UNSET))

        _member_list = d.pop("memberList", UNSET)
        member_list: list[SdWanMemberSelected] | Unset = UNSET
        if _member_list is not UNSET:
            member_list = []
            for member_list_item_data in _member_list:
                member_list_item = SdWanMemberSelected.from_dict(member_list_item_data)

                member_list.append(member_list_item)

        group_id = d.pop("groupId", UNSET)

        sd_wan_selected_map_network = cls(
            lan_networks=lan_networks,
            custom_network=custom_network,
            map_network_list=map_network_list,
            member_list=member_list,
            group_id=group_id,
        )

        sd_wan_selected_map_network.additional_properties = d
        return sd_wan_selected_map_network

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
