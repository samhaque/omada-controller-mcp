from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_client_wireless_link_info import (
        TopologyClientWirelessLinkInfo,
    )


T = TypeVar("T", bound="TopologyClientWirelessUpInfo")


@_attrs_define
class TopologyClientWirelessUpInfo:
    """Client uplink information while connection is wireless.

    Attributes:
        ssid (str | Unset): Ssid.
        radio (int | Unset): Radio, it should be a value as follows: 0:2G, 1:5G, 2:5G2, 3:6G.
        channel (int | Unset): Channel.
        rssi (int | Unset): Signal strength, unit: dBm
        support5g2 (bool | Unset): Whether the device supports the 5G2 frequency band.
        multi_link (list[TopologyClientWirelessLinkInfo] | Unset): Client link information while client connects to
            multiple frequency bands.
    """

    ssid: str | Unset = UNSET
    radio: int | Unset = UNSET
    channel: int | Unset = UNSET
    rssi: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    multi_link: list[TopologyClientWirelessLinkInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid = self.ssid

        radio = self.radio

        channel = self.channel

        rssi = self.rssi

        support5g2 = self.support5g2

        multi_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_link, Unset):
            multi_link = []
            for multi_link_item_data in self.multi_link:
                multi_link_item = multi_link_item_data.to_dict()
                multi_link.append(multi_link_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if radio is not UNSET:
            field_dict["radio"] = radio
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if multi_link is not UNSET:
            field_dict["multiLink"] = multi_link

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_client_wireless_link_info import (
            TopologyClientWirelessLinkInfo,
        )

        d = dict(src_dict)
        ssid = d.pop("ssid", UNSET)

        radio = d.pop("radio", UNSET)

        channel = d.pop("channel", UNSET)

        rssi = d.pop("rssi", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        _multi_link = d.pop("multiLink", UNSET)
        multi_link: list[TopologyClientWirelessLinkInfo] | Unset = UNSET
        if _multi_link is not UNSET:
            multi_link = []
            for multi_link_item_data in _multi_link:
                multi_link_item = TopologyClientWirelessLinkInfo.from_dict(
                    multi_link_item_data
                )

                multi_link.append(multi_link_item)

        topology_client_wireless_up_info = cls(
            ssid=ssid,
            radio=radio,
            channel=channel,
            rssi=rssi,
            support5g2=support5g2,
            multi_link=multi_link,
        )

        topology_client_wireless_up_info.additional_properties = d
        return topology_client_wireless_up_info

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
