from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OltDevCapVO")


@_attrs_define
class OltDevCapVO:
    """Capability of device

    Attributes:
        pon_port_count (int | Unset): Number of pon ports
        lag_count (int | Unset): Number of LAGs(Link Aggregation Group)
        network_check_support (bool | Unset): Whether this OLT supports network check function
        ping_support (bool | Unset): Whether this OLT supports ping function
        trace_route_support (bool | Unset): Whether this OLT supports traceRoute function
    """

    pon_port_count: int | Unset = UNSET
    lag_count: int | Unset = UNSET
    network_check_support: bool | Unset = UNSET
    ping_support: bool | Unset = UNSET
    trace_route_support: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pon_port_count = self.pon_port_count

        lag_count = self.lag_count

        network_check_support = self.network_check_support

        ping_support = self.ping_support

        trace_route_support = self.trace_route_support

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pon_port_count is not UNSET:
            field_dict["ponPortCount"] = pon_port_count
        if lag_count is not UNSET:
            field_dict["lagCount"] = lag_count
        if network_check_support is not UNSET:
            field_dict["networkCheckSupport"] = network_check_support
        if ping_support is not UNSET:
            field_dict["pingSupport"] = ping_support
        if trace_route_support is not UNSET:
            field_dict["traceRouteSupport"] = trace_route_support

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pon_port_count = d.pop("ponPortCount", UNSET)

        lag_count = d.pop("lagCount", UNSET)

        network_check_support = d.pop("networkCheckSupport", UNSET)

        ping_support = d.pop("pingSupport", UNSET)

        trace_route_support = d.pop("traceRouteSupport", UNSET)

        olt_dev_cap_vo = cls(
            pon_port_count=pon_port_count,
            lag_count=lag_count,
            network_check_support=network_check_support,
            ping_support=ping_support,
            trace_route_support=trace_route_support,
        )

        olt_dev_cap_vo.additional_properties = d
        return olt_dev_cap_vo

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
