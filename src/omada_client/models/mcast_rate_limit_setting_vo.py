from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="McastRateLimitSettingVO")


@_attrs_define
class McastRateLimitSettingVO:
    """
    Attributes:
        enable (bool | Unset): Parameter [enable] indicates whether to enable the multicast rate limiting function.
            True: on, false: off
        arp_enable (bool | Unset): Whether to enable ARP.
        arp_pps (int | Unset): Parameter [arpPps] indicates the number of ARP packets allowed to pass per second.
        nd_enable (bool | Unset): Whether to enable ND.
        nd_pps (int | Unset): Parameter [ndPps] indicates the number of ND packets allowed to pass per second.
        igmp_enable (bool | Unset): Whether to enable IGMP.
        igmp_pps (int | Unset): Parameter [igmpPps] indicates the number of IGMP packets allowed to pass per second.
        dhcp_enable (bool | Unset): Whether to enable DHCP.
        dhcp_pps (int | Unset): Parameter [dhcpPps] indicates the number of DHCP packets allowed to pass per second.
        dhcpv_6_enable (bool | Unset): Whether to enable DHCP v6.
        dhcpv_6_pps (int | Unset): Parameter [dhcpv6Pps] indicates the number of DHCP v6 packets allowed to pass per
            second.
        mdns_enable (bool | Unset): Whether to enable MDNS.
        mdns_pps (int | Unset): Parameter [mdnsPps] indicates the number of MDNS packets allowed to pass per second.
        other_bcast_enable (bool | Unset): Whether to enable OTHER BROADCAST.
        other_bcast_pps (int | Unset): Parameter [otherBcastPps] indicates the number of OTHER BROADCAST packets allowed
            to pass per second.
        other_mcast_enable (bool | Unset): Whether to enable OTHER MULTICAST.
        other_mcast_pps (int | Unset): Parameter [otherMcastPps] indicates the number of OTHER MULTICAST packets allowed
            to pass per second.
    """

    enable: bool | Unset = UNSET
    arp_enable: bool | Unset = UNSET
    arp_pps: int | Unset = UNSET
    nd_enable: bool | Unset = UNSET
    nd_pps: int | Unset = UNSET
    igmp_enable: bool | Unset = UNSET
    igmp_pps: int | Unset = UNSET
    dhcp_enable: bool | Unset = UNSET
    dhcp_pps: int | Unset = UNSET
    dhcpv_6_enable: bool | Unset = UNSET
    dhcpv_6_pps: int | Unset = UNSET
    mdns_enable: bool | Unset = UNSET
    mdns_pps: int | Unset = UNSET
    other_bcast_enable: bool | Unset = UNSET
    other_bcast_pps: int | Unset = UNSET
    other_mcast_enable: bool | Unset = UNSET
    other_mcast_pps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        arp_enable = self.arp_enable

        arp_pps = self.arp_pps

        nd_enable = self.nd_enable

        nd_pps = self.nd_pps

        igmp_enable = self.igmp_enable

        igmp_pps = self.igmp_pps

        dhcp_enable = self.dhcp_enable

        dhcp_pps = self.dhcp_pps

        dhcpv_6_enable = self.dhcpv_6_enable

        dhcpv_6_pps = self.dhcpv_6_pps

        mdns_enable = self.mdns_enable

        mdns_pps = self.mdns_pps

        other_bcast_enable = self.other_bcast_enable

        other_bcast_pps = self.other_bcast_pps

        other_mcast_enable = self.other_mcast_enable

        other_mcast_pps = self.other_mcast_pps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if arp_enable is not UNSET:
            field_dict["arpEnable"] = arp_enable
        if arp_pps is not UNSET:
            field_dict["arpPps"] = arp_pps
        if nd_enable is not UNSET:
            field_dict["ndEnable"] = nd_enable
        if nd_pps is not UNSET:
            field_dict["ndPps"] = nd_pps
        if igmp_enable is not UNSET:
            field_dict["igmpEnable"] = igmp_enable
        if igmp_pps is not UNSET:
            field_dict["igmpPps"] = igmp_pps
        if dhcp_enable is not UNSET:
            field_dict["dhcpEnable"] = dhcp_enable
        if dhcp_pps is not UNSET:
            field_dict["dhcpPps"] = dhcp_pps
        if dhcpv_6_enable is not UNSET:
            field_dict["dhcpv6Enable"] = dhcpv_6_enable
        if dhcpv_6_pps is not UNSET:
            field_dict["dhcpv6Pps"] = dhcpv_6_pps
        if mdns_enable is not UNSET:
            field_dict["mdnsEnable"] = mdns_enable
        if mdns_pps is not UNSET:
            field_dict["mdnsPps"] = mdns_pps
        if other_bcast_enable is not UNSET:
            field_dict["otherBcastEnable"] = other_bcast_enable
        if other_bcast_pps is not UNSET:
            field_dict["otherBcastPps"] = other_bcast_pps
        if other_mcast_enable is not UNSET:
            field_dict["otherMcastEnable"] = other_mcast_enable
        if other_mcast_pps is not UNSET:
            field_dict["otherMcastPps"] = other_mcast_pps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        arp_enable = d.pop("arpEnable", UNSET)

        arp_pps = d.pop("arpPps", UNSET)

        nd_enable = d.pop("ndEnable", UNSET)

        nd_pps = d.pop("ndPps", UNSET)

        igmp_enable = d.pop("igmpEnable", UNSET)

        igmp_pps = d.pop("igmpPps", UNSET)

        dhcp_enable = d.pop("dhcpEnable", UNSET)

        dhcp_pps = d.pop("dhcpPps", UNSET)

        dhcpv_6_enable = d.pop("dhcpv6Enable", UNSET)

        dhcpv_6_pps = d.pop("dhcpv6Pps", UNSET)

        mdns_enable = d.pop("mdnsEnable", UNSET)

        mdns_pps = d.pop("mdnsPps", UNSET)

        other_bcast_enable = d.pop("otherBcastEnable", UNSET)

        other_bcast_pps = d.pop("otherBcastPps", UNSET)

        other_mcast_enable = d.pop("otherMcastEnable", UNSET)

        other_mcast_pps = d.pop("otherMcastPps", UNSET)

        mcast_rate_limit_setting_vo = cls(
            enable=enable,
            arp_enable=arp_enable,
            arp_pps=arp_pps,
            nd_enable=nd_enable,
            nd_pps=nd_pps,
            igmp_enable=igmp_enable,
            igmp_pps=igmp_pps,
            dhcp_enable=dhcp_enable,
            dhcp_pps=dhcp_pps,
            dhcpv_6_enable=dhcpv_6_enable,
            dhcpv_6_pps=dhcpv_6_pps,
            mdns_enable=mdns_enable,
            mdns_pps=mdns_pps,
            other_bcast_enable=other_bcast_enable,
            other_bcast_pps=other_bcast_pps,
            other_mcast_enable=other_mcast_enable,
            other_mcast_pps=other_mcast_pps,
        )

        mcast_rate_limit_setting_vo.additional_properties = d
        return mcast_rate_limit_setting_vo

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
