from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyClientWirelessLinkInfo")


@_attrs_define
class TopologyClientWirelessLinkInfo:
    """Client wireless link information.

    Attributes:
        radio_id (int | Unset): RadioId, it should be a value as follows: 0:2G, 1:5G, 2:5G2, 3:6G.
        channel (int | Unset): Channel.
        rssi (int | Unset): Signal strength, unit: dBm
    """

    radio_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    rssi: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        channel = self.channel

        rssi = self.rssi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rssi is not UNSET:
            field_dict["rssi"] = rssi

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        channel = d.pop("channel", UNSET)

        rssi = d.pop("rssi", UNSET)

        topology_client_wireless_link_info = cls(
            radio_id=radio_id,
            channel=channel,
            rssi=rssi,
        )

        topology_client_wireless_link_info.additional_properties = d
        return topology_client_wireless_link_info

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
