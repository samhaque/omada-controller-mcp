from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AntSettingVO")


@_attrs_define
class AntSettingVO:
    """Antenna Setting in radio 6g.

    Attributes:
        ant_mode (int | Unset): antenna mode
        ant_gain (int | Unset): antenna gain
        ant_pattern (int | Unset): antenna pattern,0 is built-In and 1 is External.
        custom_gain_limit (int | Unset): custom antMode max antenna gain.
        default_omni_gain (int | Unset): default Omni Antenna Mode gain.
    """

    ant_mode: int | Unset = UNSET
    ant_gain: int | Unset = UNSET
    ant_pattern: int | Unset = UNSET
    custom_gain_limit: int | Unset = UNSET
    default_omni_gain: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ant_mode = self.ant_mode

        ant_gain = self.ant_gain

        ant_pattern = self.ant_pattern

        custom_gain_limit = self.custom_gain_limit

        default_omni_gain = self.default_omni_gain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ant_mode is not UNSET:
            field_dict["antMode"] = ant_mode
        if ant_gain is not UNSET:
            field_dict["antGain"] = ant_gain
        if ant_pattern is not UNSET:
            field_dict["antPattern"] = ant_pattern
        if custom_gain_limit is not UNSET:
            field_dict["customGainLimit"] = custom_gain_limit
        if default_omni_gain is not UNSET:
            field_dict["defaultOmniGain"] = default_omni_gain

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ant_mode = d.pop("antMode", UNSET)

        ant_gain = d.pop("antGain", UNSET)

        ant_pattern = d.pop("antPattern", UNSET)

        custom_gain_limit = d.pop("customGainLimit", UNSET)

        default_omni_gain = d.pop("defaultOmniGain", UNSET)

        ant_setting_vo = cls(
            ant_mode=ant_mode,
            ant_gain=ant_gain,
            ant_pattern=ant_pattern,
            custom_gain_limit=custom_gain_limit,
            default_omni_gain=default_omni_gain,
        )

        ant_setting_vo.additional_properties = d
        return ant_setting_vo

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
