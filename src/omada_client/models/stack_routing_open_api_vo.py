from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StackRoutingOpenApiVO")


@_attrs_define
class StackRoutingOpenApiVO:
    """
    Attributes:
        stack_id (str | Unset): Stack ID.
        name (str | Unset): Stack Name.
        distance (int | Unset): Distance.
        destination_ip (str | Unset): Destination IP.
        next_hops (list[str] | Unset): Next IP list.
        next_hop (str | Unset): Next Ip.
        interface_name (list[str] | Unset): Interface Name
        dest_ip_vrf_name (str | Unset): Destination ip vrf name
        next_hop_vrf_name (str | Unset): Next ip vrf name
        next_hops_vrf (list[str] | Unset): Next ip vrf
        metric (int | Unset): Metric
        type_ (str | Unset): Type
    """

    stack_id: str | Unset = UNSET
    name: str | Unset = UNSET
    distance: int | Unset = UNSET
    destination_ip: str | Unset = UNSET
    next_hops: list[str] | Unset = UNSET
    next_hop: str | Unset = UNSET
    interface_name: list[str] | Unset = UNSET
    dest_ip_vrf_name: str | Unset = UNSET
    next_hop_vrf_name: str | Unset = UNSET
    next_hops_vrf: list[str] | Unset = UNSET
    metric: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        name = self.name

        distance = self.distance

        destination_ip = self.destination_ip

        next_hops: list[str] | Unset = UNSET
        if not isinstance(self.next_hops, Unset):
            next_hops = self.next_hops

        next_hop = self.next_hop

        interface_name: list[str] | Unset = UNSET
        if not isinstance(self.interface_name, Unset):
            interface_name = self.interface_name

        dest_ip_vrf_name = self.dest_ip_vrf_name

        next_hop_vrf_name = self.next_hop_vrf_name

        next_hops_vrf: list[str] | Unset = UNSET
        if not isinstance(self.next_hops_vrf, Unset):
            next_hops_vrf = self.next_hops_vrf

        metric = self.metric

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if name is not UNSET:
            field_dict["name"] = name
        if distance is not UNSET:
            field_dict["distance"] = distance
        if destination_ip is not UNSET:
            field_dict["destinationIp"] = destination_ip
        if next_hops is not UNSET:
            field_dict["nextHops"] = next_hops
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if dest_ip_vrf_name is not UNSET:
            field_dict["destIpVrfName"] = dest_ip_vrf_name
        if next_hop_vrf_name is not UNSET:
            field_dict["nextHopVrfName"] = next_hop_vrf_name
        if next_hops_vrf is not UNSET:
            field_dict["nextHopsVrf"] = next_hops_vrf
        if metric is not UNSET:
            field_dict["metric"] = metric
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        name = d.pop("name", UNSET)

        distance = d.pop("distance", UNSET)

        destination_ip = d.pop("destinationIp", UNSET)

        next_hops = cast(list[str], d.pop("nextHops", UNSET))

        next_hop = d.pop("nextHop", UNSET)

        interface_name = cast(list[str], d.pop("interfaceName", UNSET))

        dest_ip_vrf_name = d.pop("destIpVrfName", UNSET)

        next_hop_vrf_name = d.pop("nextHopVrfName", UNSET)

        next_hops_vrf = cast(list[str], d.pop("nextHopsVrf", UNSET))

        metric = d.pop("metric", UNSET)

        type_ = d.pop("type", UNSET)

        stack_routing_open_api_vo = cls(
            stack_id=stack_id,
            name=name,
            distance=distance,
            destination_ip=destination_ip,
            next_hops=next_hops,
            next_hop=next_hop,
            interface_name=interface_name,
            dest_ip_vrf_name=dest_ip_vrf_name,
            next_hop_vrf_name=next_hop_vrf_name,
            next_hops_vrf=next_hops_vrf,
            metric=metric,
            type_=type_,
        )

        stack_routing_open_api_vo.additional_properties = d
        return stack_routing_open_api_vo

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
