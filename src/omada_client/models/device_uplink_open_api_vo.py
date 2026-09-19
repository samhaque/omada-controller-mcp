from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceUplinkOpenApiVO")


@_attrs_define
class DeviceUplinkOpenApiVO:
    """
    Attributes:
        mac (str | Unset): Current Device MAC
        uplink_device_mac (str | Unset): Uplink device mac
        uplink_device_name (str | Unset): Uplink device name
        uplink_device_port (str | Unset): Uplink device port
        link_speed (int | Unset): Device uplink port linkSpeed, linkSpeed should be a value as follows: 0: Auto; 1: 10M;
            2: 100M; 3: 1000M; 4: 2500M; 5: 10G; 6: 5G; 7: 25G, 8: 100G.
        duplex (int | Unset): Device uplink port duplex mode, duplex should be a value as follows: 0: Auto; 1: Half; 2:
            Full.
    """

    mac: str | Unset = UNSET
    uplink_device_mac: str | Unset = UNSET
    uplink_device_name: str | Unset = UNSET
    uplink_device_port: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        uplink_device_mac = self.uplink_device_mac

        uplink_device_name = self.uplink_device_name

        uplink_device_port = self.uplink_device_port

        link_speed = self.link_speed

        duplex = self.duplex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        uplink_device_mac = d.pop("uplinkDeviceMac", UNSET)

        uplink_device_name = d.pop("uplinkDeviceName", UNSET)

        uplink_device_port = d.pop("uplinkDevicePort", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        device_uplink_open_api_vo = cls(
            mac=mac,
            uplink_device_mac=uplink_device_mac,
            uplink_device_name=uplink_device_name,
            uplink_device_port=uplink_device_port,
            link_speed=link_speed,
            duplex=duplex,
        )

        device_uplink_open_api_vo.additional_properties = d
        return device_uplink_open_api_vo

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
