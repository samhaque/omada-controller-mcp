from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_traffic_distribution import DeviceTrafficDistribution


T = TypeVar("T", bound="TrafficDistribution")


@_attrs_define
class TrafficDistribution:
    """
    Attributes:
        aps (list[DeviceTrafficDistribution] | Unset): Current Site Ap List
        switches (list[DeviceTrafficDistribution] | Unset): Current Site Switch List
    """

    aps: list[DeviceTrafficDistribution] | Unset = UNSET
    switches: list[DeviceTrafficDistribution] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aps, Unset):
            aps = []
            for aps_item_data in self.aps:
                aps_item = aps_item_data.to_dict()
                aps.append(aps_item)

        switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switches, Unset):
            switches = []
            for switches_item_data in self.switches:
                switches_item = switches_item_data.to_dict()
                switches.append(switches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aps is not UNSET:
            field_dict["aps"] = aps
        if switches is not UNSET:
            field_dict["switches"] = switches

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_traffic_distribution import (
            DeviceTrafficDistribution,
        )

        d = dict(src_dict)
        _aps = d.pop("aps", UNSET)
        aps: list[DeviceTrafficDistribution] | Unset = UNSET
        if _aps is not UNSET:
            aps = []
            for aps_item_data in _aps:
                aps_item = DeviceTrafficDistribution.from_dict(aps_item_data)

                aps.append(aps_item)

        _switches = d.pop("switches", UNSET)
        switches: list[DeviceTrafficDistribution] | Unset = UNSET
        if _switches is not UNSET:
            switches = []
            for switches_item_data in _switches:
                switches_item = DeviceTrafficDistribution.from_dict(switches_item_data)

                switches.append(switches_item)

        traffic_distribution = cls(
            aps=aps,
            switches=switches,
        )

        traffic_distribution.additional_properties = d
        return traffic_distribution

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
