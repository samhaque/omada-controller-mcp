from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BeaconControlOpenApiVO")


@_attrs_define
class BeaconControlOpenApiVO:
    """Site beacon control setting.

    Attributes:
        dtim_period_2_g (int): 2.4GHz DTIM period, parameter dtimPeriod2g should be within the range of 1-255
        rts_threshold_2_g (int): 2.4GHz RTS threshold, parameter rtsThreshold2g should be within the range of 1-2347
        dtim_period_5_g (int): 5GHz DTIM period, parameter dtimPeriod5g should be within the range of 1-255
        rts_threshold_5_g (int): 5GHz RTS threshold, parameter rtsThreshold5g should be within the range of 1-2347
        dtim_period_6_g (int): 6GHz DTIM period, parameter dtimPeriod6g should be within the range of 1-255
        rts_threshold_6_g (int): 6GHz RTS threshold, parameter rtsThreshold6g should be within the range of 1-2347
        beacon_interval_2_g (int | Unset): 2.4GHz beacon interval, parameter beaconInterval2g should be within the range
            of 40-500)
        beacon_intv_mode_2_g (int | Unset): Configuration for Beacon Interval Mode in the 2G Band:0: Auto 1: Custom
        beacon_interval_5_g (int | Unset): 5GHz beacon interval, parameter beaconInterval5g should be within the range
            of 40-500)
        beacon_intv_mode_5_g (int | Unset): Configuration for Beacon Interval Mode in the 5G Band:0: Auto 1: Custom
        beacon_interval_6_g (int | Unset): 6GHz beacon interval, parameter beaconInterval6g should be within the range
            of 40-500)
        beacon_intv_mode_6_g (int | Unset): 6g band Beacon Interval mode: 0-auto, 1-custom
    """

    dtim_period_2_g: int
    rts_threshold_2_g: int
    dtim_period_5_g: int
    rts_threshold_5_g: int
    dtim_period_6_g: int
    rts_threshold_6_g: int
    beacon_interval_2_g: int | Unset = UNSET
    beacon_intv_mode_2_g: int | Unset = UNSET
    beacon_interval_5_g: int | Unset = UNSET
    beacon_intv_mode_5_g: int | Unset = UNSET
    beacon_interval_6_g: int | Unset = UNSET
    beacon_intv_mode_6_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dtim_period_2_g = self.dtim_period_2_g

        rts_threshold_2_g = self.rts_threshold_2_g

        dtim_period_5_g = self.dtim_period_5_g

        rts_threshold_5_g = self.rts_threshold_5_g

        dtim_period_6_g = self.dtim_period_6_g

        rts_threshold_6_g = self.rts_threshold_6_g

        beacon_interval_2_g = self.beacon_interval_2_g

        beacon_intv_mode_2_g = self.beacon_intv_mode_2_g

        beacon_interval_5_g = self.beacon_interval_5_g

        beacon_intv_mode_5_g = self.beacon_intv_mode_5_g

        beacon_interval_6_g = self.beacon_interval_6_g

        beacon_intv_mode_6_g = self.beacon_intv_mode_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dtimPeriod2g": dtim_period_2_g,
                "rtsThreshold2g": rts_threshold_2_g,
                "dtimPeriod5g": dtim_period_5_g,
                "rtsThreshold5g": rts_threshold_5_g,
                "dtimPeriod6g": dtim_period_6_g,
                "rtsThreshold6g": rts_threshold_6_g,
            }
        )
        if beacon_interval_2_g is not UNSET:
            field_dict["beaconInterval2g"] = beacon_interval_2_g
        if beacon_intv_mode_2_g is not UNSET:
            field_dict["beaconIntvMode2g"] = beacon_intv_mode_2_g
        if beacon_interval_5_g is not UNSET:
            field_dict["beaconInterval5g"] = beacon_interval_5_g
        if beacon_intv_mode_5_g is not UNSET:
            field_dict["beaconIntvMode5g"] = beacon_intv_mode_5_g
        if beacon_interval_6_g is not UNSET:
            field_dict["beaconInterval6g"] = beacon_interval_6_g
        if beacon_intv_mode_6_g is not UNSET:
            field_dict["beaconIntvMode6g"] = beacon_intv_mode_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dtim_period_2_g = d.pop("dtimPeriod2g")

        rts_threshold_2_g = d.pop("rtsThreshold2g")

        dtim_period_5_g = d.pop("dtimPeriod5g")

        rts_threshold_5_g = d.pop("rtsThreshold5g")

        dtim_period_6_g = d.pop("dtimPeriod6g")

        rts_threshold_6_g = d.pop("rtsThreshold6g")

        beacon_interval_2_g = d.pop("beaconInterval2g", UNSET)

        beacon_intv_mode_2_g = d.pop("beaconIntvMode2g", UNSET)

        beacon_interval_5_g = d.pop("beaconInterval5g", UNSET)

        beacon_intv_mode_5_g = d.pop("beaconIntvMode5g", UNSET)

        beacon_interval_6_g = d.pop("beaconInterval6g", UNSET)

        beacon_intv_mode_6_g = d.pop("beaconIntvMode6g", UNSET)

        beacon_control_open_api_vo = cls(
            dtim_period_2_g=dtim_period_2_g,
            rts_threshold_2_g=rts_threshold_2_g,
            dtim_period_5_g=dtim_period_5_g,
            rts_threshold_5_g=rts_threshold_5_g,
            dtim_period_6_g=dtim_period_6_g,
            rts_threshold_6_g=rts_threshold_6_g,
            beacon_interval_2_g=beacon_interval_2_g,
            beacon_intv_mode_2_g=beacon_intv_mode_2_g,
            beacon_interval_5_g=beacon_interval_5_g,
            beacon_intv_mode_5_g=beacon_intv_mode_5_g,
            beacon_interval_6_g=beacon_interval_6_g,
            beacon_intv_mode_6_g=beacon_intv_mode_6_g,
        )

        beacon_control_open_api_vo.additional_properties = d
        return beacon_control_open_api_vo

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
