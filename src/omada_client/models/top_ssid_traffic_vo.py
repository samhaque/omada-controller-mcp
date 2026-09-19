from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopSsidTrafficVO")


@_attrs_define
class TopSsidTrafficVO:
    """
    Attributes:
        ssid (str | Unset): ssid name
        security (str | Unset): security
        channel (str | Unset): channel
        traffic (int | Unset): total traffic
        traffic_ratio (int | Unset): traffic percentage
        client_count (int | Unset): number of client
        average_singal_strength (int | Unset): average signal strength
    """

    ssid: str | Unset = UNSET
    security: str | Unset = UNSET
    channel: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_ratio: int | Unset = UNSET
    client_count: int | Unset = UNSET
    average_singal_strength: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid = self.ssid

        security = self.security

        channel = self.channel

        traffic = self.traffic

        traffic_ratio = self.traffic_ratio

        client_count = self.client_count

        average_singal_strength = self.average_singal_strength

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if security is not UNSET:
            field_dict["security"] = security
        if channel is not UNSET:
            field_dict["channel"] = channel
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_ratio is not UNSET:
            field_dict["trafficRatio"] = traffic_ratio
        if client_count is not UNSET:
            field_dict["clientCount"] = client_count
        if average_singal_strength is not UNSET:
            field_dict["averageSingalStrength"] = average_singal_strength

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssid = d.pop("ssid", UNSET)

        security = d.pop("security", UNSET)

        channel = d.pop("channel", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_ratio = d.pop("trafficRatio", UNSET)

        client_count = d.pop("clientCount", UNSET)

        average_singal_strength = d.pop("averageSingalStrength", UNSET)

        top_ssid_traffic_vo = cls(
            ssid=ssid,
            security=security,
            channel=channel,
            traffic=traffic,
            traffic_ratio=traffic_ratio,
            client_count=client_count,
            average_singal_strength=average_singal_strength,
        )

        top_ssid_traffic_vo.additional_properties = d
        return top_ssid_traffic_vo

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
