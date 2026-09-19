from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClientStatisticalDataDetailResultAvgSignal")


@_attrs_define
class ClientStatisticalDataDetailResultAvgSignal:
    """(Wireless) Average signal on each channel, the key is radioId(0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz), the value is
    average signal(unit: dBm).

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_statistical_data_detail_result_avg_signal = cls()

        client_statistical_data_detail_result_avg_signal.additional_properties = d
        return client_statistical_data_detail_result_avg_signal

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
