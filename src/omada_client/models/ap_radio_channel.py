from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApRadioChannel")


@_attrs_define
class ApRadioChannel:
    """
    Attributes:
        actual_channel (str | Unset): Actual channel of the device
        max_tx_rate (int | Unset): TxRate of the device
        tx_power (int | Unset): TxPower of the device
        region (int | Unset): Region code of the device
        band_width (str | Unset): BandWidth of the device
        rd_mode (str | Unset): RdMode of the device
        tx_util (int | Unset): TxUtil of the device, value range [0, 100].
        rx_util (int | Unset): RxUtil of the device, value range [0, 100].
        inter_util (int | Unset): InterUtil of the device, value range [0, 100].
        busy_util (int | Unset): BusyUtil of the device(Support by MTK device), value range [0, 100].
        ai_roaming_offset (int | Unset): AI Roaming offset of the device
    """

    actual_channel: str | Unset = UNSET
    max_tx_rate: int | Unset = UNSET
    tx_power: int | Unset = UNSET
    region: int | Unset = UNSET
    band_width: str | Unset = UNSET
    rd_mode: str | Unset = UNSET
    tx_util: int | Unset = UNSET
    rx_util: int | Unset = UNSET
    inter_util: int | Unset = UNSET
    busy_util: int | Unset = UNSET
    ai_roaming_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_channel = self.actual_channel

        max_tx_rate = self.max_tx_rate

        tx_power = self.tx_power

        region = self.region

        band_width = self.band_width

        rd_mode = self.rd_mode

        tx_util = self.tx_util

        rx_util = self.rx_util

        inter_util = self.inter_util

        busy_util = self.busy_util

        ai_roaming_offset = self.ai_roaming_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_channel is not UNSET:
            field_dict["actualChannel"] = actual_channel
        if max_tx_rate is not UNSET:
            field_dict["maxTxRate"] = max_tx_rate
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if region is not UNSET:
            field_dict["region"] = region
        if band_width is not UNSET:
            field_dict["bandWidth"] = band_width
        if rd_mode is not UNSET:
            field_dict["rdMode"] = rd_mode
        if tx_util is not UNSET:
            field_dict["txUtil"] = tx_util
        if rx_util is not UNSET:
            field_dict["rxUtil"] = rx_util
        if inter_util is not UNSET:
            field_dict["interUtil"] = inter_util
        if busy_util is not UNSET:
            field_dict["busyUtil"] = busy_util
        if ai_roaming_offset is not UNSET:
            field_dict["aiRoamingOffset"] = ai_roaming_offset

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        actual_channel = d.pop("actualChannel", UNSET)

        max_tx_rate = d.pop("maxTxRate", UNSET)

        tx_power = d.pop("txPower", UNSET)

        region = d.pop("region", UNSET)

        band_width = d.pop("bandWidth", UNSET)

        rd_mode = d.pop("rdMode", UNSET)

        tx_util = d.pop("txUtil", UNSET)

        rx_util = d.pop("rxUtil", UNSET)

        inter_util = d.pop("interUtil", UNSET)

        busy_util = d.pop("busyUtil", UNSET)

        ai_roaming_offset = d.pop("aiRoamingOffset", UNSET)

        ap_radio_channel = cls(
            actual_channel=actual_channel,
            max_tx_rate=max_tx_rate,
            tx_power=tx_power,
            region=region,
            band_width=band_width,
            rd_mode=rd_mode,
            tx_util=tx_util,
            rx_util=rx_util,
            inter_util=inter_util,
            busy_util=busy_util,
            ai_roaming_offset=ai_roaming_offset,
        )

        ap_radio_channel.additional_properties = d
        return ap_radio_channel

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
