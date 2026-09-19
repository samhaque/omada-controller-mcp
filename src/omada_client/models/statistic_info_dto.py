from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatisticInfoDTO")


@_attrs_define
class StatisticInfoDTO:
    """Content

    Attributes:
        service_port_index (int): ID of service port.ServicePortIndex should be within the range of 1 to 8100
        packets_rx (int | Unset): Packets received
        packets_tx (int | Unset): Packets transmitted
        octets_rx (int | Unset): Octets received
        octets_tx (int | Unset): Octets transmitted
    """

    service_port_index: int
    packets_rx: int | Unset = UNSET
    packets_tx: int | Unset = UNSET
    octets_rx: int | Unset = UNSET
    octets_tx: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_port_index = self.service_port_index

        packets_rx = self.packets_rx

        packets_tx = self.packets_tx

        octets_rx = self.octets_rx

        octets_tx = self.octets_tx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servicePortIndex": service_port_index,
            }
        )
        if packets_rx is not UNSET:
            field_dict["packetsRx"] = packets_rx
        if packets_tx is not UNSET:
            field_dict["packetsTx"] = packets_tx
        if octets_rx is not UNSET:
            field_dict["octetsRx"] = octets_rx
        if octets_tx is not UNSET:
            field_dict["octetsTx"] = octets_tx

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_port_index = d.pop("servicePortIndex")

        packets_rx = d.pop("packetsRx", UNSET)

        packets_tx = d.pop("packetsTx", UNSET)

        octets_rx = d.pop("octetsRx", UNSET)

        octets_tx = d.pop("octetsTx", UNSET)

        statistic_info_dto = cls(
            service_port_index=service_port_index,
            packets_rx=packets_rx,
            packets_tx=packets_tx,
            octets_rx=octets_rx,
            octets_tx=octets_tx,
        )

        statistic_info_dto.additional_properties = d
        return statistic_info_dto

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
