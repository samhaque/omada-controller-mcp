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
    from ..models.osw_port_stack_setting_vo import OswPortStackSettingVO
    from ..models.osw_storm_ctrl_open_api_vo import OswStormCtrlOpenApiVO
    from ..models.spanning_tree_setting_vo import SpanningTreeSettingVO


T = TypeVar("T", bound="OswPortSettingOpenApiVO")


@_attrs_define
class OswPortSettingOpenApiVO:
    """
    Attributes:
        profile_override_enable (bool): Indicates whether to enable Profile Override
        mac (str | Unset): The device mac to which the port belongs
        name (str | Unset): Port name
        profile_id (str | Unset): Lan Profile ID
        operation (str | Unset): Operation should be a value as follows: SWITCHING; MIRRORING; AGGREGATING
        mirrored_ports (list[int] | Unset): Monitored Port
        mirrored_lags (list[int] | Unset): Monitored LAG
        lag_setting (OswLagBasicVO | Unset): Lag Setting
        link_speed (int | Unset): LinkSpeed should be a value as follows: 0: Auto; 1: 10M; 2: 100M; 3: 1000M; 4: 2500M;
            5: 10G; 6: 5G; 7: 25G; 8: 100G; 9: 40G.
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
        dot1x (int | Unset): Dot1x should be a value as follows: 0: Force unauthorized; 1: Force authorized; 2: Auto
        poe (int | Unset): PoE switch should be a value as follows: 0: Off; 1: 802.3at/af
        band_width_ctrl_type (int | Unset): BandWidthCtrlType should be a value as follows: 0: Off; 1: Rate Limit; 2:
            Storming Control
        band_ctrl (OswBandCtrlVO | Unset): Speed Limit
        storm_ctrl (OswStormCtrlOpenApiVO | Unset): Storm Control
        lldp_med_enable (bool | Unset): LLDP-MED enable status
        topo_notify_enable (bool | Unset): TopoNotify enable status
        spanning_tree_enable (bool | Unset): SpanningTree enable status
        spanning_tree_setting (SpanningTreeSettingVO | Unset): SpanningTree Setting
        loopback_detect_enable (bool | Unset): LoopbackDetect enable status
        loopback_detect_vlan_based_enable (bool | Unset): LoopbackDetectVLANBased enable status
        igmp_fast_leave_enable (bool | Unset): Indicates whether igmp fast leave is enabled
        mld_fast_leave_enable (bool | Unset): Indicates whether mld fast leave is enabled
        port_isolation_enable (bool | Unset): Port-isolation enable status
        eee_enable (bool | Unset): EEE enable status
        flow_control_enable (bool | Unset): FlowControl enable status
        fast_leave_enable (bool | Unset): Indicates whether igmpSnooping fastLeave is enabled
        dhcp_l2_relay_settings (OswPortDhcpL2RelayVO | Unset): Dhcp L2 Relay Setting
        stack_setting (OswPortStackSettingVO | Unset): Port Stack Setting
        dot_1_p_priority (int | Unset): Dot1p Priority
        trust_mode (int | Unset): TrustMode should be a value as follows: 0: Untrusted; 1: Trust 802.1p; 2: Trust DSCP
    """

    profile_override_enable: bool
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    profile_id: str | Unset = UNSET
    operation: str | Unset = UNSET
    mirrored_ports: list[int] | Unset = UNSET
    mirrored_lags: list[int] | Unset = UNSET
    lag_setting: OswLagBasicVO | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    dot1x: int | Unset = UNSET
    poe: int | Unset = UNSET
    band_width_ctrl_type: int | Unset = UNSET
    band_ctrl: OswBandCtrlVO | Unset = UNSET
    storm_ctrl: OswStormCtrlOpenApiVO | Unset = UNSET
    lldp_med_enable: bool | Unset = UNSET
    topo_notify_enable: bool | Unset = UNSET
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
    stack_setting: OswPortStackSettingVO | Unset = UNSET
    dot_1_p_priority: int | Unset = UNSET
    trust_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_override_enable = self.profile_override_enable

        mac = self.mac

        name = self.name

        profile_id = self.profile_id

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

        link_speed = self.link_speed

        duplex = self.duplex

        dot1x = self.dot1x

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

        eee_enable = self.eee_enable

        flow_control_enable = self.flow_control_enable

        fast_leave_enable = self.fast_leave_enable

        dhcp_l2_relay_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_l2_relay_settings, Unset):
            dhcp_l2_relay_settings = self.dhcp_l2_relay_settings.to_dict()

        stack_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_setting, Unset):
            stack_setting = self.stack_setting.to_dict()

        dot_1_p_priority = self.dot_1_p_priority

        trust_mode = self.trust_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileOverrideEnable": profile_override_enable,
            }
        )
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if mirrored_lags is not UNSET:
            field_dict["mirroredLags"] = mirrored_lags
        if lag_setting is not UNSET:
            field_dict["lagSetting"] = lag_setting
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if dot1x is not UNSET:
            field_dict["dot1x"] = dot1x
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
        if eee_enable is not UNSET:
            field_dict["eeeEnable"] = eee_enable
        if flow_control_enable is not UNSET:
            field_dict["flowControlEnable"] = flow_control_enable
        if fast_leave_enable is not UNSET:
            field_dict["fastLeaveEnable"] = fast_leave_enable
        if dhcp_l2_relay_settings is not UNSET:
            field_dict["dhcpL2RelaySettings"] = dhcp_l2_relay_settings
        if stack_setting is not UNSET:
            field_dict["stackSetting"] = stack_setting
        if dot_1_p_priority is not UNSET:
            field_dict["dot1pPriority"] = dot_1_p_priority
        if trust_mode is not UNSET:
            field_dict["trustMode"] = trust_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_band_ctrl_vo import OswBandCtrlVO
        from ..models.osw_lag_basic_vo import OswLagBasicVO
        from ..models.osw_port_dhcp_l2_relay_vo import (
            OswPortDhcpL2RelayVO,
        )
        from ..models.osw_port_stack_setting_vo import (
            OswPortStackSettingVO,
        )
        from ..models.osw_storm_ctrl_open_api_vo import (
            OswStormCtrlOpenApiVO,
        )
        from ..models.spanning_tree_setting_vo import (
            SpanningTreeSettingVO,
        )

        d = dict(src_dict)
        profile_override_enable = d.pop("profileOverrideEnable")

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        profile_id = d.pop("profileId", UNSET)

        operation = d.pop("operation", UNSET)

        mirrored_ports = cast(list[int], d.pop("mirroredPorts", UNSET))

        mirrored_lags = cast(list[int], d.pop("mirroredLags", UNSET))

        _lag_setting = d.pop("lagSetting", UNSET)
        lag_setting: OswLagBasicVO | Unset
        if isinstance(_lag_setting, Unset):
            lag_setting = UNSET
        else:
            lag_setting = OswLagBasicVO.from_dict(_lag_setting)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        dot1x = d.pop("dot1x", UNSET)

        poe = d.pop("poe", UNSET)

        band_width_ctrl_type = d.pop("bandWidthCtrlType", UNSET)

        _band_ctrl = d.pop("bandCtrl", UNSET)
        band_ctrl: OswBandCtrlVO | Unset
        if isinstance(_band_ctrl, Unset):
            band_ctrl = UNSET
        else:
            band_ctrl = OswBandCtrlVO.from_dict(_band_ctrl)

        _storm_ctrl = d.pop("stormCtrl", UNSET)
        storm_ctrl: OswStormCtrlOpenApiVO | Unset
        if isinstance(_storm_ctrl, Unset):
            storm_ctrl = UNSET
        else:
            storm_ctrl = OswStormCtrlOpenApiVO.from_dict(_storm_ctrl)

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

        _stack_setting = d.pop("stackSetting", UNSET)
        stack_setting: OswPortStackSettingVO | Unset
        if isinstance(_stack_setting, Unset):
            stack_setting = UNSET
        else:
            stack_setting = OswPortStackSettingVO.from_dict(_stack_setting)

        dot_1_p_priority = d.pop("dot1pPriority", UNSET)

        trust_mode = d.pop("trustMode", UNSET)

        osw_port_setting_open_api_vo = cls(
            profile_override_enable=profile_override_enable,
            mac=mac,
            name=name,
            profile_id=profile_id,
            operation=operation,
            mirrored_ports=mirrored_ports,
            mirrored_lags=mirrored_lags,
            lag_setting=lag_setting,
            link_speed=link_speed,
            duplex=duplex,
            dot1x=dot1x,
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
            eee_enable=eee_enable,
            flow_control_enable=flow_control_enable,
            fast_leave_enable=fast_leave_enable,
            dhcp_l2_relay_settings=dhcp_l2_relay_settings,
            stack_setting=stack_setting,
            dot_1_p_priority=dot_1_p_priority,
            trust_mode=trust_mode,
        )

        osw_port_setting_open_api_vo.additional_properties = d
        return osw_port_setting_open_api_vo

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
