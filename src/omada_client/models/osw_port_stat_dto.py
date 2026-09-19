from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswPortStatDTO")


@_attrs_define
class OswPortStatDTO:
    """
    Attributes:
        port (int | Unset):
        standard_port (str | Unset):
        tx (int | Unset):
        rx (int | Unset):
        tx_rate (int | Unset):
        rx_rate (int | Unset):
        tx_pkts (int | Unset):
        rx_pkts (int | Unset):
        tx_broad_pkts (int | Unset):
        rx_broad_pkts (int | Unset):
        tx_multi_pkts (int | Unset):
        rx_multi_pkts (int | Unset):
        drop_pkts (int | Unset):
        tx_err_pkts (int | Unset):
        rx_err_pkts (int | Unset):
        link_down_cnt (int | Unset):
    """

    port: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx_pkts: int | Unset = UNSET
    rx_pkts: int | Unset = UNSET
    tx_broad_pkts: int | Unset = UNSET
    rx_broad_pkts: int | Unset = UNSET
    tx_multi_pkts: int | Unset = UNSET
    rx_multi_pkts: int | Unset = UNSET
    drop_pkts: int | Unset = UNSET
    tx_err_pkts: int | Unset = UNSET
    rx_err_pkts: int | Unset = UNSET
    link_down_cnt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        tx = self.tx

        rx = self.rx

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        tx_pkts = self.tx_pkts

        rx_pkts = self.rx_pkts

        tx_broad_pkts = self.tx_broad_pkts

        rx_broad_pkts = self.rx_broad_pkts

        tx_multi_pkts = self.tx_multi_pkts

        rx_multi_pkts = self.rx_multi_pkts

        drop_pkts = self.drop_pkts

        tx_err_pkts = self.tx_err_pkts

        rx_err_pkts = self.rx_err_pkts

        link_down_cnt = self.link_down_cnt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_pkts is not UNSET:
            field_dict["txPkts"] = tx_pkts
        if rx_pkts is not UNSET:
            field_dict["rxPkts"] = rx_pkts
        if tx_broad_pkts is not UNSET:
            field_dict["txBroadPkts"] = tx_broad_pkts
        if rx_broad_pkts is not UNSET:
            field_dict["rxBroadPkts"] = rx_broad_pkts
        if tx_multi_pkts is not UNSET:
            field_dict["txMultiPkts"] = tx_multi_pkts
        if rx_multi_pkts is not UNSET:
            field_dict["rxMultiPkts"] = rx_multi_pkts
        if drop_pkts is not UNSET:
            field_dict["dropPkts"] = drop_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if link_down_cnt is not UNSET:
            field_dict["linkDownCnt"] = link_down_cnt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx_pkts = d.pop("txPkts", UNSET)

        rx_pkts = d.pop("rxPkts", UNSET)

        tx_broad_pkts = d.pop("txBroadPkts", UNSET)

        rx_broad_pkts = d.pop("rxBroadPkts", UNSET)

        tx_multi_pkts = d.pop("txMultiPkts", UNSET)

        rx_multi_pkts = d.pop("rxMultiPkts", UNSET)

        drop_pkts = d.pop("dropPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        link_down_cnt = d.pop("linkDownCnt", UNSET)

        osw_port_stat_dto = cls(
            port=port,
            standard_port=standard_port,
            tx=tx,
            rx=rx,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            tx_pkts=tx_pkts,
            rx_pkts=rx_pkts,
            tx_broad_pkts=tx_broad_pkts,
            rx_broad_pkts=rx_broad_pkts,
            tx_multi_pkts=tx_multi_pkts,
            rx_multi_pkts=rx_multi_pkts,
            drop_pkts=drop_pkts,
            tx_err_pkts=tx_err_pkts,
            rx_err_pkts=rx_err_pkts,
            link_down_cnt=link_down_cnt,
        )

        osw_port_stat_dto.additional_properties = d
        return osw_port_stat_dto

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
