from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_config_result_base_setting_vo import ApConfigResultBaseSettingVO
    from ..models.ap_config_result_port_setting_vo import ApConfigResultPortSettingVO
    from ..models.ap_config_result_radio_setting_vo import ApConfigResultRadioSettingVO


T = TypeVar("T", bound="ApConfigResultSettingsVO")


@_attrs_define
class ApConfigResultSettingsVO:
    """ap config result detail setting.

    Attributes:
        led_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        rssi_led_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        wifi_control_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        gps_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        remote_reset_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        disable_hw_reset_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        enable_slide_switch_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        lb_setting_2_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        lb_setting_5_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        lb_setting_5_g_1 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        lb_setting_5_g_2 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        lb_setting_6_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        rssi_setting_2_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        rssi_setting_5_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        rssi_setting_5_g_1 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        rssi_setting_5_g_2 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        rssi_setting_6_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        qos_setting_2_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        qos_setting_5_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        qos_setting_5_g_1 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        qos_setting_5_g_2 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        qos_setting_6_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        non_psc_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ofdma_enable_2_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ofdma_enable_5_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ofdma_enable_5_g_1 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ofdma_enable_5_g_2 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ofdma_enable_6_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        trunk_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        mvlan_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        snmp_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        l_3_access_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        lldp_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        loopback_detect_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        voip_vlan_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        smart_antenna_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        power_saving_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        antenna_gain_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ant_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ant_setting_2_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ant_setting_5_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ant_setting_5_g_2 (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        ant_setting_6_g (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        wlan_group_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        channel_limit_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        afc_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        radio_setting_2_g (ApConfigResultRadioSettingVO | Unset): radio 6g setting config result
        radio_setting_5_g (ApConfigResultRadioSettingVO | Unset): radio 6g setting config result
        radio_setting_5_g_1 (ApConfigResultRadioSettingVO | Unset): radio 6g setting config result
        radio_setting_5_g_2 (ApConfigResultRadioSettingVO | Unset): radio 6g setting config result
        radio_setting_6_g (ApConfigResultRadioSettingVO | Unset): radio 6g setting config result
        port_setting_list (list[ApConfigResultPortSettingVO] | Unset): port setting config result list
    """

    led_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    rssi_led_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    wifi_control_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    gps_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    remote_reset_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    disable_hw_reset_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    enable_slide_switch_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    lb_setting_2_g: ApConfigResultBaseSettingVO | Unset = UNSET
    lb_setting_5_g: ApConfigResultBaseSettingVO | Unset = UNSET
    lb_setting_5_g_1: ApConfigResultBaseSettingVO | Unset = UNSET
    lb_setting_5_g_2: ApConfigResultBaseSettingVO | Unset = UNSET
    lb_setting_6_g: ApConfigResultBaseSettingVO | Unset = UNSET
    rssi_setting_2_g: ApConfigResultBaseSettingVO | Unset = UNSET
    rssi_setting_5_g: ApConfigResultBaseSettingVO | Unset = UNSET
    rssi_setting_5_g_1: ApConfigResultBaseSettingVO | Unset = UNSET
    rssi_setting_5_g_2: ApConfigResultBaseSettingVO | Unset = UNSET
    rssi_setting_6_g: ApConfigResultBaseSettingVO | Unset = UNSET
    qos_setting_2_g: ApConfigResultBaseSettingVO | Unset = UNSET
    qos_setting_5_g: ApConfigResultBaseSettingVO | Unset = UNSET
    qos_setting_5_g_1: ApConfigResultBaseSettingVO | Unset = UNSET
    qos_setting_5_g_2: ApConfigResultBaseSettingVO | Unset = UNSET
    qos_setting_6_g: ApConfigResultBaseSettingVO | Unset = UNSET
    non_psc_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    ofdma_enable_2_g: ApConfigResultBaseSettingVO | Unset = UNSET
    ofdma_enable_5_g: ApConfigResultBaseSettingVO | Unset = UNSET
    ofdma_enable_5_g_1: ApConfigResultBaseSettingVO | Unset = UNSET
    ofdma_enable_5_g_2: ApConfigResultBaseSettingVO | Unset = UNSET
    ofdma_enable_6_g: ApConfigResultBaseSettingVO | Unset = UNSET
    trunk_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    mvlan_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    snmp_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    l_3_access_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    lldp_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    loopback_detect_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    voip_vlan_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    smart_antenna_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    power_saving_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    antenna_gain_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    ant_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    ant_setting_2_g: ApConfigResultBaseSettingVO | Unset = UNSET
    ant_setting_5_g: ApConfigResultBaseSettingVO | Unset = UNSET
    ant_setting_5_g_2: ApConfigResultBaseSettingVO | Unset = UNSET
    ant_setting_6_g: ApConfigResultBaseSettingVO | Unset = UNSET
    wlan_group_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    channel_limit_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    afc_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    radio_setting_2_g: ApConfigResultRadioSettingVO | Unset = UNSET
    radio_setting_5_g: ApConfigResultRadioSettingVO | Unset = UNSET
    radio_setting_5_g_1: ApConfigResultRadioSettingVO | Unset = UNSET
    radio_setting_5_g_2: ApConfigResultRadioSettingVO | Unset = UNSET
    radio_setting_6_g: ApConfigResultRadioSettingVO | Unset = UNSET
    port_setting_list: list[ApConfigResultPortSettingVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        led_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.led_setting, Unset):
            led_setting = self.led_setting.to_dict()

        rssi_led_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_led_setting, Unset):
            rssi_led_setting = self.rssi_led_setting.to_dict()

        wifi_control_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wifi_control_setting, Unset):
            wifi_control_setting = self.wifi_control_setting.to_dict()

        gps_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gps_setting, Unset):
            gps_setting = self.gps_setting.to_dict()

        remote_reset_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_reset_setting, Unset):
            remote_reset_setting = self.remote_reset_setting.to_dict()

        disable_hw_reset_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_hw_reset_setting, Unset):
            disable_hw_reset_setting = self.disable_hw_reset_setting.to_dict()

        enable_slide_switch_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enable_slide_switch_setting, Unset):
            enable_slide_switch_setting = self.enable_slide_switch_setting.to_dict()

        lb_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_2_g, Unset):
            lb_setting_2_g = self.lb_setting_2_g.to_dict()

        lb_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g, Unset):
            lb_setting_5_g = self.lb_setting_5_g.to_dict()

        lb_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g_1, Unset):
            lb_setting_5_g_1 = self.lb_setting_5_g_1.to_dict()

        lb_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g_2, Unset):
            lb_setting_5_g_2 = self.lb_setting_5_g_2.to_dict()

        lb_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_6_g, Unset):
            lb_setting_6_g = self.lb_setting_6_g.to_dict()

        rssi_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_2_g, Unset):
            rssi_setting_2_g = self.rssi_setting_2_g.to_dict()

        rssi_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_5_g, Unset):
            rssi_setting_5_g = self.rssi_setting_5_g.to_dict()

        rssi_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_5_g_1, Unset):
            rssi_setting_5_g_1 = self.rssi_setting_5_g_1.to_dict()

        rssi_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_5_g_2, Unset):
            rssi_setting_5_g_2 = self.rssi_setting_5_g_2.to_dict()

        rssi_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_6_g, Unset):
            rssi_setting_6_g = self.rssi_setting_6_g.to_dict()

        qos_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_2_g, Unset):
            qos_setting_2_g = self.qos_setting_2_g.to_dict()

        qos_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g, Unset):
            qos_setting_5_g = self.qos_setting_5_g.to_dict()

        qos_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g_1, Unset):
            qos_setting_5_g_1 = self.qos_setting_5_g_1.to_dict()

        qos_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = self.qos_setting_5_g_2.to_dict()

        qos_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_6_g, Unset):
            qos_setting_6_g = self.qos_setting_6_g.to_dict()

        non_psc_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.non_psc_setting, Unset):
            non_psc_setting = self.non_psc_setting.to_dict()

        ofdma_enable_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ofdma_enable_2_g, Unset):
            ofdma_enable_2_g = self.ofdma_enable_2_g.to_dict()

        ofdma_enable_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ofdma_enable_5_g, Unset):
            ofdma_enable_5_g = self.ofdma_enable_5_g.to_dict()

        ofdma_enable_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ofdma_enable_5_g_1, Unset):
            ofdma_enable_5_g_1 = self.ofdma_enable_5_g_1.to_dict()

        ofdma_enable_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ofdma_enable_5_g_2, Unset):
            ofdma_enable_5_g_2 = self.ofdma_enable_5_g_2.to_dict()

        ofdma_enable_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ofdma_enable_6_g, Unset):
            ofdma_enable_6_g = self.ofdma_enable_6_g.to_dict()

        trunk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trunk_setting, Unset):
            trunk_setting = self.trunk_setting.to_dict()

        mvlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mvlan_setting, Unset):
            mvlan_setting = self.mvlan_setting.to_dict()

        snmp_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp_setting, Unset):
            snmp_setting = self.snmp_setting.to_dict()

        l_3_access_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.l_3_access_setting, Unset):
            l_3_access_setting = self.l_3_access_setting.to_dict()

        lldp_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lldp_setting, Unset):
            lldp_setting = self.lldp_setting.to_dict()

        loopback_detect_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loopback_detect_setting, Unset):
            loopback_detect_setting = self.loopback_detect_setting.to_dict()

        voip_vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voip_vlan_setting, Unset):
            voip_vlan_setting = self.voip_vlan_setting.to_dict()

        smart_antenna_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smart_antenna_setting, Unset):
            smart_antenna_setting = self.smart_antenna_setting.to_dict()

        power_saving_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power_saving_setting, Unset):
            power_saving_setting = self.power_saving_setting.to_dict()

        antenna_gain_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.antenna_gain_setting, Unset):
            antenna_gain_setting = self.antenna_gain_setting.to_dict()

        ant_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting, Unset):
            ant_setting = self.ant_setting.to_dict()

        ant_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_2_g, Unset):
            ant_setting_2_g = self.ant_setting_2_g.to_dict()

        ant_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_5_g, Unset):
            ant_setting_5_g = self.ant_setting_5_g.to_dict()

        ant_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_5_g_2, Unset):
            ant_setting_5_g_2 = self.ant_setting_5_g_2.to_dict()

        ant_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_6_g, Unset):
            ant_setting_6_g = self.ant_setting_6_g.to_dict()

        wlan_group_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wlan_group_setting, Unset):
            wlan_group_setting = self.wlan_group_setting.to_dict()

        channel_limit_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_limit_setting, Unset):
            channel_limit_setting = self.channel_limit_setting.to_dict()

        afc_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.afc_setting, Unset):
            afc_setting = self.afc_setting.to_dict()

        radio_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_2_g, Unset):
            radio_setting_2_g = self.radio_setting_2_g.to_dict()

        radio_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g, Unset):
            radio_setting_5_g = self.radio_setting_5_g.to_dict()

        radio_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g_1, Unset):
            radio_setting_5_g_1 = self.radio_setting_5_g_1.to_dict()

        radio_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g_2, Unset):
            radio_setting_5_g_2 = self.radio_setting_5_g_2.to_dict()

        radio_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_6_g, Unset):
            radio_setting_6_g = self.radio_setting_6_g.to_dict()

        port_setting_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_setting_list, Unset):
            port_setting_list = []
            for port_setting_list_item_data in self.port_setting_list:
                port_setting_list_item = port_setting_list_item_data.to_dict()
                port_setting_list.append(port_setting_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if rssi_led_setting is not UNSET:
            field_dict["rssiLedSetting"] = rssi_led_setting
        if wifi_control_setting is not UNSET:
            field_dict["wifiControlSetting"] = wifi_control_setting
        if gps_setting is not UNSET:
            field_dict["gpsSetting"] = gps_setting
        if remote_reset_setting is not UNSET:
            field_dict["remoteResetSetting"] = remote_reset_setting
        if disable_hw_reset_setting is not UNSET:
            field_dict["disableHwResetSetting"] = disable_hw_reset_setting
        if enable_slide_switch_setting is not UNSET:
            field_dict["enableSlideSwitchSetting"] = enable_slide_switch_setting
        if lb_setting_2_g is not UNSET:
            field_dict["lbSetting2g"] = lb_setting_2_g
        if lb_setting_5_g is not UNSET:
            field_dict["lbSetting5g"] = lb_setting_5_g
        if lb_setting_5_g_1 is not UNSET:
            field_dict["lbSetting5g1"] = lb_setting_5_g_1
        if lb_setting_5_g_2 is not UNSET:
            field_dict["lbSetting5g2"] = lb_setting_5_g_2
        if lb_setting_6_g is not UNSET:
            field_dict["lbSetting6g"] = lb_setting_6_g
        if rssi_setting_2_g is not UNSET:
            field_dict["rssiSetting2g"] = rssi_setting_2_g
        if rssi_setting_5_g is not UNSET:
            field_dict["rssiSetting5g"] = rssi_setting_5_g
        if rssi_setting_5_g_1 is not UNSET:
            field_dict["rssiSetting5g1"] = rssi_setting_5_g_1
        if rssi_setting_5_g_2 is not UNSET:
            field_dict["rssiSetting5g2"] = rssi_setting_5_g_2
        if rssi_setting_6_g is not UNSET:
            field_dict["rssiSetting6g"] = rssi_setting_6_g
        if qos_setting_2_g is not UNSET:
            field_dict["qosSetting2g"] = qos_setting_2_g
        if qos_setting_5_g is not UNSET:
            field_dict["qosSetting5g"] = qos_setting_5_g
        if qos_setting_5_g_1 is not UNSET:
            field_dict["qosSetting5g1"] = qos_setting_5_g_1
        if qos_setting_5_g_2 is not UNSET:
            field_dict["qosSetting5g2"] = qos_setting_5_g_2
        if qos_setting_6_g is not UNSET:
            field_dict["qosSetting6g"] = qos_setting_6_g
        if non_psc_setting is not UNSET:
            field_dict["nonPscSetting"] = non_psc_setting
        if ofdma_enable_2_g is not UNSET:
            field_dict["ofdmaEnable2g"] = ofdma_enable_2_g
        if ofdma_enable_5_g is not UNSET:
            field_dict["ofdmaEnable5g"] = ofdma_enable_5_g
        if ofdma_enable_5_g_1 is not UNSET:
            field_dict["ofdmaEnable5g1"] = ofdma_enable_5_g_1
        if ofdma_enable_5_g_2 is not UNSET:
            field_dict["ofdmaEnable5g2"] = ofdma_enable_5_g_2
        if ofdma_enable_6_g is not UNSET:
            field_dict["ofdmaEnable6g"] = ofdma_enable_6_g
        if trunk_setting is not UNSET:
            field_dict["trunkSetting"] = trunk_setting
        if mvlan_setting is not UNSET:
            field_dict["mvlanSetting"] = mvlan_setting
        if snmp_setting is not UNSET:
            field_dict["snmpSetting"] = snmp_setting
        if l_3_access_setting is not UNSET:
            field_dict["l3AccessSetting"] = l_3_access_setting
        if lldp_setting is not UNSET:
            field_dict["lldpSetting"] = lldp_setting
        if loopback_detect_setting is not UNSET:
            field_dict["loopbackDetectSetting"] = loopback_detect_setting
        if voip_vlan_setting is not UNSET:
            field_dict["voipVlanSetting"] = voip_vlan_setting
        if smart_antenna_setting is not UNSET:
            field_dict["smartAntennaSetting"] = smart_antenna_setting
        if power_saving_setting is not UNSET:
            field_dict["powerSavingSetting"] = power_saving_setting
        if antenna_gain_setting is not UNSET:
            field_dict["antennaGainSetting"] = antenna_gain_setting
        if ant_setting is not UNSET:
            field_dict["antSetting"] = ant_setting
        if ant_setting_2_g is not UNSET:
            field_dict["antSetting2g"] = ant_setting_2_g
        if ant_setting_5_g is not UNSET:
            field_dict["antSetting5g"] = ant_setting_5_g
        if ant_setting_5_g_2 is not UNSET:
            field_dict["antSetting5g2"] = ant_setting_5_g_2
        if ant_setting_6_g is not UNSET:
            field_dict["antSetting6g"] = ant_setting_6_g
        if wlan_group_setting is not UNSET:
            field_dict["wlanGroupSetting"] = wlan_group_setting
        if channel_limit_setting is not UNSET:
            field_dict["channelLimitSetting"] = channel_limit_setting
        if afc_setting is not UNSET:
            field_dict["afcSetting"] = afc_setting
        if radio_setting_2_g is not UNSET:
            field_dict["radioSetting2g"] = radio_setting_2_g
        if radio_setting_5_g is not UNSET:
            field_dict["radioSetting5g"] = radio_setting_5_g
        if radio_setting_5_g_1 is not UNSET:
            field_dict["radioSetting5g1"] = radio_setting_5_g_1
        if radio_setting_5_g_2 is not UNSET:
            field_dict["radioSetting5g2"] = radio_setting_5_g_2
        if radio_setting_6_g is not UNSET:
            field_dict["radioSetting6g"] = radio_setting_6_g
        if port_setting_list is not UNSET:
            field_dict["portSettingList"] = port_setting_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_config_result_base_setting_vo import (
            ApConfigResultBaseSettingVO,
        )
        from ..models.ap_config_result_port_setting_vo import (
            ApConfigResultPortSettingVO,
        )
        from ..models.ap_config_result_radio_setting_vo import (
            ApConfigResultRadioSettingVO,
        )

        d = dict(src_dict)
        _led_setting = d.pop("ledSetting", UNSET)
        led_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_led_setting, Unset):
            led_setting = UNSET
        else:
            led_setting = ApConfigResultBaseSettingVO.from_dict(_led_setting)

        _rssi_led_setting = d.pop("rssiLedSetting", UNSET)
        rssi_led_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_rssi_led_setting, Unset):
            rssi_led_setting = UNSET
        else:
            rssi_led_setting = ApConfigResultBaseSettingVO.from_dict(_rssi_led_setting)

        _wifi_control_setting = d.pop("wifiControlSetting", UNSET)
        wifi_control_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_wifi_control_setting, Unset):
            wifi_control_setting = UNSET
        else:
            wifi_control_setting = ApConfigResultBaseSettingVO.from_dict(
                _wifi_control_setting
            )

        _gps_setting = d.pop("gpsSetting", UNSET)
        gps_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_gps_setting, Unset):
            gps_setting = UNSET
        else:
            gps_setting = ApConfigResultBaseSettingVO.from_dict(_gps_setting)

        _remote_reset_setting = d.pop("remoteResetSetting", UNSET)
        remote_reset_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_remote_reset_setting, Unset):
            remote_reset_setting = UNSET
        else:
            remote_reset_setting = ApConfigResultBaseSettingVO.from_dict(
                _remote_reset_setting
            )

        _disable_hw_reset_setting = d.pop("disableHwResetSetting", UNSET)
        disable_hw_reset_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_disable_hw_reset_setting, Unset):
            disable_hw_reset_setting = UNSET
        else:
            disable_hw_reset_setting = ApConfigResultBaseSettingVO.from_dict(
                _disable_hw_reset_setting
            )

        _enable_slide_switch_setting = d.pop("enableSlideSwitchSetting", UNSET)
        enable_slide_switch_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_enable_slide_switch_setting, Unset):
            enable_slide_switch_setting = UNSET
        else:
            enable_slide_switch_setting = ApConfigResultBaseSettingVO.from_dict(
                _enable_slide_switch_setting
            )

        _lb_setting_2_g = d.pop("lbSetting2g", UNSET)
        lb_setting_2_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_lb_setting_2_g, Unset):
            lb_setting_2_g = UNSET
        else:
            lb_setting_2_g = ApConfigResultBaseSettingVO.from_dict(_lb_setting_2_g)

        _lb_setting_5_g = d.pop("lbSetting5g", UNSET)
        lb_setting_5_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_lb_setting_5_g, Unset):
            lb_setting_5_g = UNSET
        else:
            lb_setting_5_g = ApConfigResultBaseSettingVO.from_dict(_lb_setting_5_g)

        _lb_setting_5_g_1 = d.pop("lbSetting5g1", UNSET)
        lb_setting_5_g_1: ApConfigResultBaseSettingVO | Unset
        if isinstance(_lb_setting_5_g_1, Unset):
            lb_setting_5_g_1 = UNSET
        else:
            lb_setting_5_g_1 = ApConfigResultBaseSettingVO.from_dict(_lb_setting_5_g_1)

        _lb_setting_5_g_2 = d.pop("lbSetting5g2", UNSET)
        lb_setting_5_g_2: ApConfigResultBaseSettingVO | Unset
        if isinstance(_lb_setting_5_g_2, Unset):
            lb_setting_5_g_2 = UNSET
        else:
            lb_setting_5_g_2 = ApConfigResultBaseSettingVO.from_dict(_lb_setting_5_g_2)

        _lb_setting_6_g = d.pop("lbSetting6g", UNSET)
        lb_setting_6_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_lb_setting_6_g, Unset):
            lb_setting_6_g = UNSET
        else:
            lb_setting_6_g = ApConfigResultBaseSettingVO.from_dict(_lb_setting_6_g)

        _rssi_setting_2_g = d.pop("rssiSetting2g", UNSET)
        rssi_setting_2_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_rssi_setting_2_g, Unset):
            rssi_setting_2_g = UNSET
        else:
            rssi_setting_2_g = ApConfigResultBaseSettingVO.from_dict(_rssi_setting_2_g)

        _rssi_setting_5_g = d.pop("rssiSetting5g", UNSET)
        rssi_setting_5_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_rssi_setting_5_g, Unset):
            rssi_setting_5_g = UNSET
        else:
            rssi_setting_5_g = ApConfigResultBaseSettingVO.from_dict(_rssi_setting_5_g)

        _rssi_setting_5_g_1 = d.pop("rssiSetting5g1", UNSET)
        rssi_setting_5_g_1: ApConfigResultBaseSettingVO | Unset
        if isinstance(_rssi_setting_5_g_1, Unset):
            rssi_setting_5_g_1 = UNSET
        else:
            rssi_setting_5_g_1 = ApConfigResultBaseSettingVO.from_dict(
                _rssi_setting_5_g_1
            )

        _rssi_setting_5_g_2 = d.pop("rssiSetting5g2", UNSET)
        rssi_setting_5_g_2: ApConfigResultBaseSettingVO | Unset
        if isinstance(_rssi_setting_5_g_2, Unset):
            rssi_setting_5_g_2 = UNSET
        else:
            rssi_setting_5_g_2 = ApConfigResultBaseSettingVO.from_dict(
                _rssi_setting_5_g_2
            )

        _rssi_setting_6_g = d.pop("rssiSetting6g", UNSET)
        rssi_setting_6_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_rssi_setting_6_g, Unset):
            rssi_setting_6_g = UNSET
        else:
            rssi_setting_6_g = ApConfigResultBaseSettingVO.from_dict(_rssi_setting_6_g)

        _qos_setting_2_g = d.pop("qosSetting2g", UNSET)
        qos_setting_2_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_qos_setting_2_g, Unset):
            qos_setting_2_g = UNSET
        else:
            qos_setting_2_g = ApConfigResultBaseSettingVO.from_dict(_qos_setting_2_g)

        _qos_setting_5_g = d.pop("qosSetting5g", UNSET)
        qos_setting_5_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_qos_setting_5_g, Unset):
            qos_setting_5_g = UNSET
        else:
            qos_setting_5_g = ApConfigResultBaseSettingVO.from_dict(_qos_setting_5_g)

        _qos_setting_5_g_1 = d.pop("qosSetting5g1", UNSET)
        qos_setting_5_g_1: ApConfigResultBaseSettingVO | Unset
        if isinstance(_qos_setting_5_g_1, Unset):
            qos_setting_5_g_1 = UNSET
        else:
            qos_setting_5_g_1 = ApConfigResultBaseSettingVO.from_dict(
                _qos_setting_5_g_1
            )

        _qos_setting_5_g_2 = d.pop("qosSetting5g2", UNSET)
        qos_setting_5_g_2: ApConfigResultBaseSettingVO | Unset
        if isinstance(_qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = UNSET
        else:
            qos_setting_5_g_2 = ApConfigResultBaseSettingVO.from_dict(
                _qos_setting_5_g_2
            )

        _qos_setting_6_g = d.pop("qosSetting6g", UNSET)
        qos_setting_6_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_qos_setting_6_g, Unset):
            qos_setting_6_g = UNSET
        else:
            qos_setting_6_g = ApConfigResultBaseSettingVO.from_dict(_qos_setting_6_g)

        _non_psc_setting = d.pop("nonPscSetting", UNSET)
        non_psc_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_non_psc_setting, Unset):
            non_psc_setting = UNSET
        else:
            non_psc_setting = ApConfigResultBaseSettingVO.from_dict(_non_psc_setting)

        _ofdma_enable_2_g = d.pop("ofdmaEnable2g", UNSET)
        ofdma_enable_2_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ofdma_enable_2_g, Unset):
            ofdma_enable_2_g = UNSET
        else:
            ofdma_enable_2_g = ApConfigResultBaseSettingVO.from_dict(_ofdma_enable_2_g)

        _ofdma_enable_5_g = d.pop("ofdmaEnable5g", UNSET)
        ofdma_enable_5_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ofdma_enable_5_g, Unset):
            ofdma_enable_5_g = UNSET
        else:
            ofdma_enable_5_g = ApConfigResultBaseSettingVO.from_dict(_ofdma_enable_5_g)

        _ofdma_enable_5_g_1 = d.pop("ofdmaEnable5g1", UNSET)
        ofdma_enable_5_g_1: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ofdma_enable_5_g_1, Unset):
            ofdma_enable_5_g_1 = UNSET
        else:
            ofdma_enable_5_g_1 = ApConfigResultBaseSettingVO.from_dict(
                _ofdma_enable_5_g_1
            )

        _ofdma_enable_5_g_2 = d.pop("ofdmaEnable5g2", UNSET)
        ofdma_enable_5_g_2: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ofdma_enable_5_g_2, Unset):
            ofdma_enable_5_g_2 = UNSET
        else:
            ofdma_enable_5_g_2 = ApConfigResultBaseSettingVO.from_dict(
                _ofdma_enable_5_g_2
            )

        _ofdma_enable_6_g = d.pop("ofdmaEnable6g", UNSET)
        ofdma_enable_6_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ofdma_enable_6_g, Unset):
            ofdma_enable_6_g = UNSET
        else:
            ofdma_enable_6_g = ApConfigResultBaseSettingVO.from_dict(_ofdma_enable_6_g)

        _trunk_setting = d.pop("trunkSetting", UNSET)
        trunk_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_trunk_setting, Unset):
            trunk_setting = UNSET
        else:
            trunk_setting = ApConfigResultBaseSettingVO.from_dict(_trunk_setting)

        _mvlan_setting = d.pop("mvlanSetting", UNSET)
        mvlan_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_mvlan_setting, Unset):
            mvlan_setting = UNSET
        else:
            mvlan_setting = ApConfigResultBaseSettingVO.from_dict(_mvlan_setting)

        _snmp_setting = d.pop("snmpSetting", UNSET)
        snmp_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_snmp_setting, Unset):
            snmp_setting = UNSET
        else:
            snmp_setting = ApConfigResultBaseSettingVO.from_dict(_snmp_setting)

        _l_3_access_setting = d.pop("l3AccessSetting", UNSET)
        l_3_access_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_l_3_access_setting, Unset):
            l_3_access_setting = UNSET
        else:
            l_3_access_setting = ApConfigResultBaseSettingVO.from_dict(
                _l_3_access_setting
            )

        _lldp_setting = d.pop("lldpSetting", UNSET)
        lldp_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_lldp_setting, Unset):
            lldp_setting = UNSET
        else:
            lldp_setting = ApConfigResultBaseSettingVO.from_dict(_lldp_setting)

        _loopback_detect_setting = d.pop("loopbackDetectSetting", UNSET)
        loopback_detect_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_loopback_detect_setting, Unset):
            loopback_detect_setting = UNSET
        else:
            loopback_detect_setting = ApConfigResultBaseSettingVO.from_dict(
                _loopback_detect_setting
            )

        _voip_vlan_setting = d.pop("voipVlanSetting", UNSET)
        voip_vlan_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_voip_vlan_setting, Unset):
            voip_vlan_setting = UNSET
        else:
            voip_vlan_setting = ApConfigResultBaseSettingVO.from_dict(
                _voip_vlan_setting
            )

        _smart_antenna_setting = d.pop("smartAntennaSetting", UNSET)
        smart_antenna_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_smart_antenna_setting, Unset):
            smart_antenna_setting = UNSET
        else:
            smart_antenna_setting = ApConfigResultBaseSettingVO.from_dict(
                _smart_antenna_setting
            )

        _power_saving_setting = d.pop("powerSavingSetting", UNSET)
        power_saving_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_power_saving_setting, Unset):
            power_saving_setting = UNSET
        else:
            power_saving_setting = ApConfigResultBaseSettingVO.from_dict(
                _power_saving_setting
            )

        _antenna_gain_setting = d.pop("antennaGainSetting", UNSET)
        antenna_gain_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_antenna_gain_setting, Unset):
            antenna_gain_setting = UNSET
        else:
            antenna_gain_setting = ApConfigResultBaseSettingVO.from_dict(
                _antenna_gain_setting
            )

        _ant_setting = d.pop("antSetting", UNSET)
        ant_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ant_setting, Unset):
            ant_setting = UNSET
        else:
            ant_setting = ApConfigResultBaseSettingVO.from_dict(_ant_setting)

        _ant_setting_2_g = d.pop("antSetting2g", UNSET)
        ant_setting_2_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ant_setting_2_g, Unset):
            ant_setting_2_g = UNSET
        else:
            ant_setting_2_g = ApConfigResultBaseSettingVO.from_dict(_ant_setting_2_g)

        _ant_setting_5_g = d.pop("antSetting5g", UNSET)
        ant_setting_5_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ant_setting_5_g, Unset):
            ant_setting_5_g = UNSET
        else:
            ant_setting_5_g = ApConfigResultBaseSettingVO.from_dict(_ant_setting_5_g)

        _ant_setting_5_g_2 = d.pop("antSetting5g2", UNSET)
        ant_setting_5_g_2: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ant_setting_5_g_2, Unset):
            ant_setting_5_g_2 = UNSET
        else:
            ant_setting_5_g_2 = ApConfigResultBaseSettingVO.from_dict(
                _ant_setting_5_g_2
            )

        _ant_setting_6_g = d.pop("antSetting6g", UNSET)
        ant_setting_6_g: ApConfigResultBaseSettingVO | Unset
        if isinstance(_ant_setting_6_g, Unset):
            ant_setting_6_g = UNSET
        else:
            ant_setting_6_g = ApConfigResultBaseSettingVO.from_dict(_ant_setting_6_g)

        _wlan_group_setting = d.pop("wlanGroupSetting", UNSET)
        wlan_group_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_wlan_group_setting, Unset):
            wlan_group_setting = UNSET
        else:
            wlan_group_setting = ApConfigResultBaseSettingVO.from_dict(
                _wlan_group_setting
            )

        _channel_limit_setting = d.pop("channelLimitSetting", UNSET)
        channel_limit_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_channel_limit_setting, Unset):
            channel_limit_setting = UNSET
        else:
            channel_limit_setting = ApConfigResultBaseSettingVO.from_dict(
                _channel_limit_setting
            )

        _afc_setting = d.pop("afcSetting", UNSET)
        afc_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_afc_setting, Unset):
            afc_setting = UNSET
        else:
            afc_setting = ApConfigResultBaseSettingVO.from_dict(_afc_setting)

        _radio_setting_2_g = d.pop("radioSetting2g", UNSET)
        radio_setting_2_g: ApConfigResultRadioSettingVO | Unset
        if isinstance(_radio_setting_2_g, Unset):
            radio_setting_2_g = UNSET
        else:
            radio_setting_2_g = ApConfigResultRadioSettingVO.from_dict(
                _radio_setting_2_g
            )

        _radio_setting_5_g = d.pop("radioSetting5g", UNSET)
        radio_setting_5_g: ApConfigResultRadioSettingVO | Unset
        if isinstance(_radio_setting_5_g, Unset):
            radio_setting_5_g = UNSET
        else:
            radio_setting_5_g = ApConfigResultRadioSettingVO.from_dict(
                _radio_setting_5_g
            )

        _radio_setting_5_g_1 = d.pop("radioSetting5g1", UNSET)
        radio_setting_5_g_1: ApConfigResultRadioSettingVO | Unset
        if isinstance(_radio_setting_5_g_1, Unset):
            radio_setting_5_g_1 = UNSET
        else:
            radio_setting_5_g_1 = ApConfigResultRadioSettingVO.from_dict(
                _radio_setting_5_g_1
            )

        _radio_setting_5_g_2 = d.pop("radioSetting5g2", UNSET)
        radio_setting_5_g_2: ApConfigResultRadioSettingVO | Unset
        if isinstance(_radio_setting_5_g_2, Unset):
            radio_setting_5_g_2 = UNSET
        else:
            radio_setting_5_g_2 = ApConfigResultRadioSettingVO.from_dict(
                _radio_setting_5_g_2
            )

        _radio_setting_6_g = d.pop("radioSetting6g", UNSET)
        radio_setting_6_g: ApConfigResultRadioSettingVO | Unset
        if isinstance(_radio_setting_6_g, Unset):
            radio_setting_6_g = UNSET
        else:
            radio_setting_6_g = ApConfigResultRadioSettingVO.from_dict(
                _radio_setting_6_g
            )

        _port_setting_list = d.pop("portSettingList", UNSET)
        port_setting_list: list[ApConfigResultPortSettingVO] | Unset = UNSET
        if _port_setting_list is not UNSET:
            port_setting_list = []
            for port_setting_list_item_data in _port_setting_list:
                port_setting_list_item = ApConfigResultPortSettingVO.from_dict(
                    port_setting_list_item_data
                )

                port_setting_list.append(port_setting_list_item)

        ap_config_result_settings_vo = cls(
            led_setting=led_setting,
            rssi_led_setting=rssi_led_setting,
            wifi_control_setting=wifi_control_setting,
            gps_setting=gps_setting,
            remote_reset_setting=remote_reset_setting,
            disable_hw_reset_setting=disable_hw_reset_setting,
            enable_slide_switch_setting=enable_slide_switch_setting,
            lb_setting_2_g=lb_setting_2_g,
            lb_setting_5_g=lb_setting_5_g,
            lb_setting_5_g_1=lb_setting_5_g_1,
            lb_setting_5_g_2=lb_setting_5_g_2,
            lb_setting_6_g=lb_setting_6_g,
            rssi_setting_2_g=rssi_setting_2_g,
            rssi_setting_5_g=rssi_setting_5_g,
            rssi_setting_5_g_1=rssi_setting_5_g_1,
            rssi_setting_5_g_2=rssi_setting_5_g_2,
            rssi_setting_6_g=rssi_setting_6_g,
            qos_setting_2_g=qos_setting_2_g,
            qos_setting_5_g=qos_setting_5_g,
            qos_setting_5_g_1=qos_setting_5_g_1,
            qos_setting_5_g_2=qos_setting_5_g_2,
            qos_setting_6_g=qos_setting_6_g,
            non_psc_setting=non_psc_setting,
            ofdma_enable_2_g=ofdma_enable_2_g,
            ofdma_enable_5_g=ofdma_enable_5_g,
            ofdma_enable_5_g_1=ofdma_enable_5_g_1,
            ofdma_enable_5_g_2=ofdma_enable_5_g_2,
            ofdma_enable_6_g=ofdma_enable_6_g,
            trunk_setting=trunk_setting,
            mvlan_setting=mvlan_setting,
            snmp_setting=snmp_setting,
            l_3_access_setting=l_3_access_setting,
            lldp_setting=lldp_setting,
            loopback_detect_setting=loopback_detect_setting,
            voip_vlan_setting=voip_vlan_setting,
            smart_antenna_setting=smart_antenna_setting,
            power_saving_setting=power_saving_setting,
            antenna_gain_setting=antenna_gain_setting,
            ant_setting=ant_setting,
            ant_setting_2_g=ant_setting_2_g,
            ant_setting_5_g=ant_setting_5_g,
            ant_setting_5_g_2=ant_setting_5_g_2,
            ant_setting_6_g=ant_setting_6_g,
            wlan_group_setting=wlan_group_setting,
            channel_limit_setting=channel_limit_setting,
            afc_setting=afc_setting,
            radio_setting_2_g=radio_setting_2_g,
            radio_setting_5_g=radio_setting_5_g,
            radio_setting_5_g_1=radio_setting_5_g_1,
            radio_setting_5_g_2=radio_setting_5_g_2,
            radio_setting_6_g=radio_setting_6_g,
            port_setting_list=port_setting_list,
        )

        ap_config_result_settings_vo.additional_properties = d
        return ap_config_result_settings_vo

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
