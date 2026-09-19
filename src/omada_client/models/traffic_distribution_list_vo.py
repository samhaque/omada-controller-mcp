from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrafficDistributionListVO")


@_attrs_define
class TrafficDistributionListVO:
    """traffic data point

    Attributes:
        time (int | Unset): time
        wireless_data (int | Unset): wireless traffic
        wired_data (int | Unset): wired traffic
        total_data (int | Unset): total traffic
    """

    time: int | Unset = UNSET
    wireless_data: int | Unset = UNSET
    wired_data: int | Unset = UNSET
    total_data: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        wireless_data = self.wireless_data

        wired_data = self.wired_data

        total_data = self.total_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if wireless_data is not UNSET:
            field_dict["wirelessData"] = wireless_data
        if wired_data is not UNSET:
            field_dict["wiredData"] = wired_data
        if total_data is not UNSET:
            field_dict["totalData"] = total_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        wireless_data = d.pop("wirelessData", UNSET)

        wired_data = d.pop("wiredData", UNSET)

        total_data = d.pop("totalData", UNSET)

        traffic_distribution_list_vo = cls(
            time=time,
            wireless_data=wireless_data,
            wired_data=wired_data,
            total_data=total_data,
        )

        traffic_distribution_list_vo.additional_properties = d
        return traffic_distribution_list_vo

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
