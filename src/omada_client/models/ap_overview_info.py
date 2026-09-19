from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_wireless_uplink import ApWirelessUplink


T = TypeVar("T", bound="ApOverviewInfo")


@_attrs_define
class ApOverviewInfo:
    """
    Attributes:
        type_ (str | Unset): Device type
        mac (str | Unset): Device MAC, e.g. 00-00-FF-FF-0C-E9
        name (str | Unset): Device name
        ip (str | Unset): Device IP
        ipv_6_list (list[str] | Unset): Device IPv6
        wlan_group_id (str | Unset): WLAN group ID
        wireless_linked (bool | Unset): Whether AP is wireless linked
        wireless_uplink_info (ApWirelessUplink | Unset): Wireless uplink info
        model (str | Unset): Device model
        firmware_version (str | Unset): Device firmware version
        cpu_util (int | Unset): Device cpu util(like 1 means 1% cpu util)
        memory_util (int | Unset): Device memory util(like 50 means 50% memory util)
        uptime_long (int | Unset): Device uptime(unit:second)
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;
            1:Disconnected(Migrating); 10:Provisioning; 11:Configuring; 12:Upgrading; 13:Rebooting; 14:Connected;
            15:Connected(Wireless); 16:Connected(Migrating); 17:Connected(Wireless,Migrating); 20:Pending;
            21:Pending(Wireless); 22:Adopting; 23:Adopting(Wireless); 24:Adopt Failed; 25:Adopt Failed(Wireless); 26:Managed
            By Others; 27:Managed By Others(Wireless); 30:Heartbeat Missed; 31:Heartbeat Missed(Wireless); 32:Heartbeat
            Missed(Migrating); 33:Heartbeat Missed(Wireless,Migrating); 40:Isolated; 41:Isolated(Migrating); 50:Slice
            Configuring
        status_category (int | Unset): Category of device status, statusCategory should be a value as follows:
            0:Disconnected; 1:Connected; 2:Pending; 3:Heartbeat Missed; 4:Isolated
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    wlan_group_id: str | Unset = UNSET
    wireless_linked: bool | Unset = UNSET
    wireless_uplink_info: ApWirelessUplink | Unset = UNSET
    model: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    cpu_util: int | Unset = UNSET
    memory_util: int | Unset = UNSET
    uptime_long: int | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        ip = self.ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        wlan_group_id = self.wlan_group_id

        wireless_linked = self.wireless_linked

        wireless_uplink_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_uplink_info, Unset):
            wireless_uplink_info = self.wireless_uplink_info.to_dict()

        model = self.model

        firmware_version = self.firmware_version

        cpu_util = self.cpu_util

        memory_util = self.memory_util

        uptime_long = self.uptime_long

        status = self.status

        status_category = self.status_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if wlan_group_id is not UNSET:
            field_dict["wlan group id"] = wlan_group_id
        if wireless_linked is not UNSET:
            field_dict["wirelessLinked"] = wireless_linked
        if wireless_uplink_info is not UNSET:
            field_dict["wireless uplink info"] = wireless_uplink_info
        if model is not UNSET:
            field_dict["model"] = model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if memory_util is not UNSET:
            field_dict["memoryUtil"] = memory_util
        if uptime_long is not UNSET:
            field_dict["uptimeLong"] = uptime_long
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_wireless_uplink import ApWirelessUplink

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        wlan_group_id = d.pop("wlan group id", UNSET)

        wireless_linked = d.pop("wirelessLinked", UNSET)

        _wireless_uplink_info = d.pop("wireless uplink info", UNSET)
        wireless_uplink_info: ApWirelessUplink | Unset
        if isinstance(_wireless_uplink_info, Unset):
            wireless_uplink_info = UNSET
        else:
            wireless_uplink_info = ApWirelessUplink.from_dict(_wireless_uplink_info)

        model = d.pop("model", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        memory_util = d.pop("memoryUtil", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        ap_overview_info = cls(
            type_=type_,
            mac=mac,
            name=name,
            ip=ip,
            ipv_6_list=ipv_6_list,
            wlan_group_id=wlan_group_id,
            wireless_linked=wireless_linked,
            wireless_uplink_info=wireless_uplink_info,
            model=model,
            firmware_version=firmware_version,
            cpu_util=cpu_util,
            memory_util=memory_util,
            uptime_long=uptime_long,
            status=status,
            status_category=status_category,
        )

        ap_overview_info.additional_properties = d
        return ap_overview_info

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
