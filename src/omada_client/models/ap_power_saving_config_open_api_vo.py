from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApPowerSavingConfigOpenApiVO")


@_attrs_define
class ApPowerSavingConfigOpenApiVO:
    """
    Attributes:
        mode (int | Unset): Power Saving Mode of device. 0: OFF, 1: Standard( based on the user‑specified time and/or
            band settings ), 2: Smart, 3: Deep Power‑Saving
        time_enable (bool | Unset): Power Saving trigger by time config status. True: enable, false: disable.
        start_time_h (int | Unset): Start time of trigger by time(unit: hour); It should be within the range of 0–23.
        start_time_m (int | Unset): Start time of trigger by time(unit: minute); It should be within the range of 0–59.
        end_time_h (int | Unset): End time of trigger by time(unit: hour); It should be within the range of 0–23.
        end_time_m (int | Unset): End time of trigger by time(unit: minute); It should be within the range of 0–59.
        band_enable (bool | Unset): Power Saving trigger by band config status. True: enable, false: disable.
        bands (list[int] | Unset): Select bands list config of trigger by band;It should be a value as follows: 0:
            2.4GHz; 1: 5GHz; 2: 5G2Hz; 3: 6GHz.
        idle_duration (int | Unset): Idle duration config of trigger by band.
        support_power_saving (bool | Unset): Indicates whether the device supports power saving. True: support, false:
            unSupport.
    """

    mode: int | Unset = UNSET
    time_enable: bool | Unset = UNSET
    start_time_h: int | Unset = UNSET
    start_time_m: int | Unset = UNSET
    end_time_h: int | Unset = UNSET
    end_time_m: int | Unset = UNSET
    band_enable: bool | Unset = UNSET
    bands: list[int] | Unset = UNSET
    idle_duration: int | Unset = UNSET
    support_power_saving: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        time_enable = self.time_enable

        start_time_h = self.start_time_h

        start_time_m = self.start_time_m

        end_time_h = self.end_time_h

        end_time_m = self.end_time_m

        band_enable = self.band_enable

        bands: list[int] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = self.bands

        idle_duration = self.idle_duration

        support_power_saving = self.support_power_saving

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if time_enable is not UNSET:
            field_dict["timeEnable"] = time_enable
        if start_time_h is not UNSET:
            field_dict["startTimeH"] = start_time_h
        if start_time_m is not UNSET:
            field_dict["startTimeM"] = start_time_m
        if end_time_h is not UNSET:
            field_dict["endTimeH"] = end_time_h
        if end_time_m is not UNSET:
            field_dict["endTimeM"] = end_time_m
        if band_enable is not UNSET:
            field_dict["bandEnable"] = band_enable
        if bands is not UNSET:
            field_dict["bands"] = bands
        if idle_duration is not UNSET:
            field_dict["idleDuration"] = idle_duration
        if support_power_saving is not UNSET:
            field_dict["supportPowerSaving"] = support_power_saving

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode", UNSET)

        time_enable = d.pop("timeEnable", UNSET)

        start_time_h = d.pop("startTimeH", UNSET)

        start_time_m = d.pop("startTimeM", UNSET)

        end_time_h = d.pop("endTimeH", UNSET)

        end_time_m = d.pop("endTimeM", UNSET)

        band_enable = d.pop("bandEnable", UNSET)

        bands = cast(list[int], d.pop("bands", UNSET))

        idle_duration = d.pop("idleDuration", UNSET)

        support_power_saving = d.pop("supportPowerSaving", UNSET)

        ap_power_saving_config_open_api_vo = cls(
            mode=mode,
            time_enable=time_enable,
            start_time_h=start_time_h,
            start_time_m=start_time_m,
            end_time_h=end_time_h,
            end_time_m=end_time_m,
            band_enable=band_enable,
            bands=bands,
            idle_duration=idle_duration,
            support_power_saving=support_power_saving,
        )

        ap_power_saving_config_open_api_vo.additional_properties = d
        return ap_power_saving_config_open_api_vo

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
