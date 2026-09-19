from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatisticInfoDetailDTO")


@_attrs_define
class StatisticInfoDetailDTO:
    """
    Attributes:
        service_port_index (int | Unset): Service port index
        received_broadcast (int | Unset): Received broadcast
        received_multicast (int | Unset): Received multicast
        received_unicast (int | Unset): Received unicast
        received_jumbo (int | Unset): Received jumbo
        alignment_errors (int | Unset): Alignment errors
        undersize_packets (int | Unset): Undersize packets
        packets_of_64_octets (int | Unset): Packets Of 64 Octets
        packets_of_65_to_127_octets (int | Unset): Packets of 65 to 127 octets
        packets_of_128_to_255_octets (int | Unset): Packets of 128 to 255 octets
        packets_of_256_to_511_octets (int | Unset): Packets of 256 to511 octets
        packets_of_512_to_1023_octets (int | Unset): Packets of 512 to 1023 octets
        packets_of_1023_to_1518_octets (int | Unset): Packets of 1023 to 1518 octets
        received_packets (int | Unset): Received packets
        received_bytes (int | Unset): Received bytes
        sent_broadcast (int | Unset): Sent broadcast
        sent_multicast (int | Unset): Sent multicast
        sent_unicast (int | Unset): Sent unicast
        sent_jumbo (int | Unset): Sent jumbo
        sent_packets (int | Unset): Sent packets
        sent_bytes (int | Unset): Sent bytes
        collisions_errors (int | Unset): Collision errors
    """

    service_port_index: int | Unset = UNSET
    received_broadcast: int | Unset = UNSET
    received_multicast: int | Unset = UNSET
    received_unicast: int | Unset = UNSET
    received_jumbo: int | Unset = UNSET
    alignment_errors: int | Unset = UNSET
    undersize_packets: int | Unset = UNSET
    packets_of_64_octets: int | Unset = UNSET
    packets_of_65_to_127_octets: int | Unset = UNSET
    packets_of_128_to_255_octets: int | Unset = UNSET
    packets_of_256_to_511_octets: int | Unset = UNSET
    packets_of_512_to_1023_octets: int | Unset = UNSET
    packets_of_1023_to_1518_octets: int | Unset = UNSET
    received_packets: int | Unset = UNSET
    received_bytes: int | Unset = UNSET
    sent_broadcast: int | Unset = UNSET
    sent_multicast: int | Unset = UNSET
    sent_unicast: int | Unset = UNSET
    sent_jumbo: int | Unset = UNSET
    sent_packets: int | Unset = UNSET
    sent_bytes: int | Unset = UNSET
    collisions_errors: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_port_index = self.service_port_index

        received_broadcast = self.received_broadcast

        received_multicast = self.received_multicast

        received_unicast = self.received_unicast

        received_jumbo = self.received_jumbo

        alignment_errors = self.alignment_errors

        undersize_packets = self.undersize_packets

        packets_of_64_octets = self.packets_of_64_octets

        packets_of_65_to_127_octets = self.packets_of_65_to_127_octets

        packets_of_128_to_255_octets = self.packets_of_128_to_255_octets

        packets_of_256_to_511_octets = self.packets_of_256_to_511_octets

        packets_of_512_to_1023_octets = self.packets_of_512_to_1023_octets

        packets_of_1023_to_1518_octets = self.packets_of_1023_to_1518_octets

        received_packets = self.received_packets

        received_bytes = self.received_bytes

        sent_broadcast = self.sent_broadcast

        sent_multicast = self.sent_multicast

        sent_unicast = self.sent_unicast

        sent_jumbo = self.sent_jumbo

        sent_packets = self.sent_packets

        sent_bytes = self.sent_bytes

        collisions_errors = self.collisions_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_port_index is not UNSET:
            field_dict["servicePortIndex"] = service_port_index
        if received_broadcast is not UNSET:
            field_dict["receivedBroadcast"] = received_broadcast
        if received_multicast is not UNSET:
            field_dict["receivedMulticast"] = received_multicast
        if received_unicast is not UNSET:
            field_dict["receivedUnicast"] = received_unicast
        if received_jumbo is not UNSET:
            field_dict["receivedJumbo"] = received_jumbo
        if alignment_errors is not UNSET:
            field_dict["alignmentErrors"] = alignment_errors
        if undersize_packets is not UNSET:
            field_dict["undersizePackets"] = undersize_packets
        if packets_of_64_octets is not UNSET:
            field_dict["packetsOf64Octets"] = packets_of_64_octets
        if packets_of_65_to_127_octets is not UNSET:
            field_dict["packetsOf65To127Octets"] = packets_of_65_to_127_octets
        if packets_of_128_to_255_octets is not UNSET:
            field_dict["packetsOf128To255Octets"] = packets_of_128_to_255_octets
        if packets_of_256_to_511_octets is not UNSET:
            field_dict["packetsOf256To511Octets"] = packets_of_256_to_511_octets
        if packets_of_512_to_1023_octets is not UNSET:
            field_dict["packetsOf512To1023Octets"] = packets_of_512_to_1023_octets
        if packets_of_1023_to_1518_octets is not UNSET:
            field_dict["packetsOf1023To1518Octets"] = packets_of_1023_to_1518_octets
        if received_packets is not UNSET:
            field_dict["receivedPackets"] = received_packets
        if received_bytes is not UNSET:
            field_dict["receivedBytes"] = received_bytes
        if sent_broadcast is not UNSET:
            field_dict["sentBroadcast"] = sent_broadcast
        if sent_multicast is not UNSET:
            field_dict["sentMulticast"] = sent_multicast
        if sent_unicast is not UNSET:
            field_dict["sentUnicast"] = sent_unicast
        if sent_jumbo is not UNSET:
            field_dict["sentJumbo"] = sent_jumbo
        if sent_packets is not UNSET:
            field_dict["sentPackets"] = sent_packets
        if sent_bytes is not UNSET:
            field_dict["sentBytes"] = sent_bytes
        if collisions_errors is not UNSET:
            field_dict["collisionsErrors"] = collisions_errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_port_index = d.pop("servicePortIndex", UNSET)

        received_broadcast = d.pop("receivedBroadcast", UNSET)

        received_multicast = d.pop("receivedMulticast", UNSET)

        received_unicast = d.pop("receivedUnicast", UNSET)

        received_jumbo = d.pop("receivedJumbo", UNSET)

        alignment_errors = d.pop("alignmentErrors", UNSET)

        undersize_packets = d.pop("undersizePackets", UNSET)

        packets_of_64_octets = d.pop("packetsOf64Octets", UNSET)

        packets_of_65_to_127_octets = d.pop("packetsOf65To127Octets", UNSET)

        packets_of_128_to_255_octets = d.pop("packetsOf128To255Octets", UNSET)

        packets_of_256_to_511_octets = d.pop("packetsOf256To511Octets", UNSET)

        packets_of_512_to_1023_octets = d.pop("packetsOf512To1023Octets", UNSET)

        packets_of_1023_to_1518_octets = d.pop("packetsOf1023To1518Octets", UNSET)

        received_packets = d.pop("receivedPackets", UNSET)

        received_bytes = d.pop("receivedBytes", UNSET)

        sent_broadcast = d.pop("sentBroadcast", UNSET)

        sent_multicast = d.pop("sentMulticast", UNSET)

        sent_unicast = d.pop("sentUnicast", UNSET)

        sent_jumbo = d.pop("sentJumbo", UNSET)

        sent_packets = d.pop("sentPackets", UNSET)

        sent_bytes = d.pop("sentBytes", UNSET)

        collisions_errors = d.pop("collisionsErrors", UNSET)

        statistic_info_detail_dto = cls(
            service_port_index=service_port_index,
            received_broadcast=received_broadcast,
            received_multicast=received_multicast,
            received_unicast=received_unicast,
            received_jumbo=received_jumbo,
            alignment_errors=alignment_errors,
            undersize_packets=undersize_packets,
            packets_of_64_octets=packets_of_64_octets,
            packets_of_65_to_127_octets=packets_of_65_to_127_octets,
            packets_of_128_to_255_octets=packets_of_128_to_255_octets,
            packets_of_256_to_511_octets=packets_of_256_to_511_octets,
            packets_of_512_to_1023_octets=packets_of_512_to_1023_octets,
            packets_of_1023_to_1518_octets=packets_of_1023_to_1518_octets,
            received_packets=received_packets,
            received_bytes=received_bytes,
            sent_broadcast=sent_broadcast,
            sent_multicast=sent_multicast,
            sent_unicast=sent_unicast,
            sent_jumbo=sent_jumbo,
            sent_packets=sent_packets,
            sent_bytes=sent_bytes,
            collisions_errors=collisions_errors,
        )

        statistic_info_detail_dto.additional_properties = d
        return statistic_info_detail_dto

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
