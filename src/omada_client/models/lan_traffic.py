from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanTraffic")


@_attrs_define
class LanTraffic:
    """LAN traffic info

    Attributes:
        rx_pkts (int | Unset): Total RX packets
        tx_pkts (int | Unset): Total TX packets
        rx (int | Unset): Total RX bytes, Unit: Byte
        tx (int | Unset): Total TX bytes, Unit: Byte
        rx_drop_pkts (int | Unset): RX dropped packets
        tx_drop_pkts (int | Unset): TX dropped packets
        rx_err_pkts (int | Unset): RX error packets
        tx_err_pkts (int | Unset): TX error packets
    """

    rx_pkts: int | Unset = UNSET
    tx_pkts: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx: int | Unset = UNSET
    rx_drop_pkts: int | Unset = UNSET
    tx_drop_pkts: int | Unset = UNSET
    rx_err_pkts: int | Unset = UNSET
    tx_err_pkts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rx_pkts = self.rx_pkts

        tx_pkts = self.tx_pkts

        rx = self.rx

        tx = self.tx

        rx_drop_pkts = self.rx_drop_pkts

        tx_drop_pkts = self.tx_drop_pkts

        rx_err_pkts = self.rx_err_pkts

        tx_err_pkts = self.tx_err_pkts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rx_pkts is not UNSET:
            field_dict["rxPkts"] = rx_pkts
        if tx_pkts is not UNSET:
            field_dict["txPkts"] = tx_pkts
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx_drop_pkts is not UNSET:
            field_dict["rxDropPkts"] = rx_drop_pkts
        if tx_drop_pkts is not UNSET:
            field_dict["txDropPkts"] = tx_drop_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rx_pkts = d.pop("rxPkts", UNSET)

        tx_pkts = d.pop("txPkts", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        rx_drop_pkts = d.pop("rxDropPkts", UNSET)

        tx_drop_pkts = d.pop("txDropPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        lan_traffic = cls(
            rx_pkts=rx_pkts,
            tx_pkts=tx_pkts,
            rx=rx,
            tx=tx,
            rx_drop_pkts=rx_drop_pkts,
            tx_drop_pkts=tx_drop_pkts,
            rx_err_pkts=rx_err_pkts,
            tx_err_pkts=tx_err_pkts,
        )

        lan_traffic.additional_properties = d
        return lan_traffic

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
