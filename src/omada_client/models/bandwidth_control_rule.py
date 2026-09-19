from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandwidthControlRule")


@_attrs_define
class BandwidthControlRule:
    """
    Attributes:
        name (str): Name should contain 1 to 64 characters.
        status (bool): Status of the bandwidth control rule.
        source_ids (list[str]): Source IDs of the bandwidth control rule. Network can be created using 'Create LAN
            network' interface, and network ID can be obtained from 'Get LAN network list' interface. IP group can be
            created using 'Create a new group profile' interface, and IP group ID can be obtained from 'Get group profile
            list' interface.
        wan_port_ids (list[str]): WAN port IDs of the bandwidth control rule.WAN port ID can be obtained from 'Get
            internet basic info' interface.
        upstream_bandwidth (int): Upstream bandwidth should be within the range of 1–9999999.
        upstream_bandwidth_unit (int): Upstream bandwidth unit should be a value as follows: 1: Kbps, 2: Mbps.
        downstream_bandwidth (int): Downstream bandwidth should be within the range of 1–9999999.
        downstream_bandwidth_unit (int): Downstream bandwidth unit should be a value as follows: 1: Kbps, 2: Mbps.
        mode (int): Mode should be a value as follows: 0: share; 1: individual.
        id (str | Unset): ID of the bandwidth control rule.
        index (int | Unset): Index of the bandwidth control rule.
        source_type (int | Unset): Source type should be a value as follows: 0: network; 1: IP group.
    """

    name: str
    status: bool
    source_ids: list[str]
    wan_port_ids: list[str]
    upstream_bandwidth: int
    upstream_bandwidth_unit: int
    downstream_bandwidth: int
    downstream_bandwidth_unit: int
    mode: int
    id: str | Unset = UNSET
    index: int | Unset = UNSET
    source_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        source_ids = self.source_ids

        wan_port_ids = self.wan_port_ids

        upstream_bandwidth = self.upstream_bandwidth

        upstream_bandwidth_unit = self.upstream_bandwidth_unit

        downstream_bandwidth = self.downstream_bandwidth

        downstream_bandwidth_unit = self.downstream_bandwidth_unit

        mode = self.mode

        id = self.id

        index = self.index

        source_type = self.source_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "sourceIds": source_ids,
                "wanPortIds": wan_port_ids,
                "upstreamBandwidth": upstream_bandwidth,
                "upstreamBandwidthUnit": upstream_bandwidth_unit,
                "downstreamBandwidth": downstream_bandwidth,
                "downstreamBandwidthUnit": downstream_bandwidth_unit,
                "mode": mode,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        source_ids = cast(list[str], d.pop("sourceIds"))

        wan_port_ids = cast(list[str], d.pop("wanPortIds"))

        upstream_bandwidth = d.pop("upstreamBandwidth")

        upstream_bandwidth_unit = d.pop("upstreamBandwidthUnit")

        downstream_bandwidth = d.pop("downstreamBandwidth")

        downstream_bandwidth_unit = d.pop("downstreamBandwidthUnit")

        mode = d.pop("mode")

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        source_type = d.pop("sourceType", UNSET)

        bandwidth_control_rule = cls(
            name=name,
            status=status,
            source_ids=source_ids,
            wan_port_ids=wan_port_ids,
            upstream_bandwidth=upstream_bandwidth,
            upstream_bandwidth_unit=upstream_bandwidth_unit,
            downstream_bandwidth=downstream_bandwidth,
            downstream_bandwidth_unit=downstream_bandwidth_unit,
            mode=mode,
            id=id,
            index=index,
            source_type=source_type,
        )

        bandwidth_control_rule.additional_properties = d
        return bandwidth_control_rule

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
