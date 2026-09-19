from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInfo")


@_attrs_define
class DeviceInfo:
    """
    Attributes:
        mac (str | Unset): Device MAC
        name (str | Unset): Device name
        type_ (str | Unset): Device type
        subtype (str | Unset): Switch subtype should be a value as follows: smart: Non-Agile Series Switch; es: Agile
            Series Switch.
        device_series_type (int | Unset): Device series type. 0 means basic, 1 means pro.
        model (str | Unset): Device model name with version
        model_name (str | Unset): Device model name
        ip (str | Unset): Device IP
        ipv6 (list[str] | Unset): Device IPv6 list
        uptime (str | Unset): Device uptime
        status (int | Unset): Device status should be a value as follows: 0: Disconnected; 1: Connected; 2: Pending; 3:
            Heartbeat Missed; 4: Isolated
        detail_status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected
            (Migrating);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Conn
            ected(Migrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wirele
            ss);24:Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        model_version (str | Unset): Model version of device,for example:3.0
        last_seen (int | Unset): Device lastSeen
        cpu_util (int | Unset): Device cpuUtil
        mem_util (int | Unset): Device memUtil
        sn (str | Unset): Device serial number
        license_status (int | Unset): Device license status (Only for cloud base) should be a value as follows: 0:
            unActive; 1: Unbind; 2: Expired; 3: active
        tag_name (str | Unset): Device tag name
        uplink_device_mac (str | Unset): Uplink device mac
        uplink_device_name (str | Unset): Uplink device name
        uplink_device_port (str | Unset): Uplink device port
        link_speed (int | Unset): Device uplink port linkSpeed, linkSpeed should be a value as follows: 0: Auto; 1: 10M;
            2: 100M; 3: 1000M; 4: 2500M; 5: 10G; 6: 5G; 7: 25G, 8: 100G.
        duplex (int | Unset): Device uplink port duplex mode, duplex should be a value as follows: 0: Auto; 1: Half; 2:
            Full.
        switch_consistent (bool | Unset): Whether the device can be adopted by the site.
        public_ip (str | Unset): Device public IP
        firmware_version (str | Unset): The device firmware version.
        compatible (int | Unset): The compatible type of device.
        active (bool | Unset): Indicates whether the device is activated.
        in_white_list (bool | Unset): Whether the device is in white list.
        support_afc (bool | Unset): Whether the device supports AFC.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    subtype: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    model: str | Unset = UNSET
    model_name: str | Unset = UNSET
    ip: str | Unset = UNSET
    ipv6: list[str] | Unset = UNSET
    uptime: str | Unset = UNSET
    status: int | Unset = UNSET
    detail_status: int | Unset = UNSET
    model_version: str | Unset = UNSET
    last_seen: int | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_util: int | Unset = UNSET
    sn: str | Unset = UNSET
    license_status: int | Unset = UNSET
    tag_name: str | Unset = UNSET
    uplink_device_mac: str | Unset = UNSET
    uplink_device_name: str | Unset = UNSET
    uplink_device_port: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    switch_consistent: bool | Unset = UNSET
    public_ip: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    compatible: int | Unset = UNSET
    active: bool | Unset = UNSET
    in_white_list: bool | Unset = UNSET
    support_afc: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        type_ = self.type_

        subtype = self.subtype

        device_series_type = self.device_series_type

        model = self.model

        model_name = self.model_name

        ip = self.ip

        ipv6: list[str] | Unset = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = self.ipv6

        uptime = self.uptime

        status = self.status

        detail_status = self.detail_status

        model_version = self.model_version

        last_seen = self.last_seen

        cpu_util = self.cpu_util

        mem_util = self.mem_util

        sn = self.sn

        license_status = self.license_status

        tag_name = self.tag_name

        uplink_device_mac = self.uplink_device_mac

        uplink_device_name = self.uplink_device_name

        uplink_device_port = self.uplink_device_port

        link_speed = self.link_speed

        duplex = self.duplex

        switch_consistent = self.switch_consistent

        public_ip = self.public_ip

        firmware_version = self.firmware_version

        compatible = self.compatible

        active = self.active

        in_white_list = self.in_white_list

        support_afc = self.support_afc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if model is not UNSET:
            field_dict["model"] = model
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if status is not UNSET:
            field_dict["status"] = status
        if detail_status is not UNSET:
            field_dict["detailStatus"] = detail_status
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util
        if sn is not UNSET:
            field_dict["sn"] = sn
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name
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
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if active is not UNSET:
            field_dict["active"] = active
        if in_white_list is not UNSET:
            field_dict["inWhiteList"] = in_white_list
        if support_afc is not UNSET:
            field_dict["supportAfc"] = support_afc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        subtype = d.pop("subtype", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        model = d.pop("model", UNSET)

        model_name = d.pop("modelName", UNSET)

        ip = d.pop("ip", UNSET)

        ipv6 = cast(list[str], d.pop("ipv6", UNSET))

        uptime = d.pop("uptime", UNSET)

        status = d.pop("status", UNSET)

        detail_status = d.pop("detailStatus", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        sn = d.pop("sn", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        tag_name = d.pop("tagName", UNSET)

        uplink_device_mac = d.pop("uplinkDeviceMac", UNSET)

        uplink_device_name = d.pop("uplinkDeviceName", UNSET)

        uplink_device_port = d.pop("uplinkDevicePort", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        switch_consistent = d.pop("switchConsistent", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        compatible = d.pop("compatible", UNSET)

        active = d.pop("active", UNSET)

        in_white_list = d.pop("inWhiteList", UNSET)

        support_afc = d.pop("supportAfc", UNSET)

        device_info = cls(
            mac=mac,
            name=name,
            type_=type_,
            subtype=subtype,
            device_series_type=device_series_type,
            model=model,
            model_name=model_name,
            ip=ip,
            ipv6=ipv6,
            uptime=uptime,
            status=status,
            detail_status=detail_status,
            model_version=model_version,
            last_seen=last_seen,
            cpu_util=cpu_util,
            mem_util=mem_util,
            sn=sn,
            license_status=license_status,
            tag_name=tag_name,
            uplink_device_mac=uplink_device_mac,
            uplink_device_name=uplink_device_name,
            uplink_device_port=uplink_device_port,
            link_speed=link_speed,
            duplex=duplex,
            switch_consistent=switch_consistent,
            public_ip=public_ip,
            firmware_version=firmware_version,
            compatible=compatible,
            active=active,
            in_white_list=in_white_list,
            support_afc=support_afc,
        )

        device_info.additional_properties = d
        return device_info

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
