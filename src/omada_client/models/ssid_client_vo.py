from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidClientVO")


@_attrs_define
class SsidClientVO:
    """
    Attributes:
        client_mac (str | Unset): Client Mac.
        name (str | Unset): Client Name, alias.
        client_model (str | Unset): Model of client device.
        client_type (str | Unset): Type of client device: iphone, ipod, android, pc, printer, tv...
        device_mac (str | Unset): Device Mac.
        device_name (str | Unset): Device Name.
        device_type (str | Unset): Type of the device that client is connected to.
        device_model (str | Unset): Model of the device that client is connected to.
        device_model_version (str | Unset): Model version of the device that client is connected to.
        ip (str | Unset): IP Address.
        down_traffic (int | Unset): Downstream traffic (Byte).
        up_traffic (int | Unset): Upstream traffic (Byte).
        traffic (int | Unset): Total traffic (Byte).
    """

    client_mac: str | Unset = UNSET
    name: str | Unset = UNSET
    client_model: str | Unset = UNSET
    client_type: str | Unset = UNSET
    device_mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_model: str | Unset = UNSET
    device_model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    down_traffic: int | Unset = UNSET
    up_traffic: int | Unset = UNSET
    traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_mac = self.client_mac

        name = self.name

        client_model = self.client_model

        client_type = self.client_type

        device_mac = self.device_mac

        device_name = self.device_name

        device_type = self.device_type

        device_model = self.device_model

        device_model_version = self.device_model_version

        ip = self.ip

        down_traffic = self.down_traffic

        up_traffic = self.up_traffic

        traffic = self.traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_mac is not UNSET:
            field_dict["clientMac"] = client_mac
        if name is not UNSET:
            field_dict["name"] = name
        if client_model is not UNSET:
            field_dict["clientModel"] = client_model
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if device_model_version is not UNSET:
            field_dict["deviceModelVersion"] = device_model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if down_traffic is not UNSET:
            field_dict["downTraffic"] = down_traffic
        if up_traffic is not UNSET:
            field_dict["upTraffic"] = up_traffic
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_mac = d.pop("clientMac", UNSET)

        name = d.pop("name", UNSET)

        client_model = d.pop("clientModel", UNSET)

        client_type = d.pop("clientType", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        device_model_version = d.pop("deviceModelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        down_traffic = d.pop("downTraffic", UNSET)

        up_traffic = d.pop("upTraffic", UNSET)

        traffic = d.pop("traffic", UNSET)

        ssid_client_vo = cls(
            client_mac=client_mac,
            name=name,
            client_model=client_model,
            client_type=client_type,
            device_mac=device_mac,
            device_name=device_name,
            device_type=device_type,
            device_model=device_model,
            device_model_version=device_model_version,
            ip=ip,
            down_traffic=down_traffic,
            up_traffic=up_traffic,
            traffic=traffic,
        )

        ssid_client_vo.additional_properties = d
        return ssid_client_vo

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
