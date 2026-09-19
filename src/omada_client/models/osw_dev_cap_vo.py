from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lag_cap_vo import LagCapVO
    from ..models.osw_dev_cap_vo_stack_port_cap import OswDevCapVOStackPortCap


T = TypeVar("T", bound="OswDevCapVO")


@_attrs_define
class OswDevCapVO:
    """Capability of device

    Attributes:
        max_mirror_group (int | Unset): Max Mirror Group
        max_mirrored_port (int | Unset): Max Mirrored Port
        max_lag_num (int | Unset): Max Lag Num
        max_lag_member (int | Unset): Max Lacp Member
        poe_port_num (int | Unset): Poe Port Num
        mstp_ins_num (int | Unset): Mstp Instance Num
        mstp_ins_no (int | Unset): Mstp Max InstanceId
        rpvst_ins_num (int | Unset): Max Rpvst Instance Num
        vlan_if_num (int | Unset): Vlan Interface Num
        poe_support (bool | Unset): Poe Support
        support_fan (bool | Unset): Support Fan
        support_bt (bool | Unset): Support Poe Bt
        jumbo_support (bool | Unset): Jumbo Support
        jumbo_odd_support (bool | Unset): Jumbo Odd Support
        support_multicast (bool | Unset): Whether support multicast
        support_es_multicast (bool | Unset): Whether Agile Series Switch support multicast
        support_dhcp_snoop (bool | Unset): Whether support dhcp snoop
        support_arp_detect (bool | Unset): Whether support arp detect
        support_impb (bool | Unset): Whether support impb
        support_layout (bool | Unset): Whether the device supports reporting port layout information.
        lag_cap (LagCapVO | Unset): Capability of lag
        fec_support (bool | Unset): FEC Support
        eee_support (bool | Unset): eee Support
        flow_control_support (bool | Unset): FlowControl Support
        storm_rate_mode_support (bool | Unset): StormControl RateMode Support
        igmp_fast_leave_support (bool | Unset): Igmp FastLeve Support
        loopback_vlan_based_support (bool | Unset): Loopback Detect Vlan Based Support
        dhcp_l2_relay_support (bool | Unset): Dhcp L2 Relay Support
        ospf_support (bool | Unset): OSPF Support
        ospf_dead_interval_support (bool | Unset): OSPF Dead Interval Support
        ospf_auto_cost_ref_support (bool | Unset): OSPF Process Auto-Cost Reference Bandwidth Support
        ospf_passive_support (bool | Unset): OSPF Interface Passive Support
        loopback_interface_support (bool | Unset): Loopback Interface Support
        loopback_interface_create_support (bool | Unset): Loopback Interface Create Support
        pmtud_support (bool | Unset): Path MTU Discovery Support
        mtu_in_vlan_support (bool | Unset): MTU In VLAN Support
        qos_support (bool | Unset): QoS Support
        es_qos_support (bool | Unset): Agile Series Switch QoS Support
        qos_for_vlan_support (bool | Unset): Qos for Vlan Support
        ddm_support (bool | Unset): DDM Support
        ipc_detect_support (bool | Unset): IPC Detect Support
        custom_dhcp_option_support (bool | Unset): Custom DHCP Option Support
        voice_network_support (bool | Unset): Voice Network Support
        voice_dscp_support (bool | Unset): Voice DSCP Support
        snmp_support (bool | Unset): SNMP Support
        sfp_begin_num (int | Unset): SFP Begin Num
        sfp_num (int | Unset): SFP Num
        vrrp_support (bool | Unset): Vrrp Support
        stp_support (bool | Unset): STP Support
        stp_extend_support (bool | Unset): STP Extend Support
        es_stp_extend_support (bool | Unset): ES STP Extend Support
        rpvst_extend_support (bool | Unset): RPVST Extend Support
        mstp_port_support (bool | Unset): MSTP Port Support
        mstp_get_active_support (bool | Unset): MSTP Get Active Support
        mirror_support (bool | Unset): Mirror Support
        uplink_support (bool | Unset): Uplink Support
        gpon_support (bool | Unset): Gpon Support
        network_check_support (bool | Unset): Network Check Support
        ping_support (bool | Unset): Ping Support
        traceroute_support (bool | Unset): Traceroute Support
        dns_loop_up_support (bool | Unset): DNS Loop Up Support
        arp_table_support (bool | Unset): Arp Table Support
        packet_capture_support (bool | Unset): Packet Capture Support
        terminal_support (bool | Unset): Terminal Support
        cable_test_support (bool | Unset): Cable Test Support
        domain_ping_support (bool | Unset): Domain Ping Support
        domain_trace_route_support (bool | Unset): Domain Trace Route Support
        dhcp_range_support (bool | Unset): Whether the device supports DHCP server address pool
        dhcp_reservation_support (bool | Unset): Whether the device supports DHCP reservation
        support_get_dhcp_client_table (bool | Unset): Whether the device supports getting DHCP client table via get
            message
        support_get_dhcp_server_info (bool | Unset): Whether the device supports getting DHCP server info via get
            message
        support_get_vlan_if_info (bool | Unset): Whether the device supports getting VLAN interface info via get message
        dhcp_server_pool_num (int | Unset): DHCP Server Pool Num
        dhcp_relay_if_num (int | Unset): DHCP Relay Interface Num
        dhcp_manual_bind_num (int | Unset): DHCP Manual Bind Num
        ipv_4_static_route_num (int | Unset): IPv4 Static Route Num
        ipv_6_static_route_num (int | Unset): IPv6 Static Route Num
        static_route_num (int | Unset): Static Route Num
        support_es_health (bool | Unset): Whether the device supports ES health check
        support_relay_multi_server (bool | Unset): Whether the device supports DHCP relay multi Server
        support_tpcl_res_info (bool | Unset): Whether the device supports returning TPCL resource information
        max_relay_server_num (int | Unset): Max DHCP relay server num
        oui_based_vlan_support (bool | Unset): Oui Based Vlan Support
        oui_based_vlan_es_support (bool | Unset): Oui Based Vlan Support
        locate_port_support (bool | Unset): Locate port Support
        support_clear_counters (bool | Unset): Whether the device supports clear counters
        cli_support (bool | Unset): CLI Support
        support_config_sync (bool | Unset): Whether the device supports config sync
        support_running_config (bool | Unset): Whether the device supports showing running config
        need_full_sync (bool | Unset): Need full sync
        max_stack_group_number (int | Unset): Max Stack Group Number
        max_stack_unit_number (int | Unset): Max Stack Unit Number
        stkable_group_id (int | Unset): Stackable Group ID
        stk_ver (str | Unset): Stack Version
        vrf_num (int | Unset): VRF Num
        mlag_group_id (int | Unset): MLAG Group ID
        mlag_version (str | Unset): MLAG Version
        support_vrf (bool | Unset): Whether the device supports VRF
        support_sdm (bool | Unset): Whether the device supports SDM
        support_mlag (bool | Unset): Whether the device supports MLAG
        support_mad (bool | Unset): Whether the device supports MAD
        stack_port_cap (OswDevCapVOStackPortCap | Unset): Stack Port Capability
        support_get_ospf_neighbor_table (bool | Unset): Whether the device supports getting OSPF neighbor table via get
            message
    """

    max_mirror_group: int | Unset = UNSET
    max_mirrored_port: int | Unset = UNSET
    max_lag_num: int | Unset = UNSET
    max_lag_member: int | Unset = UNSET
    poe_port_num: int | Unset = UNSET
    mstp_ins_num: int | Unset = UNSET
    mstp_ins_no: int | Unset = UNSET
    rpvst_ins_num: int | Unset = UNSET
    vlan_if_num: int | Unset = UNSET
    poe_support: bool | Unset = UNSET
    support_fan: bool | Unset = UNSET
    support_bt: bool | Unset = UNSET
    jumbo_support: bool | Unset = UNSET
    jumbo_odd_support: bool | Unset = UNSET
    support_multicast: bool | Unset = UNSET
    support_es_multicast: bool | Unset = UNSET
    support_dhcp_snoop: bool | Unset = UNSET
    support_arp_detect: bool | Unset = UNSET
    support_impb: bool | Unset = UNSET
    support_layout: bool | Unset = UNSET
    lag_cap: LagCapVO | Unset = UNSET
    fec_support: bool | Unset = UNSET
    eee_support: bool | Unset = UNSET
    flow_control_support: bool | Unset = UNSET
    storm_rate_mode_support: bool | Unset = UNSET
    igmp_fast_leave_support: bool | Unset = UNSET
    loopback_vlan_based_support: bool | Unset = UNSET
    dhcp_l2_relay_support: bool | Unset = UNSET
    ospf_support: bool | Unset = UNSET
    ospf_dead_interval_support: bool | Unset = UNSET
    ospf_auto_cost_ref_support: bool | Unset = UNSET
    ospf_passive_support: bool | Unset = UNSET
    loopback_interface_support: bool | Unset = UNSET
    loopback_interface_create_support: bool | Unset = UNSET
    pmtud_support: bool | Unset = UNSET
    mtu_in_vlan_support: bool | Unset = UNSET
    qos_support: bool | Unset = UNSET
    es_qos_support: bool | Unset = UNSET
    qos_for_vlan_support: bool | Unset = UNSET
    ddm_support: bool | Unset = UNSET
    ipc_detect_support: bool | Unset = UNSET
    custom_dhcp_option_support: bool | Unset = UNSET
    voice_network_support: bool | Unset = UNSET
    voice_dscp_support: bool | Unset = UNSET
    snmp_support: bool | Unset = UNSET
    sfp_begin_num: int | Unset = UNSET
    sfp_num: int | Unset = UNSET
    vrrp_support: bool | Unset = UNSET
    stp_support: bool | Unset = UNSET
    stp_extend_support: bool | Unset = UNSET
    es_stp_extend_support: bool | Unset = UNSET
    rpvst_extend_support: bool | Unset = UNSET
    mstp_port_support: bool | Unset = UNSET
    mstp_get_active_support: bool | Unset = UNSET
    mirror_support: bool | Unset = UNSET
    uplink_support: bool | Unset = UNSET
    gpon_support: bool | Unset = UNSET
    network_check_support: bool | Unset = UNSET
    ping_support: bool | Unset = UNSET
    traceroute_support: bool | Unset = UNSET
    dns_loop_up_support: bool | Unset = UNSET
    arp_table_support: bool | Unset = UNSET
    packet_capture_support: bool | Unset = UNSET
    terminal_support: bool | Unset = UNSET
    cable_test_support: bool | Unset = UNSET
    domain_ping_support: bool | Unset = UNSET
    domain_trace_route_support: bool | Unset = UNSET
    dhcp_range_support: bool | Unset = UNSET
    dhcp_reservation_support: bool | Unset = UNSET
    support_get_dhcp_client_table: bool | Unset = UNSET
    support_get_dhcp_server_info: bool | Unset = UNSET
    support_get_vlan_if_info: bool | Unset = UNSET
    dhcp_server_pool_num: int | Unset = UNSET
    dhcp_relay_if_num: int | Unset = UNSET
    dhcp_manual_bind_num: int | Unset = UNSET
    ipv_4_static_route_num: int | Unset = UNSET
    ipv_6_static_route_num: int | Unset = UNSET
    static_route_num: int | Unset = UNSET
    support_es_health: bool | Unset = UNSET
    support_relay_multi_server: bool | Unset = UNSET
    support_tpcl_res_info: bool | Unset = UNSET
    max_relay_server_num: int | Unset = UNSET
    oui_based_vlan_support: bool | Unset = UNSET
    oui_based_vlan_es_support: bool | Unset = UNSET
    locate_port_support: bool | Unset = UNSET
    support_clear_counters: bool | Unset = UNSET
    cli_support: bool | Unset = UNSET
    support_config_sync: bool | Unset = UNSET
    support_running_config: bool | Unset = UNSET
    need_full_sync: bool | Unset = UNSET
    max_stack_group_number: int | Unset = UNSET
    max_stack_unit_number: int | Unset = UNSET
    stkable_group_id: int | Unset = UNSET
    stk_ver: str | Unset = UNSET
    vrf_num: int | Unset = UNSET
    mlag_group_id: int | Unset = UNSET
    mlag_version: str | Unset = UNSET
    support_vrf: bool | Unset = UNSET
    support_sdm: bool | Unset = UNSET
    support_mlag: bool | Unset = UNSET
    support_mad: bool | Unset = UNSET
    stack_port_cap: OswDevCapVOStackPortCap | Unset = UNSET
    support_get_ospf_neighbor_table: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_mirror_group = self.max_mirror_group

        max_mirrored_port = self.max_mirrored_port

        max_lag_num = self.max_lag_num

        max_lag_member = self.max_lag_member

        poe_port_num = self.poe_port_num

        mstp_ins_num = self.mstp_ins_num

        mstp_ins_no = self.mstp_ins_no

        rpvst_ins_num = self.rpvst_ins_num

        vlan_if_num = self.vlan_if_num

        poe_support = self.poe_support

        support_fan = self.support_fan

        support_bt = self.support_bt

        jumbo_support = self.jumbo_support

        jumbo_odd_support = self.jumbo_odd_support

        support_multicast = self.support_multicast

        support_es_multicast = self.support_es_multicast

        support_dhcp_snoop = self.support_dhcp_snoop

        support_arp_detect = self.support_arp_detect

        support_impb = self.support_impb

        support_layout = self.support_layout

        lag_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_cap, Unset):
            lag_cap = self.lag_cap.to_dict()

        fec_support = self.fec_support

        eee_support = self.eee_support

        flow_control_support = self.flow_control_support

        storm_rate_mode_support = self.storm_rate_mode_support

        igmp_fast_leave_support = self.igmp_fast_leave_support

        loopback_vlan_based_support = self.loopback_vlan_based_support

        dhcp_l2_relay_support = self.dhcp_l2_relay_support

        ospf_support = self.ospf_support

        ospf_dead_interval_support = self.ospf_dead_interval_support

        ospf_auto_cost_ref_support = self.ospf_auto_cost_ref_support

        ospf_passive_support = self.ospf_passive_support

        loopback_interface_support = self.loopback_interface_support

        loopback_interface_create_support = self.loopback_interface_create_support

        pmtud_support = self.pmtud_support

        mtu_in_vlan_support = self.mtu_in_vlan_support

        qos_support = self.qos_support

        es_qos_support = self.es_qos_support

        qos_for_vlan_support = self.qos_for_vlan_support

        ddm_support = self.ddm_support

        ipc_detect_support = self.ipc_detect_support

        custom_dhcp_option_support = self.custom_dhcp_option_support

        voice_network_support = self.voice_network_support

        voice_dscp_support = self.voice_dscp_support

        snmp_support = self.snmp_support

        sfp_begin_num = self.sfp_begin_num

        sfp_num = self.sfp_num

        vrrp_support = self.vrrp_support

        stp_support = self.stp_support

        stp_extend_support = self.stp_extend_support

        es_stp_extend_support = self.es_stp_extend_support

        rpvst_extend_support = self.rpvst_extend_support

        mstp_port_support = self.mstp_port_support

        mstp_get_active_support = self.mstp_get_active_support

        mirror_support = self.mirror_support

        uplink_support = self.uplink_support

        gpon_support = self.gpon_support

        network_check_support = self.network_check_support

        ping_support = self.ping_support

        traceroute_support = self.traceroute_support

        dns_loop_up_support = self.dns_loop_up_support

        arp_table_support = self.arp_table_support

        packet_capture_support = self.packet_capture_support

        terminal_support = self.terminal_support

        cable_test_support = self.cable_test_support

        domain_ping_support = self.domain_ping_support

        domain_trace_route_support = self.domain_trace_route_support

        dhcp_range_support = self.dhcp_range_support

        dhcp_reservation_support = self.dhcp_reservation_support

        support_get_dhcp_client_table = self.support_get_dhcp_client_table

        support_get_dhcp_server_info = self.support_get_dhcp_server_info

        support_get_vlan_if_info = self.support_get_vlan_if_info

        dhcp_server_pool_num = self.dhcp_server_pool_num

        dhcp_relay_if_num = self.dhcp_relay_if_num

        dhcp_manual_bind_num = self.dhcp_manual_bind_num

        ipv_4_static_route_num = self.ipv_4_static_route_num

        ipv_6_static_route_num = self.ipv_6_static_route_num

        static_route_num = self.static_route_num

        support_es_health = self.support_es_health

        support_relay_multi_server = self.support_relay_multi_server

        support_tpcl_res_info = self.support_tpcl_res_info

        max_relay_server_num = self.max_relay_server_num

        oui_based_vlan_support = self.oui_based_vlan_support

        oui_based_vlan_es_support = self.oui_based_vlan_es_support

        locate_port_support = self.locate_port_support

        support_clear_counters = self.support_clear_counters

        cli_support = self.cli_support

        support_config_sync = self.support_config_sync

        support_running_config = self.support_running_config

        need_full_sync = self.need_full_sync

        max_stack_group_number = self.max_stack_group_number

        max_stack_unit_number = self.max_stack_unit_number

        stkable_group_id = self.stkable_group_id

        stk_ver = self.stk_ver

        vrf_num = self.vrf_num

        mlag_group_id = self.mlag_group_id

        mlag_version = self.mlag_version

        support_vrf = self.support_vrf

        support_sdm = self.support_sdm

        support_mlag = self.support_mlag

        support_mad = self.support_mad

        stack_port_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_port_cap, Unset):
            stack_port_cap = self.stack_port_cap.to_dict()

        support_get_ospf_neighbor_table = self.support_get_ospf_neighbor_table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_mirror_group is not UNSET:
            field_dict["maxMirrorGroup"] = max_mirror_group
        if max_mirrored_port is not UNSET:
            field_dict["maxMirroredPort"] = max_mirrored_port
        if max_lag_num is not UNSET:
            field_dict["maxLagNum"] = max_lag_num
        if max_lag_member is not UNSET:
            field_dict["maxLagMember"] = max_lag_member
        if poe_port_num is not UNSET:
            field_dict["poePortNum"] = poe_port_num
        if mstp_ins_num is not UNSET:
            field_dict["mstpInsNum"] = mstp_ins_num
        if mstp_ins_no is not UNSET:
            field_dict["mstpInsNo"] = mstp_ins_no
        if rpvst_ins_num is not UNSET:
            field_dict["rpvstInsNum"] = rpvst_ins_num
        if vlan_if_num is not UNSET:
            field_dict["vlanIfNum"] = vlan_if_num
        if poe_support is not UNSET:
            field_dict["poeSupport"] = poe_support
        if support_fan is not UNSET:
            field_dict["supportFan"] = support_fan
        if support_bt is not UNSET:
            field_dict["supportBt"] = support_bt
        if jumbo_support is not UNSET:
            field_dict["jumboSupport"] = jumbo_support
        if jumbo_odd_support is not UNSET:
            field_dict["jumboOddSupport"] = jumbo_odd_support
        if support_multicast is not UNSET:
            field_dict["supportMulticast"] = support_multicast
        if support_es_multicast is not UNSET:
            field_dict["supportEsMulticast"] = support_es_multicast
        if support_dhcp_snoop is not UNSET:
            field_dict["supportDhcpSnoop"] = support_dhcp_snoop
        if support_arp_detect is not UNSET:
            field_dict["supportArpDetect"] = support_arp_detect
        if support_impb is not UNSET:
            field_dict["supportImpb"] = support_impb
        if support_layout is not UNSET:
            field_dict["supportLayout"] = support_layout
        if lag_cap is not UNSET:
            field_dict["lagCap"] = lag_cap
        if fec_support is not UNSET:
            field_dict["fecSupport"] = fec_support
        if eee_support is not UNSET:
            field_dict["eeeSupport"] = eee_support
        if flow_control_support is not UNSET:
            field_dict["flowControlSupport"] = flow_control_support
        if storm_rate_mode_support is not UNSET:
            field_dict["stormRateModeSupport"] = storm_rate_mode_support
        if igmp_fast_leave_support is not UNSET:
            field_dict["igmpFastLeaveSupport"] = igmp_fast_leave_support
        if loopback_vlan_based_support is not UNSET:
            field_dict["loopbackVlanBasedSupport"] = loopback_vlan_based_support
        if dhcp_l2_relay_support is not UNSET:
            field_dict["dhcpL2RelaySupport"] = dhcp_l2_relay_support
        if ospf_support is not UNSET:
            field_dict["ospfSupport"] = ospf_support
        if ospf_dead_interval_support is not UNSET:
            field_dict["ospfDeadIntervalSupport"] = ospf_dead_interval_support
        if ospf_auto_cost_ref_support is not UNSET:
            field_dict["ospfAutoCostRefSupport"] = ospf_auto_cost_ref_support
        if ospf_passive_support is not UNSET:
            field_dict["ospfPassiveSupport"] = ospf_passive_support
        if loopback_interface_support is not UNSET:
            field_dict["loopbackInterfaceSupport"] = loopback_interface_support
        if loopback_interface_create_support is not UNSET:
            field_dict["loopbackInterfaceCreateSupport"] = (
                loopback_interface_create_support
            )
        if pmtud_support is not UNSET:
            field_dict["pmtudSupport"] = pmtud_support
        if mtu_in_vlan_support is not UNSET:
            field_dict["mtuInVlanSupport"] = mtu_in_vlan_support
        if qos_support is not UNSET:
            field_dict["qosSupport"] = qos_support
        if es_qos_support is not UNSET:
            field_dict["esQosSupport"] = es_qos_support
        if qos_for_vlan_support is not UNSET:
            field_dict["qosForVlanSupport"] = qos_for_vlan_support
        if ddm_support is not UNSET:
            field_dict["ddmSupport"] = ddm_support
        if ipc_detect_support is not UNSET:
            field_dict["ipcDetectSupport"] = ipc_detect_support
        if custom_dhcp_option_support is not UNSET:
            field_dict["customDhcpOptionSupport"] = custom_dhcp_option_support
        if voice_network_support is not UNSET:
            field_dict["voiceNetworkSupport"] = voice_network_support
        if voice_dscp_support is not UNSET:
            field_dict["voiceDscpSupport"] = voice_dscp_support
        if snmp_support is not UNSET:
            field_dict["snmpSupport"] = snmp_support
        if sfp_begin_num is not UNSET:
            field_dict["sfpBeginNum"] = sfp_begin_num
        if sfp_num is not UNSET:
            field_dict["sfpNum"] = sfp_num
        if vrrp_support is not UNSET:
            field_dict["vrrpSupport"] = vrrp_support
        if stp_support is not UNSET:
            field_dict["stpSupport"] = stp_support
        if stp_extend_support is not UNSET:
            field_dict["stpExtendSupport"] = stp_extend_support
        if es_stp_extend_support is not UNSET:
            field_dict["esStpExtendSupport"] = es_stp_extend_support
        if rpvst_extend_support is not UNSET:
            field_dict["rpvstExtendSupport"] = rpvst_extend_support
        if mstp_port_support is not UNSET:
            field_dict["mstpPortSupport"] = mstp_port_support
        if mstp_get_active_support is not UNSET:
            field_dict["mstpGetActiveSupport"] = mstp_get_active_support
        if mirror_support is not UNSET:
            field_dict["mirrorSupport"] = mirror_support
        if uplink_support is not UNSET:
            field_dict["uplinkSupport"] = uplink_support
        if gpon_support is not UNSET:
            field_dict["gponSupport"] = gpon_support
        if network_check_support is not UNSET:
            field_dict["networkCheckSupport"] = network_check_support
        if ping_support is not UNSET:
            field_dict["pingSupport"] = ping_support
        if traceroute_support is not UNSET:
            field_dict["tracerouteSupport"] = traceroute_support
        if dns_loop_up_support is not UNSET:
            field_dict["dnsLoopUpSupport"] = dns_loop_up_support
        if arp_table_support is not UNSET:
            field_dict["arpTableSupport"] = arp_table_support
        if packet_capture_support is not UNSET:
            field_dict["packetCaptureSupport"] = packet_capture_support
        if terminal_support is not UNSET:
            field_dict["terminalSupport"] = terminal_support
        if cable_test_support is not UNSET:
            field_dict["cableTestSupport"] = cable_test_support
        if domain_ping_support is not UNSET:
            field_dict["domainPingSupport"] = domain_ping_support
        if domain_trace_route_support is not UNSET:
            field_dict["domainTraceRouteSupport"] = domain_trace_route_support
        if dhcp_range_support is not UNSET:
            field_dict["dhcpRangeSupport"] = dhcp_range_support
        if dhcp_reservation_support is not UNSET:
            field_dict["dhcpReservationSupport"] = dhcp_reservation_support
        if support_get_dhcp_client_table is not UNSET:
            field_dict["supportGetDhcpClientTable"] = support_get_dhcp_client_table
        if support_get_dhcp_server_info is not UNSET:
            field_dict["supportGetDhcpServerInfo"] = support_get_dhcp_server_info
        if support_get_vlan_if_info is not UNSET:
            field_dict["supportGetVlanIfInfo"] = support_get_vlan_if_info
        if dhcp_server_pool_num is not UNSET:
            field_dict["dhcpServerPoolNum"] = dhcp_server_pool_num
        if dhcp_relay_if_num is not UNSET:
            field_dict["dhcpRelayIfNum"] = dhcp_relay_if_num
        if dhcp_manual_bind_num is not UNSET:
            field_dict["dhcpManualBindNum"] = dhcp_manual_bind_num
        if ipv_4_static_route_num is not UNSET:
            field_dict["ipv4StaticRouteNum"] = ipv_4_static_route_num
        if ipv_6_static_route_num is not UNSET:
            field_dict["ipv6StaticRouteNum"] = ipv_6_static_route_num
        if static_route_num is not UNSET:
            field_dict["staticRouteNum"] = static_route_num
        if support_es_health is not UNSET:
            field_dict["supportEsHealth"] = support_es_health
        if support_relay_multi_server is not UNSET:
            field_dict["supportRelayMultiServer"] = support_relay_multi_server
        if support_tpcl_res_info is not UNSET:
            field_dict["supportTpclResInfo"] = support_tpcl_res_info
        if max_relay_server_num is not UNSET:
            field_dict["maxRelayServerNum"] = max_relay_server_num
        if oui_based_vlan_support is not UNSET:
            field_dict["ouiBasedVlanSupport"] = oui_based_vlan_support
        if oui_based_vlan_es_support is not UNSET:
            field_dict["ouiBasedVlanESSupport"] = oui_based_vlan_es_support
        if locate_port_support is not UNSET:
            field_dict["locatePortSupport"] = locate_port_support
        if support_clear_counters is not UNSET:
            field_dict["supportClearCounters"] = support_clear_counters
        if cli_support is not UNSET:
            field_dict["cliSupport"] = cli_support
        if support_config_sync is not UNSET:
            field_dict["supportConfigSync"] = support_config_sync
        if support_running_config is not UNSET:
            field_dict["supportRunningConfig"] = support_running_config
        if need_full_sync is not UNSET:
            field_dict["needFullSync"] = need_full_sync
        if max_stack_group_number is not UNSET:
            field_dict["maxStackGroupNumber"] = max_stack_group_number
        if max_stack_unit_number is not UNSET:
            field_dict["maxStackUnitNumber"] = max_stack_unit_number
        if stkable_group_id is not UNSET:
            field_dict["stkableGroupId"] = stkable_group_id
        if stk_ver is not UNSET:
            field_dict["stkVer"] = stk_ver
        if vrf_num is not UNSET:
            field_dict["vrfNum"] = vrf_num
        if mlag_group_id is not UNSET:
            field_dict["mlagGroupId"] = mlag_group_id
        if mlag_version is not UNSET:
            field_dict["mlagVersion"] = mlag_version
        if support_vrf is not UNSET:
            field_dict["supportVrf"] = support_vrf
        if support_sdm is not UNSET:
            field_dict["supportSdm"] = support_sdm
        if support_mlag is not UNSET:
            field_dict["supportMlag"] = support_mlag
        if support_mad is not UNSET:
            field_dict["supportMad"] = support_mad
        if stack_port_cap is not UNSET:
            field_dict["stackPortCap"] = stack_port_cap
        if support_get_ospf_neighbor_table is not UNSET:
            field_dict["supportGetOspfNeighborTable"] = support_get_ospf_neighbor_table

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lag_cap_vo import LagCapVO
        from ..models.osw_dev_cap_vo_stack_port_cap import (
            OswDevCapVOStackPortCap,
        )

        d = dict(src_dict)
        max_mirror_group = d.pop("maxMirrorGroup", UNSET)

        max_mirrored_port = d.pop("maxMirroredPort", UNSET)

        max_lag_num = d.pop("maxLagNum", UNSET)

        max_lag_member = d.pop("maxLagMember", UNSET)

        poe_port_num = d.pop("poePortNum", UNSET)

        mstp_ins_num = d.pop("mstpInsNum", UNSET)

        mstp_ins_no = d.pop("mstpInsNo", UNSET)

        rpvst_ins_num = d.pop("rpvstInsNum", UNSET)

        vlan_if_num = d.pop("vlanIfNum", UNSET)

        poe_support = d.pop("poeSupport", UNSET)

        support_fan = d.pop("supportFan", UNSET)

        support_bt = d.pop("supportBt", UNSET)

        jumbo_support = d.pop("jumboSupport", UNSET)

        jumbo_odd_support = d.pop("jumboOddSupport", UNSET)

        support_multicast = d.pop("supportMulticast", UNSET)

        support_es_multicast = d.pop("supportEsMulticast", UNSET)

        support_dhcp_snoop = d.pop("supportDhcpSnoop", UNSET)

        support_arp_detect = d.pop("supportArpDetect", UNSET)

        support_impb = d.pop("supportImpb", UNSET)

        support_layout = d.pop("supportLayout", UNSET)

        _lag_cap = d.pop("lagCap", UNSET)
        lag_cap: LagCapVO | Unset
        if isinstance(_lag_cap, Unset):
            lag_cap = UNSET
        else:
            lag_cap = LagCapVO.from_dict(_lag_cap)

        fec_support = d.pop("fecSupport", UNSET)

        eee_support = d.pop("eeeSupport", UNSET)

        flow_control_support = d.pop("flowControlSupport", UNSET)

        storm_rate_mode_support = d.pop("stormRateModeSupport", UNSET)

        igmp_fast_leave_support = d.pop("igmpFastLeaveSupport", UNSET)

        loopback_vlan_based_support = d.pop("loopbackVlanBasedSupport", UNSET)

        dhcp_l2_relay_support = d.pop("dhcpL2RelaySupport", UNSET)

        ospf_support = d.pop("ospfSupport", UNSET)

        ospf_dead_interval_support = d.pop("ospfDeadIntervalSupport", UNSET)

        ospf_auto_cost_ref_support = d.pop("ospfAutoCostRefSupport", UNSET)

        ospf_passive_support = d.pop("ospfPassiveSupport", UNSET)

        loopback_interface_support = d.pop("loopbackInterfaceSupport", UNSET)

        loopback_interface_create_support = d.pop(
            "loopbackInterfaceCreateSupport", UNSET
        )

        pmtud_support = d.pop("pmtudSupport", UNSET)

        mtu_in_vlan_support = d.pop("mtuInVlanSupport", UNSET)

        qos_support = d.pop("qosSupport", UNSET)

        es_qos_support = d.pop("esQosSupport", UNSET)

        qos_for_vlan_support = d.pop("qosForVlanSupport", UNSET)

        ddm_support = d.pop("ddmSupport", UNSET)

        ipc_detect_support = d.pop("ipcDetectSupport", UNSET)

        custom_dhcp_option_support = d.pop("customDhcpOptionSupport", UNSET)

        voice_network_support = d.pop("voiceNetworkSupport", UNSET)

        voice_dscp_support = d.pop("voiceDscpSupport", UNSET)

        snmp_support = d.pop("snmpSupport", UNSET)

        sfp_begin_num = d.pop("sfpBeginNum", UNSET)

        sfp_num = d.pop("sfpNum", UNSET)

        vrrp_support = d.pop("vrrpSupport", UNSET)

        stp_support = d.pop("stpSupport", UNSET)

        stp_extend_support = d.pop("stpExtendSupport", UNSET)

        es_stp_extend_support = d.pop("esStpExtendSupport", UNSET)

        rpvst_extend_support = d.pop("rpvstExtendSupport", UNSET)

        mstp_port_support = d.pop("mstpPortSupport", UNSET)

        mstp_get_active_support = d.pop("mstpGetActiveSupport", UNSET)

        mirror_support = d.pop("mirrorSupport", UNSET)

        uplink_support = d.pop("uplinkSupport", UNSET)

        gpon_support = d.pop("gponSupport", UNSET)

        network_check_support = d.pop("networkCheckSupport", UNSET)

        ping_support = d.pop("pingSupport", UNSET)

        traceroute_support = d.pop("tracerouteSupport", UNSET)

        dns_loop_up_support = d.pop("dnsLoopUpSupport", UNSET)

        arp_table_support = d.pop("arpTableSupport", UNSET)

        packet_capture_support = d.pop("packetCaptureSupport", UNSET)

        terminal_support = d.pop("terminalSupport", UNSET)

        cable_test_support = d.pop("cableTestSupport", UNSET)

        domain_ping_support = d.pop("domainPingSupport", UNSET)

        domain_trace_route_support = d.pop("domainTraceRouteSupport", UNSET)

        dhcp_range_support = d.pop("dhcpRangeSupport", UNSET)

        dhcp_reservation_support = d.pop("dhcpReservationSupport", UNSET)

        support_get_dhcp_client_table = d.pop("supportGetDhcpClientTable", UNSET)

        support_get_dhcp_server_info = d.pop("supportGetDhcpServerInfo", UNSET)

        support_get_vlan_if_info = d.pop("supportGetVlanIfInfo", UNSET)

        dhcp_server_pool_num = d.pop("dhcpServerPoolNum", UNSET)

        dhcp_relay_if_num = d.pop("dhcpRelayIfNum", UNSET)

        dhcp_manual_bind_num = d.pop("dhcpManualBindNum", UNSET)

        ipv_4_static_route_num = d.pop("ipv4StaticRouteNum", UNSET)

        ipv_6_static_route_num = d.pop("ipv6StaticRouteNum", UNSET)

        static_route_num = d.pop("staticRouteNum", UNSET)

        support_es_health = d.pop("supportEsHealth", UNSET)

        support_relay_multi_server = d.pop("supportRelayMultiServer", UNSET)

        support_tpcl_res_info = d.pop("supportTpclResInfo", UNSET)

        max_relay_server_num = d.pop("maxRelayServerNum", UNSET)

        oui_based_vlan_support = d.pop("ouiBasedVlanSupport", UNSET)

        oui_based_vlan_es_support = d.pop("ouiBasedVlanESSupport", UNSET)

        locate_port_support = d.pop("locatePortSupport", UNSET)

        support_clear_counters = d.pop("supportClearCounters", UNSET)

        cli_support = d.pop("cliSupport", UNSET)

        support_config_sync = d.pop("supportConfigSync", UNSET)

        support_running_config = d.pop("supportRunningConfig", UNSET)

        need_full_sync = d.pop("needFullSync", UNSET)

        max_stack_group_number = d.pop("maxStackGroupNumber", UNSET)

        max_stack_unit_number = d.pop("maxStackUnitNumber", UNSET)

        stkable_group_id = d.pop("stkableGroupId", UNSET)

        stk_ver = d.pop("stkVer", UNSET)

        vrf_num = d.pop("vrfNum", UNSET)

        mlag_group_id = d.pop("mlagGroupId", UNSET)

        mlag_version = d.pop("mlagVersion", UNSET)

        support_vrf = d.pop("supportVrf", UNSET)

        support_sdm = d.pop("supportSdm", UNSET)

        support_mlag = d.pop("supportMlag", UNSET)

        support_mad = d.pop("supportMad", UNSET)

        _stack_port_cap = d.pop("stackPortCap", UNSET)
        stack_port_cap: OswDevCapVOStackPortCap | Unset
        if isinstance(_stack_port_cap, Unset):
            stack_port_cap = UNSET
        else:
            stack_port_cap = OswDevCapVOStackPortCap.from_dict(_stack_port_cap)

        support_get_ospf_neighbor_table = d.pop("supportGetOspfNeighborTable", UNSET)

        osw_dev_cap_vo = cls(
            max_mirror_group=max_mirror_group,
            max_mirrored_port=max_mirrored_port,
            max_lag_num=max_lag_num,
            max_lag_member=max_lag_member,
            poe_port_num=poe_port_num,
            mstp_ins_num=mstp_ins_num,
            mstp_ins_no=mstp_ins_no,
            rpvst_ins_num=rpvst_ins_num,
            vlan_if_num=vlan_if_num,
            poe_support=poe_support,
            support_fan=support_fan,
            support_bt=support_bt,
            jumbo_support=jumbo_support,
            jumbo_odd_support=jumbo_odd_support,
            support_multicast=support_multicast,
            support_es_multicast=support_es_multicast,
            support_dhcp_snoop=support_dhcp_snoop,
            support_arp_detect=support_arp_detect,
            support_impb=support_impb,
            support_layout=support_layout,
            lag_cap=lag_cap,
            fec_support=fec_support,
            eee_support=eee_support,
            flow_control_support=flow_control_support,
            storm_rate_mode_support=storm_rate_mode_support,
            igmp_fast_leave_support=igmp_fast_leave_support,
            loopback_vlan_based_support=loopback_vlan_based_support,
            dhcp_l2_relay_support=dhcp_l2_relay_support,
            ospf_support=ospf_support,
            ospf_dead_interval_support=ospf_dead_interval_support,
            ospf_auto_cost_ref_support=ospf_auto_cost_ref_support,
            ospf_passive_support=ospf_passive_support,
            loopback_interface_support=loopback_interface_support,
            loopback_interface_create_support=loopback_interface_create_support,
            pmtud_support=pmtud_support,
            mtu_in_vlan_support=mtu_in_vlan_support,
            qos_support=qos_support,
            es_qos_support=es_qos_support,
            qos_for_vlan_support=qos_for_vlan_support,
            ddm_support=ddm_support,
            ipc_detect_support=ipc_detect_support,
            custom_dhcp_option_support=custom_dhcp_option_support,
            voice_network_support=voice_network_support,
            voice_dscp_support=voice_dscp_support,
            snmp_support=snmp_support,
            sfp_begin_num=sfp_begin_num,
            sfp_num=sfp_num,
            vrrp_support=vrrp_support,
            stp_support=stp_support,
            stp_extend_support=stp_extend_support,
            es_stp_extend_support=es_stp_extend_support,
            rpvst_extend_support=rpvst_extend_support,
            mstp_port_support=mstp_port_support,
            mstp_get_active_support=mstp_get_active_support,
            mirror_support=mirror_support,
            uplink_support=uplink_support,
            gpon_support=gpon_support,
            network_check_support=network_check_support,
            ping_support=ping_support,
            traceroute_support=traceroute_support,
            dns_loop_up_support=dns_loop_up_support,
            arp_table_support=arp_table_support,
            packet_capture_support=packet_capture_support,
            terminal_support=terminal_support,
            cable_test_support=cable_test_support,
            domain_ping_support=domain_ping_support,
            domain_trace_route_support=domain_trace_route_support,
            dhcp_range_support=dhcp_range_support,
            dhcp_reservation_support=dhcp_reservation_support,
            support_get_dhcp_client_table=support_get_dhcp_client_table,
            support_get_dhcp_server_info=support_get_dhcp_server_info,
            support_get_vlan_if_info=support_get_vlan_if_info,
            dhcp_server_pool_num=dhcp_server_pool_num,
            dhcp_relay_if_num=dhcp_relay_if_num,
            dhcp_manual_bind_num=dhcp_manual_bind_num,
            ipv_4_static_route_num=ipv_4_static_route_num,
            ipv_6_static_route_num=ipv_6_static_route_num,
            static_route_num=static_route_num,
            support_es_health=support_es_health,
            support_relay_multi_server=support_relay_multi_server,
            support_tpcl_res_info=support_tpcl_res_info,
            max_relay_server_num=max_relay_server_num,
            oui_based_vlan_support=oui_based_vlan_support,
            oui_based_vlan_es_support=oui_based_vlan_es_support,
            locate_port_support=locate_port_support,
            support_clear_counters=support_clear_counters,
            cli_support=cli_support,
            support_config_sync=support_config_sync,
            support_running_config=support_running_config,
            need_full_sync=need_full_sync,
            max_stack_group_number=max_stack_group_number,
            max_stack_unit_number=max_stack_unit_number,
            stkable_group_id=stkable_group_id,
            stk_ver=stk_ver,
            vrf_num=vrf_num,
            mlag_group_id=mlag_group_id,
            mlag_version=mlag_version,
            support_vrf=support_vrf,
            support_sdm=support_sdm,
            support_mlag=support_mlag,
            support_mad=support_mad,
            stack_port_cap=stack_port_cap,
            support_get_ospf_neighbor_table=support_get_ospf_neighbor_table,
        )

        osw_dev_cap_vo.additional_properties = d
        return osw_dev_cap_vo

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
