from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_vrrp_device_open_api_vo import OswVrrpDeviceOpenApiVO


T = TypeVar("T", bound="OswVrrpOpenApiVO")


@_attrs_define
class OswVrrpOpenApiVO:
    """
    Attributes:
        name (str): VRRP name, it should be visible ASCII, and should contain 1 to 64 characters.
        vr_id (int): Virtual Router ID, its value should be within the range of 1-255.
        advertise_timer (int): AdvertiseTimer should be within the range of 1-255, the default setting value is 100 and
            the unit is millimeter second.
        preempt_mode (bool): Whether the preemption mode is enabled or not, it defaults to enabled.
        delay_time (int): DelayTime should be within the range of 0-255, default setting is 0 and the unit is second
        authentication (int): Authentication type should be a value as follows: 0: NONE, 1: Simple, 2: MD5
        id (str | Unset): VRRP ID
        device_list (list[OswVrrpDeviceOpenApiVO] | Unset): Up to 8 entries are allowed for the deviceList, and it
            cannot be empty.
        virtual_ipv_4_s (list[str] | Unset): Up to 32 entries are allowed for the virtualIpv4s.
        ip_v6_link_local (str | Unset): Virtual IpV6LinkLocal Address
        ip_v6_global (list[str] | Unset): Up to 15 entries are allowed for the ipV6Global.
        key (str | Unset): Key of VRRP
        status (int | Unset): The current status of VRRP, it should be a value as follows: 0: NORMAL, 1: FAILED, 2:
            ABNORMAL
        ipv_4_master_device (str | Unset): IPV4 Master Device
        ipv_6_master_device (str | Unset): IPV6 Master Device
    """

    name: str
    vr_id: int
    advertise_timer: int
    preempt_mode: bool
    delay_time: int
    authentication: int
    id: str | Unset = UNSET
    device_list: list[OswVrrpDeviceOpenApiVO] | Unset = UNSET
    virtual_ipv_4_s: list[str] | Unset = UNSET
    ip_v6_link_local: str | Unset = UNSET
    ip_v6_global: list[str] | Unset = UNSET
    key: str | Unset = UNSET
    status: int | Unset = UNSET
    ipv_4_master_device: str | Unset = UNSET
    ipv_6_master_device: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        vr_id = self.vr_id

        advertise_timer = self.advertise_timer

        preempt_mode = self.preempt_mode

        delay_time = self.delay_time

        authentication = self.authentication

        id = self.id

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        virtual_ipv_4_s: list[str] | Unset = UNSET
        if not isinstance(self.virtual_ipv_4_s, Unset):
            virtual_ipv_4_s = self.virtual_ipv_4_s

        ip_v6_link_local = self.ip_v6_link_local

        ip_v6_global: list[str] | Unset = UNSET
        if not isinstance(self.ip_v6_global, Unset):
            ip_v6_global = self.ip_v6_global

        key = self.key

        status = self.status

        ipv_4_master_device = self.ipv_4_master_device

        ipv_6_master_device = self.ipv_6_master_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "vrId": vr_id,
                "advertiseTimer": advertise_timer,
                "preemptMode": preempt_mode,
                "delayTime": delay_time,
                "authentication": authentication,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list
        if virtual_ipv_4_s is not UNSET:
            field_dict["virtualIpv4s"] = virtual_ipv_4_s
        if ip_v6_link_local is not UNSET:
            field_dict["ipV6LinkLocal"] = ip_v6_link_local
        if ip_v6_global is not UNSET:
            field_dict["ipV6Global"] = ip_v6_global
        if key is not UNSET:
            field_dict["key"] = key
        if status is not UNSET:
            field_dict["status"] = status
        if ipv_4_master_device is not UNSET:
            field_dict["ipv4MasterDevice"] = ipv_4_master_device
        if ipv_6_master_device is not UNSET:
            field_dict["ipv6MasterDevice"] = ipv_6_master_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_vrrp_device_open_api_vo import (
            OswVrrpDeviceOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        vr_id = d.pop("vrId")

        advertise_timer = d.pop("advertiseTimer")

        preempt_mode = d.pop("preemptMode")

        delay_time = d.pop("delayTime")

        authentication = d.pop("authentication")

        id = d.pop("id", UNSET)

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[OswVrrpDeviceOpenApiVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = OswVrrpDeviceOpenApiVO.from_dict(
                    device_list_item_data
                )

                device_list.append(device_list_item)

        virtual_ipv_4_s = cast(list[str], d.pop("virtualIpv4s", UNSET))

        ip_v6_link_local = d.pop("ipV6LinkLocal", UNSET)

        ip_v6_global = cast(list[str], d.pop("ipV6Global", UNSET))

        key = d.pop("key", UNSET)

        status = d.pop("status", UNSET)

        ipv_4_master_device = d.pop("ipv4MasterDevice", UNSET)

        ipv_6_master_device = d.pop("ipv6MasterDevice", UNSET)

        osw_vrrp_open_api_vo = cls(
            name=name,
            vr_id=vr_id,
            advertise_timer=advertise_timer,
            preempt_mode=preempt_mode,
            delay_time=delay_time,
            authentication=authentication,
            id=id,
            device_list=device_list,
            virtual_ipv_4_s=virtual_ipv_4_s,
            ip_v6_link_local=ip_v6_link_local,
            ip_v6_global=ip_v6_global,
            key=key,
            status=status,
            ipv_4_master_device=ipv_4_master_device,
            ipv_6_master_device=ipv_6_master_device,
        )

        osw_vrrp_open_api_vo.additional_properties = d
        return osw_vrrp_open_api_vo

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
