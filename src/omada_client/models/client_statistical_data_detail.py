from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_multi_link_info import ClientMultiLinkInfo


T = TypeVar("T", bound="ClientStatisticalDataDetail")


@_attrs_define
class ClientStatisticalDataDetail:
    """Client Statistical Data Detail list.

    Attributes:
        mac (str | Unset): Client MAC Address.
        wireless (bool | Unset): true: Wireless client;  false: Not wireless client
        time (int | Unset): The statistical data collected timestamp, unit: second.
        down (int | Unset): Downstream traffic (Byte).
        up (int | Unset): Upstream traffic (Byte).
        down_rate (int | Unset): Downlink rate (Byte/s).
        up_rate (int | Unset): Uplink rate (Byte/s).
        tx_r (int | Unset): (Wireless) Downlink negotiation rate (bit/s).
        rx_r (int | Unset): (Wireless) Uplink negotiation rate (bit/s).
        signal (int | Unset): (Wireless) Signal strength, unit: dBm.
        radio_id (int | Unset): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz; 2:5GHz-2; 3: 6GHz
        tx_fp (int | Unset): Number of downstream failed packets.
        multi_links (list[ClientMultiLinkInfo] | Unset): (MLO) Client multi link info.
    """

    mac: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    time: int | Unset = UNSET
    down: int | Unset = UNSET
    up: int | Unset = UNSET
    down_rate: int | Unset = UNSET
    up_rate: int | Unset = UNSET
    tx_r: int | Unset = UNSET
    rx_r: int | Unset = UNSET
    signal: int | Unset = UNSET
    radio_id: int | Unset = UNSET
    tx_fp: int | Unset = UNSET
    multi_links: list[ClientMultiLinkInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        wireless = self.wireless

        time = self.time

        down = self.down

        up = self.up

        down_rate = self.down_rate

        up_rate = self.up_rate

        tx_r = self.tx_r

        rx_r = self.rx_r

        signal = self.signal

        radio_id = self.radio_id

        tx_fp = self.tx_fp

        multi_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_links, Unset):
            multi_links = []
            for multi_links_item_data in self.multi_links:
                multi_links_item = multi_links_item_data.to_dict()
                multi_links.append(multi_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if time is not UNSET:
            field_dict["time"] = time
        if down is not UNSET:
            field_dict["down"] = down
        if up is not UNSET:
            field_dict["up"] = up
        if down_rate is not UNSET:
            field_dict["downRate"] = down_rate
        if up_rate is not UNSET:
            field_dict["upRate"] = up_rate
        if tx_r is not UNSET:
            field_dict["txR"] = tx_r
        if rx_r is not UNSET:
            field_dict["rxR"] = rx_r
        if signal is not UNSET:
            field_dict["signal"] = signal
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if tx_fp is not UNSET:
            field_dict["txFP"] = tx_fp
        if multi_links is not UNSET:
            field_dict["multiLinks"] = multi_links

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_multi_link_info import ClientMultiLinkInfo

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        wireless = d.pop("wireless", UNSET)

        time = d.pop("time", UNSET)

        down = d.pop("down", UNSET)

        up = d.pop("up", UNSET)

        down_rate = d.pop("downRate", UNSET)

        up_rate = d.pop("upRate", UNSET)

        tx_r = d.pop("txR", UNSET)

        rx_r = d.pop("rxR", UNSET)

        signal = d.pop("signal", UNSET)

        radio_id = d.pop("radioId", UNSET)

        tx_fp = d.pop("txFP", UNSET)

        _multi_links = d.pop("multiLinks", UNSET)
        multi_links: list[ClientMultiLinkInfo] | Unset = UNSET
        if _multi_links is not UNSET:
            multi_links = []
            for multi_links_item_data in _multi_links:
                multi_links_item = ClientMultiLinkInfo.from_dict(multi_links_item_data)

                multi_links.append(multi_links_item)

        client_statistical_data_detail = cls(
            mac=mac,
            wireless=wireless,
            time=time,
            down=down,
            up=up,
            down_rate=down_rate,
            up_rate=up_rate,
            tx_r=tx_r,
            rx_r=rx_r,
            signal=signal,
            radio_id=radio_id,
            tx_fp=tx_fp,
            multi_links=multi_links,
        )

        client_statistical_data_detail.additional_properties = d
        return client_statistical_data_detail

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
