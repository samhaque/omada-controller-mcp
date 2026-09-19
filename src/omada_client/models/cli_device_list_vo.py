from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CliDeviceListVO")


@_attrs_define
class CliDeviceListVO:
    """
    Attributes:
        mac (str | Unset): Device mac
        name (str | Unset): Device name
        model (str | Unset): Model of device
        model_version (str | Unset): Model version of device
        ip (str | Unset): Ip address
        status (int | Unset): Status of device.Status should be a value as follows: 0:Disconnected;
            1:Disconnected(Migrating); 10:Provisioning; 11:Configuring; 12:Upgrading; 13:Rebooting; 14:Connected;
            15:Connected(Wireless); 16:Connected(Migrating); 17:Connected(Wireless,Migrating); 20:Pending;
            21:Pending(Wireless); 22:Adopting; 23:Adopting(Wireless); 24:Adopt Failed; 25:Adopt Failed(Wireless); 26:Managed
            By Others; 27:Managed By Others(Wireless); 30:Heartbeat Missed; 31:Heartbeat Missed(Wireless); 32:Heartbeat
            Missed(Migrating); 33:Heartbeat Missed(Wireless,Migrating); 40:Isolated; 41:Isolated(Migrating); 50:Slice
            Configuring
        support_cli (bool | Unset): Whether the device supports Cli
        stack_id (str | Unset): The ID of the associated stack. If the device is not a member of stack, stackId should
            be null
        stack_name (str | Unset): The name of the associated stack. If the device is not a member of stack, stackName
            should be null
        master_mac (str | Unset): Master mac. If the device is not a member of stack, masterMac should be null
        device_series_type (int | Unset): DeviceSeriesType should be a value as follows: 0:advanced; 1:pro
        type_ (str | Unset): Type of device should be a value as follows: switch
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    status: int | Unset = UNSET
    support_cli: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    master_mac: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        ip = self.ip

        status = self.status

        support_cli = self.support_cli

        stack_id = self.stack_id

        stack_name = self.stack_name

        master_mac = self.master_mac

        device_series_type = self.device_series_type

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status is not UNSET:
            field_dict["status"] = status
        if support_cli is not UNSET:
            field_dict["supportCli"] = support_cli
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        status = d.pop("status", UNSET)

        support_cli = d.pop("supportCli", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        type_ = d.pop("type", UNSET)

        cli_device_list_vo = cls(
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            ip=ip,
            status=status,
            support_cli=support_cli,
            stack_id=stack_id,
            stack_name=stack_name,
            master_mac=master_mac,
            device_series_type=device_series_type,
            type_=type_,
        )

        cli_device_list_vo.additional_properties = d
        return cli_device_list_vo

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
