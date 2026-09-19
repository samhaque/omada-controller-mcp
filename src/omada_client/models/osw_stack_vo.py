from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_delay_vo import MacDelayVO
    from ..models.mad_setting_vo import MadSettingVO
    from ..models.osw_qos_config_vo import OswQosConfigVO
    from ..models.osw_stack_member_vo import OswStackMemberVO


T = TypeVar("T", bound="OswStackVO")


@_attrs_define
class OswStackVO:
    """
    Attributes:
        name (str): Stack Name
        id (str | Unset): Stack ID
        site_id (str | Unset): Site ID
        site_name (str | Unset): Site Name
        status (int | Unset): Stack Status should be a value as follows: 0: normal; 1: abnormal; 2: stack not ready
        abnormal_reason (int | Unset): Abnormal Reason
        ip (str | Unset): IP
        devices_num (int | Unset): Number of devices
        license_status (int | Unset): License Status should be a value as follows: 0: Activated; 1: Unactivated; 2: Not
            All Activated, 3: Expired
        due_time (int | Unset): Expiration time
        due_time_left (int | Unset): The number of milliseconds from the current time to the expiration time
        traffic_down (int | Unset): Traffic Down
        traffic_up (int | Unset): Traffic Up
        clients (int | Unset): Clients
        master_mac (str | Unset): Master device mac
        master_device_active (bool | Unset): Marks whether the master device of the stack system is activated
        loopback_num (int | Unset): Loopback Num
        loop (str | Unset): Loopback port
        block_num (int | Unset): Block Num
        block (str | Unset): Block port
        tag (str | Unset): Tag
        member (list[OswStackMemberVO] | Unset): Stack member list
        detected_member (list[OswStackMemberVO] | Unset): List of members that have been detected by the stack
        locate_enable (bool | Unset): Indicates whether the locate function is enabled
        version (str | Unset): Version
        latest_version (str | Unset): Latest Version
        need_upgrade (bool | Unset): Indicates whether an upgrade is required
        fw_download (bool | Unset): Indicates whether the upgrade status is downloading
        description (str | Unset):
        qos_config (OswQosConfigVO | Unset): Switch qos config
        mac_delay (MacDelayVO | Unset): Mac Delay
        virtual_mac (str | Unset): Virtual Mac
        mad_setting (MadSettingVO | Unset): Mad Setting
        support_mac_delay (bool | Unset):
    """

    name: str
    id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    site_name: str | Unset = UNSET
    status: int | Unset = UNSET
    abnormal_reason: int | Unset = UNSET
    ip: str | Unset = UNSET
    devices_num: int | Unset = UNSET
    license_status: int | Unset = UNSET
    due_time: int | Unset = UNSET
    due_time_left: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    clients: int | Unset = UNSET
    master_mac: str | Unset = UNSET
    master_device_active: bool | Unset = UNSET
    loopback_num: int | Unset = UNSET
    loop: str | Unset = UNSET
    block_num: int | Unset = UNSET
    block: str | Unset = UNSET
    tag: str | Unset = UNSET
    member: list[OswStackMemberVO] | Unset = UNSET
    detected_member: list[OswStackMemberVO] | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    version: str | Unset = UNSET
    latest_version: str | Unset = UNSET
    need_upgrade: bool | Unset = UNSET
    fw_download: bool | Unset = UNSET
    description: str | Unset = UNSET
    qos_config: OswQosConfigVO | Unset = UNSET
    mac_delay: MacDelayVO | Unset = UNSET
    virtual_mac: str | Unset = UNSET
    mad_setting: MadSettingVO | Unset = UNSET
    support_mac_delay: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        site_id = self.site_id

        site_name = self.site_name

        status = self.status

        abnormal_reason = self.abnormal_reason

        ip = self.ip

        devices_num = self.devices_num

        license_status = self.license_status

        due_time = self.due_time

        due_time_left = self.due_time_left

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        clients = self.clients

        master_mac = self.master_mac

        master_device_active = self.master_device_active

        loopback_num = self.loopback_num

        loop = self.loop

        block_num = self.block_num

        block = self.block

        tag = self.tag

        member: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = []
            for member_item_data in self.member:
                member_item = member_item_data.to_dict()
                member.append(member_item)

        detected_member: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detected_member, Unset):
            detected_member = []
            for detected_member_item_data in self.detected_member:
                detected_member_item = detected_member_item_data.to_dict()
                detected_member.append(detected_member_item)

        locate_enable = self.locate_enable

        version = self.version

        latest_version = self.latest_version

        need_upgrade = self.need_upgrade

        fw_download = self.fw_download

        description = self.description

        qos_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_config, Unset):
            qos_config = self.qos_config.to_dict()

        mac_delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac_delay, Unset):
            mac_delay = self.mac_delay.to_dict()

        virtual_mac = self.virtual_mac

        mad_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mad_setting, Unset):
            mad_setting = self.mad_setting.to_dict()

        support_mac_delay = self.support_mac_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if status is not UNSET:
            field_dict["status"] = status
        if abnormal_reason is not UNSET:
            field_dict["abnormalReason"] = abnormal_reason
        if ip is not UNSET:
            field_dict["ip"] = ip
        if devices_num is not UNSET:
            field_dict["devicesNum"] = devices_num
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if due_time is not UNSET:
            field_dict["dueTime"] = due_time
        if due_time_left is not UNSET:
            field_dict["dueTimeLeft"] = due_time_left
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if clients is not UNSET:
            field_dict["clients"] = clients
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if master_device_active is not UNSET:
            field_dict["masterDeviceActive"] = master_device_active
        if loopback_num is not UNSET:
            field_dict["loopbackNum"] = loopback_num
        if loop is not UNSET:
            field_dict["loop"] = loop
        if block_num is not UNSET:
            field_dict["blockNum"] = block_num
        if block is not UNSET:
            field_dict["block"] = block
        if tag is not UNSET:
            field_dict["tag"] = tag
        if member is not UNSET:
            field_dict["member"] = member
        if detected_member is not UNSET:
            field_dict["detectedMember"] = detected_member
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if version is not UNSET:
            field_dict["version"] = version
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if need_upgrade is not UNSET:
            field_dict["needUpgrade"] = need_upgrade
        if fw_download is not UNSET:
            field_dict["fwDownload"] = fw_download
        if description is not UNSET:
            field_dict["description"] = description
        if qos_config is not UNSET:
            field_dict["qosConfig"] = qos_config
        if mac_delay is not UNSET:
            field_dict["macDelay"] = mac_delay
        if virtual_mac is not UNSET:
            field_dict["virtualMac"] = virtual_mac
        if mad_setting is not UNSET:
            field_dict["madSetting"] = mad_setting
        if support_mac_delay is not UNSET:
            field_dict["supportMacDelay"] = support_mac_delay

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mac_delay_vo import MacDelayVO
        from ..models.mad_setting_vo import MadSettingVO
        from ..models.osw_qos_config_vo import OswQosConfigVO
        from ..models.osw_stack_member_vo import OswStackMemberVO

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        status = d.pop("status", UNSET)

        abnormal_reason = d.pop("abnormalReason", UNSET)

        ip = d.pop("ip", UNSET)

        devices_num = d.pop("devicesNum", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        due_time = d.pop("dueTime", UNSET)

        due_time_left = d.pop("dueTimeLeft", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        clients = d.pop("clients", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        master_device_active = d.pop("masterDeviceActive", UNSET)

        loopback_num = d.pop("loopbackNum", UNSET)

        loop = d.pop("loop", UNSET)

        block_num = d.pop("blockNum", UNSET)

        block = d.pop("block", UNSET)

        tag = d.pop("tag", UNSET)

        _member = d.pop("member", UNSET)
        member: list[OswStackMemberVO] | Unset = UNSET
        if _member is not UNSET:
            member = []
            for member_item_data in _member:
                member_item = OswStackMemberVO.from_dict(member_item_data)

                member.append(member_item)

        _detected_member = d.pop("detectedMember", UNSET)
        detected_member: list[OswStackMemberVO] | Unset = UNSET
        if _detected_member is not UNSET:
            detected_member = []
            for detected_member_item_data in _detected_member:
                detected_member_item = OswStackMemberVO.from_dict(
                    detected_member_item_data
                )

                detected_member.append(detected_member_item)

        locate_enable = d.pop("locateEnable", UNSET)

        version = d.pop("version", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        need_upgrade = d.pop("needUpgrade", UNSET)

        fw_download = d.pop("fwDownload", UNSET)

        description = d.pop("description", UNSET)

        _qos_config = d.pop("qosConfig", UNSET)
        qos_config: OswQosConfigVO | Unset
        if isinstance(_qos_config, Unset):
            qos_config = UNSET
        else:
            qos_config = OswQosConfigVO.from_dict(_qos_config)

        _mac_delay = d.pop("macDelay", UNSET)
        mac_delay: MacDelayVO | Unset
        if isinstance(_mac_delay, Unset):
            mac_delay = UNSET
        else:
            mac_delay = MacDelayVO.from_dict(_mac_delay)

        virtual_mac = d.pop("virtualMac", UNSET)

        _mad_setting = d.pop("madSetting", UNSET)
        mad_setting: MadSettingVO | Unset
        if isinstance(_mad_setting, Unset):
            mad_setting = UNSET
        else:
            mad_setting = MadSettingVO.from_dict(_mad_setting)

        support_mac_delay = d.pop("supportMacDelay", UNSET)

        osw_stack_vo = cls(
            name=name,
            id=id,
            site_id=site_id,
            site_name=site_name,
            status=status,
            abnormal_reason=abnormal_reason,
            ip=ip,
            devices_num=devices_num,
            license_status=license_status,
            due_time=due_time,
            due_time_left=due_time_left,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            clients=clients,
            master_mac=master_mac,
            master_device_active=master_device_active,
            loopback_num=loopback_num,
            loop=loop,
            block_num=block_num,
            block=block,
            tag=tag,
            member=member,
            detected_member=detected_member,
            locate_enable=locate_enable,
            version=version,
            latest_version=latest_version,
            need_upgrade=need_upgrade,
            fw_download=fw_download,
            description=description,
            qos_config=qos_config,
            mac_delay=mac_delay,
            virtual_mac=virtual_mac,
            mad_setting=mad_setting,
            support_mac_delay=support_mac_delay,
        )

        osw_stack_vo.additional_properties = d
        return osw_stack_vo

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
