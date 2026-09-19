from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopOswPacketLossOpenApiVO")


@_attrs_define
class TopOswPacketLossOpenApiVO:
    """Packet loss information list

    Attributes:
        name (str | Unset): Device name
        mac (str | Unset): Device mac
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        health_score (int | Unset): Health score
        type_ (str | Unset): Device type
        device_series_type (int | Unset): Device series type should be a value as follows: 0:advanced, 1:pro
        port_cnt (int | Unset): Total number of ports
        pkts_loss_port_cnt (int | Unset): Number of Ports with Packet Loss
        loss_pkts (int | Unset): Total number of lost packets
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    health_score: int | Unset = UNSET
    type_: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    port_cnt: int | Unset = UNSET
    pkts_loss_port_cnt: int | Unset = UNSET
    loss_pkts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        health_score = self.health_score

        type_ = self.type_

        device_series_type = self.device_series_type

        port_cnt = self.port_cnt

        pkts_loss_port_cnt = self.pkts_loss_port_cnt

        loss_pkts = self.loss_pkts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if type_ is not UNSET:
            field_dict["type"] = type_
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if port_cnt is not UNSET:
            field_dict["portCnt"] = port_cnt
        if pkts_loss_port_cnt is not UNSET:
            field_dict["pktsLossPortCnt"] = pkts_loss_port_cnt
        if loss_pkts is not UNSET:
            field_dict["lossPkts"] = loss_pkts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        health_score = d.pop("healthScore", UNSET)

        type_ = d.pop("type", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        port_cnt = d.pop("portCnt", UNSET)

        pkts_loss_port_cnt = d.pop("pktsLossPortCnt", UNSET)

        loss_pkts = d.pop("lossPkts", UNSET)

        top_osw_packet_loss_open_api_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            health_score=health_score,
            type_=type_,
            device_series_type=device_series_type,
            port_cnt=port_cnt,
            pkts_loss_port_cnt=pkts_loss_port_cnt,
            loss_pkts=loss_pkts,
        )

        top_osw_packet_loss_open_api_vo.additional_properties = d
        return top_osw_packet_loss_open_api_vo

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
