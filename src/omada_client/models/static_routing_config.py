from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticRoutingConfig")


@_attrs_define
class StaticRoutingConfig:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Status
        destinations (list[str]): IP address/SubNet
        route_type (int): RouteType should be a value as follows: 0: NextHop; 1: Interface
        metric (int): Metric should be within the range of 0–15.
        next_hop_ip (str | Unset): Only for routeType:0 or routeType:1 and selected WAN is Static IP/Dynamic IP mode
        interface_type (int | Unset): Only for routeType:1, interfaceType should be a value as follows: 0:
            Internet(WAN); 1: Network(LAN); 2: L2TP, 3: PPTP, 5: Virtual WAN.
        interface_id (str | Unset): Interface ID, for example: if interfaceType is network, interfaceId should be LAN
            network ID. LAN Network can be created using 'Create LAN network' interface, and LAN Network ID can be obtained
            from 'Get LAN network list' interface.
    """

    name: str
    status: bool
    destinations: list[str]
    route_type: int
    metric: int
    next_hop_ip: str | Unset = UNSET
    interface_type: int | Unset = UNSET
    interface_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        destinations = self.destinations

        route_type = self.route_type

        metric = self.metric

        next_hop_ip = self.next_hop_ip

        interface_type = self.interface_type

        interface_id = self.interface_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "destinations": destinations,
                "routeType": route_type,
                "metric": metric,
            }
        )
        if next_hop_ip is not UNSET:
            field_dict["nextHopIp"] = next_hop_ip
        if interface_type is not UNSET:
            field_dict["interfaceType"] = interface_type
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        destinations = cast(list[str], d.pop("destinations"))

        route_type = d.pop("routeType")

        metric = d.pop("metric")

        next_hop_ip = d.pop("nextHopIp", UNSET)

        interface_type = d.pop("interfaceType", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        static_routing_config = cls(
            name=name,
            status=status,
            destinations=destinations,
            route_type=route_type,
            metric=metric,
            next_hop_ip=next_hop_ip,
            interface_type=interface_type,
            interface_id=interface_id,
        )

        static_routing_config.additional_properties = d
        return static_routing_config

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
