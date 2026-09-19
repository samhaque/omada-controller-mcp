from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelInterInfoVO")


@_attrs_define
class ChannelInterInfoVO:
    """
    Attributes:
        mac (str | Unset): Mac address
        ip (str | Unset): ip
        model (str | Unset): Device model name with version
        model_version (str | Unset): Model version of device, for example:3.0
        device_name (str | Unset): Device name
        device_type (str | Unset): Device type
        channel_interf (int | Unset): Channel interference rate
        channel_interf_2_g (int | Unset): Channel interference rate
        channel_interf_5_g (int | Unset): Channel interference rate
        channel_interf_6_g (int | Unset): Channel interference rate
        noise_floor_2_g (int | Unset): Noise floor of 2.4g
        noise_floor_5_g (int | Unset): Noise floor of 5g
        noise_floor_6_g (int | Unset): Noise floor of 6g
    """

    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    channel_interf: int | Unset = UNSET
    channel_interf_2_g: int | Unset = UNSET
    channel_interf_5_g: int | Unset = UNSET
    channel_interf_6_g: int | Unset = UNSET
    noise_floor_2_g: int | Unset = UNSET
    noise_floor_5_g: int | Unset = UNSET
    noise_floor_6_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        model = self.model

        model_version = self.model_version

        device_name = self.device_name

        device_type = self.device_type

        channel_interf = self.channel_interf

        channel_interf_2_g = self.channel_interf_2_g

        channel_interf_5_g = self.channel_interf_5_g

        channel_interf_6_g = self.channel_interf_6_g

        noise_floor_2_g = self.noise_floor_2_g

        noise_floor_5_g = self.noise_floor_5_g

        noise_floor_6_g = self.noise_floor_6_g

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
        if channel_interf is not UNSET:
            field_dict["channelInterf"] = channel_interf
        if channel_interf_2_g is not UNSET:
            field_dict["channelInterf2g"] = channel_interf_2_g
        if channel_interf_5_g is not UNSET:
            field_dict["channelInterf5g"] = channel_interf_5_g
        if channel_interf_6_g is not UNSET:
            field_dict["channelInterf6g"] = channel_interf_6_g
        if noise_floor_2_g is not UNSET:
            field_dict["noiseFloor2g"] = noise_floor_2_g
        if noise_floor_5_g is not UNSET:
            field_dict["noiseFloor5g"] = noise_floor_5_g
        if noise_floor_6_g is not UNSET:
            field_dict["noiseFloor6g"] = noise_floor_6_g

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

        channel_interf = d.pop("channelInterf", UNSET)

        channel_interf_2_g = d.pop("channelInterf2g", UNSET)

        channel_interf_5_g = d.pop("channelInterf5g", UNSET)

        channel_interf_6_g = d.pop("channelInterf6g", UNSET)

        noise_floor_2_g = d.pop("noiseFloor2g", UNSET)

        noise_floor_5_g = d.pop("noiseFloor5g", UNSET)

        noise_floor_6_g = d.pop("noiseFloor6g", UNSET)

        channel_inter_info_vo = cls(
            mac=mac,
            ip=ip,
            model=model,
            model_version=model_version,
            device_name=device_name,
            device_type=device_type,
            channel_interf=channel_interf,
            channel_interf_2_g=channel_interf_2_g,
            channel_interf_5_g=channel_interf_5_g,
            channel_interf_6_g=channel_interf_6_g,
            noise_floor_2_g=noise_floor_2_g,
            noise_floor_5_g=noise_floor_5_g,
            noise_floor_6_g=noise_floor_6_g,
        )

        channel_inter_info_vo.additional_properties = d
        return channel_inter_info_vo

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
