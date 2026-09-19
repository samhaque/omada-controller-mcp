from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessUpLink")


@_attrs_define
class WirelessUpLink:
    """Wireless UpLink Info

    Attributes:
        tx_rate (str | Unset): Tx Rate
        rx_rate (str | Unset): Rx Rate
        tx (int | Unset): Tx
        rx (int | Unset): Rx
        rssi (int | Unset): Rssi
        rssi_percent (float | Unset): Rssi Percent
    """

    tx_rate: str | Unset = UNSET
    rx_rate: str | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    rssi: int | Unset = UNSET
    rssi_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        tx = self.tx

        rx = self.rx

        rssi = self.rssi

        rssi_percent = self.rssi_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if rssi_percent is not UNSET:
            field_dict["rssiPercent"] = rssi_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        rssi = d.pop("rssi", UNSET)

        rssi_percent = d.pop("rssiPercent", UNSET)

        wireless_up_link = cls(
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            tx=tx,
            rx=rx,
            rssi=rssi,
            rssi_percent=rssi_percent,
        )

        wireless_up_link.additional_properties = d
        return wireless_up_link

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
