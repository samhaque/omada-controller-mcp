from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChildApOpenApiVO")


@_attrs_define
class ChildApOpenApiVO:
    """List of child aps

    Attributes:
        mac (str | Unset): parent ap mac
        name (str | Unset): parent ap name
        rssi (int | Unset): rssi
        model (str | Unset): model
        model_version (str | Unset): model version
        ip (str | Unset): ip
        device_series_type (int | Unset): 0-advanced; 1-pro
        support_speed_test (bool | Unset): bridge device support speed test
        type_ (str | Unset): device type
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    rssi: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    support_speed_test: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        rssi = self.rssi

        model = self.model

        model_version = self.model_version

        ip = self.ip

        device_series_type = self.device_series_type

        support_speed_test = self.support_speed_test

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if support_speed_test is not UNSET:
            field_dict["supportSpeedTest"] = support_speed_test
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        rssi = d.pop("rssi", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        support_speed_test = d.pop("supportSpeedTest", UNSET)

        type_ = d.pop("type", UNSET)

        child_ap_open_api_vo = cls(
            mac=mac,
            name=name,
            rssi=rssi,
            model=model,
            model_version=model_version,
            ip=ip,
            device_series_type=device_series_type,
            support_speed_test=support_speed_test,
            type_=type_,
        )

        child_ap_open_api_vo.additional_properties = d
        return child_ap_open_api_vo

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
