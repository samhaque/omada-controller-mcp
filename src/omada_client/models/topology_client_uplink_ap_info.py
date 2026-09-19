from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyClientUplinkApInfo")


@_attrs_define
class TopologyClientUplinkApInfo:
    """Uplink Information while Uplink Device is Ap.

    Attributes:
        channel (int | Unset): Channel, only for wireless connection.
        ssid (str | Unset): Ssid, only for wireless connection.
        radio (int | Unset): Radio, it should be a value as follows: 0:2G, 1:5G, 2:5G2, 3:6G, only for wireless
            connection.
        link_speed (int | Unset): Link Speed, it should be a value as follows: 1:10Mbps, 2:100Mbps, 3:1000Mbps,
            4:2.5Gbps, 5:10Gbps, only for wired connection.
        support5g2 (bool | Unset): Whether the device supports the 5G2 frequency band.
        duplex (int | Unset): Duplex, it should be a value as follows: 1:Half Duplex, 2:Full Duplex, only for wired
            connection.
    """

    channel: int | Unset = UNSET
    ssid: str | Unset = UNSET
    radio: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    duplex: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ssid = self.ssid

        radio = self.radio

        link_speed = self.link_speed

        support5g2 = self.support5g2

        duplex = self.duplex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if radio is not UNSET:
            field_dict["radio"] = radio
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if duplex is not UNSET:
            field_dict["duplex"] = duplex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        ssid = d.pop("ssid", UNSET)

        radio = d.pop("radio", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        duplex = d.pop("duplex", UNSET)

        topology_client_uplink_ap_info = cls(
            channel=channel,
            ssid=ssid,
            radio=radio,
            link_speed=link_speed,
            support5g2=support5g2,
            duplex=duplex,
        )

        topology_client_uplink_ap_info.additional_properties = d
        return topology_client_uplink_ap_info

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
