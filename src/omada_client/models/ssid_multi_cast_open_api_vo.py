from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidMultiCastOpenApiVO")


@_attrs_define
class SsidMultiCastOpenApiVO:
    """SSID Multicast/Broadcast Management config.

    Attributes:
        multi_cast_enable (bool | Unset): Whether to enable multicast to unicast, which is enabled by default. True:
            enable, false: disable.
        ipv_6_cast_enable (bool | Unset): Whether to enable IPv6 multicast to unicast, which is enabled by default.
            True: enable, false: disable.
        channel_util (int | Unset): This item indicates that when the channel utilization reaches the threshold,
            multicast will no longer be converted to unicast, the default threshold is 100, and the value should be within
            the range of 0-100.
        arp_cast_enable (bool | Unset): Whether to enable ARP cast to unicast, which is enabled by default. True:
            enable, false: disable.
        filter_enable (bool | Unset): Whether to enable the multicast filter switch, which is disabled by default. True:
            enable, false: disable.
        filter_mode (int | Unset): This item indicates the status of the filtering protocol. The lowest bit indicates
            whether IGMP is enabled; the second lowest bit indicates whether MDNS is enabled; and the third lowest bit
            indicates whether Others is enabled. 1 means enable while 0 means disable. For example, 7(111) means that all
            are enabled; 1(001) means that only IGMP is enabled.
        mac_group_id (str | Unset): This field represents MAC Group Profile ID. MAC Group Profile can be created using
            Create a new group profile interface, and MAC Group Profile ID can be obtained from Get group profile list by
            type interface.
    """

    multi_cast_enable: bool | Unset = UNSET
    ipv_6_cast_enable: bool | Unset = UNSET
    channel_util: int | Unset = UNSET
    arp_cast_enable: bool | Unset = UNSET
    filter_enable: bool | Unset = UNSET
    filter_mode: int | Unset = UNSET
    mac_group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        multi_cast_enable = self.multi_cast_enable

        ipv_6_cast_enable = self.ipv_6_cast_enable

        channel_util = self.channel_util

        arp_cast_enable = self.arp_cast_enable

        filter_enable = self.filter_enable

        filter_mode = self.filter_mode

        mac_group_id = self.mac_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if multi_cast_enable is not UNSET:
            field_dict["multiCastEnable"] = multi_cast_enable
        if ipv_6_cast_enable is not UNSET:
            field_dict["ipv6CastEnable"] = ipv_6_cast_enable
        if channel_util is not UNSET:
            field_dict["channelUtil"] = channel_util
        if arp_cast_enable is not UNSET:
            field_dict["arpCastEnable"] = arp_cast_enable
        if filter_enable is not UNSET:
            field_dict["filterEnable"] = filter_enable
        if filter_mode is not UNSET:
            field_dict["filterMode"] = filter_mode
        if mac_group_id is not UNSET:
            field_dict["macGroupId"] = mac_group_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        multi_cast_enable = d.pop("multiCastEnable", UNSET)

        ipv_6_cast_enable = d.pop("ipv6CastEnable", UNSET)

        channel_util = d.pop("channelUtil", UNSET)

        arp_cast_enable = d.pop("arpCastEnable", UNSET)

        filter_enable = d.pop("filterEnable", UNSET)

        filter_mode = d.pop("filterMode", UNSET)

        mac_group_id = d.pop("macGroupId", UNSET)

        ssid_multi_cast_open_api_vo = cls(
            multi_cast_enable=multi_cast_enable,
            ipv_6_cast_enable=ipv_6_cast_enable,
            channel_util=channel_util,
            arp_cast_enable=arp_cast_enable,
            filter_enable=filter_enable,
            filter_mode=filter_mode,
            mac_group_id=mac_group_id,
        )

        ssid_multi_cast_open_api_vo.additional_properties = d
        return ssid_multi_cast_open_api_vo

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
