from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessSummaryVO")


@_attrs_define
class WirelessSummaryVO:
    """
    Attributes:
        total (int | Unset): total traffic
        rx_total (int | Unset): rx traffic
        tx_total (int | Unset): tx traffic
        wireless_2_g_total (int | Unset): 2g traffic
        wireless_2_g_rx (int | Unset): 2g client rx traffic
        wireless_2_g_tx (int | Unset): 2g client tx traffic
        wireless_5_g_total (int | Unset): 5g traffic
        wireless_5_g_rx (int | Unset): 5g client rx traffic
        wireless_5_g_tx (int | Unset): 5g client tx traffic
        wireless_6_g_total (int | Unset): 6g traffic
        wireless_6_g_rx (int | Unset): 6g client rx traffic
        wireless_6_g_tx (int | Unset): 6g client tx traffic
    """

    total: int | Unset = UNSET
    rx_total: int | Unset = UNSET
    tx_total: int | Unset = UNSET
    wireless_2_g_total: int | Unset = UNSET
    wireless_2_g_rx: int | Unset = UNSET
    wireless_2_g_tx: int | Unset = UNSET
    wireless_5_g_total: int | Unset = UNSET
    wireless_5_g_rx: int | Unset = UNSET
    wireless_5_g_tx: int | Unset = UNSET
    wireless_6_g_total: int | Unset = UNSET
    wireless_6_g_rx: int | Unset = UNSET
    wireless_6_g_tx: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        rx_total = self.rx_total

        tx_total = self.tx_total

        wireless_2_g_total = self.wireless_2_g_total

        wireless_2_g_rx = self.wireless_2_g_rx

        wireless_2_g_tx = self.wireless_2_g_tx

        wireless_5_g_total = self.wireless_5_g_total

        wireless_5_g_rx = self.wireless_5_g_rx

        wireless_5_g_tx = self.wireless_5_g_tx

        wireless_6_g_total = self.wireless_6_g_total

        wireless_6_g_rx = self.wireless_6_g_rx

        wireless_6_g_tx = self.wireless_6_g_tx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if rx_total is not UNSET:
            field_dict["rxTotal"] = rx_total
        if tx_total is not UNSET:
            field_dict["txTotal"] = tx_total
        if wireless_2_g_total is not UNSET:
            field_dict["wireless2gTotal"] = wireless_2_g_total
        if wireless_2_g_rx is not UNSET:
            field_dict["wireless2gRx"] = wireless_2_g_rx
        if wireless_2_g_tx is not UNSET:
            field_dict["wireless2gTx"] = wireless_2_g_tx
        if wireless_5_g_total is not UNSET:
            field_dict["wireless5gTotal"] = wireless_5_g_total
        if wireless_5_g_rx is not UNSET:
            field_dict["wireless5gRx"] = wireless_5_g_rx
        if wireless_5_g_tx is not UNSET:
            field_dict["wireless5gTx"] = wireless_5_g_tx
        if wireless_6_g_total is not UNSET:
            field_dict["wireless6gTotal"] = wireless_6_g_total
        if wireless_6_g_rx is not UNSET:
            field_dict["wireless6gRx"] = wireless_6_g_rx
        if wireless_6_g_tx is not UNSET:
            field_dict["wireless6gTx"] = wireless_6_g_tx

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        rx_total = d.pop("rxTotal", UNSET)

        tx_total = d.pop("txTotal", UNSET)

        wireless_2_g_total = d.pop("wireless2gTotal", UNSET)

        wireless_2_g_rx = d.pop("wireless2gRx", UNSET)

        wireless_2_g_tx = d.pop("wireless2gTx", UNSET)

        wireless_5_g_total = d.pop("wireless5gTotal", UNSET)

        wireless_5_g_rx = d.pop("wireless5gRx", UNSET)

        wireless_5_g_tx = d.pop("wireless5gTx", UNSET)

        wireless_6_g_total = d.pop("wireless6gTotal", UNSET)

        wireless_6_g_rx = d.pop("wireless6gRx", UNSET)

        wireless_6_g_tx = d.pop("wireless6gTx", UNSET)

        wireless_summary_vo = cls(
            total=total,
            rx_total=rx_total,
            tx_total=tx_total,
            wireless_2_g_total=wireless_2_g_total,
            wireless_2_g_rx=wireless_2_g_rx,
            wireless_2_g_tx=wireless_2_g_tx,
            wireless_5_g_total=wireless_5_g_total,
            wireless_5_g_rx=wireless_5_g_rx,
            wireless_5_g_tx=wireless_5_g_tx,
            wireless_6_g_total=wireless_6_g_total,
            wireless_6_g_rx=wireless_6_g_rx,
            wireless_6_g_tx=wireless_6_g_tx,
        )

        wireless_summary_vo.additional_properties = d
        return wireless_summary_vo

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
