from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.traffic_summary_list_vo import TrafficSummaryListVO


T = TypeVar("T", bound="TrafficSummaryVO")


@_attrs_define
class TrafficSummaryVO:
    """
    Attributes:
        total_traffic (int | Unset): total traffic
        tx_traffic (int | Unset): tx traffic
        rx_traffic (int | Unset): rx traffic
        traffic_summary (list[TrafficSummaryListVO] | Unset): traffic data point
    """

    total_traffic: int | Unset = UNSET
    tx_traffic: int | Unset = UNSET
    rx_traffic: int | Unset = UNSET
    traffic_summary: list[TrafficSummaryListVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_traffic = self.total_traffic

        tx_traffic = self.tx_traffic

        rx_traffic = self.rx_traffic

        traffic_summary: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traffic_summary, Unset):
            traffic_summary = []
            for traffic_summary_item_data in self.traffic_summary:
                traffic_summary_item = traffic_summary_item_data.to_dict()
                traffic_summary.append(traffic_summary_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if tx_traffic is not UNSET:
            field_dict["txTraffic"] = tx_traffic
        if rx_traffic is not UNSET:
            field_dict["rxTraffic"] = rx_traffic
        if traffic_summary is not UNSET:
            field_dict["trafficSummary"] = traffic_summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.traffic_summary_list_vo import (
            TrafficSummaryListVO,
        )

        d = dict(src_dict)
        total_traffic = d.pop("totalTraffic", UNSET)

        tx_traffic = d.pop("txTraffic", UNSET)

        rx_traffic = d.pop("rxTraffic", UNSET)

        _traffic_summary = d.pop("trafficSummary", UNSET)
        traffic_summary: list[TrafficSummaryListVO] | Unset = UNSET
        if _traffic_summary is not UNSET:
            traffic_summary = []
            for traffic_summary_item_data in _traffic_summary:
                traffic_summary_item = TrafficSummaryListVO.from_dict(
                    traffic_summary_item_data
                )

                traffic_summary.append(traffic_summary_item)

        traffic_summary_vo = cls(
            total_traffic=total_traffic,
            tx_traffic=tx_traffic,
            rx_traffic=rx_traffic,
            traffic_summary=traffic_summary,
        )

        traffic_summary_vo.additional_properties = d
        return traffic_summary_vo

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
