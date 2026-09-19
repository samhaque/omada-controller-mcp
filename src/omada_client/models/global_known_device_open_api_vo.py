from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalKnownDeviceOpenApiVO")


@_attrs_define
class GlobalKnownDeviceOpenApiVO:
    """
    Attributes:
        mac (str | Unset): Device MAC
        name (str | Unset): Device name
        type_ (str | Unset): Device type
        subtype (str | Unset): Switch subtype should be a value as follows: smart: Non-Agile Series Switch; es: Agile
            Series Switch.
        device_series_type (int | Unset): Device series type. 0 means basic, 1 means pro.
        model (str | Unset): Device model name
        ip (str | Unset): Device IP
        ipv6 (list[str] | Unset): Device IPv6 list
        uptime (str | Unset): Device uptime
        status (int | Unset): Device status should be a value as follows: 0: Disconnected; 1: Connected; 2: Pending; 3:
            Heartbeat Missed; 4: Isolated
        last_seen (int | Unset): Device lastSeen
        cpu_util (int | Unset): Device cpuUtil
        mem_util (int | Unset): Device memUtil
        sn (str | Unset): Device serial number
        license_status (int | Unset): Device license status(Only for cloud base) should be a value as follows: 0:
            unActive; 1: Unbind; 2: Expired; 3: active
        need_active (bool | Unset): Device license status(Only for cloud base).If the value is true, the device is ready
            to be activated;If the value is false, the device cannot be activated or has already been activated.
        site_name (str | Unset): The name of the site where the device is located
        tag_name (str | Unset): Device tag name
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    subtype: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    model: str | Unset = UNSET
    ip: str | Unset = UNSET
    ipv6: list[str] | Unset = UNSET
    uptime: str | Unset = UNSET
    status: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_util: int | Unset = UNSET
    sn: str | Unset = UNSET
    license_status: int | Unset = UNSET
    need_active: bool | Unset = UNSET
    site_name: str | Unset = UNSET
    tag_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        type_ = self.type_

        subtype = self.subtype

        device_series_type = self.device_series_type

        model = self.model

        ip = self.ip

        ipv6: list[str] | Unset = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = self.ipv6

        uptime = self.uptime

        status = self.status

        last_seen = self.last_seen

        cpu_util = self.cpu_util

        mem_util = self.mem_util

        sn = self.sn

        license_status = self.license_status

        need_active = self.need_active

        site_name = self.site_name

        tag_name = self.tag_name

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
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if status is not UNSET:
            field_dict["status"] = status
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
        if need_active is not UNSET:
            field_dict["needActive"] = need_active
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name

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

        ip = d.pop("ip", UNSET)

        ipv6 = cast(list[str], d.pop("ipv6", UNSET))

        uptime = d.pop("uptime", UNSET)

        status = d.pop("status", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        sn = d.pop("sn", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        need_active = d.pop("needActive", UNSET)

        site_name = d.pop("siteName", UNSET)

        tag_name = d.pop("tagName", UNSET)

        global_known_device_open_api_vo = cls(
            mac=mac,
            name=name,
            type_=type_,
            subtype=subtype,
            device_series_type=device_series_type,
            model=model,
            ip=ip,
            ipv6=ipv6,
            uptime=uptime,
            status=status,
            last_seen=last_seen,
            cpu_util=cpu_util,
            mem_util=mem_util,
            sn=sn,
            license_status=license_status,
            need_active=need_active,
            site_name=site_name,
            tag_name=tag_name,
        )

        global_known_device_open_api_vo.additional_properties = d
        return global_known_device_open_api_vo

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
