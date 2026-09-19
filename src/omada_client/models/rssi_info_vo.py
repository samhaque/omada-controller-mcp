from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RssiInfoVO")


@_attrs_define
class RssiInfoVO:
    """
    Attributes:
        mac (str | Unset): Mac address
        ip (str | Unset): ip
        client_name (str | Unset): Client name
        device_type (str | Unset): Client-connected device type
        client_type (str | Unset): Client type for icon display (e.g. Mobile, Laptop, IPC)
        client_model (str | Unset): Client model for icon display
        connect_device_name (str | Unset): Client-connected device name
        connect_device_mac (str | Unset): Client-connected device mac
        ssid (str | Unset): ssid
        rssi (int | Unset): rssi
    """

    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    client_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    client_type: str | Unset = UNSET
    client_model: str | Unset = UNSET
    connect_device_name: str | Unset = UNSET
    connect_device_mac: str | Unset = UNSET
    ssid: str | Unset = UNSET
    rssi: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        client_name = self.client_name

        device_type = self.device_type

        client_type = self.client_type

        client_model = self.client_model

        connect_device_name = self.connect_device_name

        connect_device_mac = self.connect_device_mac

        ssid = self.ssid

        rssi = self.rssi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if client_model is not UNSET:
            field_dict["clientModel"] = client_model
        if connect_device_name is not UNSET:
            field_dict["connectDeviceName"] = connect_device_name
        if connect_device_mac is not UNSET:
            field_dict["connectDeviceMac"] = connect_device_mac
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if rssi is not UNSET:
            field_dict["rssi"] = rssi

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        client_name = d.pop("clientName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        client_type = d.pop("clientType", UNSET)

        client_model = d.pop("clientModel", UNSET)

        connect_device_name = d.pop("connectDeviceName", UNSET)

        connect_device_mac = d.pop("connectDeviceMac", UNSET)

        ssid = d.pop("ssid", UNSET)

        rssi = d.pop("rssi", UNSET)

        rssi_info_vo = cls(
            mac=mac,
            ip=ip,
            client_name=client_name,
            device_type=device_type,
            client_type=client_type,
            client_model=client_model,
            connect_device_name=connect_device_name,
            connect_device_mac=connect_device_mac,
            ssid=ssid,
            rssi=rssi,
        )

        rssi_info_vo.additional_properties = d
        return rssi_info_vo

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
