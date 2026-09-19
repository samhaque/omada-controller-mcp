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
    from ..models.olt_detail_downlink_vo import OltDetailDownlinkVO
    from ..models.olt_detail_vo_components import OltDetailVOComponents
    from ..models.olt_dev_cap_vo import OltDevCapVO
    from ..models.olt_uplink_vo import OltUplinkVO


T = TypeVar("T", bound="OltDetailVO")


@_attrs_define
class OltDetailVO:
    """
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
        ip (str | Unset): Ip address
        public_ip (str | Unset): Public ip address
        ipv_6_list (list[str] | Unset): Ipv6 address List
        uptime (str | Unset): Runtime duration, for example:0 days 00:44:09
        uptime_long (int | Unset): Runtime duration, in seconds (s).
        cpu_util (int | Unset): Cpu utilization
        mem_util (int | Unset): Memory utilization
        last_seen (int | Unset): Last online timestamp (ms)
        down (int | Unset): Total real-time down-link traffic(byte)
        up (int | Unset): Total real-time up-link traffic(byte)
        onu_count (int | Unset): Number of ONUs managed by the device
        dev_cap (OltDevCapVO | Unset): Capability of device
        tag_ids (list[str] | Unset): Bound tag ID
        components (OltDetailVOComponents | Unset): Component information of the Omada Controller sent to the OLT
        downlink_list (list[OltDetailDownlinkVO] | Unset): Down-link list
        uplink (OltUplinkVO | Unset): Up-link device
        speeds (list[int] | Unset): Supported rate list for all ports. Speeds should be a value as follows: 0:auto;
            1:10M; 2:100M; 3:1000M; 4:2.5G; 5:10G; 6:5G; 7:25G; 8:100G; 9:40G; -1:error; no value:all rate supported
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
    ip: str | Unset = UNSET
    public_ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    uptime: str | Unset = UNSET
    uptime_long: int | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_util: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    down: int | Unset = UNSET
    up: int | Unset = UNSET
    onu_count: int | Unset = UNSET
    dev_cap: OltDevCapVO | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    components: OltDetailVOComponents | Unset = UNSET
    downlink_list: list[OltDetailDownlinkVO] | Unset = UNSET
    uplink: OltUplinkVO | Unset = UNSET
    speeds: list[int] | Unset = UNSET
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

        down = self.down

        up = self.up

        onu_count = self.onu_count

        dev_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_cap, Unset):
            dev_cap = self.dev_cap.to_dict()

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        downlink_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_list, Unset):
            downlink_list = []
            for downlink_list_item_data in self.downlink_list:
                downlink_list_item = downlink_list_item_data.to_dict()
                downlink_list.append(downlink_list_item)

        uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink, Unset):
            uplink = self.uplink.to_dict()

        speeds: list[int] | Unset = UNSET
        if not isinstance(self.speeds, Unset):
            speeds = self.speeds

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
        if down is not UNSET:
            field_dict["down"] = down
        if up is not UNSET:
            field_dict["up"] = up
        if onu_count is not UNSET:
            field_dict["onuCount"] = onu_count
        if dev_cap is not UNSET:
            field_dict["devCap"] = dev_cap
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if components is not UNSET:
            field_dict["components"] = components
        if downlink_list is not UNSET:
            field_dict["downlinkList"] = downlink_list
        if uplink is not UNSET:
            field_dict["uplink"] = uplink
        if speeds is not UNSET:
            field_dict["speeds"] = speeds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )
        from ..models.device_replace_setting_vo import (
            DeviceReplaceSettingVO,
        )
        from ..models.olt_detail_downlink_vo import OltDetailDownlinkVO
        from ..models.olt_detail_vo_components import (
            OltDetailVOComponents,
        )
        from ..models.olt_dev_cap_vo import OltDevCapVO
        from ..models.olt_uplink_vo import OltUplinkVO

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

        ip = d.pop("ip", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        uptime = d.pop("uptime", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        down = d.pop("down", UNSET)

        up = d.pop("up", UNSET)

        onu_count = d.pop("onuCount", UNSET)

        _dev_cap = d.pop("devCap", UNSET)
        dev_cap: OltDevCapVO | Unset
        if isinstance(_dev_cap, Unset):
            dev_cap = UNSET
        else:
            dev_cap = OltDevCapVO.from_dict(_dev_cap)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        _components = d.pop("components", UNSET)
        components: OltDetailVOComponents | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = OltDetailVOComponents.from_dict(_components)

        _downlink_list = d.pop("downlinkList", UNSET)
        downlink_list: list[OltDetailDownlinkVO] | Unset = UNSET
        if _downlink_list is not UNSET:
            downlink_list = []
            for downlink_list_item_data in _downlink_list:
                downlink_list_item = OltDetailDownlinkVO.from_dict(
                    downlink_list_item_data
                )

                downlink_list.append(downlink_list_item)

        _uplink = d.pop("uplink", UNSET)
        uplink: OltUplinkVO | Unset
        if isinstance(_uplink, Unset):
            uplink = UNSET
        else:
            uplink = OltUplinkVO.from_dict(_uplink)

        speeds = cast(list[int], d.pop("speeds", UNSET))

        olt_detail_vo = cls(
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
            ip=ip,
            public_ip=public_ip,
            ipv_6_list=ipv_6_list,
            uptime=uptime,
            uptime_long=uptime_long,
            cpu_util=cpu_util,
            mem_util=mem_util,
            last_seen=last_seen,
            down=down,
            up=up,
            onu_count=onu_count,
            dev_cap=dev_cap,
            tag_ids=tag_ids,
            components=components,
            downlink_list=downlink_list,
            uplink=uplink,
            speeds=speeds,
        )

        olt_detail_vo.additional_properties = d
        return olt_detail_vo

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
