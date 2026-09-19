from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mirrored_lag import MirroredLag
    from ..models.mirrored_port import MirroredPort
    from ..models.osw_band_ctrl_vo import OswBandCtrlVO
    from ..models.osw_fec_cap_vo import OswFecCapVO
    from ..models.osw_lag_status_vo import OswLagStatusVO
    from ..models.osw_lag_vo import OswLagVO
    from ..models.osw_link_cap_vo import OswLinkCapVO
    from ..models.osw_mlag_peer_all_ports_config_info_vo import (
        OswMlagPeerAllPortsConfigInfoVO,
    )
    from ..models.osw_port_dhcp_l2_relay_vo import OswPortDhcpL2RelayVO
    from ..models.osw_port_oui_based_vlan_vo import OswPortOuiBasedVlanVO
    from ..models.osw_port_speed_cap_vo import OswPortSpeedCapVO
    from ..models.osw_port_stack_setting_vo import OswPortStackSettingVO
    from ..models.osw_port_status_vo import OswPortStatusVO
    from ..models.osw_stack_member_port_vo_tag_bridge_vlan_map import (
        OswStackMemberPortVOTagBridgeVlanMap,
    )
    from ..models.osw_stack_member_port_vo_untag_bridge_vlan_map import (
        OswStackMemberPortVOUntagBridgeVlanMap,
    )
    from ..models.osw_stand_port_vo import OswStandPortVO
    from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
    from ..models.spanning_tree_setting_vo import SpanningTreeSettingVO


T = TypeVar("T", bound="OswStackMemberPortVO")


