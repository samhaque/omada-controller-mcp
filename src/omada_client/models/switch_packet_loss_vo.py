from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchPacketLossVO")


@_attrs_define
class SwitchPacketLossVO:
    """Top switches by packet loss

    Attributes:
        device (str | Unset): Device name
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        mac (str | Unset): Device mac
        type_ (str | Unset): Device type
        port_cnt (int | Unset): Total number of ports
        pkts_loss_port_cnt (int | Unset): Number of ports with packet loss
        loss_pkts (int | Unset): Total number of lost packets
    """

    device: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    port_cnt: int | Unset = UNSET
    pkts_loss_port_cnt: int | Unset = UNSET
    loss_pkts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        model = self.model

        model_version = self.model_version

        mac = self.mac

        type_ = self.type_

        port_cnt = self.port_cnt

        pkts_loss_port_cnt = self.pkts_loss_port_cnt

        loss_pkts = self.loss_pkts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        device = d.pop("device", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        port_cnt = d.pop("portCnt", UNSET)

        pkts_loss_port_cnt = d.pop("pktsLossPortCnt", UNSET)

        loss_pkts = d.pop("lossPkts", UNSET)

        switch_packet_loss_vo = cls(
            device=device,
            model=model,
            model_version=model_version,
            mac=mac,
            type_=type_,
            port_cnt=port_cnt,
            pkts_loss_port_cnt=pkts_loss_port_cnt,
            loss_pkts=loss_pkts,
        )

        switch_packet_loss_vo.additional_properties = d
        return switch_packet_loss_vo

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
