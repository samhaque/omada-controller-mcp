from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WipsBlackListOpenApiVO")


@_attrs_define
class WipsBlackListOpenApiVO:
    """
    Attributes:
        station_mac (str | Unset): MAC address of the device that triggered the event.
        detect_mac (str | Unset): The Mac address of the AP that detects the event.
        time_stamp (int | Unset): Timestamp of the detected event.
    """

    station_mac: str | Unset = UNSET
    detect_mac: str | Unset = UNSET
    time_stamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_mac = self.station_mac

        detect_mac = self.detect_mac

        time_stamp = self.time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if station_mac is not UNSET:
            field_dict["stationMac"] = station_mac
        if detect_mac is not UNSET:
            field_dict["detectMac"] = detect_mac
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        station_mac = d.pop("stationMac", UNSET)

        detect_mac = d.pop("detectMac", UNSET)

        time_stamp = d.pop("timeStamp", UNSET)

        wips_black_list_open_api_vo = cls(
            station_mac=station_mac,
            detect_mac=detect_mac,
            time_stamp=time_stamp,
        )

        wips_black_list_open_api_vo.additional_properties = d
        return wips_black_list_open_api_vo

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
