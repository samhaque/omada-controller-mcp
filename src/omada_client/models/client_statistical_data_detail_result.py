from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_statistical_data_detail import ClientStatisticalDataDetail
    from ..models.client_statistical_data_detail_result_avg_signal import (
        ClientStatisticalDataDetailResultAvgSignal,
    )


T = TypeVar("T", bound="ClientStatisticalDataDetailResult")


@_attrs_define
class ClientStatisticalDataDetailResult:
    """
    Attributes:
        total_down (int | Unset): Client total downstream traffic (Byte).
        total_up (int | Unset): Client total upstream traffic (Byte).
        avg_down_rate (int | Unset): Average downlink rate (Byte/s).
        avg_up_rate (int | Unset): Average uplink rate (Byte/s).
        avg_tx_r (int | Unset): (Wireless) Average downlink negotiation rate (bit/s).
        avg_rx_r (int | Unset): (Wireless) Average uplink negotiation rate (bit/s).
        avg_signal (ClientStatisticalDataDetailResultAvgSignal | Unset): (Wireless) Average signal on each channel, the
            key is radioId(0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz), the value is average signal(unit: dBm).
        total_tx_fp (int | Unset): Total number of downstream failed packets.
        stats (list[ClientStatisticalDataDetail] | Unset): Client Statistical Data Detail list.
    """

    total_down: int | Unset = UNSET
    total_up: int | Unset = UNSET
    avg_down_rate: int | Unset = UNSET
    avg_up_rate: int | Unset = UNSET
    avg_tx_r: int | Unset = UNSET
    avg_rx_r: int | Unset = UNSET
    avg_signal: ClientStatisticalDataDetailResultAvgSignal | Unset = UNSET
    total_tx_fp: int | Unset = UNSET
    stats: list[ClientStatisticalDataDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_down = self.total_down

        total_up = self.total_up

        avg_down_rate = self.avg_down_rate

        avg_up_rate = self.avg_up_rate

        avg_tx_r = self.avg_tx_r

        avg_rx_r = self.avg_rx_r

        avg_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_signal, Unset):
            avg_signal = self.avg_signal.to_dict()

        total_tx_fp = self.total_tx_fp

        stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_down is not UNSET:
            field_dict["totalDown"] = total_down
        if total_up is not UNSET:
            field_dict["totalUp"] = total_up
        if avg_down_rate is not UNSET:
            field_dict["avgDownRate"] = avg_down_rate
        if avg_up_rate is not UNSET:
            field_dict["avgUpRate"] = avg_up_rate
        if avg_tx_r is not UNSET:
            field_dict["avgTxR"] = avg_tx_r
        if avg_rx_r is not UNSET:
            field_dict["avgRxR"] = avg_rx_r
        if avg_signal is not UNSET:
            field_dict["avgSignal"] = avg_signal
        if total_tx_fp is not UNSET:
            field_dict["totalTxFP"] = total_tx_fp
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_statistical_data_detail import (
            ClientStatisticalDataDetail,
        )
        from ..models.client_statistical_data_detail_result_avg_signal import (
            ClientStatisticalDataDetailResultAvgSignal,
        )

        d = dict(src_dict)
        total_down = d.pop("totalDown", UNSET)

        total_up = d.pop("totalUp", UNSET)

        avg_down_rate = d.pop("avgDownRate", UNSET)

        avg_up_rate = d.pop("avgUpRate", UNSET)

        avg_tx_r = d.pop("avgTxR", UNSET)

        avg_rx_r = d.pop("avgRxR", UNSET)

        _avg_signal = d.pop("avgSignal", UNSET)
        avg_signal: ClientStatisticalDataDetailResultAvgSignal | Unset
        if isinstance(_avg_signal, Unset):
            avg_signal = UNSET
        else:
            avg_signal = ClientStatisticalDataDetailResultAvgSignal.from_dict(
                _avg_signal
            )

        total_tx_fp = d.pop("totalTxFP", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: list[ClientStatisticalDataDetail] | Unset = UNSET
        if _stats is not UNSET:
            stats = []
            for stats_item_data in _stats:
                stats_item = ClientStatisticalDataDetail.from_dict(stats_item_data)

                stats.append(stats_item)

        client_statistical_data_detail_result = cls(
            total_down=total_down,
            total_up=total_up,
            avg_down_rate=avg_down_rate,
            avg_up_rate=avg_up_rate,
            avg_tx_r=avg_tx_r,
            avg_rx_r=avg_rx_r,
            avg_signal=avg_signal,
            total_tx_fp=total_tx_fp,
            stats=stats,
        )

        client_statistical_data_detail_result.additional_properties = d
        return client_statistical_data_detail_result

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
