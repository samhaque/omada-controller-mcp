from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_band_ctrl_vo import OswBandCtrlVO
    from ..models.osw_lag_status_vo import OswLagStatusVO
    from ..models.osw_mlag_peer_all_ports_config_info_vo import (
        OswMlagPeerAllPortsConfigInfoVO,
    )
    from ..models.osw_mlag_peer_setting_vo import OswMlagPeerSettingVO
    from ..models.osw_port_dhcp_l2_relay_vo import OswPortDhcpL2RelayVO
    from ..models.osw_port_oui_based_vlan_vo import OswPortOuiBasedVlanVO
    from ..models.osw_stack_member_lag_vo_tag_bridge_vlan_map import (
        OswStackMemberLagVOTagBridgeVlanMap,
    )
    from ..models.osw_stack_member_lag_vo_untag_bridge_vlan_map import (
        OswStackMemberLagVOUntagBridgeVlanMap,
    )
    from ..models.osw_stand_port_vo import OswStandPortVO
    from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
    from ..models.spanning_tree_setting_vo import SpanningTreeSettingVO


T = TypeVar("T", bound="OswStackMemberLagVO")


@_attrs_define
class OswStackMemberLagVO:
    """Stack lags

    Attributes:
        id (str | Unset): ID
        switch_id (str | Unset): Switch ID
        switch_mac (str | Unset): Switch MAC Address
        site (str | Unset): Site
        lag_id (int | Unset): Lag ID
        name (str | Unset): Lag Name
        tag_ids (list[str] | Unset): Lag label ID List
        tag_name (str | Unset): Lag label Name
        network_mode (int | Unset): Network Mode should be a value as follows: 0: Trunk, 1: Access
        native_network_id (str | Unset): Native Network ID, Native Network cannot be selected from Tagged Networks or
            Untagged Networks.
        native_bridge_vlan (int | Unset): Native Network Bridge Vlan.
        network_tags_setting (int | Unset): Network Tags Setting should be a value as follows: 0: Allow All; 1: Block
            All; 2: Custom
        tag_network_ids (list[str] | Unset): Tag Network IDs
        tag_bridge_vlan_map (OswStackMemberLagVOTagBridgeVlanMap | Unset): Tag Network Bridge Vlan Map
        untag_network_ids (list[str] | Unset): Untag Network IDs
        untag_bridge_vlan_map (OswStackMemberLagVOUntagBridgeVlanMap | Unset): Untag Network Bridge Vlan Map
        voice_network_enable (bool | Unset): Voice network enable status
        voice_network_id (str | Unset): Voice Network ID
        voice_bridge_vlan (int | Unset): Voice Network Bridge Vlan
        voice_dscp_enable (bool | Unset): Voice DSCP enable status
        voice_dscp (int | Unset): Voice DSCP
        port_alert_enable (bool | Unset): Indicates whether port alert is enabled
        ports (list[int] | Unset): Lag Ports
        st_ports (list[str] | Unset): Lag StPorts
        all_aggregating_ports (list[int] | Unset): All aggregating ports of the current Switch
        all_mirroring_ports (list[int] | Unset): All mirroring ports of the current Switch
        all_mirrored_ports (list[int] | Unset): All mirrored ports on the Switch
        all_mlag_peer_link_ports (list[int] | Unset): All ports configured with M-LAG PeerLink on the current Switch
        all_mlag_dad_ports (list[int] | Unset): All ports configured with M-LAG DAD on the current Switch
        lag_type (int | Unset): Lag Type should be a value as follows: 1: STATIC; 2: LACP; 3: LACP ACTIVE; 4: LACP
            PASSIVE
        mlag_name (str | Unset): M-LAG Name
        mlag_enable (bool | Unset): Indicates whether M-LAG is enabled
        mlag_peer_setting (OswMlagPeerSettingVO | Unset): M-LAG group peer device setting
        lag_status (OswLagStatusVO | Unset): Lag Status
        disable (bool | Unset): Indicates whether to disable
        profile_id (str | Unset): Profile ID
        profile_name (str | Unset): Lan Profile Name
        profile_override_enable (bool | Unset): Indicates whether to enable Profile Override before v6.2.10; Indicates
            the fill mode of port configuration after v6.2.10: true: custom; false: follow profile
        profile_vlan_override_enable (bool | Unset): Indicates the fill mode of vlan configuration: true: custom; false:
            follow profile
        link_speed (int | Unset): Link Speed should be a value as follows: 0: auto; 1: 10M; 2: 100M; 3: 1000M; 4: 2.5G;
            5: 10G
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
        igmp_snooping_enable (bool | Unset): Indicates whether IGMP Snooping is enabled
        band_ctrl (OswBandCtrlVO | Unset): Speed Limit
        storm_ctrl (OswStormCtrlVO | Unset): Storm Control
        band_width_ctrl_type (int | Unset): BandWidthCtrlType should be a value as follows: 0: Off; 1: Rate Limit; 2:
            Storming Control
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
        qos_support (bool | Unset): Indicates whether qos support is enabled
        es_qos_support (bool | Unset): Indicates whether the ES device port supports modification of QoS configuration
        qos_queue_enable (bool | Unset): Indicates whether the ES device port has enabled the Qos scheduling queue
            configuration
        queue_id (int | Unset): ES Qos scheduling queue ID
        es_enable_all_profile_can_add (bool | Unset): Indicates whether es enable of all profile can continue to add
            VLANs
        network_conflict (bool | Unset): Indicates whether the VLAN configuration activated on the port is inconsistent
            with the VLAN configuration in the Profile.
        resource (int | Unset): Data Source. Resource should be a value as follows: 0: new created; 1: from template; 2:
            override
        mlag_peer_all_ports_config_info (OswMlagPeerAllPortsConfigInfoVO | Unset): Configuration information of all
            M-LAG Peer ports, used to determine whether the port can be selected
        locate_enable (bool | Unset): Whether locate function is enabled
        oui_based_vlan_networks (OswPortOuiBasedVlanVO | Unset): Vlans configured in oui based rules.
        standard_ports (list[OswStandPortVO] | Unset): LAG Standard ports
        all_aggregating_st_ports (list[OswStandPortVO] | Unset): All Aggregating Standard Ports
        all_mirroring_st_ports (list[OswStandPortVO] | Unset): All Mirroring Standard Ports
        all_mirrored_st_ports (list[OswStandPortVO] | Unset): All Mirrored Standard Ports
    """

    id: str | Unset = UNSET
    switch_id: str | Unset = UNSET
    switch_mac: str | Unset = UNSET
    site: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    name: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    tag_name: str | Unset = UNSET
    network_mode: int | Unset = UNSET
    native_network_id: str | Unset = UNSET
    native_bridge_vlan: int | Unset = UNSET
    network_tags_setting: int | Unset = UNSET
    tag_network_ids: list[str] | Unset = UNSET
    tag_bridge_vlan_map: OswStackMemberLagVOTagBridgeVlanMap | Unset = UNSET
    untag_network_ids: list[str] | Unset = UNSET
    untag_bridge_vlan_map: OswStackMemberLagVOUntagBridgeVlanMap | Unset = UNSET
    voice_network_enable: bool | Unset = UNSET
    voice_network_id: str | Unset = UNSET
    voice_bridge_vlan: int | Unset = UNSET
    voice_dscp_enable: bool | Unset = UNSET
    voice_dscp: int | Unset = UNSET
    port_alert_enable: bool | Unset = UNSET
    ports: list[int] | Unset = UNSET
    st_ports: list[str] | Unset = UNSET
    all_aggregating_ports: list[int] | Unset = UNSET
    all_mirroring_ports: list[int] | Unset = UNSET
    all_mirrored_ports: list[int] | Unset = UNSET
    all_mlag_peer_link_ports: list[int] | Unset = UNSET
    all_mlag_dad_ports: list[int] | Unset = UNSET
    lag_type: int | Unset = UNSET
    mlag_name: str | Unset = UNSET
    mlag_enable: bool | Unset = UNSET
    mlag_peer_setting: OswMlagPeerSettingVO | Unset = UNSET
    lag_status: OswLagStatusVO | Unset = UNSET
    disable: bool | Unset = UNSET
    profile_id: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    profile_override_enable: bool | Unset = UNSET
    profile_vlan_override_enable: bool | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    igmp_snooping_enable: bool | Unset = UNSET
    band_ctrl: OswBandCtrlVO | Unset = UNSET
    storm_ctrl: OswStormCtrlVO | Unset = UNSET
    band_width_ctrl_type: int | Unset = UNSET
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
    qos_support: bool | Unset = UNSET
    es_qos_support: bool | Unset = UNSET
    qos_queue_enable: bool | Unset = UNSET
    queue_id: int | Unset = UNSET
    es_enable_all_profile_can_add: bool | Unset = UNSET
    network_conflict: bool | Unset = UNSET
    resource: int | Unset = UNSET
    mlag_peer_all_ports_config_info: OswMlagPeerAllPortsConfigInfoVO | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    oui_based_vlan_networks: OswPortOuiBasedVlanVO | Unset = UNSET
    standard_ports: list[OswStandPortVO] | Unset = UNSET
    all_aggregating_st_ports: list[OswStandPortVO] | Unset = UNSET
    all_mirroring_st_ports: list[OswStandPortVO] | Unset = UNSET
    all_mirrored_st_ports: list[OswStandPortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        switch_id = self.switch_id

        switch_mac = self.switch_mac

        site = self.site

        lag_id = self.lag_id

        name = self.name

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        tag_name = self.tag_name

        network_mode = self.network_mode

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

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        st_ports: list[str] | Unset = UNSET
        if not isinstance(self.st_ports, Unset):
            st_ports = self.st_ports

        all_aggregating_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_aggregating_ports, Unset):
            all_aggregating_ports = self.all_aggregating_ports

        all_mirroring_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mirroring_ports, Unset):
            all_mirroring_ports = self.all_mirroring_ports

        all_mirrored_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mirrored_ports, Unset):
            all_mirrored_ports = self.all_mirrored_ports

        all_mlag_peer_link_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mlag_peer_link_ports, Unset):
            all_mlag_peer_link_ports = self.all_mlag_peer_link_ports

        all_mlag_dad_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mlag_dad_ports, Unset):
            all_mlag_dad_ports = self.all_mlag_dad_ports

        lag_type = self.lag_type

        mlag_name = self.mlag_name

        mlag_enable = self.mlag_enable

        mlag_peer_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_peer_setting, Unset):
            mlag_peer_setting = self.mlag_peer_setting.to_dict()

        lag_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_status, Unset):
            lag_status = self.lag_status.to_dict()

        disable = self.disable

        profile_id = self.profile_id

        profile_name = self.profile_name

        profile_override_enable = self.profile_override_enable

        profile_vlan_override_enable = self.profile_vlan_override_enable

        link_speed = self.link_speed

        duplex = self.duplex

        igmp_snooping_enable = self.igmp_snooping_enable

        band_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_ctrl, Unset):
            band_ctrl = self.band_ctrl.to_dict()

        storm_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storm_ctrl, Unset):
            storm_ctrl = self.storm_ctrl.to_dict()

        band_width_ctrl_type = self.band_width_ctrl_type

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

        qos_support = self.qos_support

        es_qos_support = self.es_qos_support

        qos_queue_enable = self.qos_queue_enable

        queue_id = self.queue_id

        es_enable_all_profile_can_add = self.es_enable_all_profile_can_add

        network_conflict = self.network_conflict

        resource = self.resource

        mlag_peer_all_ports_config_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_peer_all_ports_config_info, Unset):
            mlag_peer_all_ports_config_info = (
                self.mlag_peer_all_ports_config_info.to_dict()
            )

        locate_enable = self.locate_enable

        oui_based_vlan_networks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oui_based_vlan_networks, Unset):
            oui_based_vlan_networks = self.oui_based_vlan_networks.to_dict()

        standard_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = []
            for standard_ports_item_data in self.standard_ports:
                standard_ports_item = standard_ports_item_data.to_dict()
                standard_ports.append(standard_ports_item)

        all_aggregating_st_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_aggregating_st_ports, Unset):
            all_aggregating_st_ports = []
            for all_aggregating_st_ports_item_data in self.all_aggregating_st_ports:
                all_aggregating_st_ports_item = (
                    all_aggregating_st_ports_item_data.to_dict()
                )
                all_aggregating_st_ports.append(all_aggregating_st_ports_item)

        all_mirroring_st_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_mirroring_st_ports, Unset):
            all_mirroring_st_ports = []
            for all_mirroring_st_ports_item_data in self.all_mirroring_st_ports:
                all_mirroring_st_ports_item = all_mirroring_st_ports_item_data.to_dict()
                all_mirroring_st_ports.append(all_mirroring_st_ports_item)

        all_mirrored_st_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_mirrored_st_ports, Unset):
            all_mirrored_st_ports = []
            for all_mirrored_st_ports_item_data in self.all_mirrored_st_ports:
                all_mirrored_st_ports_item = all_mirrored_st_ports_item_data.to_dict()
                all_mirrored_st_ports.append(all_mirrored_st_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if switch_id is not UNSET:
            field_dict["switchId"] = switch_id
        if switch_mac is not UNSET:
            field_dict["switchMac"] = switch_mac
        if site is not UNSET:
            field_dict["site"] = site
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if name is not UNSET:
            field_dict["name"] = name
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name
        if network_mode is not UNSET:
            field_dict["networkMode"] = network_mode
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
        if ports is not UNSET:
            field_dict["ports"] = ports
        if st_ports is not UNSET:
            field_dict["stPorts"] = st_ports
        if all_aggregating_ports is not UNSET:
            field_dict["allAggregatingPorts"] = all_aggregating_ports
        if all_mirroring_ports is not UNSET:
            field_dict["allMirroringPorts"] = all_mirroring_ports
        if all_mirrored_ports is not UNSET:
            field_dict["allMirroredPorts"] = all_mirrored_ports
        if all_mlag_peer_link_ports is not UNSET:
            field_dict["allMlagPeerLinkPorts"] = all_mlag_peer_link_ports
        if all_mlag_dad_ports is not UNSET:
            field_dict["allMlagDadPorts"] = all_mlag_dad_ports
        if lag_type is not UNSET:
            field_dict["lagType"] = lag_type
        if mlag_name is not UNSET:
            field_dict["mlagName"] = mlag_name
        if mlag_enable is not UNSET:
            field_dict["mlagEnable"] = mlag_enable
        if mlag_peer_setting is not UNSET:
            field_dict["mlagPeerSetting"] = mlag_peer_setting
        if lag_status is not UNSET:
            field_dict["lagStatus"] = lag_status
        if disable is not UNSET:
            field_dict["disable"] = disable
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
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
        if band_ctrl is not UNSET:
            field_dict["bandCtrl"] = band_ctrl
        if storm_ctrl is not UNSET:
            field_dict["stormCtrl"] = storm_ctrl
        if band_width_ctrl_type is not UNSET:
            field_dict["bandWidthCtrlType"] = band_width_ctrl_type
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
        if qos_support is not UNSET:
            field_dict["qosSupport"] = qos_support
        if es_qos_support is not UNSET:
            field_dict["esQosSupport"] = es_qos_support
        if qos_queue_enable is not UNSET:
            field_dict["qosQueueEnable"] = qos_queue_enable
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if es_enable_all_profile_can_add is not UNSET:
            field_dict["esEnableAllProfileCanAdd"] = es_enable_all_profile_can_add
        if network_conflict is not UNSET:
            field_dict["networkConflict"] = network_conflict
        if resource is not UNSET:
            field_dict["resource"] = resource
        if mlag_peer_all_ports_config_info is not UNSET:
            field_dict["mlagPeerAllPortsConfigInfo"] = mlag_peer_all_ports_config_info
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if oui_based_vlan_networks is not UNSET:
            field_dict["ouiBasedVlanNetworks"] = oui_based_vlan_networks
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports
        if all_aggregating_st_ports is not UNSET:
            field_dict["allAggregatingStPorts"] = all_aggregating_st_ports
        if all_mirroring_st_ports is not UNSET:
            field_dict["allMirroringStPorts"] = all_mirroring_st_ports
        if all_mirrored_st_ports is not UNSET:
            field_dict["allMirroredStPorts"] = all_mirrored_st_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_band_ctrl_vo import OswBandCtrlVO
        from ..models.osw_lag_status_vo import OswLagStatusVO
        from ..models.osw_mlag_peer_all_ports_config_info_vo import (
            OswMlagPeerAllPortsConfigInfoVO,
        )
        from ..models.osw_mlag_peer_setting_vo import (
            OswMlagPeerSettingVO,
        )
        from ..models.osw_port_dhcp_l2_relay_vo import (
            OswPortDhcpL2RelayVO,
        )
        from ..models.osw_port_oui_based_vlan_vo import (
            OswPortOuiBasedVlanVO,
        )
        from ..models.osw_stack_member_lag_vo_tag_bridge_vlan_map import (
            OswStackMemberLagVOTagBridgeVlanMap,
        )
        from ..models.osw_stack_member_lag_vo_untag_bridge_vlan_map import (
            OswStackMemberLagVOUntagBridgeVlanMap,
        )
        from ..models.osw_stand_port_vo import OswStandPortVO
        from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
        from ..models.spanning_tree_setting_vo import (
            SpanningTreeSettingVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        switch_id = d.pop("switchId", UNSET)

        switch_mac = d.pop("switchMac", UNSET)

        site = d.pop("site", UNSET)

        lag_id = d.pop("lagId", UNSET)

        name = d.pop("name", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        tag_name = d.pop("tagName", UNSET)

        network_mode = d.pop("networkMode", UNSET)

        native_network_id = d.pop("nativeNetworkId", UNSET)

        native_bridge_vlan = d.pop("nativeBridgeVlan", UNSET)

        network_tags_setting = d.pop("networkTagsSetting", UNSET)

        tag_network_ids = cast(list[str], d.pop("tagNetworkIds", UNSET))

        _tag_bridge_vlan_map = d.pop("tagBridgeVlanMap", UNSET)
        tag_bridge_vlan_map: OswStackMemberLagVOTagBridgeVlanMap | Unset
        if isinstance(_tag_bridge_vlan_map, Unset):
            tag_bridge_vlan_map = UNSET
        else:
            tag_bridge_vlan_map = OswStackMemberLagVOTagBridgeVlanMap.from_dict(
                _tag_bridge_vlan_map
            )

        untag_network_ids = cast(list[str], d.pop("untagNetworkIds", UNSET))

        _untag_bridge_vlan_map = d.pop("untagBridgeVlanMap", UNSET)
        untag_bridge_vlan_map: OswStackMemberLagVOUntagBridgeVlanMap | Unset
        if isinstance(_untag_bridge_vlan_map, Unset):
            untag_bridge_vlan_map = UNSET
        else:
            untag_bridge_vlan_map = OswStackMemberLagVOUntagBridgeVlanMap.from_dict(
                _untag_bridge_vlan_map
            )

        voice_network_enable = d.pop("voiceNetworkEnable", UNSET)

        voice_network_id = d.pop("voiceNetworkId", UNSET)

        voice_bridge_vlan = d.pop("voiceBridgeVlan", UNSET)

        voice_dscp_enable = d.pop("voiceDscpEnable", UNSET)

        voice_dscp = d.pop("voiceDscp", UNSET)

        port_alert_enable = d.pop("portAlertEnable", UNSET)

        ports = cast(list[int], d.pop("ports", UNSET))

        st_ports = cast(list[str], d.pop("stPorts", UNSET))

        all_aggregating_ports = cast(list[int], d.pop("allAggregatingPorts", UNSET))

        all_mirroring_ports = cast(list[int], d.pop("allMirroringPorts", UNSET))

        all_mirrored_ports = cast(list[int], d.pop("allMirroredPorts", UNSET))

        all_mlag_peer_link_ports = cast(list[int], d.pop("allMlagPeerLinkPorts", UNSET))

        all_mlag_dad_ports = cast(list[int], d.pop("allMlagDadPorts", UNSET))

        lag_type = d.pop("lagType", UNSET)

        mlag_name = d.pop("mlagName", UNSET)

        mlag_enable = d.pop("mlagEnable", UNSET)

        _mlag_peer_setting = d.pop("mlagPeerSetting", UNSET)
        mlag_peer_setting: OswMlagPeerSettingVO | Unset
        if isinstance(_mlag_peer_setting, Unset):
            mlag_peer_setting = UNSET
        else:
            mlag_peer_setting = OswMlagPeerSettingVO.from_dict(_mlag_peer_setting)

        _lag_status = d.pop("lagStatus", UNSET)
        lag_status: OswLagStatusVO | Unset
        if isinstance(_lag_status, Unset):
            lag_status = UNSET
        else:
            lag_status = OswLagStatusVO.from_dict(_lag_status)

        disable = d.pop("disable", UNSET)

        profile_id = d.pop("profileId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        profile_override_enable = d.pop("profileOverrideEnable", UNSET)

        profile_vlan_override_enable = d.pop("profileVlanOverrideEnable", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        igmp_snooping_enable = d.pop("igmpSnoopingEnable", UNSET)

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

        band_width_ctrl_type = d.pop("bandWidthCtrlType", UNSET)

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

        qos_support = d.pop("qosSupport", UNSET)

        es_qos_support = d.pop("esQosSupport", UNSET)

        qos_queue_enable = d.pop("qosQueueEnable", UNSET)

        queue_id = d.pop("queueId", UNSET)

        es_enable_all_profile_can_add = d.pop("esEnableAllProfileCanAdd", UNSET)

        network_conflict = d.pop("networkConflict", UNSET)

        resource = d.pop("resource", UNSET)

        _mlag_peer_all_ports_config_info = d.pop("mlagPeerAllPortsConfigInfo", UNSET)
        mlag_peer_all_ports_config_info: OswMlagPeerAllPortsConfigInfoVO | Unset
        if isinstance(_mlag_peer_all_ports_config_info, Unset):
            mlag_peer_all_ports_config_info = UNSET
        else:
            mlag_peer_all_ports_config_info = OswMlagPeerAllPortsConfigInfoVO.from_dict(
                _mlag_peer_all_ports_config_info
            )

        locate_enable = d.pop("locateEnable", UNSET)

        _oui_based_vlan_networks = d.pop("ouiBasedVlanNetworks", UNSET)
        oui_based_vlan_networks: OswPortOuiBasedVlanVO | Unset
        if isinstance(_oui_based_vlan_networks, Unset):
            oui_based_vlan_networks = UNSET
        else:
            oui_based_vlan_networks = OswPortOuiBasedVlanVO.from_dict(
                _oui_based_vlan_networks
            )

        _standard_ports = d.pop("standardPorts", UNSET)
        standard_ports: list[OswStandPortVO] | Unset = UNSET
        if _standard_ports is not UNSET:
            standard_ports = []
            for standard_ports_item_data in _standard_ports:
                standard_ports_item = OswStandPortVO.from_dict(standard_ports_item_data)

                standard_ports.append(standard_ports_item)

        _all_aggregating_st_ports = d.pop("allAggregatingStPorts", UNSET)
        all_aggregating_st_ports: list[OswStandPortVO] | Unset = UNSET
        if _all_aggregating_st_ports is not UNSET:
            all_aggregating_st_ports = []
            for all_aggregating_st_ports_item_data in _all_aggregating_st_ports:
                all_aggregating_st_ports_item = OswStandPortVO.from_dict(
                    all_aggregating_st_ports_item_data
                )

                all_aggregating_st_ports.append(all_aggregating_st_ports_item)

        _all_mirroring_st_ports = d.pop("allMirroringStPorts", UNSET)
        all_mirroring_st_ports: list[OswStandPortVO] | Unset = UNSET
        if _all_mirroring_st_ports is not UNSET:
            all_mirroring_st_ports = []
            for all_mirroring_st_ports_item_data in _all_mirroring_st_ports:
                all_mirroring_st_ports_item = OswStandPortVO.from_dict(
                    all_mirroring_st_ports_item_data
                )

                all_mirroring_st_ports.append(all_mirroring_st_ports_item)

        _all_mirrored_st_ports = d.pop("allMirroredStPorts", UNSET)
        all_mirrored_st_ports: list[OswStandPortVO] | Unset = UNSET
        if _all_mirrored_st_ports is not UNSET:
            all_mirrored_st_ports = []
            for all_mirrored_st_ports_item_data in _all_mirrored_st_ports:
                all_mirrored_st_ports_item = OswStandPortVO.from_dict(
                    all_mirrored_st_ports_item_data
                )

                all_mirrored_st_ports.append(all_mirrored_st_ports_item)

        osw_stack_member_lag_vo = cls(
            id=id,
            switch_id=switch_id,
            switch_mac=switch_mac,
            site=site,
            lag_id=lag_id,
            name=name,
            tag_ids=tag_ids,
            tag_name=tag_name,
            network_mode=network_mode,
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
            ports=ports,
            st_ports=st_ports,
            all_aggregating_ports=all_aggregating_ports,
            all_mirroring_ports=all_mirroring_ports,
            all_mirrored_ports=all_mirrored_ports,
            all_mlag_peer_link_ports=all_mlag_peer_link_ports,
            all_mlag_dad_ports=all_mlag_dad_ports,
            lag_type=lag_type,
            mlag_name=mlag_name,
            mlag_enable=mlag_enable,
            mlag_peer_setting=mlag_peer_setting,
            lag_status=lag_status,
            disable=disable,
            profile_id=profile_id,
            profile_name=profile_name,
            profile_override_enable=profile_override_enable,
            profile_vlan_override_enable=profile_vlan_override_enable,
            link_speed=link_speed,
            duplex=duplex,
            igmp_snooping_enable=igmp_snooping_enable,
            band_ctrl=band_ctrl,
            storm_ctrl=storm_ctrl,
            band_width_ctrl_type=band_width_ctrl_type,
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
            qos_support=qos_support,
            es_qos_support=es_qos_support,
            qos_queue_enable=qos_queue_enable,
            queue_id=queue_id,
            es_enable_all_profile_can_add=es_enable_all_profile_can_add,
            network_conflict=network_conflict,
            resource=resource,
            mlag_peer_all_ports_config_info=mlag_peer_all_ports_config_info,
            locate_enable=locate_enable,
            oui_based_vlan_networks=oui_based_vlan_networks,
            standard_ports=standard_ports,
            all_aggregating_st_ports=all_aggregating_st_ports,
            all_mirroring_st_ports=all_mirroring_st_ports,
            all_mirrored_st_ports=all_mirrored_st_ports,
        )

        osw_stack_member_lag_vo.additional_properties = d
        return osw_stack_member_lag_vo

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
