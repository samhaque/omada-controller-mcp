from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IspLoadStatVO")


@_attrs_define
class IspLoadStatVO:
    """WAN port ISP load stat data list

    Attributes:
        total_rate (int | Unset): WAN port rate (rxR+txR)
        latency (int | Unset): WAN latency, when mode is WAN and device is connected, Unit: ms
        time (int | Unset): Timestamp, in seconds, such as 1682000000
        total_traffic (int | Unset): Upstream and downstream traffic
        up_traffic (int | Unset): Upstream traffic
        down_traffic (int | Unset): Downstream traffic
    """

    total_rate: int | Unset = UNSET
    latency: int | Unset = UNSET
    time: int | Unset = UNSET
    total_traffic: int | Unset = UNSET
    up_traffic: int | Unset = UNSET
    down_traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rate = self.total_rate

        latency = self.latency

        time = self.time

        total_traffic = self.total_traffic

        up_traffic = self.up_traffic

        down_traffic = self.down_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rate is not UNSET:
            field_dict["totalRate"] = total_rate
        if latency is not UNSET:
            field_dict["latency"] = latency
        if time is not UNSET:
            field_dict["time"] = time
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if up_traffic is not UNSET:
            field_dict["upTraffic"] = up_traffic
        if down_traffic is not UNSET:
            field_dict["downTraffic"] = down_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_rate = d.pop("totalRate", UNSET)

        latency = d.pop("latency", UNSET)

        time = d.pop("time", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        up_traffic = d.pop("upTraffic", UNSET)

        down_traffic = d.pop("downTraffic", UNSET)

        isp_load_stat_vo = cls(
            total_rate=total_rate,
            latency=latency,
            time=time,
            total_traffic=total_traffic,
            up_traffic=up_traffic,
            down_traffic=down_traffic,
        )

        isp_load_stat_vo.additional_properties = d
        return isp_load_stat_vo

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
