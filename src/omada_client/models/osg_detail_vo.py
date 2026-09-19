from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_load_balance_vo import ApLoadBalanceVO
    from ..models.ap_qos_vo import ApQosVO
    from ..models.ap_radio_channel import ApRadioChannel
    from ..models.ap_radio_setting import ApRadioSetting
    from ..models.ap_radio_traffic_entity import APRadioTrafficEntity
    from ..models.ap_rssi_threshold_vo import ApRssiThresholdVO
    from ..models.device_location_detail_vo import DeviceLocationDetailVO
    from ..models.device_replace_setting_vo import DeviceReplaceSettingVO
    from ..models.exist_site_setting_vo import ExistSiteSettingVO
    from ..models.osg_cap_vo import OsgCapVO
    from ..models.osg_down_link_vo import OsgDownLinkVO
    from ..models.osg_fan_status_vo import OsgFanStatusVO
    from ..models.osg_iptv_vo import OsgIptvVO
    from ..models.osg_lan_stat_vo import OsgLanStatVO
    from ..models.osg_lte_pin_setting_vo import OsgLtePinSettingVO
    from ..models.osg_port_config_vo import OsgPortConfigVO
    from ..models.osg_port_general_config_vo import OsgPortGeneralConfigVO
    from ..models.osg_port_poe_vo import OsgPortPoeVO
    from ..models.osg_port_stat_vo import OsgPortStatVO
    from ..models.osg_rps_status_vo import OsgRpsStatusVO
    from ..models.osg_snmp_vo import OsgSnmpVO
    from ..models.osg_virtual_wan_stat_vo import OsgVirtualWanStatVO
    from ..models.site_setting_cap_vo import SiteSettingCapVO
    from ..models.ssh_setting_vo import SshSettingVO
    from ..models.ssid_override_vo import SsidOverrideVO
    from ..models.wireless_router_misc_vo import WirelessRouterMiscVO


T = TypeVar("T", bound="OsgDetailVO")


