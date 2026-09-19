from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IotDeviceRadioInfoOpenApiVO")


@_attrs_define
class IotDeviceRadioInfoOpenApiVO:
    """
    Attributes:
        mac (str | Unset): Device mac
        name (str | Unset): Device name,default value is the mac address of device
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        ip (str | Unset): Device IP
        override (bool | Unset): Whether to override the configuration.
        transmit_power (int | Unset): Broadcast transmission power.<br />The parameter [transmitPower] should be a value
            as follows:[-20, -18, -15, -12, -10, -9, -6, -5, -3, 0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20].(0 by
            default)
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    ip: str | Unset = UNSET
    override: bool | Unset = UNSET
    transmit_power: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        status = self.status

        status_category = self.status_category

        ip = self.ip

        override = self.override

        transmit_power = self.transmit_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if ip is not UNSET:
            field_dict["ip"] = ip
        if override is not UNSET:
            field_dict["override"] = override
        if transmit_power is not UNSET:
            field_dict["transmitPower"] = transmit_power

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        ip = d.pop("ip", UNSET)

        override = d.pop("override", UNSET)

        transmit_power = d.pop("transmitPower", UNSET)

        iot_device_radio_info_open_api_vo = cls(
            mac=mac,
            name=name,
            type_=type_,
            model=model,
            model_version=model_version,
            status=status,
            status_category=status_category,
            ip=ip,
            override=override,
            transmit_power=transmit_power,
        )

        iot_device_radio_info_open_api_vo.additional_properties = d
        return iot_device_radio_info_open_api_vo

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