@_attrs_define
class OswStackMemberPortVO:
    """Including some port configuration information and port real-time status

    Attributes:
        id (str | Unset): ID
        port (int | Unset): Port
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        config_stack (bool | Unset): Indicates whether the current port is configured as a stack port (joined a stack
            aggregation group)
        stack_ports_group_index (int | Unset): Number of the stacking port aggregation group to join
        switch_id (str | Unset): Switch ID to which the port belongs
        switch_mac (str | Unset): Switch Mac to which the port belongs
        site (str | Unset): Site to which the port belongs
        name (str | Unset): Port Name
        disable (bool | Unset): Indicates whether to disable the port
        type_ (int | Unset): Type should be a value as follows: 1: Copper; 2: Combo; 3: SFP
        max_speed (int | Unset): MaxSpeed should be a value as follows: 1: 10Mbps; 2: 100Mbps; 3: 1000Mbps; 4: 2.5Gbps;
            5: 10Gbps
        tag_ids (list[str] | Unset): Port label ID List
        tag_name (str | Unset): Port label Name
        network_mode (int | Unset): Network Mode should be a value as follows: 0: Trunk, 1: Access
        native_network_id (str | Unset): Native Network ID, Native Network cannot be selected from Tagged Networks or
            Untagged Networks.
        native_bridge_vlan (int | Unset): Native Network Bridge Vlan.
        network_tags_setting (int | Unset): Network Tags Setting should be a value as follows: 0: Allow All; 1: Block
            All; 2: Custom
        tag_network_ids (list[str] | Unset): Tag Network IDs
        tag_bridge_vlan_map (OswStackMemberPortVOTagBridgeVlanMap | Unset): Tag Network Bridge Vlan Map
        untag_network_ids (list[str] | Unset): Untag Network IDs
        untag_bridge_vlan_map (OswStackMemberPortVOUntagBridgeVlanMap | Unset): Untag Network Bridge Vlan Map
        voice_network_enable (bool | Unset): Voice network enable status
        voice_network_id (str | Unset): Voice Network ID
        voice_bridge_vlan (int | Unset): Voice Network Bridge Vlan
        voice_dscp_enable (bool | Unset): Voice DSCP enable status
        voice_dscp (int | Unset): Voice DSCP
        profile_id (str | Unset): Lan Profile ID
        profile_name (str | Unset): Lan Profile Name
        profile_override_enable (bool | Unset): Indicates whether to enable Profile Override before v6.2.10; Indicates
            the fill mode of port configuration after v6.2.10: true: custom; false: follow profile
        profile_vlan_override_enable (bool | Unset): Indicates the fill mode of vlan configuration: true: custom; false:
            follow profile
        operation (str | Unset): Operation should be a value as follows: SWITCHING; MIRRORING; AGGREGATING
        mirrored_ports (list[MirroredPort] | Unset): Monitored Port
        mirrored_lags (list[MirroredLag] | Unset): Monitored LAG
        aggregating_ports (list[int] | Unset): Aggregated ports (including this port), non-null only in aggregating mode
        all_aggregating_ports (list[int] | Unset): All ports in the aggregating state on the Switch
        all_mirroring_ports (list[int] | Unset): All ports in the mirroring state on the Switch
        all_mirrored_ports (list[int] | Unset): All mirrored ports on the Switch
        all_mlag_peer_link_ports (list[int] | Unset): All ports configured with M-LAG PeerLink on the Switch
        all_mlag_dad_ports (list[int] | Unset): All ports configured with M-LAG DAD on the Switch
        all_aggregating_st_ports (list[OswStandPortVO] | Unset): All aggregating ports of the current Stack
        all_mirroring_st_ports (list[OswStandPortVO] | Unset): All mirroring ports of the current Stack
        all_mirrored_st_ports (list[OswStandPortVO] | Unset): All mirrored ports of the current Stack
        lag_setting (OswLagVO | Unset): Including some port configuration information and port real-time status
        link_speed (int | Unset): Link Speed should be a value as follows: 0: auto; 1: 10M; 2: 100M; 3: 1000M; 4: 10G
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
        igmp_snooping_enable (bool | Unset): Indicates whether IGMP Snooping is enabled
        dot1x (int | Unset): Dot1x should be a value as follows: 0: Force unauthorized; 1: Force authorized; 2: Auto
        mad_used (bool | Unset): Mad Used
        es_enable_all_profile_can_add (bool | Unset): Indicates whether es enable of all profile can continue to add
            VLANs
        support_poe (bool | Unset): Indicates whether PoE is supported
        support_locate (bool | Unset): Whether the port support locate.
        poe_display_type (int | Unset): PoeDisplayType should be a value as follows: -1: Not Support POE; 0: Support
            POE; 1: POE(4W); 2: POE(7W); 3: POE(15.4W); 4: POE+(30W); 5: POE++(45W); 6: POE++(60W); 7: POE++(75W); 8:
            POE++(90W); 9: POE++(100W).
        poe (int | Unset): PoE switch should be a value as follows: 0: Off; 1: 802.3at/af
        band_width_ctrl_type (int | Unset): BandWidth Control should be a value as follows: 0: Off; 1: Rate Limit; 2:
            Storming Control
        band_ctrl (OswBandCtrlVO | Unset): Speed Limit
        storm_ctrl (OswStormCtrlVO | Unset): Storm Control
        lldp_med_enable (bool | Unset): Indicates whether LLDP MED is enabled
        topo_notify_enable (bool | Unset): Indicates whether to enable topology change notification
        spanning_tree_enable (bool | Unset): Indicates whether SpanningTree is enabled
        spanning_tree_setting (SpanningTreeSettingVO | Unset): SpanningTree Setting
        loopback_detect_enable (bool | Unset): Indicates whether loopbackDetect port based is enabled
        loopback_detect_vlan_based_enable (bool | Unset): Indicates whether loopbackDetect vlan based is enabled
        igmp_fast_leave_enable (bool | Unset): Indicates whether IGMP fast leave is enabled
        mld_fast_leave_enable (bool | Unset): Indicates whether MLD fast leave is enabled
        port_isolation_enable (bool | Unset): Indicates whether port isolation is enabled
        port_status (OswPortStatusVO | Unset): Port Status
        speed (int | Unset): Port Speed should be a value as follows: 1: 10Mbps; 2: 100Mbps; 3: 1000Mbps; 4: 10Gbps
        lag_status (OswLagStatusVO | Unset): Lag Status
        port_cap (list[OswLinkCapVO] | Unset): Port Capability
        port_speed_cap (list[OswPortSpeedCapVO] | Unset): Port Speed Capability
        eee_enable (bool | Unset): Indicates whether EEE is enabled
        flow_control_enable (bool | Unset): Indicates whether flow control is enabled
        extend_mode_support (bool | Unset): Indicates whether extend mode is supported
        extend_mode_enable (bool | Unset): Indicates whether extendMode is enabled
        fast_leave_enable (bool | Unset): Indicates whether igmpSnooping fastLeave is enabled
        dhcp_l2_relay_settings (OswPortDhcpL2RelayVO | Unset): Dhcp L2 Relay Setting
        dot_1_p_priority (int | Unset): Dot1p Priority
        trust_mode (int | Unset): TrustMode should be a value as follows: 0: Untrusted; 1: Trust 802.1p; 2: Trust DSCP
        qos_support (bool | Unset): Indicates whether the device port supports modifying qos configuration
        es_qos_support (bool | Unset): Indicates whether the ES device port supports modification of QoS configuration
        qos_queue_enable (bool | Unset): Indicates whether the ES device port has enabled the Qos scheduling queue
            configuration
        queue_id (int | Unset): ES Qos scheduling queue ID
        network_conflict (bool | Unset): Indicates whether the VLAN configuration activated on the port is inconsistent
            with the VLAN configuration in the Profile.
        resource (int | Unset): Data Source. Resource should be a value as follows: 0: new created; 1: from template; 2:
            override
        port_alert_enable (bool | Unset): Indicates whether Port Alert is enabled
        fec_support (bool | Unset): Indicates whether the port supports FEC configuration
        fec_cap (list[OswFecCapVO] | Unset): All LinkSpeed&FECMode combinations supported by the port
        fec_mode (int | Unset): FEC Mode, sourced from FecModeEnum. 0 - Reserved; 1 - FEC-OFF (Off); 2 - FEC-RS528; 3 -
            FEC-RS544; 4 - FEC-AUTO; 5 - FEC-BASER
        fec_link_peer_apply_enable (bool | Unset): Indicates whether the same FEC mode is applied to the link peer
        config_mlag_peer_link (bool | Unset): Indicates whether the port is configured with M-LAG Peer Link
        config_mlag_dad (bool | Unset): Indicates whether the port is configured with M-LAG DAD Link
        mlag_peer_all_ports_config_info (OswMlagPeerAllPortsConfigInfoVO | Unset): Configuration information of all
            M-LAG Peer ports, used to determine whether the port can be selected
        locate_enable (bool | Unset): Whether locate function is enabled
        used_functions (list[str] | Unset): List of functions that use this port
        is_copper (bool | Unset): Whether the port is copper when the port is combo.
        oui_based_vlan_networks (OswPortOuiBasedVlanVO | Unset): Vlans configured in oui based rules.
        stack_support (bool | Unset): Stack Support
        stack_setting (OswPortStackSettingVO | Unset): Port Stack Setting
        stack_id (str | Unset): Stack ID
    """

    id: str | Unset = UNSET
    port: int | Unset = UNSET
    standard_port: OswStandPortVO | Unset = UNSET
    config_stack: bool | Unset = UNSET
    stack_ports_group_index: int | Unset = UNSET
    switch_id: str | Unset = UNSET
    switch_mac: str | Unset = UNSET
    site: str | Unset = UNSET
    name: str | Unset = UNSET
    disable: bool | Unset = UNSET
    type_: int | Unset = UNSET
    max_speed: int | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    tag_name: str | Unset = UNSET
    network_mode: int | Unset = UNSET
    native_network_id: str | Unset = UNSET
    native_bridge_vlan: int | Unset = UNSET
    network_tags_setting: int | Unset = UNSET
    tag_network_ids: list[str] | Unset = UNSET
    tag_bridge_vlan_map: OswStackMemberPortVOTagBridgeVlanMap | Unset = UNSET
    untag_network_ids: list[str] | Unset = UNSET
    untag_bridge_vlan_map: OswStackMemberPortVOUntagBridgeVlanMap | Unset = UNSET
    voice_network_enable: bool | Unset = UNSET
    voice_network_id: str | Unset = UNSET
    voice_bridge_vlan: int | Unset = UNSET
    voice_dscp_enable: bool | Unset = UNSET
    voice_dscp: int | Unset = UNSET
    profile_id: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    profile_override_enable: bool | Unset = UNSET
    profile_vlan_override_enable: bool | Unset = UNSET
    operation: str | Unset = UNSET
    mirrored_ports: list[MirroredPort] | Unset = UNSET
    mirrored_lags: list[MirroredLag] | Unset = UNSET
    aggregating_ports: list[int] | Unset = UNSET
    all_aggregating_ports: list[int] | Unset = UNSET
    all_mirroring_ports: list[int] | Unset = UNSET
    all_mirrored_ports: list[int] | Unset = UNSET
    all_mlag_peer_link_ports: list[int] | Unset = UNSET
    all_mlag_dad_ports: list[int] | Unset = UNSET
    all_aggregating_st_ports: list[OswStandPortVO] | Unset = UNSET
    all_mirroring_st_ports: list[OswStandPortVO] | Unset = UNSET
    all_mirrored_st_ports: list[OswStandPortVO] | Unset = UNSET
    lag_setting: OswLagVO | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    igmp_snooping_enable: bool | Unset = UNSET
    dot1x: int | Unset = UNSET
    mad_used: bool | Unset = UNSET
    es_enable_all_profile_can_add: bool | Unset = UNSET
    support_poe: bool | Unset = UNSET
    support_locate: bool | Unset = UNSET
    poe_display_type: int | Unset = UNSET
    poe: int | Unset = UNSET
    band_width_ctrl_type: int | Unset = UNSET
    band_ctrl: OswBandCtrlVO | Unset = UNSET
    storm_ctrl: OswStormCtrlVO | Unset = UNSET
    lldp_med_enable: bool | Unset = UNSET
    topo_notify_enable: bool | Unset = UNSET
    spanning_tree_enable: bool | Unset = UNSET
    spanning_tree_setting: SpanningTreeSettingVO | Unset = UNSET
    loopback_detect_enable: bool | Unset = UNSET
    loopback_detect_vlan_based_enable: bool | Unset = UNSET
    igmp_fast_leave_enable: bool | Unset = UNSET
    mld_fast_leave_enable: bool | Unset = UNSET
    port_isolation_enable: bool | Unset = UNSET
    port_status: OswPortStatusVO | Unset = UNSET
    speed: int | Unset = UNSET
    lag_status: OswLagStatusVO | Unset = UNSET
    port_cap: list[OswLinkCapVO] | Unset = UNSET
    port_speed_cap: list[OswPortSpeedCapVO] | Unset = UNSET
    eee_enable: bool | Unset = UNSET
    flow_control_enable: bool | Unset = UNSET
    extend_mode_support: bool | Unset = UNSET
    extend_mode_enable: bool | Unset = UNSET
    fast_leave_enable: bool | Unset = UNSET
    dhcp_l2_relay_settings: OswPortDhcpL2RelayVO | Unset = UNSET
    dot_1_p_priority: int | Unset = UNSET
    trust_mode: int | Unset = UNSET
    qos_support: bool | Unset = UNSET
    es_qos_support: bool | Unset = UNSET
    qos_queue_enable: bool | Unset = UNSET
    queue_id: int | Unset = UNSET
    network_conflict: bool | Unset = UNSET
    resource: int | Unset = UNSET
    port_alert_enable: bool | Unset = UNSET
    fec_support: bool | Unset = UNSET
    fec_cap: list[OswFecCapVO] | Unset = UNSET
    fec_mode: int | Unset = UNSET
    fec_link_peer_apply_enable: bool | Unset = UNSET
    config_mlag_peer_link: bool | Unset = UNSET
    config_mlag_dad: bool | Unset = UNSET
    mlag_peer_all_ports_config_info: OswMlagPeerAllPortsConfigInfoVO | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    used_functions: list[str] | Unset = UNSET
    is_copper: bool | Unset = UNSET
    oui_based_vlan_networks: OswPortOuiBasedVlanVO | Unset = UNSET
    stack_support: bool | Unset = UNSET
    stack_setting: OswPortStackSettingVO | Unset = UNSET
    stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        port = self.port

        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        config_stack = self.config_stack

        stack_ports_group_index = self.stack_ports_group_index

        switch_id = self.switch_id

        switch_mac = self.switch_mac

        site = self.site

        name = self.name

        disable = self.disable

        type_ = self.type_

        max_speed = self.max_speed

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

        profile_id = self.profile_id

        profile_name = self.profile_name

        profile_override_enable = self.profile_override_enable

        profile_vlan_override_enable = self.profile_vlan_override_enable

        operation = self.operation

        mirrored_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = []
            for mirrored_ports_item_data in self.mirrored_ports:
                mirrored_ports_item = mirrored_ports_item_data.to_dict()
                mirrored_ports.append(mirrored_ports_item)

        mirrored_lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mirrored_lags, Unset):
            mirrored_lags = []
            for mirrored_lags_item_data in self.mirrored_lags:
                mirrored_lags_item = mirrored_lags_item_data.to_dict()
                mirrored_lags.append(mirrored_lags_item)

        aggregating_ports: list[int] | Unset = UNSET
        if not isinstance(self.aggregating_ports, Unset):
            aggregating_ports = self.aggregating_ports

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

        lag_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_setting, Unset):
            lag_setting = self.lag_setting.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        igmp_snooping_enable = self.igmp_snooping_enable

        dot1x = self.dot1x

        mad_used = self.mad_used

        es_enable_all_profile_can_add = self.es_enable_all_profile_can_add

        support_poe = self.support_poe

        support_locate = self.support_locate

        poe_display_type = self.poe_display_type

        poe = self.poe

        band_width_ctrl_type = self.band_width_ctrl_type

        band_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_ctrl, Unset):
            band_ctrl = self.band_ctrl.to_dict()

        storm_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storm_ctrl, Unset):
            storm_ctrl = self.storm_ctrl.to_dict()

        lldp_med_enable = self.lldp_med_enable

        topo_notify_enable = self.topo_notify_enable

        spanning_tree_enable = self.spanning_tree_enable

        spanning_tree_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spanning_tree_setting, Unset):
            spanning_tree_setting = self.spanning_tree_setting.to_dict()

        loopback_detect_enable = self.loopback_detect_enable

        loopback_detect_vlan_based_enable = self.loopback_detect_vlan_based_enable

        igmp_fast_leave_enable = self.igmp_fast_leave_enable

        mld_fast_leave_enable = self.mld_fast_leave_enable

        port_isolation_enable = self.port_isolation_enable

        port_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_status, Unset):
            port_status = self.port_status.to_dict()

        speed = self.speed

        lag_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_status, Unset):
            lag_status = self.lag_status.to_dict()

        port_cap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_cap, Unset):
            port_cap = []
            for port_cap_item_data in self.port_cap:
                port_cap_item = port_cap_item_data.to_dict()
                port_cap.append(port_cap_item)

        port_speed_cap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_speed_cap, Unset):
            port_speed_cap = []
            for port_speed_cap_item_data in self.port_speed_cap:
                port_speed_cap_item = port_speed_cap_item_data.to_dict()
                port_speed_cap.append(port_speed_cap_item)

        eee_enable = self.eee_enable

        flow_control_enable = self.flow_control_enable

        extend_mode_support = self.extend_mode_support

        extend_mode_enable = self.extend_mode_enable

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

        network_conflict = self.network_conflict

        resource = self.resource

        port_alert_enable = self.port_alert_enable

        fec_support = self.fec_support

        fec_cap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fec_cap, Unset):
            fec_cap = []
            for fec_cap_item_data in self.fec_cap:
                fec_cap_item = fec_cap_item_data.to_dict()
                fec_cap.append(fec_cap_item)

        fec_mode = self.fec_mode

        fec_link_peer_apply_enable = self.fec_link_peer_apply_enable

        config_mlag_peer_link = self.config_mlag_peer_link

        config_mlag_dad = self.config_mlag_dad

        mlag_peer_all_ports_config_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_peer_all_ports_config_info, Unset):
            mlag_peer_all_ports_config_info = (
                self.mlag_peer_all_ports_config_info.to_dict()
            )

        locate_enable = self.locate_enable

        used_functions: list[str] | Unset = UNSET
        if not isinstance(self.used_functions, Unset):
            used_functions = self.used_functions

        is_copper = self.is_copper

        oui_based_vlan_networks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oui_based_vlan_networks, Unset):
            oui_based_vlan_networks = self.oui_based_vlan_networks.to_dict()

        stack_support = self.stack_support

        stack_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_setting, Unset):
            stack_setting = self.stack_setting.to_dict()

        stack_id = self.stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if config_stack is not UNSET:
            field_dict["configStack"] = config_stack
        if stack_ports_group_index is not UNSET:
            field_dict["stackPortsGroupIndex"] = stack_ports_group_index
        if switch_id is not UNSET:
            field_dict["switchId"] = switch_id
        if switch_mac is not UNSET:
            field_dict["switchMac"] = switch_mac
        if site is not UNSET:
            field_dict["site"] = site
        if name is not UNSET:
            field_dict["name"] = name
        if disable is not UNSET:
            field_dict["disable"] = disable
        if type_ is not UNSET:
            field_dict["type"] = type_
        if max_speed is not UNSET:
            field_dict["maxSpeed"] = max_speed
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
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if profile_override_enable is not UNSET:
            field_dict["profileOverrideEnable"] = profile_override_enable
        if profile_vlan_override_enable is not UNSET:
            field_dict["profileVlanOverrideEnable"] = profile_vlan_override_enable
        if operation is not UNSET:
            field_dict["operation"] = operation
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if mirrored_lags is not UNSET:
            field_dict["mirroredLags"] = mirrored_lags
        if aggregating_ports is not UNSET:
            field_dict["aggregatingPorts"] = aggregating_ports
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
        if all_aggregating_st_ports is not UNSET:
            field_dict["allAggregatingStPorts"] = all_aggregating_st_ports
        if all_mirroring_st_ports is not UNSET:
            field_dict["allMirroringStPorts"] = all_mirroring_st_ports
        if all_mirrored_st_ports is not UNSET:
            field_dict["allMirroredStPorts"] = all_mirrored_st_ports
        if lag_setting is not UNSET:
            field_dict["lagSetting"] = lag_setting
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if igmp_snooping_enable is not UNSET:
            field_dict["igmpSnoopingEnable"] = igmp_snooping_enable
        if dot1x is not UNSET:
            field_dict["dot1x"] = dot1x
        if mad_used is not UNSET:
            field_dict["madUsed"] = mad_used
        if es_enable_all_profile_can_add is not UNSET:
            field_dict["esEnableAllProfileCanAdd"] = es_enable_all_profile_can_add
        if support_poe is not UNSET:
            field_dict["supportPoe"] = support_poe
        if support_locate is not UNSET:
            field_dict["supportLocate"] = support_locate
        if poe_display_type is not UNSET:
            field_dict["poeDisplayType"] = poe_display_type
        if poe is not UNSET:
            field_dict["poe"] = poe
        if band_width_ctrl_type is not UNSET:
            field_dict["bandWidthCtrlType"] = band_width_ctrl_type
        if band_ctrl is not UNSET:
            field_dict["bandCtrl"] = band_ctrl
        if storm_ctrl is not UNSET:
            field_dict["stormCtrl"] = storm_ctrl
        if lldp_med_enable is not UNSET:
            field_dict["lldpMedEnable"] = lldp_med_enable
        if topo_notify_enable is not UNSET:
            field_dict["topoNotifyEnable"] = topo_notify_enable
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
        if port_status is not UNSET:
            field_dict["portStatus"] = port_status
        if speed is not UNSET:
            field_dict["speed"] = speed
        if lag_status is not UNSET:
            field_dict["lagStatus"] = lag_status
        if port_cap is not UNSET:
            field_dict["portCap"] = port_cap
        if port_speed_cap is not UNSET:
            field_dict["portSpeedCap"] = port_speed_cap
        if eee_enable is not UNSET:
            field_dict["eeeEnable"] = eee_enable
        if flow_control_enable is not UNSET:
            field_dict["flowControlEnable"] = flow_control_enable
        if extend_mode_support is not UNSET:
            field_dict["extendModeSupport"] = extend_mode_support
        if extend_mode_enable is not UNSET:
            field_dict["extendModeEnable"] = extend_mode_enable
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
        if network_conflict is not UNSET:
            field_dict["networkConflict"] = network_conflict
        if resource is not UNSET:
            field_dict["resource"] = resource
        if port_alert_enable is not UNSET:
            field_dict["portAlertEnable"] = port_alert_enable
        if fec_support is not UNSET:
            field_dict["fecSupport"] = fec_support
        if fec_cap is not UNSET:
            field_dict["fecCap"] = fec_cap
        if fec_mode is not UNSET:
            field_dict["fecMode"] = fec_mode
        if fec_link_peer_apply_enable is not UNSET:
            field_dict["fecLinkPeerApplyEnable"] = fec_link_peer_apply_enable
        if config_mlag_peer_link is not UNSET:
            field_dict["configMlagPeerLink"] = config_mlag_peer_link
        if config_mlag_dad is not UNSET:
            field_dict["configMlagDad"] = config_mlag_dad
        if mlag_peer_all_ports_config_info is not UNSET:
            field_dict["mlagPeerAllPortsConfigInfo"] = mlag_peer_all_ports_config_info
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if used_functions is not UNSET:
            field_dict["usedFunctions"] = used_functions
        if is_copper is not UNSET:
            field_dict["isCopper"] = is_copper
        if oui_based_vlan_networks is not UNSET:
            field_dict["ouiBasedVlanNetworks"] = oui_based_vlan_networks
        if stack_support is not UNSET:
            field_dict["stackSupport"] = stack_support
        if stack_setting is not UNSET:
            field_dict["stackSetting"] = stack_setting
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mirrored_lag import MirroredLag
        from ..models.mirrored_port import MirroredPort
        from ..models.osw_band_ctrl_vo import OswBandCtrlVO
        from ..models.osw_fec_cap_vo import OswFecCapVO
        from ..models.osw_lag_status_vo import OswLagStatusVO
        from ..models.osw_lag_vo import OswLagVO
        from ..models.osw_link_cap_vo import OswLinkCapVO
        from ..models.osw_mlag_peer_all_ports_config_info_vo import (
            OswMlagPeerAllPortsConfigInfoVO,
        )
        from ..models.osw_port_dhcp_l2_relay_vo import (
            OswPortDhcpL2RelayVO,
        )
        from ..models.osw_port_oui_based_vlan_vo import (
            OswPortOuiBasedVlanVO,
        )
        from ..models.osw_port_speed_cap_vo import OswPortSpeedCapVO
        from ..models.osw_port_stack_setting_vo import (
            OswPortStackSettingVO,
        )
        from ..models.osw_port_status_vo import OswPortStatusVO
        from ..models.osw_stack_member_port_vo_tag_bridge_vlan_map import (
            OswStackMemberPortVOTagBridgeVlanMap,
        )
        from ..models.osw_stack_member_port_vo_untag_bridge_vlan_map import (
            OswStackMemberPortVOUntagBridgeVlanMap,
        )
        from ..models.osw_stand_port_vo import OswStandPortVO
        from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
        from ..models.spanning_tree_setting_vo import (
            SpanningTreeSettingVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        port = d.pop("port", UNSET)

        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        config_stack = d.pop("configStack", UNSET)

        stack_ports_group_index = d.pop("stackPortsGroupIndex", UNSET)

        switch_id = d.pop("switchId", UNSET)

        switch_mac = d.pop("switchMac", UNSET)

        site = d.pop("site", UNSET)

        name = d.pop("name", UNSET)

        disable = d.pop("disable", UNSET)

        type_ = d.pop("type", UNSET)

        max_speed = d.pop("maxSpeed", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        tag_name = d.pop("tagName", UNSET)

        network_mode = d.pop("networkMode", UNSET)

        native_network_id = d.pop("nativeNetworkId", UNSET)

        native_bridge_vlan = d.pop("nativeBridgeVlan", UNSET)

        network_tags_setting = d.pop("networkTagsSetting", UNSET)

        tag_network_ids = cast(list[str], d.pop("tagNetworkIds", UNSET))

        _tag_bridge_vlan_map = d.pop("tagBridgeVlanMap", UNSET)
        tag_bridge_vlan_map: OswStackMemberPortVOTagBridgeVlanMap | Unset
        if isinstance(_tag_bridge_vlan_map, Unset):
            tag_bridge_vlan_map = UNSET
        else:
            tag_bridge_vlan_map = OswStackMemberPortVOTagBridgeVlanMap.from_dict(
                _tag_bridge_vlan_map
            )

        untag_network_ids = cast(list[str], d.pop("untagNetworkIds", UNSET))

        _untag_bridge_vlan_map = d.pop("untagBridgeVlanMap", UNSET)
        untag_bridge_vlan_map: OswStackMemberPortVOUntagBridgeVlanMap | Unset
        if isinstance(_untag_bridge_vlan_map, Unset):
            untag_bridge_vlan_map = UNSET
        else:
            untag_bridge_vlan_map = OswStackMemberPortVOUntagBridgeVlanMap.from_dict(
                _untag_bridge_vlan_map
            )

        voice_network_enable = d.pop("voiceNetworkEnable", UNSET)

        voice_network_id = d.pop("voiceNetworkId", UNSET)

        voice_bridge_vlan = d.pop("voiceBridgeVlan", UNSET)

        voice_dscp_enable = d.pop("voiceDscpEnable", UNSET)

        voice_dscp = d.pop("voiceDscp", UNSET)

        profile_id = d.pop("profileId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        profile_override_enable = d.pop("profileOverrideEnable", UNSET)

        profile_vlan_override_enable = d.pop("profileVlanOverrideEnable", UNSET)

        operation = d.pop("operation", UNSET)

        _mirrored_ports = d.pop("mirroredPorts", UNSET)
        mirrored_ports: list[MirroredPort] | Unset = UNSET
        if _mirrored_ports is not UNSET:
            mirrored_ports = []
            for mirrored_ports_item_data in _mirrored_ports:
                mirrored_ports_item = MirroredPort.from_dict(mirrored_ports_item_data)

                mirrored_ports.append(mirrored_ports_item)

        _mirrored_lags = d.pop("mirroredLags", UNSET)
        mirrored_lags: list[MirroredLag] | Unset = UNSET
        if _mirrored_lags is not UNSET:
            mirrored_lags = []
            for mirrored_lags_item_data in _mirrored_lags:
                mirrored_lags_item = MirroredLag.from_dict(mirrored_lags_item_data)

                mirrored_lags.append(mirrored_lags_item)

        aggregating_ports = cast(list[int], d.pop("aggregatingPorts", UNSET))

        all_aggregating_ports = cast(list[int], d.pop("allAggregatingPorts", UNSET))

        all_mirroring_ports = cast(list[int], d.pop("allMirroringPorts", UNSET))

        all_mirrored_ports = cast(list[int], d.pop("allMirroredPorts", UNSET))

        all_mlag_peer_link_ports = cast(list[int], d.pop("allMlagPeerLinkPorts", UNSET))

        all_mlag_dad_ports = cast(list[int], d.pop("allMlagDadPorts", UNSET))

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

        _lag_setting = d.pop("lagSetting", UNSET)
        lag_setting: OswLagVO | Unset
        if isinstance(_lag_setting, Unset):
            lag_setting = UNSET
        else:
            lag_setting = OswLagVO.from_dict(_lag_setting)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        igmp_snooping_enable = d.pop("igmpSnoopingEnable", UNSET)

        dot1x = d.pop("dot1x", UNSET)

        mad_used = d.pop("madUsed", UNSET)

        es_enable_all_profile_can_add = d.pop("esEnableAllProfileCanAdd", UNSET)

        support_poe = d.pop("supportPoe", UNSET)

        support_locate = d.pop("supportLocate", UNSET)

        poe_display_type = d.pop("poeDisplayType", UNSET)

        poe = d.pop("poe", UNSET)

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

        lldp_med_enable = d.pop("lldpMedEnable", UNSET)

        topo_notify_enable = d.pop("topoNotifyEnable", UNSET)

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

        _port_status = d.pop("portStatus", UNSET)
        port_status: OswPortStatusVO | Unset
        if isinstance(_port_status, Unset):
            port_status = UNSET
        else:
            port_status = OswPortStatusVO.from_dict(_port_status)

        speed = d.pop("speed", UNSET)

        _lag_status = d.pop("lagStatus", UNSET)
        lag_status: OswLagStatusVO | Unset
        if isinstance(_lag_status, Unset):
            lag_status = UNSET
        else:
            lag_status = OswLagStatusVO.from_dict(_lag_status)

        _port_cap = d.pop("portCap", UNSET)
        port_cap: list[OswLinkCapVO] | Unset = UNSET
        if _port_cap is not UNSET:
            port_cap = []
            for port_cap_item_data in _port_cap:
                port_cap_item = OswLinkCapVO.from_dict(port_cap_item_data)

                port_cap.append(port_cap_item)

        _port_speed_cap = d.pop("portSpeedCap", UNSET)
        port_speed_cap: list[OswPortSpeedCapVO] | Unset = UNSET
        if _port_speed_cap is not UNSET:
            port_speed_cap = []
            for port_speed_cap_item_data in _port_speed_cap:
                port_speed_cap_item = OswPortSpeedCapVO.from_dict(
                    port_speed_cap_item_data
                )

                port_speed_cap.append(port_speed_cap_item)

        eee_enable = d.pop("eeeEnable", UNSET)

        flow_control_enable = d.pop("flowControlEnable", UNSET)

        extend_mode_support = d.pop("extendModeSupport", UNSET)

        extend_mode_enable = d.pop("extendModeEnable", UNSET)

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

        network_conflict = d.pop("networkConflict", UNSET)

        resource = d.pop("resource", UNSET)

        port_alert_enable = d.pop("portAlertEnable", UNSET)

        fec_support = d.pop("fecSupport", UNSET)

        _fec_cap = d.pop("fecCap", UNSET)
        fec_cap: list[OswFecCapVO] | Unset = UNSET
        if _fec_cap is not UNSET:
            fec_cap = []
            for fec_cap_item_data in _fec_cap:
                fec_cap_item = OswFecCapVO.from_dict(fec_cap_item_data)

                fec_cap.append(fec_cap_item)

        fec_mode = d.pop("fecMode", UNSET)

        fec_link_peer_apply_enable = d.pop("fecLinkPeerApplyEnable", UNSET)

        config_mlag_peer_link = d.pop("configMlagPeerLink", UNSET)

        config_mlag_dad = d.pop("configMlagDad", UNSET)

        _mlag_peer_all_ports_config_info = d.pop("mlagPeerAllPortsConfigInfo", UNSET)
        mlag_peer_all_ports_config_info: OswMlagPeerAllPortsConfigInfoVO | Unset
        if isinstance(_mlag_peer_all_ports_config_info, Unset):
            mlag_peer_all_ports_config_info = UNSET
        else:
            mlag_peer_all_ports_config_info = OswMlagPeerAllPortsConfigInfoVO.from_dict(
                _mlag_peer_all_ports_config_info
            )

        locate_enable = d.pop("locateEnable", UNSET)

        used_functions = cast(list[str], d.pop("usedFunctions", UNSET))

        is_copper = d.pop("isCopper", UNSET)

        _oui_based_vlan_networks = d.pop("ouiBasedVlanNetworks", UNSET)
        oui_based_vlan_networks: OswPortOuiBasedVlanVO | Unset
        if isinstance(_oui_based_vlan_networks, Unset):
            oui_based_vlan_networks = UNSET
        else:
            oui_based_vlan_networks = OswPortOuiBasedVlanVO.from_dict(
                _oui_based_vlan_networks
            )

        stack_support = d.pop("stackSupport", UNSET)

        _stack_setting = d.pop("stackSetting", UNSET)
        stack_setting: OswPortStackSettingVO | Unset
        if isinstance(_stack_setting, Unset):
            stack_setting = UNSET
        else:
            stack_setting = OswPortStackSettingVO.from_dict(_stack_setting)

        stack_id = d.pop("stackId", UNSET)

        osw_stack_member_port_vo = cls(
            id=id,
            port=port,
            standard_port=standard_port,
            config_stack=config_stack,
            stack_ports_group_index=stack_ports_group_index,
            switch_id=switch_id,
            switch_mac=switch_mac,
            site=site,
            name=name,
            disable=disable,
            type_=type_,
            max_speed=max_speed,
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
            profile_id=profile_id,
            profile_name=profile_name,
            profile_override_enable=profile_override_enable,
            profile_vlan_override_enable=profile_vlan_override_enable,
            operation=operation,
            mirrored_ports=mirrored_ports,
            mirrored_lags=mirrored_lags,
            aggregating_ports=aggregating_ports,
            all_aggregating_ports=all_aggregating_ports,
            all_mirroring_ports=all_mirroring_ports,
            all_mirrored_ports=all_mirrored_ports,
            all_mlag_peer_link_ports=all_mlag_peer_link_ports,
            all_mlag_dad_ports=all_mlag_dad_ports,
            all_aggregating_st_ports=all_aggregating_st_ports,
            all_mirroring_st_ports=all_mirroring_st_ports,
            all_mirrored_st_ports=all_mirrored_st_ports,
            lag_setting=lag_setting,
            link_speed=link_speed,
            duplex=duplex,
            igmp_snooping_enable=igmp_snooping_enable,
            dot1x=dot1x,
            mad_used=mad_used,
            es_enable_all_profile_can_add=es_enable_all_profile_can_add,
            support_poe=support_poe,
            support_locate=support_locate,
            poe_display_type=poe_display_type,
            poe=poe,
            band_width_ctrl_type=band_width_ctrl_type,
            band_ctrl=band_ctrl,
            storm_ctrl=storm_ctrl,
            lldp_med_enable=lldp_med_enable,
            topo_notify_enable=topo_notify_enable,
            spanning_tree_enable=spanning_tree_enable,
            spanning_tree_setting=spanning_tree_setting,
            loopback_detect_enable=loopback_detect_enable,
            loopback_detect_vlan_based_enable=loopback_detect_vlan_based_enable,
            igmp_fast_leave_enable=igmp_fast_leave_enable,
            mld_fast_leave_enable=mld_fast_leave_enable,
            port_isolation_enable=port_isolation_enable,
            port_status=port_status,
            speed=speed,
            lag_status=lag_status,
            port_cap=port_cap,
            port_speed_cap=port_speed_cap,
            eee_enable=eee_enable,
            flow_control_enable=flow_control_enable,
            extend_mode_support=extend_mode_support,
            extend_mode_enable=extend_mode_enable,
            fast_leave_enable=fast_leave_enable,
            dhcp_l2_relay_settings=dhcp_l2_relay_settings,
            dot_1_p_priority=dot_1_p_priority,
            trust_mode=trust_mode,
            qos_support=qos_support,
            es_qos_support=es_qos_support,
            qos_queue_enable=qos_queue_enable,
            queue_id=queue_id,
            network_conflict=network_conflict,
            resource=resource,
            port_alert_enable=port_alert_enable,
            fec_support=fec_support,
            fec_cap=fec_cap,
            fec_mode=fec_mode,
            fec_link_peer_apply_enable=fec_link_peer_apply_enable,
            config_mlag_peer_link=config_mlag_peer_link,
            config_mlag_dad=config_mlag_dad,
            mlag_peer_all_ports_config_info=mlag_peer_all_ports_config_info,
            locate_enable=locate_enable,
            used_functions=used_functions,
            is_copper=is_copper,
            oui_based_vlan_networks=oui_based_vlan_networks,
            stack_support=stack_support,
            stack_setting=stack_setting,
            stack_id=stack_id,
        )

        osw_stack_member_port_vo.additional_properties = d
        return osw_stack_member_port_vo

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
