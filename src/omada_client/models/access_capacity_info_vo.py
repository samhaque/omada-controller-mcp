from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessCapacityInfoVO")


@_attrs_define
class AccessCapacityInfoVO:
    """
    Attributes:
        mac (str | Unset): Mac address
        ip (str | Unset): ip
        model (str | Unset): Device model name with version
        model_version (str | Unset): Model version of device, for example:3.0
        device_name (str | Unset): Device name
        device_type (str | Unset): Device type
        connection_client_count (int | Unset): The number of client connected to the device
    """

    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    connection_client_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        model = self.model

        model_version = self.model_version

        device_name = self.device_name

        device_type = self.device_type

        connection_client_count = self.connection_client_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if connection_client_count is not UNSET:
            field_dict["connectionClientCount"] = connection_client_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        connection_client_count = d.pop("connectionClientCount", UNSET)

        access_capacity_info_vo = cls(
            mac=mac,
            ip=ip,
            model=model,
            model_version=model_version,
            device_name=device_name,
            device_type=device_type,
            connection_client_count=connection_client_count,
        )

        access_capacity_info_vo.additional_properties = d
        return access_capacity_info_vo

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
