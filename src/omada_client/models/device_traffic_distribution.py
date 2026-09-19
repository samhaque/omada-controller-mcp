from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTrafficDistribution")


@_attrs_define
class DeviceTrafficDistribution:
    """Current Site Switch List

    Attributes:
        name (str | Unset): Device Name
        mac (str | Unset): Device MAC
        traffic (float | Unset): Device traffic measured in MB
        traffic_proportion (float | Unset): The proportion of AP traffic in percentage
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    traffic: float | Unset = UNSET
    traffic_proportion: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        traffic = self.traffic

        traffic_proportion = self.traffic_proportion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_proportion is not UNSET:
            field_dict["trafficProportion"] = traffic_proportion

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_proportion = d.pop("trafficProportion", UNSET)

        device_traffic_distribution = cls(
            name=name,
            mac=mac,
            traffic=traffic,
            traffic_proportion=traffic_proportion,
        )

        device_traffic_distribution.additional_properties = d
        return device_traffic_distribution

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
