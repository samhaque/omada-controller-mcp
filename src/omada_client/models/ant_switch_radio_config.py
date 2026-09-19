from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AntSwitchRadioConfig")


@_attrs_define
class AntSwitchRadioConfig:
    """
    Attributes:
        ant_mode (int | Unset): antenna mode in radio setting. 0:Auto, 1: Built-In, 2: Omni
        ant_gain (int | Unset): antenna Gain
    """

    ant_mode: int | Unset = UNSET
    ant_gain: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ant_mode = self.ant_mode

        ant_gain = self.ant_gain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ant_mode is not UNSET:
            field_dict["antMode"] = ant_mode
        if ant_gain is not UNSET:
            field_dict["antGain"] = ant_gain

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ant_mode = d.pop("antMode", UNSET)

        ant_gain = d.pop("antGain", UNSET)

        ant_switch_radio_config = cls(
            ant_mode=ant_mode,
            ant_gain=ant_gain,
        )

        ant_switch_radio_config.additional_properties = d
        return ant_switch_radio_config

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
