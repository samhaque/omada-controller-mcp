from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidsDataOpenApiVO")


@_attrs_define
class WidsDataOpenApiVO:
    """
    Attributes:
        station_mac (str | Unset): MAC address of the device that triggered the event.
        station_mac_list (list[str] | Unset): List of MAC addresses of the device that triggered the event.
        detect_mac (str | Unset): The Mac address of the AP that detects the event.
        channel (int | Unset): The Channel of the AP that detects the event.
        band (int | Unset): Channel band of the AP detecting the event (0:2.4g,1:5g, 2:5G,3:6g).
        start_time (int | Unset): Detection time.
        type_ (int | Unset): Detected event type.
        level (int | Unset): Detection event level (0:Alert,1:Major,2:Normal).
    """

    station_mac: str | Unset = UNSET
    station_mac_list: list[str] | Unset = UNSET
    detect_mac: str | Unset = UNSET
    channel: int | Unset = UNSET
    band: int | Unset = UNSET
    start_time: int | Unset = UNSET
    type_: int | Unset = UNSET
    level: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_mac = self.station_mac

        station_mac_list: list[str] | Unset = UNSET
        if not isinstance(self.station_mac_list, Unset):
            station_mac_list = self.station_mac_list

        detect_mac = self.detect_mac

        channel = self.channel

        band = self.band

        start_time = self.start_time

        type_ = self.type_

        level = self.level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if station_mac is not UNSET:
            field_dict["stationMac"] = station_mac
        if station_mac_list is not UNSET:
            field_dict["stationMacList"] = station_mac_list
        if detect_mac is not UNSET:
            field_dict["detectMac"] = detect_mac
        if channel is not UNSET:
            field_dict["channel"] = channel
        if band is not UNSET:
            field_dict["band"] = band
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if type_ is not UNSET:
            field_dict["type"] = type_
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        station_mac = d.pop("stationMac", UNSET)

        station_mac_list = cast(list[str], d.pop("stationMacList", UNSET))

        detect_mac = d.pop("detectMac", UNSET)

        channel = d.pop("channel", UNSET)

        band = d.pop("band", UNSET)

        start_time = d.pop("startTime", UNSET)

        type_ = d.pop("type", UNSET)

        level = d.pop("level", UNSET)

        wids_data_open_api_vo = cls(
            station_mac=station_mac,
            station_mac_list=station_mac_list,
            detect_mac=detect_mac,
            channel=channel,
            band=band,
            start_time=start_time,
            type_=type_,
            level=level,
        )

        wids_data_open_api_vo.additional_properties = d
        return wids_data_open_api_vo

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
