from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InfluencingDeviceVO")


@_attrs_define
class InfluencingDeviceVO:
    """
    Attributes:
        mac (str | Unset): MAC address of the device
        device_name (str | Unset): Display name of the device
        device_type (str | Unset): Device type (e.g. ap, gateway, switch)
        model (str | Unset): Device model (e.g. EAP225)
        model_version (str | Unset): Device model version (e.g. 3.0)
        ip (str | Unset): IP address of the device
        status (int | Unset): Device status
        health (int | Unset): Device health score
    """

    mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    status: int | Unset = UNSET
    health: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        device_name = self.device_name

        device_type = self.device_type

        model = self.model

        model_version = self.model_version

        ip = self.ip

        status = self.status

        health = self.health

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status is not UNSET:
            field_dict["status"] = status
        if health is not UNSET:
            field_dict["health"] = health

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        status = d.pop("status", UNSET)

        health = d.pop("health", UNSET)

        influencing_device_vo = cls(
            mac=mac,
            device_name=device_name,
            device_type=device_type,
            model=model,
            model_version=model_version,
            ip=ip,
            status=status,
            health=health,
        )

        influencing_device_vo.additional_properties = d
        return influencing_device_vo

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
