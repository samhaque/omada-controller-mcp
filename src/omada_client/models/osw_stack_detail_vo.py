from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_location_detail_vo import DeviceLocationDetailVO
    from ..models.device_replace_setting_vo import DeviceReplaceSettingVO
    from ..models.ip_setting_vo import IpSettingVO
    from ..models.mac_delay_vo import MacDelayVO
    from ..models.mlag_msg_vo import MlagMsgVO
    from ..models.osw_dev_cap_vo import OswDevCapVO
    from ..models.osw_device_misc_vo import OswDeviceMiscVO
    from ..models.osw_downlink_vo import OswDownlinkVO
    from ..models.osw_lag_vo import OswLagVO
    from ..models.osw_lan_multicast_vo import OswLanMulticastVO
    from ..models.osw_mlag_peer_info_vo import OswMlagPeerInfoVO
    from ..models.osw_mtu_count_vo import OswMtuCountVO
    from ..models.osw_port_vo import OswPortVO
    from ..models.osw_qos_config_vo import OswQosConfigVO
    from ..models.osw_sdm_template_vo import OswSdmTemplateVO
    from ..models.osw_snmp_vo import OswSnmpVO
    from ..models.osw_stack_member_lag_vo import OswStackMemberLagVO
    from ..models.osw_stack_member_vo import OswStackMemberVO
    from ..models.osw_stack_port_group_vo import OswStackPortGroupVO
    from ..models.osw_stp_mstp_vo import OswStpMstpVO
    from ..models.osw_uplink_vo import OswUplinkVO
    from ..models.stack_msg_vo import StackMsgVO


T = TypeVar("T", bound="OswStackDetailVO")


