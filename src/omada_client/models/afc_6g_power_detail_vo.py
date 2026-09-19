from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Afc6GPowerDetailVO")


@_attrs_define
class Afc6GPowerDetailVO:
    """
    Attributes:
        value (int | Unset):
        channel_width (int | Unset):
        max_pow (int | Unset):
        min_pow (int | Unset):
        power_mode (bool | Unset):
        channel_value (int | Unset):
    """

    value: int | Unset = UNSET
    channel_width: int | Unset = UNSET
    max_pow: int | Unset = UNSET
    min_pow: int | Unset = UNSET
    power_mode: bool | Unset = UNSET
    channel_value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        channel_width = self.channel_width

        max_pow = self.max_pow

        min_pow = self.min_pow

        power_mode = self.power_mode

        channel_value = self.channel_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if channel_width is not UNSET:
            field_dict["channelWidth"] = channel_width
        if max_pow is not UNSET:
            field_dict["maxPow"] = max_pow
        if min_pow is not UNSET:
            field_dict["minPow"] = min_pow
        if power_mode is not UNSET:
            field_dict["powerMode"] = power_mode
        if channel_value is not UNSET:
            field_dict["channelValue"] = channel_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        channel_width = d.pop("channelWidth", UNSET)

        max_pow = d.pop("maxPow", UNSET)

        min_pow = d.pop("minPow", UNSET)

        power_mode = d.pop("powerMode", UNSET)

        channel_value = d.pop("channelValue", UNSET)

        afc_6g_power_detail_vo = cls(
            value=value,
            channel_width=channel_width,
            max_pow=max_pow,
            min_pow=min_pow,
            power_mode=power_mode,
            channel_value=channel_value,
        )

        afc_6g_power_detail_vo.additional_properties = d
        return afc_6g_power_detail_vo

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
