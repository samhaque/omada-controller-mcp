from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.igmp_config_vo import IgmpConfigVO
    from ..models.mld_config_vo import MldConfigVO
    from ..models.network_vo import NetworkVO
    from ..models.router_port_vo import RouterPortVO
    from ..models.snoop_config_vo import SnoopConfigVO
    from ..models.unknown_multicast_config_vo import UnknownMulticastConfigVO


T = TypeVar("T", bound="LanMulticastVO")


@_attrs_define
class LanMulticastVO:
    """
    Attributes:
        id (str | Unset): The primary id of the multicast snooping.
        name (str | Unset): The name of the multicast snooping.
        networks (list[NetworkVO] | Unset): The collection of snooping network ids related to this multicast snooping
            config.
        protocol (int | Unset): When multicast snooping value 0,then represents the IGMP snooping type,else if value
            1,then represents MLD snooping type.
        unknown_multicast_rule (int | Unset): When it selects 0,then send forward, it selects 1,then discard info, it
            selects 2,then route port first.
        unknown_multicast_except_device (UnknownMulticastConfigVO | Unset): UnknownMulticastConfigVO.
        flood_known_enable (bool | Unset): Whether open flood known protocols.
        querier_enable (bool | Unset): Whether open querier.
        router_port_enable (bool | Unset): Whether open manual router port config.
        resource (int | Unset): resource
        router_ports (list[RouterPortVO] | Unset): The specific list of router ports info,including network, devices and
            the ports on them.
        snoop_config (SnoopConfigVO | Unset): The snoop config model.
        igmp_queriers (list[IgmpConfigVO] | Unset): The querier configs for IGMP snooping(ipv4).
        mld_queriers (list[MldConfigVO] | Unset): The querier configs for MLD snooping(ipv6).
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    networks: list[NetworkVO] | Unset = UNSET
    protocol: int | Unset = UNSET
    unknown_multicast_rule: int | Unset = UNSET
    unknown_multicast_except_device: UnknownMulticastConfigVO | Unset = UNSET
    flood_known_enable: bool | Unset = UNSET
    querier_enable: bool | Unset = UNSET
    router_port_enable: bool | Unset = UNSET
    resource: int | Unset = UNSET
    router_ports: list[RouterPortVO] | Unset = UNSET
    snoop_config: SnoopConfigVO | Unset = UNSET
    igmp_queriers: list[IgmpConfigVO] | Unset = UNSET
    mld_queriers: list[MldConfigVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        protocol = self.protocol

        unknown_multicast_rule = self.unknown_multicast_rule

        unknown_multicast_except_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_multicast_except_device, Unset):
            unknown_multicast_except_device = (
                self.unknown_multicast_except_device.to_dict()
            )

        flood_known_enable = self.flood_known_enable

        querier_enable = self.querier_enable

        router_port_enable = self.router_port_enable

        resource = self.resource

        router_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.router_ports, Unset):
            router_ports = []
            for router_ports_item_data in self.router_ports:
                router_ports_item = router_ports_item_data.to_dict()
                router_ports.append(router_ports_item)

        snoop_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snoop_config, Unset):
            snoop_config = self.snoop_config.to_dict()

        igmp_queriers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.igmp_queriers, Unset):
            igmp_queriers = []
            for igmp_queriers_item_data in self.igmp_queriers:
                igmp_queriers_item = igmp_queriers_item_data.to_dict()
                igmp_queriers.append(igmp_queriers_item)

        mld_queriers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mld_queriers, Unset):
            mld_queriers = []
            for mld_queriers_item_data in self.mld_queriers:
                mld_queriers_item = mld_queriers_item_data.to_dict()
                mld_queriers.append(mld_queriers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if networks is not UNSET:
            field_dict["networks"] = networks
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if unknown_multicast_rule is not UNSET:
            field_dict["unknownMulticastRule"] = unknown_multicast_rule
        if unknown_multicast_except_device is not UNSET:
            field_dict["unknownMulticastExceptDevice"] = unknown_multicast_except_device
        if flood_known_enable is not UNSET:
            field_dict["floodKnownEnable"] = flood_known_enable
        if querier_enable is not UNSET:
            field_dict["querierEnable"] = querier_enable
        if router_port_enable is not UNSET:
            field_dict["routerPortEnable"] = router_port_enable
        if resource is not UNSET:
            field_dict["resource"] = resource
        if router_ports is not UNSET:
            field_dict["routerPorts"] = router_ports
        if snoop_config is not UNSET:
            field_dict["snoopConfig"] = snoop_config
        if igmp_queriers is not UNSET:
            field_dict["igmpQueriers"] = igmp_queriers
        if mld_queriers is not UNSET:
            field_dict["mldQueriers"] = mld_queriers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.igmp_config_vo import IgmpConfigVO
        from ..models.mld_config_vo import MldConfigVO
        from ..models.network_vo import NetworkVO
        from ..models.router_port_vo import RouterPortVO
        from ..models.snoop_config_vo import SnoopConfigVO
        from ..models.unknown_multicast_config_vo import (
            UnknownMulticastConfigVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _networks = d.pop("networks", UNSET)
        networks: list[NetworkVO] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = NetworkVO.from_dict(networks_item_data)

                networks.append(networks_item)

        protocol = d.pop("protocol", UNSET)

        unknown_multicast_rule = d.pop("unknownMulticastRule", UNSET)

        _unknown_multicast_except_device = d.pop("unknownMulticastExceptDevice", UNSET)
        unknown_multicast_except_device: UnknownMulticastConfigVO | Unset
        if isinstance(_unknown_multicast_except_device, Unset):
            unknown_multicast_except_device = UNSET
        else:
            unknown_multicast_except_device = UnknownMulticastConfigVO.from_dict(
                _unknown_multicast_except_device
            )

        flood_known_enable = d.pop("floodKnownEnable", UNSET)

        querier_enable = d.pop("querierEnable", UNSET)

        router_port_enable = d.pop("routerPortEnable", UNSET)

        resource = d.pop("resource", UNSET)

        _router_ports = d.pop("routerPorts", UNSET)
        router_ports: list[RouterPortVO] | Unset = UNSET
        if _router_ports is not UNSET:
            router_ports = []
            for router_ports_item_data in _router_ports:
                router_ports_item = RouterPortVO.from_dict(router_ports_item_data)

                router_ports.append(router_ports_item)

        _snoop_config = d.pop("snoopConfig", UNSET)
        snoop_config: SnoopConfigVO | Unset
        if isinstance(_snoop_config, Unset):
            snoop_config = UNSET
        else:
            snoop_config = SnoopConfigVO.from_dict(_snoop_config)

        _igmp_queriers = d.pop("igmpQueriers", UNSET)
        igmp_queriers: list[IgmpConfigVO] | Unset = UNSET
        if _igmp_queriers is not UNSET:
            igmp_queriers = []
            for igmp_queriers_item_data in _igmp_queriers:
                igmp_queriers_item = IgmpConfigVO.from_dict(igmp_queriers_item_data)

                igmp_queriers.append(igmp_queriers_item)

        _mld_queriers = d.pop("mldQueriers", UNSET)
        mld_queriers: list[MldConfigVO] | Unset = UNSET
        if _mld_queriers is not UNSET:
            mld_queriers = []
            for mld_queriers_item_data in _mld_queriers:
                mld_queriers_item = MldConfigVO.from_dict(mld_queriers_item_data)

                mld_queriers.append(mld_queriers_item)

        lan_multicast_vo = cls(
            id=id,
            name=name,
            networks=networks,
            protocol=protocol,
            unknown_multicast_rule=unknown_multicast_rule,
            unknown_multicast_except_device=unknown_multicast_except_device,
            flood_known_enable=flood_known_enable,
            querier_enable=querier_enable,
            router_port_enable=router_port_enable,
            resource=resource,
            router_ports=router_ports,
            snoop_config=snoop_config,
            igmp_queriers=igmp_queriers,
            mld_queriers=mld_queriers,
        )

        lan_multicast_vo.additional_properties = d
        return lan_multicast_vo

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
