from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRateDistributionVO")


@_attrs_define
class DataRateDistributionVO:
    """Clients data rate distribution trend

    Attributes:
        time (int | Unset): Timestamp in seconds
        data_rate_above_wifi_4 (list[int] | Unset): 802.11n/ac/ax speed distribution: [>=72, [12,72), <12] Mbps
        data_rate_below_wifi_4 (list[int] | Unset): 802.11a/b/g speed distribution: [>=21, [12,21), <12] Mbps
    """

    time: int | Unset = UNSET
    data_rate_above_wifi_4: list[int] | Unset = UNSET
    data_rate_below_wifi_4: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        data_rate_above_wifi_4: list[int] | Unset = UNSET
        if not isinstance(self.data_rate_above_wifi_4, Unset):
            data_rate_above_wifi_4 = self.data_rate_above_wifi_4

        data_rate_below_wifi_4: list[int] | Unset = UNSET
        if not isinstance(self.data_rate_below_wifi_4, Unset):
            data_rate_below_wifi_4 = self.data_rate_below_wifi_4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if data_rate_above_wifi_4 is not UNSET:
            field_dict["dataRateAboveWifi4"] = data_rate_above_wifi_4
        if data_rate_below_wifi_4 is not UNSET:
            field_dict["dataRateBelowWifi4"] = data_rate_below_wifi_4

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        data_rate_above_wifi_4 = cast(list[int], d.pop("dataRateAboveWifi4", UNSET))

        data_rate_below_wifi_4 = cast(list[int], d.pop("dataRateBelowWifi4", UNSET))

        data_rate_distribution_vo = cls(
            time=time,
            data_rate_above_wifi_4=data_rate_above_wifi_4,
            data_rate_below_wifi_4=data_rate_below_wifi_4,
        )

        data_rate_distribution_vo.additional_properties = d
        return data_rate_distribution_vo

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
