from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTrafficActivity")


@_attrs_define
class DeviceTrafficActivity:
    """Wired network total traffic timing list

    Attributes:
        time (int | Unset): The timestamp of this data sample, in seconds, such as 1682000000
        tx_data (float | Unset): Uplink traffic in MB
        rx_data (float | Unset): Downlink traffic in MB
    """

    time: int | Unset = UNSET
    tx_data: float | Unset = UNSET
    rx_data: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        tx_data = self.tx_data

        rx_data = self.rx_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if tx_data is not UNSET:
            field_dict["txData"] = tx_data
        if rx_data is not UNSET:
            field_dict["rxData"] = rx_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        tx_data = d.pop("txData", UNSET)

        rx_data = d.pop("rxData", UNSET)

        device_traffic_activity = cls(
            time=time,
            tx_data=tx_data,
            rx_data=rx_data,
        )

        device_traffic_activity.additional_properties = d
        return device_traffic_activity

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
