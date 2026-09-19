from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.band_ctrl_vo import BandCtrlVO
    from ..models.dhcp_l2_relay_vo import DhcpL2RelayVO
    from ..models.spanning_tree_setting_vo import SpanningTreeSettingVO
    from ..models.storm_ctrl_vo import StormCtrlVO


T = TypeVar("T", bound="LanProfileConfigOpenApiVO")


@_attrs_define
class LanProfileConfigOpenApiVO:
    """
    Attributes:
        name (str): Name should contain 1 to 128 characters.
        poe (int): PoE should be a value as follows: 0: off, 1: on, 2: "do not modify"
        native_network_id (str): Native network ID, Native Network cannot be selected from Tagged Networks or Untagged
            Networks.
        dot1x (int): Dot1x should be a value as follows: 0: force unauthorized, 1: force authorized, 2:auto
        port_isolation_enable (bool): Port-isolation enable status
        lldp_med_enable (bool): LLDP-MED enable status
        band_width_ctrl_type (int): BandWidthCtrlType should be a value as follows: 0: off, 1: rate limit, 2: storming
            control
        spanning_tree_enable (bool): SpanningTree enable status
        loopback_detect_enable (bool): LoopbackDetect enable status
        tag_network_ids (list[str] | Unset): Tag network IDs
        untag_network_ids (list[str] | Unset): Untag network IDs
        voice_network_id (str | Unset): Voice Network ID
        storm_ctrl (StormCtrlVO | Unset): StormCtrl
        band_ctrl (BandCtrlVO | Unset): BandCtrl
        spanning_tree_setting (SpanningTreeSettingVO | Unset): SpanningTree Setting
        eee_enable (bool | Unset): EEE enable status
        flow_control_enable (bool | Unset): FlowControl enable status
        loopback_detect_vlan_based_enable (bool | Unset): LoopbackDetectVLANBased enable status
        igmp_fast_leave_enable (bool | Unset): Indicates whether igmp fast leave is enabled
        mld_fast_leave_enable (bool | Unset): Indicates whether mld fast leave is enabled
        dhcp_l2_relay_settings (DhcpL2RelayVO | Unset): DHCPL2RelaySettings
        fast_leave_enable (bool | Unset): IGMP Snooping fast leave enable status
        dot_1_p_priority (int | Unset): 802.1p Priority
        trust_mode (int | Unset): Trust mode
    """

    name: str
    poe: int
    native_network_id: str
    dot1x: int
    port_isolation_enable: bool
    lldp_med_enable: bool
    band_width_ctrl_type: int
    spanning_tree_enable: bool
    loopback_detect_enable: bool
    tag_network_ids: list[str] | Unset = UNSET
    untag_network_ids: list[str] | Unset = UNSET
    voice_network_id: str | Unset = UNSET
    storm_ctrl: StormCtrlVO | Unset = UNSET
    band_ctrl: BandCtrlVO | Unset = UNSET
    spanning_tree_setting: SpanningTreeSettingVO | Unset = UNSET
    eee_enable: bool | Unset = UNSET
    flow_control_enable: bool | Unset = UNSET
    loopback_detect_vlan_based_enable: bool | Unset = UNSET
    igmp_fast_leave_enable: bool | Unset = UNSET
    mld_fast_leave_enable: bool | Unset = UNSET
    dhcp_l2_relay_settings: DhcpL2RelayVO | Unset = UNSET
    fast_leave_enable: bool | Unset = UNSET
    dot_1_p_priority: int | Unset = UNSET
    trust_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        poe = self.poe

        native_network_id = self.native_network_id

        dot1x = self.dot1x

        port_isolation_enable = self.port_isolation_enable

        lldp_med_enable = self.lldp_med_enable

        band_width_ctrl_type = self.band_width_ctrl_type

        spanning_tree_enable = self.spanning_tree_enable

        loopback_detect_enable = self.loopback_detect_enable

        tag_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_network_ids, Unset):
            tag_network_ids = self.tag_network_ids

        untag_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.untag_network_ids, Unset):
            untag_network_ids = self.untag_network_ids

        voice_network_id = self.voice_network_id

        storm_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storm_ctrl, Unset):
            storm_ctrl = self.storm_ctrl.to_dict()

        band_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_ctrl, Unset):
            band_ctrl = self.band_ctrl.to_dict()

        spanning_tree_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spanning_tree_setting, Unset):
            spanning_tree_setting = self.spanning_tree_setting.to_dict()

        eee_enable = self.eee_enable

        flow_control_enable = self.flow_control_enable

        loopback_detect_vlan_based_enable = self.loopback_detect_vlan_based_enable

        igmp_fast_leave_enable = self.igmp_fast_leave_enable

        mld_fast_leave_enable = self.mld_fast_leave_enable

        dhcp_l2_relay_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_l2_relay_settings, Unset):
            dhcp_l2_relay_settings = self.dhcp_l2_relay_settings.to_dict()

        fast_leave_enable = self.fast_leave_enable

        dot_1_p_priority = self.dot_1_p_priority

        trust_mode = self.trust_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "poe": poe,
                "nativeNetworkId": native_network_id,
                "dot1x": dot1x,
                "portIsolationEnable": port_isolation_enable,
                "lldpMedEnable": lldp_med_enable,
                "bandWidthCtrlType": band_width_ctrl_type,
                "spanningTreeEnable": spanning_tree_enable,
                "loopbackDetectEnable": loopback_detect_enable,
            }
        )
        if tag_network_ids is not UNSET:
            field_dict["tagNetworkIds"] = tag_network_ids
        if untag_network_ids is not UNSET:
            field_dict["untagNetworkIds"] = untag_network_ids
        if voice_network_id is not UNSET:
            field_dict["voiceNetworkId"] = voice_network_id
        if storm_ctrl is not UNSET:
            field_dict["stormCtrl"] = storm_ctrl
        if band_ctrl is not UNSET:
            field_dict["bandCtrl"] = band_ctrl
        if spanning_tree_setting is not UNSET:
            field_dict["spanningTreeSetting"] = spanning_tree_setting
        if eee_enable is not UNSET:
            field_dict["eeeEnable"] = eee_enable
        if flow_control_enable is not UNSET:
            field_dict["flowControlEnable"] = flow_control_enable
        if loopback_detect_vlan_based_enable is not UNSET:
            field_dict["loopbackDetectVlanBasedEnable"] = (
                loopback_detect_vlan_based_enable
            )
        if igmp_fast_leave_enable is not UNSET:
            field_dict["igmpFastLeaveEnable"] = igmp_fast_leave_enable
        if mld_fast_leave_enable is not UNSET:
            field_dict["mldFastLeaveEnable"] = mld_fast_leave_enable
        if dhcp_l2_relay_settings is not UNSET:
            field_dict["dhcpL2RelaySettings"] = dhcp_l2_relay_settings
        if fast_leave_enable is not UNSET:
            field_dict["fastLeaveEnable"] = fast_leave_enable
        if dot_1_p_priority is not UNSET:
            field_dict["dot1pPriority"] = dot_1_p_priority
        if trust_mode is not UNSET:
            field_dict["trustMode"] = trust_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.band_ctrl_vo import BandCtrlVO
        from ..models.dhcp_l2_relay_vo import DhcpL2RelayVO
        from ..models.spanning_tree_setting_vo import (
            SpanningTreeSettingVO,
        )
        from ..models.storm_ctrl_vo import StormCtrlVO

        d = dict(src_dict)
        name = d.pop("name")

        poe = d.pop("poe")

        native_network_id = d.pop("nativeNetworkId")

        dot1x = d.pop("dot1x")

        port_isolation_enable = d.pop("portIsolationEnable")

        lldp_med_enable = d.pop("lldpMedEnable")

        band_width_ctrl_type = d.pop("bandWidthCtrlType")

        spanning_tree_enable = d.pop("spanningTreeEnable")

        loopback_detect_enable = d.pop("loopbackDetectEnable")

        tag_network_ids = cast(list[str], d.pop("tagNetworkIds", UNSET))

        untag_network_ids = cast(list[str], d.pop("untagNetworkIds", UNSET))

        voice_network_id = d.pop("voiceNetworkId", UNSET)

        _storm_ctrl = d.pop("stormCtrl", UNSET)
        storm_ctrl: StormCtrlVO | Unset
        if isinstance(_storm_ctrl, Unset):
            storm_ctrl = UNSET
        else:
            storm_ctrl = StormCtrlVO.from_dict(_storm_ctrl)

        _band_ctrl = d.pop("bandCtrl", UNSET)
        band_ctrl: BandCtrlVO | Unset
        if isinstance(_band_ctrl, Unset):
            band_ctrl = UNSET
        else:
            band_ctrl = BandCtrlVO.from_dict(_band_ctrl)

        _spanning_tree_setting = d.pop("spanningTreeSetting", UNSET)
        spanning_tree_setting: SpanningTreeSettingVO | Unset
        if isinstance(_spanning_tree_setting, Unset):
            spanning_tree_setting = UNSET
        else:
            spanning_tree_setting = SpanningTreeSettingVO.from_dict(
                _spanning_tree_setting
            )

        eee_enable = d.pop("eeeEnable", UNSET)

        flow_control_enable = d.pop("flowControlEnable", UNSET)

        loopback_detect_vlan_based_enable = d.pop(
            "loopbackDetectVlanBasedEnable", UNSET
        )

        igmp_fast_leave_enable = d.pop("igmpFastLeaveEnable", UNSET)

        mld_fast_leave_enable = d.pop("mldFastLeaveEnable", UNSET)

        _dhcp_l2_relay_settings = d.pop("dhcpL2RelaySettings", UNSET)
        dhcp_l2_relay_settings: DhcpL2RelayVO | Unset
        if isinstance(_dhcp_l2_relay_settings, Unset):
            dhcp_l2_relay_settings = UNSET
        else:
            dhcp_l2_relay_settings = DhcpL2RelayVO.from_dict(_dhcp_l2_relay_settings)

        fast_leave_enable = d.pop("fastLeaveEnable", UNSET)

        dot_1_p_priority = d.pop("dot1pPriority", UNSET)

        trust_mode = d.pop("trustMode", UNSET)

        lan_profile_config_open_api_vo = cls(
            name=name,
            poe=poe,
            native_network_id=native_network_id,
            dot1x=dot1x,
            port_isolation_enable=port_isolation_enable,
            lldp_med_enable=lldp_med_enable,
            band_width_ctrl_type=band_width_ctrl_type,
            spanning_tree_enable=spanning_tree_enable,
            loopback_detect_enable=loopback_detect_enable,
            tag_network_ids=tag_network_ids,
            untag_network_ids=untag_network_ids,
            voice_network_id=voice_network_id,
            storm_ctrl=storm_ctrl,
            band_ctrl=band_ctrl,
            spanning_tree_setting=spanning_tree_setting,
            eee_enable=eee_enable,
            flow_control_enable=flow_control_enable,
            loopback_detect_vlan_based_enable=loopback_detect_vlan_based_enable,
            igmp_fast_leave_enable=igmp_fast_leave_enable,
            mld_fast_leave_enable=mld_fast_leave_enable,
            dhcp_l2_relay_settings=dhcp_l2_relay_settings,
            fast_leave_enable=fast_leave_enable,
            dot_1_p_priority=dot_1_p_priority,
            trust_mode=trust_mode,
        )

        lan_profile_config_open_api_vo.additional_properties = d
        return lan_profile_config_open_api_vo

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
