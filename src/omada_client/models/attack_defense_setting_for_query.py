from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO
    from ..models.specified_option_open_api_vo import SpecifiedOptionOpenApiVO


T = TypeVar("T", bound="AttackDefenseSettingForQuery")


@_attrs_define
class AttackDefenseSettingForQuery:
    """
    Attributes:
        tcp_conn_enable (bool | Unset): Multi-connections TCP SYN flood enable of the attack defense setting.
        tcp_conn_limit (int | Unset): Multi-connections TCP SYN flood limit should be within the range of 100–99999.
        udp_conn_enable (bool | Unset): Multi-connections UDP flood enable of the attack defense setting.
        udp_conn_limit (int | Unset): Multi-connections UDP flood limit should be within the range of 100–99999.
        icmp_conn_enable (bool | Unset): Multi-connections ICMP flood enable of the attack defense setting.
        icmp_conn_limit (int | Unset): Multi-connections ICMP flood limit should be within the range of 100–99999.
        tcp_src_enable (bool | Unset): Stationary source TCP SYN flood enable of the attack defense setting.
        tcp_src_limit (int | Unset): Stationary source TCP SYN flood limit should be within the range of 100–99999.
        udp_src_enable (bool | Unset): Stationary source UDP flood enable of the attack defense setting.
        udp_src_limit (int | Unset): Stationary source UDP flood limit should be within the range of 100–99999.
        icmp_src_enable (bool | Unset): Stationary source ICMP flood enable of the attack defense setting.
        icmp_src_limit (int | Unset): Stationary source ICMP flood limit should be within the range of 100–99999.
        tcp_scan_enable (bool | Unset): Block TCP scan enable of the attack defense setting.
        tcp_scan_reject (bool | Unset): Block TCP scan with reject of the attack defense setting.
        support_tcp_scan_reject (bool | Unset): Whether Block TCP scan with reject of the attack defense setting is
            supported.
        exist_tcp_scan_reject (bool | Unset): Whether Block TCP scan with reject of the attack defense setting is ON.
        ping_death_enable (bool | Unset): Block ping of death of the attack defense setting.
        large_ping_enable (bool | Unset): Block Large Ping Threshold of the attack defense setting.
        large_ping_threshold (int | Unset): Block Large Ping Threshold of the attack defense setting, Value is between
            28 and 65535.
        support_large_ping_threshold (bool | Unset): Whether custom Block Large Ping Threshold of the attack defense is
            supported.
        exist_large_ping_threshold (bool | Unset): Whether custom Block Large Ping Threshold of attack defense is
            configured.
        ping_wan_enable (bool | Unset): Block ping from WAN of the attack defense setting.
        win_nuke_attack_enable (bool | Unset): Block WinNuke attack of the attack defense setting.
        tcp_syn_fin_enable (bool | Unset): Block TCP packets with SYN and FIN Bits set of the attack defense setting.
        tcp_fin_no_ack_enable (bool | Unset): Block TCP packets with FIN Bit set but no ACK Bit set of the attack
            defense setting.
        specified_option_enable (bool | Unset): Block packets with specified options of the attack defense setting.
        specified_option (SpecifiedOptionOpenApiVO | Unset): Specified option of the attack defense setting.
        icmp_timestamp_request_reject (bool | Unset): ICMP Timestamp Request setting of the attack defense setting.
        support_icmp_timestamp_request_reject (bool | Unset): Whether ICMP Timestamp Request is supported of the attack
            defense setting.
        exist_icmp_timestamp_request_reject (bool | Unset): Whether ICMP Timestamp Request of the attack defense setting
            is ON.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    tcp_conn_enable: bool | Unset = UNSET
    tcp_conn_limit: int | Unset = UNSET
    udp_conn_enable: bool | Unset = UNSET
    udp_conn_limit: int | Unset = UNSET
    icmp_conn_enable: bool | Unset = UNSET
    icmp_conn_limit: int | Unset = UNSET
    tcp_src_enable: bool | Unset = UNSET
    tcp_src_limit: int | Unset = UNSET
    udp_src_enable: bool | Unset = UNSET
    udp_src_limit: int | Unset = UNSET
    icmp_src_enable: bool | Unset = UNSET
    icmp_src_limit: int | Unset = UNSET
    tcp_scan_enable: bool | Unset = UNSET
    tcp_scan_reject: bool | Unset = UNSET
    support_tcp_scan_reject: bool | Unset = UNSET
    exist_tcp_scan_reject: bool | Unset = UNSET
    ping_death_enable: bool | Unset = UNSET
    large_ping_enable: bool | Unset = UNSET
    large_ping_threshold: int | Unset = UNSET
    support_large_ping_threshold: bool | Unset = UNSET
    exist_large_ping_threshold: bool | Unset = UNSET
    ping_wan_enable: bool | Unset = UNSET
    win_nuke_attack_enable: bool | Unset = UNSET
    tcp_syn_fin_enable: bool | Unset = UNSET
    tcp_fin_no_ack_enable: bool | Unset = UNSET
    specified_option_enable: bool | Unset = UNSET
    specified_option: SpecifiedOptionOpenApiVO | Unset = UNSET
    icmp_timestamp_request_reject: bool | Unset = UNSET
    support_icmp_timestamp_request_reject: bool | Unset = UNSET
    exist_icmp_timestamp_request_reject: bool | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcp_conn_enable = self.tcp_conn_enable

        tcp_conn_limit = self.tcp_conn_limit

        udp_conn_enable = self.udp_conn_enable

        udp_conn_limit = self.udp_conn_limit

        icmp_conn_enable = self.icmp_conn_enable

        icmp_conn_limit = self.icmp_conn_limit

        tcp_src_enable = self.tcp_src_enable

        tcp_src_limit = self.tcp_src_limit

        udp_src_enable = self.udp_src_enable

        udp_src_limit = self.udp_src_limit

        icmp_src_enable = self.icmp_src_enable

        icmp_src_limit = self.icmp_src_limit

        tcp_scan_enable = self.tcp_scan_enable

        tcp_scan_reject = self.tcp_scan_reject

        support_tcp_scan_reject = self.support_tcp_scan_reject

        exist_tcp_scan_reject = self.exist_tcp_scan_reject

        ping_death_enable = self.ping_death_enable

        large_ping_enable = self.large_ping_enable

        large_ping_threshold = self.large_ping_threshold

        support_large_ping_threshold = self.support_large_ping_threshold

        exist_large_ping_threshold = self.exist_large_ping_threshold

        ping_wan_enable = self.ping_wan_enable

        win_nuke_attack_enable = self.win_nuke_attack_enable

        tcp_syn_fin_enable = self.tcp_syn_fin_enable

        tcp_fin_no_ack_enable = self.tcp_fin_no_ack_enable

        specified_option_enable = self.specified_option_enable

        specified_option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specified_option, Unset):
            specified_option = self.specified_option.to_dict()

        icmp_timestamp_request_reject = self.icmp_timestamp_request_reject

        support_icmp_timestamp_request_reject = (
            self.support_icmp_timestamp_request_reject
        )

        exist_icmp_timestamp_request_reject = self.exist_icmp_timestamp_request_reject

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tcp_conn_enable is not UNSET:
            field_dict["tcpConnEnable"] = tcp_conn_enable
        if tcp_conn_limit is not UNSET:
            field_dict["tcpConnLimit"] = tcp_conn_limit
        if udp_conn_enable is not UNSET:
            field_dict["udpConnEnable"] = udp_conn_enable
        if udp_conn_limit is not UNSET:
            field_dict["udpConnLimit"] = udp_conn_limit
        if icmp_conn_enable is not UNSET:
            field_dict["icmpConnEnable"] = icmp_conn_enable
        if icmp_conn_limit is not UNSET:
            field_dict["icmpConnLimit"] = icmp_conn_limit
        if tcp_src_enable is not UNSET:
            field_dict["tcpSrcEnable"] = tcp_src_enable
        if tcp_src_limit is not UNSET:
            field_dict["tcpSrcLimit"] = tcp_src_limit
        if udp_src_enable is not UNSET:
            field_dict["udpSrcEnable"] = udp_src_enable
        if udp_src_limit is not UNSET:
            field_dict["udpSrcLimit"] = udp_src_limit
        if icmp_src_enable is not UNSET:
            field_dict["icmpSrcEnable"] = icmp_src_enable
        if icmp_src_limit is not UNSET:
            field_dict["icmpSrcLimit"] = icmp_src_limit
        if tcp_scan_enable is not UNSET:
            field_dict["tcpScanEnable"] = tcp_scan_enable
        if tcp_scan_reject is not UNSET:
            field_dict["tcpScanReject"] = tcp_scan_reject
        if support_tcp_scan_reject is not UNSET:
            field_dict["supportTcpScanReject"] = support_tcp_scan_reject
        if exist_tcp_scan_reject is not UNSET:
            field_dict["existTcpScanReject"] = exist_tcp_scan_reject
        if ping_death_enable is not UNSET:
            field_dict["pingDeathEnable"] = ping_death_enable
        if large_ping_enable is not UNSET:
            field_dict["largePingEnable"] = large_ping_enable
        if large_ping_threshold is not UNSET:
            field_dict["largePingThreshold"] = large_ping_threshold
        if support_large_ping_threshold is not UNSET:
            field_dict["supportLargePingThreshold"] = support_large_ping_threshold
        if exist_large_ping_threshold is not UNSET:
            field_dict["existLargePingThreshold"] = exist_large_ping_threshold
        if ping_wan_enable is not UNSET:
            field_dict["pingWanEnable"] = ping_wan_enable
        if win_nuke_attack_enable is not UNSET:
            field_dict["winNukeAttackEnable"] = win_nuke_attack_enable
        if tcp_syn_fin_enable is not UNSET:
            field_dict["tcpSynFinEnable"] = tcp_syn_fin_enable
        if tcp_fin_no_ack_enable is not UNSET:
            field_dict["tcpFinNoAckEnable"] = tcp_fin_no_ack_enable
        if specified_option_enable is not UNSET:
            field_dict["specifiedOptionEnable"] = specified_option_enable
        if specified_option is not UNSET:
            field_dict["specifiedOption"] = specified_option
        if icmp_timestamp_request_reject is not UNSET:
            field_dict["icmpTimestampRequestReject"] = icmp_timestamp_request_reject
        if support_icmp_timestamp_request_reject is not UNSET:
            field_dict["supportIcmpTimestampRequestReject"] = (
                support_icmp_timestamp_request_reject
            )
        if exist_icmp_timestamp_request_reject is not UNSET:
            field_dict["existIcmpTimestampRequestReject"] = (
                exist_icmp_timestamp_request_reject
            )
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO
        from ..models.specified_option_open_api_vo import (
            SpecifiedOptionOpenApiVO,
        )

        d = dict(src_dict)
        tcp_conn_enable = d.pop("tcpConnEnable", UNSET)

        tcp_conn_limit = d.pop("tcpConnLimit", UNSET)

        udp_conn_enable = d.pop("udpConnEnable", UNSET)

        udp_conn_limit = d.pop("udpConnLimit", UNSET)

        icmp_conn_enable = d.pop("icmpConnEnable", UNSET)

        icmp_conn_limit = d.pop("icmpConnLimit", UNSET)

        tcp_src_enable = d.pop("tcpSrcEnable", UNSET)

        tcp_src_limit = d.pop("tcpSrcLimit", UNSET)

        udp_src_enable = d.pop("udpSrcEnable", UNSET)

        udp_src_limit = d.pop("udpSrcLimit", UNSET)

        icmp_src_enable = d.pop("icmpSrcEnable", UNSET)

        icmp_src_limit = d.pop("icmpSrcLimit", UNSET)

        tcp_scan_enable = d.pop("tcpScanEnable", UNSET)

        tcp_scan_reject = d.pop("tcpScanReject", UNSET)

        support_tcp_scan_reject = d.pop("supportTcpScanReject", UNSET)

        exist_tcp_scan_reject = d.pop("existTcpScanReject", UNSET)

        ping_death_enable = d.pop("pingDeathEnable", UNSET)

        large_ping_enable = d.pop("largePingEnable", UNSET)

        large_ping_threshold = d.pop("largePingThreshold", UNSET)

        support_large_ping_threshold = d.pop("supportLargePingThreshold", UNSET)

        exist_large_ping_threshold = d.pop("existLargePingThreshold", UNSET)

        ping_wan_enable = d.pop("pingWanEnable", UNSET)

        win_nuke_attack_enable = d.pop("winNukeAttackEnable", UNSET)

        tcp_syn_fin_enable = d.pop("tcpSynFinEnable", UNSET)

        tcp_fin_no_ack_enable = d.pop("tcpFinNoAckEnable", UNSET)

        specified_option_enable = d.pop("specifiedOptionEnable", UNSET)

        _specified_option = d.pop("specifiedOption", UNSET)
        specified_option: SpecifiedOptionOpenApiVO | Unset
        if isinstance(_specified_option, Unset):
            specified_option = UNSET
        else:
            specified_option = SpecifiedOptionOpenApiVO.from_dict(_specified_option)

        icmp_timestamp_request_reject = d.pop("icmpTimestampRequestReject", UNSET)

        support_icmp_timestamp_request_reject = d.pop(
            "supportIcmpTimestampRequestReject", UNSET
        )

        exist_icmp_timestamp_request_reject = d.pop(
            "existIcmpTimestampRequestReject", UNSET
        )

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        attack_defense_setting_for_query = cls(
            tcp_conn_enable=tcp_conn_enable,
            tcp_conn_limit=tcp_conn_limit,
            udp_conn_enable=udp_conn_enable,
            udp_conn_limit=udp_conn_limit,
            icmp_conn_enable=icmp_conn_enable,
            icmp_conn_limit=icmp_conn_limit,
            tcp_src_enable=tcp_src_enable,
            tcp_src_limit=tcp_src_limit,
            udp_src_enable=udp_src_enable,
            udp_src_limit=udp_src_limit,
            icmp_src_enable=icmp_src_enable,
            icmp_src_limit=icmp_src_limit,
            tcp_scan_enable=tcp_scan_enable,
            tcp_scan_reject=tcp_scan_reject,
            support_tcp_scan_reject=support_tcp_scan_reject,
            exist_tcp_scan_reject=exist_tcp_scan_reject,
            ping_death_enable=ping_death_enable,
            large_ping_enable=large_ping_enable,
            large_ping_threshold=large_ping_threshold,
            support_large_ping_threshold=support_large_ping_threshold,
            exist_large_ping_threshold=exist_large_ping_threshold,
            ping_wan_enable=ping_wan_enable,
            win_nuke_attack_enable=win_nuke_attack_enable,
            tcp_syn_fin_enable=tcp_syn_fin_enable,
            tcp_fin_no_ack_enable=tcp_fin_no_ack_enable,
            specified_option_enable=specified_option_enable,
            specified_option=specified_option,
            icmp_timestamp_request_reject=icmp_timestamp_request_reject,
            support_icmp_timestamp_request_reject=support_icmp_timestamp_request_reject,
            exist_icmp_timestamp_request_reject=exist_icmp_timestamp_request_reject,
            feature_description=feature_description,
        )

        attack_defense_setting_for_query.additional_properties = d
        return attack_defense_setting_for_query

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
