from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wireless_summary_vo import WirelessSummaryVO
    from ..models.wireless_traffic_trend_vo import WirelessTrafficTrendVO


T = TypeVar("T", bound="WirelessTrafficVO")


@_attrs_define
class WirelessTrafficVO:
    """
    Attributes:
        wireless_summary (WirelessSummaryVO | Unset):
        wireless_2_g_traffic (list[WirelessTrafficTrendVO] | Unset):
        wireless_5_g_traffic (list[WirelessTrafficTrendVO] | Unset):
        wireless_6_g_traffic (list[WirelessTrafficTrendVO] | Unset):
        total_traffic (list[WirelessTrafficTrendVO] | Unset):
    """

    wireless_summary: WirelessSummaryVO | Unset = UNSET
    wireless_2_g_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
    wireless_5_g_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
    wireless_6_g_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
    total_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wireless_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_summary, Unset):
            wireless_summary = self.wireless_summary.to_dict()

        wireless_2_g_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wireless_2_g_traffic, Unset):
            wireless_2_g_traffic = []
            for wireless_2_g_traffic_item_data in self.wireless_2_g_traffic:
                wireless_2_g_traffic_item = wireless_2_g_traffic_item_data.to_dict()
                wireless_2_g_traffic.append(wireless_2_g_traffic_item)

        wireless_5_g_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wireless_5_g_traffic, Unset):
            wireless_5_g_traffic = []
            for wireless_5_g_traffic_item_data in self.wireless_5_g_traffic:
                wireless_5_g_traffic_item = wireless_5_g_traffic_item_data.to_dict()
                wireless_5_g_traffic.append(wireless_5_g_traffic_item)

        wireless_6_g_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wireless_6_g_traffic, Unset):
            wireless_6_g_traffic = []
            for wireless_6_g_traffic_item_data in self.wireless_6_g_traffic:
                wireless_6_g_traffic_item = wireless_6_g_traffic_item_data.to_dict()
                wireless_6_g_traffic.append(wireless_6_g_traffic_item)

        total_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total_traffic, Unset):
            total_traffic = []
            for total_traffic_item_data in self.total_traffic:
                total_traffic_item = total_traffic_item_data.to_dict()
                total_traffic.append(total_traffic_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wireless_summary is not UNSET:
            field_dict["wirelessSummary"] = wireless_summary
        if wireless_2_g_traffic is not UNSET:
            field_dict["wireless2gTraffic"] = wireless_2_g_traffic
        if wireless_5_g_traffic is not UNSET:
            field_dict["wireless5gTraffic"] = wireless_5_g_traffic
        if wireless_6_g_traffic is not UNSET:
            field_dict["wireless6gTraffic"] = wireless_6_g_traffic
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wireless_summary_vo import WirelessSummaryVO
        from ..models.wireless_traffic_trend_vo import (
            WirelessTrafficTrendVO,
        )

        d = dict(src_dict)
        _wireless_summary = d.pop("wirelessSummary", UNSET)
        wireless_summary: WirelessSummaryVO | Unset
        if isinstance(_wireless_summary, Unset):
            wireless_summary = UNSET
        else:
            wireless_summary = WirelessSummaryVO.from_dict(_wireless_summary)

        _wireless_2_g_traffic = d.pop("wireless2gTraffic", UNSET)
        wireless_2_g_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
        if _wireless_2_g_traffic is not UNSET:
            wireless_2_g_traffic = []
            for wireless_2_g_traffic_item_data in _wireless_2_g_traffic:
                wireless_2_g_traffic_item = WirelessTrafficTrendVO.from_dict(
                    wireless_2_g_traffic_item_data
                )

                wireless_2_g_traffic.append(wireless_2_g_traffic_item)

        _wireless_5_g_traffic = d.pop("wireless5gTraffic", UNSET)
        wireless_5_g_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
        if _wireless_5_g_traffic is not UNSET:
            wireless_5_g_traffic = []
            for wireless_5_g_traffic_item_data in _wireless_5_g_traffic:
                wireless_5_g_traffic_item = WirelessTrafficTrendVO.from_dict(
                    wireless_5_g_traffic_item_data
                )

                wireless_5_g_traffic.append(wireless_5_g_traffic_item)

        _wireless_6_g_traffic = d.pop("wireless6gTraffic", UNSET)
        wireless_6_g_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
        if _wireless_6_g_traffic is not UNSET:
            wireless_6_g_traffic = []
            for wireless_6_g_traffic_item_data in _wireless_6_g_traffic:
                wireless_6_g_traffic_item = WirelessTrafficTrendVO.from_dict(
                    wireless_6_g_traffic_item_data
                )

                wireless_6_g_traffic.append(wireless_6_g_traffic_item)

        _total_traffic = d.pop("totalTraffic", UNSET)
        total_traffic: list[WirelessTrafficTrendVO] | Unset = UNSET
        if _total_traffic is not UNSET:
            total_traffic = []
            for total_traffic_item_data in _total_traffic:
                total_traffic_item = WirelessTrafficTrendVO.from_dict(
                    total_traffic_item_data
                )

                total_traffic.append(total_traffic_item)

        wireless_traffic_vo = cls(
            wireless_summary=wireless_summary,
            wireless_2_g_traffic=wireless_2_g_traffic,
            wireless_5_g_traffic=wireless_5_g_traffic,
            wireless_6_g_traffic=wireless_6_g_traffic,
            total_traffic=total_traffic,
        )

        wireless_traffic_vo.additional_properties = d
        return wireless_traffic_vo

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
