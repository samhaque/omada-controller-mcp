from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="StaticRoutingInfo")


@_attrs_define
class StaticRoutingInfo:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Status
        destinations (list[str]): IP address/SubNet, up to 16 entries are allowed for the destinations list.
        route_type (int): RouteType should be a value as follows: 0: NextHop; 1: Interface
        metric (int): Metric should be within the range of 0–15.
        id (str | Unset): ID
        next_hop_ip (str | Unset): Only for routeType:0 or routeType:1 and selected WAN is Static IP/Dynamic IP/MAP-E
            mode
        interface_type (int | Unset): Only for routeType:1, interfaceType should be a value as follows: 0:
            Internet(WAN); 1: Network(LAN); 2: L2TP, 3: PPTP, 5: Virtual WAN.
        interface_id (str | Unset): Interface ID, for example: if interfaceType is network, interfaceId should be LAN
            network ID. LAN Network can be created using 'Create LAN network' interface, and LAN Network ID can be obtained
            from 'Get LAN network list' interface.
        exist_vpn_client (bool | Unset): Whether the interface option exists VPN client
        exist_virtual_wan (bool | Unset): Whether the interface option exists virtual WAN
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    name: str
    status: bool
    destinations: list[str]
    route_type: int
    metric: int
    id: str | Unset = UNSET
    next_hop_ip: str | Unset = UNSET
    interface_type: int | Unset = UNSET
    interface_id: str | Unset = UNSET
    exist_vpn_client: bool | Unset = UNSET
    exist_virtual_wan: bool | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        destinations = self.destinations

        route_type = self.route_type

        metric = self.metric

        id = self.id

        next_hop_ip = self.next_hop_ip

        interface_type = self.interface_type

        interface_id = self.interface_id

        exist_vpn_client = self.exist_vpn_client

        exist_virtual_wan = self.exist_virtual_wan

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

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
        if id is not UNSET:
            field_dict["id"] = id
        if next_hop_ip is not UNSET:
            field_dict["nextHopIp"] = next_hop_ip
        if interface_type is not UNSET:
            field_dict["interfaceType"] = interface_type
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if exist_vpn_client is not UNSET:
            field_dict["existVpnClient"] = exist_vpn_client
        if exist_virtual_wan is not UNSET:
            field_dict["existVirtualWan"] = exist_virtual_wan
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        destinations = cast(list[str], d.pop("destinations"))

        route_type = d.pop("routeType")

        metric = d.pop("metric")

        id = d.pop("id", UNSET)

        next_hop_ip = d.pop("nextHopIp", UNSET)

        interface_type = d.pop("interfaceType", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        exist_vpn_client = d.pop("existVpnClient", UNSET)

        exist_virtual_wan = d.pop("existVirtualWan", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        static_routing_info = cls(
            name=name,
            status=status,
            destinations=destinations,
            route_type=route_type,
            metric=metric,
            id=id,
            next_hop_ip=next_hop_ip,
            interface_type=interface_type,
            interface_id=interface_id,
            exist_vpn_client=exist_vpn_client,
            exist_virtual_wan=exist_virtual_wan,
            feature_description=feature_description,
        )

        static_routing_info.additional_properties = d
        return static_routing_info

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
