from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wired_port_v3dto import WiredPortV3DTO


T = TypeVar("T", bound="TopologyOpenApiEdgeVO")


@_attrs_define
class TopologyOpenApiEdgeVO:
    """Topology Edges

    Attributes:
        up_link_mac (str | Unset): UpLink Mac
        down_link_mac (str | Unset): DownLink Mac
        blocked_vlans (str | Unset): Blocked Vlans
        blocked_type (int | Unset): Blocked Type
        blocked (bool | Unset): Blocked Or Not
        remain_block_num (int | Unset): Remain Block Num
        up_link_port (WiredPortV3DTO | Unset): Downlink Port
        port (WiredPortV3DTO | Unset): Downlink Port
        remain_blocked_port_list (list[TopologyOpenApiEdgeVO] | Unset): Remain Blocked PortList
    """

    up_link_mac: str | Unset = UNSET
    down_link_mac: str | Unset = UNSET
    blocked_vlans: str | Unset = UNSET
    blocked_type: int | Unset = UNSET
    blocked: bool | Unset = UNSET
    remain_block_num: int | Unset = UNSET
    up_link_port: WiredPortV3DTO | Unset = UNSET
    port: WiredPortV3DTO | Unset = UNSET
    remain_blocked_port_list: list[TopologyOpenApiEdgeVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up_link_mac = self.up_link_mac

        down_link_mac = self.down_link_mac

        blocked_vlans = self.blocked_vlans

        blocked_type = self.blocked_type

        blocked = self.blocked

        remain_block_num = self.remain_block_num

        up_link_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_link_port, Unset):
            up_link_port = self.up_link_port.to_dict()

        port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        remain_blocked_port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remain_blocked_port_list, Unset):
            remain_blocked_port_list = []
            for remain_blocked_port_list_item_data in self.remain_blocked_port_list:
                remain_blocked_port_list_item = (
                    remain_blocked_port_list_item_data.to_dict()
                )
                remain_blocked_port_list.append(remain_blocked_port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if up_link_mac is not UNSET:
            field_dict["upLinkMac"] = up_link_mac
        if down_link_mac is not UNSET:
            field_dict["downLinkMac"] = down_link_mac
        if blocked_vlans is not UNSET:
            field_dict["blockedVlans"] = blocked_vlans
        if blocked_type is not UNSET:
            field_dict["blockedType"] = blocked_type
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if remain_block_num is not UNSET:
            field_dict["remainBlockNum"] = remain_block_num
        if up_link_port is not UNSET:
            field_dict["upLinkPort"] = up_link_port
        if port is not UNSET:
            field_dict["port"] = port
        if remain_blocked_port_list is not UNSET:
            field_dict["remainBlockedPortList"] = remain_blocked_port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wired_port_v3dto import WiredPortV3DTO

        d = dict(src_dict)
        up_link_mac = d.pop("upLinkMac", UNSET)

        down_link_mac = d.pop("downLinkMac", UNSET)

        blocked_vlans = d.pop("blockedVlans", UNSET)

        blocked_type = d.pop("blockedType", UNSET)

        blocked = d.pop("blocked", UNSET)

        remain_block_num = d.pop("remainBlockNum", UNSET)

        _up_link_port = d.pop("upLinkPort", UNSET)
        up_link_port: WiredPortV3DTO | Unset
        if isinstance(_up_link_port, Unset):
            up_link_port = UNSET
        else:
            up_link_port = WiredPortV3DTO.from_dict(_up_link_port)

        _port = d.pop("port", UNSET)
        port: WiredPortV3DTO | Unset
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = WiredPortV3DTO.from_dict(_port)

        _remain_blocked_port_list = d.pop("remainBlockedPortList", UNSET)
        remain_blocked_port_list: list[TopologyOpenApiEdgeVO] | Unset = UNSET
        if _remain_blocked_port_list is not UNSET:
            remain_blocked_port_list = []
            for remain_blocked_port_list_item_data in _remain_blocked_port_list:
                remain_blocked_port_list_item = TopologyOpenApiEdgeVO.from_dict(
                    remain_blocked_port_list_item_data
                )

                remain_blocked_port_list.append(remain_blocked_port_list_item)

        topology_open_api_edge_vo = cls(
            up_link_mac=up_link_mac,
            down_link_mac=down_link_mac,
            blocked_vlans=blocked_vlans,
            blocked_type=blocked_type,
            blocked=blocked,
            remain_block_num=remain_block_num,
            up_link_port=up_link_port,
            port=port,
            remain_blocked_port_list=remain_blocked_port_list,
        )

        topology_open_api_edge_vo.additional_properties = d
        return topology_open_api_edge_vo

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
