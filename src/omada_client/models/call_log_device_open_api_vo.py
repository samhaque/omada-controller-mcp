from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallLogDeviceOpenApiVO")


@_attrs_define
class CallLogDeviceOpenApiVO:
    """The telephonyDevice description of callLog.

    Attributes:
        device_name (str | Unset): The device name of callLog.
        device_mac (str | Unset): The device mac name of callLog.
        model (str | Unset): The device model of callLog.
        model_version (str | Unset): The device modelVersion of callLog.
        type_ (str | Unset): The device type of callLog.
    """

    device_name: str | Unset = UNSET
    device_mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        device_mac = self.device_mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_name = d.pop("deviceName", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        call_log_device_open_api_vo = cls(
            device_name=device_name,
            device_mac=device_mac,
            model=model,
            model_version=model_version,
            type_=type_,
        )

        call_log_device_open_api_vo.additional_properties = d
        return call_log_device_open_api_vo

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
