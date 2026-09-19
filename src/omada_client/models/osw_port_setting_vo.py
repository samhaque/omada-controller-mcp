from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_band_ctrl_vo import OswBandCtrlVO
    from ..models.osw_lag_basic_vo import OswLagBasicVO
    from ..models.osw_port_dhcp_l2_relay_vo import OswPortDhcpL2RelayVO
    from ..models.osw_port_setting_vo_tag_bridge_vlan_map import (
        OswPortSettingVOTagBridgeVlanMap,
    )
    from ..models.osw_port_setting_vo_untag_bridge_vlan_map import (
        OswPortSettingVOUntagBridgeVlanMap,
    )
    from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
    from ..models.spanning_tree_setting_vo import SpanningTreeSettingVO


T = TypeVar("T", bound="OswPortSettingVO")


@_attrs_define
class OswPortSettingVO:
    """
    Attributes:
        name (str | Unset): Port or Lag Name
        tag_ids (list[str] | Unset): Tag ID List
        native_network_id (str | Unset): Native Network ID, Native Network cannot be selected from Tagged Networks or
            Untagged Networks.
        native_bridge_vlan (int | Unset): Native Network Bridge Vlan.
        network_tags_setting (int | Unset): Network Tags Setting should be a value as follows: 0: Allow All; 1: Block
            All; 2: Custom
        tag_network_ids (list[str] | Unset): Tag Network IDs
        tag_bridge_vlan_map (OswPortSettingVOTagBridgeVlanMap | Unset): Tag Network Bridge Vlan Map
        untag_network_ids (list[str] | Unset): Untag Network IDs
        untag_bridge_vlan_map (OswPortSettingVOUntagBridgeVlanMap | Unset): Untag Network Bridge Vlan Map
        voice_network_enable (bool | Unset): Indicates whether voice network is enabled
        voice_network_id (str | Unset): Voice Network ID
        voice_bridge_vlan (int | Unset): Voice Network Bridge Vlan
        voice_dscp_enable (bool | Unset): Indicates whether voice DSCP is enabled
        voice_dscp (int | Unset): Voice DSCP
        port_alert_enable (bool | Unset): Indicates whether port alert is enabled
        fec_mode (int | Unset): FEC mode should be a value as follows: 1: Off; 2: RS528; 3: RS544; 4: Auto; 5: Base-R
        fec_link_peer_apply_enable (bool | Unset): Indicates whether the FEC Mode is synchronously applied to the link
            peer port.
        disable (bool | Unset): Indicates whether to disable
        profile_id (str | Unset): Profile ID is required (not null) when modifying a single port.
        profile_override_enable (bool | Unset): Indicates whether to enable Profile Override before v6.2.10; Indicates
            the fill mode of port configuration after v6.2.10: true: custom; false: follow profile
        profile_vlan_override_enable (bool | Unset): Indicates the fill mode of vlan configuration: true: custom; false:
            follow profile
        link_speed (int | Unset): Link Speed should be a value as follows: 0: auto; 1: 10M; 2: 100M; 3: 1000M; 4: 2.5G;
            5: 10G
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
        igmp_snooping_enable (bool | Unset): Indicates whether IGMP Snooping is enabled
        band_width_ctrl_type (int | Unset): BandWidthCtrlType should be a value as follows: 0: Off; 1: Rate Limit; 2:
            Storming Control
        band_ctrl (OswBandCtrlVO | Unset): Speed Limit
        storm_ctrl (OswStormCtrlVO | Unset): Storm Control
        spanning_tree_enable (bool | Unset): Indicates whether SpanningTree is enabled
        spanning_tree_setting (SpanningTreeSettingVO | Unset): SpanningTree Setting
        loopback_detect_enable (bool | Unset): Indicates whether loopbackDetect port based is enabled
        loopback_detect_vlan_based_enable (bool | Unset): Indicates whether loopbackDetect vlan based is enabled
        igmp_fast_leave_enable (bool | Unset): Indicates whether igmp fast leave is enabled
        mld_fast_leave_enable (bool | Unset): Indicates whether mld fast leave is enabled
        port_isolation_enable (bool | Unset): Indicates whether port isolation is enabled
        eee_enable (bool | Unset): Indicates whether EEE is enabled
        flow_control_enable (bool | Unset): Indicates whether flow control is enabled
        fast_leave_enable (bool | Unset): Indicates whether igmpSnooping fastLeave is enabled
        dhcp_l2_relay_settings (OswPortDhcpL2RelayVO | Unset): Dhcp L2 Relay Setting
        dot_1_p_priority (int | Unset): Dot1p Priority
        trust_mode (int | Unset): TrustMode should be a value as follows: 0: Untrusted; 1: Trust 802.1p; 2: Trust DSCP
        qos_queue_enable (bool | Unset): Indicates whether the ES device port has enabled the Qos scheduling queue
            configuration
        queue_id (int | Unset): ES Qos scheduling queue ID
        removed_oui_based_rule_ids (list[str] | Unset): The id of oui based vlan rule removded.
        operation (str | Unset): Operation should be a value as follows: "switching" or "mirroring" or "aggregating"
        mirrored_ports (list[int] | Unset): Mirrored Ports
        mirrored_lags (list[int] | Unset): Mirrored Lags
        lag_setting (OswLagBasicVO | Unset): Lag Setting
        lag_delete (bool | Unset): When the operation changes from aggregating to switching, this parameter should be
            set to true, and the "lagSetting" parameter needs to include the lagId.
        dot1x (int | Unset): Dot1x should be a value as follows: 0: Force unauthorized; 1: Force authorized; 2: Auto
        poe (int | Unset): Poe should be a value as follows: 0: Off; 1: 802.3at/af
        lldp_med_enable (bool | Unset): Indicates whether LLDP-MED is enabled
        topo_notify_enable (bool | Unset): Indicates whether Topology Notify is enabled
    """

    name: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    native_network_id: str | Unset = UNSET
    native_bridge_vlan: int | Unset = UNSET
    network_tags_setting: int | Unset = UNSET
    tag_network_ids: list[str] | Unset = UNSET
    tag_bridge_vlan_map: OswPortSettingVOTagBridgeVlanMap | Unset = UNSET
    untag_network_ids: list[str] | Unset = UNSET
    untag_bridge_vlan_map: OswPortSettingVOUntagBridgeVlanMap | Unset = UNSET
    voice_network_enable: bool | Unset = UNSET
    voice_network_id: str | Unset = UNSET
    voice_bridge_vlan: int | Unset = UNSET
    voice_dscp_enable: bool | Unset = UNSET
    voice_dscp: int | Unset = UNSET
    port_alert_enable: bool | Unset = UNSET
    fec_mode: int | Unset = UNSET
    fec_link_peer_apply_enable: bool | Unset = UNSET
    disable: bool | Unset = UNSET
    profile_id: str | Unset = UNSET
    profile_override_enable: bool | Unset = UNSET
    profile_vlan_override_enable: bool | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    igmp_snooping_enable: bool | Unset = UNSET
    band_width_ctrl_type: int | Unset = UNSET
    band_ctrl: OswBandCtrlVO | Unset = UNSET
    storm_ctrl: OswStormCtrlVO | Unset = UNSET
    spanning_tree_enable: bool | Unset = UNSET
    spanning_tree_setting: SpanningTreeSettingVO | Unset = UNSET
    loopback_detect_enable: bool | Unset = UNSET
    loopback_detect_vlan_based_enable: bool | Unset = UNSET
    igmp_fast_leave_enable: bool | Unset = UNSET
    mld_fast_leave_enable: bool | Unset = UNSET
    port_isolation_enable: bool | Unset = UNSET
    eee_enable: bool | Unset = UNSET
    flow_control_enable: bool | Unset = UNSET
    fast_leave_enable: bool | Unset = UNSET
    dhcp_l2_relay_settings: OswPortDhcpL2RelayVO | Unset = UNSET
    dot_1_p_priority: int | Unset = UNSET
    trust_mode: int | Unset = UNSET
    qos_queue_enable: bool | Unset = UNSET
    queue_id: int | Unset = UNSET
    removed_oui_based_rule_ids: list[str] | Unset = UNSET
    operation: str | Unset = UNSET
    mirrored_ports: list[int] | Unset = UNSET
    mirrored_lags: list[int] | Unset = UNSET
    lag_setting: OswLagBasicVO | Unset = UNSET
    lag_delete: bool | Unset = UNSET
    dot1x: int | Unset = UNSET
    poe: int | Unset = UNSET
    lldp_med_enable: bool | Unset = UNSET
    topo_notify_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        native_network_id = self.native_network_id

        native_bridge_vlan = self.native_bridge_vlan

        network_tags_setting = self.network_tags_setting

        tag_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_network_ids, Unset):
            tag_network_ids = self.tag_network_ids

        tag_bridge_vlan_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_bridge_vlan_map, Unset):
            tag_bridge_vlan_map = self.tag_bridge_vlan_map.to_dict()

        untag_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.untag_network_ids, Unset):
            untag_network_ids = self.untag_network_ids

        untag_bridge_vlan_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.untag_bridge_vlan_map, Unset):
            untag_bridge_vlan_map = self.untag_bridge_vlan_map.to_dict()

        voice_network_enable = self.voice_network_enable

        voice_network_id = self.voice_network_id

        voice_bridge_vlan = self.voice_bridge_vlan

        voice_dscp_enable = self.voice_dscp_enable

        voice_dscp = self.voice_dscp

        port_alert_enable = self.port_alert_enable

        fec_mode = self.fec_mode

        fec_link_peer_apply_enable = self.fec_link_peer_apply_enable

        disable = self.disable

        profile_id = self.profile_id

        profile_override_enable = self.profile_override_enable

        profile_vlan_override_enable = self.profile_vlan_override_enable

        link_speed = self.link_speed

        duplex = self.duplex

        igmp_snooping_enable = self.igmp_snooping_enable

        band_width_ctrl_type = self.band_width_ctrl_type

        band_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_ctrl, Unset):
            band_ctrl = self.band_ctrl.to_dict()

        storm_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storm_ctrl, Unset):
            storm_ctrl = self.storm_ctrl.to_dict()

        spanning_tree_enable = self.spanning_tree_enable

        spanning_tree_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spanning_tree_setting, Unset):
            spanning_tree_setting = self.spanning_tree_setting.to_dict()

        loopback_detect_enable = self.loopback_detect_enable

        loopback_detect_vlan_based_enable = self.loopback_detect_vlan_based_enable

        igmp_fast_leave_enable = self.igmp_fast_leave_enable

        mld_fast_leave_enable = self.mld_fast_leave_enable

        port_isolation_enable = self.port_isolation_enable

        eee_enable = self.eee_enable

        flow_control_enable = self.flow_control_enable

        fast_leave_enable = self.fast_leave_enable

        dhcp_l2_relay_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_l2_relay_settings, Unset):
            dhcp_l2_relay_settings = self.dhcp_l2_relay_settings.to_dict()

        dot_1_p_priority = self.dot_1_p_priority

        trust_mode = self.trust_mode

        qos_queue_enable = self.qos_queue_enable

        queue_id = self.queue_id

        removed_oui_based_rule_ids: list[str] | Unset = UNSET
        if not isinstance(self.removed_oui_based_rule_ids, Unset):
            removed_oui_based_rule_ids = self.removed_oui_based_rule_ids

        operation = self.operation

        mirrored_ports: list[int] | Unset = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = self.mirrored_ports

        mirrored_lags: list[int] | Unset = UNSET
        if not isinstance(self.mirrored_lags, Unset):
            mirrored_lags = self.mirrored_lags

        lag_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_setting, Unset):
            lag_setting = self.lag_setting.to_dict()

        lag_delete = self.lag_delete

        dot1x = self.dot1x

        poe = self.poe

        lldp_med_enable = self.lldp_med_enable

        topo_notify_enable = self.topo_notify_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if native_network_id is not UNSET:
            field_dict["nativeNetworkId"] = native_network_id
        if native_bridge_vlan is not UNSET:
            field_dict["nativeBridgeVlan"] = native_bridge_vlan
        if network_tags_setting is not UNSET:
            field_dict["networkTagsSetting"] = network_tags_setting
        if tag_network_ids is not UNSET:
            field_dict["tagNetworkIds"] = tag_network_ids
        if tag_bridge_vlan_map is not UNSET:
            field_dict["tagBridgeVlanMap"] = tag_bridge_vlan_map
        if untag_network_ids is not UNSET:
            field_dict["untagNetworkIds"] = untag_network_ids
        if untag_bridge_vlan_map is not UNSET:
            field_dict["untagBridgeVlanMap"] = untag_bridge_vlan_map
        if voice_network_enable is not UNSET:
            field_dict["voiceNetworkEnable"] = voice_network_enable
        if voice_network_id is not UNSET:
            field_dict["voiceNetworkId"] = voice_network_id
        if voice_bridge_vlan is not UNSET:
            field_dict["voiceBridgeVlan"] = voice_bridge_vlan
        if voice_dscp_enable is not UNSET:
            field_dict["voiceDscpEnable"] = voice_dscp_enable
        if voice_dscp is not UNSET:
            field_dict["voiceDscp"] = voice_dscp
        if port_alert_enable is not UNSET:
            field_dict["portAlertEnable"] = port_alert_enable
        if fec_mode is not UNSET:
            field_dict["fecMode"] = fec_mode
        if fec_link_peer_apply_enable is not UNSET:
            field_dict["fecLinkPeerApplyEnable"] = fec_link_peer_apply_enable
        if disable is not UNSET:
            field_dict["disable"] = disable
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_override_enable is not UNSET:
            field_dict["profileOverrideEnable"] = profile_override_enable
        if profile_vlan_override_enable is not UNSET:
            field_dict["profileVlanOverrideEnable"] = profile_vlan_override_enable
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if igmp_snooping_enable is not UNSET:
            field_dict["igmpSnoopingEnable"] = igmp_snooping_enable
        if band_width_ctrl_type is not UNSET:
            field_dict["bandWidthCtrlType"] = band_width_ctrl_type
        if band_ctrl is not UNSET:
            field_dict["bandCtrl"] = band_ctrl
        if storm_ctrl is not UNSET:
            field_dict["stormCtrl"] = storm_ctrl
        if spanning_tree_enable is not UNSET:
            field_dict["spanningTreeEnable"] = spanning_tree_enable
        if spanning_tree_setting is not UNSET:
            field_dict["spanningTreeSetting"] = spanning_tree_setting
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if loopback_detect_vlan_based_enable is not UNSET:
            field_dict["loopbackDetectVlanBasedEnable"] = (
                loopback_detect_vlan_based_enable
            )
        if igmp_fast_leave_enable is not UNSET:
            field_dict["igmpFastLeaveEnable"] = igmp_fast_leave_enable
        if mld_fast_leave_enable is not UNSET:
            field_dict["mldFastLeaveEnable"] = mld_fast_leave_enable
        if port_isolation_enable is not UNSET:
            field_dict["portIsolationEnable"] = port_isolation_enable
        if eee_enable is not UNSET:
            field_dict["eeeEnable"] = eee_enable
        if flow_control_enable is not UNSET:
            field_dict["flowControlEnable"] = flow_control_enable
        if fast_leave_enable is not UNSET:
            field_dict["fastLeaveEnable"] = fast_leave_enable
        if dhcp_l2_relay_settings is not UNSET:
            field_dict["dhcpL2RelaySettings"] = dhcp_l2_relay_settings
        if dot_1_p_priority is not UNSET:
            field_dict["dot1pPriority"] = dot_1_p_priority
        if trust_mode is not UNSET:
            field_dict["trustMode"] = trust_mode
        if qos_queue_enable is not UNSET:
            field_dict["qosQueueEnable"] = qos_queue_enable
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if removed_oui_based_rule_ids is not UNSET:
            field_dict["removedOuiBasedRuleIds"] = removed_oui_based_rule_ids
        if operation is not UNSET:
            field_dict["operation"] = operation
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if mirrored_lags is not UNSET:
            field_dict["mirroredLags"] = mirrored_lags
        if lag_setting is not UNSET:
            field_dict["lagSetting"] = lag_setting
        if lag_delete is not UNSET:
            field_dict["lagDelete"] = lag_delete
        if dot1x is not UNSET:
            field_dict["dot1x"] = dot1x
        if poe is not UNSET:
            field_dict["poe"] = poe
        if lldp_med_enable is not UNSET:
            field_dict["lldpMedEnable"] = lldp_med_enable
        if topo_notify_enable is not UNSET:
            field_dict["topoNotifyEnable"] = topo_notify_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_band_ctrl_vo import OswBandCtrlVO
        from ..models.osw_lag_basic_vo import OswLagBasicVO
        from ..models.osw_port_dhcp_l2_relay_vo import (
            OswPortDhcpL2RelayVO,
        )
        from ..models.osw_port_setting_vo_tag_bridge_vlan_map import (
            OswPortSettingVOTagBridgeVlanMap,
        )
        from ..models.osw_port_setting_vo_untag_bridge_vlan_map import (
            OswPortSettingVOUntagBridgeVlanMap,
        )
        from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
        from ..models.spanning_tree_setting_vo import (
            SpanningTreeSettingVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        native_network_id = d.pop("nativeNetworkId", UNSET)

        native_bridge_vlan = d.pop("nativeBridgeVlan", UNSET)

        network_tags_setting = d.pop("networkTagsSetting", UNSET)

        tag_network_ids = cast(list[str], d.pop("tagNetworkIds", UNSET))

        _tag_bridge_vlan_map = d.pop("tagBridgeVlanMap", UNSET)
        tag_bridge_vlan_map: OswPortSettingVOTagBridgeVlanMap | Unset
        if isinstance(_tag_bridge_vlan_map, Unset):
            tag_bridge_vlan_map = UNSET
        else:
            tag_bridge_vlan_map = OswPortSettingVOTagBridgeVlanMap.from_dict(
                _tag_bridge_vlan_map
            )

        untag_network_ids = cast(list[str], d.pop("untagNetworkIds", UNSET))

        _untag_bridge_vlan_map = d.pop("untagBridgeVlanMap", UNSET)
        untag_bridge_vlan_map: OswPortSettingVOUntagBridgeVlanMap | Unset
        if isinstance(_untag_bridge_vlan_map, Unset):
            untag_bridge_vlan_map = UNSET
        else:
            untag_bridge_vlan_map = OswPortSettingVOUntagBridgeVlanMap.from_dict(
                _untag_bridge_vlan_map
            )

        voice_network_enable = d.pop("voiceNetworkEnable", UNSET)

        voice_network_id = d.pop("voiceNetworkId", UNSET)

        voice_bridge_vlan = d.pop("voiceBridgeVlan", UNSET)

        voice_dscp_enable = d.pop("voiceDscpEnable", UNSET)

        voice_dscp = d.pop("voiceDscp", UNSET)

        port_alert_enable = d.pop("portAlertEnable", UNSET)

        fec_mode = d.pop("fecMode", UNSET)

        fec_link_peer_apply_enable = d.pop("fecLinkPeerApplyEnable", UNSET)

        disable = d.pop("disable", UNSET)

        profile_id = d.pop("profileId", UNSET)

        profile_override_enable = d.pop("profileOverrideEnable", UNSET)

        profile_vlan_override_enable = d.pop("profileVlanOverrideEnable", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        igmp_snooping_enable = d.pop("igmpSnoopingEnable", UNSET)

        band_width_ctrl_type = d.pop("bandWidthCtrlType", UNSET)

        _band_ctrl = d.pop("bandCtrl", UNSET)
        band_ctrl: OswBandCtrlVO | Unset
        if isinstance(_band_ctrl, Unset):
            band_ctrl = UNSET
        else:
            band_ctrl = OswBandCtrlVO.from_dict(_band_ctrl)

        _storm_ctrl = d.pop("stormCtrl", UNSET)
        storm_ctrl: OswStormCtrlVO | Unset
        if isinstance(_storm_ctrl, Unset):
            storm_ctrl = UNSET
        else:
            storm_ctrl = OswStormCtrlVO.from_dict(_storm_ctrl)

        spanning_tree_enable = d.pop("spanningTreeEnable", UNSET)

        _spanning_tree_setting = d.pop("spanningTreeSetting", UNSET)
        spanning_tree_setting: SpanningTreeSettingVO | Unset
        if isinstance(_spanning_tree_setting, Unset):
            spanning_tree_setting = UNSET
        else:
            spanning_tree_setting = SpanningTreeSettingVO.from_dict(
                _spanning_tree_setting
            )

        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        loopback_detect_vlan_based_enable = d.pop(
            "loopbackDetectVlanBasedEnable", UNSET
        )

        igmp_fast_leave_enable = d.pop("igmpFastLeaveEnable", UNSET)

        mld_fast_leave_enable = d.pop("mldFastLeaveEnable", UNSET)

        port_isolation_enable = d.pop("portIsolationEnable", UNSET)

        eee_enable = d.pop("eeeEnable", UNSET)

        flow_control_enable = d.pop("flowControlEnable", UNSET)

        fast_leave_enable = d.pop("fastLeaveEnable", UNSET)

        _dhcp_l2_relay_settings = d.pop("dhcpL2RelaySettings", UNSET)
        dhcp_l2_relay_settings: OswPortDhcpL2RelayVO | Unset
        if isinstance(_dhcp_l2_relay_settings, Unset):
            dhcp_l2_relay_settings = UNSET
        else:
            dhcp_l2_relay_settings = OswPortDhcpL2RelayVO.from_dict(
                _dhcp_l2_relay_settings
            )

        dot_1_p_priority = d.pop("dot1pPriority", UNSET)

        trust_mode = d.pop("trustMode", UNSET)

        qos_queue_enable = d.pop("qosQueueEnable", UNSET)

        queue_id = d.pop("queueId", UNSET)

        removed_oui_based_rule_ids = cast(
            list[str], d.pop("removedOuiBasedRuleIds", UNSET)
        )

        operation = d.pop("operation", UNSET)

        mirrored_ports = cast(list[int], d.pop("mirroredPorts", UNSET))

        mirrored_lags = cast(list[int], d.pop("mirroredLags", UNSET))

        _lag_setting = d.pop("lagSetting", UNSET)
        lag_setting: OswLagBasicVO | Unset
        if isinstance(_lag_setting, Unset):
            lag_setting = UNSET
        else:
            lag_setting = OswLagBasicVO.from_dict(_lag_setting)

        lag_delete = d.pop("lagDelete", UNSET)

        dot1x = d.pop("dot1x", UNSET)

        poe = d.pop("poe", UNSET)

        lldp_med_enable = d.pop("lldpMedEnable", UNSET)

        topo_notify_enable = d.pop("topoNotifyEnable", UNSET)

        osw_port_setting_vo = cls(
            name=name,
            tag_ids=tag_ids,
            native_network_id=native_network_id,
            native_bridge_vlan=native_bridge_vlan,
            network_tags_setting=network_tags_setting,
            tag_network_ids=tag_network_ids,
            tag_bridge_vlan_map=tag_bridge_vlan_map,
            untag_network_ids=untag_network_ids,
            untag_bridge_vlan_map=untag_bridge_vlan_map,
            voice_network_enable=voice_network_enable,
            voice_network_id=voice_network_id,
            voice_bridge_vlan=voice_bridge_vlan,
            voice_dscp_enable=voice_dscp_enable,
            voice_dscp=voice_dscp,
            port_alert_enable=port_alert_enable,
            fec_mode=fec_mode,
            fec_link_peer_apply_enable=fec_link_peer_apply_enable,
            disable=disable,
            profile_id=profile_id,
            profile_override_enable=profile_override_enable,
            profile_vlan_override_enable=profile_vlan_override_enable,
            link_speed=link_speed,
            duplex=duplex,
            igmp_snooping_enable=igmp_snooping_enable,
            band_width_ctrl_type=band_width_ctrl_type,
            band_ctrl=band_ctrl,
            storm_ctrl=storm_ctrl,
            spanning_tree_enable=spanning_tree_enable,
            spanning_tree_setting=spanning_tree_setting,
            loopback_detect_enable=loopback_detect_enable,
            loopback_detect_vlan_based_enable=loopback_detect_vlan_based_enable,
            igmp_fast_leave_enable=igmp_fast_leave_enable,
            mld_fast_leave_enable=mld_fast_leave_enable,
            port_isolation_enable=port_isolation_enable,
            eee_enable=eee_enable,
            flow_control_enable=flow_control_enable,
            fast_leave_enable=fast_leave_enable,
            dhcp_l2_relay_settings=dhcp_l2_relay_settings,
            dot_1_p_priority=dot_1_p_priority,
            trust_mode=trust_mode,
            qos_queue_enable=qos_queue_enable,
            queue_id=queue_id,
            removed_oui_based_rule_ids=removed_oui_based_rule_ids,
            operation=operation,
            mirrored_ports=mirrored_ports,
            mirrored_lags=mirrored_lags,
            lag_setting=lag_setting,
            lag_delete=lag_delete,
            dot1x=dot1x,
            poe=poe,
            lldp_med_enable=lldp_med_enable,
            topo_notify_enable=topo_notify_enable,
        )

        osw_port_setting_vo.additional_properties = d
        return osw_port_setting_vo

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
