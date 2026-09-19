from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessTrafficTrendVO")


@_attrs_define
class WirelessTrafficTrendVO:
    """
    Attributes:
        time (int | Unset): time
        total_traffic (int | Unset): total traffic
        rx_traffic (int | Unset): client rx traffic
        tx_traffic (int | Unset): client tx traffic
        wireless_count (int | Unset): number of wireless device
        wired_count (int | Unset): number of wired device
    """

    time: int | Unset = UNSET
    total_traffic: int | Unset = UNSET
    rx_traffic: int | Unset = UNSET
    tx_traffic: int | Unset = UNSET
    wireless_count: int | Unset = UNSET
    wired_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        total_traffic = self.total_traffic

        rx_traffic = self.rx_traffic

        tx_traffic = self.tx_traffic

        wireless_count = self.wireless_count

        wired_count = self.wired_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if rx_traffic is not UNSET:
            field_dict["rxTraffic"] = rx_traffic
        if tx_traffic is not UNSET:
            field_dict["txTraffic"] = tx_traffic
        if wireless_count is not UNSET:
            field_dict["wirelessCount"] = wireless_count
        if wired_count is not UNSET:
            field_dict["wiredCount"] = wired_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        rx_traffic = d.pop("rxTraffic", UNSET)

        tx_traffic = d.pop("txTraffic", UNSET)

        wireless_count = d.pop("wirelessCount", UNSET)

        wired_count = d.pop("wiredCount", UNSET)

        wireless_traffic_trend_vo = cls(
            time=time,
            total_traffic=total_traffic,
            rx_traffic=rx_traffic,
            tx_traffic=tx_traffic,
            wireless_count=wireless_count,
            wired_count=wired_count,
        )

        wireless_traffic_trend_vo.additional_properties = d
        return wireless_traffic_trend_vo

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
