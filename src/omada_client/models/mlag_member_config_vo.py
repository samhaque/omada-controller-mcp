from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlagMemberConfigVO")


@_attrs_define
class MlagMemberConfigVO:
    """M-LAG group members configuration

    Attributes:
        mac (str): Device Mac.
        priority (int): Priority of the device in the M-LAG group, it must be between 1 and 255.
        dad_enable (bool): Whether the DAD enable.
        peer_link_ports (list[str]): Peer Link Ports(Required parameters)
        dad_link_ports (list[str] | Unset): DAD Link Ports(This parameter is required when DAD is enabled.)
        dad_local_ip (str | Unset): DAD Local IP
        dad_local_ipv_6 (str | Unset): DAD Local IPv6
        dad_peer_ip (str | Unset): DAD Peer IP
        dad_peer_ipv_6 (str | Unset): DAD Peer IPv6
    """

    mac: str
    priority: int
    dad_enable: bool
    peer_link_ports: list[str]
    dad_link_ports: list[str] | Unset = UNSET
    dad_local_ip: str | Unset = UNSET
    dad_local_ipv_6: str | Unset = UNSET
    dad_peer_ip: str | Unset = UNSET
    dad_peer_ipv_6: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        priority = self.priority

        dad_enable = self.dad_enable

        peer_link_ports = self.peer_link_ports

        dad_link_ports: list[str] | Unset = UNSET
        if not isinstance(self.dad_link_ports, Unset):
            dad_link_ports = self.dad_link_ports

        dad_local_ip = self.dad_local_ip

        dad_local_ipv_6 = self.dad_local_ipv_6

        dad_peer_ip = self.dad_peer_ip

        dad_peer_ipv_6 = self.dad_peer_ipv_6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "priority": priority,
                "dadEnable": dad_enable,
                "peerLinkPorts": peer_link_ports,
            }
        )
        if dad_link_ports is not UNSET:
            field_dict["dadLinkPorts"] = dad_link_ports
        if dad_local_ip is not UNSET:
            field_dict["dadLocalIp"] = dad_local_ip
        if dad_local_ipv_6 is not UNSET:
            field_dict["dadLocalIpv6"] = dad_local_ipv_6
        if dad_peer_ip is not UNSET:
            field_dict["dadPeerIp"] = dad_peer_ip
        if dad_peer_ipv_6 is not UNSET:
            field_dict["dadPeerIpv6"] = dad_peer_ipv_6

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        priority = d.pop("priority")

        dad_enable = d.pop("dadEnable")

        peer_link_ports = cast(list[str], d.pop("peerLinkPorts"))

        dad_link_ports = cast(list[str], d.pop("dadLinkPorts", UNSET))

        dad_local_ip = d.pop("dadLocalIp", UNSET)

        dad_local_ipv_6 = d.pop("dadLocalIpv6", UNSET)

        dad_peer_ip = d.pop("dadPeerIp", UNSET)

        dad_peer_ipv_6 = d.pop("dadPeerIpv6", UNSET)

        mlag_member_config_vo = cls(
            mac=mac,
            priority=priority,
            dad_enable=dad_enable,
            peer_link_ports=peer_link_ports,
            dad_link_ports=dad_link_ports,
            dad_local_ip=dad_local_ip,
            dad_local_ipv_6=dad_local_ipv_6,
            dad_peer_ip=dad_peer_ip,
            dad_peer_ipv_6=dad_peer_ipv_6,
        )

        mlag_member_config_vo.additional_properties = d
        return mlag_member_config_vo

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
