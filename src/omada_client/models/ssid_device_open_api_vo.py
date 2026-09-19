from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidDeviceOpenApiVO")


@_attrs_define
class SsidDeviceOpenApiVO:
    """
    Attributes:
        id (str | Unset): Device ID
        mac (str | Unset): Device MAC address
        name (str | Unset): Device name
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        ap_group_name (str | Unset): AP Group Name
        ap_group_id (str | Unset): apGroupId
        client_num (int | Unset): number of clients connected to Device
        traffic (int | Unset): total traffic of Device
        device_type (str | Unset): Device type, such as EAP, Gateway
        ip (str | Unset): Ip address,such as 192.168.0.105
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        override_num (int | Unset): Override ssid number for AP
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ap_group_name: str | Unset = UNSET
    ap_group_id: str | Unset = UNSET
    client_num: int | Unset = UNSET
    traffic: int | Unset = UNSET
    device_type: str | Unset = UNSET
    ip: str | Unset = UNSET
    show_model: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    override_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        ap_group_name = self.ap_group_name

        ap_group_id = self.ap_group_id

        client_num = self.client_num

        traffic = self.traffic

        device_type = self.device_type

        ip = self.ip

        show_model = self.show_model

        status = self.status

        status_category = self.status_category

        override_num = self.override_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ap_group_name is not UNSET:
            field_dict["apGroupName"] = ap_group_name
        if ap_group_id is not UNSET:
            field_dict["apGroupId"] = ap_group_id
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if ip is not UNSET:
            field_dict["ip"] = ip
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if override_num is not UNSET:
            field_dict["overrideNum"] = override_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ap_group_name = d.pop("apGroupName", UNSET)

        ap_group_id = d.pop("apGroupId", UNSET)

        client_num = d.pop("clientNum", UNSET)

        traffic = d.pop("traffic", UNSET)

        device_type = d.pop("deviceType", UNSET)

        ip = d.pop("ip", UNSET)

        show_model = d.pop("showModel", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        override_num = d.pop("overrideNum", UNSET)

        ssid_device_open_api_vo = cls(
            id=id,
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            ap_group_name=ap_group_name,
            ap_group_id=ap_group_id,
            client_num=client_num,
            traffic=traffic,
            device_type=device_type,
            ip=ip,
            show_model=show_model,
            status=status,
            status_category=status_category,
            override_num=override_num,
        )

        ssid_device_open_api_vo.additional_properties = d
        return ssid_device_open_api_vo

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
