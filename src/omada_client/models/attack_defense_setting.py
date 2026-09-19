from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.specified_option_open_api_vo import SpecifiedOptionOpenApiVO


T = TypeVar("T", bound="AttackDefenseSetting")


@_attrs_define
class AttackDefenseSetting:
    """
    Attributes:
        tcp_conn_enable (bool): Multi-connections TCP SYN flood enable of the attack defense setting.
        udp_conn_enable (bool): Multi-connections UDP flood enable of the attack defense setting.
        icmp_conn_enable (bool): Multi-connections ICMP flood enable of the attack defense setting.
        tcp_src_enable (bool): Stationary source TCP SYN flood enable of the attack defense setting.
        udp_src_enable (bool): Stationary source UDP flood enable of the attack defense setting.
        icmp_src_enable (bool): Stationary source ICMP flood enable of the attack defense setting.
        tcp_scan_enable (bool): Block TCP scan enable of the attack defense setting.
        ping_death_enable (bool): Block ping of death of the attack defense setting.
        large_ping_enable (bool): Block large ping of the attack defense setting.
        ping_wan_enable (bool): Block ping from WAN of the attack defense setting.
        win_nuke_attack_enable (bool): Block WinNuke attack of the attack defense setting.
        tcp_syn_fin_enable (bool): Block TCP packets with SYN and FIN Bits set of the attack defense setting.
        tcp_fin_no_ack_enable (bool): Block TCP packets with FIN Bit set but no ACK Bit set of the attack defense
            setting.
        specified_option_enable (bool): Block packets with specified options of the attack defense setting.
        tcp_conn_limit (int | Unset): Multi-connections TCP SYN flood limit should be within the range of 100–99999.
        udp_conn_limit (int | Unset): Multi-connections UDP flood limit should be within the range of 100–99999.
        icmp_conn_limit (int | Unset): Multi-connections ICMP flood limit should be within the range of 100–99999.
        tcp_src_limit (int | Unset): Stationary source TCP SYN flood limit should be within the range of 100–99999.
        udp_src_limit (int | Unset): Stationary source UDP flood limit should be within the range of 100–99999.
        icmp_src_limit (int | Unset): Stationary source ICMP flood limit should be within the range of 100–99999.
        tcp_scan_reject (bool | Unset): Block TCP scan with reject of the attack defense setting.
        large_ping_threshold (int | Unset): Block large ping threshold of the attack defense setting, Value is between
            28 and 65535.
        specified_option (SpecifiedOptionOpenApiVO | Unset): Specified option of the attack defense setting.
        icmp_timestamp_request_reject (bool | Unset): ICMP Timestamp Request setting of the attack defense setting.
    """

    tcp_conn_enable: bool
    udp_conn_enable: bool
    icmp_conn_enable: bool
    tcp_src_enable: bool
    udp_src_enable: bool
    icmp_src_enable: bool
    tcp_scan_enable: bool
    ping_death_enable: bool
    large_ping_enable: bool
    ping_wan_enable: bool
    win_nuke_attack_enable: bool
    tcp_syn_fin_enable: bool
    tcp_fin_no_ack_enable: bool
    specified_option_enable: bool
    tcp_conn_limit: int | Unset = UNSET
    udp_conn_limit: int | Unset = UNSET
    icmp_conn_limit: int | Unset = UNSET
    tcp_src_limit: int | Unset = UNSET
    udp_src_limit: int | Unset = UNSET
    icmp_src_limit: int | Unset = UNSET
    tcp_scan_reject: bool | Unset = UNSET
    large_ping_threshold: int | Unset = UNSET
    specified_option: SpecifiedOptionOpenApiVO | Unset = UNSET
    icmp_timestamp_request_reject: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcp_conn_enable = self.tcp_conn_enable

        udp_conn_enable = self.udp_conn_enable

        icmp_conn_enable = self.icmp_conn_enable

        tcp_src_enable = self.tcp_src_enable

        udp_src_enable = self.udp_src_enable

        icmp_src_enable = self.icmp_src_enable

        tcp_scan_enable = self.tcp_scan_enable

        ping_death_enable = self.ping_death_enable

        large_ping_enable = self.large_ping_enable

        ping_wan_enable = self.ping_wan_enable

        win_nuke_attack_enable = self.win_nuke_attack_enable

        tcp_syn_fin_enable = self.tcp_syn_fin_enable

        tcp_fin_no_ack_enable = self.tcp_fin_no_ack_enable

        specified_option_enable = self.specified_option_enable

        tcp_conn_limit = self.tcp_conn_limit

        udp_conn_limit = self.udp_conn_limit

        icmp_conn_limit = self.icmp_conn_limit

        tcp_src_limit = self.tcp_src_limit

        udp_src_limit = self.udp_src_limit

        icmp_src_limit = self.icmp_src_limit

        tcp_scan_reject = self.tcp_scan_reject

        large_ping_threshold = self.large_ping_threshold

        specified_option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specified_option, Unset):
            specified_option = self.specified_option.to_dict()

        icmp_timestamp_request_reject = self.icmp_timestamp_request_reject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tcpConnEnable": tcp_conn_enable,
                "udpConnEnable": udp_conn_enable,
                "icmpConnEnable": icmp_conn_enable,
                "tcpSrcEnable": tcp_src_enable,
                "udpSrcEnable": udp_src_enable,
                "icmpSrcEnable": icmp_src_enable,
                "tcpScanEnable": tcp_scan_enable,
                "pingDeathEnable": ping_death_enable,
                "largePingEnable": large_ping_enable,
                "pingWanEnable": ping_wan_enable,
                "winNukeAttackEnable": win_nuke_attack_enable,
                "tcpSynFinEnable": tcp_syn_fin_enable,
                "tcpFinNoAckEnable": tcp_fin_no_ack_enable,
                "specifiedOptionEnable": specified_option_enable,
            }
        )
        if tcp_conn_limit is not UNSET:
            field_dict["tcpConnLimit"] = tcp_conn_limit
        if udp_conn_limit is not UNSET:
            field_dict["udpConnLimit"] = udp_conn_limit
        if icmp_conn_limit is not UNSET:
            field_dict["icmpConnLimit"] = icmp_conn_limit
        if tcp_src_limit is not UNSET:
            field_dict["tcpSrcLimit"] = tcp_src_limit
        if udp_src_limit is not UNSET:
            field_dict["udpSrcLimit"] = udp_src_limit
        if icmp_src_limit is not UNSET:
            field_dict["icmpSrcLimit"] = icmp_src_limit
        if tcp_scan_reject is not UNSET:
            field_dict["tcpScanReject"] = tcp_scan_reject
        if large_ping_threshold is not UNSET:
            field_dict["largePingThreshold"] = large_ping_threshold
        if specified_option is not UNSET:
            field_dict["specifiedOption"] = specified_option
        if icmp_timestamp_request_reject is not UNSET:
            field_dict["icmpTimestampRequestReject"] = icmp_timestamp_request_reject

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.specified_option_open_api_vo import (
            SpecifiedOptionOpenApiVO,
        )

        d = dict(src_dict)
        tcp_conn_enable = d.pop("tcpConnEnable")

        udp_conn_enable = d.pop("udpConnEnable")

        icmp_conn_enable = d.pop("icmpConnEnable")

        tcp_src_enable = d.pop("tcpSrcEnable")

        udp_src_enable = d.pop("udpSrcEnable")

        icmp_src_enable = d.pop("icmpSrcEnable")

        tcp_scan_enable = d.pop("tcpScanEnable")

        ping_death_enable = d.pop("pingDeathEnable")

        large_ping_enable = d.pop("largePingEnable")

        ping_wan_enable = d.pop("pingWanEnable")

        win_nuke_attack_enable = d.pop("winNukeAttackEnable")

        tcp_syn_fin_enable = d.pop("tcpSynFinEnable")

        tcp_fin_no_ack_enable = d.pop("tcpFinNoAckEnable")

        specified_option_enable = d.pop("specifiedOptionEnable")

        tcp_conn_limit = d.pop("tcpConnLimit", UNSET)

        udp_conn_limit = d.pop("udpConnLimit", UNSET)

        icmp_conn_limit = d.pop("icmpConnLimit", UNSET)

        tcp_src_limit = d.pop("tcpSrcLimit", UNSET)

        udp_src_limit = d.pop("udpSrcLimit", UNSET)

        icmp_src_limit = d.pop("icmpSrcLimit", UNSET)

        tcp_scan_reject = d.pop("tcpScanReject", UNSET)

        large_ping_threshold = d.pop("largePingThreshold", UNSET)

        _specified_option = d.pop("specifiedOption", UNSET)
        specified_option: SpecifiedOptionOpenApiVO | Unset
        if isinstance(_specified_option, Unset):
            specified_option = UNSET
        else:
            specified_option = SpecifiedOptionOpenApiVO.from_dict(_specified_option)

        icmp_timestamp_request_reject = d.pop("icmpTimestampRequestReject", UNSET)

        attack_defense_setting = cls(
            tcp_conn_enable=tcp_conn_enable,
            udp_conn_enable=udp_conn_enable,
            icmp_conn_enable=icmp_conn_enable,
            tcp_src_enable=tcp_src_enable,
            udp_src_enable=udp_src_enable,
            icmp_src_enable=icmp_src_enable,
            tcp_scan_enable=tcp_scan_enable,
            ping_death_enable=ping_death_enable,
            large_ping_enable=large_ping_enable,
            ping_wan_enable=ping_wan_enable,
            win_nuke_attack_enable=win_nuke_attack_enable,
            tcp_syn_fin_enable=tcp_syn_fin_enable,
            tcp_fin_no_ack_enable=tcp_fin_no_ack_enable,
            specified_option_enable=specified_option_enable,
            tcp_conn_limit=tcp_conn_limit,
            udp_conn_limit=udp_conn_limit,
            icmp_conn_limit=icmp_conn_limit,
            tcp_src_limit=tcp_src_limit,
            udp_src_limit=udp_src_limit,
            icmp_src_limit=icmp_src_limit,
            tcp_scan_reject=tcp_scan_reject,
            large_ping_threshold=large_ping_threshold,
            specified_option=specified_option,
            icmp_timestamp_request_reject=icmp_timestamp_request_reject,
        )

        attack_defense_setting.additional_properties = d
        return attack_defense_setting

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
