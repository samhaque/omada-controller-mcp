from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanDetailVO")


@_attrs_define
class WanDetailVO:
    """Gateway wan port detail list

    Attributes:
        port (int | Unset):
        name (str | Unset):
        ip (str | Unset):
        proto (int | Unset):
        speed (int | Unset):
        duplex (int | Unset):
        rx (int | Unset):
        tx (int | Unset):
        rx_rate (int | Unset):
        tx_rate (int | Unset):
        latency (int | Unset):
        loss (float | Unset):
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    proto: int | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    latency: int | Unset = UNSET
    loss: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        ip = self.ip

        proto = self.proto

        speed = self.speed

        duplex = self.duplex

        rx = self.rx

        tx = self.tx

        rx_rate = self.rx_rate

        tx_rate = self.tx_rate

        latency = self.latency

        loss = self.loss

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if proto is not UNSET:
            field_dict["proto"] = proto
        if speed is not UNSET:
            field_dict["speed"] = speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        proto = d.pop("proto", UNSET)

        speed = d.pop("speed", UNSET)

        duplex = d.pop("duplex", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        wan_detail_vo = cls(
            port=port,
            name=name,
            ip=ip,
            proto=proto,
            speed=speed,
            duplex=duplex,
            rx=rx,
            tx=tx,
            rx_rate=rx_rate,
            tx_rate=tx_rate,
            latency=latency,
            loss=loss,
        )

        wan_detail_vo.additional_properties = d
        return wan_detail_vo

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
