from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.traffic_distribution_list_vo import TrafficDistributionListVO


T = TypeVar("T", bound="TrafficDistributionVO")


@_attrs_define
class TrafficDistributionVO:
    """
    Attributes:
        total_traffic (int | Unset): total traffic
        wired_traffic (int | Unset): traffic of wired device
        wireless_traffic (int | Unset): traffic of wireless device
        traffic_distribution (list[TrafficDistributionListVO] | Unset): traffic data point
    """

    total_traffic: int | Unset = UNSET
    wired_traffic: int | Unset = UNSET
    wireless_traffic: int | Unset = UNSET
    traffic_distribution: list[TrafficDistributionListVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_traffic = self.total_traffic

        wired_traffic = self.wired_traffic

        wireless_traffic = self.wireless_traffic

        traffic_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traffic_distribution, Unset):
            traffic_distribution = []
            for traffic_distribution_item_data in self.traffic_distribution:
                traffic_distribution_item = traffic_distribution_item_data.to_dict()
                traffic_distribution.append(traffic_distribution_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if wired_traffic is not UNSET:
            field_dict["wiredTraffic"] = wired_traffic
        if wireless_traffic is not UNSET:
            field_dict["wirelessTraffic"] = wireless_traffic
        if traffic_distribution is not UNSET:
            field_dict["trafficDistribution"] = traffic_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.traffic_distribution_list_vo import (
            TrafficDistributionListVO,
        )

        d = dict(src_dict)
        total_traffic = d.pop("totalTraffic", UNSET)

        wired_traffic = d.pop("wiredTraffic", UNSET)

        wireless_traffic = d.pop("wirelessTraffic", UNSET)

        _traffic_distribution = d.pop("trafficDistribution", UNSET)
        traffic_distribution: list[TrafficDistributionListVO] | Unset = UNSET
        if _traffic_distribution is not UNSET:
            traffic_distribution = []
            for traffic_distribution_item_data in _traffic_distribution:
                traffic_distribution_item = TrafficDistributionListVO.from_dict(
                    traffic_distribution_item_data
                )

                traffic_distribution.append(traffic_distribution_item)

        traffic_distribution_vo = cls(
            total_traffic=total_traffic,
            wired_traffic=wired_traffic,
            wireless_traffic=wireless_traffic,
            traffic_distribution=traffic_distribution,
        )

        traffic_distribution_vo.additional_properties = d
        return traffic_distribution_vo

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
