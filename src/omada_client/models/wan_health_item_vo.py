from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanHealthItemVO")


@_attrs_define
class WanHealthItemVO:
    """
    Attributes:
        name (str | Unset): WAN name
        port (int | Unset): WAN port number
        latency (str | Unset): Latency
        jitter (str | Unset): Jitter
        packet_loss (float | Unset): Packet loss
        throughput (int | Unset): Throughput
    """

    name: str | Unset = UNSET
    port: int | Unset = UNSET
    latency: str | Unset = UNSET
    jitter: str | Unset = UNSET
    packet_loss: float | Unset = UNSET
    throughput: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        port = self.port

        latency = self.latency

        jitter = self.jitter

        packet_loss = self.packet_loss

        throughput = self.throughput

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if latency is not UNSET:
            field_dict["latency"] = latency
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if packet_loss is not UNSET:
            field_dict["packetLoss"] = packet_loss
        if throughput is not UNSET:
            field_dict["throughput"] = throughput

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        port = d.pop("port", UNSET)

        latency = d.pop("latency", UNSET)

        jitter = d.pop("jitter", UNSET)

        packet_loss = d.pop("packetLoss", UNSET)

        throughput = d.pop("throughput", UNSET)

        wan_health_item_vo = cls(
            name=name,
            port=port,
            latency=latency,
            jitter=jitter,
            packet_loss=packet_loss,
            throughput=throughput,
        )

        wan_health_item_vo.additional_properties = d
        return wan_health_item_vo

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
