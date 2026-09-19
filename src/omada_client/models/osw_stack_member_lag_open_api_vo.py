from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_band_ctrl_vo import OswBandCtrlVO
    from ..models.osw_port_dhcp_l2_relay_vo import OswPortDhcpL2RelayVO
    from ..models.osw_stand_port_vo import OswStandPortVO
    from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
    from ..models.spanning_tree_setting_vo import SpanningTreeSettingVO


T = TypeVar("T", bound="OswStackMemberLagOpenApiVO")


@_attrs_define
class OswStackMemberLagOpenApiVO:
    """
    Attributes:
        profile_override_enable (bool): Indicates whether to enable Profile Override
        name (str | Unset): Lag Name
        profile_id (str | Unset): Profile ID
        link_speed (int | Unset): Link Speed should be a value as follows: 0: auto; 1: 10M; 2: 100M; 3: 1000M; 4: 2.5G;
            5: 10G
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
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
        standard_ports (list[OswStandPortVO] | Unset): LAG Standard ports
    """

    profile_override_enable: bool
    name: str | Unset = UNSET
    profile_id: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
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
    standard_ports: list[OswStandPortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_override_enable = self.profile_override_enable

        name = self.name

        profile_id = self.profile_id

        link_speed = self.link_speed

        duplex = self.duplex

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

        standard_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = []
            for standard_ports_item_data in self.standard_ports:
                standard_ports_item = standard_ports_item_data.to_dict()
                standard_ports.append(standard_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileOverrideEnable": profile_override_enable,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
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
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_band_ctrl_vo import OswBandCtrlVO
        from ..models.osw_port_dhcp_l2_relay_vo import (
            OswPortDhcpL2RelayVO,
        )
        from ..models.osw_stand_port_vo import OswStandPortVO
        from ..models.osw_storm_ctrl_vo import OswStormCtrlVO
        from ..models.spanning_tree_setting_vo import (
            SpanningTreeSettingVO,
        )

        d = dict(src_dict)
        profile_override_enable = d.pop("profileOverrideEnable")

        name = d.pop("name", UNSET)

        profile_id = d.pop("profileId", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

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

        _standard_ports = d.pop("standardPorts", UNSET)
        standard_ports: list[OswStandPortVO] | Unset = UNSET
        if _standard_ports is not UNSET:
            standard_ports = []
            for standard_ports_item_data in _standard_ports:
                standard_ports_item = OswStandPortVO.from_dict(standard_ports_item_data)

                standard_ports.append(standard_ports_item)

        osw_stack_member_lag_open_api_vo = cls(
            profile_override_enable=profile_override_enable,
            name=name,
            profile_id=profile_id,
            link_speed=link_speed,
            duplex=duplex,
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
            standard_ports=standard_ports,
        )

        osw_stack_member_lag_open_api_vo.additional_properties = d
        return osw_stack_member_lag_open_api_vo

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
