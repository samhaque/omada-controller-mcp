from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelUtilInfoVO")


@_attrs_define
class ChannelUtilInfoVO:
    """
    Attributes:
        mac (str | Unset): Mac address
        ip (str | Unset): ip
        model (str | Unset): Device model name with version
        model_version (str | Unset): Model version of device, for example:3.0
        device_name (str | Unset): Device name
        device_type (str | Unset): Device type
        channel_util (int | Unset): Channel utilization rate
        channel_util_2_g (int | Unset): Channel 2g utilization rate
        channel_util_5_g (int | Unset): Channel 5g utilization rate
        channel_util_6_g (int | Unset): Channel 6g utilization rate
    """

    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    channel_util: int | Unset = UNSET
    channel_util_2_g: int | Unset = UNSET
    channel_util_5_g: int | Unset = UNSET
    channel_util_6_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        model = self.model

        model_version = self.model_version

        device_name = self.device_name

        device_type = self.device_type

        channel_util = self.channel_util

        channel_util_2_g = self.channel_util_2_g

        channel_util_5_g = self.channel_util_5_g

        channel_util_6_g = self.channel_util_6_g

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
        if channel_util is not UNSET:
            field_dict["channelUtil"] = channel_util
        if channel_util_2_g is not UNSET:
            field_dict["channelUtil2g"] = channel_util_2_g
        if channel_util_5_g is not UNSET:
            field_dict["channelUtil5g"] = channel_util_5_g
        if channel_util_6_g is not UNSET:
            field_dict["channelUtil6g"] = channel_util_6_g

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

        channel_util = d.pop("channelUtil", UNSET)

        channel_util_2_g = d.pop("channelUtil2g", UNSET)

        channel_util_5_g = d.pop("channelUtil5g", UNSET)

        channel_util_6_g = d.pop("channelUtil6g", UNSET)

        channel_util_info_vo = cls(
            mac=mac,
            ip=ip,
            model=model,
            model_version=model_version,
            device_name=device_name,
            device_type=device_type,
            channel_util=channel_util,
            channel_util_2_g=channel_util_2_g,
            channel_util_5_g=channel_util_5_g,
            channel_util_6_g=channel_util_6_g,
        )

        channel_util_info_vo.additional_properties = d
        return channel_util_info_vo

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
