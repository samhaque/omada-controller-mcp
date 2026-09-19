from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessUpLinkInfo")


@_attrs_define
class WirelessUpLinkInfo:
    """Exists when connected to upper level device via wireless connection

    Attributes:
        tx_rate (str | Unset): Tx Rate
        rx_rate (str | Unset): Rx Rate
        rssi (int | Unset): Rssi
        rssi_percent (int | Unset): Rssi percent
        rx_drop_pkts (int | Unset): Rx Dropped Packets
        tx_drop_pkts (int | Unset): Tx Dropped Packets
        rx_err_pkts (int | Unset): Rx Error Packets
        tx_err_pkts (int | Unset): Tx Error Packets
        snr (int | Unset): Wireless P2P Ap Snr
    """

    tx_rate: str | Unset = UNSET
    rx_rate: str | Unset = UNSET
    rssi: int | Unset = UNSET
    rssi_percent: int | Unset = UNSET
    rx_drop_pkts: int | Unset = UNSET
    tx_drop_pkts: int | Unset = UNSET
    rx_err_pkts: int | Unset = UNSET
    tx_err_pkts: int | Unset = UNSET
    snr: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        rssi = self.rssi

        rssi_percent = self.rssi_percent

        rx_drop_pkts = self.rx_drop_pkts

        tx_drop_pkts = self.tx_drop_pkts

        rx_err_pkts = self.rx_err_pkts

        tx_err_pkts = self.tx_err_pkts

        snr = self.snr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if rssi_percent is not UNSET:
            field_dict["rssiPercent"] = rssi_percent
        if rx_drop_pkts is not UNSET:
            field_dict["rxDropPkts"] = rx_drop_pkts
        if tx_drop_pkts is not UNSET:
            field_dict["txDropPkts"] = tx_drop_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts
        if snr is not UNSET:
            field_dict["snr"] = snr

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        rssi = d.pop("rssi", UNSET)

        rssi_percent = d.pop("rssiPercent", UNSET)

        rx_drop_pkts = d.pop("rxDropPkts", UNSET)

        tx_drop_pkts = d.pop("txDropPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        snr = d.pop("snr", UNSET)

        wireless_up_link_info = cls(
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            rssi=rssi,
            rssi_percent=rssi_percent,
            rx_drop_pkts=rx_drop_pkts,
            tx_drop_pkts=tx_drop_pkts,
            rx_err_pkts=rx_err_pkts,
            tx_err_pkts=tx_err_pkts,
            snr=snr,
        )

        wireless_up_link_info.additional_properties = d
        return wireless_up_link_info

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
