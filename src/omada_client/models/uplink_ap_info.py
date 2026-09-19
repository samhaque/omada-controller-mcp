from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_multi_link_info import APMultiLinkInfo


T = TypeVar("T", bound="UplinkAPInfo")


@_attrs_define
class UplinkAPInfo:
    """Uplink AP info, exists when parameter [upDeviceType] is 0.

    Attributes:
        port (int | Unset): Client connected port.
        name (str | Unset): Client connected port name.
        lag_id (int | Unset): Lag Id
        channel (int | Unset): Connected actual channel.
        ssid (str | Unset): Connected SSID name.
        radio (int | Unset): Radio ID, 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz.
        support5g2 (bool | Unset): Whether the AP support 5G2 radio.
        rssi (int | Unset): Signal strength, unit: dBm.
        traffic_down (int | Unset): Downstream traffic (Byte).
        traffic_up (int | Unset): Upstream traffic (Byte).
        tx_rate (int | Unset): Downlink negotiation rate (Kbit/s)
        rx_rate (int | Unset): Uplink negotiation rate (Kbit/s)
        multi_link (list[APMultiLinkInfo] | Unset): Multi link info (MLO)
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    ssid: str | Unset = UNSET
    radio: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    rssi: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    multi_link: list[APMultiLinkInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        lag_id = self.lag_id

        channel = self.channel

        ssid = self.ssid

        radio = self.radio

        support5g2 = self.support5g2

        rssi = self.rssi

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        multi_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_link, Unset):
            multi_link = []
            for multi_link_item_data in self.multi_link:
                multi_link_item = multi_link_item_data.to_dict()
                multi_link.append(multi_link_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if radio is not UNSET:
            field_dict["radio"] = radio
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if multi_link is not UNSET:
            field_dict["multiLink"] = multi_link

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_multi_link_info import APMultiLinkInfo

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        lag_id = d.pop("lagId", UNSET)

        channel = d.pop("channel", UNSET)

        ssid = d.pop("ssid", UNSET)

        radio = d.pop("radio", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        rssi = d.pop("rssi", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        _multi_link = d.pop("multiLink", UNSET)
        multi_link: list[APMultiLinkInfo] | Unset = UNSET
        if _multi_link is not UNSET:
            multi_link = []
            for multi_link_item_data in _multi_link:
                multi_link_item = APMultiLinkInfo.from_dict(multi_link_item_data)

                multi_link.append(multi_link_item)

        uplink_ap_info = cls(
            port=port,
            name=name,
            lag_id=lag_id,
            channel=channel,
            ssid=ssid,
            radio=radio,
            support5g2=support5g2,
            rssi=rssi,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            multi_link=multi_link,
        )

        uplink_ap_info.additional_properties = d
        return uplink_ap_info

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
