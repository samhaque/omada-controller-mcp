from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wireless_traffic_trend_vo import WirelessTrafficTrendVO


T = TypeVar("T", bound="WirelessTrafficSingleVO")


@_attrs_define
class WirelessTrafficSingleVO:
    """
    Attributes:
        total_traffic (int | Unset): total traffic
        rx_traffic (int | Unset): client rx traffic
        tx_traffic (int | Unset): client tx traffic
        traffic_trend (list[WirelessTrafficTrendVO] | Unset):
    """

    total_traffic: int | Unset = UNSET
    rx_traffic: int | Unset = UNSET
    tx_traffic: int | Unset = UNSET
    traffic_trend: list[WirelessTrafficTrendVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_traffic = self.total_traffic

        rx_traffic = self.rx_traffic

        tx_traffic = self.tx_traffic

        traffic_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traffic_trend, Unset):
            traffic_trend = []
            for traffic_trend_item_data in self.traffic_trend:
                traffic_trend_item = traffic_trend_item_data.to_dict()
                traffic_trend.append(traffic_trend_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if rx_traffic is not UNSET:
            field_dict["rxTraffic"] = rx_traffic
        if tx_traffic is not UNSET:
            field_dict["txTraffic"] = tx_traffic
        if traffic_trend is not UNSET:
            field_dict["trafficTrend"] = traffic_trend

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wireless_traffic_trend_vo import (
            WirelessTrafficTrendVO,
        )

        d = dict(src_dict)
        total_traffic = d.pop("totalTraffic", UNSET)

        rx_traffic = d.pop("rxTraffic", UNSET)

        tx_traffic = d.pop("txTraffic", UNSET)

        _traffic_trend = d.pop("trafficTrend", UNSET)
        traffic_trend: list[WirelessTrafficTrendVO] | Unset = UNSET
        if _traffic_trend is not UNSET:
            traffic_trend = []
            for traffic_trend_item_data in _traffic_trend:
                traffic_trend_item = WirelessTrafficTrendVO.from_dict(
                    traffic_trend_item_data
                )

                traffic_trend.append(traffic_trend_item)

        wireless_traffic_single_vo = cls(
            total_traffic=total_traffic,
            rx_traffic=rx_traffic,
            tx_traffic=tx_traffic,
            traffic_trend=traffic_trend,
        )

        wireless_traffic_single_vo.additional_properties = d
        return wireless_traffic_single_vo

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