@_attrs_define
class OswStackDetailVO:
    """Stack detail

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
        status (int | Unset): Status is a value as follows: 0: normal; 1:abnormal; 2:stackNotReady
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        es (bool | Unset): Whether the switch is Agile Series Switch
        site (str | Unset): Site of the device
        site_name (str | Unset): Site Name
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
        sn (str | Unset): Device serial number
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
        device_misc (OswDeviceMiscVO | Unset): Device Misc
        dev_cap (OswDevCapVO | Unset): Capability of device
        led_setting (int | Unset): LedSetting should be a value as follows: 0: Off; 1: On; 2:follow site
        mvlan_network_id (str | Unset): Management VLAN network ID
        mvlan_bridge_vlan (int | Unset): Only valid when mvlanNetworkId is bridge vlan
        ip_setting (IpSettingVO | Unset): Ip Setting
        loopback_detect_enable (bool | Unset): Loopback Detect Enable
        stp (int | Unset): Spanning Tree Protocol should be a value as follows: 1: STP; 2: RSTP; 3: MSTP; 0: OFF
        priority (int | Unset): STP priority
        hello_time (int | Unset): STP helloTime
        max_age (int | Unset): STP maxAge
        forward_delay (int | Unset): STP forwardDelay
        tx_hold_count (int | Unset): STP txHoldCount
        max_hops (int | Unset): STP maxHops
        mstp (OswStpMstpVO | Unset): STP MSTP mode settging
        qos_config (OswQosConfigVO | Unset): Switch qos config
        snmp (OswSnmpVO | Unset): Snmp setting
        multicast (OswLanMulticastVO | Unset):
        ports (list[OswPortVO] | Unset): Port List
        lags (list[OswLagVO] | Unset): Lag List
        tag_ids (list[str] | Unset): The bound TAG ID List
        ip (str | Unset): Switch IP
        public_ip (str | Unset): Public IP
        ipv_6_list (list[str] | Unset): IPV6 List
        last_seen (int | Unset): Last Seen
        need_upgrade (bool | Unset): Need Upgrade
        uptime (str | Unset): Uptime
        uptime_long (int | Unset): UptimeLong, Running duration, Units: seconds
        cpu_util (int | Unset): Real-time CPU usage
        mem_uitl (int | Unset): Real-time memory usage
        poe_total_power (float | Unset): PoE Total Power (W)
        poe_remain (float | Unset): PoE Residual Power (W)
        poe_remain_percent (float | Unset): PoE Residual Power Percentage
        fan_status (int | Unset): Fan Status should be a value as follows: 0:normal; 1:fault; 2:no fan
        uplink (OswUplinkVO | Unset): Uplink Omada device
        uplink_port (int | Unset): Uplink port
        uplink_st_port (str | Unset): Uplink standard port,unit/slot/port
        downlink_list (list[OswDownlinkVO] | Unset): Downlink Omada device list
        stp_link_list (list[OswDownlinkVO] | Unset): STP Blocked Link Omada device list
        download (int | Unset): Total Download (Byte)
        upload (int | Unset): Total Upload (Byte)
        support_vlan_if (bool | Unset): Support Vlan Interface
        jumbo (int | Unset): Jumbo should be within the range of 1518-9216.
        jumbo_follow_site (bool | Unset): When enabled, the jumbo frame setting follows the site-level configuration;
            otherwise, a custom setting is used.
        lag_hash_alg (int | Unset): It should be a value as follows: 0: SRC MAC; 1: DST MAC; 2: SRC MAC + DST MAC; 3:
            SRC IP; 4: DST IP; 5: SRC IP + DST IP
        lag_hash_alg_follow_site (bool | Unset): When enabled, the lag hash alg setting follows the site-level
            configuration; otherwise, a custom setting is used.
        speeds (list[int] | Unset): Supported rate list for all ports. Speeds should be a value as follows: 0:auto;
            1:10M; 2:100M; 3:1000M; 4:2.5G; 5:10G; 6:5G; 7:25G; 8:100G; 9:40G; -1:error; no value:all rate supported
        support_ipv_6_acl (bool | Unset): Support Ipv6 Acl
        stack_device (bool | Unset): Stack Device
        support_vrf (bool | Unset): Support Vrf
        unit (int | Unset): Unit ID
        stack_ports (list[OswStackPortGroupVO] | Unset): Stack Port List
        stack_msg (StackMsgVO | Unset): Stack Message
        template_settings (list[int] | Unset): Template Setting List
        loop (str | Unset): Loop information
        loopback_num (int | Unset): Loopback Num
        block (str | Unset): Block information
        block_num (int | Unset): Block Num
        tx_rate (int | Unset): Tx Rate
        rx_rate (int | Unset): Rx Rate
        mlag_msg (MlagMsgVO | Unset): M-LAG Message
        mlag_peer_info (OswMlagPeerInfoVO | Unset): M-LAG Peer device info
        sdm (OswSdmTemplateVO | Unset): Sdm template
        terminal_prefix (str | Unset): TerminalPrefix represents the device name within the terminal function, designed
            to prevent terminal command recognition errors when device name contains illegal characters such as '#'.
        support_health (bool | Unset): Support health
        pmtud_enable (bool | Unset): Path MTU Discovery enable.
        support_auto_add_oui_based_vlan (bool | Unset): Whether support auto add oui based vlan.
        mtu_list (list[OswMtuCountVO] | Unset): MTU List
        id (str | Unset): Stack ID
        site_id (str | Unset): Site ID
        master_mac (str | Unset): Master Device Mac
        master_active (bool | Unset): Master Active
        abnormal_reason (int | Unset): When status is 1, show abnormal reason.
        inactive_units (list[int] | Unset): Inactive units
        member (list[OswStackMemberVO] | Unset): Member List
        stack_lags (list[OswStackMemberLagVO] | Unset): Stack Lag List
        locate_enable (bool | Unset): Locate Enable
        mac_delay (MacDelayVO | Unset): Mac Delay
        virtual_mac (str | Unset): Virtual Mac
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
    device_misc: OswDeviceMiscVO | Unset = UNSET
    dev_cap: OswDevCapVO | Unset = UNSET
    led_setting: int | Unset = UNSET
    mvlan_network_id: str | Unset = UNSET
    mvlan_bridge_vlan: int | Unset = UNSET
    ip_setting: IpSettingVO | Unset = UNSET
    loopback_detect_enable: bool | Unset = UNSET
    stp: int | Unset = UNSET
    priority: int | Unset = UNSET
    hello_time: int | Unset = UNSET
    max_age: int | Unset = UNSET
    forward_delay: int | Unset = UNSET
    tx_hold_count: int | Unset = UNSET
    max_hops: int | Unset = UNSET
    mstp: OswStpMstpVO | Unset = UNSET
    qos_config: OswQosConfigVO | Unset = UNSET
    snmp: OswSnmpVO | Unset = UNSET
    multicast: OswLanMulticastVO | Unset = UNSET
    ports: list[OswPortVO] | Unset = UNSET
    lags: list[OswLagVO] | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    ip: str | Unset = UNSET
    public_ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    last_seen: int | Unset = UNSET
    need_upgrade: bool | Unset = UNSET
    uptime: str | Unset = UNSET
    uptime_long: int | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_uitl: int | Unset = UNSET
    poe_total_power: float | Unset = UNSET
    poe_remain: float | Unset = UNSET
    poe_remain_percent: float | Unset = UNSET
    fan_status: int | Unset = UNSET
    uplink: OswUplinkVO | Unset = UNSET
    uplink_port: int | Unset = UNSET
    uplink_st_port: str | Unset = UNSET
    downlink_list: list[OswDownlinkVO] | Unset = UNSET
    stp_link_list: list[OswDownlinkVO] | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    support_vlan_if: bool | Unset = UNSET
    jumbo: int | Unset = UNSET
    jumbo_follow_site: bool | Unset = UNSET
    lag_hash_alg: int | Unset = UNSET
    lag_hash_alg_follow_site: bool | Unset = UNSET
    speeds: list[int] | Unset = UNSET
    support_ipv_6_acl: bool | Unset = UNSET
    stack_device: bool | Unset = UNSET
    support_vrf: bool | Unset = UNSET
    unit: int | Unset = UNSET
    stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
    stack_msg: StackMsgVO | Unset = UNSET
    template_settings: list[int] | Unset = UNSET
    loop: str | Unset = UNSET
    loopback_num: int | Unset = UNSET
    block: str | Unset = UNSET
    block_num: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    mlag_msg: MlagMsgVO | Unset = UNSET
    mlag_peer_info: OswMlagPeerInfoVO | Unset = UNSET
    sdm: OswSdmTemplateVO | Unset = UNSET
    terminal_prefix: str | Unset = UNSET
    support_health: bool | Unset = UNSET
    pmtud_enable: bool | Unset = UNSET
    support_auto_add_oui_based_vlan: bool | Unset = UNSET
    mtu_list: list[OswMtuCountVO] | Unset = UNSET
    id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    master_mac: str | Unset = UNSET
    master_active: bool | Unset = UNSET
    abnormal_reason: int | Unset = UNSET
    inactive_units: list[int] | Unset = UNSET
    member: list[OswStackMemberVO] | Unset = UNSET
    stack_lags: list[OswStackMemberLagVO] | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    mac_delay: MacDelayVO | Unset = UNSET
    virtual_mac: str | Unset = UNSET
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

        device_misc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_misc, Unset):
            device_misc = self.device_misc.to_dict()

        dev_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_cap, Unset):
            dev_cap = self.dev_cap.to_dict()

        led_setting = self.led_setting

        mvlan_network_id = self.mvlan_network_id

        mvlan_bridge_vlan = self.mvlan_bridge_vlan

        ip_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_setting, Unset):
            ip_setting = self.ip_setting.to_dict()

        loopback_detect_enable = self.loopback_detect_enable

        stp = self.stp

        priority = self.priority

        hello_time = self.hello_time

        max_age = self.max_age

        forward_delay = self.forward_delay

        tx_hold_count = self.tx_hold_count

        max_hops = self.max_hops

        mstp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mstp, Unset):
            mstp = self.mstp.to_dict()

        qos_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_config, Unset):
            qos_config = self.qos_config.to_dict()

        snmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        multicast: dict[str, Any] | Unset = UNSET
        if not isinstance(self.multicast, Unset):
            multicast = self.multicast.to_dict()

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        ip = self.ip

        public_ip = self.public_ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        last_seen = self.last_seen

        need_upgrade = self.need_upgrade

        uptime = self.uptime

        uptime_long = self.uptime_long

        cpu_util = self.cpu_util

        mem_uitl = self.mem_uitl

        poe_total_power = self.poe_total_power

        poe_remain = self.poe_remain

        poe_remain_percent = self.poe_remain_percent

        fan_status = self.fan_status

        uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink, Unset):
            uplink = self.uplink.to_dict()

        uplink_port = self.uplink_port

        uplink_st_port = self.uplink_st_port

        downlink_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_list, Unset):
            downlink_list = []
            for downlink_list_item_data in self.downlink_list:
                downlink_list_item = downlink_list_item_data.to_dict()
                downlink_list.append(downlink_list_item)

        stp_link_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stp_link_list, Unset):
            stp_link_list = []
            for stp_link_list_item_data in self.stp_link_list:
                stp_link_list_item = stp_link_list_item_data.to_dict()
                stp_link_list.append(stp_link_list_item)

        download = self.download

        upload = self.upload

        support_vlan_if = self.support_vlan_if

        jumbo = self.jumbo

        jumbo_follow_site = self.jumbo_follow_site

        lag_hash_alg = self.lag_hash_alg

        lag_hash_alg_follow_site = self.lag_hash_alg_follow_site

        speeds: list[int] | Unset = UNSET
        if not isinstance(self.speeds, Unset):
            speeds = self.speeds

        support_ipv_6_acl = self.support_ipv_6_acl

        stack_device = self.stack_device

        support_vrf = self.support_vrf

        unit = self.unit

        stack_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_ports, Unset):
            stack_ports = []
            for stack_ports_item_data in self.stack_ports:
                stack_ports_item = stack_ports_item_data.to_dict()
                stack_ports.append(stack_ports_item)

        stack_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_msg, Unset):
            stack_msg = self.stack_msg.to_dict()

        template_settings: list[int] | Unset = UNSET
        if not isinstance(self.template_settings, Unset):
            template_settings = self.template_settings

        loop = self.loop

        loopback_num = self.loopback_num

        block = self.block

        block_num = self.block_num

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        mlag_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_msg, Unset):
            mlag_msg = self.mlag_msg.to_dict()

        mlag_peer_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_peer_info, Unset):
            mlag_peer_info = self.mlag_peer_info.to_dict()

        sdm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sdm, Unset):
            sdm = self.sdm.to_dict()

        terminal_prefix = self.terminal_prefix

        support_health = self.support_health

        pmtud_enable = self.pmtud_enable

        support_auto_add_oui_based_vlan = self.support_auto_add_oui_based_vlan

        mtu_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mtu_list, Unset):
            mtu_list = []
            for mtu_list_item_data in self.mtu_list:
                mtu_list_item = mtu_list_item_data.to_dict()
                mtu_list.append(mtu_list_item)

        id = self.id

        site_id = self.site_id

        master_mac = self.master_mac

        master_active = self.master_active

        abnormal_reason = self.abnormal_reason

        inactive_units: list[int] | Unset = UNSET
        if not isinstance(self.inactive_units, Unset):
            inactive_units = self.inactive_units

        member: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = []
            for member_item_data in self.member:
                member_item = member_item_data.to_dict()
                member.append(member_item)

        stack_lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_lags, Unset):
            stack_lags = []
            for stack_lags_item_data in self.stack_lags:
                stack_lags_item = stack_lags_item_data.to_dict()
                stack_lags.append(stack_lags_item)

        locate_enable = self.locate_enable

        mac_delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac_delay, Unset):
            mac_delay = self.mac_delay.to_dict()

        virtual_mac = self.virtual_mac

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
        if device_misc is not UNSET:
            field_dict["deviceMisc"] = device_misc
        if dev_cap is not UNSET:
            field_dict["devCap"] = dev_cap
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if mvlan_network_id is not UNSET:
            field_dict["mvlanNetworkId"] = mvlan_network_id
        if mvlan_bridge_vlan is not UNSET:
            field_dict["mvlanBridgeVlan"] = mvlan_bridge_vlan
        if ip_setting is not UNSET:
            field_dict["ipSetting"] = ip_setting
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if stp is not UNSET:
            field_dict["stp"] = stp
        if priority is not UNSET:
            field_dict["priority"] = priority
        if hello_time is not UNSET:
            field_dict["helloTime"] = hello_time
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if forward_delay is not UNSET:
            field_dict["forwardDelay"] = forward_delay
        if tx_hold_count is not UNSET:
            field_dict["txHoldCount"] = tx_hold_count
        if max_hops is not UNSET:
            field_dict["maxHops"] = max_hops
        if mstp is not UNSET:
            field_dict["mstp"] = mstp
        if qos_config is not UNSET:
            field_dict["qosConfig"] = qos_config
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if multicast is not UNSET:
            field_dict["multicast"] = multicast
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lags is not UNSET:
            field_dict["lags"] = lags
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if ip is not UNSET:
            field_dict["ip"] = ip
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if need_upgrade is not UNSET:
            field_dict["needUpgrade"] = need_upgrade
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if uptime_long is not UNSET:
            field_dict["uptimeLong"] = uptime_long
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_uitl is not UNSET:
            field_dict["memUitl"] = mem_uitl
        if poe_total_power is not UNSET:
            field_dict["poeTotalPower"] = poe_total_power
        if poe_remain is not UNSET:
            field_dict["poeRemain"] = poe_remain
        if poe_remain_percent is not UNSET:
            field_dict["poeRemainPercent"] = poe_remain_percent
        if fan_status is not UNSET:
            field_dict["fanStatus"] = fan_status
        if uplink is not UNSET:
            field_dict["uplink"] = uplink
        if uplink_port is not UNSET:
            field_dict["uplinkPort"] = uplink_port
        if uplink_st_port is not UNSET:
            field_dict["uplinkStPort"] = uplink_st_port
        if downlink_list is not UNSET:
            field_dict["downlinkList"] = downlink_list
        if stp_link_list is not UNSET:
            field_dict["stpLinkList"] = stp_link_list
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if support_vlan_if is not UNSET:
            field_dict["supportVlanIf"] = support_vlan_if
        if jumbo is not UNSET:
            field_dict["jumbo"] = jumbo
        if jumbo_follow_site is not UNSET:
            field_dict["jumboFollowSite"] = jumbo_follow_site
        if lag_hash_alg is not UNSET:
            field_dict["lagHashAlg"] = lag_hash_alg
        if lag_hash_alg_follow_site is not UNSET:
            field_dict["lagHashAlgFollowSite"] = lag_hash_alg_follow_site
        if speeds is not UNSET:
            field_dict["speeds"] = speeds
        if support_ipv_6_acl is not UNSET:
            field_dict["supportIpv6Acl"] = support_ipv_6_acl
        if stack_device is not UNSET:
            field_dict["stackDevice"] = stack_device
        if support_vrf is not UNSET:
            field_dict["supportVrf"] = support_vrf
        if unit is not UNSET:
            field_dict["unit"] = unit
        if stack_ports is not UNSET:
            field_dict["stackPorts"] = stack_ports
        if stack_msg is not UNSET:
            field_dict["stackMsg"] = stack_msg
        if template_settings is not UNSET:
            field_dict["templateSettings"] = template_settings
        if loop is not UNSET:
            field_dict["loop"] = loop
        if loopback_num is not UNSET:
            field_dict["loopbackNum"] = loopback_num
        if block is not UNSET:
            field_dict["block"] = block
        if block_num is not UNSET:
            field_dict["blockNum"] = block_num
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if mlag_msg is not UNSET:
            field_dict["mlagMsg"] = mlag_msg
        if mlag_peer_info is not UNSET:
            field_dict["mlagPeerInfo"] = mlag_peer_info
        if sdm is not UNSET:
            field_dict["sdm"] = sdm
        if terminal_prefix is not UNSET:
            field_dict["terminalPrefix"] = terminal_prefix
        if support_health is not UNSET:
            field_dict["supportHealth"] = support_health
        if pmtud_enable is not UNSET:
            field_dict["pmtudEnable"] = pmtud_enable
        if support_auto_add_oui_based_vlan is not UNSET:
            field_dict["supportAutoAddOuiBasedVlan"] = support_auto_add_oui_based_vlan
        if mtu_list is not UNSET:
            field_dict["mtuList"] = mtu_list
        if id is not UNSET:
            field_dict["id"] = id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if master_active is not UNSET:
            field_dict["masterActive"] = master_active
        if abnormal_reason is not UNSET:
            field_dict["abnormalReason"] = abnormal_reason
        if inactive_units is not UNSET:
            field_dict["inactiveUnits"] = inactive_units
        if member is not UNSET:
            field_dict["member"] = member
        if stack_lags is not UNSET:
            field_dict["stackLags"] = stack_lags
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if mac_delay is not UNSET:
            field_dict["macDelay"] = mac_delay
        if virtual_mac is not UNSET:
            field_dict["virtualMac"] = virtual_mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )
        from ..models.device_replace_setting_vo import (
            DeviceReplaceSettingVO,
        )
        from ..models.ip_setting_vo import IpSettingVO
        from ..models.mac_delay_vo import MacDelayVO
        from ..models.mlag_msg_vo import MlagMsgVO
        from ..models.osw_dev_cap_vo import OswDevCapVO
        from ..models.osw_device_misc_vo import OswDeviceMiscVO
        from ..models.osw_downlink_vo import OswDownlinkVO
        from ..models.osw_lag_vo import OswLagVO
        from ..models.osw_lan_multicast_vo import OswLanMulticastVO
        from ..models.osw_mlag_peer_info_vo import OswMlagPeerInfoVO
        from ..models.osw_mtu_count_vo import OswMtuCountVO
        from ..models.osw_port_vo import OswPortVO
        from ..models.osw_qos_config_vo import OswQosConfigVO
        from ..models.osw_sdm_template_vo import OswSdmTemplateVO
        from ..models.osw_snmp_vo import OswSnmpVO
        from ..models.osw_stack_member_lag_vo import (
            OswStackMemberLagVO,
        )
        from ..models.osw_stack_member_vo import OswStackMemberVO
        from ..models.osw_stack_port_group_vo import (
            OswStackPortGroupVO,
        )
        from ..models.osw_stp_mstp_vo import OswStpMstpVO
        from ..models.osw_uplink_vo import OswUplinkVO
        from ..models.stack_msg_vo import StackMsgVO

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

        _device_misc = d.pop("deviceMisc", UNSET)
        device_misc: OswDeviceMiscVO | Unset
        if isinstance(_device_misc, Unset):
            device_misc = UNSET
        else:
            device_misc = OswDeviceMiscVO.from_dict(_device_misc)

        _dev_cap = d.pop("devCap", UNSET)
        dev_cap: OswDevCapVO | Unset
        if isinstance(_dev_cap, Unset):
            dev_cap = UNSET
        else:
            dev_cap = OswDevCapVO.from_dict(_dev_cap)

        led_setting = d.pop("ledSetting", UNSET)

        mvlan_network_id = d.pop("mvlanNetworkId", UNSET)

        mvlan_bridge_vlan = d.pop("mvlanBridgeVlan", UNSET)

        _ip_setting = d.pop("ipSetting", UNSET)
        ip_setting: IpSettingVO | Unset
        if isinstance(_ip_setting, Unset):
            ip_setting = UNSET
        else:
            ip_setting = IpSettingVO.from_dict(_ip_setting)

        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        stp = d.pop("stp", UNSET)

        priority = d.pop("priority", UNSET)

        hello_time = d.pop("helloTime", UNSET)

        max_age = d.pop("maxAge", UNSET)

        forward_delay = d.pop("forwardDelay", UNSET)

        tx_hold_count = d.pop("txHoldCount", UNSET)

        max_hops = d.pop("maxHops", UNSET)

        _mstp = d.pop("mstp", UNSET)
        mstp: OswStpMstpVO | Unset
        if isinstance(_mstp, Unset):
            mstp = UNSET
        else:
            mstp = OswStpMstpVO.from_dict(_mstp)

        _qos_config = d.pop("qosConfig", UNSET)
        qos_config: OswQosConfigVO | Unset
        if isinstance(_qos_config, Unset):
            qos_config = UNSET
        else:
            qos_config = OswQosConfigVO.from_dict(_qos_config)

        _snmp = d.pop("snmp", UNSET)
        snmp: OswSnmpVO | Unset
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = OswSnmpVO.from_dict(_snmp)

        _multicast = d.pop("multicast", UNSET)
        multicast: OswLanMulticastVO | Unset
        if isinstance(_multicast, Unset):
            multicast = UNSET
        else:
            multicast = OswLanMulticastVO.from_dict(_multicast)

        _ports = d.pop("ports", UNSET)
        ports: list[OswPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _lags = d.pop("lags", UNSET)
        lags: list[OswLagVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = OswLagVO.from_dict(lags_item_data)

                lags.append(lags_item)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        ip = d.pop("ip", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        last_seen = d.pop("lastSeen", UNSET)

        need_upgrade = d.pop("needUpgrade", UNSET)

        uptime = d.pop("uptime", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_uitl = d.pop("memUitl", UNSET)

        poe_total_power = d.pop("poeTotalPower", UNSET)

        poe_remain = d.pop("poeRemain", UNSET)

        poe_remain_percent = d.pop("poeRemainPercent", UNSET)

        fan_status = d.pop("fanStatus", UNSET)

        _uplink = d.pop("uplink", UNSET)
        uplink: OswUplinkVO | Unset
        if isinstance(_uplink, Unset):
            uplink = UNSET
        else:
            uplink = OswUplinkVO.from_dict(_uplink)

        uplink_port = d.pop("uplinkPort", UNSET)

        uplink_st_port = d.pop("uplinkStPort", UNSET)

        _downlink_list = d.pop("downlinkList", UNSET)
        downlink_list: list[OswDownlinkVO] | Unset = UNSET
        if _downlink_list is not UNSET:
            downlink_list = []
            for downlink_list_item_data in _downlink_list:
                downlink_list_item = OswDownlinkVO.from_dict(downlink_list_item_data)

                downlink_list.append(downlink_list_item)

        _stp_link_list = d.pop("stpLinkList", UNSET)
        stp_link_list: list[OswDownlinkVO] | Unset = UNSET
        if _stp_link_list is not UNSET:
            stp_link_list = []
            for stp_link_list_item_data in _stp_link_list:
                stp_link_list_item = OswDownlinkVO.from_dict(stp_link_list_item_data)

                stp_link_list.append(stp_link_list_item)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        support_vlan_if = d.pop("supportVlanIf", UNSET)

        jumbo = d.pop("jumbo", UNSET)

        jumbo_follow_site = d.pop("jumboFollowSite", UNSET)

        lag_hash_alg = d.pop("lagHashAlg", UNSET)

        lag_hash_alg_follow_site = d.pop("lagHashAlgFollowSite", UNSET)

        speeds = cast(list[int], d.pop("speeds", UNSET))

        support_ipv_6_acl = d.pop("supportIpv6Acl", UNSET)

        stack_device = d.pop("stackDevice", UNSET)

        support_vrf = d.pop("supportVrf", UNSET)

        unit = d.pop("unit", UNSET)

        _stack_ports = d.pop("stackPorts", UNSET)
        stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
        if _stack_ports is not UNSET:
            stack_ports = []
            for stack_ports_item_data in _stack_ports:
                stack_ports_item = OswStackPortGroupVO.from_dict(stack_ports_item_data)

                stack_ports.append(stack_ports_item)

        _stack_msg = d.pop("stackMsg", UNSET)
        stack_msg: StackMsgVO | Unset
        if isinstance(_stack_msg, Unset):
            stack_msg = UNSET
        else:
            stack_msg = StackMsgVO.from_dict(_stack_msg)

        template_settings = cast(list[int], d.pop("templateSettings", UNSET))

        loop = d.pop("loop", UNSET)

        loopback_num = d.pop("loopbackNum", UNSET)

        block = d.pop("block", UNSET)

        block_num = d.pop("blockNum", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        _mlag_msg = d.pop("mlagMsg", UNSET)
        mlag_msg: MlagMsgVO | Unset
        if isinstance(_mlag_msg, Unset):
            mlag_msg = UNSET
        else:
            mlag_msg = MlagMsgVO.from_dict(_mlag_msg)

        _mlag_peer_info = d.pop("mlagPeerInfo", UNSET)
        mlag_peer_info: OswMlagPeerInfoVO | Unset
        if isinstance(_mlag_peer_info, Unset):
            mlag_peer_info = UNSET
        else:
            mlag_peer_info = OswMlagPeerInfoVO.from_dict(_mlag_peer_info)

        _sdm = d.pop("sdm", UNSET)
        sdm: OswSdmTemplateVO | Unset
        if isinstance(_sdm, Unset):
            sdm = UNSET
        else:
            sdm = OswSdmTemplateVO.from_dict(_sdm)

        terminal_prefix = d.pop("terminalPrefix", UNSET)

        support_health = d.pop("supportHealth", UNSET)

        pmtud_enable = d.pop("pmtudEnable", UNSET)

        support_auto_add_oui_based_vlan = d.pop("supportAutoAddOuiBasedVlan", UNSET)

        _mtu_list = d.pop("mtuList", UNSET)
        mtu_list: list[OswMtuCountVO] | Unset = UNSET
        if _mtu_list is not UNSET:
            mtu_list = []
            for mtu_list_item_data in _mtu_list:
                mtu_list_item = OswMtuCountVO.from_dict(mtu_list_item_data)

                mtu_list.append(mtu_list_item)

        id = d.pop("id", UNSET)

        site_id = d.pop("siteId", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        master_active = d.pop("masterActive", UNSET)

        abnormal_reason = d.pop("abnormalReason", UNSET)

        inactive_units = cast(list[int], d.pop("inactiveUnits", UNSET))

        _member = d.pop("member", UNSET)
        member: list[OswStackMemberVO] | Unset = UNSET
        if _member is not UNSET:
            member = []
            for member_item_data in _member:
                member_item = OswStackMemberVO.from_dict(member_item_data)

                member.append(member_item)

        _stack_lags = d.pop("stackLags", UNSET)
        stack_lags: list[OswStackMemberLagVO] | Unset = UNSET
        if _stack_lags is not UNSET:
            stack_lags = []
            for stack_lags_item_data in _stack_lags:
                stack_lags_item = OswStackMemberLagVO.from_dict(stack_lags_item_data)

                stack_lags.append(stack_lags_item)

        locate_enable = d.pop("locateEnable", UNSET)

        _mac_delay = d.pop("macDelay", UNSET)
        mac_delay: MacDelayVO | Unset
        if isinstance(_mac_delay, Unset):
            mac_delay = UNSET
        else:
            mac_delay = MacDelayVO.from_dict(_mac_delay)

        virtual_mac = d.pop("virtualMac", UNSET)

        osw_stack_detail_vo = cls(
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
            device_misc=device_misc,
            dev_cap=dev_cap,
            led_setting=led_setting,
            mvlan_network_id=mvlan_network_id,
            mvlan_bridge_vlan=mvlan_bridge_vlan,
            ip_setting=ip_setting,
            loopback_detect_enable=loopback_detect_enable,
            stp=stp,
            priority=priority,
            hello_time=hello_time,
            max_age=max_age,
            forward_delay=forward_delay,
            tx_hold_count=tx_hold_count,
            max_hops=max_hops,
            mstp=mstp,
            qos_config=qos_config,
            snmp=snmp,
            multicast=multicast,
            ports=ports,
            lags=lags,
            tag_ids=tag_ids,
            ip=ip,
            public_ip=public_ip,
            ipv_6_list=ipv_6_list,
            last_seen=last_seen,
            need_upgrade=need_upgrade,
            uptime=uptime,
            uptime_long=uptime_long,
            cpu_util=cpu_util,
            mem_uitl=mem_uitl,
            poe_total_power=poe_total_power,
            poe_remain=poe_remain,
            poe_remain_percent=poe_remain_percent,
            fan_status=fan_status,
            uplink=uplink,
            uplink_port=uplink_port,
            uplink_st_port=uplink_st_port,
            downlink_list=downlink_list,
            stp_link_list=stp_link_list,
            download=download,
            upload=upload,
            support_vlan_if=support_vlan_if,
            jumbo=jumbo,
            jumbo_follow_site=jumbo_follow_site,
            lag_hash_alg=lag_hash_alg,
            lag_hash_alg_follow_site=lag_hash_alg_follow_site,
            speeds=speeds,
            support_ipv_6_acl=support_ipv_6_acl,
            stack_device=stack_device,
            support_vrf=support_vrf,
            unit=unit,
            stack_ports=stack_ports,
            stack_msg=stack_msg,
            template_settings=template_settings,
            loop=loop,
            loopback_num=loopback_num,
            block=block,
            block_num=block_num,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            mlag_msg=mlag_msg,
            mlag_peer_info=mlag_peer_info,
            sdm=sdm,
            terminal_prefix=terminal_prefix,
            support_health=support_health,
            pmtud_enable=pmtud_enable,
            support_auto_add_oui_based_vlan=support_auto_add_oui_based_vlan,
            mtu_list=mtu_list,
            id=id,
            site_id=site_id,
            master_mac=master_mac,
            master_active=master_active,
            abnormal_reason=abnormal_reason,
            inactive_units=inactive_units,
            member=member,
            stack_lags=stack_lags,
            locate_enable=locate_enable,
            mac_delay=mac_delay,
            virtual_mac=virtual_mac,
        )

        osw_stack_detail_vo.additional_properties = d
        return osw_stack_detail_vo

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
