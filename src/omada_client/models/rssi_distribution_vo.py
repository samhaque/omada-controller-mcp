from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RssiDistributionVO")


@_attrs_define
class RssiDistributionVO:
    """Clients RSSI distribution trend

    Attributes:
        time (int | Unset): Timestamp in seconds
        rssi_distribution (list[int] | Unset): RSSI distribution: [>=−65dBm, [−72,−65), <−72dBm]
    """

    time: int | Unset = UNSET
    rssi_distribution: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        rssi_distribution: list[int] | Unset = UNSET
        if not isinstance(self.rssi_distribution, Unset):
            rssi_distribution = self.rssi_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if rssi_distribution is not UNSET:
            field_dict["rssiDistribution"] = rssi_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        rssi_distribution = cast(list[int], d.pop("rssiDistribution", UNSET))

        rssi_distribution_vo = cls(
            time=time,
            rssi_distribution=rssi_distribution,
        )

        rssi_distribution_vo.additional_properties = d
        return rssi_distribution_vo

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
