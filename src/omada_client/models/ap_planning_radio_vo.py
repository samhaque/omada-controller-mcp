from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApPlanningRadioVO")


@_attrs_define
class ApPlanningRadioVO:
    """Optimization results in band 6 GHz.

    Attributes:
        orig_chan (str | Unset): The original channel.
        rcmd_chan (str | Unset): Channel recommended by the algorithm.
        orig_chan_width (str | Unset): The original channel width.
        rcmd_chan_width (str | Unset): Channel width recommended by the algorithm.
        orig_power (int | Unset): The original power value.
        rcmd_power (int | Unset): Power value recommended by the algorithm.
        orig_band (int | Unset): The original switch status of band. 0: off, 1: on.
        rcmd_band (int | Unset): Band switch status recommended by the algorithm. 0: off, 1: on.
        err_code (int | Unset): Error code returned by the algorithm. 0: OK. -34820: The configured bandwidth has no
            optional channel. -34821: The lowest power supported by this device is out of the configured Power Range.
            -34822: The highest power supported by this device is out of the configured Power Range. -34815: Failed to
            optimize device because of no scan result. -34816: Failed to apply deploy config because of this device is not
            connected. -34823: Cannot optimize the channels because you have excluded them.
    """

    orig_chan: str | Unset = UNSET
    rcmd_chan: str | Unset = UNSET
    orig_chan_width: str | Unset = UNSET
    rcmd_chan_width: str | Unset = UNSET
    orig_power: int | Unset = UNSET
    rcmd_power: int | Unset = UNSET
    orig_band: int | Unset = UNSET
    rcmd_band: int | Unset = UNSET
    err_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orig_chan = self.orig_chan

        rcmd_chan = self.rcmd_chan

        orig_chan_width = self.orig_chan_width

        rcmd_chan_width = self.rcmd_chan_width

        orig_power = self.orig_power

        rcmd_power = self.rcmd_power

        orig_band = self.orig_band

        rcmd_band = self.rcmd_band

        err_code = self.err_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orig_chan is not UNSET:
            field_dict["origChan"] = orig_chan
        if rcmd_chan is not UNSET:
            field_dict["rcmdChan"] = rcmd_chan
        if orig_chan_width is not UNSET:
            field_dict["origChanWidth"] = orig_chan_width
        if rcmd_chan_width is not UNSET:
            field_dict["rcmdChanWidth"] = rcmd_chan_width
        if orig_power is not UNSET:
            field_dict["origPower"] = orig_power
        if rcmd_power is not UNSET:
            field_dict["rcmdPower"] = rcmd_power
        if orig_band is not UNSET:
            field_dict["origBand"] = orig_band
        if rcmd_band is not UNSET:
            field_dict["rcmdBand"] = rcmd_band
        if err_code is not UNSET:
            field_dict["errCode"] = err_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        orig_chan = d.pop("origChan", UNSET)

        rcmd_chan = d.pop("rcmdChan", UNSET)

        orig_chan_width = d.pop("origChanWidth", UNSET)

        rcmd_chan_width = d.pop("rcmdChanWidth", UNSET)

        orig_power = d.pop("origPower", UNSET)

        rcmd_power = d.pop("rcmdPower", UNSET)

        orig_band = d.pop("origBand", UNSET)

        rcmd_band = d.pop("rcmdBand", UNSET)

        err_code = d.pop("errCode", UNSET)

        ap_planning_radio_vo = cls(
            orig_chan=orig_chan,
            rcmd_chan=rcmd_chan,
            orig_chan_width=orig_chan_width,
            rcmd_chan_width=rcmd_chan_width,
            orig_power=orig_power,
            rcmd_power=rcmd_power,
            orig_band=orig_band,
            rcmd_band=rcmd_band,
            err_code=err_code,
        )

        ap_planning_radio_vo.additional_properties = d
        return ap_planning_radio_vo

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
