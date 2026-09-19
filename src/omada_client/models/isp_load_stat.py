from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IspLoadStat")


@_attrs_define
class IspLoadStat:
    """WAN port data list

    Attributes:
        total_rate (int | Unset): WAN port rate (rxR+txR)
        latency (int | Unset): WAN port delay should be within the range of 0 or 1000. (in ms)
        time (int | Unset): Timestamp of statistical data (in seconds)
    """

    total_rate: int | Unset = UNSET
    latency: int | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rate = self.total_rate

        latency = self.latency

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rate is not UNSET:
            field_dict["totalRate"] = total_rate
        if latency is not UNSET:
            field_dict["latency"] = latency
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_rate = d.pop("totalRate", UNSET)

        latency = d.pop("latency", UNSET)

        time = d.pop("time", UNSET)

        isp_load_stat = cls(
            total_rate=total_rate,
            latency=latency,
            time=time,
        )

        isp_load_stat.additional_properties = d
        return isp_load_stat

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
