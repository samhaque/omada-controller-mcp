from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortBandwidthVO")


@_attrs_define
class PortBandwidthVO:
    """Set port bandwidth info list.

    Attributes:
        port_uuid (str | Unset): Port uuid.
        rx_bandwidth (int | Unset): Set down link bandwidth.
        tx_bandwidth (int | Unset): Set up link bandwidth.
    """

    port_uuid: str | Unset = UNSET
    rx_bandwidth: int | Unset = UNSET
    tx_bandwidth: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        rx_bandwidth = self.rx_bandwidth

        tx_bandwidth = self.tx_bandwidth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if rx_bandwidth is not UNSET:
            field_dict["rxBandwidth"] = rx_bandwidth
        if tx_bandwidth is not UNSET:
            field_dict["txBandwidth"] = tx_bandwidth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid", UNSET)

        rx_bandwidth = d.pop("rxBandwidth", UNSET)

        tx_bandwidth = d.pop("txBandwidth", UNSET)

        port_bandwidth_vo = cls(
            port_uuid=port_uuid,
            rx_bandwidth=rx_bandwidth,
            tx_bandwidth=tx_bandwidth,
        )

        port_bandwidth_vo.additional_properties = d
        return port_bandwidth_vo

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
