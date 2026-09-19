from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandwidthPortSetting")


@_attrs_define
class BandwidthPortSetting:
    """Bandwidth port settings of the bandwidth control.

    Attributes:
        port_uuid (str): Port uuid.
        upstream_bandwidth (int | Unset): Upstream bandwidth should be within the range of 1–9999999.
        upstream_bandwidth_unit (int | Unset): Upstream bandwidth unit should be a value as follows: 1: Kbps, 2: Mbps.
        downstream_bandwidth (int | Unset): Downstream bandwidth should be within the range of 1–9999999.
        downstream_bandwidth_unit (int | Unset): Downstream bandwidth unit should be a value as follows: 1: Kbps, 2:
            Mbps.
    """

    port_uuid: str
    upstream_bandwidth: int | Unset = UNSET
    upstream_bandwidth_unit: int | Unset = UNSET
    downstream_bandwidth: int | Unset = UNSET
    downstream_bandwidth_unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        upstream_bandwidth = self.upstream_bandwidth

        upstream_bandwidth_unit = self.upstream_bandwidth_unit

        downstream_bandwidth = self.downstream_bandwidth

        downstream_bandwidth_unit = self.downstream_bandwidth_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portUuid": port_uuid,
            }
        )
        if upstream_bandwidth is not UNSET:
            field_dict["upstreamBandwidth"] = upstream_bandwidth
        if upstream_bandwidth_unit is not UNSET:
            field_dict["upstreamBandwidthUnit"] = upstream_bandwidth_unit
        if downstream_bandwidth is not UNSET:
            field_dict["downstreamBandwidth"] = downstream_bandwidth
        if downstream_bandwidth_unit is not UNSET:
            field_dict["downstreamBandwidthUnit"] = downstream_bandwidth_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid")

        upstream_bandwidth = d.pop("upstreamBandwidth", UNSET)

        upstream_bandwidth_unit = d.pop("upstreamBandwidthUnit", UNSET)

        downstream_bandwidth = d.pop("downstreamBandwidth", UNSET)

        downstream_bandwidth_unit = d.pop("downstreamBandwidthUnit", UNSET)

        bandwidth_port_setting = cls(
            port_uuid=port_uuid,
            upstream_bandwidth=upstream_bandwidth,
            upstream_bandwidth_unit=upstream_bandwidth_unit,
            downstream_bandwidth=downstream_bandwidth,
            downstream_bandwidth_unit=downstream_bandwidth_unit,
        )

        bandwidth_port_setting.additional_properties = d
        return bandwidth_port_setting

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
