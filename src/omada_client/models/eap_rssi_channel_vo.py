from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EapRssiChannelVO")


@_attrs_define
class EapRssiChannelVO:
    """
    Attributes:
        name (str | Unset):
        mac (str | Unset):
        model (str | Unset):
        type_ (str | Unset):
        model_version (str | Unset):
        traffic (int | Unset):
        traffic_percent (int | Unset):
        clients_count (int | Unset):
        health_score (int | Unset):
        signal_level (int | Unset):
        rssi (int | Unset):
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    type_: str | Unset = UNSET
    model_version: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: int | Unset = UNSET
    clients_count: int | Unset = UNSET
    health_score: int | Unset = UNSET
    signal_level: int | Unset = UNSET
    rssi: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        type_ = self.type_

        model_version = self.model_version

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        clients_count = self.clients_count

        health_score = self.health_score

        signal_level = self.signal_level

        rssi = self.rssi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if clients_count is not UNSET:
            field_dict["clientsCount"] = clients_count
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if signal_level is not UNSET:
            field_dict["signalLevel"] = signal_level
        if rssi is not UNSET:
            field_dict["rssi"] = rssi

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        type_ = d.pop("type", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        clients_count = d.pop("clientsCount", UNSET)

        health_score = d.pop("healthScore", UNSET)

        signal_level = d.pop("signalLevel", UNSET)

        rssi = d.pop("rssi", UNSET)

        eap_rssi_channel_vo = cls(
            name=name,
            mac=mac,
            model=model,
            type_=type_,
            model_version=model_version,
            traffic=traffic,
            traffic_percent=traffic_percent,
            clients_count=clients_count,
            health_score=health_score,
            signal_level=signal_level,
            rssi=rssi,
        )

        eap_rssi_channel_vo.additional_properties = d
        return eap_rssi_channel_vo

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
