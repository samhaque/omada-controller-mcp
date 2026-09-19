from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stack_msg_open_api_vo import StackMsgOpenApiVO


T = TypeVar("T", bound="OswRoutingOpenApiVO")


@_attrs_define
class OswRoutingOpenApiVO:
    """
    Attributes:
        mac (str | Unset): Switch Mac.
        name (str | Unset): Switch Name.
        distance (int | Unset): Distance.
        destination_ip (str | Unset): Destination IP.
        dest_ip_vrf (str | Unset): Destination Vrf.
        osw_destination_ips (list[str] | Unset): Destination IP list.
        next_hops (list[str] | Unset): Next IP list.
        next_hop (str | Unset): Next Ip.
        next_hop_vrf (str | Unset): Next Vrf.
        next_hops_vrf (list[str] | Unset): Next vrfs
        interface_name (list[str] | Unset): Interface Name
        metric (int | Unset): Metric
        type_ (str | Unset): Type
        stack_msg (StackMsgOpenApiVO | Unset): The information of the stack to which it belongs.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    distance: int | Unset = UNSET
    destination_ip: str | Unset = UNSET
    dest_ip_vrf: str | Unset = UNSET
    osw_destination_ips: list[str] | Unset = UNSET
    next_hops: list[str] | Unset = UNSET
    next_hop: str | Unset = UNSET
    next_hop_vrf: str | Unset = UNSET
    next_hops_vrf: list[str] | Unset = UNSET
    interface_name: list[str] | Unset = UNSET
    metric: int | Unset = UNSET
    type_: str | Unset = UNSET
    stack_msg: StackMsgOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        distance = self.distance

        destination_ip = self.destination_ip

        dest_ip_vrf = self.dest_ip_vrf

        osw_destination_ips: list[str] | Unset = UNSET
        if not isinstance(self.osw_destination_ips, Unset):
            osw_destination_ips = self.osw_destination_ips

        next_hops: list[str] | Unset = UNSET
        if not isinstance(self.next_hops, Unset):
            next_hops = self.next_hops

        next_hop = self.next_hop

        next_hop_vrf = self.next_hop_vrf

        next_hops_vrf: list[str] | Unset = UNSET
        if not isinstance(self.next_hops_vrf, Unset):
            next_hops_vrf = self.next_hops_vrf

        interface_name: list[str] | Unset = UNSET
        if not isinstance(self.interface_name, Unset):
            interface_name = self.interface_name

        metric = self.metric

        type_ = self.type_

        stack_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_msg, Unset):
            stack_msg = self.stack_msg.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if distance is not UNSET:
            field_dict["distance"] = distance
        if destination_ip is not UNSET:
            field_dict["destinationIp"] = destination_ip
        if dest_ip_vrf is not UNSET:
            field_dict["destIpVrf"] = dest_ip_vrf
        if osw_destination_ips is not UNSET:
            field_dict["oswDestinationIps"] = osw_destination_ips
        if next_hops is not UNSET:
            field_dict["nextHops"] = next_hops
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if next_hop_vrf is not UNSET:
            field_dict["nextHopVrf"] = next_hop_vrf
        if next_hops_vrf is not UNSET:
            field_dict["nextHopsVrf"] = next_hops_vrf
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if metric is not UNSET:
            field_dict["metric"] = metric
        if type_ is not UNSET:
            field_dict["type"] = type_
        if stack_msg is not UNSET:
            field_dict["stackMsg"] = stack_msg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stack_msg_open_api_vo import StackMsgOpenApiVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        distance = d.pop("distance", UNSET)

        destination_ip = d.pop("destinationIp", UNSET)

        dest_ip_vrf = d.pop("destIpVrf", UNSET)

        osw_destination_ips = cast(list[str], d.pop("oswDestinationIps", UNSET))

        next_hops = cast(list[str], d.pop("nextHops", UNSET))

        next_hop = d.pop("nextHop", UNSET)

        next_hop_vrf = d.pop("nextHopVrf", UNSET)

        next_hops_vrf = cast(list[str], d.pop("nextHopsVrf", UNSET))

        interface_name = cast(list[str], d.pop("interfaceName", UNSET))

        metric = d.pop("metric", UNSET)

        type_ = d.pop("type", UNSET)

        _stack_msg = d.pop("stackMsg", UNSET)
        stack_msg: StackMsgOpenApiVO | Unset
        if isinstance(_stack_msg, Unset):
            stack_msg = UNSET
        else:
            stack_msg = StackMsgOpenApiVO.from_dict(_stack_msg)

        osw_routing_open_api_vo = cls(
            mac=mac,
            name=name,
            distance=distance,
            destination_ip=destination_ip,
            dest_ip_vrf=dest_ip_vrf,
            osw_destination_ips=osw_destination_ips,
            next_hops=next_hops,
            next_hop=next_hop,
            next_hop_vrf=next_hop_vrf,
            next_hops_vrf=next_hops_vrf,
            interface_name=interface_name,
            metric=metric,
            type_=type_,
            stack_msg=stack_msg,
        )

        osw_routing_open_api_vo.additional_properties = d
        return osw_routing_open_api_vo

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
