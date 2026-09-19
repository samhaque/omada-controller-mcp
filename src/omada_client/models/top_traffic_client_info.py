from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopTrafficClientInfo")


@_attrs_define
class TopTrafficClientInfo:
    """Top traffic clients.

    Attributes:
        name (str | Unset): Client name.
        mac (str | Unset): Client MAC.
        type_ (str | Unset): Client type.
        traffic (int | Unset): Client traffic, unit is Byte.
        traffic_percent (int | Unset): Percentage of this client's traffic to total traffic
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        type_ = self.type_

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        top_traffic_client_info = cls(
            name=name,
            mac=mac,
            type_=type_,
            traffic=traffic,
            traffic_percent=traffic_percent,
        )

        top_traffic_client_info.additional_properties = d
        return top_traffic_client_info

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