@_attrs_define
class OsgDetailVO:
    """Gateway detail.

    Attributes:
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        mac (str | Unset): Device mac
        name (str | Unset): Device name,default value is the mac address of device
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        compound_model (str | Unset): Model complex used in the backend.Ap：model+(country)+modelVersion,  EAP225(EU)
            v3.0 Ap: specialModel+modelVersion, EAP225-Outdoor-1a20a950b8d950e8 v1.0  Gateway/Switch：model+modelVersion, Osg
            v3.0
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        special_model (str | Unset): Special device model,for example:EAP225-Outdoor-1a20a950b8d950e8
        firmware_version (str | Unset): Version of firmware,for example:2.5.0 Build 20190118 Rel. 64821
        version (str | Unset): Simplified version of firmware,for example:2.5.0
        hw_version (str | Unset): Version of hardware,for example 1.0
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        es (bool | Unset): Whether the device is Agile Series Switch
        site (str | Unset): Site of the device
        site_name (str | Unset): Site name of the device
        omadac_id (str | Unset): OmadacId of the device
        compatible (int | Unset): Device firmware and controller compatibility type.Compatible should be a value as
            follows: 0:COMPATIBLE;1:HIGH_MAJOR_VER;2:LOW_MAJOR_VER;3:HIGH_MINOR_VER;4:LOW_MINOR_VER;7:HIGH_COMPONENT_VER;10:
            DEVICE_NOT_COMPATIBLE;11:HIGH_ADOPT_COMMPONENT;12:DEVICE_CATEGORY_NOT_COMPATIBLE;14:DEVICE_NOT_COMPATIBLE_IN_CLU
            STER
        support_anomaly (bool | Unset): Whether the device firmware support intelligent anomaly detection
        support_locate_port (bool | Unset): Whether the device supports locating port
        active (bool | Unset): whether to active the device(cloud base exclusive)
        license_status (int | Unset): License status(cloud base exclusive).LicenseStatus should be a value as follows:
            0:unActive 1:Unbind 2:Expired 3:active
        due_time (int | Unset): Expire timestamp of license(cloud base exclusive)
        due_time_left (int | Unset): Milliseconds from the current moment to the expiration time(cloud base exclusive)
        license_id (str | Unset): License key on detail page of device(cloud base exclusive)
        license_unbinding_limit (int | Unset): Remaining unbind count for license on detail Page of device(cloud base
            exclusive)
        initial_unbinding_limit (int | Unset): Initial unbind count for license(cloud base exclusive)
        category (str | Unset): Category of license
        forget_id (str | Unset): Forget ID of device
        sn (str | Unset): SN code of device
        eost (int | Unset): End of service time of device(CBC exclusive)
        eos (int | Unset): End of support time of device(CBC exclusive)
        in_whitelist (bool | Unset): Whether the device is in white list
        location (DeviceLocationDetailVO | Unset): Device location
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
        custom_id (str | Unset): Customer ID
        custom_name (str | Unset): Customer name
        move_site_id (str | Unset): Record that the device is in a moveSite operation; if it is null, then it is not in
            the moveSite operation.
        remember (bool | Unset): Whether to remember the device(deprecated)
        remember_device (int | Unset): Whether to remember the device.RememberDevice should be a value as follows:
            0:off, 1:on, 2: follow site
        description (str | Unset): Description of the device
        disable_hw_reset (bool | Unset): Whether to disable hardware reset
        template_id (str | Unset): ID of the template bound to the device
        template_name (str | Unset): Name of the template bound to the device
        bound_site_template (bool | Unset): Whether the site where the device is located is bound to a site template
        device_template_available (bool | Unset): Whether there is an available device template for the device; it is
            false if the model is not supported or the site template has not created the corresponding device template.
        bound_device_template (bool | Unset): Whether the device is bound to device template
        site_template_name (str | Unset): Template name bound to the site
        site_template_id (str | Unset): Template ID bound to the site
        device_series_type (int | Unset): Device series type.DeviceSeriesType should be a value as follows:
            0:advanced;1:pro
        resource (int | Unset): Data source.Resource should be a value as follows: 0:new created;1:from
            template;2:override
        ecsp_first_version (int | Unset): Ecsp first version
        latest_version (str | Unset): Latest firmware version
        replace_device_info (DeviceReplaceSettingVO | Unset):
        dev_cap (OsgCapVO | Unset):
        port_num (int | Unset):
        led_setting (int | Unset):
        snmp_seting (OsgSnmpVO | Unset):
        iptv_setting (OsgIptvVO | Unset):
        support_hw_offload (bool | Unset):
        support_poe (bool | Unset):
        hw_offload_enable (bool | Unset):
        poe_settings (list[OsgPortPoeVO] | Unset):
        lldp_enable (bool | Unset):
        lldp_setting (int | Unset):
        echo_server (str | Unset):
        ip (str | Unset):
        public_ip (str | Unset):
        ipv_6_list (list[str] | Unset):
        uptime (str | Unset):
        uptime_long (int | Unset):
        cpu_util (int | Unset):
        mem_util (int | Unset):
        last_seen (int | Unset):
        port_stats (list[OsgPortStatVO] | Unset):
        virtual_wan_stats (list[OsgVirtualWanStatVO] | Unset):
        support_lan_client_stats (bool | Unset):
        support_port_forwarding_status (bool | Unset):
        support_session_limit_status (bool | Unset):
        support_channel_utilization_status (bool | Unset):
        support_dropped_packets_status (bool | Unset):
        support_retried_packets_status (bool | Unset):
        support_band_scan (bool | Unset):
        support_network_search (bool | Unset):
        lan_client_stats (list[OsgLanStatVO] | Unset):
        controller_id (str | Unset):
        need_upgrade (bool | Unset):
        support_dsl (bool | Unset):
        support_virtual_wan (bool | Unset):
        support_dual_sim (int | Unset):
        support_batch_edit (bool | Unset):
        download (int | Unset):
        upload (int | Unset):
        tx_rate (int | Unset):
        rx_rate (int | Unset):
        network_comptent (int | Unset):
        temp (int | Unset):
        fan (list[OsgFanStatusVO] | Unset):
        rps (list[OsgRpsStatusVO] | Unset):
        port_configs (list[OsgPortConfigVO] | Unset):
        port_general_configs (list[OsgPortGeneralConfigVO] | Unset):
        support_speed_duplex (bool | Unset):
        support_mirror (bool | Unset):
        support_pvid (bool | Unset):
        support_wan_set_pvid (bool | Unset):
        support_snmp (bool | Unset):
        unsupported_ports (list[int] | Unset):
        combined_gateway (bool | Unset):
        speeds (list[int] | Unset):
        support_lte (bool | Unset):
        pin_setting (OsgLtePinSettingVO | Unset):
        ippt (bool | Unset):
        ippt_preconfig (bool | Unset):
        support_ippt (bool | Unset):
        contain_net_type_5g (bool | Unset):
        ssh_setting (SshSettingVO | Unset):
        multi_chip_gateway (bool | Unset):
        multi_chip_infos (list[list[int]] | Unset):
        support_flow_control (bool | Unset):
        support_port_control (bool | Unset):
        support_loopback_control (bool | Unset):
        support_port_isolation (bool | Unset):
        support_band_width_ctrl (bool | Unset):
        support_storm_ctrl_action (bool | Unset):
        support_jumbo (bool | Unset):
        jumbo_size (int | Unset):
        jumbo_options (list[int] | Unset):
        downlink_list (list[OsgDownLinkVO] | Unset):
        wireless_router (bool | Unset):
        wireless_health (bool | Unset):
        device_misc (WirelessRouterMiscVO | Unset):
        wp2g (ApRadioChannel | Unset):
        wp5g (ApRadioChannel | Unset):
        wp5g2 (ApRadioChannel | Unset):
        wp6g (ApRadioChannel | Unset):
        radio_setting_2_g (ApRadioSetting | Unset): Radio Setting
        radio_setting_5_g (ApRadioSetting | Unset): Radio Setting
        radio_setting_5_g_2 (ApRadioSetting | Unset): Radio Setting
        radio_setting_6_g (ApRadioSetting | Unset): Radio Setting
        radio_traffic_2_g (APRadioTrafficEntity | Unset):
        radio_traffic_5_g (APRadioTrafficEntity | Unset):
        radio_traffic_5_g_2 (APRadioTrafficEntity | Unset):
        radio_traffic_6_g (APRadioTrafficEntity | Unset):
        lb_setting_2_g (ApLoadBalanceVO | Unset):
        lb_setting_5_g (ApLoadBalanceVO | Unset):
        lb_setting_5_g_2 (ApLoadBalanceVO | Unset):
        lb_setting_6_g (ApLoadBalanceVO | Unset):
        rssi_setting_2_g (ApRssiThresholdVO | Unset):
        rssi_setting_5_g (ApRssiThresholdVO | Unset):
        rssi_setting_5_g_2 (ApRssiThresholdVO | Unset):
        rssi_setting_6_g (ApRssiThresholdVO | Unset):
        qos_setting_2_g (ApQosVO | Unset):
        qos_setting_5_g (ApQosVO | Unset):
        qos_setting_5_g_2 (ApQosVO | Unset):
        qos_setting_6_g (ApQosVO | Unset):
        ofdma_enable_2_g (bool | Unset):
        ofdma_enable_5_g (bool | Unset):
        ofdma_enable_5_g_2 (bool | Unset):
        ofdma_enable_6_g (bool | Unset):
        wlan_id (str | Unset):
        ssid_overrides (list[SsidOverrideVO] | Unset):
        non_psc_enable (bool | Unset):
        channel_limit_type (int | Unset):
        support_rf_scan (bool | Unset):
        user_num (int | Unset):
        guest_num (int | Unset):
        tag_ids (list[str] | Unset):
        add_by_template (bool | Unset):
        services_resource (int | Unset):
        advanced_resource (int | Unset):
        common_advanced_resource (int | Unset):
        wireless_advanced_resource (int | Unset):
        radios_resource (int | Unset):
        wlans_resource (int | Unset):
        template_settings (list[int] | Unset):
        support_ip_mac_binding (bool | Unset):
        support_new_ip_mac_binding (bool | Unset):
        poe_limit (float | Unset):
        poe_remain (float | Unset):
        poe_remain_percent (float | Unset):
        osg_cap (SiteSettingCapVO | Unset):
        osg_exist (ExistSiteSettingVO | Unset):
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    compound_model: str | Unset = UNSET
    show_model: str | Unset = UNSET
    special_model: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    version: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    es: bool | Unset = UNSET
    site: str | Unset = UNSET
    site_name: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    compatible: int | Unset = UNSET
    support_anomaly: bool | Unset = UNSET
    support_locate_port: bool | Unset = UNSET
    active: bool | Unset = UNSET
    license_status: int | Unset = UNSET
    due_time: int | Unset = UNSET
    due_time_left: int | Unset = UNSET
    license_id: str | Unset = UNSET
    license_unbinding_limit: int | Unset = UNSET
    initial_unbinding_limit: int | Unset = UNSET
    category: str | Unset = UNSET
    forget_id: str | Unset = UNSET
    sn: str | Unset = UNSET
    eost: int | Unset = UNSET
    eos: int | Unset = UNSET
    in_whitelist: bool | Unset = UNSET
    location: DeviceLocationDetailVO | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    custom_id: str | Unset = UNSET
    custom_name: str | Unset = UNSET
    move_site_id: str | Unset = UNSET
    remember: bool | Unset = UNSET
    remember_device: int | Unset = UNSET
    description: str | Unset = UNSET
    disable_hw_reset: bool | Unset = UNSET
    template_id: str | Unset = UNSET
    template_name: str | Unset = UNSET
    bound_site_template: bool | Unset = UNSET
    device_template_available: bool | Unset = UNSET
    bound_device_template: bool | Unset = UNSET
    site_template_name: str | Unset = UNSET
    site_template_id: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    resource: int | Unset = UNSET
    ecsp_first_version: int | Unset = UNSET
    latest_version: str | Unset = UNSET
    replace_device_info: DeviceReplaceSettingVO | Unset = UNSET
    dev_cap: OsgCapVO | Unset = UNSET
    port_num: int | Unset = UNSET
    led_setting: int | Unset = UNSET
    snmp_seting: OsgSnmpVO | Unset = UNSET
    iptv_setting: OsgIptvVO | Unset = UNSET
    support_hw_offload: bool | Unset = UNSET
    support_poe: bool | Unset = UNSET
    hw_offload_enable: bool | Unset = UNSET
    poe_settings: list[OsgPortPoeVO] | Unset = UNSET
    lldp_enable: bool | Unset = UNSET
    lldp_setting: int | Unset = UNSET
    echo_server: str | Unset = UNSET
    ip: str | Unset = UNSET
    public_ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    uptime: str | Unset = UNSET
    uptime_long: int | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_util: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    port_stats: list[OsgPortStatVO] | Unset = UNSET
    virtual_wan_stats: list[OsgVirtualWanStatVO] | Unset = UNSET
    support_lan_client_stats: bool | Unset = UNSET
    support_port_forwarding_status: bool | Unset = UNSET
    support_session_limit_status: bool | Unset = UNSET
    support_channel_utilization_status: bool | Unset = UNSET
    support_dropped_packets_status: bool | Unset = UNSET
    support_retried_packets_status: bool | Unset = UNSET
    support_band_scan: bool | Unset = UNSET
    support_network_search: bool | Unset = UNSET
    lan_client_stats: list[OsgLanStatVO] | Unset = UNSET
    controller_id: str | Unset = UNSET
    need_upgrade: bool | Unset = UNSET
    support_dsl: bool | Unset = UNSET
    support_virtual_wan: bool | Unset = UNSET
    support_dual_sim: int | Unset = UNSET
    support_batch_edit: bool | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    network_comptent: int | Unset = UNSET
    temp: int | Unset = UNSET
    fan: list[OsgFanStatusVO] | Unset = UNSET
    rps: list[OsgRpsStatusVO] | Unset = UNSET
    port_configs: list[OsgPortConfigVO] | Unset = UNSET
    port_general_configs: list[OsgPortGeneralConfigVO] | Unset = UNSET
    support_speed_duplex: bool | Unset = UNSET
    support_mirror: bool | Unset = UNSET
    support_pvid: bool | Unset = UNSET
    support_wan_set_pvid: bool | Unset = UNSET
    support_snmp: bool | Unset = UNSET
    unsupported_ports: list[int] | Unset = UNSET
    combined_gateway: bool | Unset = UNSET
    speeds: list[int] | Unset = UNSET
    support_lte: bool | Unset = UNSET
    pin_setting: OsgLtePinSettingVO | Unset = UNSET
    ippt: bool | Unset = UNSET
    ippt_preconfig: bool | Unset = UNSET
    support_ippt: bool | Unset = UNSET
    contain_net_type_5g: bool | Unset = UNSET
    ssh_setting: SshSettingVO | Unset = UNSET
    multi_chip_gateway: bool | Unset = UNSET
    multi_chip_infos: list[list[int]] | Unset = UNSET
    support_flow_control: bool | Unset = UNSET
    support_port_control: bool | Unset = UNSET
    support_loopback_control: bool | Unset = UNSET
    support_port_isolation: bool | Unset = UNSET
    support_band_width_ctrl: bool | Unset = UNSET
    support_storm_ctrl_action: bool | Unset = UNSET
    support_jumbo: bool | Unset = UNSET
    jumbo_size: int | Unset = UNSET
    jumbo_options: list[int] | Unset = UNSET
    downlink_list: list[OsgDownLinkVO] | Unset = UNSET
    wireless_router: bool | Unset = UNSET
    wireless_health: bool | Unset = UNSET
    device_misc: WirelessRouterMiscVO | Unset = UNSET
    wp2g: ApRadioChannel | Unset = UNSET
    wp5g: ApRadioChannel | Unset = UNSET
    wp5g2: ApRadioChannel | Unset = UNSET
    wp6g: ApRadioChannel | Unset = UNSET
    radio_setting_2_g: ApRadioSetting | Unset = UNSET
    radio_setting_5_g: ApRadioSetting | Unset = UNSET
    radio_setting_5_g_2: ApRadioSetting | Unset = UNSET
    radio_setting_6_g: ApRadioSetting | Unset = UNSET
    radio_traffic_2_g: APRadioTrafficEntity | Unset = UNSET
    radio_traffic_5_g: APRadioTrafficEntity | Unset = UNSET
    radio_traffic_5_g_2: APRadioTrafficEntity | Unset = UNSET
    radio_traffic_6_g: APRadioTrafficEntity | Unset = UNSET
    lb_setting_2_g: ApLoadBalanceVO | Unset = UNSET
    lb_setting_5_g: ApLoadBalanceVO | Unset = UNSET
    lb_setting_5_g_2: ApLoadBalanceVO | Unset = UNSET
    lb_setting_6_g: ApLoadBalanceVO | Unset = UNSET
    rssi_setting_2_g: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_5_g: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_5_g_2: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_6_g: ApRssiThresholdVO | Unset = UNSET
    qos_setting_2_g: ApQosVO | Unset = UNSET
    qos_setting_5_g: ApQosVO | Unset = UNSET
    qos_setting_5_g_2: ApQosVO | Unset = UNSET
    qos_setting_6_g: ApQosVO | Unset = UNSET
    ofdma_enable_2_g: bool | Unset = UNSET
    ofdma_enable_5_g: bool | Unset = UNSET
    ofdma_enable_5_g_2: bool | Unset = UNSET
    ofdma_enable_6_g: bool | Unset = UNSET
    wlan_id: str | Unset = UNSET
    ssid_overrides: list[SsidOverrideVO] | Unset = UNSET
    non_psc_enable: bool | Unset = UNSET
    channel_limit_type: int | Unset = UNSET
    support_rf_scan: bool | Unset = UNSET
    user_num: int | Unset = UNSET
    guest_num: int | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    add_by_template: bool | Unset = UNSET
    services_resource: int | Unset = UNSET
    advanced_resource: int | Unset = UNSET
    common_advanced_resource: int | Unset = UNSET
    wireless_advanced_resource: int | Unset = UNSET
    radios_resource: int | Unset = UNSET
    wlans_resource: int | Unset = UNSET
    template_settings: list[int] | Unset = UNSET
    support_ip_mac_binding: bool | Unset = UNSET
    support_new_ip_mac_binding: bool | Unset = UNSET
    poe_limit: float | Unset = UNSET
    poe_remain: float | Unset = UNSET
    poe_remain_percent: float | Unset = UNSET
    osg_cap: SiteSettingCapVO | Unset = UNSET
    osg_exist: ExistSiteSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        compound_model = self.compound_model

        show_model = self.show_model

        special_model = self.special_model

        firmware_version = self.firmware_version

        version = self.version

        hw_version = self.hw_version

        status = self.status

        status_category = self.status_category

        es = self.es

        site = self.site

        site_name = self.site_name

        omadac_id = self.omadac_id

        compatible = self.compatible

        support_anomaly = self.support_anomaly

        support_locate_port = self.support_locate_port

        active = self.active

        license_status = self.license_status

        due_time = self.due_time

        due_time_left = self.due_time_left

        license_id = self.license_id

        license_unbinding_limit = self.license_unbinding_limit

        initial_unbinding_limit = self.initial_unbinding_limit

        category = self.category

        forget_id = self.forget_id

        sn = self.sn

        eost = self.eost

        eos = self.eos

        in_whitelist = self.in_whitelist

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        added_in_advanced = self.added_in_advanced

        custom_id = self.custom_id

        custom_name = self.custom_name

        move_site_id = self.move_site_id

        remember = self.remember

        remember_device = self.remember_device

        description = self.description

        disable_hw_reset = self.disable_hw_reset

        template_id = self.template_id

        template_name = self.template_name

        bound_site_template = self.bound_site_template

        device_template_available = self.device_template_available

        bound_device_template = self.bound_device_template

        site_template_name = self.site_template_name

        site_template_id = self.site_template_id

        device_series_type = self.device_series_type

        resource = self.resource

        ecsp_first_version = self.ecsp_first_version

        latest_version = self.latest_version

        replace_device_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replace_device_info, Unset):
            replace_device_info = self.replace_device_info.to_dict()

        dev_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_cap, Unset):
            dev_cap = self.dev_cap.to_dict()

        port_num = self.port_num

        led_setting = self.led_setting

        snmp_seting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp_seting, Unset):
            snmp_seting = self.snmp_seting.to_dict()

        iptv_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.iptv_setting, Unset):
            iptv_setting = self.iptv_setting.to_dict()

        support_hw_offload = self.support_hw_offload

        support_poe = self.support_poe

        hw_offload_enable = self.hw_offload_enable

        poe_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.poe_settings, Unset):
            poe_settings = []
            for poe_settings_item_data in self.poe_settings:
                poe_settings_item = poe_settings_item_data.to_dict()
                poe_settings.append(poe_settings_item)

        lldp_enable = self.lldp_enable

        lldp_setting = self.lldp_setting

        echo_server = self.echo_server

        ip = self.ip

        public_ip = self.public_ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        uptime = self.uptime

        uptime_long = self.uptime_long

        cpu_util = self.cpu_util

        mem_util = self.mem_util

        last_seen = self.last_seen

        port_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_stats, Unset):
            port_stats = []
            for port_stats_item_data in self.port_stats:
                port_stats_item = port_stats_item_data.to_dict()
                port_stats.append(port_stats_item)

        virtual_wan_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.virtual_wan_stats, Unset):
            virtual_wan_stats = []
            for virtual_wan_stats_item_data in self.virtual_wan_stats:
                virtual_wan_stats_item = virtual_wan_stats_item_data.to_dict()
                virtual_wan_stats.append(virtual_wan_stats_item)

        support_lan_client_stats = self.support_lan_client_stats

        support_port_forwarding_status = self.support_port_forwarding_status

        support_session_limit_status = self.support_session_limit_status

        support_channel_utilization_status = self.support_channel_utilization_status

        support_dropped_packets_status = self.support_dropped_packets_status

        support_retried_packets_status = self.support_retried_packets_status

        support_band_scan = self.support_band_scan

        support_network_search = self.support_network_search

        lan_client_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_client_stats, Unset):
            lan_client_stats = []
            for lan_client_stats_item_data in self.lan_client_stats:
                lan_client_stats_item = lan_client_stats_item_data.to_dict()
                lan_client_stats.append(lan_client_stats_item)

        controller_id = self.controller_id

        need_upgrade = self.need_upgrade

        support_dsl = self.support_dsl

        support_virtual_wan = self.support_virtual_wan

        support_dual_sim = self.support_dual_sim

        support_batch_edit = self.support_batch_edit

        download = self.download

        upload = self.upload

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        network_comptent = self.network_comptent

        temp = self.temp

        fan: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fan, Unset):
            fan = []
            for fan_item_data in self.fan:
                fan_item = fan_item_data.to_dict()
                fan.append(fan_item)

        rps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rps, Unset):
            rps = []
            for rps_item_data in self.rps:
                rps_item = rps_item_data.to_dict()
                rps.append(rps_item)

        port_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_configs, Unset):
            port_configs = []
            for port_configs_item_data in self.port_configs:
                port_configs_item = port_configs_item_data.to_dict()
                port_configs.append(port_configs_item)

        port_general_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_general_configs, Unset):
            port_general_configs = []
            for port_general_configs_item_data in self.port_general_configs:
                port_general_configs_item = port_general_configs_item_data.to_dict()
                port_general_configs.append(port_general_configs_item)

        support_speed_duplex = self.support_speed_duplex

        support_mirror = self.support_mirror

        support_pvid = self.support_pvid

        support_wan_set_pvid = self.support_wan_set_pvid

        support_snmp = self.support_snmp

        unsupported_ports: list[int] | Unset = UNSET
        if not isinstance(self.unsupported_ports, Unset):
            unsupported_ports = self.unsupported_ports

        combined_gateway = self.combined_gateway

        speeds: list[int] | Unset = UNSET
        if not isinstance(self.speeds, Unset):
            speeds = self.speeds

        support_lte = self.support_lte

        pin_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pin_setting, Unset):
            pin_setting = self.pin_setting.to_dict()

        ippt = self.ippt

        ippt_preconfig = self.ippt_preconfig

        support_ippt = self.support_ippt

        contain_net_type_5g = self.contain_net_type_5g

        ssh_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh_setting, Unset):
            ssh_setting = self.ssh_setting.to_dict()

        multi_chip_gateway = self.multi_chip_gateway

        multi_chip_infos: list[list[int]] | Unset = UNSET
        if not isinstance(self.multi_chip_infos, Unset):
            multi_chip_infos = []
            for multi_chip_infos_item_data in self.multi_chip_infos:
                multi_chip_infos_item = multi_chip_infos_item_data

                multi_chip_infos.append(multi_chip_infos_item)

        support_flow_control = self.support_flow_control

        support_port_control = self.support_port_control

        support_loopback_control = self.support_loopback_control

        support_port_isolation = self.support_port_isolation

        support_band_width_ctrl = self.support_band_width_ctrl

        support_storm_ctrl_action = self.support_storm_ctrl_action

        support_jumbo = self.support_jumbo

        jumbo_size = self.jumbo_size

        jumbo_options: list[int] | Unset = UNSET
        if not isinstance(self.jumbo_options, Unset):
            jumbo_options = self.jumbo_options

        downlink_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_list, Unset):
            downlink_list = []
            for downlink_list_item_data in self.downlink_list:
                downlink_list_item = downlink_list_item_data.to_dict()
                downlink_list.append(downlink_list_item)

        wireless_router = self.wireless_router

        wireless_health = self.wireless_health

        device_misc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_misc, Unset):
            device_misc = self.device_misc.to_dict()

        wp2g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp2g, Unset):
            wp2g = self.wp2g.to_dict()

        wp5g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp5g, Unset):
            wp5g = self.wp5g.to_dict()

        wp5g2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp5g2, Unset):
            wp5g2 = self.wp5g2.to_dict()

        wp6g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp6g, Unset):
            wp6g = self.wp6g.to_dict()

        radio_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_2_g, Unset):
            radio_setting_2_g = self.radio_setting_2_g.to_dict()

        radio_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g, Unset):
            radio_setting_5_g = self.radio_setting_5_g.to_dict()

        radio_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g_2, Unset):
            radio_setting_5_g_2 = self.radio_setting_5_g_2.to_dict()

        radio_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_6_g, Unset):
            radio_setting_6_g = self.radio_setting_6_g.to_dict()

        radio_traffic_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_2_g, Unset):
            radio_traffic_2_g = self.radio_traffic_2_g.to_dict()

        radio_traffic_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_5_g, Unset):
            radio_traffic_5_g = self.radio_traffic_5_g.to_dict()

        radio_traffic_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_5_g_2, Unset):
            radio_traffic_5_g_2 = self.radio_traffic_5_g_2.to_dict()

        radio_traffic_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_6_g, Unset):
            radio_traffic_6_g = self.radio_traffic_6_g.to_dict()

        lb_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_2_g, Unset):
            lb_setting_2_g = self.lb_setting_2_g.to_dict()

        lb_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g, Unset):
            lb_setting_5_g = self.lb_setting_5_g.to_dict()

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

        qos_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = self.qos_setting_5_g_2.to_dict()

        qos_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_6_g, Unset):
            qos_setting_6_g = self.qos_setting_6_g.to_dict()

        ofdma_enable_2_g = self.ofdma_enable_2_g

        ofdma_enable_5_g = self.ofdma_enable_5_g

        ofdma_enable_5_g_2 = self.ofdma_enable_5_g_2

        ofdma_enable_6_g = self.ofdma_enable_6_g

        wlan_id = self.wlan_id

        ssid_overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssid_overrides, Unset):
            ssid_overrides = []
            for ssid_overrides_item_data in self.ssid_overrides:
                ssid_overrides_item = ssid_overrides_item_data.to_dict()
                ssid_overrides.append(ssid_overrides_item)

        non_psc_enable = self.non_psc_enable

        channel_limit_type = self.channel_limit_type

        support_rf_scan = self.support_rf_scan

        user_num = self.user_num

        guest_num = self.guest_num

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        add_by_template = self.add_by_template

        services_resource = self.services_resource

        advanced_resource = self.advanced_resource

        common_advanced_resource = self.common_advanced_resource

        wireless_advanced_resource = self.wireless_advanced_resource

        radios_resource = self.radios_resource

        wlans_resource = self.wlans_resource

        template_settings: list[int] | Unset = UNSET
        if not isinstance(self.template_settings, Unset):
            template_settings = self.template_settings

        support_ip_mac_binding = self.support_ip_mac_binding

        support_new_ip_mac_binding = self.support_new_ip_mac_binding

        poe_limit = self.poe_limit

        poe_remain = self.poe_remain

        poe_remain_percent = self.poe_remain_percent

        osg_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osg_cap, Unset):
            osg_cap = self.osg_cap.to_dict()

        osg_exist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osg_exist, Unset):
            osg_exist = self.osg_exist.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if compound_model is not UNSET:
            field_dict["compoundModel"] = compound_model
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if version is not UNSET:
            field_dict["version"] = version
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if es is not UNSET:
            field_dict["es"] = es
        if site is not UNSET:
            field_dict["site"] = site
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if support_anomaly is not UNSET:
            field_dict["supportAnomaly"] = support_anomaly
        if support_locate_port is not UNSET:
            field_dict["supportLocatePort"] = support_locate_port
        if active is not UNSET:
            field_dict["active"] = active
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if due_time is not UNSET:
            field_dict["dueTime"] = due_time
        if due_time_left is not UNSET:
            field_dict["dueTimeLeft"] = due_time_left
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if license_unbinding_limit is not UNSET:
            field_dict["licenseUnbindingLimit"] = license_unbinding_limit
        if initial_unbinding_limit is not UNSET:
            field_dict["initialUnbindingLimit"] = initial_unbinding_limit
        if category is not UNSET:
            field_dict["category"] = category
        if forget_id is not UNSET:
            field_dict["forgetId"] = forget_id
        if sn is not UNSET:
            field_dict["sn"] = sn
        if eost is not UNSET:
            field_dict["eost"] = eost
        if eos is not UNSET:
            field_dict["eos"] = eos
        if in_whitelist is not UNSET:
            field_dict["inWhitelist"] = in_whitelist
        if location is not UNSET:
            field_dict["location"] = location
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if custom_name is not UNSET:
            field_dict["customName"] = custom_name
        if move_site_id is not UNSET:
            field_dict["moveSiteId"] = move_site_id
        if remember is not UNSET:
            field_dict["remember"] = remember
        if remember_device is not UNSET:
            field_dict["rememberDevice"] = remember_device
        if description is not UNSET:
            field_dict["description"] = description
        if disable_hw_reset is not UNSET:
            field_dict["disableHwReset"] = disable_hw_reset
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if bound_site_template is not UNSET:
            field_dict["boundSiteTemplate"] = bound_site_template
        if device_template_available is not UNSET:
            field_dict["deviceTemplateAvailable"] = device_template_available
        if bound_device_template is not UNSET:
            field_dict["boundDeviceTemplate"] = bound_device_template
        if site_template_name is not UNSET:
            field_dict["siteTemplateName"] = site_template_name
        if site_template_id is not UNSET:
            field_dict["siteTemplateId"] = site_template_id
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if resource is not UNSET:
            field_dict["resource"] = resource
        if ecsp_first_version is not UNSET:
            field_dict["ecspFirstVersion"] = ecsp_first_version
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if replace_device_info is not UNSET:
            field_dict["replaceDeviceInfo"] = replace_device_info
        if dev_cap is not UNSET:
            field_dict["devCap"] = dev_cap
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if snmp_seting is not UNSET:
            field_dict["snmpSeting"] = snmp_seting
        if iptv_setting is not UNSET:
            field_dict["iptvSetting"] = iptv_setting
        if support_hw_offload is not UNSET:
            field_dict["supportHwOffload"] = support_hw_offload
        if support_poe is not UNSET:
            field_dict["supportPoe"] = support_poe
        if hw_offload_enable is not UNSET:
            field_dict["hwOffloadEnable"] = hw_offload_enable
        if poe_settings is not UNSET:
            field_dict["poeSettings"] = poe_settings
        if lldp_enable is not UNSET:
            field_dict["lldpEnable"] = lldp_enable
        if lldp_setting is not UNSET:
            field_dict["lldpSetting"] = lldp_setting
        if echo_server is not UNSET:
            field_dict["echoServer"] = echo_server
        if ip is not UNSET:
            field_dict["ip"] = ip
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if uptime_long is not UNSET:
            field_dict["uptimeLong"] = uptime_long
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if port_stats is not UNSET:
            field_dict["portStats"] = port_stats
        if virtual_wan_stats is not UNSET:
            field_dict["virtualWanStats"] = virtual_wan_stats
        if support_lan_client_stats is not UNSET:
            field_dict["supportLanClientStats"] = support_lan_client_stats
        if support_port_forwarding_status is not UNSET:
            field_dict["supportPortForwardingStatus"] = support_port_forwarding_status
        if support_session_limit_status is not UNSET:
            field_dict["supportSessionLimitStatus"] = support_session_limit_status
        if support_channel_utilization_status is not UNSET:
            field_dict["supportChannelUtilizationStatus"] = (
                support_channel_utilization_status
            )
        if support_dropped_packets_status is not UNSET:
            field_dict["supportDroppedPacketsStatus"] = support_dropped_packets_status
        if support_retried_packets_status is not UNSET:
            field_dict["supportRetriedPacketsStatus"] = support_retried_packets_status
        if support_band_scan is not UNSET:
            field_dict["supportBandScan"] = support_band_scan
        if support_network_search is not UNSET:
            field_dict["supportNetworkSearch"] = support_network_search
        if lan_client_stats is not UNSET:
            field_dict["lanClientStats"] = lan_client_stats
        if controller_id is not UNSET:
            field_dict["controllerId"] = controller_id
        if need_upgrade is not UNSET:
            field_dict["needUpgrade"] = need_upgrade
        if support_dsl is not UNSET:
            field_dict["supportDsl"] = support_dsl
        if support_virtual_wan is not UNSET:
            field_dict["supportVirtualWan"] = support_virtual_wan
        if support_dual_sim is not UNSET:
            field_dict["supportDualSim"] = support_dual_sim
        if support_batch_edit is not UNSET:
            field_dict["supportBatchEdit"] = support_batch_edit
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if network_comptent is not UNSET:
            field_dict["networkComptent"] = network_comptent
        if temp is not UNSET:
            field_dict["temp"] = temp
        if fan is not UNSET:
            field_dict["fan"] = fan
        if rps is not UNSET:
            field_dict["rps"] = rps
        if port_configs is not UNSET:
            field_dict["portConfigs"] = port_configs
        if port_general_configs is not UNSET:
            field_dict["portGeneralConfigs"] = port_general_configs
        if support_speed_duplex is not UNSET:
            field_dict["supportSpeedDuplex"] = support_speed_duplex
        if support_mirror is not UNSET:
            field_dict["supportMirror"] = support_mirror
        if support_pvid is not UNSET:
            field_dict["supportPvid"] = support_pvid
        if support_wan_set_pvid is not UNSET:
            field_dict["supportWanSetPvid"] = support_wan_set_pvid
        if support_snmp is not UNSET:
            field_dict["supportSnmp"] = support_snmp
        if unsupported_ports is not UNSET:
            field_dict["unsupportedPorts"] = unsupported_ports
        if combined_gateway is not UNSET:
            field_dict["combinedGateway"] = combined_gateway
        if speeds is not UNSET:
            field_dict["speeds"] = speeds
        if support_lte is not UNSET:
            field_dict["supportLte"] = support_lte
        if pin_setting is not UNSET:
            field_dict["pinSetting"] = pin_setting
        if ippt is not UNSET:
            field_dict["ippt"] = ippt
        if ippt_preconfig is not UNSET:
            field_dict["ipptPreconfig"] = ippt_preconfig
        if support_ippt is not UNSET:
            field_dict["supportIppt"] = support_ippt
        if contain_net_type_5g is not UNSET:
            field_dict["containNetType5G"] = contain_net_type_5g
        if ssh_setting is not UNSET:
            field_dict["sshSetting"] = ssh_setting
        if multi_chip_gateway is not UNSET:
            field_dict["multiChipGateway"] = multi_chip_gateway
        if multi_chip_infos is not UNSET:
            field_dict["multiChipInfos"] = multi_chip_infos
        if support_flow_control is not UNSET:
            field_dict["supportFlowControl"] = support_flow_control
        if support_port_control is not UNSET:
            field_dict["supportPortControl"] = support_port_control
        if support_loopback_control is not UNSET:
            field_dict["supportLoopbackControl"] = support_loopback_control
        if support_port_isolation is not UNSET:
            field_dict["supportPortIsolation"] = support_port_isolation
        if support_band_width_ctrl is not UNSET:
            field_dict["supportBandWidthCtrl"] = support_band_width_ctrl
        if support_storm_ctrl_action is not UNSET:
            field_dict["supportStormCtrlAction"] = support_storm_ctrl_action
        if support_jumbo is not UNSET:
            field_dict["supportJumbo"] = support_jumbo
        if jumbo_size is not UNSET:
            field_dict["jumboSize"] = jumbo_size
        if jumbo_options is not UNSET:
            field_dict["jumboOptions"] = jumbo_options
        if downlink_list is not UNSET:
            field_dict["downlinkList"] = downlink_list
        if wireless_router is not UNSET:
            field_dict["wirelessRouter"] = wireless_router
        if wireless_health is not UNSET:
            field_dict["wirelessHealth"] = wireless_health
        if device_misc is not UNSET:
            field_dict["deviceMisc"] = device_misc
        if wp2g is not UNSET:
            field_dict["wp2g"] = wp2g
        if wp5g is not UNSET:
            field_dict["wp5g"] = wp5g
        if wp5g2 is not UNSET:
            field_dict["wp5g2"] = wp5g2
        if wp6g is not UNSET:
            field_dict["wp6g"] = wp6g
        if radio_setting_2_g is not UNSET:
            field_dict["radioSetting2g"] = radio_setting_2_g
        if radio_setting_5_g is not UNSET:
            field_dict["radioSetting5g"] = radio_setting_5_g
        if radio_setting_5_g_2 is not UNSET:
            field_dict["radioSetting5g2"] = radio_setting_5_g_2
        if radio_setting_6_g is not UNSET:
            field_dict["radioSetting6g"] = radio_setting_6_g
        if radio_traffic_2_g is not UNSET:
            field_dict["radioTraffic2g"] = radio_traffic_2_g
        if radio_traffic_5_g is not UNSET:
            field_dict["radioTraffic5g"] = radio_traffic_5_g
        if radio_traffic_5_g_2 is not UNSET:
            field_dict["radioTraffic5g2"] = radio_traffic_5_g_2
        if radio_traffic_6_g is not UNSET:
            field_dict["radioTraffic6g"] = radio_traffic_6_g
        if lb_setting_2_g is not UNSET:
            field_dict["lbSetting2g"] = lb_setting_2_g
        if lb_setting_5_g is not UNSET:
            field_dict["lbSetting5g"] = lb_setting_5_g
        if lb_setting_5_g_2 is not UNSET:
            field_dict["lbSetting5g2"] = lb_setting_5_g_2
        if lb_setting_6_g is not UNSET:
            field_dict["lbSetting6g"] = lb_setting_6_g
        if rssi_setting_2_g is not UNSET:
            field_dict["rssiSetting2g"] = rssi_setting_2_g
        if rssi_setting_5_g is not UNSET:
            field_dict["rssiSetting5g"] = rssi_setting_5_g
        if rssi_setting_5_g_2 is not UNSET:
            field_dict["rssiSetting5g2"] = rssi_setting_5_g_2
        if rssi_setting_6_g is not UNSET:
            field_dict["rssiSetting6g"] = rssi_setting_6_g
        if qos_setting_2_g is not UNSET:
            field_dict["qosSetting2g"] = qos_setting_2_g
        if qos_setting_5_g is not UNSET:
            field_dict["qosSetting5g"] = qos_setting_5_g
        if qos_setting_5_g_2 is not UNSET:
            field_dict["qosSetting5g2"] = qos_setting_5_g_2
        if qos_setting_6_g is not UNSET:
            field_dict["qosSetting6g"] = qos_setting_6_g
        if ofdma_enable_2_g is not UNSET:
            field_dict["ofdmaEnable2g"] = ofdma_enable_2_g
        if ofdma_enable_5_g is not UNSET:
            field_dict["ofdmaEnable5g"] = ofdma_enable_5_g
        if ofdma_enable_5_g_2 is not UNSET:
            field_dict["ofdmaEnable5g2"] = ofdma_enable_5_g_2
        if ofdma_enable_6_g is not UNSET:
            field_dict["ofdmaEnable6g"] = ofdma_enable_6_g
        if wlan_id is not UNSET:
            field_dict["wlanId"] = wlan_id
        if ssid_overrides is not UNSET:
            field_dict["ssidOverrides"] = ssid_overrides
        if non_psc_enable is not UNSET:
            field_dict["nonPscEnable"] = non_psc_enable
        if channel_limit_type is not UNSET:
            field_dict["channelLimitType"] = channel_limit_type
        if support_rf_scan is not UNSET:
            field_dict["supportRFScan"] = support_rf_scan
        if user_num is not UNSET:
            field_dict["userNum"] = user_num
        if guest_num is not UNSET:
            field_dict["guestNum"] = guest_num
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if add_by_template is not UNSET:
            field_dict["addByTemplate"] = add_by_template
        if services_resource is not UNSET:
            field_dict["servicesResource"] = services_resource
        if advanced_resource is not UNSET:
            field_dict["advancedResource"] = advanced_resource
        if common_advanced_resource is not UNSET:
            field_dict["commonAdvancedResource"] = common_advanced_resource
        if wireless_advanced_resource is not UNSET:
            field_dict["wirelessAdvancedResource"] = wireless_advanced_resource
        if radios_resource is not UNSET:
            field_dict["radiosResource"] = radios_resource
        if wlans_resource is not UNSET:
            field_dict["wlansResource"] = wlans_resource
        if template_settings is not UNSET:
            field_dict["templateSettings"] = template_settings
        if support_ip_mac_binding is not UNSET:
            field_dict["supportIpMacBinding"] = support_ip_mac_binding
        if support_new_ip_mac_binding is not UNSET:
            field_dict["supportNewIpMacBinding"] = support_new_ip_mac_binding
        if poe_limit is not UNSET:
            field_dict["poeLimit"] = poe_limit
        if poe_remain is not UNSET:
            field_dict["poeRemain"] = poe_remain
        if poe_remain_percent is not UNSET:
            field_dict["poeRemainPercent"] = poe_remain_percent
        if osg_cap is not UNSET:
            field_dict["osgCap"] = osg_cap
        if osg_exist is not UNSET:
            field_dict["osgExist"] = osg_exist

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_load_balance_vo import ApLoadBalanceVO
        from ..models.ap_qos_vo import ApQosVO
        from ..models.ap_radio_channel import ApRadioChannel
        from ..models.ap_radio_setting import ApRadioSetting
        from ..models.ap_radio_traffic_entity import (
            APRadioTrafficEntity,
        )
        from ..models.ap_rssi_threshold_vo import ApRssiThresholdVO
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )
        from ..models.device_replace_setting_vo import (
            DeviceReplaceSettingVO,
        )
        from ..models.exist_site_setting_vo import ExistSiteSettingVO
        from ..models.osg_cap_vo import OsgCapVO
        from ..models.osg_down_link_vo import OsgDownLinkVO
        from ..models.osg_fan_status_vo import OsgFanStatusVO
        from ..models.osg_iptv_vo import OsgIptvVO
        from ..models.osg_lan_stat_vo import OsgLanStatVO
        from ..models.osg_lte_pin_setting_vo import OsgLtePinSettingVO
        from ..models.osg_port_config_vo import OsgPortConfigVO
        from ..models.osg_port_general_config_vo import (
            OsgPortGeneralConfigVO,
        )
        from ..models.osg_port_poe_vo import OsgPortPoeVO
        from ..models.osg_port_stat_vo import OsgPortStatVO
        from ..models.osg_rps_status_vo import OsgRpsStatusVO
        from ..models.osg_snmp_vo import OsgSnmpVO
        from ..models.osg_virtual_wan_stat_vo import (
            OsgVirtualWanStatVO,
        )
        from ..models.site_setting_cap_vo import SiteSettingCapVO
        from ..models.ssh_setting_vo import SshSettingVO
        from ..models.ssid_override_vo import SsidOverrideVO
        from ..models.wireless_router_misc_vo import (
            WirelessRouterMiscVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        compound_model = d.pop("compoundModel", UNSET)

        show_model = d.pop("showModel", UNSET)

        special_model = d.pop("specialModel", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        version = d.pop("version", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        es = d.pop("es", UNSET)

        site = d.pop("site", UNSET)

        site_name = d.pop("siteName", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        compatible = d.pop("compatible", UNSET)

        support_anomaly = d.pop("supportAnomaly", UNSET)

        support_locate_port = d.pop("supportLocatePort", UNSET)

        active = d.pop("active", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        due_time = d.pop("dueTime", UNSET)

        due_time_left = d.pop("dueTimeLeft", UNSET)

        license_id = d.pop("licenseId", UNSET)

        license_unbinding_limit = d.pop("licenseUnbindingLimit", UNSET)

        initial_unbinding_limit = d.pop("initialUnbindingLimit", UNSET)

        category = d.pop("category", UNSET)

        forget_id = d.pop("forgetId", UNSET)

        sn = d.pop("sn", UNSET)

        eost = d.pop("eost", UNSET)

        eos = d.pop("eos", UNSET)

        in_whitelist = d.pop("inWhitelist", UNSET)

        _location = d.pop("location", UNSET)
        location: DeviceLocationDetailVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailVO.from_dict(_location)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        custom_id = d.pop("customId", UNSET)

        custom_name = d.pop("customName", UNSET)

        move_site_id = d.pop("moveSiteId", UNSET)

        remember = d.pop("remember", UNSET)

        remember_device = d.pop("rememberDevice", UNSET)

        description = d.pop("description", UNSET)

        disable_hw_reset = d.pop("disableHwReset", UNSET)

        template_id = d.pop("templateId", UNSET)

        template_name = d.pop("templateName", UNSET)

        bound_site_template = d.pop("boundSiteTemplate", UNSET)

        device_template_available = d.pop("deviceTemplateAvailable", UNSET)

        bound_device_template = d.pop("boundDeviceTemplate", UNSET)

        site_template_name = d.pop("siteTemplateName", UNSET)

        site_template_id = d.pop("siteTemplateId", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        resource = d.pop("resource", UNSET)

        ecsp_first_version = d.pop("ecspFirstVersion", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        _replace_device_info = d.pop("replaceDeviceInfo", UNSET)
        replace_device_info: DeviceReplaceSettingVO | Unset
        if isinstance(_replace_device_info, Unset):
            replace_device_info = UNSET
        else:
            replace_device_info = DeviceReplaceSettingVO.from_dict(_replace_device_info)

        _dev_cap = d.pop("devCap", UNSET)
        dev_cap: OsgCapVO | Unset
        if isinstance(_dev_cap, Unset):
            dev_cap = UNSET
        else:
            dev_cap = OsgCapVO.from_dict(_dev_cap)

        port_num = d.pop("portNum", UNSET)

        led_setting = d.pop("ledSetting", UNSET)

        _snmp_seting = d.pop("snmpSeting", UNSET)
        snmp_seting: OsgSnmpVO | Unset
        if isinstance(_snmp_seting, Unset):
            snmp_seting = UNSET
        else:
            snmp_seting = OsgSnmpVO.from_dict(_snmp_seting)

        _iptv_setting = d.pop("iptvSetting", UNSET)
        iptv_setting: OsgIptvVO | Unset
        if isinstance(_iptv_setting, Unset):
            iptv_setting = UNSET
        else:
            iptv_setting = OsgIptvVO.from_dict(_iptv_setting)

        support_hw_offload = d.pop("supportHwOffload", UNSET)

        support_poe = d.pop("supportPoe", UNSET)

        hw_offload_enable = d.pop("hwOffloadEnable", UNSET)

        _poe_settings = d.pop("poeSettings", UNSET)
        poe_settings: list[OsgPortPoeVO] | Unset = UNSET
        if _poe_settings is not UNSET:
            poe_settings = []
            for poe_settings_item_data in _poe_settings:
                poe_settings_item = OsgPortPoeVO.from_dict(poe_settings_item_data)

                poe_settings.append(poe_settings_item)

        lldp_enable = d.pop("lldpEnable", UNSET)

        lldp_setting = d.pop("lldpSetting", UNSET)

        echo_server = d.pop("echoServer", UNSET)

        ip = d.pop("ip", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        uptime = d.pop("uptime", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        _port_stats = d.pop("portStats", UNSET)
        port_stats: list[OsgPortStatVO] | Unset = UNSET
        if _port_stats is not UNSET:
            port_stats = []
            for port_stats_item_data in _port_stats:
                port_stats_item = OsgPortStatVO.from_dict(port_stats_item_data)

                port_stats.append(port_stats_item)

        _virtual_wan_stats = d.pop("virtualWanStats", UNSET)
        virtual_wan_stats: list[OsgVirtualWanStatVO] | Unset = UNSET
        if _virtual_wan_stats is not UNSET:
            virtual_wan_stats = []
            for virtual_wan_stats_item_data in _virtual_wan_stats:
                virtual_wan_stats_item = OsgVirtualWanStatVO.from_dict(
                    virtual_wan_stats_item_data
                )

                virtual_wan_stats.append(virtual_wan_stats_item)

        support_lan_client_stats = d.pop("supportLanClientStats", UNSET)

        support_port_forwarding_status = d.pop("supportPortForwardingStatus", UNSET)

        support_session_limit_status = d.pop("supportSessionLimitStatus", UNSET)

        support_channel_utilization_status = d.pop(
            "supportChannelUtilizationStatus", UNSET
        )

        support_dropped_packets_status = d.pop("supportDroppedPacketsStatus", UNSET)

        support_retried_packets_status = d.pop("supportRetriedPacketsStatus", UNSET)

        support_band_scan = d.pop("supportBandScan", UNSET)

        support_network_search = d.pop("supportNetworkSearch", UNSET)

        _lan_client_stats = d.pop("lanClientStats", UNSET)
        lan_client_stats: list[OsgLanStatVO] | Unset = UNSET
        if _lan_client_stats is not UNSET:
            lan_client_stats = []
            for lan_client_stats_item_data in _lan_client_stats:
                lan_client_stats_item = OsgLanStatVO.from_dict(
                    lan_client_stats_item_data
                )

                lan_client_stats.append(lan_client_stats_item)

        controller_id = d.pop("controllerId", UNSET)

        need_upgrade = d.pop("needUpgrade", UNSET)

        support_dsl = d.pop("supportDsl", UNSET)

        support_virtual_wan = d.pop("supportVirtualWan", UNSET)

        support_dual_sim = d.pop("supportDualSim", UNSET)

        support_batch_edit = d.pop("supportBatchEdit", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        network_comptent = d.pop("networkComptent", UNSET)

        temp = d.pop("temp", UNSET)

        _fan = d.pop("fan", UNSET)
        fan: list[OsgFanStatusVO] | Unset = UNSET
        if _fan is not UNSET:
            fan = []
            for fan_item_data in _fan:
                fan_item = OsgFanStatusVO.from_dict(fan_item_data)

                fan.append(fan_item)

        _rps = d.pop("rps", UNSET)
        rps: list[OsgRpsStatusVO] | Unset = UNSET
        if _rps is not UNSET:
            rps = []
            for rps_item_data in _rps:
                rps_item = OsgRpsStatusVO.from_dict(rps_item_data)

                rps.append(rps_item)

        _port_configs = d.pop("portConfigs", UNSET)
        port_configs: list[OsgPortConfigVO] | Unset = UNSET
        if _port_configs is not UNSET:
            port_configs = []
            for port_configs_item_data in _port_configs:
                port_configs_item = OsgPortConfigVO.from_dict(port_configs_item_data)

                port_configs.append(port_configs_item)

        _port_general_configs = d.pop("portGeneralConfigs", UNSET)
        port_general_configs: list[OsgPortGeneralConfigVO] | Unset = UNSET
        if _port_general_configs is not UNSET:
            port_general_configs = []
            for port_general_configs_item_data in _port_general_configs:
                port_general_configs_item = OsgPortGeneralConfigVO.from_dict(
                    port_general_configs_item_data
                )

                port_general_configs.append(port_general_configs_item)

        support_speed_duplex = d.pop("supportSpeedDuplex", UNSET)

        support_mirror = d.pop("supportMirror", UNSET)

        support_pvid = d.pop("supportPvid", UNSET)

        support_wan_set_pvid = d.pop("supportWanSetPvid", UNSET)

        support_snmp = d.pop("supportSnmp", UNSET)

        unsupported_ports = cast(list[int], d.pop("unsupportedPorts", UNSET))

        combined_gateway = d.pop("combinedGateway", UNSET)

        speeds = cast(list[int], d.pop("speeds", UNSET))

        support_lte = d.pop("supportLte", UNSET)

        _pin_setting = d.pop("pinSetting", UNSET)
        pin_setting: OsgLtePinSettingVO | Unset
        if isinstance(_pin_setting, Unset):
            pin_setting = UNSET
        else:
            pin_setting = OsgLtePinSettingVO.from_dict(_pin_setting)

        ippt = d.pop("ippt", UNSET)

        ippt_preconfig = d.pop("ipptPreconfig", UNSET)

        support_ippt = d.pop("supportIppt", UNSET)

        contain_net_type_5g = d.pop("containNetType5G", UNSET)

        _ssh_setting = d.pop("sshSetting", UNSET)
        ssh_setting: SshSettingVO | Unset
        if isinstance(_ssh_setting, Unset):
            ssh_setting = UNSET
        else:
            ssh_setting = SshSettingVO.from_dict(_ssh_setting)

        multi_chip_gateway = d.pop("multiChipGateway", UNSET)

        _multi_chip_infos = d.pop("multiChipInfos", UNSET)
        multi_chip_infos: list[list[int]] | Unset = UNSET
        if _multi_chip_infos is not UNSET:
            multi_chip_infos = []
            for multi_chip_infos_item_data in _multi_chip_infos:
                multi_chip_infos_item = cast(list[int], multi_chip_infos_item_data)

                multi_chip_infos.append(multi_chip_infos_item)

        support_flow_control = d.pop("supportFlowControl", UNSET)

        support_port_control = d.pop("supportPortControl", UNSET)

        support_loopback_control = d.pop("supportLoopbackControl", UNSET)

        support_port_isolation = d.pop("supportPortIsolation", UNSET)

        support_band_width_ctrl = d.pop("supportBandWidthCtrl", UNSET)

        support_storm_ctrl_action = d.pop("supportStormCtrlAction", UNSET)

        support_jumbo = d.pop("supportJumbo", UNSET)

        jumbo_size = d.pop("jumboSize", UNSET)

        jumbo_options = cast(list[int], d.pop("jumboOptions", UNSET))

        _downlink_list = d.pop("downlinkList", UNSET)
        downlink_list: list[OsgDownLinkVO] | Unset = UNSET
        if _downlink_list is not UNSET:
            downlink_list = []
            for downlink_list_item_data in _downlink_list:
                downlink_list_item = OsgDownLinkVO.from_dict(downlink_list_item_data)

                downlink_list.append(downlink_list_item)

        wireless_router = d.pop("wirelessRouter", UNSET)

        wireless_health = d.pop("wirelessHealth", UNSET)

        _device_misc = d.pop("deviceMisc", UNSET)
        device_misc: WirelessRouterMiscVO | Unset
        if isinstance(_device_misc, Unset):
            device_misc = UNSET
        else:
            device_misc = WirelessRouterMiscVO.from_dict(_device_misc)

        _wp2g = d.pop("wp2g", UNSET)
        wp2g: ApRadioChannel | Unset
        if isinstance(_wp2g, Unset):
            wp2g = UNSET
        else:
            wp2g = ApRadioChannel.from_dict(_wp2g)

        _wp5g = d.pop("wp5g", UNSET)
        wp5g: ApRadioChannel | Unset
        if isinstance(_wp5g, Unset):
            wp5g = UNSET
        else:
            wp5g = ApRadioChannel.from_dict(_wp5g)

        _wp5g2 = d.pop("wp5g2", UNSET)
        wp5g2: ApRadioChannel | Unset
        if isinstance(_wp5g2, Unset):
            wp5g2 = UNSET
        else:
            wp5g2 = ApRadioChannel.from_dict(_wp5g2)

        _wp6g = d.pop("wp6g", UNSET)
        wp6g: ApRadioChannel | Unset
        if isinstance(_wp6g, Unset):
            wp6g = UNSET
        else:
            wp6g = ApRadioChannel.from_dict(_wp6g)

        _radio_setting_2_g = d.pop("radioSetting2g", UNSET)
        radio_setting_2_g: ApRadioSetting | Unset
        if isinstance(_radio_setting_2_g, Unset):
            radio_setting_2_g = UNSET
        else:
            radio_setting_2_g = ApRadioSetting.from_dict(_radio_setting_2_g)

        _radio_setting_5_g = d.pop("radioSetting5g", UNSET)
        radio_setting_5_g: ApRadioSetting | Unset
        if isinstance(_radio_setting_5_g, Unset):
            radio_setting_5_g = UNSET
        else:
            radio_setting_5_g = ApRadioSetting.from_dict(_radio_setting_5_g)

        _radio_setting_5_g_2 = d.pop("radioSetting5g2", UNSET)
        radio_setting_5_g_2: ApRadioSetting | Unset
        if isinstance(_radio_setting_5_g_2, Unset):
            radio_setting_5_g_2 = UNSET
        else:
            radio_setting_5_g_2 = ApRadioSetting.from_dict(_radio_setting_5_g_2)

        _radio_setting_6_g = d.pop("radioSetting6g", UNSET)
        radio_setting_6_g: ApRadioSetting | Unset
        if isinstance(_radio_setting_6_g, Unset):
            radio_setting_6_g = UNSET
        else:
            radio_setting_6_g = ApRadioSetting.from_dict(_radio_setting_6_g)

        _radio_traffic_2_g = d.pop("radioTraffic2g", UNSET)
        radio_traffic_2_g: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_2_g, Unset):
            radio_traffic_2_g = UNSET
        else:
            radio_traffic_2_g = APRadioTrafficEntity.from_dict(_radio_traffic_2_g)

        _radio_traffic_5_g = d.pop("radioTraffic5g", UNSET)
        radio_traffic_5_g: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_5_g, Unset):
            radio_traffic_5_g = UNSET
        else:
            radio_traffic_5_g = APRadioTrafficEntity.from_dict(_radio_traffic_5_g)

        _radio_traffic_5_g_2 = d.pop("radioTraffic5g2", UNSET)
        radio_traffic_5_g_2: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_5_g_2, Unset):
            radio_traffic_5_g_2 = UNSET
        else:
            radio_traffic_5_g_2 = APRadioTrafficEntity.from_dict(_radio_traffic_5_g_2)

        _radio_traffic_6_g = d.pop("radioTraffic6g", UNSET)
        radio_traffic_6_g: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_6_g, Unset):
            radio_traffic_6_g = UNSET
        else:
            radio_traffic_6_g = APRadioTrafficEntity.from_dict(_radio_traffic_6_g)

        _lb_setting_2_g = d.pop("lbSetting2g", UNSET)
        lb_setting_2_g: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_2_g, Unset):
            lb_setting_2_g = UNSET
        else:
            lb_setting_2_g = ApLoadBalanceVO.from_dict(_lb_setting_2_g)

        _lb_setting_5_g = d.pop("lbSetting5g", UNSET)
        lb_setting_5_g: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_5_g, Unset):
            lb_setting_5_g = UNSET
        else:
            lb_setting_5_g = ApLoadBalanceVO.from_dict(_lb_setting_5_g)

        _lb_setting_5_g_2 = d.pop("lbSetting5g2", UNSET)
        lb_setting_5_g_2: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_5_g_2, Unset):
            lb_setting_5_g_2 = UNSET
        else:
            lb_setting_5_g_2 = ApLoadBalanceVO.from_dict(_lb_setting_5_g_2)

        _lb_setting_6_g = d.pop("lbSetting6g", UNSET)
        lb_setting_6_g: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_6_g, Unset):
            lb_setting_6_g = UNSET
        else:
            lb_setting_6_g = ApLoadBalanceVO.from_dict(_lb_setting_6_g)

        _rssi_setting_2_g = d.pop("rssiSetting2g", UNSET)
        rssi_setting_2_g: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_2_g, Unset):
            rssi_setting_2_g = UNSET
        else:
            rssi_setting_2_g = ApRssiThresholdVO.from_dict(_rssi_setting_2_g)

        _rssi_setting_5_g = d.pop("rssiSetting5g", UNSET)
        rssi_setting_5_g: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_5_g, Unset):
            rssi_setting_5_g = UNSET
        else:
            rssi_setting_5_g = ApRssiThresholdVO.from_dict(_rssi_setting_5_g)

        _rssi_setting_5_g_2 = d.pop("rssiSetting5g2", UNSET)
        rssi_setting_5_g_2: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_5_g_2, Unset):
            rssi_setting_5_g_2 = UNSET
        else:
            rssi_setting_5_g_2 = ApRssiThresholdVO.from_dict(_rssi_setting_5_g_2)

        _rssi_setting_6_g = d.pop("rssiSetting6g", UNSET)
        rssi_setting_6_g: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_6_g, Unset):
            rssi_setting_6_g = UNSET
        else:
            rssi_setting_6_g = ApRssiThresholdVO.from_dict(_rssi_setting_6_g)

        _qos_setting_2_g = d.pop("qosSetting2g", UNSET)
        qos_setting_2_g: ApQosVO | Unset
        if isinstance(_qos_setting_2_g, Unset):
            qos_setting_2_g = UNSET
        else:
            qos_setting_2_g = ApQosVO.from_dict(_qos_setting_2_g)

        _qos_setting_5_g = d.pop("qosSetting5g", UNSET)
        qos_setting_5_g: ApQosVO | Unset
        if isinstance(_qos_setting_5_g, Unset):
            qos_setting_5_g = UNSET
        else:
            qos_setting_5_g = ApQosVO.from_dict(_qos_setting_5_g)

        _qos_setting_5_g_2 = d.pop("qosSetting5g2", UNSET)
        qos_setting_5_g_2: ApQosVO | Unset
        if isinstance(_qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = UNSET
        else:
            qos_setting_5_g_2 = ApQosVO.from_dict(_qos_setting_5_g_2)

        _qos_setting_6_g = d.pop("qosSetting6g", UNSET)
        qos_setting_6_g: ApQosVO | Unset
        if isinstance(_qos_setting_6_g, Unset):
            qos_setting_6_g = UNSET
        else:
            qos_setting_6_g = ApQosVO.from_dict(_qos_setting_6_g)

        ofdma_enable_2_g = d.pop("ofdmaEnable2g", UNSET)

        ofdma_enable_5_g = d.pop("ofdmaEnable5g", UNSET)

        ofdma_enable_5_g_2 = d.pop("ofdmaEnable5g2", UNSET)

        ofdma_enable_6_g = d.pop("ofdmaEnable6g", UNSET)

        wlan_id = d.pop("wlanId", UNSET)

        _ssid_overrides = d.pop("ssidOverrides", UNSET)
        ssid_overrides: list[SsidOverrideVO] | Unset = UNSET
        if _ssid_overrides is not UNSET:
            ssid_overrides = []
            for ssid_overrides_item_data in _ssid_overrides:
                ssid_overrides_item = SsidOverrideVO.from_dict(ssid_overrides_item_data)

                ssid_overrides.append(ssid_overrides_item)

        non_psc_enable = d.pop("nonPscEnable", UNSET)

        channel_limit_type = d.pop("channelLimitType", UNSET)

        support_rf_scan = d.pop("supportRFScan", UNSET)

        user_num = d.pop("userNum", UNSET)

        guest_num = d.pop("guestNum", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        add_by_template = d.pop("addByTemplate", UNSET)

        services_resource = d.pop("servicesResource", UNSET)

        advanced_resource = d.pop("advancedResource", UNSET)

        common_advanced_resource = d.pop("commonAdvancedResource", UNSET)

        wireless_advanced_resource = d.pop("wirelessAdvancedResource", UNSET)

        radios_resource = d.pop("radiosResource", UNSET)

        wlans_resource = d.pop("wlansResource", UNSET)

        template_settings = cast(list[int], d.pop("templateSettings", UNSET))

        support_ip_mac_binding = d.pop("supportIpMacBinding", UNSET)

        support_new_ip_mac_binding = d.pop("supportNewIpMacBinding", UNSET)

        poe_limit = d.pop("poeLimit", UNSET)

        poe_remain = d.pop("poeRemain", UNSET)

        poe_remain_percent = d.pop("poeRemainPercent", UNSET)

        _osg_cap = d.pop("osgCap", UNSET)
        osg_cap: SiteSettingCapVO | Unset
        if isinstance(_osg_cap, Unset):
            osg_cap = UNSET
        else:
            osg_cap = SiteSettingCapVO.from_dict(_osg_cap)

        _osg_exist = d.pop("osgExist", UNSET)
        osg_exist: ExistSiteSettingVO | Unset
        if isinstance(_osg_exist, Unset):
            osg_exist = UNSET
        else:
            osg_exist = ExistSiteSettingVO.from_dict(_osg_exist)

        osg_detail_vo = cls(
            type_=type_,
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            compound_model=compound_model,
            show_model=show_model,
            special_model=special_model,
            firmware_version=firmware_version,
            version=version,
            hw_version=hw_version,
            status=status,
            status_category=status_category,
            es=es,
            site=site,
            site_name=site_name,
            omadac_id=omadac_id,
            compatible=compatible,
            support_anomaly=support_anomaly,
            support_locate_port=support_locate_port,
            active=active,
            license_status=license_status,
            due_time=due_time,
            due_time_left=due_time_left,
            license_id=license_id,
            license_unbinding_limit=license_unbinding_limit,
            initial_unbinding_limit=initial_unbinding_limit,
            category=category,
            forget_id=forget_id,
            sn=sn,
            eost=eost,
            eos=eos,
            in_whitelist=in_whitelist,
            location=location,
            added_in_advanced=added_in_advanced,
            custom_id=custom_id,
            custom_name=custom_name,
            move_site_id=move_site_id,
            remember=remember,
            remember_device=remember_device,
            description=description,
            disable_hw_reset=disable_hw_reset,
            template_id=template_id,
            template_name=template_name,
            bound_site_template=bound_site_template,
            device_template_available=device_template_available,
            bound_device_template=bound_device_template,
            site_template_name=site_template_name,
            site_template_id=site_template_id,
            device_series_type=device_series_type,
            resource=resource,
            ecsp_first_version=ecsp_first_version,
            latest_version=latest_version,
            replace_device_info=replace_device_info,
            dev_cap=dev_cap,
            port_num=port_num,
            led_setting=led_setting,
            snmp_seting=snmp_seting,
            iptv_setting=iptv_setting,
            support_hw_offload=support_hw_offload,
            support_poe=support_poe,
            hw_offload_enable=hw_offload_enable,
            poe_settings=poe_settings,
            lldp_enable=lldp_enable,
            lldp_setting=lldp_setting,
            echo_server=echo_server,
            ip=ip,
            public_ip=public_ip,
            ipv_6_list=ipv_6_list,
            uptime=uptime,
            uptime_long=uptime_long,
            cpu_util=cpu_util,
            mem_util=mem_util,
            last_seen=last_seen,
            port_stats=port_stats,
            virtual_wan_stats=virtual_wan_stats,
            support_lan_client_stats=support_lan_client_stats,
            support_port_forwarding_status=support_port_forwarding_status,
            support_session_limit_status=support_session_limit_status,
            support_channel_utilization_status=support_channel_utilization_status,
            support_dropped_packets_status=support_dropped_packets_status,
            support_retried_packets_status=support_retried_packets_status,
            support_band_scan=support_band_scan,
            support_network_search=support_network_search,
            lan_client_stats=lan_client_stats,
            controller_id=controller_id,
            need_upgrade=need_upgrade,
            support_dsl=support_dsl,
            support_virtual_wan=support_virtual_wan,
            support_dual_sim=support_dual_sim,
            support_batch_edit=support_batch_edit,
            download=download,
            upload=upload,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            network_comptent=network_comptent,
            temp=temp,
            fan=fan,
            rps=rps,
            port_configs=port_configs,
            port_general_configs=port_general_configs,
            support_speed_duplex=support_speed_duplex,
            support_mirror=support_mirror,
            support_pvid=support_pvid,
            support_wan_set_pvid=support_wan_set_pvid,
            support_snmp=support_snmp,
            unsupported_ports=unsupported_ports,
            combined_gateway=combined_gateway,
            speeds=speeds,
            support_lte=support_lte,
            pin_setting=pin_setting,
            ippt=ippt,
            ippt_preconfig=ippt_preconfig,
            support_ippt=support_ippt,
            contain_net_type_5g=contain_net_type_5g,
            ssh_setting=ssh_setting,
            multi_chip_gateway=multi_chip_gateway,
            multi_chip_infos=multi_chip_infos,
            support_flow_control=support_flow_control,
            support_port_control=support_port_control,
            support_loopback_control=support_loopback_control,
            support_port_isolation=support_port_isolation,
            support_band_width_ctrl=support_band_width_ctrl,
            support_storm_ctrl_action=support_storm_ctrl_action,
            support_jumbo=support_jumbo,
            jumbo_size=jumbo_size,
            jumbo_options=jumbo_options,
            downlink_list=downlink_list,
            wireless_router=wireless_router,
            wireless_health=wireless_health,
            device_misc=device_misc,
            wp2g=wp2g,
            wp5g=wp5g,
            wp5g2=wp5g2,
            wp6g=wp6g,
            radio_setting_2_g=radio_setting_2_g,
            radio_setting_5_g=radio_setting_5_g,
            radio_setting_5_g_2=radio_setting_5_g_2,
            radio_setting_6_g=radio_setting_6_g,
            radio_traffic_2_g=radio_traffic_2_g,
            radio_traffic_5_g=radio_traffic_5_g,
            radio_traffic_5_g_2=radio_traffic_5_g_2,
            radio_traffic_6_g=radio_traffic_6_g,
            lb_setting_2_g=lb_setting_2_g,
            lb_setting_5_g=lb_setting_5_g,
            lb_setting_5_g_2=lb_setting_5_g_2,
            lb_setting_6_g=lb_setting_6_g,
            rssi_setting_2_g=rssi_setting_2_g,
            rssi_setting_5_g=rssi_setting_5_g,
            rssi_setting_5_g_2=rssi_setting_5_g_2,
            rssi_setting_6_g=rssi_setting_6_g,
            qos_setting_2_g=qos_setting_2_g,
            qos_setting_5_g=qos_setting_5_g,
            qos_setting_5_g_2=qos_setting_5_g_2,
            qos_setting_6_g=qos_setting_6_g,
            ofdma_enable_2_g=ofdma_enable_2_g,
            ofdma_enable_5_g=ofdma_enable_5_g,
            ofdma_enable_5_g_2=ofdma_enable_5_g_2,
            ofdma_enable_6_g=ofdma_enable_6_g,
            wlan_id=wlan_id,
            ssid_overrides=ssid_overrides,
            non_psc_enable=non_psc_enable,
            channel_limit_type=channel_limit_type,
            support_rf_scan=support_rf_scan,
            user_num=user_num,
            guest_num=guest_num,
            tag_ids=tag_ids,
            add_by_template=add_by_template,
            services_resource=services_resource,
            advanced_resource=advanced_resource,
            common_advanced_resource=common_advanced_resource,
            wireless_advanced_resource=wireless_advanced_resource,
            radios_resource=radios_resource,
            wlans_resource=wlans_resource,
            template_settings=template_settings,
            support_ip_mac_binding=support_ip_mac_binding,
            support_new_ip_mac_binding=support_new_ip_mac_binding,
            poe_limit=poe_limit,
            poe_remain=poe_remain,
            poe_remain_percent=poe_remain_percent,
            osg_cap=osg_cap,
            osg_exist=osg_exist,
        )

        osg_detail_vo.additional_properties = d
        return osg_detail_vo

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
