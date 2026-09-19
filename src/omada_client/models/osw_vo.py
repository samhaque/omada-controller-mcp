from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_feature_limit_vo import ApFeatureLimitVO
    from ..models.device_replace_setting_vo import DeviceReplaceSettingVO
    from ..models.lag_cap_vo import LagCapVO
    from ..models.location_vo import LocationVO
    from ..models.mlag_msg_vo import MlagMsgVO
    from ..models.osw_sdm_template_vo import OswSdmTemplateVO
    from ..models.osw_stack_member_port_vo import OswStackMemberPortVO
    from ..models.osw_stack_port_cap_vo import OswStackPortCapVO
    from ..models.osw_stack_port_group_vo import OswStackPortGroupVO
    from ..models.osw_stand_port_vo import OswStandPortVO
    from ..models.osw_vo_profiles import OswVOProfiles
    from ..models.osw_vo_stack_port_cap import OswVOStackPortCap
    from ..models.stack_msg_vo import StackMsgVO


T = TypeVar("T", bound="OswVO")


@_attrs_define
class OswVO:
    """Detected Switches

    Attributes:
        custom_id (str | Unset): Customer ID
        custom_name (str | Unset): Customer name displayed in MSP mode
        site_name (str | Unset): Site name
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        sub_dev_type (int | Unset): Device subtype, indicating a special device type for wireless routers. This field is
            not present for ordinary devices, where 1 represents a wireless router.
        mac (str | Unset): Mac address
        name (str | Unset): Default uses the MAC address as the name.
        model (str | Unset): Model, such as EAP225.
        compound_model (str | Unset): Model complex used in the backend.Ap：model+(country)+modelVersion,  EAP225(EU)
            v3.0 Ap: specialModel+modelVersion, EAP225-Outdoor-1a20a950b8d950e8 v1.0  Gateway/Switch：model+modelVersion, Osg
            v3.0
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        model_version (str | Unset): Model version of device,for example:3.0
        firmware_version (str | Unset): Version of firmware,for example:2.5.0 Build 20190118 Rel. 64821
        version (str | Unset): Software version, such as "2.5.0," extracted from DeviceDO.firmwareVersion - "2.5.0 Build
            20190118 Rel. 64821."
        hw_version (str | Unset): Version of hardware,for example 1.0
        special_model (str | Unset): Special device model,for example:EAP225-Outdoor-1a20a950b8d950e8
        ip (str | Unset): Ip address,such as 192.168.0.105
        public_ip (str | Unset): Public ip address
        ipv_6_list (list[str] | Unset): Ipv6 address List
        uptime (str | Unset): Device uptime
        uptime_long (int | Unset): Runtime duration, in seconds (s).
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        adopt_fail_type (int | Unset): Adopt fail reason should be a value as follows: -1:adopt timeout;-2:user/password
            error
        last_seen (int | Unset): Last active time.
        need_upgrade (bool | Unset): Whether the device needs upgrade
        latest_version (str | Unset): Latest firmware version
        fw_download (bool | Unset): Whether the device is downloading firmware
        cpu_util (int | Unset): Cpu utilization
        mem_util (int | Unset): Memory utilization
        download (int | Unset): Real-time total downstream traffic (bytes).
        upload (int | Unset): Real-time total upstream traffic (bytes).
        site (str | Unset): "Site of the device"
        location (LocationVO | Unset): Device location information on the map; null indicates unplaced.
        client_num (int | Unset): Number of clients.
        compatible (int | Unset): Device firmware and controller compatibility type.Compatible should be a value as
            follows: 0:COMPATIBLE;1:HIGH_MAJOR_VER;2:LOW_MAJOR_VER;3:HIGH_MINOR_VER;4:LOW_MINOR_VER;7:HIGH_COMPONENT_VER;10:
            DEVICE_NOT_COMPATIBLE;11:HIGH_ADOPT_COMMPONENT;12:DEVICE_CATEGORY_NOT_COMPATIBLE;14:DEVICE_NOT_COMPATIBLE_IN_CLU
            STER
        locate_enable (bool | Unset): Whether locate function is enabled
        active (bool | Unset): Mark whether the device is activated: When license (specific to cloud base) is false, the
            status column shows the pre-bound status. When it is true or null, the status column displays as it originally
            did.
        license_status (int | Unset): License status should be a value as follows:0: unActive 1: Unbind 2: Expired 3:
            active If there is a value and it is not 3, display the Active button. license (specific to cloud base).
        due_time (int | Unset): Expire timestamp of license(cloud base exclusive)
        due_time_left (int | Unset): Milliseconds from the current moment to the expiration time(cloud base exclusive)
        license_unbinding_limit (int | Unset): Remaining unbind count for license on detail Page of device(cloud base
            exclusive)
        in_whitelist (bool | Unset): Whether the device is in white list
        sn (str | Unset): SN code of device
        eost (int | Unset): End of service time of device(CBC exclusive)
        eos (int | Unset): End of support time of device(CBC exclusive)
        combined_gateway (bool | Unset): Is it an combined gateway?
        es (bool | Unset): Whether it is Agile Series Switch
        ippt (bool | Unset): Whether it is LTE Backup
        ippt_preconfig (bool | Unset):
        support_ippt (bool | Unset):
        support_anomaly (bool | Unset): Whether the device firmware support intelligent anomaly detection
        health_score (int | Unset): 1~3: poor; 4~7: fair; 0: no data; 8~10 good.
        health_score_time (int | Unset): The time of healthScore
        tag_name (str | Unset): Device tag name
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
        category (str | Unset): Category of license.When activating in bulk for the pro site, the front end can only
            select the same type for bulk activation.
        pre_config_error_code (int | Unset): When the pre-added devices cannot properly pass through, an error will be
            returned.
        pre_config_retry_type (int | Unset): When retrying the path through, if there is a value, the front end will
            display a retry button. The types are: 1:Requires password input.2: No password input needed.
        power_mode (int | Unset): AP power mode.The power supply types are as follows: 0: DC power supply 1: 802.3bt
            power supply 2: 802.3at power supply 3: 802.3af power supply 4: Switch power supply (display restart)
        power_mode_list (list[int] | Unset): Indicating the power supply modes for AP devices across frequency bands,
            with array indices corresponding to the frequency bands: 0: 2.4G 1: 5G/5G1 2: 5G2 3: 6G. The corresponding
            values for power supply modes are: 0: Normal operation 1: Power limited 2: Frequency band disabled
        feature_limit (ApFeatureLimitVO | Unset): Functions that need to be restricted under the current power supply
            mode.
        wireless_router (bool | Unset): Indicates whether it is a wireless router; it is true only when this device is a
            wireless router.
        description (str | Unset):
        online_upgrade_status (int | Unset): Device online upgrade status should be a value as follows:
            0:IDLE,1:DOWNLOADING,2:UPGRADING
        device_series_type (int | Unset): Device type should be a value as follows:0:advanced,1:pro
        config_sync_status (int | Unset): Device configuration synchronization status , including: 0: noConfig (No
            configuration) 1: success (Success) 2: fail (Failure) 3: info (Information) 4: configuring (Configuring) 5:
            preConfig (Pre-configuration)
        support_running_config (bool | Unset): Whether the device supports show running config.
        resource (int | Unset): Data source.Resource should be a value as follows: 0:new created;1:from
            template;2:override
        address (str | Unset): Address
        uplink_device_mac (str | Unset): Uplink device mac
        uplink_device_name (str | Unset): Uplink device mac name
        uplink_device_port (str | Unset): Uplink device port
        link_speed (int | Unset): Link speed
        duplex (int | Unset): Duplex should be a value as follows:0:Auto,1:Half, 2:Full
        switch_consistent (bool | Unset): Whether the device can be adopted by the site.
        ecsp_first_version (int | Unset): Ecsp first version
        package_capture_status (int | Unset):
        replace_device_info (DeviceReplaceSettingVO | Unset):
        incidents (int | Unset): incident number
        loopback_num (int | Unset): Number of loops
        loop (str | Unset): Set of loop port
        block_num (int | Unset): Block Num
        block (str | Unset): Block information
        poe_total_power (float | Unset): PoE Total Power (W)
        poe_remain (float | Unset): PoE remaining power
        fan_status (int | Unset): FanStatus should be a value as follows: 0: normal; 1: fault; 2: no fan
        poe_support (bool | Unset): Indicates whether the switch supports PoE
        profiles (OswVOProfiles | Unset): profiles
        stack_support_ports (list[OswStandPortVO] | Unset): Stack support ports
        stack_port_cap (OswVOStackPortCap | Unset):
        max_stack_groups (int | Unset): The maximum number of stacking port aggregation groups that can be configured
        max_stack_unit_number (int | Unset): The maximum unit number supported by the device
        support_stack_group_speed (bool | Unset): Indicates whether the member device supports configuring the link
            speed of the stack port aggregation group
        stack_port_config_caps (list[OswStackPortCapVO] | Unset): Ports capability that support configuration as stack
            port
        default_group_speed_cap (list[int] | Unset): Stack port aggregation group default link speed capability
        ports (list[OswStackMemberPortVO] | Unset): Ports
        stack_ports (list[OswStackPortGroupVO] | Unset): Stack ports
        unit (int | Unset): Unit
        priority (int | Unset): Stack member priority
        stack_msg (StackMsgVO | Unset): Stack Message
        mlag_msg (MlagMsgVO | Unset): M-LAG Message
        stkable_group_id (int | Unset): The stack support list number where the switch is located, used to determine
            whether two devices can be stacked
        stk_ver (str | Unset): The stacking component version number used by the switch is used to determine whether two
            devices can be stacked
        support_power_alert (bool | Unset): Indicates whether the switch supports power alert
        support_stp (bool | Unset): Indicates whether the switch supports stp
        support_extend_stp (bool | Unset): Indicates whether the switch supports mstp
        mstp_ins_num (int | Unset): The number of MSTP instances
        mstp_ins_no (int | Unset): The range of MSTP instanceId
        rpvst_extend_support (bool | Unset): Indicates whether the switch supports rpvst
        mstp_port_support (bool | Unset): Indicates whether the switch supports MSTP Port
        mstp_get_active_support (bool | Unset): Indicates whether the switch supports MSTP Get Active
        rpvst_ins_num (int | Unset): The number of RPVST instances
        support_cable_test (bool | Unset): Indicates whether the switch supports cable test
        support_domain_ping (bool | Unset): Indicates whether the switch supports pinging domain
        support_domain_trace_route (bool | Unset): Indicates whether the switch supports tracerouting domain
        support_custom_dhcp_option (bool | Unset): Whether the device supports custom dhcp option. Only valid when type
            is switch.
        support_mac_delay (bool | Unset):
        support_dhcp_range (bool | Unset): Indicates whether the switch supports DHCP Range Pool
        support_sdm (bool | Unset): Indicates whether the switch supports SDM template
        support_dhcp_reservation (bool | Unset): Indicates whether the switch supports DHCP Reservation
        support_relay_multi_server (bool | Unset): Whether the device supports DHCP relay multi Server
        support_tpcl_res_info (bool | Unset): Whether the device supports returning TPCL resource information
        max_relay_server_num (int | Unset): Max DHCP relay server num
        sdm (OswSdmTemplateVO | Unset): Sdm template
        locating_ports (list[int] | Unset): Locating switch ports, effective when parameter[locateEnable] is true and
            device is not a member of stack
        locating_standard_ports (list[str] | Unset): Locating switch standard ports, effective when
            parameter[locateEnable] is true and device is a member of stack
        support_get_ospf_neighbor_table (bool | Unset):
        support_vrf (bool | Unset): Indicates whether the switch supports Vrf
        support_snmp (bool | Unset): Indicates whether the switch supports SNMP
        support_jumbo (bool | Unset): Indicates whether the switch supports Jumbo
        lag_cap (LagCapVO | Unset): Capability of lag
        license_status_str (str | Unset):
    """

    custom_id: str | Unset = UNSET
    custom_name: str | Unset = UNSET
    site_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    sub_dev_type: int | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    compound_model: str | Unset = UNSET
    show_model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    version: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    special_model: str | Unset = UNSET
    ip: str | Unset = UNSET
    public_ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    uptime: str | Unset = UNSET
    uptime_long: int | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    adopt_fail_type: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    need_upgrade: bool | Unset = UNSET
    latest_version: str | Unset = UNSET
    fw_download: bool | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_util: int | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    site: str | Unset = UNSET
    location: LocationVO | Unset = UNSET
    client_num: int | Unset = UNSET
    compatible: int | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    active: bool | Unset = UNSET
    license_status: int | Unset = UNSET
    due_time: int | Unset = UNSET
    due_time_left: int | Unset = UNSET
    license_unbinding_limit: int | Unset = UNSET
    in_whitelist: bool | Unset = UNSET
    sn: str | Unset = UNSET
    eost: int | Unset = UNSET
    eos: int | Unset = UNSET
    combined_gateway: bool | Unset = UNSET
    es: bool | Unset = UNSET
    ippt: bool | Unset = UNSET
    ippt_preconfig: bool | Unset = UNSET
    support_ippt: bool | Unset = UNSET
    support_anomaly: bool | Unset = UNSET
    health_score: int | Unset = UNSET
    health_score_time: int | Unset = UNSET
    tag_name: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    category: str | Unset = UNSET
    pre_config_error_code: int | Unset = UNSET
    pre_config_retry_type: int | Unset = UNSET
    power_mode: int | Unset = UNSET
    power_mode_list: list[int] | Unset = UNSET
    feature_limit: ApFeatureLimitVO | Unset = UNSET
    wireless_router: bool | Unset = UNSET
    description: str | Unset = UNSET
    online_upgrade_status: int | Unset = UNSET
    device_series_type: int | Unset = UNSET
    config_sync_status: int | Unset = UNSET
    support_running_config: bool | Unset = UNSET
    resource: int | Unset = UNSET
    address: str | Unset = UNSET
    uplink_device_mac: str | Unset = UNSET
    uplink_device_name: str | Unset = UNSET
    uplink_device_port: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    switch_consistent: bool | Unset = UNSET
    ecsp_first_version: int | Unset = UNSET
    package_capture_status: int | Unset = UNSET
    replace_device_info: DeviceReplaceSettingVO | Unset = UNSET
    incidents: int | Unset = UNSET
    loopback_num: int | Unset = UNSET
    loop: str | Unset = UNSET
    block_num: int | Unset = UNSET
    block: str | Unset = UNSET
    poe_total_power: float | Unset = UNSET
    poe_remain: float | Unset = UNSET
    fan_status: int | Unset = UNSET
    poe_support: bool | Unset = UNSET
    profiles: OswVOProfiles | Unset = UNSET
    stack_support_ports: list[OswStandPortVO] | Unset = UNSET
    stack_port_cap: OswVOStackPortCap | Unset = UNSET
    max_stack_groups: int | Unset = UNSET
    max_stack_unit_number: int | Unset = UNSET
    support_stack_group_speed: bool | Unset = UNSET
    stack_port_config_caps: list[OswStackPortCapVO] | Unset = UNSET
    default_group_speed_cap: list[int] | Unset = UNSET
    ports: list[OswStackMemberPortVO] | Unset = UNSET
    stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
    unit: int | Unset = UNSET
    priority: int | Unset = UNSET
    stack_msg: StackMsgVO | Unset = UNSET
    mlag_msg: MlagMsgVO | Unset = UNSET
    stkable_group_id: int | Unset = UNSET
    stk_ver: str | Unset = UNSET
    support_power_alert: bool | Unset = UNSET
    support_stp: bool | Unset = UNSET
    support_extend_stp: bool | Unset = UNSET
    mstp_ins_num: int | Unset = UNSET
    mstp_ins_no: int | Unset = UNSET
    rpvst_extend_support: bool | Unset = UNSET
    mstp_port_support: bool | Unset = UNSET
    mstp_get_active_support: bool | Unset = UNSET
    rpvst_ins_num: int | Unset = UNSET
    support_cable_test: bool | Unset = UNSET
    support_domain_ping: bool | Unset = UNSET
    support_domain_trace_route: bool | Unset = UNSET
    support_custom_dhcp_option: bool | Unset = UNSET
    support_mac_delay: bool | Unset = UNSET
    support_dhcp_range: bool | Unset = UNSET
    support_sdm: bool | Unset = UNSET
    support_dhcp_reservation: bool | Unset = UNSET
    support_relay_multi_server: bool | Unset = UNSET
    support_tpcl_res_info: bool | Unset = UNSET
    max_relay_server_num: int | Unset = UNSET
    sdm: OswSdmTemplateVO | Unset = UNSET
    locating_ports: list[int] | Unset = UNSET
    locating_standard_ports: list[str] | Unset = UNSET
    support_get_ospf_neighbor_table: bool | Unset = UNSET
    support_vrf: bool | Unset = UNSET
    support_snmp: bool | Unset = UNSET
    support_jumbo: bool | Unset = UNSET
    lag_cap: LagCapVO | Unset = UNSET
    license_status_str: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_id = self.custom_id

        custom_name = self.custom_name

        site_name = self.site_name

        type_ = self.type_

        sub_dev_type = self.sub_dev_type

        mac = self.mac

        name = self.name

        model = self.model

        compound_model = self.compound_model

        show_model = self.show_model

        model_version = self.model_version

        firmware_version = self.firmware_version

        version = self.version

        hw_version = self.hw_version

        special_model = self.special_model

        ip = self.ip

        public_ip = self.public_ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        uptime = self.uptime

        uptime_long = self.uptime_long

        status_category = self.status_category

        status = self.status

        adopt_fail_type = self.adopt_fail_type

        last_seen = self.last_seen

        need_upgrade = self.need_upgrade

        latest_version = self.latest_version

        fw_download = self.fw_download

        cpu_util = self.cpu_util

        mem_util = self.mem_util

        download = self.download

        upload = self.upload

        site = self.site

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        client_num = self.client_num

        compatible = self.compatible

        locate_enable = self.locate_enable

        active = self.active

        license_status = self.license_status

        due_time = self.due_time

        due_time_left = self.due_time_left

        license_unbinding_limit = self.license_unbinding_limit

        in_whitelist = self.in_whitelist

        sn = self.sn

        eost = self.eost

        eos = self.eos

        combined_gateway = self.combined_gateway

        es = self.es

        ippt = self.ippt

        ippt_preconfig = self.ippt_preconfig

        support_ippt = self.support_ippt

        support_anomaly = self.support_anomaly

        health_score = self.health_score

        health_score_time = self.health_score_time

        tag_name = self.tag_name

        added_in_advanced = self.added_in_advanced

        category = self.category

        pre_config_error_code = self.pre_config_error_code

        pre_config_retry_type = self.pre_config_retry_type

        power_mode = self.power_mode

        power_mode_list: list[int] | Unset = UNSET
        if not isinstance(self.power_mode_list, Unset):
            power_mode_list = self.power_mode_list

        feature_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_limit, Unset):
            feature_limit = self.feature_limit.to_dict()

        wireless_router = self.wireless_router

        description = self.description

        online_upgrade_status = self.online_upgrade_status

        device_series_type = self.device_series_type

        config_sync_status = self.config_sync_status

        support_running_config = self.support_running_config

        resource = self.resource

        address = self.address

        uplink_device_mac = self.uplink_device_mac

        uplink_device_name = self.uplink_device_name

        uplink_device_port = self.uplink_device_port

        link_speed = self.link_speed

        duplex = self.duplex

        switch_consistent = self.switch_consistent

        ecsp_first_version = self.ecsp_first_version

        package_capture_status = self.package_capture_status

        replace_device_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replace_device_info, Unset):
            replace_device_info = self.replace_device_info.to_dict()

        incidents = self.incidents

        loopback_num = self.loopback_num

        loop = self.loop

        block_num = self.block_num

        block = self.block

        poe_total_power = self.poe_total_power

        poe_remain = self.poe_remain

        fan_status = self.fan_status

        poe_support = self.poe_support

        profiles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = self.profiles.to_dict()

        stack_support_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_support_ports, Unset):
            stack_support_ports = []
            for stack_support_ports_item_data in self.stack_support_ports:
                stack_support_ports_item = stack_support_ports_item_data.to_dict()
                stack_support_ports.append(stack_support_ports_item)

        stack_port_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_port_cap, Unset):
            stack_port_cap = self.stack_port_cap.to_dict()

        max_stack_groups = self.max_stack_groups

        max_stack_unit_number = self.max_stack_unit_number

        support_stack_group_speed = self.support_stack_group_speed

        stack_port_config_caps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_port_config_caps, Unset):
            stack_port_config_caps = []
            for stack_port_config_caps_item_data in self.stack_port_config_caps:
                stack_port_config_caps_item = stack_port_config_caps_item_data.to_dict()
                stack_port_config_caps.append(stack_port_config_caps_item)

        default_group_speed_cap: list[int] | Unset = UNSET
        if not isinstance(self.default_group_speed_cap, Unset):
            default_group_speed_cap = self.default_group_speed_cap

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        stack_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_ports, Unset):
            stack_ports = []
            for stack_ports_item_data in self.stack_ports:
                stack_ports_item = stack_ports_item_data.to_dict()
                stack_ports.append(stack_ports_item)

        unit = self.unit

        priority = self.priority

        stack_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_msg, Unset):
            stack_msg = self.stack_msg.to_dict()

        mlag_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_msg, Unset):
            mlag_msg = self.mlag_msg.to_dict()

        stkable_group_id = self.stkable_group_id

        stk_ver = self.stk_ver

        support_power_alert = self.support_power_alert

        support_stp = self.support_stp

        support_extend_stp = self.support_extend_stp

        mstp_ins_num = self.mstp_ins_num

        mstp_ins_no = self.mstp_ins_no

        rpvst_extend_support = self.rpvst_extend_support

        mstp_port_support = self.mstp_port_support

        mstp_get_active_support = self.mstp_get_active_support

        rpvst_ins_num = self.rpvst_ins_num

        support_cable_test = self.support_cable_test

        support_domain_ping = self.support_domain_ping

        support_domain_trace_route = self.support_domain_trace_route

        support_custom_dhcp_option = self.support_custom_dhcp_option

        support_mac_delay = self.support_mac_delay

        support_dhcp_range = self.support_dhcp_range

        support_sdm = self.support_sdm

        support_dhcp_reservation = self.support_dhcp_reservation

        support_relay_multi_server = self.support_relay_multi_server

        support_tpcl_res_info = self.support_tpcl_res_info

        max_relay_server_num = self.max_relay_server_num

        sdm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sdm, Unset):
            sdm = self.sdm.to_dict()

        locating_ports: list[int] | Unset = UNSET
        if not isinstance(self.locating_ports, Unset):
            locating_ports = self.locating_ports

        locating_standard_ports: list[str] | Unset = UNSET
        if not isinstance(self.locating_standard_ports, Unset):
            locating_standard_ports = self.locating_standard_ports

        support_get_ospf_neighbor_table = self.support_get_ospf_neighbor_table

        support_vrf = self.support_vrf

        support_snmp = self.support_snmp

        support_jumbo = self.support_jumbo

        lag_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_cap, Unset):
            lag_cap = self.lag_cap.to_dict()

        license_status_str = self.license_status_str

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if custom_name is not UNSET:
            field_dict["customName"] = custom_name
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sub_dev_type is not UNSET:
            field_dict["subDevType"] = sub_dev_type
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if compound_model is not UNSET:
            field_dict["compoundModel"] = compound_model
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if version is not UNSET:
            field_dict["version"] = version
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
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
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if adopt_fail_type is not UNSET:
            field_dict["adoptFailType"] = adopt_fail_type
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if need_upgrade is not UNSET:
            field_dict["needUpgrade"] = need_upgrade
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if fw_download is not UNSET:
            field_dict["fwDownload"] = fw_download
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if site is not UNSET:
            field_dict["site"] = site
        if location is not UNSET:
            field_dict["location"] = location
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if active is not UNSET:
            field_dict["active"] = active
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if due_time is not UNSET:
            field_dict["dueTime"] = due_time
        if due_time_left is not UNSET:
            field_dict["dueTimeLeft"] = due_time_left
        if license_unbinding_limit is not UNSET:
            field_dict["licenseUnbindingLimit"] = license_unbinding_limit
        if in_whitelist is not UNSET:
            field_dict["inWhitelist"] = in_whitelist
        if sn is not UNSET:
            field_dict["sn"] = sn
        if eost is not UNSET:
            field_dict["eost"] = eost
        if eos is not UNSET:
            field_dict["eos"] = eos
        if combined_gateway is not UNSET:
            field_dict["combinedGateway"] = combined_gateway
        if es is not UNSET:
            field_dict["es"] = es
        if ippt is not UNSET:
            field_dict["ippt"] = ippt
        if ippt_preconfig is not UNSET:
            field_dict["ipptPreconfig"] = ippt_preconfig
        if support_ippt is not UNSET:
            field_dict["supportIppt"] = support_ippt
        if support_anomaly is not UNSET:
            field_dict["supportAnomaly"] = support_anomaly
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if health_score_time is not UNSET:
            field_dict["healthScoreTime"] = health_score_time
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if category is not UNSET:
            field_dict["category"] = category
        if pre_config_error_code is not UNSET:
            field_dict["preConfigErrorCode"] = pre_config_error_code
        if pre_config_retry_type is not UNSET:
            field_dict["preConfigRetryType"] = pre_config_retry_type
        if power_mode is not UNSET:
            field_dict["powerMode"] = power_mode
        if power_mode_list is not UNSET:
            field_dict["powerModeList"] = power_mode_list
        if feature_limit is not UNSET:
            field_dict["featureLimit"] = feature_limit
        if wireless_router is not UNSET:
            field_dict["wirelessRouter"] = wireless_router
        if description is not UNSET:
            field_dict["description"] = description
        if online_upgrade_status is not UNSET:
            field_dict["onlineUpgradeStatus"] = online_upgrade_status
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if config_sync_status is not UNSET:
            field_dict["configSyncStatus"] = config_sync_status
        if support_running_config is not UNSET:
            field_dict["supportRunningConfig"] = support_running_config
        if resource is not UNSET:
            field_dict["resource"] = resource
        if address is not UNSET:
            field_dict["address"] = address
        if uplink_device_mac is not UNSET:
            field_dict["uplinkDeviceMac"] = uplink_device_mac
        if uplink_device_name is not UNSET:
            field_dict["uplinkDeviceName"] = uplink_device_name
        if uplink_device_port is not UNSET:
            field_dict["uplinkDevicePort"] = uplink_device_port
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if switch_consistent is not UNSET:
            field_dict["switchConsistent"] = switch_consistent
        if ecsp_first_version is not UNSET:
            field_dict["ecspFirstVersion"] = ecsp_first_version
        if package_capture_status is not UNSET:
            field_dict["packageCaptureStatus"] = package_capture_status
        if replace_device_info is not UNSET:
            field_dict["replaceDeviceInfo"] = replace_device_info
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if loopback_num is not UNSET:
            field_dict["loopbackNum"] = loopback_num
        if loop is not UNSET:
            field_dict["loop"] = loop
        if block_num is not UNSET:
            field_dict["blockNum"] = block_num
        if block is not UNSET:
            field_dict["block"] = block
        if poe_total_power is not UNSET:
            field_dict["poeTotalPower"] = poe_total_power
        if poe_remain is not UNSET:
            field_dict["poeRemain"] = poe_remain
        if fan_status is not UNSET:
            field_dict["fanStatus"] = fan_status
        if poe_support is not UNSET:
            field_dict["poeSupport"] = poe_support
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if stack_support_ports is not UNSET:
            field_dict["stackSupportPorts"] = stack_support_ports
        if stack_port_cap is not UNSET:
            field_dict["stackPortCap"] = stack_port_cap
        if max_stack_groups is not UNSET:
            field_dict["maxStackGroups"] = max_stack_groups
        if max_stack_unit_number is not UNSET:
            field_dict["maxStackUnitNumber"] = max_stack_unit_number
        if support_stack_group_speed is not UNSET:
            field_dict["supportStackGroupSpeed"] = support_stack_group_speed
        if stack_port_config_caps is not UNSET:
            field_dict["stackPortConfigCaps"] = stack_port_config_caps
        if default_group_speed_cap is not UNSET:
            field_dict["defaultGroupSpeedCap"] = default_group_speed_cap
        if ports is not UNSET:
            field_dict["ports"] = ports
        if stack_ports is not UNSET:
            field_dict["stackPorts"] = stack_ports
        if unit is not UNSET:
            field_dict["unit"] = unit
        if priority is not UNSET:
            field_dict["priority"] = priority
        if stack_msg is not UNSET:
            field_dict["stackMsg"] = stack_msg
        if mlag_msg is not UNSET:
            field_dict["mlagMsg"] = mlag_msg
        if stkable_group_id is not UNSET:
            field_dict["stkableGroupId"] = stkable_group_id
        if stk_ver is not UNSET:
            field_dict["stkVer"] = stk_ver
        if support_power_alert is not UNSET:
            field_dict["supportPowerAlert"] = support_power_alert
        if support_stp is not UNSET:
            field_dict["supportStp"] = support_stp
        if support_extend_stp is not UNSET:
            field_dict["supportExtendStp"] = support_extend_stp
        if mstp_ins_num is not UNSET:
            field_dict["mstpInsNum"] = mstp_ins_num
        if mstp_ins_no is not UNSET:
            field_dict["mstpInsNo"] = mstp_ins_no
        if rpvst_extend_support is not UNSET:
            field_dict["rpvstExtendSupport"] = rpvst_extend_support
        if mstp_port_support is not UNSET:
            field_dict["mstpPortSupport"] = mstp_port_support
        if mstp_get_active_support is not UNSET:
            field_dict["mstpGetActiveSupport"] = mstp_get_active_support
        if rpvst_ins_num is not UNSET:
            field_dict["rpvstInsNum"] = rpvst_ins_num
        if support_cable_test is not UNSET:
            field_dict["supportCableTest"] = support_cable_test
        if support_domain_ping is not UNSET:
            field_dict["supportDomainPing"] = support_domain_ping
        if support_domain_trace_route is not UNSET:
            field_dict["supportDomainTraceRoute"] = support_domain_trace_route
        if support_custom_dhcp_option is not UNSET:
            field_dict["supportCustomDhcpOption"] = support_custom_dhcp_option
        if support_mac_delay is not UNSET:
            field_dict["supportMacDelay"] = support_mac_delay
        if support_dhcp_range is not UNSET:
            field_dict["supportDhcpRange"] = support_dhcp_range
        if support_sdm is not UNSET:
            field_dict["supportSdm"] = support_sdm
        if support_dhcp_reservation is not UNSET:
            field_dict["supportDhcpReservation"] = support_dhcp_reservation
        if support_relay_multi_server is not UNSET:
            field_dict["supportRelayMultiServer"] = support_relay_multi_server
        if support_tpcl_res_info is not UNSET:
            field_dict["supportTpclResInfo"] = support_tpcl_res_info
        if max_relay_server_num is not UNSET:
            field_dict["maxRelayServerNum"] = max_relay_server_num
        if sdm is not UNSET:
            field_dict["sdm"] = sdm
        if locating_ports is not UNSET:
            field_dict["locatingPorts"] = locating_ports
        if locating_standard_ports is not UNSET:
            field_dict["locatingStandardPorts"] = locating_standard_ports
        if support_get_ospf_neighbor_table is not UNSET:
            field_dict["supportGetOspfNeighborTable"] = support_get_ospf_neighbor_table
        if support_vrf is not UNSET:
            field_dict["supportVrf"] = support_vrf
        if support_snmp is not UNSET:
            field_dict["supportSnmp"] = support_snmp
        if support_jumbo is not UNSET:
            field_dict["supportJumbo"] = support_jumbo
        if lag_cap is not UNSET:
            field_dict["lagCap"] = lag_cap
        if license_status_str is not UNSET:
            field_dict["licenseStatusStr"] = license_status_str

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_feature_limit_vo import ApFeatureLimitVO
        from ..models.device_replace_setting_vo import (
            DeviceReplaceSettingVO,
        )
        from ..models.lag_cap_vo import LagCapVO
        from ..models.location_vo import LocationVO
        from ..models.mlag_msg_vo import MlagMsgVO
        from ..models.osw_sdm_template_vo import OswSdmTemplateVO
        from ..models.osw_stack_member_port_vo import (
            OswStackMemberPortVO,
        )
        from ..models.osw_stack_port_cap_vo import OswStackPortCapVO
        from ..models.osw_stack_port_group_vo import (
            OswStackPortGroupVO,
        )
        from ..models.osw_stand_port_vo import OswStandPortVO
        from ..models.osw_vo_profiles import OswVOProfiles
        from ..models.osw_vo_stack_port_cap import OswVOStackPortCap
        from ..models.stack_msg_vo import StackMsgVO

        d = dict(src_dict)
        custom_id = d.pop("customId", UNSET)

        custom_name = d.pop("customName", UNSET)

        site_name = d.pop("siteName", UNSET)

        type_ = d.pop("type", UNSET)

        sub_dev_type = d.pop("subDevType", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        compound_model = d.pop("compoundModel", UNSET)

        show_model = d.pop("showModel", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        version = d.pop("version", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        special_model = d.pop("specialModel", UNSET)

        ip = d.pop("ip", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        uptime = d.pop("uptime", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        adopt_fail_type = d.pop("adoptFailType", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        need_upgrade = d.pop("needUpgrade", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        fw_download = d.pop("fwDownload", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        site = d.pop("site", UNSET)

        _location = d.pop("location", UNSET)
        location: LocationVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationVO.from_dict(_location)

        client_num = d.pop("clientNum", UNSET)

        compatible = d.pop("compatible", UNSET)

        locate_enable = d.pop("locateEnable", UNSET)

        active = d.pop("active", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        due_time = d.pop("dueTime", UNSET)

        due_time_left = d.pop("dueTimeLeft", UNSET)

        license_unbinding_limit = d.pop("licenseUnbindingLimit", UNSET)

        in_whitelist = d.pop("inWhitelist", UNSET)

        sn = d.pop("sn", UNSET)

        eost = d.pop("eost", UNSET)

        eos = d.pop("eos", UNSET)

        combined_gateway = d.pop("combinedGateway", UNSET)

        es = d.pop("es", UNSET)

        ippt = d.pop("ippt", UNSET)

        ippt_preconfig = d.pop("ipptPreconfig", UNSET)

        support_ippt = d.pop("supportIppt", UNSET)

        support_anomaly = d.pop("supportAnomaly", UNSET)

        health_score = d.pop("healthScore", UNSET)

        health_score_time = d.pop("healthScoreTime", UNSET)

        tag_name = d.pop("tagName", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        category = d.pop("category", UNSET)

        pre_config_error_code = d.pop("preConfigErrorCode", UNSET)

        pre_config_retry_type = d.pop("preConfigRetryType", UNSET)

        power_mode = d.pop("powerMode", UNSET)

        power_mode_list = cast(list[int], d.pop("powerModeList", UNSET))

        _feature_limit = d.pop("featureLimit", UNSET)
        feature_limit: ApFeatureLimitVO | Unset
        if isinstance(_feature_limit, Unset):
            feature_limit = UNSET
        else:
            feature_limit = ApFeatureLimitVO.from_dict(_feature_limit)

        wireless_router = d.pop("wirelessRouter", UNSET)

        description = d.pop("description", UNSET)

        online_upgrade_status = d.pop("onlineUpgradeStatus", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        config_sync_status = d.pop("configSyncStatus", UNSET)

        support_running_config = d.pop("supportRunningConfig", UNSET)

        resource = d.pop("resource", UNSET)

        address = d.pop("address", UNSET)

        uplink_device_mac = d.pop("uplinkDeviceMac", UNSET)

        uplink_device_name = d.pop("uplinkDeviceName", UNSET)

        uplink_device_port = d.pop("uplinkDevicePort", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        switch_consistent = d.pop("switchConsistent", UNSET)

        ecsp_first_version = d.pop("ecspFirstVersion", UNSET)

        package_capture_status = d.pop("packageCaptureStatus", UNSET)

        _replace_device_info = d.pop("replaceDeviceInfo", UNSET)
        replace_device_info: DeviceReplaceSettingVO | Unset
        if isinstance(_replace_device_info, Unset):
            replace_device_info = UNSET
        else:
            replace_device_info = DeviceReplaceSettingVO.from_dict(_replace_device_info)

        incidents = d.pop("incidents", UNSET)

        loopback_num = d.pop("loopbackNum", UNSET)

        loop = d.pop("loop", UNSET)

        block_num = d.pop("blockNum", UNSET)

        block = d.pop("block", UNSET)

        poe_total_power = d.pop("poeTotalPower", UNSET)

        poe_remain = d.pop("poeRemain", UNSET)

        fan_status = d.pop("fanStatus", UNSET)

        poe_support = d.pop("poeSupport", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: OswVOProfiles | Unset
        if isinstance(_profiles, Unset):
            profiles = UNSET
        else:
            profiles = OswVOProfiles.from_dict(_profiles)

        _stack_support_ports = d.pop("stackSupportPorts", UNSET)
        stack_support_ports: list[OswStandPortVO] | Unset = UNSET
        if _stack_support_ports is not UNSET:
            stack_support_ports = []
            for stack_support_ports_item_data in _stack_support_ports:
                stack_support_ports_item = OswStandPortVO.from_dict(
                    stack_support_ports_item_data
                )

                stack_support_ports.append(stack_support_ports_item)

        _stack_port_cap = d.pop("stackPortCap", UNSET)
        stack_port_cap: OswVOStackPortCap | Unset
        if isinstance(_stack_port_cap, Unset):
            stack_port_cap = UNSET
        else:
            stack_port_cap = OswVOStackPortCap.from_dict(_stack_port_cap)

        max_stack_groups = d.pop("maxStackGroups", UNSET)

        max_stack_unit_number = d.pop("maxStackUnitNumber", UNSET)

        support_stack_group_speed = d.pop("supportStackGroupSpeed", UNSET)

        _stack_port_config_caps = d.pop("stackPortConfigCaps", UNSET)
        stack_port_config_caps: list[OswStackPortCapVO] | Unset = UNSET
        if _stack_port_config_caps is not UNSET:
            stack_port_config_caps = []
            for stack_port_config_caps_item_data in _stack_port_config_caps:
                stack_port_config_caps_item = OswStackPortCapVO.from_dict(
                    stack_port_config_caps_item_data
                )

                stack_port_config_caps.append(stack_port_config_caps_item)

        default_group_speed_cap = cast(list[int], d.pop("defaultGroupSpeedCap", UNSET))

        _ports = d.pop("ports", UNSET)
        ports: list[OswStackMemberPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswStackMemberPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _stack_ports = d.pop("stackPorts", UNSET)
        stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
        if _stack_ports is not UNSET:
            stack_ports = []
            for stack_ports_item_data in _stack_ports:
                stack_ports_item = OswStackPortGroupVO.from_dict(stack_ports_item_data)

                stack_ports.append(stack_ports_item)

        unit = d.pop("unit", UNSET)

        priority = d.pop("priority", UNSET)

        _stack_msg = d.pop("stackMsg", UNSET)
        stack_msg: StackMsgVO | Unset
        if isinstance(_stack_msg, Unset):
            stack_msg = UNSET
        else:
            stack_msg = StackMsgVO.from_dict(_stack_msg)

        _mlag_msg = d.pop("mlagMsg", UNSET)
        mlag_msg: MlagMsgVO | Unset
        if isinstance(_mlag_msg, Unset):
            mlag_msg = UNSET
        else:
            mlag_msg = MlagMsgVO.from_dict(_mlag_msg)

        stkable_group_id = d.pop("stkableGroupId", UNSET)

        stk_ver = d.pop("stkVer", UNSET)

        support_power_alert = d.pop("supportPowerAlert", UNSET)

        support_stp = d.pop("supportStp", UNSET)

        support_extend_stp = d.pop("supportExtendStp", UNSET)

        mstp_ins_num = d.pop("mstpInsNum", UNSET)

        mstp_ins_no = d.pop("mstpInsNo", UNSET)

        rpvst_extend_support = d.pop("rpvstExtendSupport", UNSET)

        mstp_port_support = d.pop("mstpPortSupport", UNSET)

        mstp_get_active_support = d.pop("mstpGetActiveSupport", UNSET)

        rpvst_ins_num = d.pop("rpvstInsNum", UNSET)

        support_cable_test = d.pop("supportCableTest", UNSET)

        support_domain_ping = d.pop("supportDomainPing", UNSET)

        support_domain_trace_route = d.pop("supportDomainTraceRoute", UNSET)

        support_custom_dhcp_option = d.pop("supportCustomDhcpOption", UNSET)

        support_mac_delay = d.pop("supportMacDelay", UNSET)

        support_dhcp_range = d.pop("supportDhcpRange", UNSET)

        support_sdm = d.pop("supportSdm", UNSET)

        support_dhcp_reservation = d.pop("supportDhcpReservation", UNSET)

        support_relay_multi_server = d.pop("supportRelayMultiServer", UNSET)

        support_tpcl_res_info = d.pop("supportTpclResInfo", UNSET)

        max_relay_server_num = d.pop("maxRelayServerNum", UNSET)

        _sdm = d.pop("sdm", UNSET)
        sdm: OswSdmTemplateVO | Unset
        if isinstance(_sdm, Unset):
            sdm = UNSET
        else:
            sdm = OswSdmTemplateVO.from_dict(_sdm)

        locating_ports = cast(list[int], d.pop("locatingPorts", UNSET))

        locating_standard_ports = cast(list[str], d.pop("locatingStandardPorts", UNSET))

        support_get_ospf_neighbor_table = d.pop("supportGetOspfNeighborTable", UNSET)

        support_vrf = d.pop("supportVrf", UNSET)

        support_snmp = d.pop("supportSnmp", UNSET)

        support_jumbo = d.pop("supportJumbo", UNSET)

        _lag_cap = d.pop("lagCap", UNSET)
        lag_cap: LagCapVO | Unset
        if isinstance(_lag_cap, Unset):
            lag_cap = UNSET
        else:
            lag_cap = LagCapVO.from_dict(_lag_cap)

        license_status_str = d.pop("licenseStatusStr", UNSET)

        osw_vo = cls(
            custom_id=custom_id,
            custom_name=custom_name,
            site_name=site_name,
            type_=type_,
            sub_dev_type=sub_dev_type,
            mac=mac,
            name=name,
            model=model,
            compound_model=compound_model,
            show_model=show_model,
            model_version=model_version,
            firmware_version=firmware_version,
            version=version,
            hw_version=hw_version,
            special_model=special_model,
            ip=ip,
            public_ip=public_ip,
            ipv_6_list=ipv_6_list,
            uptime=uptime,
            uptime_long=uptime_long,
            status_category=status_category,
            status=status,
            adopt_fail_type=adopt_fail_type,
            last_seen=last_seen,
            need_upgrade=need_upgrade,
            latest_version=latest_version,
            fw_download=fw_download,
            cpu_util=cpu_util,
            mem_util=mem_util,
            download=download,
            upload=upload,
            site=site,
            location=location,
            client_num=client_num,
            compatible=compatible,
            locate_enable=locate_enable,
            active=active,
            license_status=license_status,
            due_time=due_time,
            due_time_left=due_time_left,
            license_unbinding_limit=license_unbinding_limit,
            in_whitelist=in_whitelist,
            sn=sn,
            eost=eost,
            eos=eos,
            combined_gateway=combined_gateway,
            es=es,
            ippt=ippt,
            ippt_preconfig=ippt_preconfig,
            support_ippt=support_ippt,
            support_anomaly=support_anomaly,
            health_score=health_score,
            health_score_time=health_score_time,
            tag_name=tag_name,
            added_in_advanced=added_in_advanced,
            category=category,
            pre_config_error_code=pre_config_error_code,
            pre_config_retry_type=pre_config_retry_type,
            power_mode=power_mode,
            power_mode_list=power_mode_list,
            feature_limit=feature_limit,
            wireless_router=wireless_router,
            description=description,
            online_upgrade_status=online_upgrade_status,
            device_series_type=device_series_type,
            config_sync_status=config_sync_status,
            support_running_config=support_running_config,
            resource=resource,
            address=address,
            uplink_device_mac=uplink_device_mac,
            uplink_device_name=uplink_device_name,
            uplink_device_port=uplink_device_port,
            link_speed=link_speed,
            duplex=duplex,
            switch_consistent=switch_consistent,
            ecsp_first_version=ecsp_first_version,
            package_capture_status=package_capture_status,
            replace_device_info=replace_device_info,
            incidents=incidents,
            loopback_num=loopback_num,
            loop=loop,
            block_num=block_num,
            block=block,
            poe_total_power=poe_total_power,
            poe_remain=poe_remain,
            fan_status=fan_status,
            poe_support=poe_support,
            profiles=profiles,
            stack_support_ports=stack_support_ports,
            stack_port_cap=stack_port_cap,
            max_stack_groups=max_stack_groups,
            max_stack_unit_number=max_stack_unit_number,
            support_stack_group_speed=support_stack_group_speed,
            stack_port_config_caps=stack_port_config_caps,
            default_group_speed_cap=default_group_speed_cap,
            ports=ports,
            stack_ports=stack_ports,
            unit=unit,
            priority=priority,
            stack_msg=stack_msg,
            mlag_msg=mlag_msg,
            stkable_group_id=stkable_group_id,
            stk_ver=stk_ver,
            support_power_alert=support_power_alert,
            support_stp=support_stp,
            support_extend_stp=support_extend_stp,
            mstp_ins_num=mstp_ins_num,
            mstp_ins_no=mstp_ins_no,
            rpvst_extend_support=rpvst_extend_support,
            mstp_port_support=mstp_port_support,
            mstp_get_active_support=mstp_get_active_support,
            rpvst_ins_num=rpvst_ins_num,
            support_cable_test=support_cable_test,
            support_domain_ping=support_domain_ping,
            support_domain_trace_route=support_domain_trace_route,
            support_custom_dhcp_option=support_custom_dhcp_option,
            support_mac_delay=support_mac_delay,
            support_dhcp_range=support_dhcp_range,
            support_sdm=support_sdm,
            support_dhcp_reservation=support_dhcp_reservation,
            support_relay_multi_server=support_relay_multi_server,
            support_tpcl_res_info=support_tpcl_res_info,
            max_relay_server_num=max_relay_server_num,
            sdm=sdm,
            locating_ports=locating_ports,
            locating_standard_ports=locating_standard_ports,
            support_get_ospf_neighbor_table=support_get_ospf_neighbor_table,
            support_vrf=support_vrf,
            support_snmp=support_snmp,
            support_jumbo=support_jumbo,
            lag_cap=lag_cap,
            license_status_str=license_status_str,
        )

        osw_vo.additional_properties = d
        return osw_vo

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
